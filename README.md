# TWINEMA

**Cyfrowy bliźniak magazynu, który da się pokazać jak film.**

TWINEMA łączy projektowanie centrum dystrybucyjnego w 3D z symulacją pracy i produkcją
prezentacji: układ hali i regałów → symulacja dnia projektowego → animacja przepływów
w Blenderze → film z lektorem (ElevenLabs) i deck PDF.

> Status: **F1 — rdzeń modelowania i symulacji działa** (generator hali, widok 3D, import zadań, dzień projektowy, kalibracja, prognoza, symulacja, porównanie, eksport do Blendera). Mapa drogi i decyzje: [`docs/PLAN.md`](docs/PLAN.md).

## Moduły (plan)

| Moduł | Co robi | Faza |
|---|---|---|
| Dane | importy materiałów, nośników, regałów, historii ruchów | F2 |
| Model hali | generator hali, regały, strefy, pola odkładcze, warianty, widok 3D | F1 |
| Symulacja | dzień projektowy, flota, kalibracja, porównanie wariantów | F1 |
| Prognozy i ML | wzrost wolumenów, segmentacja SKU, czas cyklu | F4 |
| Render 3D | worker Blendera, presety kamery, animacje przepływów | F3 |
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
python ../tools/ewm_demo_tasks.py demo.xlsx --scale 0.05   # syntetyczne zadania do importu
```

Blender: eksport sceny z widoku modelu → `blender -b -P tools/blender/twinema_warehouse_anim.py -- scena.json`.

Testy: `python manage.py test` (z katalogu `web/`, z tym samym env).

## Stack

Python 3.13 · Django 5.2 LTS · PostgreSQL 17 · Docker + Coolify · Blender 4.x (headless) ·
ElevenLabs (TTS) · ffmpeg.
