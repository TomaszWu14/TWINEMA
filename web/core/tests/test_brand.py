"""L1: logo — sygnet w nagłówku i na logowaniu, favicon SVG, marka przez app_name."""
from pathlib import Path

from django.conf import settings
from django.contrib.auth.models import User
from django.test import TestCase, override_settings
from django.urls import reverse

BRAND = Path(settings.BASE_DIR) / "core" / "static" / "core" / "brand"


class BrandTests(TestCase):
    def test_login_and_header_show_mark_and_wordmark(self):
        page = self.client.get(reverse("core:login"))
        self.assertContains(page, "core/brand/mark.svg")
        self.assertContains(page, "core/brand/mark-small.svg")          # favicon
        self.assertContains(page, "<b>TW</b>INEMA", html=False)
        self.client.force_login(User.objects.create_superuser("a", "a@x.pl", "x"))
        home = self.client.get(reverse("core:home"))
        self.assertContains(home, 'aria-label="TWINEMA — strona główna"')

    @override_settings(APP_NAME="Hala Projekt")
    def test_other_app_name_plain(self):
        page = self.client.get(reverse("core:login"))
        self.assertContains(page, "Hala Projekt")
        self.assertNotContains(page, "<b>TW</b>")

    def test_svg_files_are_vector_only(self):
        for name in ("logo.svg", "logo-light.svg", "logo-orange.svg", "mark.svg", "mark-small.svg"):
            svg = (BRAND / name).read_text(encoding="utf-8")
            self.assertTrue(svg.startswith("<svg") and "viewBox" in svg, name)
            self.assertNotIn("<image", svg, name)                          # bez rastrów
