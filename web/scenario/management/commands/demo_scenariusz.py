"""Scenariusz referencyjny (syntetyczny, anonimowy): centrum dystrybucyjne z importem kontenerowym.

Dzień typowy: ~8 kontenerów 40' (≈45 palet po paletyzacji), 6–10 aut 33-paletowych (fizycznie 17–32 palet),
solówki/busy, cross-dock; wydania autami 33-pal. i solówkami, ~2 200 paczek dziennie z odbiorem kurierów do 18:00,
zwroty. Dzień szczytowy: wolumeny ×1,3. Obsada: 1–2 zmiany per proces, flota 14 wózków. Idempotentnie — ponowne
uruchomienie odtwarza plan. Do symulacji dnia (S3a) tworzy też halę demo z generatora (3 doki paletowe IN), jeśli
jej nie ma: dzień typowy ma najwyżej drobne ostrzeżenia, szczyt — wąskie gardła z podpowiedziami.
"""
from django.core.management.base import BaseCommand
from django.db import transaction

from equipment.services import assign_classes, pick_class
from scenario.models import InboundStream, OutboundStream, PROFILE_DEFAULTS, Scenario, ScenarioDay, Shift
from twin.design_generator import generate
from twin.models import WarehouseHallFeature, WarehouseModel, WarehouseModelRack

NAME = "Centrum dystrybucyjne — rok bazowy (demo)"
HALL = "Hala demo — scenariusz (generator)"
FLEET = 14
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


# proces: [(od, do, przerwa min, osób)] — obsada dobrana do dnia typowego (szczyt pokazuje braki)
SHIFTS = {
    "unload": [(6, 14, 30, 6), (14, 22, 30, 2)], "palletize": [(6, 14, 30, 8), (14, 22, 30, 5)],
    "inspect": [(6, 14, 30, 2), (14, 22, 30, 1)], "pick": [(6, 14, 30, 10), (14, 22, 30, 8)],
    "pack": [(6, 14, 30, 14), (14, 22, 30, 10)], "load": [(6, 14, 30, 3), (14, 22, 30, 5)],
    "returns": [(6, 14, 30, 2)],
}


def demo_hall():
    """Hala z generatora z 3 dokami paletowymi IN (preset ma 1 — przy 16+ autach paletowych to kolejka)."""
    wm = WarehouseModel.objects.filter(name=HALL).first()
    if wm:
        return wm, False
    g = generate(pallet_in_docks=3)
    wm = WarehouseModel.objects.create(name=HALL, notes="Dane syntetyczne — hala do symulacji scenariusza demo.",
                                       clear_height_m=g["params"]["clear_height_m"],
                                       floor_width_m=g["floor"]["width"], floor_depth_m=g["floor"]["depth"],
                                       site=g["site"])
    WarehouseModelRack.objects.bulk_create([WarehouseModelRack(model=wm, **r) for r in assign_classes(g["racks"])])
    WarehouseHallFeature.objects.bulk_create([WarehouseHallFeature(model=wm, **f) for f in g["features"]]
                                             + [WarehouseHallFeature(model=wm, **z) for z in demo_zones(g["racks"])])
    return wm, True


def demo_zones(racks):
    """Strefy specjalne demo nad dwiema parami rzędów VNA: ADR (rzędy 1–2) i temperatura (rzędy 3–4)."""
    vna = sorted((r for r in racks if r["zone"] == "V"), key=lambda r: r["y_m"])
    out = []
    for kind, label, rows in (("zone_adr", "Strefa ADR", vna[:2]), ("zone_temp", "Strefa temperaturowa", vna[2:4])):
        if not rows:
            continue
        x0 = min(r["x_m"] for r in rows)
        y0 = min(r["y_m"] for r in rows)
        x1 = max(r["x_m"] + r["n_bays"] * r["bay_width_cm"] / 100 for r in rows)
        y1 = max(r["y_m"] + r["depth_cm"] / 100 for r in rows)
        out.append({"kind": kind, "label": label, "x_m": round(x0 - 0.2, 2), "y_m": round(y0 - 0.2, 2),
                    "width_m": round(x1 - x0 + 0.4, 2), "depth_m": round(y1 - y0 + 0.4, 2), "angle_deg": 0.0})
    return out


def _r(v, k):
    return round(v * k)


class Command(BaseCommand):
    help = "Scenariusz demo: przyjęcia, wydania, paczki, zwroty, cross-dock i obsada (dzień typowy i szczyt ×1,3)."

    @transaction.atomic
    def handle(self, *args, **opts):
        sc, _ = Scenario.objects.update_or_create(name=NAME, defaults={
            "description": "Dane syntetyczne. Szczyt = wolumeny ×1,3 (sezon).", "growth": 1.0, "seed": 42,
            "fleet_units": FLEET, "fleet_equipment": pick_class("vna", 0)})
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
                                  for p, rows in SHIFTS.items() for a, b, br, n in rows)
        for day in sc.days.all():
            i, o = day.demand("avg"), day.outbound_demand("avg")
            self.stdout.write(f"{day.get_kind_display()}: IN {i['pallets_in']} palet (doki "
                              f"{i['docks_peak']['container']} kont. + {i['docks_peak']['pallet']} pal.), "
                              f"OUT {o['pallets_out']} palet (doki {o['docks_peak']}), {o['parcels']} paczek, "
                              f"{i['person_hours']['total']} + {sum(o['person_hours'].values()):.1f} osobogodzin")
        wm, created = demo_hall()
        self.stdout.write(f"Hala do symulacji: „{wm}” (id {wm.pk}{', utworzona' if created else ''}).")
        self.stdout.write(self.style.SUCCESS(f"Scenariusz „{sc}” gotowy (id {sc.pk})."))
