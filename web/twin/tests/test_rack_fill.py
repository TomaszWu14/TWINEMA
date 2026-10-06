"""Wypełnienie regałów ze stanu: kody lokalizacji → regał (SlotLocator) / pojemność; widok modelu podaje fill_pct."""
from django.contrib.auth.models import User
from django.test import SimpleTestCase, TestCase
from django.urls import reverse

from masterdata.demo import make_code
from twin.blender_stock import rack_capacity, rack_fill_pct
from twin.models import WarehouseModel

RACK = {"zone": "V", "rack_id": "001", "width": 5.4, "n_bays": 2, "n_levels": 3}      # 2 × 3 × 3 = 18 miejsc


class RackFillTests(SimpleTestCase):
    def test_capacity_and_pct(self):
        self.assertEqual(rack_capacity(RACK), 18)
        codes = [make_code("V", "001", 10 + b, p, "ABC"[lvl]) for b in range(2) for p in range(3) for lvl in range(2)]
        other = {**RACK, "rack_id": "002"}
        fill = rack_fill_pct([RACK, other], codes + ["X-999-01-0A", ""])        # kody spoza modelu pomijane
        self.assertEqual(fill, {("V", "001"): 67, ("V", "002"): 0})

    def test_never_above_100(self):
        codes = [make_code("V", "001", 10 + b, p, lvl) for b in range(9) for p in range(9) for lvl in "ABCDE"]
        self.assertEqual(rack_fill_pct([RACK], codes)[("V", "001")], 100)


class RackFillViewTests(TestCase):
    def test_model_view_has_fill_after_stock_import(self):
        from masterdata.services import load_demo
        self.client.force_login(User.objects.create_superuser("a", "a@x.pl", "x"))
        wm = WarehouseModel.objects.create(name="H", floor_width_m=40, floor_depth_m=30)
        wm.racks.create(zone="V", rack_id="001", n_bays=4, n_levels=4, x_m=4, y_m=4)
        url = reverse("twin:warehouse_model_view", args=[wm.pk])
        self.assertContains(self.client.get(url), '"fill_pct": null')         # bez importu stanów — brak danych
        load_demo(wm, fill=0.5)
        pct = self.client.get(url).context["racks_json"]
        self.assertRegex(pct, r'"fill_pct": (3\d|4\d|5\d|6\d)\b')               # ~50 % miejsc zajętych
