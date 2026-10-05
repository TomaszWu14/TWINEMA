"""Obsada: potrzebna vs zakładana per proces i zmiana + ryzyko cut-off kurierów (czysty Python).

Osobogodziny procesu (z `inbound.day_demand` i `outbound.day_outbound`) dzielimy między jego zmiany
proporcjonalnie do zakładanej zdolności zmiany (osoby × czas efektywny = długość − przerwa) — rozkład obsady
planisty traktujemy jako zamierzony (rano kontenery, po południu załadunek); gdy nikt nie jest przypisany,
dzielimy po czasie efektywnym. Potrzebna obsada zmiany = ⌈udział / czas efektywny⌉.

shift: {process, start_h, end_h, break_min, people}   (end < start = zmiana przez północ)
"""
import math

PROCESSES = [("unload", "Rozładunek"), ("palletize", "Paletyzacja i przepakowanie"), ("inspect", "Kontrola"),
             ("pick", "Kompletacja"), ("pack", "Pakowanie i nadanie"), ("load", "Załadunek i owijanie"),
             ("returns", "Zwroty")]


def process_hours(inbound, outbound):
    i, o = inbound["person_hours"], outbound["person_hours"]
    return {"unload": i["unload"], "palletize": round(i["palletize"] + i["repack"], 1), "inspect": i["inspect"],
            "pick": o["pick"], "pack": o["pack"], "load": o["load"], "returns": o["returns"]}


def span(shift):
    end = shift["end_h"] + (24 if shift["end_h"] <= shift["start_h"] else 0)
    return shift["start_h"], end


def productive_h(shift):
    a, b = span(shift)
    return max(0.0, b - a - shift["break_min"] / 60)


def staffing(hours, shifts):
    """→ [{process, label, hours, shifts:[{…, needed, gap}], needed, assumed, short}] w kolejności PROCESSES."""
    out = []
    for key, label in PROCESSES:
        own = [s for s in shifts if s["process"] == key]
        weights = [productive_h(s) * s["people"] for s in own]
        if not sum(weights):
            weights = [productive_h(s) for s in own]
        total_w = sum(weights)
        h = hours.get(key, 0.0)
        rows = []
        for s, w in zip(own, weights, strict=True):
            prod = productive_h(s)
            need = math.ceil(h * w / total_w / prod - 1e-9) if h and prod and total_w else 0
            rows.append({**s, "productive_h": round(prod, 2), "needed": need, "gap": s["people"] - need})
        needed, assumed = sum(r["needed"] for r in rows), sum(s["people"] for s in own)
        out.append({"process": key, "label": label, "hours": h, "shifts": rows, "needed": needed,
                    "assumed": assumed, "short": any(r["gap"] < 0 for r in rows) or (h > 0 and not own)})
    return out


def cutoff_risk(pack_hours, shifts, cutoff_h):
    """Czy pakowanie (wszystkie paczki) zdąży do ostatniego odbioru kuriera przy zakładanej obsadzie.
    ponytail: jedna granica = ostatni cut-off; podział paczek między kurierów policzy symulacja S3."""
    if cutoff_h is None or not pack_hours:
        return None
    cap = 0.0
    for s in shifts:
        if s["process"] != "pack":
            continue
        a, b = span(s)
        length = b - a
        if length <= 0:
            continue
        before = max(0.0, min(b, cutoff_h) - a)
        cap += s["people"] * before * productive_h(s) / length
    return {"cutoff": cutoff_h, "capacity_h": round(cap, 1), "demand_h": round(pack_hours, 1),
            "ok": cap + 1e-9 >= pack_hours, "missing_h": round(max(0.0, pack_hours - cap), 1)}
