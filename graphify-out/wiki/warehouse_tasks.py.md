# warehouse_tasks.py

> 33 nodes · cohesion 0.11

## Key Concepts

- **warehouse_tasks.py** (22 connections) — `web/twin/views/warehouse_tasks.py`
- **ewm_tasks_import.py** (16 connections) — `web/twin/ewm_tasks_import.py`
- **run_import()** (8 connections) — `web/twin/ewm_tasks_import.py`
- **ewm_tasks_import()** (8 connections) — `web/twin/views/warehouse_tasks.py`
- **ewm_tasks_preview()** (8 connections) — `web/twin/views/warehouse_tasks.py`
- **location_report()** (7 connections) — `web/twin/ewm_tasks_import.py`
- **upload_path()** (7 connections) — `web/twin/ewm_tasks_import.py`
- **save_upload()** (6 connections) — `web/twin/ewm_tasks_import.py`
- **_md_role** (6 connections)
- **ewm_tasks_status()** (5 connections) — `web/twin/views/warehouse_tasks.py`
- **_form()** (5 connections) — `web/twin/views/warehouse_tasks.py`
- **purge_stale()** (4 connections) — `web/twin/ewm_tasks_import.py`
- **upload_dir()** (4 connections) — `web/twin/ewm_tasks_import.py`
- **_dispatch()** (4 connections) — `web/twin/views/warehouse_tasks.py`
- **ewm_tasks_detail()** (4 connections) — `web/twin/views/warehouse_tasks.py`
- **_progress()** (4 connections) — `web/twin/views/warehouse_tasks.py`
- **ewm_tasks_delete()** (3 connections) — `web/twin/views/warehouse_tasks.py`
- **require_POST** (3 connections)
- **_run_in_thread()** (3 connections) — `web/twin/views/warehouse_tasks.py`
- **ewm_tasks_list()** (2 connections) — `web/twin/views/warehouse_tasks.py`
- **never_cache** (1 connections)
- **Import zadań magazynowych EWM do bazy: `ewm_tasks.Scan` (strumień) →…** (1 connections) — `web/twin/ewm_tasks_import.py`
- **Lokalizacje z zadań partii vs regały modelu: ile trafia w gniazda, ile jest…** (1 connections) — `web/twin/ewm_tasks_import.py`
- **Porzucone podglądy (nikt nie kliknął „Importuj”) — kasowane po dobie.** (1 connections) — `web/twin/ewm_tasks_import.py`
- **Zapis uploadu na dysk kawałkami → token (nazwa pliku) do podglądu i importu.** (1 connections) — `web/twin/ewm_tasks_import.py`
- *... and 8 more nodes in this community*

## Relationships

- [WarehouseTaskBatch](WarehouseTaskBatch.md) (10 shared connections)
- [scene-builder.js](scene-builder.js.md) (4 shared connections)
- [ADR-0001: Kopia kodu modelowania magazynu, nie przeniesienie](ADR-0001-_Kopia_kodu_modelowania_magazynu%2C_nie_przeniesienie.md) (2 shared connections)
- [Scan](Scan.md) (2 shared connections)
- [StudioViewTests](StudioViewTests.md) (2 shared connections)
- [Pochodzenie kodu](Pochodzenie_kodu.md) (2 shared connections)

## Source Files

- `web/twin/ewm_tasks_import.py`
- `web/twin/views/warehouse_tasks.py`

## Audit Trail

- EXTRACTED: 140 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*