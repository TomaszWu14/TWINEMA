# blender_route.py

> 12 nodes · cohesion 0.18

## Key Concepts

- **blender_stock.py** (24 connections) — `web/twin/blender_stock.py`
- **build_scene_for_model()** (16 connections) — `web/twin/blender_scene.py`
- **stock_for_scene()** (5 connections) — `web/masterdata/services.py`
- **load_stock_inputs()** (5 connections) — `web/twin/blender_stock.py`
- **window_source()** (4 connections) — `web/twin/blender_tasks.py`
- **_activity_picks()** (3 connections) — `web/twin/blender_scene.py`
- **Pozycje stanu jako dicty `build_pallets`: location, hu, sku, name, lot, expiry,…** (1 connections) — `web/masterdata/services.py`
- **Aktywność pickerów (picker, kod, materiał; kolejność = confirmed_at) → trasy.…** (1 connections) — `web/twin/blender_scene.py`
- **Scena dla `WarehouseModel`. `batch` = PickerActivityBatch (None → demo…** (1 connections) — `web/twin/blender_scene.py`
- **Rzeczywiste palety w lokalizacjach → scena Blendera („cyfrowe zdjęcie"…** (1 connections) — `web/twin/blender_stock.py`
- **Dane do `build_pallets`: (wiersze migawki, stany, aktywność). Stany = najnowszy…** (1 connections) — `web/twin/blender_stock.py`
- **Opis źródła wózków do `scene.source` (odtwarzacz pokazuje go pod animacją).** (1 connections) — `web/twin/blender_tasks.py`

## Relationships

- [warehouse_blender.py](warehouse_blender.py.md) (8 shared connections)
- [blender_scene.py](blender_scene.py.md) (6 shared connections)
- [SlotLocator](SlotLocator.md) (4 shared connections)
- [blender_stock.py](blender_stock.py.md) (3 shared connections)
- [ewm_levels.py](ewm_levels.py.md) (3 shared connections)
- [test_dane.py](test_dane.py.md) (2 shared connections)
- [twin/models.py](twin-models.py.md) (2 shared connections)
- [test_voice.py](test_voice.py.md) (1 shared connections)
- [masterdata/views.py](masterdata-views.py.md) (1 shared connections)
- [._scene](_scene.md) (1 shared connections)
- [studio/api.py](studio-api.py.md) (1 shared connections)
- [ml/views.py](ml-views.py.md) (1 shared connections)

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