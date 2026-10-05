"""Studio prezentacji: film o modelu hali składany z ujęć (preset kamery + kwestia lektora).

Statusy idą tylko do przodu: szkic → tekst zatwierdzony → audio → render → montaż → gotowe.
Kwestie wolno edytować wyłącznie w szkicu — nic nie idzie do lektora ani renderu przed akceptacją.
"""
import math
import secrets

from django.conf import settings
from django.db import models

from render.models import RenderJob

from .script import estimate_seconds
from .voice import voice_key


class Presentation(models.Model):
    STATUS_CHOICES = [
        ("draft", "Szkic"),
        ("approved", "Tekst zatwierdzony"),
        ("audio", "Lektor"),
        ("render", "Render ujęć"),
        ("montage", "Montaż"),
        ("done", "Gotowe"),
    ]

    model = models.ForeignKey("twin.WarehouseModel", on_delete=models.CASCADE, related_name="presentations",
                              verbose_name="Model hali")
    title = models.CharField(max_length=200, verbose_name="Tytuł filmu")
    voice_id = models.CharField(max_length=64, blank=True, default="", verbose_name="Głos lektora (voice_id)",
                                help_text="Puste = domyślny głos z ELEVENLABS_VOICE_ID.")
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default="draft", db_index=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    approved_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-updated_at", "-pk"]
        verbose_name = "Prezentacja"
        verbose_name_plural = "Prezentacje"

    def __str__(self):
        return self.title

    @property
    def is_draft(self):
        return self.status == "draft"

    @property
    def estimated_seconds(self):
        return round(sum(estimate_seconds(s.text) for s in self.shots.all()))

    @property
    def effective_voice(self):
        return self.voice_id or settings.ELEVENLABS_VOICE_ID

    def all_voiced(self):
        shots = list(self.shots.select_related("voice"))       # shot.presentation = self (cache menedżera)
        return bool(shots) and all(s.voice_ok for s in shots)


class VoiceTrack(models.Model):
    """Nagranie lektora — cache po hashu (tekst + głos + model), współdzielony między ujęciami."""
    key = models.CharField(max_length=64, unique=True)
    voice_id = models.CharField(max_length=64)
    model_id = models.CharField(max_length=64)
    text = models.TextField()
    audio = models.FileField(upload_to="voice/%Y/%m/")
    duration_s = models.FloatField()
    alignment = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Nagranie lektora"
        verbose_name_plural = "Nagrania lektora"

    def __str__(self):
        return f"{self.text[:40]}… ({self.duration_s:.1f} s)"


class Shot(models.Model):
    presentation = models.ForeignKey(Presentation, on_delete=models.CASCADE, related_name="shots")
    order = models.PositiveSmallIntegerField(default=0, verbose_name="Kolejność")
    preset = models.CharField(max_length=12, choices=RenderJob.PRESET_CHOICES, default="ogolny",
                              verbose_name="Ujęcie")
    text = models.TextField(verbose_name="Kwestia lektora")
    voice = models.ForeignKey(VoiceTrack, on_delete=models.SET_NULL, null=True, blank=True, related_name="shots")
    render = models.ForeignKey(RenderJob, on_delete=models.SET_NULL, null=True, blank=True, related_name="studio_shots")
    render_key = models.CharField(max_length=64, blank=True, default="", db_index=True)
    still = models.ForeignKey(RenderJob, on_delete=models.SET_NULL, null=True, blank=True, related_name="studio_stills")
    still_key = models.CharField(max_length=64, blank=True, default="", db_index=True)

    class Meta:
        ordering = ["order", "pk"]
        verbose_name = "Ujęcie prezentacji"
        verbose_name_plural = "Ujęcia prezentacji"

    def __str__(self):
        return f"{self.order}. {self.get_preset_display()}"

    @property
    def estimated_seconds(self):
        return estimate_seconds(self.text)

    @property
    def voice_key(self):
        return voice_key(self.text, self.presentation.effective_voice, settings.ELEVENLABS_MODEL)

    @property
    def voice_ok(self):
        """Nagranie pasuje do obecnego tekstu i głosu (po poprawce kwestii — nieaktualne)."""
        return self.voice is not None and self.voice.key == self.voice_key

    @property
    def render_seconds(self):
        """Długość klipu: nagranie + zapas 0,5 s, w granicach kolejki renderów (2–60 s)."""
        return min(60, max(2, math.ceil(self.voice.duration_s + 0.5))) if self.voice else None

    @property
    def render_current(self):
        """Render pasuje do obecnego presetu i długości kwestii (stan zlecenia osobno)."""
        r = self.render
        return (r is not None and self.voice_ok and r.preset == self.preset and r.seconds == self.render_seconds
                and r.resolution == RENDER_RESOLUTION)


RENDER_RESOLUTION = "1920x1080"       # film dla zarządu — Full HD; podgląd ujęć i tak jest w kolejce F3


class MontageJob(models.Model):
    """Montaż filmu (ffmpeg w workerze na PC). Cache: ten sam `input_key` i gotowe → bez ponownego montażu."""
    STATUS_CHOICES = RenderJob.STATUS_CHOICES

    presentation = models.ForeignKey(Presentation, on_delete=models.CASCADE, related_name="montages")
    input_key = models.CharField(max_length=64, db_index=True)
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default="queued", db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    claimed_at = models.DateTimeField(null=True, blank=True)
    finished_at = models.DateTimeField(null=True, blank=True)
    worker = models.CharField(max_length=80, blank=True, default="")
    claim_token = models.CharField(max_length=64, blank=True, default="", editable=False)
    result = models.FileField(upload_to="films/%Y/%m/", blank=True)
    log = models.TextField(blank=True, default="")

    class Meta:
        ordering = ["-created_at", "-pk"]
        verbose_name = "Montaż filmu"
        verbose_name_plural = "Montaże filmów"

    def __str__(self):
        return f"Montaż: {self.presentation}"

    def new_claim(self):
        self.claim_token = secrets.token_urlsafe(24)
        return self.claim_token
