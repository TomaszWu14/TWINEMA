# Przekazanie — stan projektu i następny krok (F6)

Plik dla kolejnej sesji (człowieka albo AI). Aktualny na 2026-10-05, po scaleniu F5 (PR #8–#11).

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
| F5c | `studio` | #10 | ujęcia jako `RenderJob` z kolejki F3 (Full HD, długość = nagranie + 0,5 s, cache po hashu scena+preset+długość), `MontageJob` + API workera (`/api/studio/montage/…`, ten sam token), `tools/twinema_montage.py` (plansze, tpad/apad, concat, napisy mov_text) — montuje `render_worker.py`, gdy ma ffmpeg |
| F5d | `studio` | #11 | kadr PNG na ujęcie (ten sam klik co klipy, cache po hashu), deck PDF 16:9 (`studio/deck.py`, fpdf2 + DejaVu w repo): tytuł → liczby z KPI → ujęcie na slajd → koniec; film i deck na górze gotowej prezentacji i na liście |
| E1 | `twin` | #12 | silnik edytora layoutu: `twin/layout.py` + API `uklad.json` / `uklad/sprawdz/` / `uklad/zapisz/`, nowy rodzaj cechy „Pole odkładcze” (`staging`) |
| S2a | `scenario` | #14 | scenariusz niezależny od layoutu (dzień typowy + szczytowy, mnożnik wzrostu, normy), plan przyjęć (kontener 40' / auto 33-pal. / solówka, min/śr/max, okna awizacji), wynik: palety/dzień, doki w szczycie, osobogodziny, stanowiska paletyzacji; `manage.py demo_scenariusz` |
| S2b | `scenario` | — | wydania (auta OUT jak przyjęcia, cut-off, profil zamówień, % palet pełnych), paczki z pakowaniem i nadaniem, zwroty, cross-dock (przyjazd i wyjazd, bez składowania), zmiany i obsada per proces; wynik: palety OUT, doki OUT, osobogodziny 7 procesów, obsada potrzebna vs zakładana z niedoborami, ryzyko cut-off; godziny GG:MM |

Przepływ filmu: kwestie (szablon/Claude) → zatwierdź → „Nagraj lektora” → „Renderuj ujęcia i kadry” (worker
z Blenderem) → „Zmontuj film” (worker z ffmpeg) → MP4 + deck PDF + SRT. Do Claude i ElevenLabs idzie wyłącznie
tekst narracji (Claude: zdania z `studio/script.kpi_facts` — zagregowane liczby, bez nazw).

Testy: `cd web && python manage.py test --parallel 4` (env: `DJANGO_DEBUG=true DJANGO_ALLOWED_HOSTS='*'`).

## Po stronie właściciela (zanim pierwszy prawdziwy film)
- Klucze w env serwera (Coolify) i wpisy w `.env.example`: `ANTHROPIC_API_KEY`, `CLAUDE_MODEL`,
  `ELEVENLABS_API_KEY`, `ELEVENLABS_VOICE_ID`, `ELEVENLABS_MODEL`.
- ffmpeg na PC z workerem (`winget install Gyan.FFmpeg`), potem `python tools/render_worker.py`
  z `TWINEMA_URL` + `TWINEMA_WORKER_TOKEN` (worker przy starcie mówi, czy montaż włączony).
- Coolify: aplikacja z Dockerfile, Postgres, domena (np. `twinema.twapp.pl`), trwały wolumen `/app/web/media`.
- Sekrety repo: `COOLIFY_WEBHOOK_URL`, `SMOKE_URL`, `AUTOMERGE_PAT` (bez nich deploy się pomija).
- Env serwera: `RENDER_WORKER_TOKEN` (≥ 32 znaki).
- **Obejrzeć pierwszy prawdziwy film i deck**: prawdziwe ElevenLabs, Blender i ffmpeg nie były jeszcze
  uruchomione razem (testy mockują API i komendy) — sprawdzić synchronizację głosu, plansze, napisy, kadry.

## Następny krok: F6 — szlif (wg burzy mózgów, `docs/PLAN.md` §2.2 i §6)
- **Priorytet od 2026-10-05:** E1 ✅ → S2a ✅ → S2b ✅ (z obsadą) → E2 (plan 2D) → E3 (podgląd 3D) → S1 → S3 symulacja
  scenariusza → S4 animacja dnia → tryb prezentacji 3D → katalog sprzętu — szczegóły w `docs/PLAN.md`
  („Po F5”) i `docs/ZALOZENIA.md` (decyzje właściciela).
- ML3: model czasu cyklu (gradient boosting vs mediana real÷sym, MAE na odłożonych dniach).
- Porównania wariantów w filmie (split-screen „obecny vs wariant”), katalog rynku → CAPEX/OPEX.
- Unieważnianie renderów po zmianie samego modelu hali (dziś dopiero przy ponownym „Renderuj ujęcia”).
- Muzyka pod lektorem, wersja EN.

## Zasady repo (skrót — pełne w `CLAUDE.md`)
- Bez nazw firm, klientów i lokalizacji w kodzie i danych demo (dane syntetyczne).
- Polski interfejs; logika obliczeniowa w czystym Pythonie; jedna zmiana = gałąź `claude/**` + PR (auto-merge po CI).
- Przed PR: `ruff check .`, `manage.py check`, `makemigrations --check`, pełne testy.
