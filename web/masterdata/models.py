"""Dane podstawowe bliźniaka: materiały, stany w lokalizacjach i dziennik importów.

Master lokalizacji żyje w `twin` (WarehouseLocationMaster) — tu tylko go importujemy.
Klucze integracji to stringi (kod materiału, kod lokalizacji), bez FK do modelu hali."""
from django.conf import settings
from django.db import models


class ImportLog(models.Model):
    """Jeden import pliku: rodzaj, wynik i próbka odrzuconych wierszy. Import stanów jest
    jednocześnie partią stanów — najnowszy zakończony to aktualny stan magazynu."""
    KIND_CHOICES = [("materials", "Materiały"), ("locations", "Master lokalizacji"), ("stock", "Stany")]
    kind = models.CharField(max_length=12, choices=KIND_CHOICES, verbose_name="Rodzaj")
    name = models.CharField(max_length=200, verbose_name="Nazwa / plik")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    rows_total = models.PositiveIntegerField(default=0)
    rows_ok = models.PositiveIntegerField(default=0)
    rows_rejected = models.PositiveIntegerField(default=0)
    rejects = models.JSONField(default=list, blank=True, verbose_name="Odrzucone (próbka)")
    columns = models.JSONField(default=dict, blank=True, verbose_name="Rozpoznane kolumny")

    class Meta:
        ordering = ["-uploaded_at", "-pk"]
        verbose_name = "Import danych"
        verbose_name_plural = "Importy danych"

    def __str__(self):
        return f"{self.get_kind_display()}: {self.name}"


class Material(models.Model):
    """Materiał (SKU): opakowanie zbiorcze i paletyzacja — wejście do rozmieszczenia i symulacji."""
    code = models.CharField(max_length=40, unique=True, verbose_name="Kod materiału")
    name = models.CharField(max_length=200, blank=True, default="", verbose_name="Nazwa")
    group = models.CharField(max_length=80, blank=True, default="", db_index=True, verbose_name="Grupa towarowa")
    unit = models.CharField(max_length=10, blank=True, default="SZT", verbose_name="Jednostka bazowa")
    pcs_per_carton = models.PositiveIntegerField(null=True, blank=True, verbose_name="Sztuk w kartonie")
    carton_l_cm = models.FloatField(null=True, blank=True, verbose_name="Karton dł. [cm]")
    carton_w_cm = models.FloatField(null=True, blank=True, verbose_name="Karton szer. [cm]")
    carton_h_cm = models.FloatField(null=True, blank=True, verbose_name="Karton wys. [cm]")
    carton_kg = models.FloatField(null=True, blank=True, verbose_name="Karton waga [kg]")
    cartons_per_pallet = models.PositiveIntegerField(null=True, blank=True, verbose_name="Kartonów na palecie")
    pallet_h_cm = models.FloatField(null=True, blank=True, verbose_name="Wys. palety z towarem [cm]")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["code"]
        verbose_name = "Materiał"
        verbose_name_plural = "Materiały"

    def __str__(self):
        return f"{self.code} {self.name}".strip()


class StockItem(models.Model):
    """Pozycja stanu: materiał w lokalizacji (z jednego importu stanów)."""
    log = models.ForeignKey(ImportLog, on_delete=models.CASCADE, related_name="stock_items")
    location_code = models.CharField(max_length=50, db_index=True, verbose_name="Lokalizacja")
    material_code = models.CharField(max_length=40, verbose_name="Materiał")
    qty = models.FloatField(default=0, verbose_name="Ilość")
    unit = models.CharField(max_length=10, blank=True, default="", verbose_name="Jednostka")
    hu = models.CharField(max_length=40, blank=True, default="", verbose_name="Nośnik / HU")
    lot = models.CharField(max_length=40, blank=True, default="", verbose_name="Partia")
    expiry = models.DateField(null=True, blank=True, verbose_name="Data ważności")

    class Meta:
        ordering = ["location_code", "pk"]
        verbose_name = "Pozycja stanu"
        verbose_name_plural = "Stany"
