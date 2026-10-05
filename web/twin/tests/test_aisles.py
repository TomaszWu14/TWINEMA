"""R2: alejki dla par 0°/180° (blok „Dodaj blok” — plecami / frontami), najbliższy sąsiad."""
from unittest import TestCase

from twin.design_catalog import BACK_GAP_M, check_aisles, params_for

D, W = 1.1, 27.0                       # głębokość regału, szerokość (10 × 2,7 m)


def rack(x, y, angle, label):
    return {"kind": "rack_std", "label": label, "x": x, "y": y, "angle": angle,
            "params": params_for("rack_std", bays=10, levels=5, bay_width=2.7, depth=D, level_h=1.8,
                                 pallets_per_bay=3)}


def block(aisle):
    """Jak makeBlock w layout-core.js: 0° | 180° (narożnik w x+w, y+d) | alejka | 0°."""
    y1 = D + BACK_GAP_M
    return [rack(0, 0, 0, "A"), rack(W, y1 + D, 180, "B"), rack(0, y1 + D + aisle, 0, "C")]


class AisleTests(TestCase):
    def test_block_back_to_back_and_front_aisle(self):
        bad = check_aisles(block(1.0))
        self.assertEqual([(i["type"], i["a"], i["b"], i["gap_m"]) for i in bad],
                         [("za wąska alejka", "B", "C", 1.0)])     # dawniej 0/180° było pomijane
        self.assertEqual(check_aisles(block(3.2)), [])                # alejka OK, plecy A|B bez alejki

    def test_overlap_of_opposite_racks_is_collision(self):
        issues = check_aisles([rack(0, 0, 0, "A"), rack(W, D - 0.5 + D, 180, "B")])
        self.assertEqual([i["type"] for i in issues], ["kolizja"])

    def test_only_nearest_neighbours(self):
        # A (front w −y) … C ma za sobą B: alejka A–C nie istnieje, bo B stoi pomiędzy
        a, b = rack(0, 3.0, 180, "A"), rack(0, 4.4, 0, "B")
        c = rack(0, 4.4 + D + 0.2, 0, "C")
        types = {(i["a"], i["b"]) for i in check_aisles([a, b, c])}
        self.assertNotIn(("A", "C"), types)
