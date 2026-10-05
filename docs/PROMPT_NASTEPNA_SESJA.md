# Prompt na następną sesję (stan: koniec sesji 2026-10-05)

Wklej poniższy tekst jako pierwszą wiadomość nowej sesji Claude Code.

```
Kontynuujemy projekt TWINEMA — to repozytorium (GitHub: TomaszWu14/TWINEMA, prywatne). Mów do mnie po polsku.
Pracuję często głosowo — jeśli prompt jest mętny, nazwij założenia albo zadaj jedno krótkie pytanie.

## 1. Kontekst — przeczytaj najpierw
CLAUDE.md, docs/HANDOFF.md, docs/PLAN.md, docs/ZALOZENIA.md (decyzje właściciela — źródło prawdy), README.md.
Na pytania „jak/gdzie działa” → `graphify query "<pytanie>" --budget 1500` (porównaj „Built from commit”
w graphify-out/GRAPH_REPORT.md z `git rev-parse HEAD`; w razie potrzeby `graphify update .` + `graphify export wiki`).

TWINEMA = cyfrowy bliźniak magazynu: edytor hali 2D+3D, działka (od D2 także wielokąt), scenariusze wolumenów,
symulacja dnia (P95, wąskie gardła), animacja dnia 3D (od D3 auta jadą po drogach działki), prezentacja 3D,
katalog sprzętu z osprzętem, koszty CAPEX/OPEX. Film/montaż (studio F5) ODSTAWIONY. Odbiorcy: zarząd i rekruterzy
→ jakość „portfolio-grade”.

## 2. Stan (koniec sesji 2026-10-05)
Scalone: #1–#39, #41, #42, #43 — m.in. R2 alejki, R5 testy JS w CI, L1 logo, G2a kolory regałów
(typy/strefy/wypełnienie) + obrysy + cienie kontaktowe, G2b modele 3D sprzętu, R3 wydajność (cache, wersja modelu
przez sygnały, GET bez zapisów, has_events), F1 wypełnienie regałów ze stanu, D2 działka-wielokąt, D3 trasy aut.
Main: 643 testy Django + 71 JS zielone.

**SPRAWDŹ NAJPIERW** (`gh pr list --state all --limit 12`, `git worktree list`):
- #40 R4 (nawigacja z core.views.MODULES, CTA hala → scenariusz, „Wczytaj demo”, „Odśwież” zamiast auto-reload,
  GIT_SHA w config.py, defusedxml).
- #44 G2c — POPRAWKA MIGANIA 3D („miga jak stroboskop” przy ruchu kamery). Przyczyna: z-fighting (stałe near
  0,05 m / far 4000 m); fix: dynamiczny near = 2 % odległości do celu + wygaszanie obrysów. Po scaleniu poproś mnie
  o potwierdzenie w zwykłej przeglądarce; jeśli dalej miga — następny podejrzany: moiré tekstur kreskowanych
  (drogi pożarowe).
Poprzednia sesja: incydent GitHub Actions — joby anulowane w kolejce (także job auto-merge). Jeśli `test` jest
zielony, a auto-merge anulowany → `gh pr merge N --merge`; jeśli `test` anulowany → `gh run rerun <id>`.
Po scaleniu kilku PR-ów naraz uruchom pełny zestaw testów na main.
Usuń stare worktree w .claude/worktrees (d2, d3, fill, g2c, r3, r4, prompt i inne nieużywane).

## 3. W toku: K3 mieszana flota
Gałąź `claude/k3-mieszana-flota` (commit WIP 2799afa, zawiera R4; worktree .claude/worktrees/k3).
GOTOWE: silnik `scenario/sim/engine.py` — FleetMix (grupy role: vna / rack / transport / any), paleta do VNA
(udział `vna_share`, deterministycznie po id) przy grupie transportu jedzie dwoma etapami (AGV → punkt przekazania
→ VNA, `leg_min`), inaczej jednym ruchem (`min_per_move`) grupy właściwej albo zastępczej; KPI per grupa
(`kpi["fleet_groups"]`); wąskie gardło „Flota” dokłada do grupy z najdłuższym czekaniem; bez `fleet_groups`
działa jak dawna jedna flota. Testy scenario zielone.
DO ZROBIENIA:
1. Model `ScenarioFleet` (scenariusz, sprzęt z katalogu, sztuk) + migracja; rola z typu sprzętu
   (equipment/catalog.py: vna → vna; reach/czołowy/podnośnikowy/kompletacja → rack; AGV/AMR/paletowy/ciągnik →
   transport; przenośnik/sorter — nie).
2. services.simulate: grupy z katalogu (czas ruchu jak `fleet_from_catalog`; etap transportu ≈ droga bez
   podnoszenia, etap VNA ≈ krótszy odcinek + podniesienie — oznacz uproszczenia komentarzem `ponytail:`),
   `vna_share` z miejsc paletowych layoutu.
3. Formularz floty w scenariuszu (formset), wyniki per grupa w widoku symulacji, koszty CAPEX/OPEX per grupa
   (scenario/costs.py, services.run_costs — godziny pracy grupy z przebiegu reprezentatywnego).
4. Animacja dnia: AGV/AMR na trasach, reach/VNA przy swoich regałach (`fleet_kind` w views_play).
5. Testy silnika FleetMix (czysty Python) + widoków; potem PR.
Pokaż krótki plan przed startem, jeśli zmieniasz coś w powyższym.

## 4. Kolejka po K3
Do ustalenia ze mną. Odłożone: wdrożenie na serwer (Coolify, sekrety, RENDER_WORKER_TOKEN), plansza kosztów jako
slajd prezentacji, publiczny link prezentacji, trasowanie aut także w serwerowym sprawdzeniu działki
(`twin/site.py` `_dock_issues` — dziś odcinek prosty).

## 5. Zasady (twarde)
- Zero nazw firm/producentów/modeli handlowych w kodzie, migracjach, testach, danych demo, docs, commitach, PR.
  Prawdziwy katalog sprzętu jest TYLKO w mojej lokalnej bazie (web/db.sqlite3) i w pliku xlsx poza repo
  (Documents/TWINEMA_katalog_sprzetu.xlsx).
- Rola Podgląd (zarząd/rekruter) widzi wyniki i 3D, NIGDY danych źródłowych (materiały, SKU, partie, HU, lokalizacje EWM).
- Konfiguracja tylko przez web/twinema/config.py; logika obliczeniowa w czystym Pythonie bez Django; UI po polsku,
  system designu repo, dostępność (etykiety, aria-live, bez meta-refresh), pełny ekran przez `static/twin/js/fullscreen.js`.
- Pliki JS/PY < 500 linii (scene-builder.js ma dokładnie 500 — nowe rzeczy do osobnych modułów).
- Sesja nie może czytać/edytować `.env*` — nowe zmienne podaj mi jako gotowe linie do .env.example.

## 6. Sposób pracy
- Jedna zmiana = gałąź `claude/<nazwa>` + PR na main (gotowy, nie draft); CI `test` (Postgres 17, node) + auto-merge.
- Równolegle najwyżej 2 wątki w osobnych worktree (mało RAM); zadania nie mogą dotykać tych samych plików;
  przed pushem merge main. graphify-out commituj tylko w jednym PR naraz (inaczej konflikty).
- Przed PR: `ruff check .`, `cd web && python manage.py check`, `makemigrations --check --dry-run`,
  `python manage.py test --parallel 2` (env DJANGO_DEBUG=true DJANGO_ALLOWED_HOSTS='*'),
  `node --test web/twin/tests/js/*.test.mjs`.
- Pułapki: każda klasa testów z plikami — własny katalog mediów; w testach brak wartości przypominających sekrety
  w kwargach *_KEY/*_ID/TOKEN (gitleaks); zamykanie odpowiedzi strumieniowej w teście zrywa połączenie z Postgresem.
- Weryfikacja wizualna: baza tymczasowa w scratchpadzie (DB_PATH/MEDIA_ROOT ze ścieżkami z ukośnikami „/”),
  `manage.py demo_scenariusz` + `demo_dane --model 1` + symulacja przez `scenario.services.simulate`, serwer
  localhost:8098/8099 (`--noreload` — po zmianie Pythona restart). W Chrome sterowanym przez Claude NIE działa
  requestAnimationFrame ani natywny fullscreen → 3D przez `?debug3d=1` (`window.__tw3d.look(...)`, `renderNow()`
  DWA RAZY przed zrzutem — pierwszy bywa pusty), animacja: `window.__twDay.seek(s)`. Z-fighting/artefakty widać też
  na nieruchomej klatce. Worktree nie ma vendor JS — skopiuj z głównej kopii.
- Commit kończ liniami Co-Authored-By zgodnie z ustawieniami sesji. Nie ogłaszaj „gotowe”, dopóki testy i CI
  nie są zielone. Po każdym PR: co zrobione, co sprawdzone (ze zrzutami), co po mojej stronie.

## 7. Po mojej stronie (przypominaj w podsumowaniach)
- Opcjonalnie do .env.example: `GIT_SHA=` i `SOURCE_COMMIT=`.
- Klucze: ANTHROPIC_API_KEY, CLAUDE_MODEL, ELEVENLABS_API_KEY/VOICE_ID/MODEL (gdy wrócimy do studia).
- MCP: `APIFY_TOKEN` w zmiennych Windows, logowanie Gamma i Descript przez /mcp, potem `claude mcp list` i testy tylko do odczytu.
- W moich halach: role doków, nośność regałów, VNA w strefie V, działka z planu miejscowego (teraz także wielokąt),
  „Dni szczytowe w roku” w scenariuszach.
- Lokalnie: PyCharm → konfiguracja Python → TWINEMA (.run/); konto `demo`.
- Obejrzeć w zwykłej przeglądarce: brak migania 3D po #44, płynność, natywny pełny ekran, prezentację 3D.

Zacznij od punktu 2 (#40, #44, sprzątanie worktree), potem dokończ K3 (punkt 3).
```
