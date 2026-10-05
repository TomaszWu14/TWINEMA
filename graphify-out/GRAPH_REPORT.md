# Graph Report - agent-acddf53671c205e0a  (2026-10-05)

## Corpus Check
- 185 files · ~105,566 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 2016 nodes · 3975 edges · 144 communities (109 shown, 35 thin omitted)
- Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 117 edges (avg confidence: 0.57)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `363367e4`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- warehouse_blender.py
- rack_corners
- studio/api.py
- FloorGrid
- twinema_warehouse_anim.py
- test_foundation.py
- warehouse_tasks.py
- simulate
- twin/models.py
- test_dane.py
- design_kpi.py
- blender_scene.py
- generate
- test_model_edit.py
- design_catalog.py
- EwmViewsTests
- ml/views.py
- test_design_sim_scene.py
- twinema_design_kit.py
- ValueError
- context_processors.py
- test_voice.py
- ewm_levels.py
- WorkerApiTests
- twinema_montage.py
- addressing.py
- test_design_forecast.py
- flow-player.js
- TasksEndpointAndImportTests
- WarehouseModelViewTests
- Agent
- design_day.py
- forecast.py
- masterdata/services.py
- kpi_facts
- TWINEMA — zakres i plan
- BayTemplate
- ParseTests
- test_design_compare.py
- warehouse_model_ewm.py
- warehouse_variants.py
- masterdata/views.py
- StudioViewTests
- load_groups
- build_scene
- BayTemplateViewTests
- test_equipment_agents.py
- middleware.py
- SlotLocator
- test_design_calibration.py
- Scan
- SimulationViewTests
- studio/views.py
- CLAUDE.md — TWINEMA
- WarehouseModelPasteTests
- test_deck.py
- ADR-0001: Kopia kodu modelowania magazynu, nie przeniesienie
- RenderMontageTests
- ._scene
- DaneViewTests
- _save
- VoiceViewTests
- blender_route.py
- pre-push
- ForecastTests
- WarehouseHallFeatureTests
- render/views.py
- VariantViewTests
- test_container_inbound.py
- EwmTasksPollingTests
- test_blender_export.py
- FlowSceneEndpointTests
- bay_templates.py
- ewm_demo_tasks.py
- blender_stock.py
- RackTypeWeightsTests
- test_ml.py
- params_for
- Pochodzenie kodu
- CalibrationViewTests
- studio/models.py
- LoadAndViewTests
- GeneratorViewTests
- segmentation.py
- ewm_tasks.py
- icon
- shared.py
- DesignHubTests
- CoreConfig
- health
- MasterdataConfig
- MlConfig
- RenderConfig
- fetch_vendor.sh
- TwinConfig
- blender_tasks.py
- docker-entrypoint.sh
- masterdata/migrations/0001_initial.py
- ml/migrations/0001_initial.py
- render/migrations/0001_initial.py
- map_columns
- parse_stamp
- build_pallets
- parse_row
- SimSceneViewTests
- 0002_lektor.py
- GeneratorTests
- ml/services.py
- twinema_render.py
- _tasks
- StudioConfig
- ClampTests
- studio/migrations/0001_initial.py
- BlenderExportViewTests
- VariantEditViewTests
- demo.py
- CompareViewTests
- warehouse_model_copy
- 0003_render_montaz.py
- Command
- Command
- twin/__init__.py
- locations.py
- MetaRefreshGuardTests
- 0004_kadry.py

## God Nodes (most connected - your core abstractions)
1. `SlotLocator` - 33 edges
2. `WarehouseModel` - 31 edges
3. `simulate()` - 29 edges
4. `build_scene()` - 24 edges
5. `Scan` - 23 edges
6. `Agent` - 22 edges
7. `WarehouseTaskBatch` - 22 edges
8. `model_racks()` - 21 edges
9. `FloorGrid` - 20 edges
10. `params_for()` - 20 edges

## Surprising Connections (you probably didn't know these)
- `start()` --calls--> `params_for()`  [EXTRACTED]
  tools/blender/twinema_design_kit.py → web/twin/design_catalog.py
- `load_variant()` --calls--> `params_for()`  [EXTRACTED]
  tools/blender/twinema_design_kit.py → web/twin/design_catalog.py
- `add()` --calls--> `params_for()`  [EXTRACTED]
  tools/blender/twinema_design_kit.py → web/twin/design_catalog.py
- `add_block()` --calls--> `rack_axes()`  [EXTRACTED]
  tools/blender/twinema_design_kit.py → web/twin/blender_route.py
- `add_block()` --calls--> `block_rows()`  [EXTRACTED]
  tools/blender/twinema_design_kit.py → web/twin/design_catalog.py

## Import Cycles
- None detected.

## Communities (144 total, 35 thin omitted)

### Community 0 - "warehouse_blender.py"
Cohesion: 0.12
Nodes (31): model_racks(), Regały WarehouseModel jako dicty w formacie sceny (x, y, width, depth,…, load_inputs(), Agregaty zadań potwierdzonych partii (czas lokalny) — liczone w bazie, nie w…, load_day_tasks(), Zadania potwierdzone w dniu `day` (czas lokalny) jako sekundy od DAY_START_H., Zadania magazynowe EWM (WT) — import z monitora magazynu (/SCWM/MON) do…, WarehouseTaskBatch (+23 more)

### Community 1 - "rack_corners"
Cohesion: 0.12
Nodes (16): rack_corners(), floor_size(), is_geometry_csv(), _num(), parse_geometry_csv(), Geometria regałów z pliku CSV (np. odczytana z rysunku hali) → regały modelu…, Plik geometrii poznajemy po nagłówku (plik kodów lokalizacji go nie ma)., Tekst CSV → (racks, errors). Wiersz z błędem trafia do `errors` (nr linii +… (+8 more)

### Community 2 - "studio/api.py"
Cohesion: 0.13
Nodes (31): claim(), _claimed_job(), fail(), _forbidden(), require_GET, require_POST, API workera renderów. Uwierzytelnienie: nagłówek X-Worker-Token…, Zlecenia „w toku” dłużej niż RENDER_STALE_MIN (worker padł) wracają do kolejki. (+23 more)

### Community 3 - "FloorGrid"
Cohesion: 0.22
Nodes (7): _dedupe(), FloorGrid, Trasa A* (8-sąsiedztwo, bez ścinania narożników regałów) z punktu a do b.…, Usuwa węzły leżące na prostej (zostają tylko zakręty)., Siatka zajętości posadzki: komórka zablokowana, jeśli leży w obrysie regału.…, Najbliższa wolna komórka (BFS od komórki punktu) albo None, gdy hala zapchana., _simplify()

### Community 4 - "twinema_warehouse_anim.py"
Cohesion: 0.14
Nodes (37): _animate_agent(), _animate_item(), _bl(), _box_mesh(), build(), _build_feature(), _build_floor(), _build_pallets() (+29 more)

### Community 5 - "test_foundation.py"
Cohesion: 0.07
Nodes (17): BaseSettings, login_required, model_validator, AccessTests, ConfigTests, GroupContractTests, HealthTests, SimpleTestCase (+9 more)

### Community 6 - "warehouse_tasks.py"
Cohesion: 0.11
Nodes (33): never_cache, load_master_levels(), {kod: poziom} z aktywnego mastera lokalizacji (pusty dict, gdy brak)., location_report(), purge_stale(), Import zadań magazynowych EWM do bazy: `ewm_tasks.Scan` (strumień) →…, Lokalizacje z zadań partii vs regały modelu: ile trafia w gniazda, ile jest…, Porzucone podglądy (nikt nie kliknął „Importuj”) — kasowane po dobie. (+25 more)

### Community 7 - "simulate"
Cohesion: 0.12
Nodes (20): _is_shelf(), _Agent, _kpi(), Layout, _manh(), _p95(), _pick(), Symulacja dnia projektowego na wariancie hali (plan 2026-10-02, etap 3a) —… (+12 more)

### Community 8 - "twin/models.py"
Cohesion: 0.05
Nodes (39): has_role(), True dla superusera albo członka którejś z grup., Dekorator: wymaga zalogowania + członkostwa w grupie (superuser zawsze…, role_required(), Kolejka renderów: API workera (token, przejęcie, scena, wynik) i ekran zleceń., Ekrany studia: role, szkic z szablonu, edycja tylko w szkicu, akceptacja, szkic…, compliance(), Raport zgodności modelu z EWM: kody z planu (expand_model) vs kody z mastera,… (+31 more)

### Community 9 - "test_dane.py"
Cohesion: 0.15
Nodes (15): demo_stock(), Pozycje stanu dla regałów modelu: ~`fill` miejsc zajętych, materiały wg rotacji…, ImportLog, Material, Meta, Dane podstawowe bliźniaka: materiały, stany w lokalizacjach i dziennik…, Jeden import pliku: rodzaj, wynik i próbka odrzuconych wierszy. Import stanów…, Materiał (SKU): opakowanie zbiorcze i paletyzacja — wejście do rozmieszczenia i… (+7 more)

### Community 10 - "design_kpi.py"
Cohesion: 0.15
Nodes (18): anchor_count(), anchors(), _center(), compute_kpi(), equipment_capacity(), rack_to_element(), Wskaźniki wariantu projektu magazynu (czysty Python — testowalny bez bazy i…, Regał modelu magazynu (dict jak w scenie: width/depth/level_h/n_bays/n_levels)… (+10 more)

### Community 11 - "blender_scene.py"
Cohesion: 0.09
Nodes (36): rack_axes(), rack_point(), (u_w, u_d) — jednostkowe osie szerokości i głębokości regału w układzie hali., Punkt hali: `along` [m] wzdłuż szerokości, `across` [m] wzdłuż głębokości…, _access(), _activity_picks(), _aisle_m(), build_scene_for_model() (+28 more)

### Community 12 - "generate"
Cohesion: 0.28
Nodes (11): _docks(), _feature(), generate(), _pair_pitch(), _rack(), Generator hali od parametrów — nowy magazyn „od zera” (plan 2026-10-02, etap…, Poziomy składowania z podłogą: góra najwyższej palety ≤ wysokość − tryskacze., [korytarz][A|B][korytarz]… — y każdego rzędu; A patrzy na korytarz przed, B za. (+3 more)

### Community 13 - "test_model_edit.py"
Cohesion: 0.18
Nodes (16): apply_zone_edit(), _box(), collisions(), fit_floor(), Edycja wariantu hali blokami (plan 2026-10-02, etap 4) — czysty Python.…, {strefa: liczba rzędów, gniazd w rzędzie (maks.), poziomy (maks.)} dla…, Zmienia regały strefy w miejscu (dicty jak `model_racks`) i zwraca listę…, Pary regałów nachodzących na siebie (obrysy osiowe, tolerancja `tol` m) —… (+8 more)

### Community 14 - "design_catalog.py"
Cohesion: 0.15
Nodes (19): _geometry(), block_rows(), check_aisles(), element_summary(), footprint(), height(), pallet_positions(), Katalog elementów do projektowania wariantów magazynu — JEDNO źródło prawdy.… (+11 more)

### Community 15 - "EwmViewsTests"
Cohesion: 0.10
Nodes (8): load_sample(), Syntetyczna próbka mastera lokalizacji (hala B0) dla testów „Wykryj z EWM” i…, [(kod, typ EWM)] — kod B0-<rząd>-<gniazdo><pozycja palety><litera poziomu>., make_model_and_master(), TestCase, ServiceTests, EwmViewsTests, TestCase

### Community 16 - "ml/views.py"
Cohesion: 0.25
Nodes (8): detail(), home(), _int(), any_role, designer, require_POST, run(), segments_csv()

### Community 17 - "test_design_sim_scene.py"
Cohesion: 0.11
Nodes (13): build_sim_scene(), CorridorRouter, _pick_time(), Animacja godziny z symulacji dnia (plan 2026-10-02, etap 3b) — czysty Python.…, Trasa „jak w magazynie”: wzdłuż korytarza do przejazdu poprzecznego, nim do…, Chwila przejęcia ładunku: kombi rusza wcześniej niż AGV, ale paletę bierze po…, Przebiegi rozpoczęte w godzinie `hour` (zegar 5–21). Zwraca (przebiegi, ile…, window_legs() (+5 more)

### Community 18 - "twinema_design_kit.py"
Cohesion: 0.19
Nodes (21): add(), add_block(), _clear(), _coll(), elements(), export_variant(), load_variant(), _make() (+13 more)

### Community 19 - "ValueError"
Cohesion: 0.18
Nodes (21): ValueError, _bool(), _cell(), _code(), _date(), ImportFileError, map_columns(), norm() (+13 more)

### Community 21 - "test_voice.py"
Cohesion: 0.11
Nodes (24): align(), AlignmentTests, CueTests, TestCase, Czysta logika lektora: hash cache, długość, słowa, plansze napisów, SRT., Sztuczne wyrównanie: każdy znak trwa per_char sekund., SrtTests, VoiceKeyTests (+16 more)

### Community 22 - "ewm_levels.py"
Cohesion: 0.17
Nodes (16): NamedTuple, code_slot(), is_hall_a(), letter_slot(), LetterSlot, level_height_keys(), level_height_mm(), Litera kodu lokalizacji EWM → fizyczne miejsce w stosie (JEDNO źródło prawdy).… (+8 more)

### Community 23 - "WorkerApiTests"
Cohesion: 0.16
Nodes (4): override_settings, TestCase, RenderScreenTests, WorkerApiTests

### Community 24 - "twinema_montage.py"
Cohesion: 0.06
Nodes (32): Api, find_blender(), main(), Worker renderów TWINEMA — uruchamiany na komputerze z Blenderem (np. z GPU).…, Montaż filmu: pobierz ujęcia i nagrania, wykonaj komendy z…, BLENDER_BIN / --blender → PATH → typowe katalogi instalacji (najnowsza wersja)., run_job(), run_montage() (+24 more)

### Community 25 - "addressing.py"
Cohesion: 0.06
Nodes (47): _bay_locations(), expand_model(), expand_row(), format_bay_numbers(), letter_rank(), make_code(), parse_bay_numbers(), parse_code() (+39 more)

### Community 26 - "test_design_forecast.py"
Cohesion: 0.19
Nodes (13): backtest(), fit(), forecast(), Prognoza wzrostu wolumenów z historii zadań EWM (plan 2026-10-02, etap 5) —…, series: [(dzień porządkowy, wartość)] → (nachylenie log/tydzień, wyraz wolny,…, MAPE [%] prognozy ostatnich `weeks` tygodni z modelu uczonego bez nich (None —…, Wzrost per strumień: roczne tempo P50/P90, mnożnik na `years` lat, MAPE testu…, _daily() (+5 more)

### Community 27 - "flow-player.js"
Cohesion: 0.10
Nodes (11): _e, FLOW_LABELS, FLOW_Y, _m, _p, _q, _s, SIM_KEYS (+3 more)

### Community 28 - "TasksEndpointAndImportTests"
Cohesion: 0.15
Nodes (4): override_settings, TestCase, Duży plik → import w wątku w tle (bez blokowania żądania), partia kończy się…, TasksEndpointAndImportTests

### Community 29 - "WarehouseModelViewTests"
Cohesion: 0.11
Nodes (9): InstancingGuardTests, TestCase, UX #5: widok 3D nie może cicho paść czarnym ekranem — spinner + guard WebGL +…, Regresja bezpieczeństwa: wolny tekst pól regału/elementu (zone/rack_id/label)…, Regresja: FLOOR_W/FLOOR_D w JS muszą mieć KROPKĘ dziesiętną, nie polski…, R1: stal regałów renderowana przez InstancedMesh (3 draw calle), nie per-mesh.…, StoredXSSGuardTests, ViewFloatLocalizationTests (+1 more)

### Community 30 - "Agent"
Cohesion: 0.19
Nodes (7): Agent, _r(), Postój do chwili `t` (realny znacznik zadania); zajęty agent nie cofa się w…, Przejęcie ładunku: klatka „na miejscu" → po `handling` s ładunek jest na…, Odłożenie ładunku w `pos` na wysokości `z` (np. gniazdo regału albo dok)., Agent z osią czasu ruchu: rodzaj z `SPEED` (wózek, pracownik, kombi, AGV, EPT)., Jazda/przejście trasą A* do `target`; trasa trafia też do mapy przepływów.

### Community 31 - "design_day.py"
Cohesion: 0.11
Nodes (18): _abc_xyz(), build_profile(), _groups(), _order_profile(), percentile(), Profil ruchów i dzień projektowy z zadań EWM (spec projektowania magazynu, krok…, daily: {data: {rodzaj: n, "orders": n}}; hourly: {(data, godzina): {rodzaj:…, Percentyl z interpolacją liniową (jak numpy/Excel PERCENTILE.INC); pusta lista… (+10 more)

### Community 32 - "forecast.py"
Cohesion: 0.16
Nodes (13): candidates(), _demo(), evaluate(), fit(), _grid(), mape(), ML1 — prognoza tygodniowych wolumenów: kilka modeli wygładzania wykładniczego…, Najlepsze parametry modelu na serii `y` → (params, fitted, prognoza h→v, sd… (+5 more)

### Community 33 - "masterdata/services.py"
Cohesion: 0.17
Nodes (16): missing_required(), parse_rows(), → (poprawne dicty, odrzucone [{row, reason}] — próbka), liczba odrzuconych.…, import_file(), _level_of(), load_demo(), Zapis importów do bazy + odczyt danych dla bliźniaka (stany do sceny, grupy do…, Materiały demo (upsert) + import stanów demo dla modelu hali → (liczba… (+8 more)

### Community 34 - "kpi_facts"
Cohesion: 0.11
Nodes (18): clean_draft(), estimate_seconds(), _get(), kpi_facts(), _num(), Scenariusz prezentacji (czysty Python — bez Django i bez sieci). • `kpi_facts`…, Liczba po polsku: spacja tysięcy, przecinek dziesiętny., Zdania z liczbami wariantu. Brak wartości → zdanie pominięte (nie zgadujemy). (+10 more)

### Community 35 - "TWINEMA — zakres i plan"
Cohesion: 0.08
Nodes (22): Następny krok: F6 — szlif (wg burzy mózgów, `docs/PLAN.md` §2.2 i §6), Po stronie właściciela (zanim pierwszy prawdziwy film), Przekazanie — stan projektu i następny krok (F6), Stan, Zasady repo (skrót — pełne w `CLAUDE.md`), 1. Decyzje, 2.1 MVP, 2.2 Po MVP (wsad do burzy mózgów) (+14 more)

### Community 36 - "BayTemplate"
Cohesion: 0.16
Nodes (6): BayTemplate, Szablon gniazda (słupa regału): belka, palety na belce, poziomy od podłogi w…, BayTemplateTests, levels(), TestCase, RackRuleAndOverrideTests

### Community 37 - "ParseTests"
Cohesion: 0.12
Nodes (7): MapColumnsTests, ParseTests, SimpleTestCase, Parser plików modułu Dane — czysty Python (bez bazy)., Wzór pliku z ekranu Dane musi się importować bez ręcznych poprawek., ReadTableTests, _xlsx()

### Community 38 - "test_design_compare.py"
Cohesion: 0.18
Nodes (13): capacity(), comparison(), Porównanie wariantów hali na tym samym dniu projektowym (plan 2026-10-02, etap…, Miejsca paletowe (regały nie-półkowe), lokalizacje kartonowe (półki K1), bramy,…, Symulacja z flotą sugerowaną przez poprzedni przebieg, aż flota się ustali (≤…, [{wiersz KPI z wartościami per wariant + najlepszy}] dla tabeli., required_fleet(), variant_row() (+5 more)

### Community 39 - "warehouse_model_ewm.py"
Cohesion: 0.10
Nodes (29): atomic, active_master(), apply_proposal(), compliance_for_model(), detect_for_model(), master_rows(), plan_for_model(), Aktywny (najnowszy) import mastera lokalizacji albo None. (+21 more)

### Community 40 - "warehouse_variants.py"
Cohesion: 0.19
Nodes (15): clean_elements(), Walidacja elementów z pliku: znany rodzaj, liczby, parametry przez params_for.…, _comparison(), _get(), _md_role, _planner, require_POST, Wariant jako twinema.design-variant — do dalszej edycji w Blenderze… (+7 more)

### Community 41 - "masterdata/views.py"
Cohesion: 0.15
Nodes (15): Wzór pliku: nagłówki (pierwszy alias = polska nazwa) — do pobrania z ekranu…, template_csv(), current_stock_log(), Najnowszy import stanów = aktualny stan magazynu (None, gdy brak)., Pozycje stanu jako dicty `build_pallets`: location, hu, sku, name, lot, expiry,…, stock_for_scene(), demo(), home() (+7 more)

### Community 42 - "StudioViewTests"
Cohesion: 0.10
Nodes (19): BaseModel, draft_script(), enabled(), Exception, Szkic scenariusza z Claude API. Do modelu trafiają WYŁĄCZNIE zdania z…, Błąd do pokazania użytkownikowi (bez szczegółów technicznych)., facts: lista zdań z liczbami → (shots, ostrzeżenia). Rzuca ScriptAIError., ScriptAIError (+11 more)

### Community 43 - "load_groups"
Cohesion: 0.40
Nodes (4): groups_for(), {materiał: grupa towarowa} albo None, gdy materiałów jeszcze nie zaimportowano.…, load_groups(), {materiał z zadań: grupa towarowa} z modułu Dane; None, gdy materiałów jeszcze…

### Community 44 - "build_scene"
Cohesion: 0.16
Nodes (15): build_scene(), _carry(), _container_flow(), _Ctx, _demo_picks(), _forklift_task(), _labelled(), _point_end() (+7 more)

### Community 45 - "BayTemplateViewTests"
Cohesion: 0.20
Nodes (4): BayTemplateViewTests, CoordsRuleColumnsTests, level_post(), TestCase

### Community 46 - "test_equipment_agents.py"
Cohesion: 0.20
Nodes (7): EquipmentAgentsTests, SimpleTestCase, _rack(), Sprzęt nowego magazynu w animacji (plan 2026-10-02, etap 2): AGV + kombi w…, Paleta przechodzi AGV → kombi w jednym miejscu: między klatkami nie skacze…, Czas klatek palety rośnie: kombi czeka (wait_until), zamiast „cofać" paletę w…, _scene()

### Community 47 - "middleware.py"
Cohesion: 0.13
Nodes (9): client_ip(), Middleware przekrojowe: identyfikator żądania (korelacja logów) + nagłówki…, Dopisuje `record.request_id` z bieżącego żądania ("-" poza żądaniem)., Bierze X-Request-ID od proxy albo nadaje nowy; odsyła go w odpowiedzi., Permissions-Policy + Content-Security-Policy (domyślnie report-only)., IP klienta dla django-axes za jednym zaufanym proxy (Traefik/Coolify): ostatni…, RequestIDLogFilter, RequestIDMiddleware (+1 more)

### Community 48 - "SlotLocator"
Cohesion: 0.25
Nodes (6): _inside(), Czy punkt leży w obrysie regału poszerzonym o `margin` [m]., Kod lokalizacji → gniazdo w regale modelu (środek palety, wysokość, obrót).…, SlotLocator, Palety w lokalizacjach (stan magazynu) w scenie Blendera —…, SlotLocatorTests

### Community 49 - "test_design_calibration.py"
Cohesion: 0.20
Nodes (10): calibrate(), ideal_cycle(), Czas cyklu wg fizyki symulacji: dojazd prev → src, chwyt, przewóz src → dst,…, rows: krotki `blender_tasks.ROW_FIELDS` jednego dnia (rosnąco po potwierdzeniu)., CalibrationTests, SimpleTestCase, Kalibracja symulacji na obecnej hali (plan 2026-10-02, etap 6)., Wózek przewozi palety między dwoma gniazdami co `gap_s` sekund. (+2 more)

### Community 50 - "Scan"
Cohesion: 0.23
Nodes (5): Przebieg po pliku: nagłówek → mapowanie kolumn → wiersze sparsowane albo błędy,…, Poprawne, nieanulowane zadania (dicty pól modelu)., [(etykieta pola, nagłówek z pliku)] w kolejności pól., Scan, ScanFileTests

### Community 51 - "SimulationViewTests"
Cohesion: 0.14
Nodes (6): Meta, WarehouseTask, ForecastViewTests, TestCase, TestCase, SimulationViewTests

### Community 52 - "studio/views.py"
Cohesion: 0.12
Nodes (34): approve(), deck_pdf(), _draft_or_back(), film_file(), model_kpi(), montage_create(), montage_input_key(), montage_ready() (+26 more)

### Community 53 - "CLAUDE.md — TWINEMA"
Cohesion: 0.33
Nodes (5): CLAUDE.md — TWINEMA, Git, Graphify query-first, Testy (przed każdym PR), Zasady

### Community 55 - "test_deck.py"
Cohesion: 0.11
Nodes (15): FPDF, PlainTestCase, build_deck(), _Deck, Deck PDF prezentacji (czysty Python — fpdf2, bez Django i bez bazy). Strony…, „Etykieta: wartość.” → (etykieta, wartość) do kafla; zdanie bez dwukropka →…, slides: [{"label": "Przelot nad halą", "text": kwestia, "image": bytes PNG albo…, split_fact() (+7 more)

### Community 56 - "ADR-0001: Kopia kodu modelowania magazynu, nie przeniesienie"
Cohesion: 0.40
Nodes (4): ADR-0001: Kopia kodu modelowania magazynu, nie przeniesienie, Decyzja, Kontekst, Skutki

### Community 57 - "RenderMontageTests"
Cohesion: 0.19
Nodes (3): override_settings, TestCase, RenderMontageTests

### Community 58 - "._scene"
Cohesion: 0.24
Nodes (5): SimpleTestCase, _racks(), ResolveMovesTests, _row(), SceneFromTasksTests

### Community 59 - "DaneViewTests"
Cohesion: 0.23
Nodes (3): _csv(), DaneViewTests, ImportServiceTests

### Community 60 - "_save"
Cohesion: 0.43
Nodes (5): HallGeneratorForm, _initial(), _md_role, _save(), warehouse_model_generator()

### Community 61 - "VoiceViewTests"
Cohesion: 0.09
Nodes (19): FakeResp, opener_err(), opener_ok(), override_settings, SimpleTestCase, Klient ElevenLabs — zawsze z podstawionym `opener` (bez sieci)., SynthesizeTests, fake_tts() (+11 more)

### Community 62 - "blender_route.py"
Cohesion: 0.17
Nodes (13): Item, Osie czasu agentów (wózki widłowe, ludzie) i ładunków (palety, kartony) dla…, Ładunek: paleta albo karton. `appear`/`vanish` sterują widocznością w Blenderze., _at(), container_inbound(), Przyjęcie kontenera z kartonami luzem (plan 2026-10-02, etap 2b) — czysty…, docks: [(środek doku kontenerowego)], stations: [(środek stanowiska…, heading_deg() (+5 more)

### Community 64 - "ForecastTests"
Cohesion: 0.17
Nodes (3): ForecastTests, SimpleTestCase, SegmentationTests

### Community 65 - "WarehouseHallFeatureTests"
Cohesion: 0.23
Nodes (3): TestCase, rows: lista dictów pól równoległych → payload z listami., WarehouseHallFeatureTests

### Community 66 - "render/views.py"
Cohesion: 0.16
Nodes (12): create(), delete(), jobs(), Meta, any_role, designer, require_POST, Stan zleceń w toku — strona odpytuje i przeładowuje się, gdy coś się zmieni. (+4 more)

### Community 68 - "test_container_inbound.py"
Cohesion: 0.22
Nodes (8): outward(), Kierunek „na zewnątrz hali” od elementu przy ścianie: normalna najbliższej…, ContainerInboundTests, _f(), _items(), SimpleTestCase, Przyjęcie kontenera w animacji (plan 2026-10-02, etap 2b): kontener przy doku →…, _scene()

### Community 69 - "EwmTasksPollingTests"
Cohesion: 0.25
Nodes (3): EwmTasksPollingTests, TestCase, Import „w tle” ponad STALE_AFTER = proces padł — polling ma się zatrzymać.

### Community 70 - "test_blender_export.py"
Cohesion: 0.20
Nodes (6): BuildSceneTests, SimpleTestCase, _rack(), Eksport modelu magazynu do animacji przepływów w Blenderze (tools/blender/)., RouteGeometryTests, _scene()

### Community 71 - "FlowSceneEndpointTests"
Cohesion: 0.24
Nodes (3): FlowPlayerPanelTests, FlowSceneEndpointTests, TestCase

### Community 72 - "bay_templates.py"
Cohesion: 0.19
Nodes (12): Named location type template — dimensions apply to all locations with matching…, WarehouseRackType, bay_template_delete(), bay_template_form(), bay_template_list(), _int(), _levels_from_post(), _md_role (+4 more)

### Community 73 - "ewm_demo_tasks.py"
Cohesion: 0.31
Nodes (9): bin_code(), day_tasks(), main(), Demonstracyjny eksport zadań magazynowych EWM (/SCWM/MON) do importu w TWINEMA.…, Zadania jednego dnia: [(rodzaj, materiał, dokument)] w kolejności do rozdania…, `n` chwil potwierdzeń jednego zasobu w zmianie: start + odstępy ~ mean_gap,…, row(), rows_for_day() (+1 more)

### Community 74 - "blender_stock.py"
Cohesion: 0.20
Nodes (9): _deg(), _half(), Rzeczywiste palety w lokalizacjach → scena Blendera („cyfrowe zdjęcie"…, 1/2 dla połówki miejsca (kod z końcówką -1/-2, np. B0-07-300C-1), inaczej 0.…, dict gniazda: x, y, z (dół palety), heading, rozmiar [w, d] (+ half 1/2) albo…, Na ile części (w pionie) dzielony jest otwór poziomu danej półki; całe miejsce…, shelves_in_opening(), parse_code() (+1 more)

### Community 76 - "test_ml.py"
Cohesion: 0.17
Nodes (6): Meta, ModelRun, Przebiegi modeli ML: wersja algorytmu, dane wejściowe, parametry, miary i wynik…, MlRunTests, TestCase, ML1 prognoza + ML2 segmentacja: czyste moduły, zapis przebiegów, ekrany.

### Community 77 - "params_for"
Cohesion: 0.24
Nodes (6): params_for(), Parametry elementu: domyślne z katalogu + nadpisania (tylko znane klucze)., BlenderImportGuardTests, CatalogTests, SimpleTestCase, Blender importuje te moduły bez Django — żadnego importu Django na poziomie…

### Community 80 - "studio/models.py"
Cohesion: 0.08
Nodes (18): Meta, Zlecenia renderu: aplikacja kolejkuje, worker z Blenderem (poza serwerem)…, RenderJob, Meta, MontageJob, Presentation, Studio prezentacji: film o modelu hali składany z ujęć (preset kamery + kwestia…, Nagranie pasuje do obecnego tekstu i głosu (po poprawce kwestii — nieaktualne). (+10 more)

### Community 83 - "segmentation.py"
Cohesion: 0.23
Nodes (12): _demo(), _dist2(), features(), kmeans(), _name(), ML2 — segmentacja materiałów pod rozmieszczenie (slotting): k-means na profilu…, {materiał: {hits, cv, active, volume?}} — tylko materiały z ruchem., k-means++ → (przypisania, centroidy, inercja). Deterministyczne dla danego… (+4 more)

### Community 84 - "ewm_tasks.py"
Cohesion: 0.18
Nodes (13): _delimiter(), _encoding(), is_cancelled(), iter_table(), kind_from_word(), norm_header(), _parse_dt(), _parse_time() (+5 more)

### Community 85 - "icon"
Cohesion: 0.40
Nodes (4): simple_tag, icon(), Tagi szablonów modułu: ikony Lucide ze sprite'a static/twin/icons/lucide.svg., {% icon "package" %} → dekoracyjna (aria-hidden); z label → role=img + aria-…

### Community 86 - "shared.py"
Cohesion: 0.09
Nodes (31): letter_level(), Sam numer poziomu 1..5 (``default`` dla nieznanej litery)., hall_feature_kinds(), _parse_location_code(), Wspólne importy i pomocnicze widoków bliźniaka — odpowiednik jądra widoków ze…, Zapis edytowalnej tabeli elementów hali z równoległych list POST + deleted_ids., JSON bezpieczny do osadzenia w <script> przez |safe (escapuje <, >, & i…, B0-01-300A → (zone, rack, bay, level_letter, level_num). (+23 more)

### Community 95 - "blender_tasks.py"
Cohesion: 0.22
Nodes (10): default_start(), load_window(), parse_start(), Wózki w animacji z realnych zadań magazynowych EWM (WT) zamiast symulacji demo.…, Początek pierwszej pełnej godziny z zadaniami partii (czas lokalny)., „2026-03-02T06:00” (input datetime-local, czas lokalny) → datetime ze strefą…, Zadania partii potwierdzone w oknie [start, start + hours) — najwyżej `limit`…, _clamped_float() (+2 more)

### Community 117 - "map_columns"
Cohesion: 0.24
Nodes (7): map_columns(), missing_required(), {pole: indeks kolumny}. Najpierw dokładne aliasy, potem nagłówek zaczynający…, DemoFileTests, SimpleTestCase, Zakładka „Projektowanie magazynu” w Magazyn 3D + plik demonstracyjny WT…, HeaderAliasTests

### Community 118 - "parse_stamp"
Cohesion: 0.36
Nodes (3): parse_stamp(), Data (+ osobny czas, jak w eksporcie SAP) → datetime ze strefą `tz` albo None., ValueParsingTests

### Community 119 - "build_pallets"
Cohesion: 0.20
Nodes (5): build_pallets(), Czysta funkcja: dane wejściowe jako proste krotki/dicty → (pallets, stats,…, BuildPalletsTests, ParseCodeTests, SimpleTestCase

### Community 120 - "parse_row"
Cohesion: 0.15
Nodes (12): map_kind(), parse_number(), parse_overrides(), parse_row(), „1.234,5” / „1,234.5” / „1 234,5” / „5-” (minus SAP na końcu) / liczba → float;…, „2010 = wydanie” (linia na proces) → ({proces: rodzaj}, [błędy])., Rodzaj procesu mag. → rodzaj ruchu. Kolejność: nadpisania → słownik wyjątków →…, Wiersz → dict pól `WarehouseTask` (+ `cancelled`); None = pusty wiersz;… (+4 more)

### Community 123 - "GeneratorTests"
Cohesion: 0.18
Nodes (3): GeneratorTests, SimpleTestCase, _rect()

### Community 124 - "ml/services.py"
Cohesion: 0.29
Nodes (10): Przebiegi ML na imporcie zadań: dane z bliźniaka → czyste moduły…, run_forecast(), run_segmentation(), _user(), abc_by_hits(), Klasa ABC wg udziału w pobraniach (ta sama reguła progów co…, Dni z ruchem ≥ WORKDAY_SHARE mediany dni z jakimkolwiek ruchem (rosnąco)., working_days() (+2 more)

### Community 125 - "twinema_render.py"
Cohesion: 0.33
Nodes (8): apply_preset(), _key(), main(), TWINEMA → Blender: render ujęcia (preset kamery) ze sceny „twinema.scene”.…, FFmpeg H.264 w MP4 — Blender 5 przeniósł format wideo do `media_type`., Ustawia „Kamerę TWINEMA” i jej cel wg presetu na klatkach 1…frames., render(), _video_settings()

### Community 126 - "_tasks"
Cohesion: 0.31
Nodes (3): SimpleTestCase, SimulationTests, _tasks()

### Community 134 - "demo.py"
Cohesion: 0.50
Nodes (4): demo_materials(), material_codes(), Dane demonstracyjne (syntetyczne): materiały zgodne z `tools/ewm_demo_tasks.py`…, Wiersze materiałów (dicty pól Material) z losowymi, ale wiarygodnymi wymiarami.

### Community 136 - "warehouse_model_copy"
Cohesion: 0.50
Nodes (4): _md_role, require_POST, Kopia modelu (regały + elementy hali) — wariant do przeróbek bez ruszania…, warehouse_model_copy()

### Community 141 - "locations.py"
Cohesion: 0.50
Nodes (3): active_master_qs(), Kody lokalizacji magazynu — wspólna konwencja mapy 3D / eksportu SAP. Litera na…, Lokalizacje z aktywnej partii master-daty (pusty queryset, gdy brak partii).…

## Knowledge Gaps
- **47 isolated node(s):** `docker-entrypoint.sh script`, `Migration`, `Migration`, `Meta`, `Migration` (+42 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **35 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `WarehouseModel` connect `twin/models.py` to `rack_corners`, `render/views.py`, `test_blender_export.py`, `test_dane.py`, `masterdata/views.py`, `generate`, `test_model_edit.py`, `studio/models.py`, `test_design_calibration.py`, `studio/views.py`, `shared.py`, `test_deck.py`, `VoiceViewTests`?**
  _High betweenness centrality (0.074) - this node is a cross-community bridge._
- **Why does `synthesize()` connect `VoiceViewTests` to `twinema_montage.py`, `studio/views.py`?**
  _High betweenness centrality (0.050) - this node is a cross-community bridge._
- **Why does `Api` connect `twinema_montage.py` to `VoiceViewTests`?**
  _High betweenness centrality (0.048) - this node is a cross-community bridge._
- **Are the 8 inferred relationships involving `SlotLocator` (e.g. with `BuildPalletsTests` and `ParseCodeTests`) actually correct?**
  _`SlotLocator` has 8 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `WarehouseModel` (e.g. with `Meta` and `WarehouseModelForm`) actually correct?**
  _`WarehouseModel` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Are the 5 inferred relationships involving `Scan` (e.g. with `HeaderAliasTests` and `KindMappingTests`) actually correct?**
  _`Scan` has 5 INFERRED edges - model-reasoned connections that need verification._
- **What connects `docker-entrypoint.sh script`, `Migration`, `Migration` to the rest of the system?**
  _47 weakly-connected nodes found - possible documentation gaps or missing edges._