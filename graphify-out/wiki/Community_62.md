# Community 62

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

- [Community 0](Community_0.md) (8 shared connections)
- [Community 11](Community_11.md) (6 shared connections)
- [Community 48](Community_48.md) (4 shared connections)
- [Community 74](Community_74.md) (3 shared connections)
- [Community 22](Community_22.md) (3 shared connections)
- [Community 9](Community_9.md) (2 shared connections)
- [Community 8](Community_8.md) (2 shared connections)
- [Community 21](Community_21.md) (1 shared connections)
- [Community 41](Community_41.md) (1 shared connections)
- [Community 58](Community_58.md) (1 shared connections)
- [Community 2](Community_2.md) (1 shared connections)
- [Community 16](Community_16.md) (1 shared connections)

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