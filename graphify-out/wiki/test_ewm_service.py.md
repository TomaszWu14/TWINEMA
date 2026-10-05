# test_ewm_service.py

> 24 nodes · cohesion 0.12

## Key Concepts

- **test_ewm_service.py** (18 connections) — `web/twin/tests/test_ewm_service.py`
- **WarehouseLocationMasterBatch** (12 connections) — `web/twin/models.py`
- **WarehouseLocationMaster** (10 connections) — `web/twin/models.py`
- **make_model_and_master()** (9 connections) — `web/twin/tests/test_ewm_service.py`
- **test_ewm_views.py** (8 connections) — `web/twin/tests/test_ewm_views.py`
- **locations.py** (7 connections) — `web/twin/locations.py`
- **ServiceTests** (6 connections) — `web/twin/tests/test_ewm_service.py`
- **load_sample()** (4 connections) — `web/twin/tests/ewm_sample.py`
- **ewm_sample.py** (3 connections) — `web/twin/tests/ewm_sample.py`
- **active_master_qs()** (2 connections) — `web/twin/locations.py`
- **.test_detect_apply_and_compliance_is_100_percent()** (2 connections) — `web/twin/tests/test_ewm_service.py`
- **.test_master_rows_filters_by_zone_and_active_master()** (2 connections) — `web/twin/tests/test_ewm_service.py`
- **.test_rack_without_template_and_missing_master()** (2 connections) — `web/twin/tests/test_ewm_service.py`
- **.test_second_detect_reuses_templates_and_replaces_overrides()** (2 connections) — `web/twin/tests/test_ewm_service.py`
- **Kody lokalizacji magazynu — wspólna konwencja mapy 3D / eksportu SAP. Litera na…** (1 connections) — `web/twin/locations.py`
- **Lokalizacje z aktywnej partii master-daty (pusty queryset, gdy brak partii).…** (1 connections) — `web/twin/locations.py`
- **One import of location master data (height, volume, weight, type).** (1 connections) — `web/twin/models.py`
- **Master data for a single warehouse location.** (1 connections) — `web/twin/models.py`
- **.__str__()** (1 connections) — `web/twin/models.py`
- **Syntetyczna próbka mastera lokalizacji (hala B0) dla testów „Wykryj z EWM” i…** (1 connections) — `web/twin/tests/ewm_sample.py`
- **[(kod, typ EWM)] — kod B0-<rząd>-<gniazdo><pozycja palety><litera poziomu>.** (1 connections) — `web/twin/tests/ewm_sample.py`
- **TestCase** (1 connections)
- **Warstwa ORM części 1: zapis „Wykryj z EWM” + raport zgodności na syntetycznej…** (1 connections) — `web/twin/tests/test_ewm_service.py`
- **Ekrany „Wykryj z EWM” (podgląd → zapis) i „Zgodność z EWM” (+ XLSX), z rolami.** (1 connections) — `web/twin/tests/test_ewm_views.py`

## Relationships

- [twin/models.py](twin-models.py.md) (6 shared connections)
- [test_voice.py](test_voice.py.md) (4 shared connections)
- [EwmViewsTests](EwmViewsTests.md) (4 shared connections)
- [warehouse_variants.py](warehouse_variants.py.md) (3 shared connections)
- [SimViewTests](SimViewTests.md) (3 shared connections)
- [warehouse_model.py](warehouse_model.py.md) (2 shared connections)
- [BayTemplate](BayTemplate.md) (2 shared connections)
- [FloorGrid](FloorGrid.md) (2 shared connections)
- [views_sim.py](views_sim.py.md) (1 shared connections)
- [packaging.py](packaging.py.md) (1 shared connections)
- [masterdata/services.py](masterdata-services.py.md) (1 shared connections)
- [masterdata/views.py](masterdata-views.py.md) (1 shared connections)

## Source Files

- `web/twin/locations.py`
- `web/twin/models.py`
- `web/twin/tests/ewm_sample.py`
- `web/twin/tests/test_ewm_service.py`
- `web/twin/tests/test_ewm_views.py`

## Audit Trail

- EXTRACTED: 97 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*