"""Symulacja dnia (S3a) — czysty Python: plan, kolejki doków, pole odkładcze, cut-off, P95, reguły."""
from unittest import TestCase

from scenario.sim import FLEET_DEFAULTS, run_day, run_many
from scenario.sim.engine import simulate_plan
from scenario.sim.places import dock_role, needed_roles, places_from_features, with_extra_docks
from scenario.sim.plan import build_plan, times_in_window
from scenario.sim.report import aggregate, bottlenecks, run_report

NORMS = dict(container_cartons_per_h=500, container_people=2, cartons_per_pallet=40, truck_min_per_pallet=1.5,
             palletize_cartons_per_h=360, repack_min_per_pallet=15, load_min_per_pallet=1.5, pick_lines_per_h=60,
             wrap_min_per_pallet=2, pack_min_per_parcel=1.5, pack_min_per_line=0.3, label_min_per_parcel=0.3,
             courier_dock_min=30, return_min=6, return_restock_pct=70, growth=1.0, **FLEET_DEFAULTS)
ONE_DOCK = places_from_features([{"id": 1, "kind": "dock", "label": "Dok wspólny", "width": 3, "depth": 4},
                                 {"id": 2, "kind": "staging", "label": "Pole przyjęć", "width": 10, "depth": 10}])


def shifts(**people):
    return [{"process": p, "start_h": 0, "end_h": 24, "break_min": 0, "people": n} for p, n in people.items()]


def truck(i, arrive, pallets, kind="truck33", mono=100):
    return {"id": f"in{i}", "kind": kind, "arrive": arrive, "pallets": pallets, "mono_pct": mono,
            "inspect_pct": 0, "inspect_min": 0}


def plan(vin=(), vout=(), orders=(), returns=()):
    return {"in": list(vin), "out": list(vout), "orders": list(orders), "returns": list(returns), "xdock_spare": []}


DAY = {"inbound": [{"kind": "truck33", "arrivals": (4, 6, 8), "pallets": (17, 26, 32), "window": (8, 16),
                    "mono_pct": 75, "inspect_pct": 20, "inspect_min": 2}],
       "outbound": [{"kind": "truck33", "departures": (4, 5, 6), "pallets": (20, 26, 30), "window": (12, 20)},
                    {"kind": "courier", "departures": (2, 2, 2), "pallets": (0, 0, 0), "window": (15, 18)}],
       "profile": {"orders": (100, 150, 200), "lines": (2, 4, 6), "parcels": (200, 300, 400),
                   "returns": (10, 20, 30), "full_pallet_pct": 50}}
STAFF = shifts(unload=3, palletize=3, inspect=1, pick=4, pack=4, load=3, returns=1)


class PlanTests(TestCase):
    def test_times_spread_in_window_and_sorted(self):
        import random
        ts = times_in_window(random.Random(1), 8, (6, 14))
        self.assertEqual(len(ts), 8)
        self.assertEqual(ts, sorted(ts))
        self.assertTrue(all(6 <= t <= 14 for t in ts))
        self.assertLess(ts[0], 7.0)                     # pierwsze auto w pierwszym odcinku okna
        self.assertGreater(ts[-1], 13.0)

    def test_same_seed_same_day_other_seed_differs(self):
        a, b, c = (build_plan(DAY, NORMS, s) for s in (7, 7, 8))
        self.assertEqual(a, b)
        self.assertNotEqual(a, c)
        self.assertTrue(all(4 <= sum(v["kind"] == "truck33" for v in p["in"]) <= 8 for p in (a, c)))

    def test_orders_go_to_courier_arriving_at_least_hour_later(self):
        p = build_plan(DAY, NORMS, 3)
        couriers = {v["id"]: v for v in p["out"] if v["kind"] == "courier"}
        for o in p["orders"]:
            c = couriers[o["courier"]]
            self.assertTrue(c["arrive"] >= o["release"] + 1.0 or c is max(couriers.values(), key=lambda v: v["arrive"]))


class EngineTests(TestCase):
    def test_dock_queue_small_example(self):
        # dwa auta po 20 palet o 8:00, jeden dok, 1,5 min/paleta → 30 min każde; drugie czeka 30 min
        rec = simulate_plan(plan([truck(1, 8.0, 20), truck(2, 8.0, 20)]), {**NORMS, "fleet_units": 5},
                            shifts(unload=2), ONE_DOCK)
        t = sorted(rec["trucks"], key=lambda r: r["start"])
        self.assertEqual([(r["start"], r["end"]) for r in t], [(8.0, 8.5), (8.5, 9.0)])
        kpi = run_report(rec)["kpi"]
        self.assertEqual(kpi["queue_in_pallet_max"], 1)
        self.assertAlmostEqual(kpi["wait_in_pallet_p95_min"], 30.0)

    def test_staging_max_when_fleet_is_slow(self):
        # 4 palety co 1,5 min, 1 wózek, ruch 60 min: pierwsza od razu na regał, trzy czekają na polu
        rec = simulate_plan(plan([truck(1, 8.0, 4)]), {**NORMS, "fleet_units": 1, "fleet_min_per_move": 60},
                            shifts(unload=1), ONE_DOCK)
        self.assertEqual(run_report(rec)["kpi"]["staging_in_max"], 3)

    def test_parcels_after_courier_pickup_are_late(self):
        courier = {"id": "out1", "kind": "courier", "arrive": 15.0, "cutoff": 15.5, "pallets": 0}
        orders = [{"id": "o1", "release": 14.0, "lines": 1, "parcels": 40, "courier": "out1"},
                  {"id": "o2", "release": 9.0, "lines": 1, "parcels": 5, "courier": "out1"}]
        # o2 spakowane rano; o1: kompletacja 1 min, pakowanie 40 × 1,8 + 0,3 = 72,3 min → 15:13 > odbiór 15:00
        rec = simulate_plan(plan(vout=[courier], orders=orders), NORMS,
                            shifts(pick=1) + [{"process": "pack", "start_h": 9, "end_h": 22, "break_min": 0,
                                               "people": 1}], ONE_DOCK)
        kpi = run_report(rec)["kpi"]
        self.assertEqual((kpi["parcels"], kpi["parcels_late"]), (45, 40))
        self.assertEqual(kpi["late_cut_h"], 15.0)

    def test_task_after_last_shift_is_unfinished(self):
        rec = simulate_plan(plan([truck(1, 20.0, 5)]), NORMS,
                            [{"process": "unload", "start_h": 6, "end_h": 14, "break_min": 30, "people": 2}], ONE_DOCK)
        kpi = run_report(rec)["kpi"]
        self.assertEqual(kpi["unfinished_by"], {"unload": 1})
        self.assertEqual(kpi["unfinished_last"], {"unload": 20.0})

    def test_break_stretches_task(self):
        # zmiana 8 h z 60 min przerwy → praca 1 h trwa 8/7 h
        rec = simulate_plan(plan([truck(1, 6.0, 40)]), NORMS,
                            [{"process": "unload", "start_h": 6, "end_h": 14, "break_min": 60, "people": 1}], ONE_DOCK)
        self.assertAlmostEqual(rec["trucks"][0]["end"], 6.0 + 1.0 * 8 / 7)


class ManyRunsTests(TestCase):
    def test_reproducible_and_worst_case_is_p95(self):
        a = run_many(DAY, NORMS, STAFF, ONE_DOCK, 5, runs=6)
        b = run_many(DAY, NORMS, STAFF, ONE_DOCK, 5, runs=6)
        self.assertEqual(a["agg"], b["agg"])
        self.assertEqual(a["events"], b["events"])
        w = a["agg"]["wait_out_p95_min"]
        self.assertGreaterEqual(w["worst"], w["mean"] - 1e-9)
        self.assertLessEqual(a["agg"]["pallets_in"]["worst"], a["agg"]["pallets_in"]["mean"] + 1e-9)  # P5

    def test_events_format(self):
        r = run_day(DAY, NORMS, STAFF, ONE_DOCK, 11)
        ev = r["events"]
        self.assertEqual(ev, sorted(ev))
        kinds = {e[2] for e in ev}
        self.assertTrue({"truck", "pallet", "parcel", "courier"} <= kinds)
        self.assertTrue(any(e[4] == "dock:1" for e in ev))
        self.assertTrue(all(isinstance(e[0], int) for e in ev))


class PlacesTests(TestCase):
    def test_dock_roles_from_labels(self):
        self.assertEqual([dock_role({"label": x}) for x in (
            "Dok kontenerowy (przenośnik)", "Dok paczek → kontener", "Dok paletowy", "Dok FTL", "Brama busów",
            "Dok wspólny 3")], ["in_container", "courier", "in_pallet", "out", "out", "shared"])

    def test_explicit_role_beats_label_and_warns_only_needed(self):
        f = {"id": 7, "kind": "dock", "label": "Dok FTL 1", "dock_role": "in_container", "width": 3, "depth": 4}
        self.assertEqual(dock_role(f), "in_container")
        day = {"inbound": [{"kind": "container40"}], "outbound": []}
        pl = places_from_features([f], needed_roles(day))
        self.assertEqual(pl["roles"]["in_container"], [7])
        self.assertEqual(pl["warnings"], [])                       # wydań/kuriera scenariusz nie potrzebuje
        pl = places_from_features([{**f, "dock_role": "out"}], needed_roles(day))
        self.assertIn("kontenerowego", pl["warnings"][0])

    def test_fallback_and_staging_split(self):
        pl = places_from_features([{"id": 5, "kind": "dock", "label": "Dok FTL", "width": 3, "depth": 4},
                                   {"id": 6, "kind": "staging", "label": "", "width": 10, "depth": 4}])
        self.assertEqual(pl["roles"]["in_container"], [5])
        self.assertTrue(pl["warnings"])
        self.assertEqual(pl["staging_m2"], {"in": 20.0, "out": 20.0})
        self.assertEqual(with_extra_docks(pl, "in_pallet", 2)["counts"]["in_pallet"], 3)


def _rep(**kpi):
    base = {"unfinished_by": {}, "unfinished_last": {}, "late_cut_h": None}
    tl = {k: [0] * 104 for k in ("queue_in_container", "queue_in_pallet", "queue_out", "docks_in_container",
                                  "docks_in_pallet", "docks_out", "staging_in", "staging_out", "fleet_busy")}
    tl["fleet_units"] = 2
    return {"kpi": {**base, **kpi}, "timeline": tl}


class BottleneckTests(TestCase):
    def _agg(self, **over):
        rep = run_day(DAY, NORMS, STAFF, ONE_DOCK, 1)
        kpi = {**rep["kpi"], **over}
        return aggregate([kpi]), kpi

    def test_dock_rule_uses_rerun_for_count(self):
        agg, kpi = self._agg(wait_in_pallet_p95_min=90, queue_in_pallet_max=3)
        rep = _rep(**kpi)
        rep["timeline"]["docks_in_pallet"][40] = 1                 # jedyny dok pełny → brakuje doków
        calls = []

        def rerun(kind, *a):
            calls.append((kind, *a))
            return {**kpi, "wait_in_pallet_p95_min": 10 if kind == "docks" and a[1] >= 2 else 90}
        out = bottlenecks(agg, rep, ONE_DOCK, STAFF, rerun)
        b = next(x for x in out if x["area"].startswith("Doki paletowe"))
        self.assertIn("+2 doki", b["suggestion"])
        self.assertEqual(b["severity"], "error")
        self.assertIn(("docks", "in_pallet", 2), calls)

    def test_staging_rule_compares_with_drawn_area(self):
        agg, kpi = self._agg(staging_in_max=200)
        out = bottlenecks(agg, _rep(**kpi), ONE_DOCK, STAFF, lambda *a: kpi)
        b = next(x for x in out if x["area"] == "Pole odkładcze przyjęć")
        self.assertIn("+200 m²", b["suggestion"])                    # 200 × 1,5 − 100 narysowane

    def test_lost_after_shift_suggests_extra_shift_not_people(self):
        agg, kpi = self._agg(unfinished=5)
        kpi.update(unfinished_by={"returns": 5}, unfinished_last={"returns": 15.6})
        sh = [s for s in STAFF if s["process"] != "returns"] + [
            {"process": "returns", "start_h": 6, "end_h": 14, "break_min": 30, "people": 1}]
        out = bottlenecks(agg, _rep(**kpi), ONE_DOCK, sh, lambda *a: kpi)
        b = next(x for x in out if x["area"] == "Zwroty")
        self.assertIn("Dodaj zmianę od 14:00", b["suggestion"])

    def test_quiet_day_has_no_bottlenecks(self):
        quiet = {**DAY, "inbound": [{**DAY["inbound"][0], "arrivals": (1, 1, 1)}]}
        r = run_many(quiet, {**NORMS, "fleet_units": 10}, shifts(unload=4, palletize=4, inspect=2, pick=6, pack=6,
                                                                load=4, returns=2),
                     places_from_features([{"id": i, "kind": "dock", "label": "Dok wspólny", "width": 3, "depth": 4}
                                           for i in range(1, 6)]
                                          + [{"id": 9, "kind": "staging", "label": "", "width": 40, "depth": 30}]),
                     3, runs=4)
        self.assertEqual(r["bottlenecks"], [])
