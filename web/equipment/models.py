"""Katalog sprzętu (K1): klasy systemowe (anonimowe, z migracji) i własne modele użytkownika.

Osobna aplikacja, bo katalog zasila dwa moduły: layout hali (`twin` — alejka, wysokość, udźwig) i symulację
scenariusza (`scenario` — czas ruchu palety, bateria). Sam niczego nie importuje z tamtych.
"""
from django.conf import settings
from django.db import models

from .catalog import KINDS, RACK_CATEGORY

PARAM_FIELDS = ["speed_loaded_kmh", "speed_empty_kmh", "lift_speed_ms", "lower_speed_ms", "max_lift_m",
                "capacity_kg", "lift_curve", "aisle_m", "pick_s", "drop_s", "battery_h", "charge_h",
                "turn_radius_m", "length_m", "width_m", "throughput_h"]


class Equipment(models.Model):
    kind = models.CharField(max_length=16, choices=KINDS, verbose_name="Typ")
    name = models.CharField(max_length=120, verbose_name="Nazwa")
    is_system = models.BooleanField(default=False, editable=False, verbose_name="Klasa systemowa")
    speed_loaded_kmh = models.FloatField(verbose_name="Jazda z ładunkiem [km/h]")
    speed_empty_kmh = models.FloatField(verbose_name="Jazda bez ładunku [km/h]")
    lift_speed_ms = models.FloatField(null=True, blank=True, verbose_name="Podnoszenie [m/s]")
    lower_speed_ms = models.FloatField(null=True, blank=True, verbose_name="Opuszczanie [m/s]")
    max_lift_m = models.FloatField(null=True, blank=True, verbose_name="Maks. wysokość podnoszenia [m]")
    capacity_kg = models.PositiveIntegerField(verbose_name="Udźwig nominalny [kg]")
    lift_curve = models.JSONField(default=list, blank=True, verbose_name="Redukcja udźwigu",
                                  help_text="Punkty [wysokość m, udźwig kg], np. [[6, 1600], [10, 1000]].")
    aisle_m = models.FloatField(null=True, blank=True, verbose_name="Wymagana alejka robocza Ast [m]")
    pick_s = models.FloatField(null=True, blank=True, verbose_name="Pobranie palety [s]")
    drop_s = models.FloatField(null=True, blank=True, verbose_name="Odłożenie palety [s]")
    battery_h = models.FloatField(null=True, blank=True, verbose_name="Praca na baterii [h]")
    charge_h = models.FloatField(null=True, blank=True, verbose_name="Ładowanie / wymiana [h]")
    turn_radius_m = models.FloatField(null=True, blank=True, verbose_name="Promień skrętu [m]")
    length_m = models.FloatField(null=True, blank=True, verbose_name="Długość [m]")
    width_m = models.FloatField(null=True, blank=True, verbose_name="Szerokość [m]")
    throughput_h = models.PositiveIntegerField(null=True, blank=True, verbose_name="Wydajność nominalna [szt./h]")
    # pod przyszły CAPEX/OPEX (UI kosztów później)
    cost_purchase = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True,
                                        verbose_name="Koszt zakupu [zł]")
    cost_per_hour = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True,
                                        verbose_name="Koszt godziny pracy [zł]")
    notes = models.TextField(blank=True, verbose_name="Uwagi")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["kind", "-is_system", "name"]
        verbose_name = "Sprzęt"
        verbose_name_plural = "Katalog sprzętu"

    def __str__(self):
        return self.name

    @property
    def rack_category(self):
        return RACK_CATEGORY.get(self.kind)

    def params(self):
        return {f: getattr(self, f) for f in PARAM_FIELDS} | {"id": self.pk, "kind": self.kind, "name": self.name}
