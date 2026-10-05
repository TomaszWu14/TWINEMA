"""API workera dla montażu filmu — ten sam token (RENDER_WORKER_TOKEN) i ten sam wzorzec jednorazowego
przejęcia co kolejka renderów (render/api.py). Pliki ujęć i nagrań tylko z X-Worker-Token + X-Claim.

  POST /api/studio/montage/claim/                  → 200 manifest (JSON) albo 204
  GET  /api/studio/montage/<id>/clip/<n>/           → MP4 ujęcia n (0…)
  GET  /api/studio/montage/<id>/audio/<n>/          → MP3 kwestii n
  POST /api/studio/montage/<id>/result/             → multipart: file (MP4), log
  POST /api/studio/montage/<id>/fail/               → error (tekst)
"""
import hmac
from datetime import timedelta

from django.conf import settings
from django.core.files.base import File
from django.db import transaction
from django.http import FileResponse, Http404, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.http import require_GET, require_POST

from render.api import LOG_MAX, SIGNATURES, _forbidden, worker_required

from .models import RENDER_RESOLUTION, MontageJob

TITLE_S, END_S = 3.0, 3.0


def _claimed(request, pk):
    job = get_object_or_404(MontageJob.objects.select_related("presentation"), pk=pk)
    claim = request.headers.get("X-Claim", "")
    if job.status != "running" or not job.claim_token or not hmac.compare_digest(
            job.claim_token.encode(), claim.encode()):
        return None
    return job


def _shots(job):
    return list(job.presentation.shots.select_related("voice", "render"))


def manifest(request, job):
    from .views import film_srt

    shots = _shots(job)
    url = request.build_absolute_uri
    return {
        "id": job.pk, "claim": job.claim_token, "title": job.presentation.title, "subtitle": settings.APP_NAME,
        "end_title": settings.APP_NAME, "resolution": RENDER_RESOLUTION, "title_s": TITLE_S, "end_s": END_S,
        "srt": film_srt(shots, start_s=TITLE_S),
        "shots": [{"duration": s.voice.duration_s,
                   "clip_url": url(reverse("studio:api_clip", args=[job.pk, i])),
                   "audio_url": url(reverse("studio:api_audio", args=[job.pk, i]))} for i, s in enumerate(shots)],
        "result_url": url(reverse("studio:api_result", args=[job.pk])),
        "fail_url": url(reverse("studio:api_fail", args=[job.pk])),
    }


@worker_required
@require_POST
def claim(request):
    limit = timezone.now() - timedelta(minutes=settings.RENDER_STALE_MIN)
    MontageJob.objects.filter(status="running", claimed_at__lt=limit).update(
        status="queued", claim_token="", log="Wróciło do kolejki: worker nie odesłał wyniku w czasie.")
    worker = (request.POST.get("worker") or request.headers.get("User-Agent", ""))[:80]
    for _ in range(5):
        job = MontageJob.objects.filter(status="queued").order_by("created_at", "pk").first()
        if job is None:
            return HttpResponse(status=204)
        token = job.new_claim()
        with transaction.atomic():
            won = MontageJob.objects.filter(pk=job.pk, status="queued").update(
                status="running", claim_token=token, claimed_at=timezone.now(), worker=worker)
        if won:
            return JsonResponse(manifest(request, job), json_dumps_params={"ensure_ascii": False})
    return HttpResponse(status=204)


def _shot_file(request, pk, n, field):
    job = _claimed(request, pk)
    if job is None:
        return _forbidden("Zlecenie nie jest przejęte przez tego workera.")
    shots = _shots(job)
    if not 0 <= n < len(shots):
        raise Http404
    f = shots[n].render.result if field == "clip" else shots[n].voice.audio
    if not f:
        raise Http404
    return FileResponse(f.open("rb"), content_type="video/mp4" if field == "clip" else "audio/mpeg")


@worker_required
@require_GET
def clip(request, pk, n):
    return _shot_file(request, pk, n, "clip")


@worker_required
@require_GET
def audio(request, pk, n):
    return _shot_file(request, pk, n, "audio")


@worker_required
@require_POST
def result(request, pk):
    job = _claimed(request, pk)
    if job is None:
        return _forbidden("Zlecenie nie jest przejęte przez tego workera.")
    f = request.FILES.get("file")
    if f is None:
        return JsonResponse({"error": "Brak pliku."}, status=400)
    if f.size > settings.RENDER_MAX_MB * 1024 * 1024:
        return JsonResponse({"error": f"Plik większy niż {settings.RENDER_MAX_MB} MB."}, status=413)
    head = f.read(16)
    f.seek(0)
    if not SIGNATURES["mp4"](head):
        return JsonResponse({"error": "To nie jest plik MP4."}, status=400)
    job.result.save(f"film_{job.presentation_id}_{job.pk}.mp4", File(f), save=False)
    job.status, job.finished_at, job.claim_token = "done", timezone.now(), ""
    job.log = (request.POST.get("log") or "")[-LOG_MAX:]
    job.save()
    p = job.presentation
    if p.status == "montage":
        p.status = "done"
        p.save(update_fields=["status", "updated_at"])
    return JsonResponse({"ok": True, "id": job.pk})


@worker_required
@require_POST
def fail(request, pk):
    job = _claimed(request, pk)
    if job is None:
        return _forbidden("Zlecenie nie jest przejęte przez tego workera.")
    job.status, job.finished_at, job.claim_token = "error", timezone.now(), ""
    job.log = (request.POST.get("error") or "Błąd montażu bez opisu.")[-LOG_MAX:]
    job.save()
    return JsonResponse({"ok": True})
