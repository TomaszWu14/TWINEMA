"""Scenariusz referencyjny (syntetyczny, anonimowy): centrum dystrybucyjne z importem kontenerowym.

Dzień typowy: ~8 kontenerów 40' (≈45 palet po paletyzacji), 6–10 aut 33-paletowych (fizycznie 17–32 palet),
solówki/busy, cross-dock; wydania autami 33-pal. i solówkami, ~2 200 paczek dziennie z odbiorem kurierów do 18:00,
zwroty. Dzień szczytowy: wolumeny ×1,3. Obsada: 1–2 zmiany per proces. Idempotentnie — ponowne uruchomienie
odtwarza plan.
"""
from django.core.management.base import BaseCommand
from django.db import transaction

from scenario.models import (InboundStream, OutboundStream, PROFILE_DEFAULTS, Scenario, ScenarioDay, Shift,
                             SHIFT_DEFAULTS)

NAME = "Centrum dystrybucyjne — rok bazowy (demo)"
PEAK = 1.3
# typ: (przyjazdy min/śr/max, palet min/śr/max, okno, % mono, % kontroli, min kontroli)
PLAN = {
    "container40": ((7, 8, 9), (38, 45, 52), (6, 14), 100, 10, 2.0),
    "truck33": ((6, 8, 10), (17, 26, 32), (8, 18), 75, 20, 2.0),
    "solo": ((4, 6, 8), (6, 12, 18), (7, 15), 60, 30, 2.0),
    "crossdock": ((2, 3, 4), (20, 26, 32), (6, 12), 100, 0, 0.0),
}
# typ: (wyjazdy min/śr/max, palet min/śr/max, załadunek od–cut-off)
OUT = {
    "truck33": ((14, 18, 22), (24, 28, 32), (12, 20)),
    "solo": ((8, 10, 14), (6, 10, 14), (10, 18)),
    "courier": ((3, 4, 5), (0, 0, 0), (15, 18)),
    "crossdock": ((2, 3, 4), (20, 26, 32), (10, 16)),
}


def _r(v, k):
    return round(v * k)


class Command(BaseCommand):
    help = "Scenariusz demo: przyjęcia, wydania, paczki, zwroty, cross-dock i obsada (dzień typowy i szczyt ×1,3)."

    @transaction.atomic
    def handle(self, *args, **opts):
        sc, _ = Scenario.objects.update_or_create(name=NAME, defaults={
            "description": "Dane syntetyczne. Szczyt = wolumeny ×1,3 (sezon).", "growth": 1.0, "seed": 42})
        for kind, k in (("typical", 1.0), ("peak", PEAK)):
            day, _ = ScenarioDay.objects.get_or_create(scenario=sc, kind=kind)
            day.inbound.all().delete()
            day.outbound.all().delete()
            for stream, (arr, pal, win, mono, insp, insp_min) in PLAN.items():
                InboundStream.objects.create(
                    day=day, kind=stream, arrivals_min=_r(arr[0], k), arrivals_avg=_r(arr[1], k),
                    arrivals_max=_r(arr[2], k), pallets_min=pal[0], pallets_avg=pal[1], pallets_max=pal[2],
                    window_from=win[0], window_to=win[1], mono_pct=mono, inspect_pct=insp, inspect_min=insp_min)
            for stream, (dep, pal, win) in OUT.items():
                OutboundStream.objects.create(
                    day=day, kind=stream, departures_min=_r(dep[0], k), departures_avg=_r(dep[1], k),
                    departures_max=_r(dep[2], k), pallets_min=pal[0], pallets_avg=pal[1], pallets_max=pal[2],
                    window_from=win[0], window_to=win[1])
            for name, values in PROFILE_DEFAULTS.items():
                for x, v in zip(("min", "avg", "max"), values, strict=True):
                    setattr(day, f"{name}_{x}", v if name == "lines" else _r(v, k))
            day.full_pallet_pct = 40
            day.save()
        sc.shifts.all().delete()
        Shift.objects.bulk_create(Shift(scenario=sc, process=p, start_h=a, end_h=b, break_min=br, people=n)
                                  for p, rows in SHIFT_DEFAULTS.items() for a, b, br, n in rows)
        for day in sc.days.all():
            i, o = day.demand("avg"), day.outbound_demand("avg")
            self.stdout.write(f"{day.get_kind_display()}: IN {i['pallets_in']} palet (doki "
                              f"{i['docks_peak']['container']} kont. + {i['docks_peak']['pallet']} pal.), "
                              f"OUT {o['pallets_out']} palet (doki {o['docks_peak']}), {o['parcels']} paczek, "
                              f"{i['person_hours']['total']} + {sum(o['person_hours'].values()):.1f} osobogodzin")
        self.stdout.write(self.style.SUCCESS(f"Scenariusz „{sc}” gotowy (id {sc.pk})."))
