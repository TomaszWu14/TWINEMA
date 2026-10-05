# Scenario

> 15 nodes · cohesion 0.18

## Key Concepts

- **build_pallets()** (10 connections) — `web/twin/blender_stock.py`
- **test_blender_stock.py** (10 connections) — `web/twin/tests/test_blender_stock.py`
- **abc_by_hits()** (9 connections) — `web/twin/blender_stock.py`
- **BuildPalletsTests** (6 connections) — `web/twin/tests/test_blender_stock.py`
- **ParseCodeTests** (6 connections) — `web/twin/tests/test_blender_stock.py`
- **SimpleTestCase** (3 connections)
- **.test_abc_thresholds()** (2 connections) — `web/twin/tests/test_blender_stock.py`
- **.test_sources_merge_by_location()** (2 connections) — `web/twin/tests/test_blender_stock.py`
- **.test_stock_without_snapshot_is_enough()** (2 connections) — `web/twin/tests/test_blender_stock.py`
- **Klasa ABC wg udziału w pobraniach (ta sama reguła progów co…** (1 connections) — `web/twin/blender_stock.py`
- **Czysta funkcja: dane wejściowe jako proste krotki/dicty → (pallets, stats,…** (1 connections) — `web/twin/blender_stock.py`
- **.test_four_part_builder_code()** (1 connections) — `web/twin/tests/test_blender_stock.py`
- **.test_garbage_is_none()** (1 connections) — `web/twin/tests/test_blender_stock.py`
- **.test_letter_encodes_column_and_level_like_3d_map()** (1 connections) — `web/twin/tests/test_blender_stock.py`
- **Palety w lokalizacjach (stan magazynu) w scenie Blendera —…** (1 connections) — `web/twin/tests/test_blender_stock.py`

## Relationships

- [ADR-0001: Kopia kodu modelowania magazynu, nie przeniesienie](ADR-0001-_Kopia_kodu_modelowania_magazynu%2C_nie_przeniesienie.md) (7 shared connections)
- [layout.py](layout.py.md) (4 shared connections)
- [ml/services.py](ml-services.py.md) (2 shared connections)
- [model_edit.py](model_edit.py.md) (2 shared connections)
- [blender_scene.py](blender_scene.py.md) (1 shared connections)
- [rack_corners](rack_corners.md) (1 shared connections)
- [kpi_facts](kpi_facts.md) (1 shared connections)

## Source Files

- `web/twin/blender_stock.py`
- `web/twin/tests/test_blender_stock.py`

## Audit Trail

- EXTRACTED: 54 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*