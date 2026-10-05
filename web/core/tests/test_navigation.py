"""R4: nawigacja w nagłówku z core.views.MODULES (te same nazwy co kafle), aktywna pozycja z aria-current,
wersja w /health/ z config.py."""
from django.contrib.auth.models import User
from django.test import TestCase, override_settings
from django.urls import resolve, reverse

from core.views import MODULES, active_module


class NavigationTests(TestCase):
    def setUp(self):
        self.client.force_login(User.objects.create_superuser("a", "a@x.pl", "x"))

    def test_nav_and_tiles_use_same_names(self):
        r = self.client.get("/")
        nav = r.context["nav_modules"]
        self.assertEqual([m["name"] for m in nav], [m["name"] for m in MODULES])
        self.assertEqual([m["name"] for m in r.context["modules"]], [m["name"] for m in MODULES])

    def test_active_module_by_url_name_then_app(self):
        cases = {"scenario:showcase_list": "prezentacje", "scenario:list": "scenariusze",
                 "twin:ewm_tasks_list": "zadania", "twin:design_hub": "projektowanie",
                 "twin:warehouse_model_list": "model", "equipment:list": "sprzet", "core:home": None}
        for name, key in cases.items():
            self.assertEqual(active_module(resolve(reverse(name))), key, name)

    def test_aria_current_on_active_only(self):
        html = self.client.get(reverse("scenario:showcase_list")).content.decode()
        self.assertEqual(html.count('aria-current="page"'), 1)
        self.assertIn(f'href="{reverse("scenario:showcase_list")}" class="is-active" aria-current="page"', html)

    @override_settings(GIT_SHA="abc123")
    def test_health_version_from_config(self):
        self.assertEqual(self.client.get("/health/").json()["version"], "abc123")


class SafeXlsxTests(TestCase):
    def test_openpyxl_uses_defusedxml(self):
        # R4: importy XLSX z plików użytkownika — openpyxl musi parsować przez defusedxml (requirements.txt)
        from openpyxl import xml
        self.assertTrue(xml.DEFUSEDXML)
