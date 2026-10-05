"""Wydania, paczki, zwroty i cross-dock → zapotrzebowanie dnia (czysty Python — bez Django).

Ta sama logika co przy przyjęciach (`inbound.py`): auta rozłożone równo w oknie załadunku (koniec okna =
cut-off), dok zajęty przez czas załadunku z norm; poziomy „avg” i „max”. Wzrost: więcej aut (w górę)
i proporcjonalnie więcej zamówień, linii, paczek i zwrotów.

stream:  {kind, departures:(min,avg,max), pallets:(min,avg,max), window:(od_h, cut-off_h)}
profile: {orders, lines, parcels, returns: (min,avg,max), full_pallet_pct}
norms:   {load_min_per_pallet, pick_lines_per_h, wrap_min_per_pallet, pack_min_per_parcel,
          pack_min_per_line, label_min_per_parcel, courier_dock_min, return_min, return_restock_pct}
"""
from .inbound import _hhmm, _pick, arrivals_count, peak_concurrency, starts

COURIER, CROSSDOCK = "courier", "crossdock"


def load_hours(stream, pallets, norms):
    if stream["kind"] == COURIER:
        return norms["courier_dock_min"] / 60
    return pallets * norms["load_min_per_pallet"] / 60


def day_outbound(streams, profile, norms, *, growth=1.0, level="avg"):
    rows, docks = [], []
    pallets_out = xdock_out = 0.0
    ph = {"load": 0.0}
    for s in streams:
        n = arrivals_count(_pick(s["departures"], level), growth)
        p = 0 if s["kind"] == COURIER else _pick(s["pallets"], level)
        hours = load_hours(s, p, norms)
        docks += [(t, t + hours) for t in (starts(n, s["window"]) if n else [])]
        pallets_out += n * p
        if s["kind"] == CROSSDOCK:
            xdock_out += n * p
        ph["load"] += n * hours if s["kind"] != COURIER else 0.0
        rows.append({"kind": s["kind"], "departures": n, "pallets_per": p, "pallets": round(n * p),
                     "load_min": round(hours * 60), "cutoff": _hhmm(s["window"][1])})
    orders = _pick(profile["orders"], level) * growth
    lines = orders * _pick(profile["lines"], level)
    parcels = _pick(profile["parcels"], level) * growth
    returns = _pick(profile["returns"], level) * growth
    lines_per_order = _pick(profile["lines"], level)
    stored_out = pallets_out - xdock_out                       # cross-dock nie przechodzi przez skład
    picked = stored_out * (1 - profile["full_pallet_pct"] / 100)
    ph["load"] += picked * norms["wrap_min_per_pallet"] / 60   # owijanie palet kompletowanych przy załadunku
    ph["pick"] = lines / norms["pick_lines_per_h"]
    ph["pack"] = parcels * (norms["pack_min_per_parcel"] + lines_per_order * norms["pack_min_per_line"]
                            + norms["label_min_per_parcel"]) / 60
    ph["returns"] = returns * norms["return_min"] / 60
    ph = {k: round(v, 1) for k, v in ph.items()}
    peak, at = peak_concurrency(docks)
    return {
        "level": level, "rows": rows, "pallets_out": round(pallets_out), "pallets_xdock": round(xdock_out),
        "pallets_full": round(stored_out - picked), "pallets_picked": round(picked),
        "orders": round(orders), "lines": round(lines), "parcels": round(parcels), "returns": round(returns),
        "returns_restock": round(returns * norms["return_restock_pct"] / 100),
        "docks_peak": peak, "docks_peak_at": _hhmm(at), "person_hours": ph,
        "courier_cutoff": max((s["window"][1] for s in streams if s["kind"] == COURIER), default=None),
    }
