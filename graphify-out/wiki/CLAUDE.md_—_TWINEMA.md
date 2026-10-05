# CLAUDE.md — TWINEMA

> 14 nodes · cohesion 0.22

## Key Concepts

- **test_ewm_tasks_parser.py** (15 connections) — `web/twin/tests/test_ewm_tasks_parser.py`
- **parse_stamp()** (12 connections) — `web/twin/ewm_tasks.py`
- **ValueParsingTests** (10 connections) — `web/twin/tests/test_ewm_tasks_parser.py`
- **parse_number()** (5 connections) — `web/twin/ewm_tasks.py`
- **.test_empty_and_bad_dates()** (2 connections) — `web/twin/tests/test_ewm_tasks_parser.py`
- **.test_excel_cells_date_midnight_plus_time()** (2 connections) — `web/twin/tests/test_ewm_tasks_parser.py`
- **.test_numbers_polish_english_sap()** (2 connections) — `web/twin/tests/test_ewm_tasks_parser.py`
- **.test_sap_timestamp_and_iso()** (2 connections) — `web/twin/tests/test_ewm_tasks_parser.py`
- **.test_separate_date_and_time_columns()** (2 connections) — `web/twin/tests/test_ewm_tasks_parser.py`
- **.test_timestamp_only_in_time_column()** (2 connections) — `web/twin/tests/test_ewm_tasks_parser.py`
- **.test_timezone_local_vs_utc()** (2 connections) — `web/twin/tests/test_ewm_tasks_parser.py`
- **„1.234,5” / „1,234.5” / „1 234,5” / „5-” (minus SAP na końcu) / liczba → float;…** (1 connections) — `web/twin/ewm_tasks.py`
- **Data (+ osobny czas, jak w eksporcie SAP) → datetime ze strefą `tz` albo None.** (1 connections) — `web/twin/ewm_tasks.py`
- **Parser eksportu zadań magazynowych EWM (WT): aliasy nagłówków, liczby, daty,…** (1 connections) — `web/twin/tests/test_ewm_tasks_parser.py`

## Relationships

- [warehouse_blender.py](warehouse_blender.py.md) (5 shared connections)
- [Shot](Shot.md) (4 shared connections)
- [Pochodzenie kodu](Pochodzenie_kodu.md) (4 shared connections)
- [studio/views.py](studio-views.py.md) (3 shared connections)
- [layout-core.js](layout-core.js.md) (3 shared connections)

## Source Files

- `web/twin/ewm_tasks.py`
- `web/twin/tests/test_ewm_tasks_parser.py`

## Audit Trail

- EXTRACTED: 58 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*