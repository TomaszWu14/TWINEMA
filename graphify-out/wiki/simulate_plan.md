# simulate_plan

> 35 nodes · cohesion 0.08

## Key Concepts

- **FloorGrid** (20 connections) — `web/twin/blender_route.py`
- **BlenderExportViewTests** (10 connections) — `web/twin/tests/test_blender_export.py`
- **BuildSceneTests** (9 connections) — `web/twin/tests/test_blender_export.py`
- **.route()** (7 connections) — `web/twin/blender_route.py`
- **_scene()** (7 connections) — `web/twin/tests/test_blender_export.py`
- **.__init__()** (6 connections) — `web/twin/blender_route.py`
- **RouteGeometryTests** (6 connections) — `web/twin/tests/test_blender_export.py`
- **.nearest_free()** (5 connections) — `web/twin/blender_route.py`
- **.cell_of()** (4 connections) — `web/twin/blender_route.py`
- **._get()** (4 connections) — `web/twin/tests/test_blender_export.py`
- **._astar()** (3 connections) — `web/twin/blender_route.py`
- **.center()** (3 connections) — `web/twin/blender_route.py`
- **._clamp_i()** (3 connections) — `web/twin/blender_route.py`
- **._clamp_j()** (3 connections) — `web/twin/blender_route.py`
- **.is_free()** (3 connections) — `web/twin/blender_route.py`
- **_simplify()** (3 connections) — `web/twin/blender_route.py`
- **.test_inbound_pallet_ends_in_rack_outbound_vanishes_at_dock()** (3 connections) — `web/twin/tests/test_blender_export.py`
- **.test_route_never_crosses_a_rack()** (3 connections) — `web/twin/tests/test_blender_export.py`
- **.test_unreachable_target_falls_back_to_straight_line()** (3 connections) — `web/twin/tests/test_blender_export.py`
- **_dedupe()** (2 connections) — `web/twin/blender_route.py`
- **.test_bad_forklift_param_falls_back()** (2 connections) — `web/twin/tests/test_blender_export.py`
- **.test_demo_export_is_downloadable_json()** (2 connections) — `web/twin/tests/test_blender_export.py`
- **.test_requires_login()** (2 connections) — `web/twin/tests/test_blender_export.py`
- **.test_carried_pallet_rides_on_forks()** (2 connections) — `web/twin/tests/test_blender_export.py`
- **.test_deterministic_for_same_model()** (2 connections) — `web/twin/tests/test_blender_export.py`
- *... and 10 more nodes in this community*

## Relationships

- [twin/models.py](twin-models.py.md) (6 shared connections)
- [blender_scene.py](blender_scene.py.md) (5 shared connections)
- [kpi_facts](kpi_facts.md) (3 shared connections)
- [ADR-0001: Kopia kodu modelowania magazynu, nie przeniesienie](ADR-0001-_Kopia_kodu_modelowania_magazynu%2C_nie_przeniesienie.md) (3 shared connections)
- [scenario/models.py](scenario-models.py.md) (1 shared connections)
- [design_kpi.py](design_kpi.py.md) (1 shared connections)

## Source Files

- `web/twin/blender_route.py`
- `web/twin/tests/test_blender_export.py`

## Audit Trail

- EXTRACTED: 126 (95%)
- INFERRED: 7 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*