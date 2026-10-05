"""Typy regałów A/B/C/D: nośność per poziom (level_weights) — zapis w edytorze,
serializacja do rack_types i etykiety kg w widoku 3D."""
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from twin import models as m


class RackTypeWeightsTests(TestCase):
    def setUp(self):
        get_user_model().objects.create_superuser(username="b", password="x")
        self.client.post("/login/", {"username": "b", "password": "x"})

    def test_model_stores_level_weights(self):
        rt = m.WarehouseRackType.objects.create(code="A", name="Typ A",
                                                level_weights={"1": 1000, "2": 300})
        rt.refresh_from_db()
        self.assertEqual(rt.level_weights, {"1": 1000, "2": 300})

    def test_editor_saves_level_weights(self):
        url = reverse("twin:warehouse_rack_type_new")
        self.client.post(url, {
            "code": "B", "name": "Typ B",
            "level_1_height": "2400", "level_1_weight": "1000",
            "level_2_height": "1200", "level_2_weight": "300",
            "width_mm": "800", "manip_mm": "900", "depth_mm": "1100",
            "max_weight_kg": "1200", "max_volume_m3": "2.5",
            "color_hex": "#f59e0b", "level_cols_json": "{}",
        })
        rt = m.WarehouseRackType.objects.get(code="B")
        self.assertEqual(rt.level_weights, {"1": 1000, "2": 300})
        self.assertEqual(rt.level_heights, {"1": 2400, "2": 1200})

    def test_editor_get_200(self):
        rt = m.WarehouseRackType.objects.create(code="C", name="Typ C",
                                                level_weights={"1": 1000})
        r = self.client.get(reverse("twin:warehouse_rack_type_edit", args=[rt.pk]))
        self.assertEqual(r.status_code, 200)

