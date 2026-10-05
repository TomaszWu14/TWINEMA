"""Koszty wariantu (C1) — czysty Python: CAPEX layoutu i floty, OPEX roczny pracy i floty, koszt na jednostkę.

Wszystko jako widełki (od, do) ze stawek min–max; „środek” = średnia z widełek. Stawki domyślne są syntetyczne.
Rok = dni pracy w tygodniu × 52 dni tego typu (typowy albo szczytowy) — prosty model, bez mieszania dni.
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


def compute(rates, layout, fleet, labor_h_day, fleet_busy_h_day, work_days, volumes):
    """rates: {klucz: (od, do)} — `CostRate`; layout: {positions: {reach|vna|shelf: n}, docks, stations, area_m2};
    fleet: {name, units, purchase: (od, do) | None, hour: (od, do) | None} (None → stawki ogólne floty);
    labor_h_day: osobogodziny zakładanej obsady / dzień; fleet_busy_h_day: godziny pracy floty / dzień (symulacja);
    volumes: {pallets, parcels, orders} na dzień → koszt OPEX na jednostkę (OPEX ÷ wolumen roczny)."""
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

    days = work_days * WEEKS
    opex = [_item("Praca (zakładana obsada)", round(labor_h_day * days), "osobogodzin/rok", rates["labor_h"]),
            _item(f"Flota: {fleet['name']} (energia, serwis)", round(fleet_busy_h_day * days), "godzin pracy/rok",
                  fleet["hour"] or rates["fleet_hour"])]
    capex, opex = _total(capex), _total(opex)

    per_unit = {}
    for key, label in (("pallets", "paletę"), ("parcels", "paczkę"), ("orders", "zamówienie")):
        n = (volumes.get(key) or 0) * days
        if n:
            per_unit[key] = {"label": label, "low": round(opex["low"] / n, 2), "high": round(opex["high"] / n, 2),
                             "mid": round(opex["mid"] / n, 2)}
    return {"capex": capex, "opex": opex, "per_unit": per_unit, "days_year": days}
