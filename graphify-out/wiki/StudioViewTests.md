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

- [test_design_forecast.py](test_design_forecast.py.md) (4 shared connections)
- [WarehouseTaskBatch](WarehouseTaskBatch.md) (3 shared connections)
- [warehouse_tasks.py](warehouse_tasks.py.md) (2 shared connections)
- [simulate](simulate.md) (2 shared connections)
- [ForecastTests](ForecastTests.md) (2 shared connections)
- [scene-data.js](scene-data.js.md) (1 shared connections)
- [ScenarioViewTests](ScenarioViewTests.md) (1 shared connections)
- [sim/__init__.py](sim-__init__.py.md) (1 shared connections)

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