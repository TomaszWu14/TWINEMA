"""ML1 — prognoza tygodniowych wolumenów: kilka modeli wygładzania wykładniczego kontra
trend log-liniowy (punkt odniesienia), wybór modelu po teście wstecznym (MAPE). Czysty Python.

Modele (Hyndman & Athanasopoulos, „Forecasting: Principles and Practice”, rozdz. 8):
  trend_log    — regresja na log(wartości) (dotychczasowa prognoza bliźniaka, baseline),
  ses          — proste wygładzanie wykładnicze (poziom),
  holt         — Holt: poziom + trend liniowy,
  holt_damped  — Holt z tłumionym trendem (φ), zwykle najbezpieczniejszy na długi horyzont,
  hw_add       — Holt-Winters addytywny z sezonem rocznym (52 tyg.) — tylko gdy historia ≥ 2 lata.

Parametry dobierane siatką (minimum SSE prognoz o krok naprzód na zbiorze uczącym). Przedział 80 %
z odchylenia reszt o krok naprzód × √h — przybliżenie, wystarczające do scenariusza P50/P90.
ponytail: siatka zamiast optymalizatora — 9⁴ kombinacji przy HW to < 1 s dla kilkuset tygodni.
"""
import math
import statistics

VERSION = "forecast-v1"
BACKTEST = 8
MIN_POINTS = 12
SEASON = 52
Z80 = 1.2816
GRID = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
PHI = [0.8, 0.9, 0.95, 0.98]
LABELS = {"trend_log": "Trend log-liniowy (punkt odniesienia)", "ses": "Wygładzanie wykładnicze",
          "holt": "Holt (trend liniowy)", "holt_damped": "Holt z tłumionym trendem",
          "hw_add": "Holt-Winters (sezon roczny)"}


# ── modele: fit(y, params) → (dopasowania o krok naprzód, funkcja prognozy h → wartość) ──────

def _trend_log(y, _p):
    xs = list(range(len(y)))
    slope, icpt = statistics.linear_regression(xs, [math.log(max(v, 1e-9)) for v in y])
    fitted = [math.exp(icpt + slope * x) for x in xs]
    return fitted, lambda h: math.exp(icpt + slope * (len(y) - 1 + h))


def _ses(y, p):
    a = p["alpha"]
    level, fitted = y[0], [y[0]]
    for v in y[1:]:
        fitted.append(level)
        level = a * v + (1 - a) * level
    return fitted, lambda h: level


def _holt(y, p):
    a, b, phi = p["alpha"], p["beta"], p.get("phi", 1.0)
    level, trend = y[0], y[1] - y[0]
    fitted = [y[0]]
    for v in y[1:]:
        f = level + phi * trend
        fitted.append(f)
        new_level = a * v + (1 - a) * f
        trend = b * (new_level - level) + (1 - b) * phi * trend
        level = new_level

    def fc(h):
        damp = sum(phi ** i for i in range(1, h + 1)) if phi != 1.0 else h
        return level + damp * trend
    return fitted, fc


def _hw_add(y, p, m=SEASON):
    a, b, g = p["alpha"], p["beta"], p["gamma"]
    # Inicjalizacja z dwóch pierwszych sezonów: trend z różnicy średnich, sezon = odchylenie od
    # linii trendu (nie od samej średniej — inaczej rampa trendu siedzi w indeksach i zawyża trend).
    mean1 = statistics.fmean(y[:m])
    trend = (statistics.fmean(y[m:2 * m]) - mean1) / m
    season = [y[i] - (mean1 + trend * (i - (m - 1) / 2)) for i in range(m)]
    level = mean1 + trend * (m - 1) / 2                 # poziom na końcu 1. sezonu
    fitted = list(y[:m])                               # pierwszy sezon = tylko inicjalizacja
    for t in range(m, len(y)):
        v = y[t]
        s = season[t % m]
        fitted.append(level + trend + s)
        new_level = a * (v - s) + (1 - a) * (level + trend)
        trend = b * (new_level - level) + (1 - b) * trend
        season[t % m] = g * (v - new_level) + (1 - g) * s
        level = new_level
    n = len(y)
    return fitted, lambda h: level + h * trend + season[(n + h - 1) % m]


MODELS = {"trend_log": _trend_log, "ses": _ses, "holt": _holt, "holt_damped": _holt, "hw_add": _hw_add}


def _grid(name):
    if name == "trend_log":
        return [{}]
    if name == "ses":
        return [{"alpha": a} for a in GRID]
    if name == "holt":
        return [{"alpha": a, "beta": b} for a in GRID for b in GRID]
    if name == "holt_damped":
        return [{"alpha": a, "beta": b, "phi": f} for a in GRID for b in GRID for f in PHI]
    return [{"alpha": a, "beta": b, "gamma": g} for a in GRID[::2] for b in GRID[::2] for g in GRID[::2]]


def _sse(y, fitted, skip):
    return sum((v - f) ** 2 for v, f in zip(y[skip:], fitted[skip:], strict=True))


def fit(name, y):
    """Najlepsze parametry modelu na serii `y` → (params, fitted, prognoza h→v, sd reszt)."""
    skip = SEASON if name == "hw_add" else 1
    best = None
    for p in _grid(name):
        fitted, fc = MODELS[name](y, p)
        err = _sse(y, fitted, skip)
        if best is None or err < best[0]:
            best = (err, p, fitted, fc)
    _, p, fitted, fc = best
    resid = [v - f for v, f in zip(y[skip:], fitted[skip:], strict=True)]
    sd = statistics.pstdev(resid) if len(resid) > 1 else 0.0
    return p, fitted, fc, sd


def candidates(n):
    names = ["trend_log", "ses", "holt", "holt_damped"]
    if n >= 2 * SEASON + BACKTEST:
        names.append("hw_add")
    return names


def mape(actual, pred):
    pairs = [(a, p) for a, p in zip(actual, pred, strict=True) if a]
    return round(100 * statistics.fmean(abs(a - p) / a for a, p in pairs), 2) if pairs else None


def evaluate(y, backtest=BACKTEST):
    """Test wsteczny: każdy model uczony bez ostatnich `backtest` punktów prognozuje je.
    → [{model, label, mape, params}] posortowane od najlepszego (None MAPE na końcu)."""
    rows = []
    train, test = y[:-backtest], y[-backtest:]
    for name in candidates(len(y)):
        if name == "hw_add" and len(train) < 2 * SEASON:
            continue
        p, _, fc, _ = fit(name, train)
        pred = [fc(h) for h in range(1, backtest + 1)]
        rows.append({"model": name, "label": LABELS[name], "mape": mape(test, pred), "params": p})
    rows.sort(key=lambda r: (r["mape"] is None, r["mape"] if r["mape"] is not None else 0))
    return rows


def run(series, horizon=52, years=5, backtest=BACKTEST):
    """series: [(etykieta tygodnia, wartość)] → wynik do zapisu w ModelRun (JSON-owalny).

    Model wygrywa, gdy ma najniższe MAPE; baseline zostaje pokazany zawsze. Wzrost roczny =
    średnia prognozy na kolejne 52 tyg. ÷ średnia ostatnich 52 tyg. (albo całej historii)."""
    labels = [w for w, _ in series]
    y = [float(v) for _, v in series]
    if len(y) < MIN_POINTS + backtest // 2:
        return {"ok": False, "reason": f"Za mało tygodni ({len(y)}) — potrzeba co najmniej {MIN_POINTS + backtest // 2}."}
    ranking = evaluate(y, backtest)
    best = ranking[0]["model"]
    p, fitted, fc, sd = fit(best, y)
    fc_vals = [max(0.0, fc(h)) for h in range(1, horizon + 1)]
    band = [Z80 * sd * math.sqrt(h) for h in range(1, horizon + 1)]
    recent = statistics.fmean(y[-SEASON:])
    ahead = statistics.fmean(fc_vals[:SEASON]) if fc_vals else recent
    upper = statistics.fmean(v + b for v, b in zip(fc_vals[:SEASON], band[:SEASON], strict=True))
    g50 = ahead / recent - 1 if recent else 0.0
    g90 = upper / recent - 1 if recent else 0.0
    base = next(r for r in ranking if r["model"] == "trend_log")
    return {
        "ok": True, "version": VERSION, "chosen": best, "chosen_label": LABELS[best], "params": p,
        "ranking": ranking, "baseline_mape": base["mape"],
        "improvement_pp": (round(base["mape"] - ranking[0]["mape"], 2)
                           if base["mape"] is not None and ranking[0]["mape"] is not None else None),
        "labels": labels, "actual": y, "fitted": [round(v, 1) for v in fitted],
        "forecast": [round(v, 1) for v in fc_vals],
        "lower": [round(max(0.0, v - b), 1) for v, b in zip(fc_vals, band, strict=True)],
        "upper": [round(v + b, 1) for v, b in zip(fc_vals, band, strict=True)],
        "growth_p50_pct": round(100 * g50, 1), "growth_p90_pct": round(100 * g90, 1),
        "mult_p50": round(max(0.1, (1 + g50) ** years), 2), "mult_p90": round(max(0.1, (1 + g90) ** years), 2),
        "years": years, "weeks": len(y), "backtest": backtest,
    }


def _demo():
    """Samosprawdzenie: trend + sezon → Holt-Winters musi pobić baseline na danych sezonowych."""
    ys = [1000 + 4 * t + 150 * math.sin(2 * math.pi * t / SEASON) for t in range(2 * SEASON + 20)]
    r = run([(t, v) for t, v in enumerate(ys)])
    assert r["chosen"] == "hw_add", r["ranking"][:2]
    assert r["ranking"][0]["mape"] < r["baseline_mape"]


if __name__ == "__main__":
    _demo()
    print("forecast OK")
