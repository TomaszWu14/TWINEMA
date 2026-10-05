"""Scenariusze: tworzenie z domyślnymi, role, edycja planu, walidacja min ≤ śr ≤ max, kopia, demo."""
from io import StringIO

from django.contrib.auth.models import Group, User
from django.core.exceptions import ValidationError
from django.core.management import call_command
from django.test import TestCase
from django.urls import reverse

from core.roles import GROUP_DESIGNER, GROUP_VIEWER
from scenario.models import InboundStream, Scenario


class ScenarioViewTests(TestCase):
    def setUp(self):
        self.designer = User.objects.create_user("proj", password="x")
        self.designer.groups.add(Group.objects.create(name=GROUP_DESIGNER))
        self.viewer = User.objects.create_user("zarzad", password="x")
        self.viewer.groups.add(Group.objects.create(name=GROUP_VIEWER))
        self.client.force_login(self.designer)

    def _create(self, name="Rok bazowy"):
        self.client.post(reverse("scenario:create"), {"name": name})
        return Scenario.objects.get(name=name)

    def _day_post(self, sc, kind, rows):
        streams = list(sc.days.get(kind=kind).inbound.all())
        data = {f"{kind}-TOTAL_FORMS": len(rows), f"{kind}-INITIAL_FORMS": len(streams),
                f"{kind}-MIN_NUM_FORMS": 0, f"{kind}-MAX_NUM_FORMS": 1000}
        for i, row in enumerate(rows):
            data.update({f"{kind}-{i}-{k}": v for k, v in row.items()})
        return self.client.post(reverse("scenario:day_save", args=[sc.pk, kind]), data, follow=True)

    @staticmethod
    def _row(s, **over):
        row = {k: getattr(s, k) for k in ("kind", "arrivals_min", "arrivals_avg", "arrivals_max", "pallets_min",
                                          "pallets_avg", "pallets_max", "window_from", "window_to", "mono_pct",
                                          "inspect_pct", "inspect_min")}
        return {"id": s.pk, **row, **over}

    def test_create_seeds_typical_and_peak_with_results(self):
        sc = self._create()
        self.assertEqual(sorted(sc.days.values_list("kind", flat=True)), ["peak", "typical"])
        self.assertEqual(sc.days.get(kind="typical").inbound.count(), 3)
        peak = sc.days.get(kind="peak").inbound.get(kind="container40")
        self.assertEqual(peak.arrivals_avg, 10)                       # 8 × 1,3
        r = self.client.get(reverse("scenario:detail", args=[sc.pk]))
        self.assertContains(r, "Doki kontenerowe w szczycie")
        self.assertContains(r, "Zapisz plan przyjęć")
        self.assertContains(self.client.get(reverse("core:home")), reverse("scenario:list"))

    def test_viewer_sees_results_but_no_forms_and_cannot_post(self):
        sc = self._create()
        self.client.force_login(self.viewer)
        r = self.client.get(reverse("scenario:detail", args=[sc.pk]))
        self.assertContains(r, "Palet przyjętych / dzień")
        self.assertContains(r, "Założenia przyjęć")
        self.assertNotContains(r, "Zapisz plan przyjęć")
        self.assertEqual(self.client.post(reverse("scenario:copy", args=[sc.pk])).status_code, 403)
        self.assertEqual(self.client.post(reverse("scenario:create"), {"name": "X"}).status_code, 403)

    def test_edit_stream_recalculates(self):
        sc = self._create()
        c = sc.days.get(kind="typical").inbound.get(kind="container40")
        others = [self._row(s) for s in sc.days.get(kind="typical").inbound.exclude(pk=c.pk)]
        self._day_post(sc, "typical", [self._row(c, arrivals_avg=9, arrivals_max=12), *others])
        c.refresh_from_db()
        self.assertEqual((c.arrivals_avg, c.arrivals_max), (9, 12))
        self.assertEqual(sc.days.get(kind="typical").demand("avg")["rows"][0]["arrivals"], 9)

    def test_min_avg_max_order_is_validated(self):
        sc = self._create()
        c = sc.days.get(kind="typical").inbound.get(kind="truck33")
        others = [self._row(s) for s in sc.days.get(kind="typical").inbound.exclude(pk=c.pk)]
        r = self._day_post(sc, "typical", [self._row(c, pallets_min=30, pallets_avg=20), *others])
        self.assertContains(r, "min ≤ śr. ≤ max")
        c.refresh_from_db()
        self.assertEqual(c.pallets_min, 17)
        bad = InboundStream(day=c.day, kind="solo", arrivals_min=1, arrivals_avg=1, arrivals_max=1, pallets_min=1,
                            pallets_avg=1, pallets_max=1, window_from=14, window_to=6)
        with self.assertRaises(ValidationError):
            bad.full_clean()

    def test_save_params_and_reject_zero_norm(self):
        sc = self._create()
        data = {"name": sc.name, "description": "", "growth": 1.3, "seed": 7, "shift_h": 8,
                **{f: getattr(sc, f) for f in Scenario.NORM_FIELDS}}
        self.client.post(reverse("scenario:save", args=[sc.pk]), data)
        sc.refresh_from_db()
        self.assertEqual((sc.growth, sc.seed), (1.3, 7))
        r = self.client.post(reverse("scenario:save", args=[sc.pk]), {**data, "cartons_per_pallet": 0}, follow=True)
        self.assertContains(r, "muszą być dodatnie")

    def test_copy_is_deep_and_independent(self):
        sc = self._create()
        self.client.post(reverse("scenario:copy", args=[sc.pk]))
        copy = Scenario.objects.get(name="Rok bazowy (kopia)")
        self.assertEqual(copy.days.count(), 2)
        self.assertEqual(InboundStream.objects.filter(day__scenario=copy).count(), 6)
        InboundStream.objects.filter(day__scenario=copy).delete()
        self.assertEqual(InboundStream.objects.filter(day__scenario=sc).count(), 6)

    def test_delete(self):
        sc = self._create()
        self.client.post(reverse("scenario:delete", args=[sc.pk]))
        self.assertFalse(Scenario.objects.exists())

    def test_demo_command_is_idempotent(self):
        out = StringIO()
        call_command("demo_scenariusz", stdout=out)
        call_command("demo_scenariusz", stdout=out)
        sc = Scenario.objects.get()
        self.assertEqual(InboundStream.objects.filter(day__scenario=sc).count(), 6)
        typical = sc.days.get(kind="typical").demand("avg")
        self.assertEqual(typical["pallets_in"], 8 * 45 + 8 * 26 + 6 * 12)
        self.assertIn("osobogodzin", out.getvalue())
