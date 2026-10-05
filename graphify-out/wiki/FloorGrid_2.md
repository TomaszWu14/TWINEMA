# FloorGrid

> God node · 20 connections · `web/twin/blender_route.py`

**Community:** [test_outbound.py](test_outbound.py.md)

## Connections by Relation

### calls
- .__init__() `EXTRACTED`
- .test_route_never_crosses_a_rack() `EXTRACTED`
- .test_unreachable_target_falls_back_to_straight_line() `EXTRACTED`

### contains
- blender_route.py `EXTRACTED`

### imports
- [blender_scene.py](blender_scene.py.md) `EXTRACTED`
- test_blender_export.py `EXTRACTED`

### method
- .route() `EXTRACTED`
- .__init__() `EXTRACTED`
- .nearest_free() `EXTRACTED`
- .cell_of() `EXTRACTED`
- ._astar() `EXTRACTED`
- .center() `EXTRACTED`
- ._clamp_i() `EXTRACTED`
- ._clamp_j() `EXTRACTED`
- .is_free() `EXTRACTED`

### rationale_for
- Siatka zajętości posadzki: komórka zablokowana, jeśli leży w obrysie regału.… `EXTRACTED`

### uses
- BlenderExportViewTests `INFERRED`
- BuildSceneTests `INFERRED`
- _Ctx `INFERRED`
- RouteGeometryTests `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*