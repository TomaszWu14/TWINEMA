"""Layout z katalogiem sprzętu (K1): alejka Ast z katalogu, wysokość podnoszenia, udźwig na wysokości, zapis FK."""
import json
from unittest import TestCase as PlainTestCase

from django.contrib.auth.models import Group, User
from django.test import TestCase
from django.urls import reverse

from core.roles import GROUP_DESIGNER
from equipment.models import Equipment
from twin.design_generator import generate
from twin.layout import analyze, clean_layout
from twin.models import WarehouseModel

from .test_layout import KINDS, codes, layout, rack

REACH = {"id": 1, "kind": "reach", "name": "Reach 10 m", "aisle_m": 2.9, "max_lift_m": 10, "capacity_kg": 1600,
         "lift_curve": [[6, 1600], [10, 1000]]}
COUNTER = {"id": 2, "kind": "counterbalance", "name": "Czołowy", "aisle_m": 3.8, "max_lift_m": 4.5,
           "capacity_kg": 2500, "lift_curve": []}
VNA = {"id": 3, "kind": "vna", "name": "VNA 14 m", "aisle_m": 1.8, "max_lift_m": 14, "capacity_kg": 1500,
       "lift_curve": [[10, 1500], [14, 1200]]}
CAT = {e["id"]: e for e in (REACH, COUNTER, VNA)}


class LayoutEquipmentTests(PlainTestCase):
    def test_aisle_from_catalog_overrides_category(self):
        # para regałów (głęb. 1,1 m) z alejką 3,4 m: reach (2,9 m) OK, wózek czołowy (Ast 3,8 m) — za wąsko
        pair = [rack(n_levels=2), rack(rid="002", y=9.6, n_levels=2)]
        self.assertEqual(analyze(layout([{**r, "equipment_id": 1} for r in pair]), CAT)[1], [])
        self.assertEqual(codes(analyze(layout([{**r, "equipment_id": 2} for r in pair]), CAT)[1]),
                         [("aisle", "warning")])

    def test_catalog_kind_sets_category_and_unknown_id_is_dropped(self):
        lay = layout([rack(equipment="reach", equipment_id=3), rack(rid="002", y=20, equipment_id=99)])
        analyze(lay, CAT)
        self.assertEqual((lay["racks"][0]["equipment"], lay["racks"][1]["equipment_id"]), ("vna", None))

    def test_lift_height_error_and_capacity_warning(self):
        high = rack(n_levels=7, level_height_cm=180, equipment_id=1)                  # belka 10,8 m > 10 m
        self.assertEqual(codes(analyze(layout([high]), CAT)[1]), [("lift", "error")])
        heavy = rack(n_levels=6, level_height_cm=180, load_kg=1500, equipment_id=1)     # belka 9 m: udźwig 1150 kg
        _, issues = analyze(layout([heavy]), CAT)
        self.assertEqual(codes(issues), [("lift_load", "warning")])
        self.assertIn("od poziomu 5", issues[0]["message"])                            # 7,2 m → 1420 kg < 1500
        self.assertEqual(analyze(layout([rack(n_levels=6, level_height_cm=180, load_kg=1000, equipment_id=1)]),
                                 CAT)[1], [])

    def test_generated_hall_with_assigned_vna_class_has_no_issues(self):
        g = generate()
        data = {"floor": {**g["floor"], "clear_height": g["params"]["clear_height_m"]}, "version": "",
                "racks": [{"zone": r["zone"], "rack_id": r["rack_id"], "x": r["x_m"], "y": r["y_m"],
                           "angle": r["angle_deg"], "equipment_id": 3 if r["equipment"] == "vna" else None,
                           **{k: r[k] for k in ("n_bays", "n_levels", "bay_width_cm", "depth_cm", "level_height_cm",
                                                "equipment")}} for r in g["racks"]],
                "features": [{"kind": f["kind"], "label": f["label"], "x": f["x_m"], "y": f["y_m"],
                              "width": f["width_m"], "depth": f["depth_m"], "angle": f["angle_deg"]}
                             for f in g["features"]]}
        self.assertEqual(analyze(clean_layout(data, KINDS), CAT)[1], [])


class LayoutEquipmentSaveTests(TestCase):
    def setUp(self):
        u = User.objects.create_user("proj", password="x")
        u.groups.add(Group.objects.create(name=GROUP_DESIGNER))
        self.client.force_login(u)
        self.wm = WarehouseModel.objects.create(name="Hala", floor_width_m=40, floor_depth_m=30)
        self.r = self.wm.racks.create(zone="V", rack_id="001", n_bays=4, n_levels=4, x_m=4, y_m=4)
        self.vna = Equipment.objects.get(name="VNA kombi 1,5 t / 14 m")

    def _save(self, **rack_over):
        data = self.client.get(reverse("twin:warehouse_layout_json", args=[self.wm.pk])).json()
        for r in data["racks"]:
            r.update(rack_over)
            if "equipment_id" in rack_over and rack_over["equipment_id"] is ...:
                del r["equipment_id"]
        return self.client.post(reverse("twin:warehouse_layout_save", args=[self.wm.pk]), json.dumps(data),
                                content_type="application/json")

    def test_save_sets_fk_and_category_old_client_keeps_it(self):
        self.assertEqual(self._save(equipment_id=self.vna.pk).status_code, 200)
        self.r.refresh_from_db()
        self.assertEqual((self.r.equipment_model, self.r.equipment), (self.vna, "vna"))
        self.assertEqual(self._save(equipment_id=...).status_code, 200)               # stary klient: bez pola
        self.r.refresh_from_db()
        self.assertEqual(self.r.equipment_model, self.vna)
        self._save(equipment_id=None)
        self.r.refresh_from_db()
        self.assertIsNone(self.r.equipment_model)

    def test_editor_config_lists_rack_catalog(self):
        r = self.client.get(reverse("twin:warehouse_layout_editor", args=[self.wm.pk]))
        self.assertContains(r, "VNA kombi 1,5 t / 14 m")
        self.assertNotContains(r, "AMR półkowy")                    # AMR nie obsługuje regałów paletowych
