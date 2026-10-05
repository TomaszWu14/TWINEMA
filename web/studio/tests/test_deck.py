"""Deck PDF: czysta funkcja (polskie znaki, liczba stron, kadr albo miejsce zastępcze) i widok."""
import io
import re
import shutil
import tempfile
from unittest import TestCase as PlainTestCase

from django.contrib.auth.models import Group, User
from django.core.files.base import ContentFile
from django.test import TestCase, override_settings
from django.urls import reverse
from PIL import Image

from core.roles import GROUP_VIEWER
from render.models import RenderJob
from studio.deck import build_deck, split_fact
from studio.models import Presentation, Shot
from twin.models import WarehouseModel

MEDIA = tempfile.mkdtemp(prefix="twinema_test_deck_")


def png():
    b = io.BytesIO()
    Image.new("RGB", (160, 90), (40, 80, 120)).save(b, "PNG")
    return b.getvalue()


def pages(pdf):
    return len(re.findall(rb"/Type /Page\b", pdf))


class BuildDeckTests(PlainTestCase):
    def test_pages_polish_text_and_placeholder(self):
        pdf = build_deck("Zażółć gęślą jaźń — centrum", "TWINEMA", "05.10.2026",
                         ["Miejsca paletowe: 2 304.", "Alejki bez naruszeń szerokości i kolizji."],
                         [{"label": "Przelot nad halą", "text": "Źródło łączności.", "image": png()},
                          {"label": "Plan z góry", "text": "Bez kadru.", "image": None}])
        self.assertTrue(pdf.startswith(b"%PDF"))
        self.assertEqual(pages(pdf), 5)                       # tytuł + liczby + 2 ujęcia + koniec
        self.assertIn(b"DejaVu", pdf)                         # osadzony font z polskimi znakami

    def test_without_facts_and_slides(self):
        self.assertEqual(pages(build_deck("T", "A", "d", [], [])), 2)

    def test_split_fact(self):
        self.assertEqual(split_fact("Miejsca paletowe: 2 304 (0,77 na m² hali)."),
                         ("Miejsca paletowe", "2 304 (0,77 na m² hali)"))
        self.assertEqual(split_fact("Alejki bez naruszeń."), ("", "Alejki bez naruszeń"))


@override_settings(MEDIA_ROOT=MEDIA, APP_NAME="TWINEMA")
class DeckViewTests(TestCase):
    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        shutil.rmtree(MEDIA, ignore_errors=True)

    def setUp(self):
        wm = WarehouseModel.objects.create(name="Hala", floor_width_m=30, floor_depth_m=20)
        wm.racks.create(zone="V", rack_id="001", n_bays=4, n_levels=3, x_m=4, y_m=4)
        self.p = Presentation.objects.create(model=wm, title="Film o hali", status="approved")
        self.s1 = Shot.objects.create(presentation=self.p, order=1, preset="plan", text="Plan z góry.")
        Shot.objects.create(presentation=self.p, order=2, preset="orbita", text="Orbita.")
        still = RenderJob.objects.create(model=wm, preset="plan", kind="still", status="done")
        still.result.save("k.png", ContentFile(png()))
        Shot.objects.filter(pk=self.s1.pk).update(still=still)
        viewer = User.objects.create_user("zarzad", password="x")
        viewer.groups.add(Group.objects.create(name=GROUP_VIEWER))
        self.client.force_login(viewer)                       # deck ogląda także Podgląd

    def test_viewer_downloads_pdf_with_stills_and_placeholders(self):
        r = self.client.get(reverse("studio:deck_pdf", args=[self.p.pk]) + "?pobierz=1")
        self.assertEqual(r["Content-Type"], "application/pdf")
        self.assertIn("attachment", r["Content-Disposition"])
        self.assertTrue(r.content.startswith(b"%PDF"))
        self.assertEqual(pages(r.content), 5)
        self.assertIn(b"/Subtype /Image", r.content)          # kadr ujęcia 1 osadzony

    def test_stale_still_not_used(self):
        Shot.objects.filter(pk=self.s1.pk).update(preset="przelot")   # kadr z innej kamery
        r = self.client.get(reverse("studio:deck_pdf", args=[self.p.pk]))
        self.assertNotIn(b"/Subtype /Image", r.content)

    def test_detail_and_list_link_deck(self):
        url = reverse("studio:deck_pdf", args=[self.p.pk])
        self.assertContains(self.client.get(reverse("studio:detail", args=[self.p.pk])), url)
        self.assertContains(self.client.get(reverse("studio:list")), url)
