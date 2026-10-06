"""P3: publiczny link prezentacji — token w adresie, wygasanie, wyłączanie, zakres jak Podgląd, bez edytora."""
from datetime import timedelta

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from scenario.models import Showcase
from scenario.tests import test_showcase as base     # moduł, nie klasa — inaczej runner powtórzy testy bazowe


class PublicLinkTests(TestCase):
    setUpTestData = classmethod(base.ShowcaseViewTests.setUpTestData.__func__)
    setUp = base.ShowcaseViewTests.setUp
    _create = base.ShowcaseViewTests._create

    def _shared(self, days=14):
        _, sc = self._create()
        self.client.post(reverse("scenario:showcase_share", args=[sc.pk]), {"days": days})
        sc.refresh_from_db()
        return sc

    def test_anonymous_plays_read_only(self):
        sc = self._shared(7)
        self.assertGreaterEqual(len(sc.share_token), 32)
        self.assertAlmostEqual(sc.share_expires - timezone.now(), timedelta(days=7), delta=timedelta(minutes=1))
        self.assertContains(self.client.get(reverse("scenario:showcase", args=[sc.pk])), sc.share_token)
        self.client.logout()
        page = self.client.get(reverse("scenario:public", args=[sc.share_token]))
        self.assertContains(page, 'id="sh-canvas"')
        self.assertNotContains(page, 'id="sh-list"')                        # bez edytora
        self.assertNotContains(page, reverse("scenario:showcase_list"))     # bez linków do części dla zalogowanych
        self.assertEqual(page["X-Robots-Tag"], "noindex, nofollow")
        self.assertEqual(page["Referrer-Policy"], "no-referrer")
        data = self.client.get(reverse("scenario:public_data", args=[sc.share_token]))
        self.assertEqual(data.json()["slides"], sc.slides)
        self.assertNotIn("materials", data.content.decode())
        ev = self.client.get(reverse("scenario:public_events", args=[sc.share_token]))
        self.assertEqual(ev.json()["format"], "twinema.scenario-events")
        # pozostałe adresy dalej wymagają logowania
        for url in (reverse("scenario:showcase", args=[sc.pk]), reverse("scenario:showcase_data", args=[sc.pk]),
                    reverse("scenario:run_events", args=[self.run.pk])):
            self.assertNotEqual(self.client.get(url).status_code, 200)

    def test_designer_on_public_url_sees_show_only(self):
        sc = self._shared()
        self.assertNotContains(self.client.get(reverse("scenario:public", args=[sc.share_token])), 'id="sh-list"')

    def test_expired_disabled_regenerated_and_unknown_give_404(self):
        sc = self._shared()
        old = sc.share_token
        self.client.post(reverse("scenario:showcase_share", args=[sc.pk]), {"days": 30})
        sc.refresh_from_db()
        self.assertNotEqual(sc.share_token, old)
        self.client.logout()
        for token in (old, "x" * 32):
            self.assertEqual(self.client.get(reverse("scenario:public", args=[token])).status_code, 404)
        Showcase.objects.filter(pk=sc.pk).update(share_expires=timezone.now() - timedelta(seconds=1))
        for name in ("public", "public_data", "public_events"):
            self.assertEqual(self.client.get(reverse(f"scenario:{name}", args=[sc.share_token])).status_code, 404)
        self.client.force_login(self.designer)
        self._shared()
        sc = Showcase.objects.order_by("-pk").first()
        self.client.post(reverse("scenario:showcase_unshare", args=[sc.pk]))
        sc.refresh_from_db()
        self.assertIsNone(sc.share_token)

    def test_only_designer_shares_and_days_validated(self):
        _, sc = self._create()
        self.client.post(reverse("scenario:showcase_share", args=[sc.pk]), {"days": 365})
        sc.refresh_from_db()
        self.assertIsNone(sc.share_token)
        self.client.force_login(self.viewer)
        for name in ("showcase_share", "showcase_unshare"):
            self.assertEqual(self.client.post(reverse(f"scenario:{name}", args=[sc.pk]), {"days": 7}).status_code, 403)
