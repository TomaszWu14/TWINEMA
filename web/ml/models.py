"""Przebiegi modeli ML: wersja algorytmu, dane wejściowe, parametry, miary i wynik — każdy
przebieg jest zapisem, który da się otworzyć i porównać później (bez ponownego liczenia)."""
from django.conf import settings
from django.db import models


class ModelRun(models.Model):
    KIND_CHOICES = [("forecast", "Prognoza wolumenów"), ("segmentation", "Segmentacja materiałów")]
    kind = models.CharField(max_length=14, choices=KIND_CHOICES, verbose_name="Rodzaj")
    batch = models.ForeignKey("twin.WarehouseTaskBatch", on_delete=models.CASCADE, related_name="ml_runs",
                              verbose_name="Import zadań")
    version = models.CharField(max_length=40, verbose_name="Wersja algorytmu")
    params = models.JSONField(default=dict, verbose_name="Parametry")
    metrics = models.JSONField(default=dict, verbose_name="Miary")
    result = models.JSONField(default=dict, verbose_name="Wynik")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at", "-pk"]
        verbose_name = "Przebieg modelu"
        verbose_name_plural = "Przebiegi modeli"

    def __str__(self):
        return f"{self.get_kind_display()} #{self.pk} ({self.batch})"
