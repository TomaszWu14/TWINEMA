"""Scenariusz referencyjny (syntetyczny, anonimowy): centrum dystrybucyjne z importem kontenerowym.

Dzień typowy: ~8 kontenerów 40' (≈45 palet po paletyzacji), 6–10 aut 33-paletowych (fizycznie 17–32 palet),
solówki/busy. Dzień szczytowy: przyjazdy ×1,3. Idempotentnie — ponowne uruchomienie odtwarza plan.
"""
from django.core.management.base import BaseCommand
from django.db import transaction

from scenario.models import InboundStream, Scenario, ScenarioDay

NAME = "Centrum dystrybucyjne — rok bazowy (demo)"
PEAK = 1.3
# typ: (przyjazdy min/śr/max, palet min/śr/max, okno, % mono, % kontroli, min kontroli)
PLAN = {
    "container40": ((7, 8, 9), (38, 45, 52), (6, 14), 100, 10, 2.0),
    "truck33": ((6, 8, 10), (17, 26, 32), (8, 18), 75, 20, 2.0),
    "solo": ((4, 6, 8), (6, 12, 18), (7, 15), 60, 30, 2.0),
}


class Command(BaseCommand):
    help = "Scenariusz demo: import kontenerowy + auta 33-paletowe + solówki (dzień typowy i szczytowy ×1,3)."

    @transaction.atomic
    def handle(self, *args, **opts):
        sc, _ = Scenario.objects.update_or_create(name=NAME, defaults={
            "description": "Dane syntetyczne. Szczyt = przyjazdy ×1,3 (sezon).", "growth": 1.0, "seed": 42})
        for kind, k in (("typical", 1.0), ("peak", PEAK)):
            day, _ = ScenarioDay.objects.get_or_create(scenario=sc, kind=kind)
            day.inbound.all().delete()
            for stream, (arr, pal, win, mono, insp, insp_min) in PLAN.items():
                InboundStream.objects.create(
                    day=day, kind=stream, arrivals_min=round(arr[0] * k), arrivals_avg=round(arr[1] * k),
                    arrivals_max=round(arr[2] * k), pallets_min=pal[0], pallets_avg=pal[1], pallets_max=pal[2],
                    window_from=win[0], window_to=win[1], mono_pct=mono, inspect_pct=insp, inspect_min=insp_min)
        for day in sc.days.all():
            d = day.demand("avg")
            self.stdout.write(f"{day.get_kind_display()}: {d['pallets_in']} palet, doki w szczycie "
                              f"{d['docks_peak']['container']} kont. + {d['docks_peak']['pallet']} pal., "
                              f"{d['person_hours']['total']} osobogodzin")
        self.stdout.write(self.style.SUCCESS(f"Scenariusz „{sc}” gotowy (id {sc.pk})."))
