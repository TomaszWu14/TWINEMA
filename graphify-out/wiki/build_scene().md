# build_scene()

> God node · 24 connections · `web/twin/blender_scene.py`

**Community:** [blender_scene.py](blender_scene.py.md)

## Connections by Relation

### calls
- [Agent](Agent.md) `EXTRACTED`
- build_scene_for_model() `EXTRACTED`
- _relay_task() `EXTRACTED`
- _scene() `EXTRACTED`
- _vna_racks() `EXTRACTED`
- _scene() `EXTRACTED`
- .free_point() `EXTRACTED`
- _task_forklifts() `EXTRACTED`
- ._scene() `EXTRACTED`
- _is_shelf() `EXTRACTED`
- _Ctx `EXTRACTED`
- _picker_route() `EXTRACTED`
- _scene() `EXTRACTED`
- _forklift_task() `EXTRACTED`
- _handover() `EXTRACTED`
- _container_flow() `EXTRACTED`
- _demo_picks() `EXTRACTED`
- .test_no_racks_gives_static_scene() `EXTRACTED`

### contains
- [blender_scene.py](blender_scene.py.md) `EXTRACTED`

### imports
- test_ewm_tasks_flow.py `EXTRACTED`
- test_blender_export.py `EXTRACTED`
- test_container_inbound.py `EXTRACTED`
- test_equipment_agents.py `EXTRACTED`

### rationale_for
- Składa scenę. `picks` = \[(nazwa_pickera, \[(rack, bay_idx, level, sku), …\]), …\]… `EXTRACTED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*