"""E2b — API edytora: zapis wysokości, słupów i sprzętu; podkład (upload, sygnatura, limit, kalibracja,
bez zmiany wersji); słupy i nowe rodzaje elementów w scenie 3D/Blendera."""
import io
import json
import shutil
import tempfile
from unittest import mock

from django.contrib.auth.models import Group, User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings
from django.urls import reverse
from PIL import Image

from core.roles import GROUP_DESIGNER, GROUP_VIEWER
from twin.models import WarehouseModel

MEDIA = tempfile.mkdtemp(prefix="twinema_test_underlay_")


def png(w=200, h=100):
    buf = io.BytesIO()
    Image.new("RGB", (w, h), "white").save(buf, "PNG")
    return buf.getvalue()


@override_settings(MEDIA_ROOT=MEDIA)
class StructureApiTests(TestCase):
    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        shutil.rmtree(MEDIA, ignore_errors=True)

    def setUp(self):
        self.wm = WarehouseModel.objects.create(name="Hala", floor_width_m=60, floor_depth_m=40)
        self.wm.racks.create(zone="V", rack_id="001", n_bays=4, n_levels=4, x_m=5, y_m=5)
        self.designer = User.objects.create_user("proj", password="x")
        self.designer.groups.add(Group.objects.create(name=GROUP_DESIGNER))
        self.viewer = User.objects.create_user("zarzad", password="x")
        self.viewer.groups.add(Group.objects.create(name=GROUP_VIEWER))
        self.client.force_login(self.designer)

    def _get(self):
        return self.client.get(reverse("twin:warehouse_layout_json", args=[self.wm.pk])).json()

    def _post(self, name, data):
        return self.client.post(reverse(f"twin:warehouse_layout_{name}", args=[self.wm.pk]),
                                json.dumps(data), content_type="application/json")

    def _upload(self, data, name="rzut.png"):
        return self.client.post(reverse("twin:warehouse_layout_underlay_upload", args=[self.wm.pk]),
                                {"file": SimpleUploadedFile(name, data)})

    def test_save_height_columns_equipment(self):
        data = self._get()
        self.assertEqual((data["floor"]["clear_height"], data["columns"], data["column_list"], data["underlay"]),
                         (None, {}, [], None))
        data["floor"]["clear_height"] = 12
        data["columns"] = {"pitch_x": 20, "pitch_y": 20, "offset_x": 30, "offset_y": 30, "size": 0.5,
                           "removed": [], "extra": [[50, 2]]}
        data["racks"][0]["equipment"] = "vna"
        r = self._post("save", data)
        self.assertEqual(r.status_code, 200, r.content)
        self.assertEqual(len(r.json()["column_list"]), 3)                # (30; 30), (50; 30) + dodany (50; 2)
        self.wm.refresh_from_db()
        self.assertEqual((self.wm.clear_height_m, self.wm.columns["pitch_x"]), (12.0, 20.0))
        self.assertEqual(self.wm.racks.get().equipment, "vna")
        check = self._post("check", self._get()).json()
        self.assertEqual(len(check["column_list"]), 3)
        self.assertEqual(check["kpi"]["columns"], 3)

    def test_rack_on_column_blocks_save(self):
        data = self._get()
        data["columns"] = {"pitch_x": 0, "pitch_y": 0, "extra": [[7, 5.5]]}   # w środku regału
        r = self._post("save", data)
        self.assertEqual(r.status_code, 422)
        self.assertEqual([i["code"] for i in r.json()["issues"]], ["column"])

    def test_underlay_upload_keeps_version_and_calibration_saves(self):
        version = self._get()["version"]
        r = self._upload(png(300, 150))
        self.assertEqual(r.status_code, 200, r.content)
        u = r.json()["underlay"]
        self.assertEqual((u["w_px"], u["h_px"], u["scale"]), (300, 150, 0.2))   # 60 m / 300 px
        self.assertEqual(self._get()["version"], version)                        # edytor nie dostanie 409
        img = self.client.get(u["url"])
        self.assertEqual((img.status_code, img["Content-Type"]), (200, "image/png"))
        self.assertTrue(b"".join(img.streaming_content).startswith(b"\x89PNG"))
        img.close()                                                      # Windows: zwolnij plik przed usunięciem
        data = self._get()
        data["underlay"] = {"scale": 0.25, "x": 1.5, "y": -2, "opacity": 0.3}
        self.assertEqual(self._post("save", data).status_code, 200)
        self.wm.refresh_from_db()
        self.assertEqual(self.wm.underlay_meta, {"scale": 0.25, "x": 1.5, "y": -2.0, "opacity": 0.3,
                                                 "w_px": 300, "h_px": 150})
        r = self.client.post(reverse("twin:warehouse_layout_underlay_upload", args=[self.wm.pk]), {"delete": "1"})
        self.assertEqual(r.json(), {"underlay": None})
        self.assertIsNone(self._get()["underlay"])

    def test_underlay_rejects_non_images_and_too_big(self):
        self.assertEqual(self._upload(b"%PDF-1.7 rzut", "rzut.pdf").status_code, 400)
        self.assertEqual(self._upload(b"\x89PNG\r\n\x1a\nzepsuty").status_code, 400)       # sygnatura bez obrazu
        with mock.patch("twin.views.warehouse_layout.MAX_UNDERLAY", 10):
            self.assertEqual(self._upload(png()).status_code, 413)
        self.assertEqual(self.client.post(reverse("twin:warehouse_layout_underlay_upload", args=[self.wm.pk]))
                         .status_code, 400)

    def test_viewer_cannot_upload_or_fetch_underlay(self):
        self._upload(png())
        self.client.force_login(self.viewer)
        self.assertEqual(self._upload(png()).status_code, 403)
        self.assertEqual(self.client.get(reverse("twin:warehouse_layout_underlay", args=[self.wm.pk])).status_code,
                         403)

    def test_scene_has_columns_and_new_kinds(self):
        self.wm.clear_height_m = 11
        self.wm.columns = {"pitch_x": 0, "pitch_y": 0, "size": 0.6, "removed": [], "extra": [[40, 20]]}
        self.wm.save()
        for kind in ("fire_route", "charging", "walkway", "zone_adr"):
            self.wm.features.create(kind=kind, label=kind, x_m=30, y_m=30, width_m=5, depth_m=3)
        scene = self.client.get(reverse("twin:warehouse_model_blender_json", args=[self.wm.pk])).json()
        cols = [f for f in scene["features"] if f["kind"] == "column"]
        self.assertEqual(len(cols), 1)
        self.assertEqual((cols[0]["x"], cols[0]["height"]), (39.7, 11))
        self.assertEqual({f["kind"] for f in scene["features"]} - {"column"},
                         {"fire_route", "charging", "walkway", "zone_adr"})
        page = self.client.get(reverse("twin:warehouse_model_view", args=[self.wm.pk]))
        self.assertContains(page, "zone_adr")
        self.assertContains(page, '"kind": "column"')
