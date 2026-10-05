"""E2b — konstrukcja hali w silniku layoutu: słupy, wysokość w świetle, drogi pożarowe i ruchu, ładowanie,
strefy specjalne, alejka zależna od sprzętu (VNA/półki), wydajność z siatką słupów."""
import time
from unittest import TestCase

from twin.design_generator import generate
from twin.layout import (BLOCKING_KINDS, ROOF_GAP_M, SPECIAL_ZONE_KINDS, TRAFFIC_KINDS, LayoutError, analyze,
                         check_layout, clean_layout, column_list)
from twin.models import WarehouseHallFeature

from .test_layout import KINDS as BASE_KINDS, codes, feat, layout, rack

KINDS = set(dict(WarehouseHallFeature.KIND_CHOICES))


def grid(px=12, py=24, ox=0, oy=0, size=0.6, **kw):
    return {"pitch_x": px, "pitch_y": py, "offset_x": ox, "offset_y": oy, "size": size, **kw}


class ColumnTests(TestCase):
    def test_grid_with_removed_and_extra(self):
        cols = column_list(grid(removed=[[0, 0]], extra=[[7.5, 3.0]]), {"width": 24, "depth": 24})
        self.assertEqual(len(cols), 3 * 2 - 1 + 1)
        self.assertNotIn([0, 0], [c["ref"] for c in cols])
        self.assertEqual(cols[-1], {"x": 7.5, "y": 3.0, "size": 0.6, "ref": ["e", 0]})
        self.assertEqual(column_list({}, {"width": 24, "depth": 24}), [])

    def test_rack_on_column_is_error_dock_too_but_staging_not(self):
        cols = grid(px=10, py=10, ox=10, oy=10)                         # słup w (10; 10)
        on = layout([rack(x=8, y=9.6)])                                  # regał 10,8 m × 1,1 m przez (10; 10)
        on["columns"] = cols
        self.assertEqual(codes(check_layout(on)), [("column", "error")])
        clear = layout([rack(x=8, y=12)])
        clear["columns"] = cols
        self.assertEqual(check_layout(clear), [])
        dock = layout([], [feat("dock", 8, 8, 4, 3.5)])
        dock["columns"] = cols
        self.assertEqual(codes(check_layout(dock)), [("column", "error")])
        field = layout([], [feat("staging", 8, 8, 6, 6)])               # słup w polu odkładczym — normalne
        field["columns"] = cols
        self.assertEqual(check_layout(field), [])

    def test_clean_columns_validation(self):
        for bad in ({"pitch_x": 1}, {"pitch_x": 12, "removed": [[1]]}, {"size": 9}, "x"):
            with self.subTest(bad=bad), self.assertRaises(LayoutError):
                clean_layout({**layout(), "columns": bad}, KINDS)
        out = clean_layout({**layout(), "columns": grid(removed=[[1, 0], [1, 0]])}, KINDS)
        self.assertEqual(out["columns"]["removed"], [[1, 0]])

    def test_too_dense_grid_rejected(self):
        with self.assertRaises(LayoutError):
            column_list(grid(px=2, py=2), {"width": 5000, "depth": 5000})


class HeightTests(TestCase):
    def test_rack_above_usable_height_is_error_and_kpi_shows_max_levels(self):
        data = layout([rack(n_levels=5, level_height_cm=200)])           # 10 m
        data["floor"]["clear_height"] = 10.4                             # użytkowa 9,9 m
        self.assertEqual(codes(check_layout(data)), [("height", "error")])
        data["floor"]["clear_height"] = 10.5
        kpi, issues = analyze(data)
        self.assertEqual(issues, [])
        self.assertEqual(kpi["height"], {"clear_m": 10.5, "usable_m": 10.5 - ROOF_GAP_M,
                                         "zones": {"V": {"levels": 5, "max_levels": 5}}})
        data["floor"]["clear_height"] = None
        self.assertIsNone(analyze(data)[0]["height"])

    def test_clean_height(self):
        self.assertEqual(clean_layout({**layout(), "floor": {"width": 9, "depth": 9, "clear_height": 12}}, KINDS)
                         ["floor"]["clear_height"], 12.0)
        with self.assertRaises(LayoutError):
            clean_layout({**layout(), "floor": {"width": 9, "depth": 9, "clear_height": 1}}, KINDS)


class FeatureKindTests(TestCase):
    def test_kinds_exist_in_model(self):
        self.assertTrue(BLOCKING_KINDS | TRAFFIC_KINDS | SPECIAL_ZONE_KINDS <= KINDS)
        self.assertTrue(BASE_KINDS <= KINDS)

    def test_fire_route_and_charging_block_traffic_warns_special_zone_allows(self):
        r = [rack(x=30, y=5)]
        for kind in ("fire_route", "charging"):
            self.assertEqual(codes(check_layout(layout(r, [feat(kind)]))), [("blocked", "error")], kind)
        for kind in ("walkway", "truckway"):
            issues = check_layout(layout(r, [feat(kind)]))
            self.assertEqual(codes(issues), [("traffic", "warning")], kind)
            self.assertEqual((issues[0]["racks"], issues[0]["features"]), ([0], [0]))
        for kind in SPECIAL_ZONE_KINDS:
            self.assertEqual(check_layout(layout(r, [feat(kind)])), [], kind)


class EquipmentAisleTests(TestCase):
    def test_aisle_requirement_follows_equipment(self):
        pair = [rack(), rack(rid="002", y=7.9)]                          # 1,8 m alejki
        self.assertEqual(codes(analyze(layout(pair))[1]), [("aisle", "warning")])          # reach: 3,0 m
        vna = [{**r, "equipment": "vna"} for r in pair]
        self.assertEqual(analyze(layout(vna))[1], [])
        shelf = [rack(), rack(rid="002", y=8.1)]                         # 2,0 m
        self.assertEqual(analyze(layout([{**r, "equipment": "shelf"} for r in shelf]))[1], [])
        with self.assertRaises(LayoutError):
            clean_layout(layout([rack(equipment="dron")]), KINDS)

    def test_generated_hall_has_no_false_aisle_warnings_and_fits_height(self):
        g = generate()
        data = {"floor": {**g["floor"], "clear_height": g["params"]["clear_height_m"]}, "version": "",
                "racks": [{"zone": r["zone"], "rack_id": r["rack_id"], "x": r["x_m"], "y": r["y_m"],
                           "angle": r["angle_deg"], **{k: r[k] for k in ("n_bays", "n_levels", "bay_width_cm",
                                                                        "depth_cm", "level_height_cm", "equipment")}}
                          for r in g["racks"]],
                "features": [{"kind": f["kind"], "label": f["label"], "x": f["x_m"], "y": f["y_m"],
                              "width": f["width_m"], "depth": f["depth_m"], "angle": f["angle_deg"]}
                             for f in g["features"]]}
        _, issues = analyze(clean_layout(data, KINDS))
        self.assertEqual(issues, [])


class PerformanceTests(TestCase):
    def test_hall_120x80_with_column_grid(self):
        racks = [rack(zone=f"Z{i // 50}", rid=f"{i % 50:03d}", x=2 + (i % 10) * 11.5, y=2 + (i // 10) * 0.75,
                      bays=4, depth_cm=60) for i in range(100)]
        data = clean_layout({**layout(racks, [feat("staging", 2, 78, 4, 1)], w=120, d=80),
                             "columns": grid(px=12, py=24, ox=6, oy=12)}, KINDS)
        racks = [rack(zone=f"Z{i // 50}", rid=f"{i % 50:03d}", x=2 + (i % 50) * 12.0, y=2 + (i // 50) * 5.0,
                      bays=4) for i in range(1000)]
        big = clean_layout({**layout(racks, [], w=620, d=160), "columns": grid(px=12, py=24, ox=6, oy=12)}, KINDS)
        t0 = time.perf_counter()
        analyze(data)
        analyze(big)
        took = time.perf_counter() - t0
        self.assertLess(took, 1.5, f"analiza z siatką słupów trwała {took:.2f} s")
