# SlotLocator

> God node · 33 connections · `web/twin/blender_stock.py`

**Community:** [ADR-0001: Kopia kodu modelowania magazynu, nie przeniesienie](ADR-0001-_Kopia_kodu_modelowania_magazynu%2C_nie_przeniesienie.md)

## Connections by Relation

### calls
- build_pallets() `EXTRACTED`
- ewm_tasks_calibration() `EXTRACTED`
- ._scene() `EXTRACTED`
- location_report() `EXTRACTED`
- .test_bays_ranked_and_lanes_inside_rack() `EXTRACTED`
- .test_halves_split_the_cell_side_by_side() `EXTRACTED`
- .test_physical_bays_spread_pallet_positions() `EXTRACTED`
- .setUp() `EXTRACTED`
- .setUp() `EXTRACTED`
- .test_gh_split_x_vertically() `EXTRACTED`
- .test_level_clamped_to_rack() `EXTRACTED`
- .test_master_level_overrides_letter() `EXTRACTED`
- .test_shelves_bcd_stack_vertically_in_level_one() `EXTRACTED`
- .test_unknown_rack_is_none() `EXTRACTED`

### contains
- [blender_stock.py](blender_stock.py.md) `EXTRACTED`

### imports
- [test_design_calibration.py](test_design_calibration.py.md) `EXTRACTED`
- test_ewm_tasks_flow.py `EXTRACTED`
- warehouse_calibration.py `EXTRACTED`
- ewm_tasks_import.py `EXTRACTED`
- test_blender_stock.py `EXTRACTED`

### method
- .slot() `EXTRACTED`
- ._parse() `EXTRACTED`
- .__init__() `EXTRACTED`
- .rack_and_bay() `EXTRACTED`

### rationale_for
- Kod lokalizacji → gniazdo w regale modelu (środek palety, wysokość, obrót).… `EXTRACTED`

### uses
- [TasksEndpointAndImportTests](TasksEndpointAndImportTests.md) `INFERRED`
- SlotLocatorTests `INFERRED`
- [CalibrationTests](CalibrationTests.md) `INFERRED`
- CalibrationViewTests `INFERRED`
- ResolveMovesTests `INFERRED`
- SceneFromTasksTests `INFERRED`
- BuildPalletsTests `INFERRED`
- ParseCodeTests `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*