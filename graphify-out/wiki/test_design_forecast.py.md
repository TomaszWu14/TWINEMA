# test_design_forecast.py

> 20 nodes · cohesion 0.20

## Key Concepts

- **test_design_forecast.py** (13 connections) — `web/twin/tests/test_design_forecast.py`
- **forecast()** (12 connections) — `web/twin/design_forecast.py`
- **ForecastTests** (11 connections) — `web/twin/tests/test_design_forecast.py`
- **_daily()** (9 connections) — `web/twin/tests/test_design_forecast.py`
- **backtest()** (6 connections) — `web/twin/design_forecast.py`
- **fit()** (6 connections) — `web/twin/design_forecast.py`
- **_total()** (5 connections) — `web/twin/tests/test_design_forecast.py`
- **.test_backtest_small_error_on_clean_trend()** (4 connections) — `web/twin/tests/test_design_forecast.py`
- **.test_flat_history_gives_multiplier_one()** (4 connections) — `web/twin/tests/test_design_forecast.py`
- **.test_p90_is_above_p50_with_noise()** (4 connections) — `web/twin/tests/test_design_forecast.py`
- **.test_recovers_known_growth()** (4 connections) — `web/twin/tests/test_design_forecast.py`
- **.test_short_history_is_flagged()** (4 connections) — `web/twin/tests/test_design_forecast.py`
- **.test_partial_weeks_and_weekends_are_dropped()** (3 connections) — `web/twin/tests/test_design_forecast.py`
- **.test_fit_slope_is_log_weekly_rate()** (2 connections) — `web/twin/tests/test_design_forecast.py`
- **series: [(dzień porządkowy, wartość)] → (nachylenie log/tydzień, wyraz wolny,…** (1 connections) — `web/twin/design_forecast.py`
- **MAPE [%] prognozy ostatnich `weeks` tygodni z modelu uczonego bez nich (None —…** (1 connections) — `web/twin/design_forecast.py`
- **Wzrost per strumień: roczne tempo P50/P90, mnożnik na `years` lat, MAPE testu…** (1 connections) — `web/twin/design_forecast.py`
- **SimpleTestCase** (1 connections)
- **Prognoza wzrostu z historii zadań EWM (plan 2026-10-02, etap 5).** (1 connections) — `web/twin/tests/test_design_forecast.py`
- **Dni robocze (pn–pt) z wykładniczym wzrostem `growth_year` rocznie; weekendy…** (1 connections) — `web/twin/tests/test_design_forecast.py`

## Relationships

- [shared.py](shared.py.md) (5 shared connections)
- [day-timeline.js](day-timeline.js.md) (4 shared connections)
- [ml/services.py](ml-services.py.md) (4 shared connections)
- [StudioViewTests](StudioViewTests.md) (4 shared connections)

## Source Files

- `web/twin/design_forecast.py`
- `web/twin/tests/test_design_forecast.py`

## Audit Trail

- EXTRACTED: 91 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*