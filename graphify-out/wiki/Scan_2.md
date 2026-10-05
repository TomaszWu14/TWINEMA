# Scan

> God node · 23 connections · `web/twin/ewm_tasks.py`

**Community:** [StudioViewTests](StudioViewTests.md)

## Connections by Relation

### calls
- run_import() `EXTRACTED`
- ewm_tasks_preview() `EXTRACTED`
- .test_cp1250_semicolon_csv_with_title_line() `EXTRACTED`
- .test_missing_columns_yield_nothing() `EXTRACTED`
- .test_xls_rejected_with_hint() `EXTRACTED`
- .test_xlsx_with_excel_date_and_time_cells() `EXTRACTED`

### contains
- ewm_tasks.py `EXTRACTED`

### imports
- [warehouse_tasks.py](warehouse_tasks.py.md) `EXTRACTED`
- ewm_tasks_import.py `EXTRACTED`
- test_ewm_tasks_parser.py `EXTRACTED`

### method
- .__init__() `EXTRACTED`
- .__iter__() `EXTRACTED`
- .close() `EXTRACTED`
- .columns() `EXTRACTED`
- .stats() `EXTRACTED`
- ._count() `EXTRACTED`
- .unmapped_headers() `EXTRACTED`

### rationale_for
- Przebieg po pliku: nagłówek → mapowanie kolumn → wiersze sparsowane albo błędy,… `EXTRACTED`

### uses
- ValueParsingTests `INFERRED`
- RowTests `INFERRED`
- ScanFileTests `INFERRED`
- HeaderAliasTests `INFERRED`
- KindMappingTests `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*