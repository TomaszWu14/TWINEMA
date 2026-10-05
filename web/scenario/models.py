"""Scenariusz: założenia wolumenów niezależne od layoutu (ten sam scenariusz testuje różne hale).

Dzień typowy i szczytowy mają własne plany przyjęć; normy wydajności są wspólne dla scenariusza.
Wartości domyślne są syntetyczne (rząd wielkości z praktyki, bez danych firm).
Kolejne kawałki (wydania, paczki, zwroty, cross-dock, obsada) dołożą strumienie do `ScenarioDay`.
"""
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models

from .inbound import day_demand

INBOUND_KINDS = [("container40", "Kontener 40' luzem"), ("truck33", "Auto 33-paletowe"), ("solo", "Solówka / bus")]
# (przyjazdy min/śr/max, palet na przyjazd min/śr/max, okno od–do h, % mono-SKU, % kontroli, min kontroli)
INBOUND_DEFAULTS = {
    "container40": ((6, 8, 10), (38, 45, 52), (6, 14), 100, 10, 2.0),
    "truck33": ((6, 8, 10), (17, 26, 32), (8, 18), 75, 20, 2.0),
    "solo": ((3, 5, 8), (6, 12, 18), (7, 15), 60, 30, 2.0),
}


class Scenario(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nazwa")
    description = models.TextField(blank=True, verbose_name="Opis")
    growth = models.FloatField(default=1.0, verbose_name="Mnożnik wzrostu",
                               help_text="Np. 1,3 = wolumeny +30 % (więcej przyjazdów).")
    seed = models.PositiveIntegerField(default=42, verbose_name="Ziarno losowania")
    shift_h = models.FloatField(default=8.0, verbose_name="Długość zmiany [h]")
    # normy wydajności (przyjęcia)
    container_cartons_per_h = models.FloatField(default=500, verbose_name="Rozładunek kontenera: kartonów/h na osobę")
    container_people = models.PositiveSmallIntegerField(default=2, verbose_name="Osób przy kontenerze")
    cartons_per_pallet = models.FloatField(default=40, verbose_name="Średnio kartonów na paletę (z kontenera)")
    truck_min_per_pallet = models.FloatField(default=1.5, verbose_name="Rozładunek auta: min na paletę")
    palletize_cartons_per_h = models.FloatField(default=360, verbose_name="Paletyzacja ręczna: kartonów/h na osobę")
    repack_min_per_pallet = models.FloatField(default=15, verbose_name="Przepakowanie palety mieszanej: min")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    NORM_FIELDS = ["container_cartons_per_h", "container_people", "cartons_per_pallet", "truck_min_per_pallet",
                   "palletize_cartons_per_h", "repack_min_per_pallet"]

    class Meta:
        ordering = ["-updated_at", "-pk"]
        verbose_name = "Scenariusz"
        verbose_name_plural = "Scenariusze"

    def __str__(self):
        return self.name

    def clean(self):
        if self.growth <= 0 or self.shift_h <= 0:
            raise ValidationError("Mnożnik wzrostu i długość zmiany muszą być dodatnie.")
        if any((getattr(self, f) or 0) <= 0 for f in self.NORM_FIELDS):
            raise ValidationError("Normy wydajności muszą być dodatnie.")

    @property
    def norms(self):
        return {f: getattr(self, f) for f in self.NORM_FIELDS}

    def ensure_days(self, with_defaults=True):
        """Dzień typowy i szczytowy; nowe dostają domyślne strumienie (szczyt: przyjazdy ×1,3)."""
        for kind, _ in ScenarioDay.KIND_CHOICES:
            day, created = ScenarioDay.objects.get_or_create(scenario=self, kind=kind)
            if created and with_defaults:
                k = 1.3 if kind == "peak" else 1.0
                for stream_kind, (arr, pal, win, mono, insp, insp_min) in INBOUND_DEFAULTS.items():
                    InboundStream.objects.create(
                        day=day, kind=stream_kind,
                        arrivals_min=round(arr[0] * k), arrivals_avg=round(arr[1] * k), arrivals_max=round(arr[2] * k),
                        pallets_min=pal[0], pallets_avg=pal[1], pallets_max=pal[2],
                        window_from=win[0], window_to=win[1], mono_pct=mono, inspect_pct=insp, inspect_min=insp_min)


class ScenarioDay(models.Model):
    KIND_CHOICES = [("typical", "Dzień typowy"), ("peak", "Dzień szczytowy")]
    scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE, related_name="days")
    kind = models.CharField(max_length=8, choices=KIND_CHOICES)

    class Meta:
        ordering = ["scenario", "-kind"]           # typical przed peak
        constraints = [models.UniqueConstraint(fields=["scenario", "kind"], name="scenario_day_unique")]

    def __str__(self):
        return f"{self.scenario} — {self.get_kind_display()}"

    def demand(self, level):
        streams = [s.as_dict() for s in self.inbound.all()]
        sc = self.scenario
        return day_demand(streams, sc.norms, growth=sc.growth, level=level, shift_h=sc.shift_h)


class InboundStream(models.Model):
    day = models.ForeignKey(ScenarioDay, on_delete=models.CASCADE, related_name="inbound")
    kind = models.CharField(max_length=12, choices=INBOUND_KINDS, verbose_name="Typ dostawy")
    arrivals_min = models.FloatField(default=0, verbose_name="Przyjazdów min")
    arrivals_avg = models.FloatField(default=0, verbose_name="Przyjazdów śr.")
    arrivals_max = models.FloatField(default=0, verbose_name="Przyjazdów max")
    pallets_min = models.FloatField(default=0, verbose_name="Palet na przyjazd min")
    pallets_avg = models.FloatField(default=0, verbose_name="Palet na przyjazd śr.")
    pallets_max = models.FloatField(default=0, verbose_name="Palet na przyjazd max")
    window_from = models.FloatField(default=6, verbose_name="Okno awizacji od [h]")
    window_to = models.FloatField(default=14, verbose_name="Okno awizacji do [h]")
    mono_pct = models.FloatField(default=100, verbose_name="% palet mono-SKU")
    inspect_pct = models.FloatField(default=10, verbose_name="% palet do kontroli")
    inspect_min = models.FloatField(default=2, verbose_name="Kontrola: min na paletę")

    class Meta:
        ordering = ["day", "pk"]
        verbose_name = "Strumień przyjęć"
        verbose_name_plural = "Strumienie przyjęć"

    def clean(self):
        errors = []
        for name, label in (("arrivals", "przyjazdów"), ("pallets", "palet na przyjazd")):
            lo, mid, hi = (getattr(self, f"{name}_{x}") for x in ("min", "avg", "max"))
            if None in (lo, mid, hi) or not 0 <= lo <= mid <= hi:
                errors.append(f"Liczba {label}: musi być 0 ≤ min ≤ śr. ≤ max.")
        if not 0 <= (self.window_from or 0) < (self.window_to or 0) <= 24:
            errors.append("Okno awizacji: od < do, w granicach 0–24 h.")
        for f, label in (("mono_pct", "% mono-SKU"), ("inspect_pct", "% kontroli")):
            if not 0 <= (getattr(self, f) or 0) <= 100:
                errors.append(f"{label}: 0–100.")
        if (self.inspect_min or 0) < 0:
            errors.append("Czas kontroli nie może być ujemny.")
        if errors:
            raise ValidationError(errors)

    def as_dict(self):
        return {"kind": self.kind, "arrivals": (self.arrivals_min, self.arrivals_avg, self.arrivals_max),
                "pallets": (self.pallets_min, self.pallets_avg, self.pallets_max),
                "window": (self.window_from, self.window_to), "mono_pct": self.mono_pct,
                "inspect_pct": self.inspect_pct, "inspect_min": self.inspect_min}
