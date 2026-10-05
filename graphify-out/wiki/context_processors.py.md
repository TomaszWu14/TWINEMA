# context_processors.py

> 9 nodes · cohesion 0.18

## Key Concepts

- **blender_stock.py** (24 connections) — `web/twin/blender_stock.py`
- **build_scene_for_model()** (17 connections) — `web/twin/blender_scene.py`
- **stock_for_scene()** (5 connections) — `web/masterdata/services.py`
- **load_stock_inputs()** (5 connections) — `web/twin/blender_stock.py`
- **window_source()** (4 connections) — `web/twin/blender_tasks.py`
- **_activity_picks()** (3 connections) — `web/twin/blender_scene.py`
- **Rzeczywiste palety w lokalizacjach → scena Blendera („cyfrowe zdjęcie"…** (1 connections) — `web/twin/blender_stock.py`
- **Dane do `build_pallets`: (wiersze migawki, stany, aktywność). Stany = najnowszy…** (1 connections) — `web/twin/blender_stock.py`
- **Opis źródła wózków do `scene.source` (odtwarzacz pokazuje go pod animacją).** (1 connections) — `web/twin/blender_tasks.py`

## Relationships

- [scenario/services.py](scenario-services.py.md) (8 shared connections)
- [blender_scene.py](blender_scene.py.md) (6 shared connections)
- [scenario/models.py](scenario-models.py.md) (4 shared connections)
- [masterdata/views.py](masterdata-views.py.md) (3 shared connections)
- [ewm_levels.py](ewm_levels.py.md) (3 shared connections)
- [test_showcase.py](test_showcase.py.md) (2 shared connections)
- [twin/models.py](twin-models.py.md) (2 shared connections)
- [test_voice.py](test_voice.py.md) (1 shared connections)
- [Equipment](Equipment.md) (1 shared connections)
- [layout-hall.js](layout-hall.js.md) (1 shared connections)
- [RenderJob](RenderJob.md) (1 shared connections)
- [ml/services.py](ml-services.py.md) (1 shared connections)

## Source Files

- `web/masterdata/services.py`
- `web/twin/blender_scene.py`
- `web/twin/blender_stock.py`
- `web/twin/blender_tasks.py`

## Audit Trail

- EXTRACTED: 61 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*