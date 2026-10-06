"""Prezentacja 3D (P1) — czysty Python (bez Django): walidacja slajdów, karty KPI, szablon startowy.

Slajd (JSON w `Showcase.slides`, kolejność listy = kolejność pokazu), wspólne pola: `type`, `title`, `caption`.
  camera     — `cam`: {"preset": "site" | "iso" | "top" | "docks" | "zone:<strefa>"} albo {"pos": [x,y,z],
               "target": [x,y,z]} (ujęcie zapisane z bieżącego widoku); presety rozwiązuje odtwarzacz w JS.
  kpi        — `cards`: klucze z CARDS (plansza na tle sceny).
  bottleneck — `index`: wąskie gardło wyniku symulacji (kamera i podświetlenie z animacji dnia).
  anim       — `t0`, `t1` [s od 0:00], `speed` (×10…×300): fragment animacji dnia.
  text       — sam tytuł i podpis (np. wnioski).
"""
import math

TYPES = ("camera", "kpi", "bottleneck", "anim", "text")
CARDS = {"throughput": "Przepustowość dnia", "docks": "Doki i pole odkładcze", "staff": "Obsada i flota",
         "capacity": "Pojemność vs potrzeba", "site": "Działka", "costs": "Koszty (widełki)"}
PRESETS = ("site", "iso", "top", "docks")
SPEEDS = (10, 30, 60, 120, 300)
MAX_SLIDES, TITLE_MAX, CAPTION_MAX, CARD_ROWS = 60, 120, 400, 6


class SlideError(ValueError):
    """Komunikat dla użytkownika (po polsku)."""


def _text(v, what, n, i):
    if v is None:
        return ""
    if not isinstance(v, str):
        raise SlideError(f"Slajd {i}: {what} — oczekiwany tekst.")
    v = " ".join(v.split())
    if len(v) > n:
        raise SlideError(f"Slajd {i}: {what} — maks. {n} znaków.")
    return v


def _vec(v, what, i):
    if not (isinstance(v, list) and len(v) == 3 and all(isinstance(x, (int, float)) and math.isfinite(x)
                                                         and abs(x) <= 1e5 for x in v)):
        raise SlideError(f"Slajd {i}: {what} — trzy liczby.")
    return [round(float(x), 3) for x in v]


def _cam(c, i):
    if not isinstance(c, dict):
        raise SlideError(f"Slajd {i}: brak ujęcia kamery.")
    if "preset" in c:
        p = c["preset"]
        if not isinstance(p, str) or not (p in PRESETS or (p.startswith("zone:") and 5 < len(p) <= 40)):
            raise SlideError(f"Slajd {i}: nieznane ujęcie „{p}”.")
        return {"preset": p}
    return {"pos": _vec(c.get("pos"), "pozycja kamery", i), "target": _vec(c.get("target"), "cel kamery", i)}


def clean_slides(raw):
    """Lista z edytora (zaufana granica) → znormalizowana lista slajdów. SlideError przy złych danych."""
    if not isinstance(raw, list):
        raise SlideError("Slajdy: oczekiwana lista.")
    if len(raw) > MAX_SLIDES:
        raise SlideError(f"Maks. {MAX_SLIDES} slajdów.")
    out = []
    for i, s in enumerate(raw, 1):
        if not isinstance(s, dict) or s.get("type") not in TYPES:
            raise SlideError(f"Slajd {i}: typ {', '.join(TYPES)}.")
        d = {"type": s["type"], "title": _text(s.get("title"), "tytuł", TITLE_MAX, i),
             "caption": _text(s.get("caption"), "podpis", CAPTION_MAX, i)}
        if s["type"] in ("camera", "kpi"):
            d["cam"] = _cam(s.get("cam") or {"preset": "iso"}, i)
        if s["type"] == "kpi":
            cards = s.get("cards")
            if not isinstance(cards, list) or not cards or any(c not in CARDS for c in cards):
                raise SlideError(f"Slajd {i}: karty KPI z listy {', '.join(CARDS)}.")
            d["cards"] = list(dict.fromkeys(cards))
        elif s["type"] == "bottleneck":
            idx = s.get("index")
            if not isinstance(idx, int) or isinstance(idx, bool) or not 0 <= idx < 100:
                raise SlideError(f"Slajd {i}: numer wąskiego gardła 0–99.")
            d["index"] = idx
        elif s["type"] == "anim":
            t0, t1, sp = s.get("t0"), s.get("t1"), s.get("speed", 60)
            if not all(isinstance(v, (int, float)) and not isinstance(v, bool) for v in (t0, t1)) \
                    or not 0 <= t0 < t1 <= 2 * 86400:
                raise SlideError(f"Slajd {i}: fragment animacji — początek przed końcem (0–48 h).")
            if sp not in SPEEDS:
                raise SlideError(f"Slajd {i}: prędkość {', '.join(f'×{x}' for x in SPEEDS)}.")
            d.update(t0=int(t0), t1=int(t1), speed=sp)
        out.append(d)
    return out


# ── karty KPI ───────────────────────────────────────────────────────────────────────────────
def _fmt(x, digits=0):
    if x is None:
        return "—"
    return f"{x:,.{digits}f}".replace(",", " ").replace(".", ",")     # twarda spacja: liczba się nie łamie


def _range(c, k=1000, digits=0):
    return f"{_fmt(c['low'] / k, digits)}–{_fmt(c['high'] / k, digits)}"


def kpi_cards(groups=(), capacity=None, site=None, costs=None):
    """groups: [(tytuł, [{label, unit, mean, worst}])] z `views_sim._sim_view` (kolejność: przepustowość, doki,
    obsada i flota); capacity: `placement.capacity`; site: `twin.site.site_kpi`; costs: `costs.compute`.
    → {klucz: {title, rows}}."""
    cards = {}
    pl = lambda s: str(s).replace(".", ",")                          # noqa: E731 — „917.5” → „917,5”
    for key, (_, cells) in zip(("throughput", "docks", "staff"), groups, strict=False):
        cards[key] = {"title": CARDS[key], "rows": [
            {"label": c["label"], "value": pl(c["mean"]), "worst": pl(c["worst"]), "unit": c["unit"]}
            for c in cells[:CARD_ROWS]]}
    if capacity:
        cards["capacity"] = {"title": CARDS["capacity"], "rows": [
            {"label": "Miejsca paletowe w layoucie", "value": _fmt(capacity.get("positions")), "unit": ""},
            {"label": "Potrzeba (stan × wzrost)", "value": _fmt(capacity.get("need")), "unit": "palet"},
            {"label": "Wypełnienie", "value": _fmt(capacity.get("fill_pct"), 1), "unit": "%"}]}
    if site:
        cards["site"] = {"title": CARDS["site"], "rows": [
            {"label": "Powierzchnia działki", "value": _fmt(site["plot_m2"]), "unit": "m²"},
            {"label": "Zabudowa", "value": _fmt(site["coverage_pct"], 1), "unit": "%"},
            {"label": "Biologicznie czynna", "value": _fmt(site["bio_pct"], 1), "unit": "%"},
            {"label": "Rezerwa pod rozbudowę", "value": _fmt(site["reserve_m2"]), "unit": "m²"},
            {"label": "Wysokość budynku", "value": _fmt(site["building_height_m"], 1), "unit": "m"}]}
    if costs:
        cards["costs"] = {"title": CARDS["costs"], "rows": [
            {"label": "CAPEX (layout i flota)", "value": _range(costs["capex"]), "unit": "tys. zł"},
            {"label": "OPEX roczny", "value": _range(costs["opex"]), "unit": "tys. zł/rok"},
            *({"label": f"OPEX na {u['label']}", "value": _range(u, 1, 2), "unit": "zł"}
              for u in costs["per_unit"].values())][:CARD_ROWS]}
    return cards


# ── szablon startowy ────────────────────────────────────────────────────────────────────────
def _hhmm(s):
    s = int(s) % 86400
    return f"{s // 3600:02d}:{s % 3600 // 60:02d}"


def summary_caption(f):
    """Podsumowanie z liczb (bez AI). f: positions, need, fill_pct, day („typowym” / „szczytowym”), pallets_in,
    pallets_out, parcels, bottlenecks, errors, coverage_pct, reserve_m2 — brakujące klucze pomijane."""
    parts = []
    if f.get("positions"):
        fill = f" (wypełnienie {_fmt(f['fill_pct'], 1)} %)" if f.get("need") else ""      # bez stanu — bez %
        parts.append(f"Hala mieści {_fmt(f['positions'])} miejsc paletowych{fill}.")
    if f.get("pallets_in") is not None:
        parts.append(f"W dniu {f.get('day', 'projektowym')} przyjmuje średnio {_fmt(f['pallets_in'])} palet, "
                     f"wydaje {_fmt(f['pallets_out'])} i pakuje {_fmt(f['parcels'])} paczek.")
    if f.get("bottlenecks") is not None:
        parts.append("Brak wąskich gardeł." if not f["bottlenecks"] else
                     f"Wąskie gardła: {f['bottlenecks']}"
                     + (f", w tym krytyczne: {f['errors']}." if f.get("errors") else "."))
    if f.get("coverage_pct") is not None:
        parts.append(f"Zabudowa działki {_fmt(f['coverage_pct'], 1)} %, rezerwa pod rozbudowę "
                     f"{_fmt(f['reserve_m2'])} m².")
    return " ".join(parts)[:CAPTION_MAX]


def template_slides(*, title, floor, racks, places, site_kpi_=None, cards=(), run=None, facts=None):
    """Szablon: przelot nad działką → hala ogólnie → strefy z bliska → doki → plansza KPI → szczyt animacji dnia
    → wąskie gardła → podsumowanie. racks: dicty z `zone`, `n_levels`; places: `views_play.layout_places`;
    run: {"day", "has_events", "peak_t", "bottlenecks"} albo None."""
    s = [{"type": "text", "title": title, "caption": "Projekt magazynu — layout, przepływy i wyniki dnia."}]
    if site_kpi_:
        s.append({"type": "camera", "cam": {"preset": "site"}, "title": "Działka i dojazd",
                  "caption": f"Działka {_fmt(site_kpi_['plot_m2'])} m², zabudowa {_fmt(site_kpi_['coverage_pct'], 1)} %, "
                             f"zieleń {_fmt(site_kpi_['bio_pct'], 1)} %."})
    s.append({"type": "camera", "cam": {"preset": "iso"}, "title": "Hala",
              "caption": f"Hala {_fmt(floor['width'], 1)} × {_fmt(floor['depth'], 1)} m, {len(racks)} regałów."})
    zones = {}
    for r in racks:
        z = zones.setdefault(r["zone"], {"n": 0, "levels": 0})
        z["n"] += 1
        z["levels"] = max(z["levels"], r["n_levels"])
    for z, v in sorted(zones.items(), key=lambda kv: -kv[1]["n"])[:2]:
        s.append({"type": "camera", "cam": {"preset": f"zone:{z}"}, "title": f"Strefa {z}",
                  "caption": f"{v['n']} regałów, do {v['levels']} poziomów."})
    docks = list(places.get("docks", {}).values())
    if docks:
        n_in = sum(d["role"].startswith("in_") for d in docks)
        s.append({"type": "camera", "cam": {"preset": "docks"}, "title": "Doki",
                  "caption": f"{n_in} doków przyjęć, {len(docks) - n_in} wydań i wspólnych."})
    # Maks. 3 karty na planszy (czytelność): wyniki dnia osobno, pojemność i działka osobno.
    for keys, name in ((["throughput", "docks", "staff"], f"Wyniki — {run['day']}" if run else "Wyniki"),
                       (["capacity", "site", "costs"], "Pojemność, działka i koszty")):
        keys = [k for k in keys if k in cards]
        if keys:
            s.append({"type": "kpi", "cam": {"preset": "iso"}, "cards": keys, "title": name, "caption": ""})
    if run and run.get("has_events"):
        t0 = max(0, int(run["peak_t"]) - 1800)
        s.append({"type": "anim", "t0": t0, "t1": t0 + 3600, "speed": 60, "title": "Szczyt dnia",
                  "caption": f"{_hhmm(t0)}–{_hhmm(t0 + 3600)}: najwięcej aut w kolejce i palet na polach odkładczych."})
        bns = [(i, b) for i, b in enumerate(run.get("bottlenecks") or []) if b.get("t0") is not None]
        bns.sort(key=lambda ib: ib[1].get("severity") != "error")
        for i, b in bns[:3]:
            s.append({"type": "bottleneck", "index": i, "title": b["area"],
                      "caption": f"{b.get('window') or 'cały dzień'}: {b.get('suggestion', '')}"[:CAPTION_MAX]})
    s.append({"type": "text", "title": "Podsumowanie", "caption": summary_caption(facts or {})})
    return clean_slides(s)
