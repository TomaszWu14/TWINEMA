"""S3b czysty Python: pojemność vs potrzeba, strefy specjalne, nośność, kartony z master daty, porównanie."""
from unittest import TestCase

from scenario.compare import compare_columns
from scenario.placement import check_placement, positions
from scenario.sim.engine import cartons_for


def rack(x=0, y=0, bays=10, levels=4, load=1000, equipment="reach", angle=0):
    # gniazdo 2,7 m → 3 palety; 10 gniazd × 3 × poziomy
    return {"zone": "V", "rack_id": f"{x}-{y}", "x": x, "y": y, "angle": angle, "n_bays": bays, "n_levels": levels,
            "bay_width_cm": 270, "depth_cm": 110, "level_height_cm": 180, "equipment": equipment, "load_kg": load}


def zone(kind, x, y, w, d):
    return {"kind": kind, "x": x, "y": y, "width": w, "depth": d, "angle": 0}


def stock(pallets, kg=500, **flags):
    return {"code": "x", "pallets": pallets, "kg": kg, "heavy": flags.pop("heavy", False), **flags}


def codes(res):
    return [i["code"] for i in res["issues"]]


class PlacementTests(TestCase):
    def test_positions_and_shelves(self):
        self.assertEqual(positions(rack()), 120)
        self.assertEqual(positions(rack(equipment="shelf")), 0)

    def test_capacity_ok_tight_over(self):
        racks = [rack(), rack(y=5)]                                  # 240 miejsc
        self.assertEqual(codes(check_placement(racks, [], [stock(100)])), [])
        tight = check_placement(racks, [], [stock(200)], growth=1.1)  # 220 → 91,7 %
        self.assertEqual(codes(tight), ["capacity_tight"])
        self.assertEqual(tight["capacity"]["need"], 220)
        over = check_placement(racks, [], [stock(300)])
        self.assertEqual((codes(over)[0], over["issues"][0]["severity"]), ("capacity_over", "error"))

    def test_special_zone_capacity_vs_need(self):
        racks = [rack(x=0, y=0), rack(x=0, y=10)]
        adr = zone("zone_adr", -1, -1, 30, 3)                        # obejmuje tylko pierwszy regał
        res = check_placement(racks, [adr], [stock(50), stock(150, adr=True)])
        z = next(z for z in res["capacity"]["zones"] if z["kind"] == "zone_adr")
        self.assertEqual((z["positions"], z["need"]), (120, 150))
        self.assertIn("zone_adr_short", codes(res))
        issue = next(i for i in res["issues"] if i["code"] == "zone_adr_short")
        self.assertEqual((issue["racks"], issue["features"]), ([0], [0]))
        missing = check_placement(racks, [], [stock(5, temp_controlled=True)])
        self.assertIn("zone_temp_missing", codes(missing))

    def test_zone_with_rotated_rack(self):
        r = rack(x=10, y=0, angle=90)            # obrócony o 90°: rząd biegnie w −y, środek ok. (10,55; −13,5)
        res = check_placement([r], [zone("zone_value", 5, -30, 10, 35)], [stock(10, high_value=True)])
        self.assertEqual(check_placement([r], [zone("zone_value", 5, 5, 10, 20)], [])["capacity"]["zones"][3]
                         ["positions"], 0)                                            # strefa obok — nie liczy
        self.assertEqual(res["capacity"]["zones"][3]["positions"], 120)
        self.assertNotIn("zone_value_short", codes(res))

    def test_load_and_heavy_low_levels(self):
        racks = [rack(load=800), rack(y=5, load=1500, levels=2)]     # 120 miejsc ≤ 800 kg, 60 miejsc 1500 kg
        res = check_placement(racks, [], [stock(70, kg=1000), stock(10, kg=300)])
        issue = next(i for i in res["issues"] if i["code"] == "load_over")
        self.assertIn("ponad 800 kg", issue["message"])
        self.assertEqual(issue["racks"], [0])
        ok = check_placement(racks, [], [stock(50, kg=1000)])
        self.assertNotIn("load_over", codes(ok))
        heavy = check_placement([rack(levels=6)], [], [stock(70, heavy=True)], heavy_max_level=2)
        self.assertEqual(heavy["capacity"]["heavy_low_positions"], 60)
        self.assertIn("heavy_high", codes(heavy))


class CartonsTests(TestCase):
    def test_deterministic_and_follows_weights(self):
        dist = [(20, 1), (60, 3)]
        picks = [cartons_for(f"in{i}-p{k}", dist, 40) for i in range(20) for k in range(20)]
        self.assertEqual(picks, [cartons_for(f"in{i}-p{k}", dist, 40) for i in range(20) for k in range(20)])
        self.assertAlmostEqual(picks.count(60) / len(picks), 0.75, delta=0.08)
        self.assertEqual(cartons_for("in1-p1", None, 40), 40)


class CompareTests(TestCase):
    def test_best_and_delta(self):
        a = {"agg": {"wait_out_p95_min": {"worst": 40}, "pallets_in": {"mean": 600}},
             "placement": {"capacity": {"positions": 1000}}, "bottlenecks": [{"severity": "error"}]}
        b = {"agg": {"wait_out_p95_min": {"worst": 20}, "pallets_in": {"mean": 600}},
             "placement": {"capacity": {"positions": 1200}}, "bottlenecks": []}
        rows = {r["label"]: r["cells"] for r in compare_columns([a, b])}
        wait = rows["Czekanie aut OUT (P95)"]
        self.assertEqual((wait[0]["best"], wait[1]["best"], wait[1]["delta"], wait[1]["good"]), (False, True, -50, True))
        cap = rows["Miejsca paletowe w layoucie"]
        self.assertTrue(cap[1]["best"])
        self.assertEqual(cap[1]["delta"], 20)
        self.assertFalse(any(c["best"] for c in rows["Palet przyjętych (średnio)"]))   # remis — bez wyróżnienia
        self.assertEqual([c["value"] for c in rows["w tym krytyczne"]], [1, 0])
        self.assertIsNone(rows["Doki wydań"][0]["value"])                              # brak danych → —
