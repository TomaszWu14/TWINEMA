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


class Carrier(models.Model):
    """Nośnik (paleta): EUR 120×80 domyślnie, reszta edytowalna."""
    name = models.CharField(max_length=60, unique=True, verbose_name="Nazwa")
    length_cm = models.FloatField(verbose_name="Długość [cm]")
    width_cm = models.FloatField(verbose_name="Szerokość [cm]")
    height_cm = models.FloatField(default=14.4, verbose_name="Wysokość własna [cm]")
    weight_kg = models.FloatField(default=25, verbose_name="Waga własna [kg]")
    max_load_h_cm = models.FloatField(default=180, verbose_name="Max wysokość ładunku [cm]")
    max_load_kg = models.FloatField(default=1000, verbose_name="Max waga ładunku [kg]")
    is_default = models.BooleanField(default=False, verbose_name="Domyślny")

    class Meta:
        ordering = ["-is_default", "name"]
        verbose_name = "Nośnik"
        verbose_name_plural = "Nośniki"

    def __str__(self):
        return self.name

    def as_dict(self):
        return {"name": self.name, "length_cm": self.length_cm, "width_cm": self.width_cm,
                "height_cm": self.height_cm, "weight_kg": self.weight_kg,
                "max_load_h_cm": self.max_load_h_cm, "max_load_kg": self.max_load_kg}


class PalletClass(models.Model):
    """Klasa wysokości albo wagi palety z towarem (np. do 1,4 m / do 600 kg) — do ostrzeżeń nośności w S3."""
    KIND_CHOICES = [("height", "Wysokość [cm]"), ("weight", "Waga [kg]")]
    kind = models.CharField(max_length=6, choices=KIND_CHOICES, verbose_name="Rodzaj")
    label = models.CharField(max_length=30, verbose_name="Nazwa klasy")
    limit = models.FloatField(verbose_name="Do (włącznie)")

    class Meta:
        ordering = ["kind", "limit"]
        unique_together = [("kind", "label")]
        verbose_name = "Klasa palety"
        verbose_name_plural = "Klasy palet"

    def __str__(self):
        return self.label


SPECIAL_FLAGS = [("temp_controlled", "Temperatura kontrolowana"), ("adr", "ADR / niebezpieczny"),
                 ("oversize", "Gabaryt / dłużyca"), ("high_value", "Wysoka wartość")]


class Material(models.Model):
    """Materiał (SKU): hierarchia sztuka → karton → paleta, nośnik, klasy, ABC i strefy specjalne —
    wejście do rozmieszczenia i symulacji. Przeliczenia w `packaging.py`."""
    ABC_CHOICES = [("", "z historii"), ("A", "A"), ("B", "B"), ("C", "C")]

    code = models.CharField(max_length=40, unique=True, verbose_name="Kod materiału")
    name = models.CharField(max_length=200, blank=True, default="", verbose_name="Nazwa")
    group = models.CharField(max_length=80, blank=True, default="", db_index=True, verbose_name="Grupa towarowa")
    unit = models.CharField(max_length=10, blank=True, default="SZT", verbose_name="Jednostka bazowa")
    piece_l_cm = models.FloatField(null=True, blank=True, verbose_name="Sztuka dł. [cm]")
    piece_w_cm = models.FloatField(null=True, blank=True, verbose_name="Sztuka szer. [cm]")
    piece_h_cm = models.FloatField(null=True, blank=True, verbose_name="Sztuka wys. [cm]")
    piece_kg = models.FloatField(null=True, blank=True, verbose_name="Sztuka waga [kg]")
    pcs_per_carton = models.PositiveIntegerField(null=True, blank=True, verbose_name="Sztuk w kartonie")
    carton_l_cm = models.FloatField(null=True, blank=True, verbose_name="Karton dł. [cm]")
    carton_w_cm = models.FloatField(null=True, blank=True, verbose_name="Karton szer. [cm]")
    carton_h_cm = models.FloatField(null=True, blank=True, verbose_name="Karton wys. [cm]")
    carton_kg = models.FloatField(null=True, blank=True, verbose_name="Karton waga [kg]")
    cartons_per_layer = models.PositiveIntegerField(null=True, blank=True, verbose_name="Kartonów na warstwę")
    layers_per_pallet = models.PositiveIntegerField(null=True, blank=True, verbose_name="Warstw na palecie")
    cartons_per_pallet = models.PositiveIntegerField(null=True, blank=True, verbose_name="Kartonów na palecie")
    pallet_h_cm = models.FloatField(null=True, blank=True, verbose_name="Wys. palety z towarem [cm]")
    carrier = models.ForeignKey(Carrier, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Nośnik")
    height_class = models.ForeignKey(PalletClass, on_delete=models.SET_NULL, null=True, blank=True,
                                     related_name="+", limit_choices_to={"kind": "height"},
                                     verbose_name="Klasa wysokości")
    weight_class = models.ForeignKey(PalletClass, on_delete=models.SET_NULL, null=True, blank=True,
                                     related_name="+", limit_choices_to={"kind": "weight"},
                                     verbose_name="Klasa wagi")
    abc_manual = models.CharField(max_length=1, blank=True, default="", choices=ABC_CHOICES,
                                  verbose_name="Klasa ABC (ręcznie)")
    temp_controlled = models.BooleanField(default=False, verbose_name="Temperatura kontrolowana")
    adr = models.BooleanField(default=False, verbose_name="ADR / niebezpieczny")
    oversize = models.BooleanField(default=False, verbose_name="Gabaryt / dłużyca")
    high_value = models.BooleanField(default=False, verbose_name="Wysoka wartość")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["code"]
        verbose_name = "Materiał"
        verbose_name_plural = "Materiały"

    def __str__(self):
        return f"{self.code} {self.name}".strip()

    def as_dict(self):
        return {f.attname: getattr(self, f.attname) for f in self._meta.concrete_fields}

    @property
    def flags(self):
        return [label for f, label in SPECIAL_FLAGS if getattr(self, f)]


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
