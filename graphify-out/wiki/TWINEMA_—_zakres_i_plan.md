# TWINEMA — zakres i plan

> 13 nodes · cohesion 0.18

## Key Concepts

- **rack_point()** (17 connections) — `web/twin/blender_route.py`
- **design_calibration.py** (15 connections) — `web/twin/design_calibration.py`
- **_slot()** (11 connections) — `web/twin/blender_scene.py`
- **_relay_task()** (10 connections) — `web/twin/blender_scene.py`
- **_picker_route()** (7 connections) — `web/twin/blender_scene.py`
- **_rack_end()** (7 connections) — `web/twin/blender_scene.py`
- **_point()** (7 connections) — `web/twin/design_calibration.py`
- **_access()** (6 connections) — `web/twin/blender_scene.py`
- **_handover()** (6 connections) — `web/twin/blender_scene.py`
- **_manh()** (3 connections) — `web/twin/design_calibration.py`
- **Punkt hali: `along` [m] wzdłuż szerokości, `across` [m] wzdłuż głębokości…** (1 connections) — `web/twin/blender_route.py`
- **Kalibracja symulacji na obecnej hali (plan 2026-10-02, etap 6) — czysty Python.…** (1 connections) — `web/twin/design_calibration.py`
- **Koniec ruchu z `resolve_moves` → (punkt na posadzce, wysokość gniazda).** (1 connections) — `web/twin/design_calibration.py`

## Relationships

- [blender_scene.py](blender_scene.py.md) (17 shared connections)
- [kpi_facts](kpi_facts.md) (7 shared connections)
- [RenderMontageTests](RenderMontageTests.md) (5 shared connections)
- [resolve_moves](resolve_moves.md) (4 shared connections)
- [simulate](simulate.md) (2 shared connections)
- [test_sim.py](test_sim.py.md) (2 shared connections)
- [site.py](site.py.md) (1 shared connections)
- [day_demand](day_demand.md) (1 shared connections)
- [scenario/services.py](scenario-services.py.md) (1 shared connections)
- [packaging.py](packaging.py.md) (1 shared connections)
- [layout-site.js](layout-site.js.md) (1 shared connections)
- [twin/models.py](twin-models.py.md) (1 shared connections)

## Source Files

- `web/twin/blender_route.py`
- `web/twin/blender_scene.py`
- `web/twin/design_calibration.py`

## Audit Trail

- EXTRACTED: 92 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*