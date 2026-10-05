# StudioViewTests

> 16 nodes · cohesion 0.13

## Key Concepts

- **WarehouseTask** (15 connections) — `web/twin/models_tasks.py`
- **ForecastViewTests** (8 connections) — `web/twin/tests/test_design_forecast.py`
- **MlRunTests** (6 connections) — `web/ml/tests/test_ml.py`
- **.setUpTestData()** (3 connections) — `web/twin/tests/test_design_forecast.py`
- **.setUpTestData()** (3 connections) — `web/twin/tests/test_design_sim.py`
- **.setUpTestData()** (2 connections) — `web/ml/tests/test_ml.py`
- **Meta** (2 connections) — `web/twin/models_tasks.py`
- **.test_home_lists_runs()** (1 connections) — `web/ml/tests/test_ml.py`
- **.test_segmentation_run_and_csv()** (1 connections) — `web/ml/tests/test_ml.py`
- **.test_viewer_cannot_run_designer_can_and_run_is_recorded()** (1 connections) — `web/ml/tests/test_ml.py`
- **TestCase** (1 connections)
- **.__str__()** (1 connections) — `web/twin/models_tasks.py`
- **.setUp()** (1 connections) — `web/twin/tests/test_design_forecast.py`
- **.test_page_shows_multiplier_and_links()** (1 connections) — `web/twin/tests/test_design_forecast.py`
- **.test_profile_links_to_forecast()** (1 connections) — `web/twin/tests/test_design_forecast.py`
- **TestCase** (1 connections)

## Relationships

- [WarehouseTask](WarehouseTask.md) (4 shared connections)
- [shared.py](shared.py.md) (3 shared connections)
- [warehouse_tasks.py](warehouse_tasks.py.md) (2 shared connections)
- [simulate](simulate.md) (2 shared connections)
- [test_ml.py](test_ml.py.md) (2 shared connections)
- [roles.py](roles.py.md) (1 shared connections)
- [ScenarioViewTests](ScenarioViewTests.md) (1 shared connections)
- [test_layout_structure.py](test_layout_structure.py.md) (1 shared connections)

## Source Files

- `web/ml/tests/test_ml.py`
- `web/twin/models_tasks.py`
- `web/twin/tests/test_design_forecast.py`
- `web/twin/tests/test_design_sim.py`

## Audit Trail

- EXTRACTED: 39 (81%)
- INFERRED: 9 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*