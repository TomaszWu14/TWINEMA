"""Wydania, paczki, zwroty, obsada i cut-off — liczby policzone ręcznie."""
from unittest import TestCase

from scenario.inbound import day_demand
from scenario.outbound import day_outbound
from scenario.staffing import cutoff_risk, process_hours, productive_h, staffing

NORMS = {"load_min_per_pallet": 1.5, "pick_lines_per_h": 60, "wrap_min_per_pallet": 2, "pack_min_per_parcel": 1.5,
         "pack_min_per_line": 0.3, "label_min_per_parcel": 0.3, "courier_dock_min": 30, "return_min": 6,
         "return_restock_pct": 70}
PROFILE = {"orders": (600, 800, 1000), "lines": (3, 5, 8), "parcels": (1500, 2200, 3000),
           "returns": (60, 90, 140), "full_pallet_pct": 40}
TRUCKS = {"kind": "truck33", "departures": (14, 18, 22), "pallets": (24, 28, 32), "window": (12, 20)}
COURIER = {"kind": "courier", "departures": (3, 4, 5), "pallets": (0, 0, 0), "window": (15, 18)}
XDOCK = {"kind": "crossdock", "departures": (2, 3, 4), "pallets": (20, 26, 32), "window": (10, 16)}
PACK = [{"process": "pack", "start_h": 6, "end_h": 14, "break_min": 30, "people": 10},
        {"process": "pack", "start_h": 14, "end_h": 22, "break_min": 30, "people": 6}]


class OutboundTests(TestCase):
    def test_trucks_profile_and_person_hours(self):
        d = day_outbound([TRUCKS], PROFILE, NORMS)
        # 18 aut × 28 palet = 504; 40 % pełnych → 302,4 kompletowanych
        self.assertEqual((d["pallets_out"], d["pallets_full"], d["pallets_picked"]), (504, 202, 302))
        # załadunek 28 × 1,5 min = 0,7 h/auto → 12,6 h + owijanie 302,4 × 2 min = 10,08 h
        self.assertEqual(d["person_hours"]["load"], 22.7)
        # odjazdy co 8/18 h, załadunek 0,7 h → 2 doki naraz
        self.assertEqual(d["docks_peak"], 2)
        # 800 zamówień × 5 linii = 4 000 / 60 = 66,7 h; 2 200 paczek × (1,5 + 5 × 0,3 + 0,3) min = 121 h
        self.assertEqual((d["lines"], d["person_hours"]["pick"], d["person_hours"]["pack"]), (4000, 66.7, 121.0))
        # 90 zwrotów × 6 min = 9 h; 70 % na skład = 63
        self.assertEqual((d["person_hours"]["returns"], d["returns_restock"]), (9.0, 63))
        self.assertIsNone(d["courier_cutoff"])

    def test_crossdock_not_wrapped_and_courier_cutoff(self):
        d = day_outbound([XDOCK, COURIER], PROFILE, NORMS)
        self.assertEqual((d["pallets_out"], d["pallets_xdock"], d["pallets_picked"]), (78, 78, 0))
        self.assertEqual(d["person_hours"]["load"], 2.0)       # 3 × 26 × 1,5 min = 1,95 h; kurier nie ładuje palet
        self.assertEqual(d["courier_cutoff"], 18)
        self.assertEqual([r["cutoff"] for r in d["rows"]], ["16:00", "18:00"])

    def test_growth_scales_volumes_and_rounds_vehicles_up(self):
        d = day_outbound([TRUCKS], PROFILE, NORMS, growth=1.3, level="max")
        self.assertEqual(d["rows"][0]["departures"], 29)                    # ⌈22 × 1,3⌉
        self.assertEqual((d["orders"], d["parcels"], d["returns"]), (1300, 3900, 182))

    def test_inbound_crossdock_pallets_counted_separately(self):
        norms = {"container_cartons_per_h": 500, "container_people": 2, "cartons_per_pallet": 40,
                 "truck_min_per_pallet": 1.5, "palletize_cartons_per_h": 360, "repack_min_per_pallet": 15}
        x = {"kind": "crossdock", "arrivals": (2, 3, 4), "pallets": (20, 26, 32), "window": (6, 12),
             "mono_pct": 100, "inspect_pct": 0, "inspect_min": 0}
        d = day_demand([x], norms)
        self.assertEqual((d["pallets_in"], d["pallets_xdock"], d["person_hours"]["repack"]), (78, 78, 0.0))


class StaffingTests(TestCase):
    def test_needed_vs_assumed_per_shift(self):
        rows = {p["process"]: p for p in staffing({"pack": 121.0}, PACK)}
        pack = rows["pack"]
        # 121 h wg zdolności zmian 10 × 7,5 : 6 × 7,5 → 75,6 h i 45,4 h; / 7,5 h → 10,08 → 11 i 6,05 → 7 osób
        self.assertEqual([s["needed"] for s in pack["shifts"]], [11, 7])
        self.assertEqual([s["gap"] for s in pack["shifts"]], [-1, -1])
        self.assertTrue(pack["short"])
        self.assertEqual((pack["needed"], pack["assumed"]), (18, 16))
        # wystarczająca obsada → bez fałszywego niedoboru na słabiej obsadzonej zmianie
        ok = {p["process"]: p for p in staffing({"pack": 120.0}, PACK)}["pack"]       # 75 h / 7,5 = 10; 45 / 7,5 = 6
        self.assertEqual(([s["gap"] for s in ok["shifts"]], ok["short"]), ([0, 0], False))
        self.assertFalse(rows["unload"]["short"])                           # brak pracy, brak zmian = OK

    def test_work_without_shift_is_short(self):
        rows = {p["process"]: p for p in staffing({"returns": 5.0}, [])}
        self.assertTrue(rows["returns"]["short"])

    def test_night_shift_crosses_midnight(self):
        self.assertEqual(productive_h({"start_h": 22, "end_h": 6, "break_min": 30}), 7.5)

    def test_cutoff_capacity(self):
        # do 18:00: 10 os. × 8 h × 7,5/8 + 6 os. × 4 h × 7,5/8 = 75 + 22,5 = 97,5 h < 121 h
        r = cutoff_risk(121.0, PACK, 18)
        self.assertEqual((r["capacity_h"], r["ok"], r["missing_h"]), (97.5, False, 23.5))
        self.assertTrue(cutoff_risk(90.0, PACK, 18)["ok"])
        self.assertIsNone(cutoff_risk(121.0, PACK, None))

    def test_process_hours_mapping(self):
        i = {"person_hours": {"unload": 10, "palletize": 20, "repack": 5, "inspect": 2}}
        o = {"person_hours": {"pick": 30, "pack": 40, "load": 8, "returns": 3}}
        self.assertEqual(process_hours(i, o), {"unload": 10, "palletize": 25, "inspect": 2, "pick": 30,
                                               "pack": 40, "load": 8, "returns": 3})
