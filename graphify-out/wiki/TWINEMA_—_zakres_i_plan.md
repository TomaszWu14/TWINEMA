# TWINEMA — zakres i plan

> 18 nodes · cohesion 0.18

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
- **Koniec ruchu w gnieździe regału: (punkt dojazdu z alejki, środek gniazda,…** (1 connections) — `web/twin/blender_scene.py`
- **Przekazanie palety w przejeździe poprzecznym: przed tym czołem rzędu, które…** (1 connections) — `web/twin/blender_scene.py`
- **Demo VNA: AGV wozi paletę dok ↔ czoło rzędu, kombi przejmuje ją tam i odkłada w…** (1 connections) — `web/twin/blender_scene.py`
- **Gniazdo regału: środek boku `bay_idx` (0..n-1) na poziomie `level` (1 =…** (1 connections) — `web/twin/blender_scene.py`
- **Punkt obsługi gniazda z alejki: przód regału (−u_d), a gdy zablokowany — tył.** (1 connections) — `web/twin/blender_scene.py`
- **Kalibracja symulacji na obecnej hali (plan 2026-10-02, etap 6) — czysty Python.…** (1 connections) — `web/twin/design_calibration.py`
- **Koniec ruchu z `resolve_moves` → (punkt na posadzce, wysokość gniazda).** (1 connections) — `web/twin/design_calibration.py`

## Relationships

- [blender_scene.py](blender_scene.py.md) (17 shared connections)
- [kpi_facts](kpi_facts.md) (7 shared connections)
- [RenderMontageTests](RenderMontageTests.md) (5 shared connections)
- [test_ewm_tasks_flow.py](test_ewm_tasks_flow.py.md) (4 shared connections)
- [simulate](simulate.md) (2 shared connections)
- [shared.py](shared.py.md) (2 shared connections)
- [site.py](site.py.md) (1 shared connections)
- [scenario/models.py](scenario-models.py.md) (1 shared connections)
- [views_sim.py](views_sim.py.md) (1 shared connections)
- [packaging.py](packaging.py.md) (1 shared connections)
- [layout-editor.js](layout-editor.js.md) (1 shared connections)
- [twin/models.py](twin-models.py.md) (1 shared connections)

## Source Files

- `web/twin/blender_route.py`
- `web/twin/blender_scene.py`
- `web/twin/design_calibration.py`

## Audit Trail

- EXTRACTED: 97 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*