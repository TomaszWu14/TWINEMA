"""Plan przyjęć — liczby policzone ręcznie."""
from unittest import TestCase

from scenario.inbound import arrivals_count, day_demand, peak_concurrency, starts

NORMS = {"container_cartons_per_h": 500, "container_people": 2, "cartons_per_pallet": 40,
         "truck_min_per_pallet": 1.5, "palletize_cartons_per_h": 360, "repack_min_per_pallet": 15}
CONTAINERS = {"kind": "container40", "arrivals": (7, 8, 9), "pallets": (38, 45, 52), "window": (6, 14),
              "mono_pct": 100, "inspect_pct": 0, "inspect_min": 0}
TRUCKS = {"kind": "truck33", "arrivals": (6, 8, 10), "pallets": (17, 26, 32), "window": (8, 18),
          "mono_pct": 75, "inspect_pct": 20, "inspect_min": 3}


class HelpersTests(TestCase):
    def test_starts_evenly_in_window(self):
        self.assertEqual(starts(4, (6, 14)), [7.0, 9.0, 11.0, 13.0])

    def test_peak_concurrency_end_before_start(self):
        self.assertEqual(peak_concurrency([(1, 3), (3, 5)])[0], 1)          # styk = nie naraz
        self.assertEqual(peak_concurrency([(1, 4), (2, 5), (3, 6), (4.5, 7)]), (3, 3))
        self.assertEqual(peak_concurrency([]), (0, None))

    def test_arrivals_rounded_up_after_growth(self):
        self.assertEqual(arrivals_count(8, 1.0), 8)
        self.assertEqual(arrivals_count(8, 1.3), 11)       # 10,4 → 11 aut, nie 10,4
        self.assertEqual(arrivals_count(0, 1.3), 0)


class DayDemandTests(TestCase):
    def test_eight_containers_by_45_pallets(self):
        d = day_demand([CONTAINERS], NORMS)
        # 8 × 45 = 360 palet; 360 × 40 = 14 400 kartonów; rozładunek 1 800 / (500 × 2) = 1,8 h
        self.assertEqual((d["pallets_in"], d["cartons_in"]), (360, 14400))
        self.assertEqual(d["rows"][0]["unload_min"], 108)
        # przyjazdy co 1 h (6:30, 7:30, …) po 1,8 h → naraz 2 doki kontenerowe
        self.assertEqual(d["docks_peak"], {"container": 2, "pallet": 0})
        self.assertEqual(d["docks_peak_at"]["container"], "07:30")
        # osobogodziny: rozładunek 14 400 / 500 = 28,8; paletyzacja 14 400 / 360 = 40 → 5 stanowisk na 8 h
        self.assertEqual(d["person_hours"]["unload"], 28.8)
        self.assertEqual(d["person_hours"]["palletize"], 40.0)
        self.assertEqual(d["palletize_stations"], 5)

    def test_trucks_repack_and_inspection(self):
        d = day_demand([TRUCKS], NORMS)
        # 8 aut × 26 palet = 208; rozładunek 26 × 1,5 min = 39 min/auto → 8 × 0,65 h = 5,2 h
        self.assertEqual(d["pallets_in"], 208)
        self.assertEqual(d["person_hours"]["unload"], 5.2)
        # przepakowanie 25 % × 208 × 15 min = 13 h; kontrola 20 % × 208 × 3 min = 2,08 h
        self.assertEqual(d["person_hours"]["repack"], 13.0)
        self.assertEqual(d["person_hours"]["inspect"], 2.1)
        self.assertEqual(d["docks_peak"]["pallet"], 1)          # co 1,25 h, rozładunek 39 min
        self.assertEqual(d["palletize_stations"], 0)

    def test_max_level_and_growth(self):
        d = day_demand([CONTAINERS, TRUCKS], NORMS, level="max", growth=1.3)
        # kontenery: ceil(9 × 1,3) = 12 × 52; auta: ceil(10 × 1,3) = 13 × 32
        self.assertEqual([r["arrivals"] for r in d["rows"]], [12, 13])
        self.assertEqual(d["pallets_in"], 12 * 52 + 13 * 32)
        self.assertGreater(d["docks_peak"]["container"], 2)
        self.assertEqual(d["person_hours"]["total"], round(sum(v for k, v in d["person_hours"].items()
                                                                if k != "total"), 1))
