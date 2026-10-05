# warehouse_model_ewm.py

> 17 nodes · cohesion 0.18

## Key Concepts

- **warehouse_model_ewm.py** (16 connections) — `web/twin/views/warehouse_model_ewm.py`
- **compliance_for_model()** (7 connections) — `web/twin/ewm_service.py`
- **_compliance_xlsx()** (5 connections) — `web/twin/views/warehouse_model_ewm.py`
- **warehouse_model_compliance()** (5 connections) — `web/twin/views/warehouse_model_ewm.py`
- **xlsx.py** (5 connections) — `web/twin/xlsx.py`
- **warehouse_model_detect()** (4 connections) — `web/twin/views/warehouse_model_ewm.py`
- **_finalize_xlsx()** (4 connections) — `web/twin/xlsx.py`
- **_make_xlsx_response()** (4 connections) — `web/twin/xlsx.py`
- **_safe()** (3 connections) — `web/twin/views/warehouse_model_ewm.py`
- **safe_cell()** (3 connections) — `web/twin/xlsx.py`
- **_planner** (2 connections)
- **Raport zgodności planu modelu z aktywnym masterem (batch=None → brak kodów EWM).** (1 connections) — `web/twin/ewm_service.py`
- **„Wykryj z EWM” (podgląd propozycji → zapis) i raport zgodności modelu z EWM (+…** (1 connections) — `web/twin/views/warehouse_model_ewm.py`
- **Ucieczka przed wstrzyknięciem formuły XLSX: string zaczynający się od =+-@…** (1 connections) — `web/twin/views/warehouse_model_ewm.py`
- **Eksport XLSX z neutralizacją formuł (CSV/formula injection).** (1 connections) — `web/twin/xlsx.py`
- **Tekst zaczynający się od = + - @ TAB CR → prefiks `'`. Liczby bez zmian.** (1 connections) — `web/twin/xlsx.py`
- **(workbook, worksheet, HttpResponse) gotowe do wypełnienia.** (1 connections) — `web/twin/xlsx.py`

## Relationships

- [model_racks](model_racks.md) (8 shared connections)
- [day_demand](day_demand.md) (3 shared connections)
- [shared.py](shared.py.md) (2 shared connections)
- [ewm_tasks.py](ewm_tasks.py.md) (1 shared connections)

## Source Files

- `web/twin/ewm_service.py`
- `web/twin/views/warehouse_model_ewm.py`
- `web/twin/xlsx.py`

## Audit Trail

- EXTRACTED: 64 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*