# warehouse_model.py

> 5 nodes · cohesion 0.40

## Key Concepts

- **load_groups()** (7 connections) — `web/twin/design_day.py`
- **groups_for()** (4 connections) — `web/masterdata/services.py`
- **.test_groups_for_design_day()** (2 connections) — `web/masterdata/tests/test_dane.py`
- **{materiał: grupa towarowa} albo None, gdy materiałów jeszcze nie zaimportowano.…** (1 connections) — `web/masterdata/services.py`
- **{materiał z zadań: grupa towarowa} z modułu Dane; None, gdy materiałów jeszcze…** (1 connections) — `web/twin/design_day.py`

## Relationships

- [model_edit.py](model_edit.py.md) (2 shared connections)
- [masterdata/services.py](masterdata-services.py.md) (2 shared connections)
- [WarehouseTaskBatch](WarehouseTaskBatch.md) (2 shared connections)
- [test_voice.py](test_voice.py.md) (1 shared connections)

## Source Files

- `web/masterdata/services.py`
- `web/masterdata/tests/test_dane.py`
- `web/twin/design_day.py`

## Audit Trail

- EXTRACTED: 15 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*