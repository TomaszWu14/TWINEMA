"""Macierz ról: rola Podgląd nie zmienia danych i nie widzi danych źródłowych (ZALOZENIA #25).

Przechodzi wszystkie trasy aplikacji (`get_resolver`) — parametry podstawione (int → 999, tekst → „x”),
bo dekorator roli działa przed szukaniem obiektu: brak uprawnień = 403, nie 404.
Poza testem: API workerów (token zamiast ról), admin, health, logowanie.
"""
import re

from django.contrib.auth.models import Group, User
from django.db import connection
from django.test import TestCase
from django.test.utils import CaptureQueriesContext
from django.urls import URLPattern, URLResolver, get_resolver, reverse

from core.roles import GROUP_VIEWER
from twin.models import WarehouseModel

SKIP_PREFIXES = ("api/", "admin/", "health/", "login/", "logout/", "robots.txt")
WRITE = re.compile(r"\s*(INSERT|UPDATE|DELETE)\b", re.I)
IGNORED_TABLES = re.compile(r'"?(django_session|axes_\w+|auth_user)"?', re.I)   # sesja, logowanie, last_login
# GET z listami danych źródłowych (materiały, stany, kody lokalizacji, przypisania materiałów)
SOURCE_GETS = ["masterdata:materials", "masterdata:catalog", "ml:segments_csv",
               "twin:warehouse_model_detect", "twin:warehouse_model_compliance"]


def _routes(patterns, prefix="", ns=""):
    for p in patterns:
        if isinstance(p, URLResolver):
            sub_ns = f"{ns}{p.namespace}:" if p.namespace else ns
            yield from _routes(p.url_patterns, prefix + str(p.pattern), sub_ns)
        elif isinstance(p, URLPattern) and p.name:
            yield prefix + str(p.pattern), ns + p.name, p.pattern.converters


def _url(name, converters):
    kwargs = {k: 999 if type(c).__name__ == "IntConverter" else "x" for k, c in converters.items()}
    return reverse(name, kwargs=kwargs or None)


class ViewerRoleMatrixTests(TestCase):
    def setUp(self):
        self.viewer = User.objects.create_user("zarzad", password="x")
        self.viewer.groups.add(Group.objects.create(name=GROUP_VIEWER))
        self.client.force_login(self.viewer)

    def test_viewer_post_never_writes(self):
        """Widoki odczytu przyjmują POST jak GET (renderują) — liczy się, że nic nie zapisują."""
        writes = []
        for route, name, conv in _routes(get_resolver().url_patterns):
            if route.startswith(SKIP_PREFIXES):
                continue
            with CaptureQueriesContext(connection) as ctx:
                status = self.client.post(_url(name, conv)).status_code
            sql = [q["sql"] for q in ctx.captured_queries
                   if WRITE.match(q["sql"]) and not IGNORED_TABLES.search(q["sql"])]
            if sql:
                writes.append(f"{name} → {status}: {sql[0][:80]}")
        self.assertEqual(writes, [], "Podgląd zapisuje dane przez te trasy")

    def test_viewer_has_no_source_lists(self):
        names = {n for _r, n, _c in _routes(get_resolver().url_patterns)}
        for name in SOURCE_GETS:
            self.assertIn(name, names)                           # lista nie rozjeżdża się z URL-ami
            conv = next(c for _r, n, c in _routes(get_resolver().url_patterns) if n == name)
            with self.subTest(name=name):
                self.assertEqual(self.client.get(_url(name, conv)).status_code, 403)


class ViewerSceneTests(TestCase):
    def setUp(self):
        self.viewer = User.objects.create_user("zarzad", password="x")
        self.viewer.groups.add(Group.objects.create(name=GROUP_VIEWER))
        self.wm = WarehouseModel.objects.create(name="Hala", floor_width_m=30, floor_depth_m=20)
        self.wm.racks.create(zone="V", rack_id="001", n_bays=4, n_levels=3, x_m=4, y_m=4)

    def test_viewer_scene_without_source_fields(self):
        from twin.views.warehouse_blender import SOURCE_PALLET_KEYS, _for_viewer

        scene = {"pallets": [{"code": "V-001-01-A", "sku": "M1", "name": "N", "lot": "L", "hu": ["H"], "qty": 5,
                              "state": "occupied", "abc": "A"}],
                 "items": [{"id": "p1", "sku": "M1"}], "source": {"batch": "import.xlsx", "pallets": "stan_hu"}}
        out = _for_viewer(scene)
        p = out["pallets"][0]
        self.assertFalse(set(SOURCE_PALLET_KEYS) & set(p))
        self.assertEqual((p["code"], p["state"], p["abc"]), ("", "occupied", "A"))
        self.assertEqual(out["items"][0]["sku"], "")
        self.assertNotIn("batch", out["source"])

        for name in ("twin:warehouse_model_flow_json", "twin:warehouse_model_blender_json"):
            self.client.force_login(self.viewer)
            body = self.client.get(reverse(name, args=[self.wm.pk])).content.decode()
            with self.subTest(name=name):
                for key in ('"sku": "M', '"lot":', '"hu":'):
                    self.assertNotIn(key, body)
