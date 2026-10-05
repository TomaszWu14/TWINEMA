# Przekazanie — stan projektu i następny krok (F5)

Plik dla kolejnej sesji (człowieka albo AI). Aktualny na 2026-10-05, po scaleniu PR #1–#5.

## Stan

| Faza | Moduł | PR | Co działa |
|---|---|---|---|
| F0 | `core` | — | konfiguracja fail-fast, role (Administratorzy / Projektant / Podgląd), health, hub, CI/CD |
| F1 | `twin` | #1 | generator hali, model 3D (three.js), import zadań, dzień projektowy, kalibracja, prognoza, symulacja, porównanie, eksport sceny `twinema.scene` |
| F2 | `masterdata` | #2 | importy xlsx/csv (materiały, master lokalizacji, stany) z raportem; stany → palety w scenie; grupy → dzień projektowy; `manage.py demo_dane --model N` |
| F3 | `render` | #4 | kolejka ujęć, API workera (token + jednorazowy claim), `tools/render_worker.py`, presety kamery w `tools/blender/twinema_render.py` (Blender 5.2 sprawdzony) |
| F4 | `ml` | #5 | prognoza (SES/Holt/Holt tłumiony/Holt-Winters vs trend log, wybór po MAPE), segmentacja k-means, `ModelRun` |
| F5a | `studio` | #8 | `Presentation` + `Shot`, szkic kwestii z szablonu (KPI modelu) albo z Claude (`ANTHROPIC_API_KEY`, `CLAUDE_MODEL`, domyślnie `claude-opus-5`), edycja tylko w szkicu, akceptacja tekstu |
| F5b | `studio` | #9 | lektor ElevenLabs (`ELEVENLABS_API_KEY`, `ELEVENLABS_VOICE_ID`, `ELEVENLABS_MODEL`), nagrywanie kwestia po kwestii, cache `VoiceTrack` po hashu (tekst+głos+model), napisy SRT z wyrównania znaków |
| F5c | `studio` | — | ujęcia jako `RenderJob` z kolejki F3 (Full HD, długość = nagranie + 0,5 s, cache po hashu scena+preset+długość), `MontageJob` + API workera (`/api/studio/montage/…`, ten sam token), `tools/twinema_montage.py` (plansze, tpad/apad, concat, napisy mov_text) — montuje `render_worker.py`, gdy ma ffmpeg |
| E1 | `twin` | — | silnik edytora layoutu: `twin/layout.py` + API `uklad.json` / `uklad/sprawdz/` / `uklad/zapisz/`, nowy rodzaj cechy „Pole odkładcze” (`staging`) |

F5 dalej: (d) deck PDF i szlif. Do Claude idą wyłącznie zdania z `studio/script.kpi_facts` (zagregowane liczby, bez nazw).

Testy: 332 zielone (`cd web && python manage.py test`, env: `DJANGO_DEBUG=true DJANGO_ALLOWED_HOSTS='*'`).

## Otwarte przy wdrożeniu (po stronie właściciela)
- Coolify: aplikacja z Dockerfile, Postgres, domena (np. `twinema.twapp.pl`), trwały wolumen `/app/web/media`.
- Sekrety repo: `COOLIFY_WEBHOOK_URL`, `SMOKE_URL`, `AUTOMERGE_PAT` (bez nich deploy się pomija).
- Env serwera: `RENDER_WORKER_TOKEN` (≥ 32 znaki); na PC worker z `TWINEMA_URL` + tym samym tokenem.

## Następny krok: F5 — Studio prezentacji

Cel: z wariantu hali i jego KPI powstaje 2–3 min film PL z lektorem i napisami + deck PDF, z aplikacji.

```
Presentation (model hali, tytuł, głos) → Shot × N (preset kamery, kwestia, kolejność)
 → scenariusz: szkic z Claude API na podstawie KPI (do edycji) → akceptacja tekstu
 → lektor: ElevenLabs TTS z timestamps per kwestia (długość ujęcia = długość audio)
 → render: RenderJob per ujęcie (seconds = długość kwestii) — istniejąca kolejka F3
 → montaż: ffmpeg (ujęcia + audio + napisy SRT + plansza tytułowa/końcowa) → MP4
 → deck: kadry PNG + KPI → PDF
```

Zasady:
- Statusy: szkic → tekst zatwierdzony → audio → render → montaż → gotowe. Nie renderować przed akceptacją tekstu.
- Cache po hashu wejścia (tekst+głos → audio; scena+preset+długość → render), żeby poprawka zdania nie
  renderowała całego filmu.
- Na zewnątrz (Claude API, ElevenLabs) idzie wyłącznie tekst narracji — żadnych surowych danych.
- Sekrety tylko w env (`config.py`): `ANTHROPIC_API_KEY`, `ELEVENLABS_API_KEY`, `ELEVENLABS_VOICE_ID`.
  Brak klucza = funkcja wyłączona z czytelnym komunikatem, nie błąd 500. Testy mockują HTTP.
- Model Claude do szkicu: najnowszy dostępny (np. `claude-sonnet-5`) — sprawdź skillem/dokumentacją `claude-api`.

Decyzje do potwierdzenia z właścicielem na starcie F5:
1. Czy jest już plan ElevenLabs (Creator) i klucz API + zaprojektowany głos (voice_id)?
2. Gdzie montaż: worker na PC (ma Blendera, ffmpeg do doinstalowania; rekomendacja) czy serwer (ffmpeg w obrazie)?

## Zasady repo (skrót — pełne w `CLAUDE.md`)
- Bez nazw firm, klientów i lokalizacji w kodzie i danych demo (dane syntetyczne).
- Polski interfejs; logika obliczeniowa w czystym Pythonie; jedna zmiana = gałąź `claude/**` + PR (auto-merge po CI).
- Przed PR: `ruff check .`, `manage.py check`, `makemigrations --check`, pełne testy.
