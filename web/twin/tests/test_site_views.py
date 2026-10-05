"""Działka w API edytora (D1): odczyt/zapis, brak klucza = bez zmian, błędy działki blokują zapis, 409,
kopia modelu z działką, generator zapisuje działkę, scena 3D i animacja dostają działkę."""
import json

from django.contrib.auth.models import Group, User
from django.test import TestCase
from django.urls import reverse

from core.roles import GROUP_DESIGNER
from twin.models import WarehouseModel
from twin.site import default_site


class SiteApiTests(TestCase):
    def setUp(self):
        self.wm = WarehouseModel.objects.create(name="Hala", floor_width_m=60, floor_depth_m=40, clear_height_m=10)
        self.wm.racks.create(zone="V", rack_id="001", n_bays=4, n_levels=4, x_m=5, y_m=5)
        self.wm.features.create(kind="dock", label="Dok 1", x_m=0, y_m=20, width_m=4, depth_m=3.5, dock_role="in_pallet")
        user = User.objects.create_user("proj", password="x")
        user.groups.add(Group.objects.create(name=GROUP_DESIGNER))
        self.client.force_login(user)

    def _get(self):
        return self.client.get(reverse("twin:warehouse_layout_json", args=[self.wm.pk])).json()

    def _post(self, name, data):
        return self.client.post(reverse(f"twin:warehouse_layout_{name}", args=[self.wm.pk]),
                                json.dumps(data), content_type="application/json")

    def _site(self):
        return default_site({"width": 60, "depth": 40, "clear_height": 10})

    def test_editor_config_has_default_site_and_area_kinds(self):
        r = self.client.get(reverse("twin:warehouse_layout_editor", args=[self.wm.pk]))
        self.assertContains(r, "defaultSite")
        self.assertContains(r, 'data-le-view="site"')
        self.assertContains(r, 'id="le-site"')

    def test_save_and_read_site_with_kpi(self):
        data = self._get()
        self.assertEqual(data["site"], {})
        data["site"] = self._site()
        r = self._post("save", data)
        self.assertEqual(r.status_code, 200, r.content)
        self.assertGreater(r.json()["kpi"]["site"]["plot_m2"], 0)
        self.wm.refresh_from_db()
        self.assertEqual(self.wm.site["access_side"], "S")
        self.assertEqual(self._get()["site"]["width"], self.wm.site["width"])

    def test_missing_site_key_keeps_site_and_empty_removes(self):
        self.wm.site = self._site()
        self.wm.save()
        data = self._get()
        data.pop("site")
        self.assertEqual(self._post("save", data).status_code, 200)
        self.wm.refresh_from_db()
        self.assertTrue(self.wm.site)
        data = self._get()
        data["site"] = {}
        self._post("save", data)
        self.wm.refresh_from_db()
        self.assertEqual(self.wm.site, {})

    def test_site_errors_block_save(self):
        data = self._get()
        data["site"] = {**self._site(), "max_coverage_pct": 5}
        r = self._post("save", data)
        self.assertEqual(r.status_code, 422)
        self.assertIn("coverage", [i["code"] for i in r.json()["issues"]])
        check = self._post("check", data).json()
        self.assertTrue(next(i for i in check["issues"] if i["code"] == "coverage")["hall"])
        self.wm.refresh_from_db()
        self.assertEqual(self.wm.site, {})

    def test_bad_site_is_400(self):
        data = self._get()
        data["site"] = {**self._site(), "access_side": "X"}
        self.assertEqual(self._post("check", data).status_code, 400)

    def test_stale_version_is_409(self):
        data = self._get()
        data["site"] = self._site()
        data["version"] = "2000-01-01T00:00:00+00:00"
        self.assertEqual(self._post("save", data).status_code, 409)

    def test_copy_keeps_site(self):
        self.wm.site = self._site()
        self.wm.save()
        self.client.post(reverse("twin:warehouse_model_copy", args=[self.wm.pk]))
        copy = WarehouseModel.objects.exclude(pk=self.wm.pk).get()
        self.assertEqual(copy.site, self.wm.site)

    def test_model_view_passes_site_to_3d(self):
        self.wm.site = self._site()
        self.wm.save()
        r = self.client.get(reverse("twin:warehouse_model_view", args=[self.wm.pk]))
        self.assertContains(r, "const SITE_JSON")
        self.assertContains(r, '"access_side": "S"')


class GeneratorSiteTests(TestCase):
    def test_generator_saves_site(self):
        user = User.objects.create_user("proj", password="x")
        user.groups.add(Group.objects.create(name=GROUP_DESIGNER))
        self.client.force_login(user)
        from twin.design_generator import PRESET
        r = self.client.post(reverse("twin:warehouse_model_generator"), {"name": "Nowa", "create": "1", **PRESET})
        self.assertEqual(r.status_code, 302)
        wm = WarehouseModel.objects.get(name="Nowa")
        self.assertEqual(wm.site["hall"]["x"], 45.0)
        self.assertEqual(len([e for e in wm.site["entries"] if e["kind"] == "truck"]), 2)
