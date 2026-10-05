# layout.py

> 11 nodes · cohesion 0.18

## Key Concepts

- **blender_stock.py** (24 connections) — `web/twin/blender_stock.py`
- **build_scene_for_model()** (17 connections) — `web/twin/blender_scene.py`
- **stock_for_scene()** (5 connections) — `web/masterdata/services.py`
- **load_stock_inputs()** (5 connections) — `web/twin/blender_stock.py`
- **window_source()** (4 connections) — `web/twin/blender_tasks.py`
- **_activity_picks()** (3 connections) — `web/twin/blender_scene.py`
- **Aktywność pickerów (picker, kod, materiał; kolejność = confirmed_at) → trasy.…** (1 connections) — `web/twin/blender_scene.py`
- **Scena dla `WarehouseModel`. `batch` = PickerActivityBatch (None → demo…** (1 connections) — `web/twin/blender_scene.py`
- **Rzeczywiste palety w lokalizacjach → scena Blendera („cyfrowe zdjęcie"…** (1 connections) — `web/twin/blender_stock.py`
- **Dane do `build_pallets`: (wiersze migawki, stany, aktywność). Stany = najnowszy…** (1 connections) — `web/twin/blender_stock.py`
- **Opis źródła wózków do `scene.source` (odtwarzacz pokazuje go pod animacją).** (1 connections) — `web/twin/blender_tasks.py`

## Relationships

- [warehouse_design_sim.py](warehouse_design_sim.py.md) (8 shared connections)
- [build_scene](build_scene.md) (6 shared connections)
- [Scenario](Scenario.md) (4 shared connections)
- [packaging.py](packaging.py.md) (3 shared connections)
- [ewm_levels.py](ewm_levels.py.md) (3 shared connections)
- [masterdata/services.py](masterdata-services.py.md) (2 shared connections)
- [twin/models.py](twin-models.py.md) (2 shared connections)
- [test_voice.py](test_voice.py.md) (1 shared connections)
- [masterdata/views.py](masterdata-views.py.md) (1 shared connections)
- [render/views.py](render-views.py.md) (1 shared connections)
- [studio/api.py](studio-api.py.md) (1 shared connections)
- [blender_stock.py](blender_stock.py.md) (1 shared connections)

## Source Files

- `web/masterdata/services.py`
- `web/twin/blender_scene.py`
- `web/twin/blender_stock.py`
- `web/twin/blender_tasks.py`

## Audit Trail

- EXTRACTED: 63 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*