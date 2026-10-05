"""Silnik edytora layoutu (czysty Python): walidacja wejścia, SAT, kolizje, alejki, wydajność."""
import time
from types import SimpleNamespace
from unittest import TestCase

from twin.blender_route import near_pairs, overlap_depth, rack_corners
from twin.design_generator import generate
from twin.layout import LayoutError, analyze, check_layout, clean_layout, feature_row, rack_row
from twin.model_edit import collisions

KINDS = {"dock", "gate", "staging", "station", "leader", "corridor", "block_zone", "returns", "other"}


def rack(zone="V", rid="001", x=5.0, y=5.0, angle=0.0, bays=4, **kw):
    return {"id": None, "zone": zone, "rack_id": rid, "x": x, "y": y, "angle": angle, "n_bays": bays,
            "n_levels": 4, "bay_width_cm": 270, "depth_cm": 110, "level_height_cm": 180, **kw}


def feat(kind="staging", x=30.0, y=5.0, w=6.0, d=4.0, label="Pole"):
    return {"id": None, "kind": kind, "label": label, "x": x, "y": y, "width": w, "depth": d, "angle": 0.0}


def layout(racks=(), feats=(), w=60.0, d=40.0):
    return {"floor": {"width": w, "depth": d}, "racks": list(racks), "features": list(feats), "version": ""}


def codes(issues):
    return sorted((i["code"], i["severity"]) for i in issues)


class GeometryTests(TestCase):
    def test_sat_rotated_rectangles_no_false_hit(self):
        # Dwa wąskie regały pod 45°, równoległe, 1 m odstępu: obrysy osiowe nachodzą, prostokąty — nie.
        a = {"x": 0, "y": 0, "angle": 45, "width": 10, "depth": 1}
        b = {"x": 1.5, "y": 1.5, "angle": 45, "width": 10, "depth": 1}
        ca, cb = rack_corners(a), rack_corners(b)
        self.assertLess(overlap_depth(ca, cb), 0)
        self.assertGreater(overlap_depth(ca, rack_corners({**b, "x": 0.3, "y": 0.3})), 0)

    def test_collisions_use_obb_not_aabb(self):
        r1 = {"zone": "V", "rack_id": "1", "x": 0, "y": 0, "angle": 45, "width": 10, "depth": 1}
        r2 = {"zone": "V", "rack_id": "2", "x": 1.5, "y": 1.5, "angle": 45, "width": 10, "depth": 1}
        self.assertEqual(collisions([r1, r2]), [])
        self.assertEqual(collisions([r1, {**r2, "x": 0.3, "y": 0.3}]), [("V-1", "V-2")])

    def test_near_pairs_matches_brute_force(self):
        boxes = [(i * 3.0, (i % 7) * 2.0, i * 3.0 + 2.5, (i % 7) * 2.0 + 1.0) for i in range(60)]
        brute = [(i, j) for i in range(60) for j in range(i + 1, 60)
                 if boxes[i][0] - 1 <= boxes[j][2] + 1 and boxes[j][0] - 1 <= boxes[i][2] + 1
                 and boxes[i][1] - 1 <= boxes[j][3] + 1 and boxes[j][1] - 1 <= boxes[i][3] + 1]
        self.assertEqual(near_pairs(boxes, pad=2.0), brute)


class CleanLayoutTests(TestCase):
    def test_valid_roundtrip_types(self):
        data = layout([rack(x=1, y=2, angle=-90, bays=3.0)], [feat()])
        out = clean_layout(data, KINDS)
        self.assertEqual(out["racks"][0]["angle"], 270.0)
        self.assertEqual(out["racks"][0]["n_bays"], 3)
        self.assertIsInstance(out["racks"][0]["x"], float)

    def test_rejects_bad_input(self):
        bad = [
            None, {"floor": {}, "racks": [], "features": []},
            layout([rack(x="1")]), layout([rack(x=float("nan"))]), layout([rack(bays=0)]),
            layout([rack(zone="")]), layout([rack(bays=True)]), layout([], [feat(kind="lava")]),
            layout([rack(id="5")]), layout([], [feat(w=0)]),
        ]
        for data in bad:
            with self.subTest(data=data), self.assertRaises(LayoutError):
                clean_layout(data, KINDS)

    def test_row_converters_roundtrip(self):
        r = SimpleNamespace(pk=7, zone="V", rack_id="001", x_m=None, y_m=3.5, angle_deg=None, n_bays=4,
                            n_levels=5, bay_width_cm=270, depth_cm=110, level_height_cm=180)
        f = SimpleNamespace(pk=3, kind="dock", label="Dok 1", x_m=0.0, y_m=1.0, width_m=4.0, depth_m=3.5,
                            angle_deg=0.0)
        row = rack_row(r)
        self.assertEqual((row["x"], row["angle"]), (0.0, 0.0))            # brak pozycji = 0 (jak model_racks)
        again = clean_layout(layout([row], [feature_row(f)]), KINDS)
        self.assertEqual(again["racks"][0], {**row, "x": 0.0, "y": 3.5, "angle": 0.0})
        self.assertEqual(again["features"][0]["kind"], "dock")


class CheckLayoutTests(TestCase):
    def test_clean_layout_has_no_issues(self):
        self.assertEqual(check_layout(layout([rack(), rack(rid="002", y=10)])), [])

    def test_collision_duplicate_outside(self):
        issues = check_layout(layout([rack(), rack(rid="002", x=6), rack(rid="001", y=20), rack(rid="003", x=55)]))
        self.assertEqual(codes(issues), [("collision", "error"), ("duplicate", "error"), ("outside", "error")])
        col = next(i for i in issues if i["code"] == "collision")
        self.assertEqual(col["racks"], [0, 1])

    def test_blocking_features_and_plain_areas(self):
        racks = [rack(x=30, y=5)]                               # stoi w polu odkładczym
        self.assertEqual(codes(check_layout(layout(racks, [feat("staging")]))), [("blocked", "error")])
        self.assertEqual(check_layout(layout(racks, [feat("block_zone")])), [])     # obszar = tylko oznaczenie
        docks = [feat("dock", 0, 0, 4, 3.5), feat("gate", 2, 0, 4, 3.5)]
        self.assertEqual(check_layout(layout([], docks)), [])                        # cecha–cecha: OK

    def test_feature_outside_is_warning(self):
        self.assertEqual(codes(check_layout(layout([], [feat("dock", -2, 5, 4, 3)]))), [("outside", "warning")])

    def test_back_to_back_is_not_collision_narrow_aisle_is_warning(self):
        pair = [rack(), rack(rid="002", y=6.1)]                 # plecami (1,1 m głębokości + 0 m)
        self.assertEqual(check_layout(layout(pair)), [])
        _, issues = analyze(layout([rack(), rack(rid="002", y=7.6)]))   # 1,5 m alejki < 3 m
        self.assertEqual(codes(issues), [("aisle", "warning")])
        self.assertEqual(issues[0]["racks"], [0, 1])

    def test_generated_hall_has_no_errors(self):
        g = generate()
        data = {"floor": g["floor"], "version": "",
                "racks": [{"zone": r["zone"], "rack_id": r["rack_id"], "x": r["x_m"], "y": r["y_m"],
                           "angle": r["angle_deg"], **{k: r[k] for k in ("n_bays", "n_levels", "bay_width_cm",
                                                                        "depth_cm", "level_height_cm")}}
                          for r in g["racks"]],
                "features": [{"kind": f["kind"], "label": f["label"], "x": f["x_m"], "y": f["y_m"],
                              "width": f["width_m"], "depth": f["depth_m"], "angle": f["angle_deg"]}
                             for f in g["features"]]}
        kpi, issues = analyze(clean_layout(data, KINDS))
        self.assertEqual([i for i in issues if i["severity"] == "error"], [])
        self.assertGreater(kpi["pallet_positions"], 0)

    def test_performance_1000_racks_100_features(self):
        racks = [rack(zone=f"Z{i // 50}", rid=f"{i % 50:03d}", x=2 + (i % 50) * 12.0, y=2 + (i // 50) * 5.0,
                      bays=4) for i in range(1000)]
        feats = [feat("staging", 2 + (k % 10) * 60.0, 105 + (k // 10) * 5.0, 4, 3) for k in range(100)]
        data = clean_layout(layout(racks, feats, w=620, d=160), KINDS)
        t0 = time.perf_counter()
        kpi, issues = analyze(data)
        took = time.perf_counter() - t0
        self.assertEqual([i for i in issues if i["severity"] == "error"], [])
        self.assertLess(took, 1.5, f"analiza 1000 regałów trwała {took:.2f} s")
