"""Render ujęć z kolejki F3 (cache po hashu) i montaż przez API workera (token + jednorazowy claim)."""
import shutil
import tempfile

from django.contrib.auth.models import Group, User
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings
from django.urls import reverse

from core.roles import GROUP_DESIGNER, GROUP_VIEWER
from render.models import RenderJob
from studio.models import MontageJob, Presentation, Shot, VoiceTrack
from twin.models import WarehouseModel

TOKEN = "t" * 40
MP4 = b"\x00\x00\x00\x18ftypmp42" + b"\x00" * 64
MEDIA = tempfile.mkdtemp(prefix="twinema_test_montage_")


def _voice(text, seconds):
    n = len(text)
    vt = VoiceTrack(key="", voice_id="g", model_id="m", text=text, duration_s=seconds, alignment={
        "characters": list(text), "character_start_times_seconds": [i * seconds / n for i in range(n)],
        "character_end_times_seconds": [(i + 1) * seconds / n for i in range(n)]})
    return vt


@override_settings(MEDIA_ROOT=MEDIA, RENDER_WORKER_TOKEN=TOKEN, APP_NAME="TWINEMA")
class RenderMontageTests(TestCase):
    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        shutil.rmtree(MEDIA, ignore_errors=True)

    def setUp(self):
        self.wm = WarehouseModel.objects.create(name="Hala", floor_width_m=30, floor_depth_m=20)
        self.wm.racks.create(zone="V", rack_id="001", n_bays=4, n_levels=3, x_m=4, y_m=4)
        self.user = User.objects.create_user("proj", password="x")
        self.user.groups.add(Group.objects.create(name=GROUP_DESIGNER))
        self.client.force_login(self.user)
        self.p = Presentation.objects.create(model=self.wm, title="Film", status="audio", voice_id="lektor-testowy")
        for i, (preset, text, sec) in enumerate([("przelot", "Pierwsza kwestia.", 4.2), ("plan", "Druga.", 1.0)]):
            shot = Shot.objects.create(presentation=self.p, order=i, preset=preset, text=text)
            vt = _voice(text, sec)
            vt.key = shot.voice_key
            vt.audio.save(f"a{i}.mp3", ContentFile(b"ID3audio"))
            shot.voice = vt
            shot.save()

    def _render(self):
        return self.client.post(reverse("studio:render_shots", args=[self.p.pk]))

    def _finish_renders(self):
        for job in RenderJob.objects.all():
            job.result.save(f"r{job.pk}.mp4", ContentFile(MP4), save=False)
            job.status = "done"
            job.save()

    def test_render_creates_jobs_with_voice_length_and_status(self):
        self._render()
        jobs = list(RenderJob.objects.order_by("pk"))
        self.assertEqual([(j.preset, j.kind, j.resolution, j.seconds) for j in jobs],
                         [("przelot", "video", "1920x1080", 5), ("plan", "video", "1920x1080", 2)])
        self.assertEqual(jobs[0].title, "Film — ujęcie 1")
        self.p.refresh_from_db()
        self.assertEqual(self.p.status, "render")

    def test_render_cache_same_scene_preset_length(self):
        self._render()
        self._render()                                        # drugi klik — nic nowego
        self.assertEqual(RenderJob.objects.count(), 2)
        other = Presentation.objects.create(model=self.wm, title="Inny film", status="audio", voice_id="lektor-testowy")
        s = self.p.shots.first()
        copy = Shot.objects.create(presentation=other, order=0, preset=s.preset, text=s.text, voice=s.voice)
        self.client.post(reverse("studio:render_shots", args=[other.pk]))
        copy.refresh_from_db()
        self.assertEqual(copy.render_id, s.render_id)         # ten sam render z innej prezentacji
        self.assertEqual(RenderJob.objects.count(), 2)

    def test_preset_change_needs_new_render(self):
        self._render()
        Shot.objects.filter(preset="plan").update(preset="orbita")
        self._render()
        self.assertEqual(RenderJob.objects.count(), 3)

    def test_render_blocked_without_voice(self):
        Shot.objects.update(voice=None)
        self._render()
        self.assertFalse(RenderJob.objects.exists())

    def test_viewer_cannot_render_or_montage(self):
        viewer = User.objects.create_user("zarzad", password="x")
        viewer.groups.add(Group.objects.create(name=GROUP_VIEWER))
        self.client.force_login(viewer)
        self.assertEqual(self._render().status_code, 403)
        self.assertEqual(self.client.post(reverse("studio:montage_create", args=[self.p.pk])).status_code, 403)

    def test_montage_waits_for_renders_then_queues_once(self):
        self._render()
        self.client.post(reverse("studio:montage_create", args=[self.p.pk]))
        self.assertFalse(MontageJob.objects.exists())
        self._finish_renders()
        self.client.post(reverse("studio:montage_create", args=[self.p.pk]))
        self.client.post(reverse("studio:montage_create", args=[self.p.pk]))
        self.assertEqual(MontageJob.objects.count(), 1)
        self.p.refresh_from_db()
        self.assertEqual(self.p.status, "montage")
        self.assertContains(self.client.get(reverse("studio:detail", args=[self.p.pk])), "Czeka na worker z ffmpeg")

    def _queued_montage(self):
        self._render()
        self._finish_renders()
        self.client.post(reverse("studio:montage_create", args=[self.p.pk]))
        return MontageJob.objects.get()

    def _api(self, name, *args, method="post", claim="", token=TOKEN, **data):
        return getattr(self.client, method)(reverse(name, args=args), data, HTTP_X_WORKER_TOKEN=token,
                                            HTTP_X_CLAIM=claim)

    def test_worker_flow_manifest_files_result(self):
        job = self._queued_montage()
        self.assertEqual(self._api("studio:api_claim", token="zly" * 12).status_code, 403)
        man = self._api("studio:api_claim", worker="pc").json()
        self.assertEqual((man["id"], man["resolution"], man["title_s"]), (job.pk, "1920x1080", 3.0))
        self.assertEqual([s["duration"] for s in man["shots"]], [4.2, 1.0])
        self.assertTrue(man["srt"].startswith("1\n00:00:03,000 --> "))          # przesunięte o planszę
        self.assertEqual(self._api("studio:api_claim").status_code, 204)        # jeden worker naraz
        claim = man["claim"]
        self.assertEqual(self._api("studio:api_clip", job.pk, 0, method="get", claim="inny").status_code, 403)
        clip = self._api("studio:api_clip", job.pk, 0, method="get", claim=claim)
        self.assertEqual(b"".join(clip.streaming_content), MP4)
        audio = self._api("studio:api_audio", job.pk, 1, method="get", claim=claim)
        self.assertEqual(b"".join(audio.streaming_content), b"ID3audio")
        self.assertEqual(self._api("studio:api_clip", job.pk, 5, method="get", claim=claim).status_code, 404)
        bad = self._api("studio:api_result", job.pk, claim=claim, file=SimpleUploadedFile("f.mp4", b"nie-mp4" * 4))
        self.assertEqual(bad.status_code, 400)
        ok = self._api("studio:api_result", job.pk, claim=claim, file=SimpleUploadedFile("f.mp4", MP4), log="ok")
        self.assertEqual(ok.status_code, 200)
        job.refresh_from_db()
        self.p.refresh_from_db()
        self.assertEqual((job.status, self.p.status), ("done", "done"))
        page = self.client.get(reverse("studio:detail", args=[self.p.pk]))
        self.assertContains(page, reverse("studio:film_file", args=[job.pk]))
        self.assertEqual(self.client.get(reverse("studio:film_file", args=[job.pk]))["Content-Type"], "video/mp4")
        self.client.post(reverse("studio:montage_create", args=[self.p.pk]))   # ten sam materiał — cache
        self.assertEqual(MontageJob.objects.count(), 1)

    def test_worker_fail_shows_log_and_allows_retry(self):
        job = self._queued_montage()
        claim = self._api("studio:api_claim").json()["claim"]
        self._api("studio:api_fail", job.pk, claim=claim, error="ffmpeg: brak kodeka")
        page = self.client.get(reverse("studio:detail", args=[self.p.pk]))
        self.assertContains(page, "ffmpeg: brak kodeka")
        self.assertContains(page, "Zmontuj ponownie")
        self.client.post(reverse("studio:montage_create", args=[self.p.pk]))
        self.assertEqual(MontageJob.objects.filter(status="queued").count(), 1)

    def test_status_json(self):
        self._render()
        d = self.client.get(reverse("studio:status_json", args=[self.p.pk])).json()
        self.assertTrue(d["active"])
        self.assertEqual(d["state"], "render|queued,queued|")
