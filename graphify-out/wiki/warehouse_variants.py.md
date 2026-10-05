# warehouse_variants.py

> 16 nodes · cohesion 0.15

## Key Concepts

- **ewm_service.py** (22 connections) — `web/twin/ewm_service.py`
- **expand_model()** (9 connections) — `web/twin/addressing.py`
- **detect_for_model()** (7 connections) — `web/twin/ewm_service.py`
- **apply_proposal()** (6 connections) — `web/twin/ewm_service.py`
- **warehouse_model_detect_save()** (6 connections) — `web/twin/views/warehouse_model_ewm.py`
- **master_rows()** (4 connections) — `web/twin/ewm_service.py`
- **plan_for_model()** (4 connections) — `web/twin/ewm_service.py`
- **atomic** (1 connections)
- **[(rząd, szablon, wyjątki), …] → (miejsca z kluczami zone/aisle, {kod: [„B0-07”,…** (1 connections) — `web/twin/addressing.py`
- **Warstwa ORM nad czystymi modułami adresowania: master EWM, plan modelu, zapis…** (1 connections) — `web/twin/ewm_service.py`
- **[(kod, typ EWM, wysokość mm, udźwig kg)] z mastera — tylko kody stref modelu.** (1 connections) — `web/twin/ewm_service.py`
- **Propozycja „Wykryj z EWM” dla rzędów modelu (nic nie zapisuje).** (1 connections) — `web/twin/ewm_service.py`
- **Zapis propozycji: nowe szablony, szablon domyślny + numeracja rzędów, wyjątki…** (1 connections) — `web/twin/ewm_service.py`
- **Rozwinięty plan modelu → (rzędy, miejsca, duplikaty).** (1 connections) — `web/twin/ewm_service.py`
- **_md_role** (1 connections)
- **require_POST** (1 connections)

## Relationships

- [warehouse_model_ewm.py](warehouse_model_ewm.py.md) (8 shared connections)
- [addressing.py](addressing.py.md) (3 shared connections)
- [load_groups](load_groups.md) (3 shared connections)
- [rack_corners](rack_corners.md) (3 shared connections)
- [EwmViewsTests](EwmViewsTests.md) (3 shared connections)
- [masterdata/services.py](masterdata-services.py.md) (2 shared connections)
- [test_container_inbound.py](test_container_inbound.py.md) (2 shared connections)
- [ewm_tasks.py](ewm_tasks.py.md) (2 shared connections)
- [twin/models.py](twin-models.py.md) (2 shared connections)
- [test_ml.py](test_ml.py.md) (2 shared connections)
- [BayTemplate](BayTemplate.md) (1 shared connections)

## Source Files

- `web/twin/addressing.py`
- `web/twin/ewm_service.py`
- `web/twin/views/warehouse_model_ewm.py`

## Audit Trail

- EXTRACTED: 67 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*