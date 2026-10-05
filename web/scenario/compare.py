"""Tabela porównania layout × scenariusz (E7) — czysty Python na zapisanych wynikach `ScenarioRun.result`.

Kolumna = jeden wynik symulacji (scenariusz, dzień, model hali). Wiersz = KPI z karty (S3a + pojemność S3b):
wartość, najlepsza w wierszu (gdy kierunek „lepiej” jest znany) i różnica % do pierwszej kolumny —
ten sam układ co porównanie wariantów w `twin.views.warehouse_variants._comparison`.
"""


def _agg(key, stat):
    return lambda r: ((r.get("agg") or {}).get(key) or {}).get(stat)


def _cap(key):
    return lambda r: ((r.get("placement") or {}).get("capacity") or {}).get(key)


def _docks(role):
    return lambda r: ((r.get("places") or {}).get("counts") or {}).get(role)


def _cost(part):
    return lambda r: ((r.get("costs") or {}).get(part) or {}).get("mid")


def _per(unit):
    return lambda r: (((r.get("costs") or {}).get("per_unit") or {}).get(unit) or {}).get("mid")


def _count(sev=None):
    return lambda r: sum(1 for b in r.get("bottlenecks", []) if sev is None or b["severity"] == sev)


# (etykieta, jednostka, lepiej = "max" | "min" | None, odczyt z result)
ROWS = [
    ("Miejsca paletowe w layoucie", "", "max", _cap("positions")),
    ("Potrzeba miejsc (stan × wzrost)", "", None, _cap("need")),
    ("Wypełnienie miejsc", "%", "min", _cap("fill_pct")),
    ("Doki kontenerowe", "szt.", None, _docks("in_container")),
    ("Doki paletowe IN", "szt.", None, _docks("in_pallet")),
    ("Doki wydań", "szt.", None, _docks("out")),
    ("Palet przyjętych (średnio)", "", "max", _agg("pallets_in", "mean")),
    ("Palet wydanych (średnio)", "", "max", _agg("pallets_out", "mean")),
    ("Paczek spakowanych (średnio)", "", "max", _agg("parcels", "mean")),
    ("Paczek po odbiorze kuriera (P95)", "", "min", _agg("parcels_late", "worst")),
    ("Aut OUT po cut-off (P95)", "", "min", _agg("trucks_out_late", "worst")),
    ("Czekanie kontenerów (P95)", "min", "min", _agg("wait_in_container_p95_min", "worst")),
    ("Czekanie aut paletowych IN (P95)", "min", "min", _agg("wait_in_pallet_p95_min", "worst")),
    ("Czekanie aut OUT (P95)", "min", "min", _agg("wait_out_p95_min", "worst")),
    ("Max palet na polu przyjęć (P95)", "", "min", _agg("staging_in_max", "worst")),
    ("Max palet na polu wydań (P95)", "", "min", _agg("staging_out_max", "worst")),
    ("Flota: wykorzystanie dnia", "%", None, _agg("fleet_util_pct", "mean")),
    ("Flota: szczyt (P95)", "%", "min", _agg("fleet_peak_pct", "worst")),
    ("Flota efektywna — bez ładowania (P5)", "", "max", _agg("fleet_effective", "worst")),
    ("Zadań bez obsady (P95)", "", "min", _agg("unfinished", "worst")),
    ("Wąskie gardła", "szt.", "min", _count()),
    ("w tym krytyczne", "szt.", "min", _count("error")),
    # C1: koszty (środek widełek) — `ScenarioRun.result` ich nie trzyma, widok dokłada `costs` przed porównaniem
    ("CAPEX (środek widełek)", "zł", "min", _cost("capex")),
    ("OPEX roczny (środek widełek)", "zł/rok", "min", _cost("opex")),
    ("OPEX na paletę", "zł", "min", _per("pallets")),
    ("OPEX na paczkę", "zł", "min", _per("parcels")),
    ("OPEX na zamówienie", "zł", "min", _per("orders")),
]


def compare_columns(results, rows=ROWS):
    """results: [ScenarioRun.result] w kolejności kolumn (pierwsza = punkt odniesienia)."""
    out = []
    for label, unit, better, get in rows:
        vals = [get(r) for r in results]
        nums = [x for x in vals if isinstance(x, (int, float))]
        best = (max(nums) if better == "max" else min(nums)) if better and len(nums) > 1 else None
        base = vals[0] if vals and isinstance(vals[0], (int, float)) else None
        cells = []
        for i, x in enumerate(vals):
            delta = None
            if i and base not in (None, 0) and isinstance(x, (int, float)):
                delta = round((x - base) / base * 100)
            good = None if (delta in (None, 0) or not better) else ((delta > 0) == (better == "max"))
            cells.append({"value": x, "best": best is not None and x == best and nums.count(best) < len(nums),
                          "delta": delta, "good": good})
        out.append({"label": label, "unit": unit, "cells": cells})
    return out
