# ADR-0001: Kopia kodu modelowania magazynu, nie przeniesienie

> 13 nodes · cohesion 0.28

## Key Concepts

- **SlotLocator** (33 connections) — `web/twin/blender_stock.py`
- **_inside()** (18 connections) — `web/twin/blender_route.py`
- **SlotLocatorTests** (11 connections) — `web/twin/tests/test_blender_stock.py`
- **.test_bays_ranked_and_lanes_inside_rack()** (3 connections) — `web/twin/tests/test_blender_stock.py`
- **.test_halves_split_the_cell_side_by_side()** (3 connections) — `web/twin/tests/test_blender_stock.py`
- **.test_physical_bays_spread_pallet_positions()** (3 connections) — `web/twin/tests/test_blender_stock.py`
- **.test_gh_split_x_vertically()** (2 connections) — `web/twin/tests/test_blender_stock.py`
- **.test_level_clamped_to_rack()** (2 connections) — `web/twin/tests/test_blender_stock.py`
- **.test_master_level_overrides_letter()** (2 connections) — `web/twin/tests/test_blender_stock.py`
- **.test_shelves_bcd_stack_vertically_in_level_one()** (2 connections) — `web/twin/tests/test_blender_stock.py`
- **.test_unknown_rack_is_none()** (2 connections) — `web/twin/tests/test_blender_stock.py`
- **Czy punkt leży w obrysie regału poszerzonym o `margin` [m].** (1 connections) — `web/twin/blender_route.py`
- **Kod lokalizacji → gniazdo w regale modelu (środek palety, wysokość, obrót).…** (1 connections) — `web/twin/blender_stock.py`

## Relationships

- [SlotLocator](SlotLocator.md) (7 shared connections)
- [.slot](slot.md) (4 shared connections)
- [FloorGrid](FloorGrid.md) (3 shared connections)
- [twin/models.py](twin-models.py.md) (3 shared connections)
- [EquipmentAgentsTests](EquipmentAgentsTests.md) (3 shared connections)
- [CalibrationViewTests](CalibrationViewTests.md) (3 shared connections)
- [resolve_moves](resolve_moves.md) (3 shared connections)
- [test_container_inbound.py](test_container_inbound.py.md) (2 shared connections)
- [warehouse_tasks.py](warehouse_tasks.py.md) (2 shared connections)
- [warehouse_design_sim.py](warehouse_design_sim.py.md) (2 shared connections)
- [script.py](script.py.md) (1 shared connections)
- [design_kpi.py](design_kpi.py.md) (1 shared connections)

## Source Files

- `web/twin/blender_route.py`
- `web/twin/blender_stock.py`
- `web/twin/tests/test_blender_stock.py`

## Audit Trail

- EXTRACTED: 74 (89%)
- INFERRED: 9 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*