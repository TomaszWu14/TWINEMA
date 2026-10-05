# equipment/models.py

> 45 nodes · cohesion 0.07

## Key Concepts

- **RenderJob** (15 connections) — `web/render/models.py`
- **render/api.py** (14 connections) — `web/render/api.py`
- **render/views.py** (12 connections) — `web/render/views.py`
- **_scene_from_request()** (12 connections) — `web/twin/views/warehouse_blender.py`
- **worker_required()** (11 connections) — `web/render/api.py`
- **render/models.py** (9 connections) — `web/render/models.py`
- **_forbidden()** (8 connections) — `web/render/api.py`
- **RenderJobForm** (8 connections) — `web/render/views.py`
- **scene()** (6 connections) — `web/render/api.py`
- **fail()** (5 connections) — `web/render/api.py`
- **result()** (5 connections) — `web/render/api.py`
- **create()** (5 connections) — `web/render/views.py`
- **claim()** (4 connections) — `web/render/api.py`
- **_claimed_job()** (4 connections) — `web/render/api.py`
- **warehouse_model_blender_json()** (4 connections) — `web/twin/views/warehouse_blender.py`
- **warehouse_model_flow_json()** (4 connections) — `web/twin/views/warehouse_blender.py`
- **require_POST** (3 connections)
- **requeue_stale()** (3 connections) — `web/render/api.py`
- **render/urls.py** (3 connections) — `web/render/urls.py`
- **delete()** (3 connections) — `web/render/views.py`
- **jobs()** (3 connections) — `web/render/views.py`
- **any_role** (3 connections)
- **.scene_query()** (3 connections) — `web/render/views.py`
- **status_json()** (3 connections) — `web/render/views.py`
- **Meta** (2 connections) — `web/render/views.py`
- *... and 20 more nodes in this community*

## Relationships

- [load_groups](load_groups.md) (6 shared connections)
- [scene-data.js](scene-data.js.md) (3 shared connections)
- [twin/models.py](twin-models.py.md) (2 shared connections)
- [views_sim.py](views_sim.py.md) (1 shared connections)

## Source Files

- `web/render/__init__.py`
- `web/render/api.py`
- `web/render/models.py`
- `web/render/urls.py`
- `web/render/views.py`
- `web/twin/views/warehouse_blender.py`

## Audit Trail

- EXTRACTED: 172 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*