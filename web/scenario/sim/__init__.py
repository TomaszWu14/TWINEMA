"""Symulacja dnia scenariusza na layoucie hali (S3a) — czysty Python, bez Django.

    run_many(day, params, shifts, places, seed, runs=12) → {agg, rep, bottlenecks, events, runs, places}

day     — {inbound:[stream], outbound:[stream], profile:{…}} (formaty jak w `scenario.inbound/outbound`)
params  — normy scenariusza + growth + return_restock_pct + flota (fleet_units, fleet_min_per_move,
          battery_h, charge_h)
shifts  — [{process, start_h, end_h, break_min, people}]
places  — `sim.places.places_from_features(features)`

Przebieg i ma ziarno `seed * 1000 + i` (powtarzalnie). KPI: średnia i najgorszy przypadek (P95 albo P5).
Reprezentatywny = przebieg o medianie „kłopotów” (czekanie aut + paczki po cut-off) — z niego oś czasu,
wąskie gardła i zdarzenia do animacji.

Format zdarzeń (dla odtwarzacza 3D, S4) — lista krotek posortowana po czasie:
    [t_s, obj, kind, what, place]
    t_s   — sekunda od 0:00 dnia,
    obj   — id obiektu: auto/kontener „in3”, „out7”; paleta „in3-p12”; zamówienie (paczki) „o154”,
    kind  — container | truck | courier | pallet | parcel,
    what  — arrive (brama) · dock (podjazd do doku) · depart (odjazd) · built (paleta z paletyzacji) ·
            staging (na polu odkładczym) · move (wózek zabiera z pola) · stored (na regale) ·
            retrieved (zdjęta z regału / z kompletacji) · packed (paczki zamówienia gotowe) ·
            loaded (paleta zabrana z pola wydań na auto w doku; od S4),
    place — gate | dock:<id elementu hali> | staging_in | staging_out | palletize | pack | pick | rack.
Id doku = id `WarehouseHallFeature` (albo „d<n>” bez id; „x-…” = dok dodany w podpowiedzi).
Rozszerzenia S4 (zgodne z v1 — stare pola bez zmian): kurier ma też arrive (gate) i depart (dok);
„packed” ma opcjonalną 6. kolumnę n = liczba paczek zamówienia. Starsze przebiegi tych zdarzeń nie mają —
odtwarzacz radzi sobie bez nich (palety wydań znikają z pola przy odjeździe auta, paczka = 1).
"""
import copy

from ..staffing import span
from .engine import simulate_plan
from .places import with_extra_docks
from .plan import build_plan
from .report import aggregate, bottlenecks, run_report

FLEET_DEFAULTS = {"fleet_units": 6, "fleet_min_per_move": 4.0, "battery_h": 6.0, "charge_h": 1.5}


def run_day(day, params, shifts, places, seed):
    plan = build_plan(day, params, seed)
    rec = simulate_plan(plan, params, shifts, places)
    rep = run_report(rec)
    rep["events"] = sorted(rec["events"])
    return rep


def _trouble(kpi):
    return (kpi["wait_in_container_p95_min"] + kpi["wait_in_pallet_p95_min"] + kpi["wait_out_p95_min"]
            + kpi["parcels_late"] / 10 + kpi["fleet_wait_p95_min"])


def returns_window(shifts):
    """Zwroty przychodzą w godzinach zmian obsługi zwrotów (bez ostatniej godziny)."""
    own = [span(s) for s in shifts if s["process"] == "returns"]
    if not own:
        return (7.0, 14.0)
    a, b = min(x[0] for x in own), max(x[1] for x in own)
    return (a, max(a + 0.5, b - 1.0))


def run_many(day, params, shifts, places, seed, runs=12):
    params = {**FLEET_DEFAULTS, "returns_window": returns_window(shifts), **params}
    seeds = [seed * 1000 + i for i in range(runs)]
    reps = [run_day(day, params, shifts, places, s) for s in seeds]
    order = sorted(range(runs), key=lambda i: _trouble(reps[i]["kpi"]))
    mid = order[runs // 2]
    rep, rep_seed = reps[mid], seeds[mid]
    agg = aggregate([r["kpi"] for r in reps])

    def rerun(kind, *args):
        p, sh, pl = params, shifts, places
        if kind == "docks":
            pl = with_extra_docks(places, args[0], args[1])
        elif kind == "people":
            sh = copy.deepcopy(shifts)
            sh[args[0]]["people"] += args[1]
        elif kind == "fleet":
            p = {**params, "fleet_units": params["fleet_units"] + args[0]}
        return run_day(day, p, sh, pl, rep_seed)["kpi"]

    return {"agg": agg, "rep": {"kpi": rep["kpi"], "timeline": rep["timeline"], "seed": rep_seed},
            "bottlenecks": bottlenecks(agg, rep, places, shifts, rerun), "events": rep["events"],
            "runs": runs, "places": {k: places[k] for k in ("counts", "staging_m2", "warnings")}}
