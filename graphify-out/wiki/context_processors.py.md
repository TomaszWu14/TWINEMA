# context_processors.py

> 22 nodes · cohesion 0.09

## Key Concepts

- **roles.py** (28 connections) — `web/core/roles.py`
- **test_ml.py** (11 connections) — `web/ml/tests/test_ml.py`
- **test_render.py** (8 connections) — `web/render/tests/test_render.py`
- **test_ewm_tasks_refresh.py** (6 connections) — `web/twin/tests/test_ewm_tasks_refresh.py`
- **has_role()** (4 connections) — `web/core/roles.py`
- **context_processors.py** (3 connections) — `web/core/context_processors.py`
- **Command** (3 connections) — `web/core/management/commands/create_roles.py`
- **MetaRefreshGuardTests** (3 connections) — `web/twin/tests/test_ewm_tasks_refresh.py`
- **user_roles()** (2 connections) — `web/core/context_processors.py`
- **create_roles.py** (2 connections) — `web/core/management/commands/create_roles.py`
- **role_required()** (2 connections) — `web/core/roles.py`
- **branding()** (1 connections) — `web/core/context_processors.py`
- **Flagi ról do szablonów — jedno zapytanie zamiast wielu has_role().** (1 connections) — `web/core/context_processors.py`
- **.handle()** (1 connections) — `web/core/management/commands/create_roles.py`
- **BaseCommand** (1 connections)
- **True dla superusera albo członka którejś z grup.** (1 connections) — `web/core/roles.py`
- **Dekorator: wymaga zalogowania + członkostwa w grupie (superuser zawsze…** (1 connections) — `web/core/roles.py`
- **ML1 prognoza + ML2 segmentacja: czyste moduły, zapis przebiegów, ekrany.** (1 connections) — `web/ml/tests/test_ml.py`
- **Kolejka renderów: API workera (token, przejęcie, scena, wynik) i ekran zleceń.** (1 connections) — `web/render/tests/test_render.py`
- **.test_no_screen_uses_meta_refresh()** (1 connections) — `web/twin/tests/test_ewm_tasks_refresh.py`
- **SimpleTestCase** (1 connections)
- **Audyt UX-004 (WCAG 2.2.1): szczegóły importu zadań EWM nie przeładowują się co…** (1 connections) — `web/twin/tests/test_ewm_tasks_refresh.py`

## Relationships

- [twin/models.py](twin-models.py.md) (6 shared connections)
- [ml/views.py](ml-views.py.md) (4 shared connections)
- [studio/api.py](studio-api.py.md) (3 shared connections)
- [pre-push](pre-push.md) (2 shared connections)
- [WorkerApiTests](WorkerApiTests.md) (2 shared connections)
- [test_foundation.py](test_foundation.py.md) (1 shared connections)
- [masterdata/services.py](masterdata-services.py.md) (1 shared connections)
- [StudioViewTests](StudioViewTests.md) (1 shared connections)
- [shared.py](shared.py.md) (1 shared connections)
- [forecast.py](forecast.py.md) (1 shared connections)
- [build_deck](build_deck.md) (1 shared connections)
- [draft_script](draft_script.md) (1 shared connections)

## Source Files

- `web/core/context_processors.py`
- `web/core/management/commands/create_roles.py`
- `web/core/roles.py`
- `web/ml/tests/test_ml.py`
- `web/render/tests/test_render.py`
- `web/twin/tests/test_ewm_tasks_refresh.py`

## Audit Trail

- EXTRACTED: 83 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*