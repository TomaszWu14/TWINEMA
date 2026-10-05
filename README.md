# TWINEMA

**Cyfrowy bliźniak magazynu, który da się pokazać jak film.**

TWINEMA łączy projektowanie centrum dystrybucyjnego w 3D z symulacją pracy i produkcją
prezentacji: układ hali i regałów → symulacja dnia projektowego → animacja przepływów
w Blenderze → film z lektorem (ElevenLabs) i deck PDF.

> Status: **F3 — render w Blenderze przez kolejkę i workera (przelot, orbita, przejazd, plan); F2 — dane z plików (materiały, master lokalizacji, stany) zasilają scenę 3D i dzień projektowy; F1 — rdzeń modelowania i symulacji działa** (generator hali, widok 3D, import zadań, dzień projektowy, kalibracja, prognoza, symulacja, porównanie, eksport do Blendera). Mapa drogi i decyzje: [`docs/PLAN.md`](docs/PLAN.md).

## Moduły (plan)

| Moduł | Co robi | Faza |
|---|---|---|
| Dane | importy materiałów, mastera lokalizacji i stanów z raportem odrzuceń; dane demo | F2 ✅ |
| Model hali | generator hali, regały, strefy, pola odkładcze, warianty, widok 3D | F1 |
| Symulacja | dzień projektowy, flota, kalibracja, porównanie wariantów | F1 |
| Prognozy i ML | Holt-Winters i spółka kontra baseline (MAPE), segmentacja materiałów k-means | F4 ✅ |
| Render 3D | kolejka ujęć, worker Blendera na PC (HTTPS + token), presety kamery, PNG/MP4 w aplikacji | F3 ✅ |
| Studio prezentacji | scenariusz, lektor, montaż — MP4 + PDF | F5 |

## Uruchomienie lokalne

```bash
python -m venv .venv && .venv/Scripts/activate      # Linux/macOS: source .venv/bin/activate
pip install -r requirements-dev.txt
cd web
export DJANGO_DEBUG=true DJANGO_ALLOWED_HOSTS='*'
python manage.py migrate && python manage.py create_roles
python manage.py createsuperuser
python manage.py runserver 8090
sh scripts/fetch_vendor.sh                           # raz: three.js + ECharts do static (bez CDN)
python ../tools/ewm_demo_tasks.py demo.xlsx --weeks 30 --scale 0.05   # syntetyczne zadania (prognoza ML: ≥ 16 pełnych tygodni)
python manage.py demo_dane --model 1                  # materiały + stan demo na regałach modelu
```

Render: ustaw na serwerze `RENDER_WORKER_TOKEN` (≥ 32 znaki), na PC z Blenderem:
```bash
set TWINEMA_URL=https://twinema.twapp.pl
set TWINEMA_WORKER_TOKEN=<ten sam token>
python tools/render_worker.py            # odpytuje co 10 s, renderuje po jednym zleceniu
```
Ręcznie: `blender -b -P tools/blender/twinema_render.py -- scena.json wynik.mp4 --preset orbita --seconds 10`.

Testy: `python manage.py test` (z katalogu `web/`, z tym samym env).

## Git hooks i graf wiedzy (Obsidian)

Dwie powierzchnie hooków git — wzajemnie się wykluczają, więc wybierz świadomie:

1. **`pre-commit install`** (zalecane dla każdego dewelopera) — ruff, `makemigrations --check`
   przy zmianach modeli i gitleaks z [`.pre-commit-config.yaml`](.pre-commit-config.yaml).
2. **`git config core.hooksPath .githooks`** — aktywuje [`.githooks/pre-push`](.githooks/pre-push):
   nieblokującą synchronizację wiki grafu (`graphify-out/wiki/`) do vaulta Obsidian. Działa tylko
   tam, gdzie istnieje `~/graphify-workspace/sync-knowledge-graph.sh`; wszędzie indziej cicho nic
   nie robi. **Uwaga:** ustawiony `core.hooksPath` blokuje `pre-commit install` — na tej maszynie
   lintery odpalaj ręcznie (`pre-commit run --all-files`) albo polegaj na CI.

Graf wiedzy (`graphify-out/`: `graph.json`, `GRAPH_REPORT.md`, `wiki/`) jest **generowany lokalnie**
(graphify nie działa w CI) i commitowany — korzysta z niego `graphify query` (patrz `CLAUDE.md`).
Odświeżenie po zmianach w kodzie:

```bash
graphify update .        # przyrostowo, bez LLM; pełny rebuild: graphify . --code-only
graphify export wiki     # strony wiki (update ich nie odświeża)
# zacommituj zmienione graphify-out/ i wypchnij (PR)
```

Workflow [`graph-freshness.yml`](.github/workflows/graph-freshness.yml) (poniedziałki 06:00 UTC
+ ręcznie) otwiera issue `graf-wiedzy`, gdy graf odstaje od `main` (≥ 30 commitów albo ≥ 7 dni
i ≥ 5 commitów).

## Stack

Python 3.13 · Django 5.2 LTS · PostgreSQL 17 · Docker + Coolify · Blender 4.x (headless) ·
ElevenLabs (TTS) · ffmpeg.
