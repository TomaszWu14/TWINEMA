"""Koszty wariantu (C1) — czysty Python: CAPEX layoutu i floty, OPEX roczny pracy i floty, koszt na jednostkę.

Wszystko jako widełki (od, do) ze stawek min–max; „środek” = średnia z widełek. Stawki domyślne są syntetyczne.
Rok = miks dni: dni typowe × dzień typowy + dni szczytowe × dzień szczytowy (`mix_days`); obsada zakładana
jest ta sama w każdym dniu, flota i wolumeny — z symulacji danego typu dnia.
"""
WEEKS = 52
RACK_RATE = {"reach": "rack_reach", "vna": "rack_vna", "shelf": "rack_shelf"}
RACK_LABEL = {"reach": "Regały standard (reach)", "vna": "Regały VNA", "shelf": "Regały półkowe / kompletacji"}


def _item(label, qty, unit, rate):
    lo, hi = rate
    return {"label": label, "qty": qty, "unit": unit, "low": round(qty * lo), "high": round(qty * hi)}


def _total(items):
    lo, hi = sum(i["low"] for i in items), sum(i["high"] for i in items)
    return {"items": items, "low": lo, "high": hi, "mid": round((lo + hi) / 2)}


def mix_days(work_days, peak_days_year, have_peak=True, have_typical=True):
    """Dni w roku: [(typ dnia, liczba dni)]. Brak symulacji jednego typu → cały rok z drugiego."""
    total = work_days * WEEKS
    peak = min(max(peak_days_year, 0), total)
    if not have_peak:
        return [("typical", total)]
    if not have_typical:
        return [("peak", total)]
    return [(k, n) for k, n in (("typical", total - peak), ("peak", peak)) if n]


def compute(rates, layout, fleet, labor_h_day, days):
    """rates: {klucz: (od, do)} — `CostRate`; layout: {positions: {reach|vna|shelf: n}, docks, stations, area_m2};
    fleet: {name, units, purchase: (od, do) | None, hour: (od, do) | None} (None → stawki ogólne floty);
    labor_h_day: osobogodziny zakładanej obsady / dzień (każdy dzień taki sam);
    days: [{kind, days, fleet_busy_h, volumes: {pallets, parcels, orders}}] — miks dni w roku; per dzień:
    godziny pracy floty (symulacja) i wolumeny → koszt OPEX na jednostkę (OPEX ÷ wolumen roczny)."""
    capex = [_item(RACK_LABEL[k], n, "miejsc", rates[RACK_RATE[k]])
             for k, n in layout["positions"].items() if n]
    if layout["docks"]:
        capex.append(_item("Doki", layout["docks"], "szt.", rates["dock"]))
    if layout["stations"]:
        capex.append(_item("Stanowiska", layout["stations"], "szt.", rates["station"]))
    if layout.get("area_m2"):
        capex.append(_item("Hala (budynek)", round(layout["area_m2"]), "m²", rates["building_m2"]))
    if fleet["units"]:
        capex.append(_item(f"Flota: {fleet['name']}", fleet["units"], "szt.", fleet["purchase"] or rates["fleet_unit"]))

    total_days = sum(d["days"] for d in days)
    fleet_h = sum(d["fleet_busy_h"] * d["days"] for d in days)
    opex = [_item("Praca (zakładana obsada)", round(labor_h_day * total_days), "osobogodzin/rok", rates["labor_h"]),
            _item(f"Flota: {fleet['name']} (energia, serwis)", round(fleet_h), "godzin pracy/rok",
                  fleet["hour"] or rates["fleet_hour"])]
    capex, opex = _total(capex), _total(opex)

    per_unit = {}
    for key, label in (("pallets", "paletę"), ("parcels", "paczkę"), ("orders", "zamówienie")):
        n = sum((d["volumes"].get(key) or 0) * d["days"] for d in days)
        if n:
            per_unit[key] = {"label": label, "low": round(opex["low"] / n, 2), "high": round(opex["high"] / n, 2),
                             "mid": round(opex["mid"] / n, 2)}
    return {"capex": capex, "opex": opex, "per_unit": per_unit, "days_year": total_days,
            "mix": [(d["kind"], d["days"]) for d in days]}
