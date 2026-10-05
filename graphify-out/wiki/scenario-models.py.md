# scenario/models.py

> 48 nodes · cohesion 0.07

## Key Concepts

- **warehouse_model.py** (31 connections) — `web/twin/views/warehouse_model.py`
- **rack_corners()** (22 connections) — `web/twin/blender_route.py`
- **test_model_geometry.py** (11 connections) — `web/twin/tests/test_model_geometry.py`
- **parse_geometry_csv()** (9 connections) — `web/twin/model_geometry.py`
- **active_master()** (8 connections) — `web/twin/ewm_service.py`
- **model_geometry.py** (7 connections) — `web/twin/model_geometry.py`
- **floor_size()** (7 connections) — `web/twin/model_geometry.py`
- **hall_feature_kinds()** (7 connections) — `web/twin/shared.py`
- **GeometryUploadTests** (7 connections) — `web/twin/tests/test_model_geometry.py`
- **_create_from_geometry()** (7 connections) — `web/twin/views/warehouse_model.py`
- **is_geometry_csv()** (6 connections) — `web/twin/model_geometry.py`
- **_parse_location_code()** (6 connections) — `web/twin/shared.py`
- **save_hall_features()** (6 connections) — `web/twin/shared.py`
- **GeometryParserTests** (6 connections) — `web/twin/tests/test_model_geometry.py`
- **warehouse_model_paste()** (6 connections) — `web/twin/views/warehouse_model.py`
- **warehouse_model_view()** (6 connections) — `web/twin/views/warehouse_model.py`
- **_features_data()** (5 connections) — `web/twin/views/warehouse_model.py`
- **_md_role** (5 connections)
- **.test_floor_fits_rotated_racks()** (4 connections) — `web/twin/tests/test_model_geometry.py`
- **._upload()** (4 connections) — `web/twin/tests/test_model_geometry.py`
- **_parse_pasted_codes()** (4 connections) — `web/twin/views/warehouse_model.py`
- **warehouse_model_features()** (4 connections) — `web/twin/views/warehouse_model.py`
- **warehouse_model_coords()** (3 connections) — `web/twin/views/warehouse_model.py`
- **_num()** (2 connections) — `web/twin/model_geometry.py`
- **.test_detects_geometry_header_not_location_codes()** (2 connections) — `web/twin/tests/test_model_geometry.py`
- *... and 23 more nodes in this community*

## Relationships

- [WarehouseModel](WarehouseModel.md) (12 shared connections)
- [WarehouseTaskBatch](WarehouseTaskBatch.md) (11 shared connections)
- [kpi_facts](kpi_facts.md) (3 shared connections)
- [layout](layout.md) (3 shared connections)
- [warehouse_variants.py](warehouse_variants.py.md) (3 shared connections)
- [warehouse_model_ewm.py](warehouse_model_ewm.py.md) (3 shared connections)
- [layout-panels.js](layout-panels.js.md) (3 shared connections)
- [ParseTests](ParseTests.md) (2 shared connections)
- [TWINEMA — zakres i plan](TWINEMA_%E2%80%94_zakres_i_plan.md) (1 shared connections)
- [test_outbound.py](test_outbound.py.md) (1 shared connections)
- [blender_scene.py](blender_scene.py.md) (1 shared connections)
- [design_catalog.py](design_catalog.py.md) (1 shared connections)

## Source Files

- `web/twin/blender_route.py`
- `web/twin/ewm_service.py`
- `web/twin/model_geometry.py`
- `web/twin/shared.py`
- `web/twin/tests/test_model_geometry.py`
- `web/twin/views/warehouse_model.py`

## Audit Trail

- EXTRACTED: 208 (96%)
- INFERRED: 8 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*