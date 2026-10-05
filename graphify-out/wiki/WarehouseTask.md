# WarehouseTask

> 15 nodes · cohesion 0.23

## Key Concepts

- **Scan** (23 connections) — `web/twin/ewm_tasks.py`
- **ScanFileTests** (8 connections) — `web/twin/tests/test_ewm_tasks_parser.py`
- **.__iter__()** (4 connections) — `web/twin/ewm_tasks.py`
- **._file()** (4 connections) — `web/twin/tests/test_ewm_tasks_parser.py`
- **.columns()** (3 connections) — `web/twin/ewm_tasks.py`
- **.stats()** (3 connections) — `web/twin/ewm_tasks.py`
- **.test_cp1250_semicolon_csv_with_title_line()** (3 connections) — `web/twin/tests/test_ewm_tasks_parser.py`
- **.test_missing_columns_yield_nothing()** (3 connections) — `web/twin/tests/test_ewm_tasks_parser.py`
- **.test_xls_rejected_with_hint()** (3 connections) — `web/twin/tests/test_ewm_tasks_parser.py`
- **._count()** (2 connections) — `web/twin/ewm_tasks.py`
- **.unmapped_headers()** (2 connections) — `web/twin/ewm_tasks.py`
- **.test_xlsx_with_excel_date_and_time_cells()** (2 connections) — `web/twin/tests/test_ewm_tasks_parser.py`
- **Przebieg po pliku: nagłówek → mapowanie kolumn → wiersze sparsowane albo błędy,…** (1 connections) — `web/twin/ewm_tasks.py`
- **Poprawne, nieanulowane zadania (dicty pól modelu).** (1 connections) — `web/twin/ewm_tasks.py`
- **[(etykieta pola, nagłówek z pliku)] w kolejności pól.** (1 connections) — `web/twin/ewm_tasks.py`

## Relationships

- [warehouse_tasks.py](warehouse_tasks.py.md) (4 shared connections)
- [CLAUDE.md — TWINEMA](CLAUDE.md_%E2%80%94_TWINEMA.md) (3 shared connections)
- [Scan](Scan.md) (2 shared connections)
- [studio/views.py](studio-views.py.md) (2 shared connections)
- [PROVENANCE.md](PROVENANCE.md.md) (2 shared connections)
- [studio/models.py](studio-models.py.md) (2 shared connections)

## Source Files

- `web/twin/ewm_tasks.py`
- `web/twin/tests/test_ewm_tasks_parser.py`

## Audit Trail

- EXTRACTED: 57 (90%)
- INFERRED: 6 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*