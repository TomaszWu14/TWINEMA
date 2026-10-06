"""Działka (D1): transformacja hala↔działka, reguły walidacji, KPI, działka domyślna generatora."""
import copy
import math
from unittest import TestCase

from twin.design_generator import generate
from twin.layout import LayoutError
from twin.site import (
    building_height, check_site, clean_site, default_site, entry_point, hall_to_site, site_kpi, site_to_hall,
)

FLOOR = {"width": 100.0, "depth": 60.0, "clear_height": 12.0}


def site(**kw):
    s = default_site(FLOOR)
    s.update(kw)
    return clean_site(s)


def dock(x, y, role="in_pallet", w=4.0, d=3.5):
    return {"kind": "dock", "label": "Dok", "x": x, "y": y, "width": w, "depth": d, "angle": 0, "dock_role": role}


def codes(issues):
    return {i["code"] for i in issues}


class TransformTests(TestCase):
    def test_round_trip_any_angle(self):
        s = site(hall={"x": 40.0, "y": 25.0, "angle": 33.0})
        for p in [(0, 0), (100, 0), (37.5, 12.25), (-5, 70)]:
            q = site_to_hall(s, hall_to_site(s, p))
            self.assertAlmostEqual(q[0], p[0])
            self.assertAlmostEqual(q[1], p[1])

    def test_corner_and_axes(self):
        s = site(hall={"x": 10.0, "y": 20.0, "angle": 90.0})
        self.assertEqual(hall_to_site(s, (0, 0)), (10.0, 20.0))
        x, y = hall_to_site(s, (5, 0))                      # u_w(90°) = (0, −1)
        self.assertAlmostEqual(x, 10.0)
        self.assertAlmostEqual(y, 15.0)

    def test_entry_point_sides(self):
        s = site()
        self.assertEqual(entry_point(s, {"side": "S", "pos": 7.0}), (7.0, s["depth"]))
        self.assertEqual(entry_point(s, {"side": "E", "pos": 3.0}, inset=1), (s["width"] - 1, 3.0))


class CleanTests(TestCase):
    def test_empty_means_no_site(self):
        self.assertEqual(clean_site(None), {})
        self.assertEqual(clean_site({}), {})

    def test_bad_values(self):
        base = default_site(FLOOR)
        for bad in ({**base, "access_side": "X"}, {**base, "width": -1},
                    {**base, "entries": [{"side": "S", "pos": 1e6, "kind": "truck"}]},
                    {**base, "areas": [{"kind": "lake", "x": 0, "y": 0, "width": 1, "depth": 1}]}):
            with self.subTest(bad=list(bad)), self.assertRaises(LayoutError):
                clean_site(bad)


class RuleTests(TestCase):
    def test_default_site_is_clean(self):
        s = site()
        feats = [dock(0, 20, "in_container"), dock(96, 20, "out"), dock(96, 40, "courier")]
        self.assertEqual(check_site(s, FLOOR, [], feats), [])
        k = site_kpi(s, FLOOR)
        self.assertLessEqual(k["coverage_pct"], 55)
        self.assertGreaterEqual(k["bio_pct"], 20)
        self.assertGreater(k["reserve_m2"], 0)

    def test_hall_outside_building_line(self):
        s = site()
        s["hall"]["y"] = 2.0                                # pas zieleni od północy, granica 6 m
        self.assertIn("building_line", codes(check_site(s, FLOOR, [], [])))

    def test_coverage_height_bio(self):
        self.assertIn("coverage", codes(check_site(site(max_coverage_pct=10.0), FLOOR, [], [])))
        self.assertIn("site_height", codes(check_site(site(max_height=10.0), FLOOR, [], [])))
        s = site()
        s["areas"] = [a for a in s["areas"] if a["kind"] != "green"]
        issue = next(i for i in check_site(s, FLOOR, [], []) if i["code"] == "bio")
        self.assertEqual(issue["severity"], "error")

    def test_building_height_from_racks_without_clear_height(self):
        racks = [{"n_levels": 5, "level_height_cm": 200}]
        self.assertEqual(building_height({"width": 1, "depth": 1}, racks), 11.5)   # 10 + 0,5 zapasu + 1 dach

    def test_entry_on_wrong_side(self):
        s = site()
        s["entries"][0]["side"] = "N"
        s["entries"][0]["pos"] = 5.0
        self.assertIn("entry_side", codes(check_site(s, FLOOR, [], [])))

    def test_dock_without_yard(self):
        s = site()
        s["hall"]["x"] = 10.0                               # plac zachodni zostaje, hala dosunięta pod granicę W
        s["setback"]["other"] = 0.0
        issues = check_site(s, FLOOR, [], [dock(0, 20, "in_container")])
        self.assertIn("dock_yard", codes(issues))
        self.assertEqual(next(i for i in issues if i["code"] == "dock_yard")["features"], [0])

    def test_route_through_green(self):
        s = site()
        e = s["entries"][0]
        s["areas"].append({"kind": "green", "label": "Skwer", "x": e["pos"] - 8, "y": s["depth"] - 20, "width": 16,
                           "depth": 19, "angle": 0})
        self.assertIn("route", codes(check_site(s, FLOOR, [], [dock(0, 20, "in_container")])))

    def test_area_under_hall_warns(self):
        s = site()
        h = s["hall"]
        s["areas"].append({"kind": "parking", "label": "", "x": h["x"] + 10, "y": h["y"] + 10, "width": 10, "depth": 10,
                           "angle": 0})
        self.assertIn("area_hall", codes(check_site(s, FLOOR, [], [])))

    def test_no_site_no_issues(self):
        self.assertEqual(check_site({}, FLOOR, [], []), [])


class GeneratorSiteTests(TestCase):
    def test_generated_hall_fits_its_site(self):
        g = generate()
        floor = {**g["floor"], "clear_height": g["params"]["clear_height_m"]}
        feats = [{"kind": f["kind"], "label": f["label"], "x": f["x_m"], "y": f["y_m"], "width": f["width_m"],
                  "depth": f["depth_m"], "angle": 0, "dock_role": f.get("dock_role", "")} for f in g["features"]]
        racks = [{"n_levels": r["n_levels"], "level_height_cm": r["level_height_cm"]} for r in g["racks"]]
        s = clean_site(copy.deepcopy(g["site"]))
        self.assertEqual(check_site(s, floor, racks, feats), [])
        self.assertTrue(math.isclose(s["hall"]["x"], 45.0))


class PolygonPlotTests(TestCase):
    """D2: granica-wielokąt — pole, linie zabudowy per krawędź, wcięcie, wjazd dosunięty do granicy."""
    # „L”: 200 × 160 bez prawego górnego narożnika 80 × 60 (dojazd od południa = dolna krawędź planu)
    L = [[0, 0], [120, 0], [120, 60], [200, 60], [200, 160], [0, 160]]

    def plot(self, hall=(20.0, 80.0), **kw):
        base = {"boundary": self.L, "hall": {"x": hall[0], "y": hall[1], "angle": 0}, "max_height": None,
                "max_coverage_pct": None, "min_bio_pct": None, "setback": {"road": 12, "other": 6},
                "access_side": "S", "entries": [{"kind": "truck", "side": "S", "pos": 100, "width": 10}], "areas": []}
        base.update(kw)
        return clean_site(base)

    def test_bbox_and_area(self):
        from twin.site import polygon_area
        s = self.plot()
        self.assertEqual((s["width"], s["depth"]), (200, 160))
        self.assertEqual(site_kpi(s, FLOOR)["plot_m2"], 200 * 160 - 80 * 60)
        self.assertEqual(abs(polygon_area([(0, 0), (0, 10), (10, 10), (10, 0)])), 100)   # kolejność bez znaczenia

    def test_road_edge_gets_road_setback(self):
        from twin.site import edge_setbacks
        sbs = edge_setbacks(self.plot())
        self.assertEqual(sbs[4], 12)                      # (200,160)→(0,160): dolna krawędź = od drogi
        self.assertEqual(set(sbs[:4] + sbs[5:]), {6})

    def test_building_line_inside_notch_and_road(self):
        ok = self.plot(hall=(20.0, 80.0))                  # hala 100 × 60 w dolnej części „L”
        self.assertNotIn("building_line", codes(check_site(ok, FLOOR, [], [])))
        notch = self.plot(hall=(90.0, 10.0))               # wchodzi we wcięcie (x > 120, y < 60)
        self.assertIn("building_line", codes(check_site(notch, FLOOR, [], [])))
        # wklęsły wierzchołek granicy 3 m od boku hali (narożniki hali daleko od krawędzi) — też naruszenie
        dent = self.plot(hall=(20.0, 80.0), boundary=[[0, 0], [120, 0], [120, 60], [200, 60], [200, 160], [0, 160],
                                                      [0, 120], [17, 110], [0, 100]])
        self.assertIn("building_line", codes(check_site(dent, FLOOR, [], [])))
        road = self.plot(hall=(20.0, 92.0))                # 8 m od dolnej granicy < 12 m od drogi
        self.assertIn("building_line", codes(check_site(road, FLOOR, [], [])))

    def test_entry_snaps_to_boundary_and_insets_inward(self):
        s = self.plot(entries=[{"kind": "truck", "side": "N", "pos": 160, "width": 10}])
        self.assertEqual(entry_point(s, s["entries"][0]), (160.0, 60.0))    # bok N obrysu → krawędź wcięcia
        self.assertEqual(entry_point(s, s["entries"][0], inset=2), (160.0, 62.0))

    def test_reserve_uses_polygon_buildable_area(self):
        k = site_kpi(self.plot(), FLOOR)
        self.assertGreater(k["reserve_m2"], 0)
        self.assertLess(k["reserve_m2"], 200 * 160 - 80 * 60)

    def test_rect_without_boundary_unchanged(self):
        s = site()
        self.assertNotIn("boundary", s)
        self.assertEqual(site_kpi(s, FLOOR)["plot_m2"], round(s["width"] * s["depth"]))

    def test_bad_boundary_rejected(self):
        for bad in ([[0, 0], [10, 0]], [[0, 0], [10, 0], [20, 0]], [[0, 0], [10, 0], ["x", 5]]):
            with self.assertRaises(LayoutError):
                self.plot(boundary=bad)
