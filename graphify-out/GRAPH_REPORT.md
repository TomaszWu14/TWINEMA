# Graph Report - agent-abffdf6c586020097  (2026-10-05)

## Corpus Check
- 243 files · ~151,179 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 2735 nodes · 5691 edges · 182 communities (142 shown, 40 thin omitted)
- Extraction: 96% EXTRACTED · 4% INFERRED · 0% AMBIGUOUS · INFERRED: 201 edges (avg confidence: 0.53)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `7e446dac`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- shared.py
- day_demand
- studio/api.py
- engine.py
- twinema_warehouse_anim.py
- test_foundation.py
- warehouse_tasks.py
- simulate
- twin/models.py
- masterdata/services.py
- design_kpi.py
- blender_scene.py
- Material
- layout.py
- design_catalog.py
- test_ewm_service.py
- ml/views.py
- test_design_sim_scene.py
- twinema_design_kit.py
- importers.py
- context_processors.py
- test_voice.py
- ewm_levels.py
- WorkerApiTests
- twinema_montage.py
- test_addressing.py
- test_design_forecast.py
- studio/models.py
- TasksEndpointAndImportTests
- WarehouseModelViewTests
- Agent
- design_day.py
- forecast.py
- layout-panels.js
- kpi_facts
- TWINEMA — zakres i plan
- BayTemplate
- ParseTests
- warehouse_compare.py
- ewm_service.py
- warehouse_variants.py
- StudioViewTests
- draft_script
- scenario/views.py
- day-timeline.js
- BayTemplateViewTests
- EquipmentAgentsTests
- middleware.py
- Scenario
- ._scene
- Scan
- layout-core.js
- studio/views.py
- CLAUDE.md — TWINEMA
- WarehouseModelPasteTests
- build_deck
- ADR-0001: Kopia kodu modelowania magazynu, nie przeniesienie
- RenderMontageTests
- layout-editor.js
- test_dane.py
- test_sim.py
- VoiceViewTests
- views_sim.py
- pre-push
- ForecastTests
- WarehouseHallFeatureTests
- LayoutApiTests
- layout-hall.js
- compliance
- EwmTasksPollingTests
- blender_route.py
- FlowSceneEndpointTests
- bay_templates.py
- ewm_demo_tasks.py
- masterdata/views.py
- RackTypeWeightsTests
- EwmViewsTests
- CalibrationTests
- Pochodzenie kodu
- ScenarioViewTests
- Shot
- LoadAndViewTests
- addressing.py
- segmentation.py
- SimViewTests
- icon
- warehouse_model.py
- DesignHubTests
- CoreConfig
- health
- MasterdataConfig
- MlConfig
- RenderConfig
- fetch_vendor.sh
- TwinConfig
- warehouse_blender.py
- docker-entrypoint.sh
- masterdata/migrations/0001_initial.py
- ml/migrations/0001_initial.py
- render/migrations/0001_initial.py
- map_columns
- test_ewm_tasks_parser.py
- SlotLocator
- parse_overrides
- TWINEMA — założenia master daty i scenariuszy
- 0002_lektor.py
- ml/services.py
- 0002_pole_odkladcze.py
- twinema_render.py
- parse_bay_numbers
- StudioConfig
- GeneratorTests
- studio/migrations/0001_initial.py
- .as_dict
- blender_stock.py
- layout-preview.js
- test_play.py
- CompareViewTests
- 0003_render_montaz.py
- test_ml.py
- .handle
- ScenarioConfig
- test_container_inbound.py
- scenario/migrations/0001_initial.py
- 0004_kadry.py
- StructureApiTests
- ewm_tasks.py
- generate
- VariantEditViewTests
- test_ewm_detect.py
- GeneratorViewTests
- test_model_edit.py
- 0002_wydania_obsada.py
- GeometryUploadTests
- _save
- views_play.py
- report.py
- 0003_konstrukcja_hali.py
- 0003_symulacja_dnia.py
- build_plan
- 0003_domyslne_nosniki_klasy.py
- simulate_plan
- 0002_opakowania_nosniki.py
- VariantViewTests
- load_groups
- Command
- params_for
- design_calibration.py
- simulate
- WarehouseTask
- fullscreen.test.mjs
- BlenderExportViewTests
- parse_row
- BuildSceneTests
- TestCase
- BottleneckTests
- warehouse_model_copy
- BlenderImportGuardTests
- MetaRefreshGuardTests

## God Nodes (most connected - your core abstractions)
1. `WarehouseModel` - 38 edges
2. `SlotLocator` - 33 edges
3. `simulate()` - 29 edges
4. `Scenario` - 25 edges
5. `build_scene()` - 24 edges
6. `WarehouseModelRack` - 24 edges
7. `generate()` - 23 edges
8. `Scan` - 23 edges
9. `clean_layout()` - 23 edges
10. `check_layout()` - 23 edges

## Surprising Connections (you probably didn't know these)
- `bottlenecks()` --calls--> `add()`  [INFERRED]
  web/scenario/sim/report.py → tools/blender/twinema_design_kit.py
- `start()` --calls--> `params_for()`  [EXTRACTED]
  tools/blender/twinema_design_kit.py → web/twin/design_catalog.py
- `load_variant()` --calls--> `params_for()`  [EXTRACTED]
  tools/blender/twinema_design_kit.py → web/twin/design_catalog.py
- `add()` --calls--> `params_for()`  [EXTRACTED]
  tools/blender/twinema_design_kit.py → web/twin/design_catalog.py
- `add_block()` --calls--> `rack_axes()`  [EXTRACTED]
  tools/blender/twinema_design_kit.py → web/twin/blender_route.py

## Import Cycles
- None detected.

## Communities (182 total, 40 thin omitted)

### Community 0 - "shared.py"
Cohesion: 0.13
Nodes (20): load_inputs(), Agregaty zadań potwierdzonych partii (czas lokalny) — liczone w bazie, nie w…, Zadania magazynowe EWM (WT) — import z monitora magazynu (/SCWM/MON) do…, WarehouseTaskBatch, Wspólne importy i pomocnicze widoków bliźniaka — odpowiednik jądra widoków ze…, JSON bezpieczny do osadzenia w <script> przez |safe (escapuje <, >, & i…, safe_json(), design_hub() (+12 more)

### Community 1 - "day_demand"
Cohesion: 0.12
Nodes (20): arrivals_count(), day_demand(), _hhmm(), peak_concurrency(), _pick(), Plan przyjęć → zapotrzebowanie dnia (czysty Python — bez Django, testowalny bez…, Liczba przyjazdów po wzroście — zaokrąglenie w górę (auto albo jest, albo go…, n przyjazdów równomiernie w oknie [od, do): środki n równych odcinków. (+12 more)

### Community 2 - "studio/api.py"
Cohesion: 0.16
Nodes (24): claim(), _claimed_job(), fail(), _forbidden(), require_GET, require_POST, API workera renderów. Uwierzytelnienie: nagłówek X-Worker-Token…, Zlecenia „w toku” dłużej niż RENDER_STALE_MIN (worker padł) wracają do kolejki. (+16 more)

### Community 3 - "engine.py"
Cohesion: 0.13
Nodes (14): Pool, Silnik zdarzeniowy dnia scenariusza (czysty Python, czas w godzinach od 0:00).…, Ludzie procesu: jeden „slot” na osobę na zmianę, dostępny [początek, koniec).…, cutoff_risk(), process_hours(), productive_h(), Obsada: potrzebna vs zakładana per proces i zmiana + ryzyko cut-off kurierów…, → [{process, label, hours, shifts:[{…, needed, gap}], needed, assumed, short}]… (+6 more)

### Community 4 - "twinema_warehouse_anim.py"
Cohesion: 0.14
Nodes (37): _animate_agent(), _animate_item(), _bl(), _box_mesh(), build(), _build_feature(), _build_floor(), _build_pallets() (+29 more)

### Community 5 - "test_foundation.py"
Cohesion: 0.07
Nodes (17): BaseSettings, login_required, model_validator, AccessTests, ConfigTests, GroupContractTests, HealthTests, SimpleTestCase (+9 more)

### Community 6 - "warehouse_tasks.py"
Cohesion: 0.11
Nodes (31): never_cache, location_report(), purge_stale(), Import zadań magazynowych EWM do bazy: `ewm_tasks.Scan` (strumień) →…, Lokalizacje z zadań partii vs regały modelu: ile trafia w gniazda, ile jest…, Porzucone podglądy (nikt nie kliknął „Importuj”) — kasowane po dobie., Zapis uploadu na dysk kawałkami → token (nazwa pliku) do podglądu i importu., Ścieżka pliku po tokenie z formularza — tylko nasz format nazwy (bez path… (+23 more)

### Community 7 - "simulate"
Cohesion: 0.09
Nodes (26): Najmniejsze k ∈ 1..limit, dla którego `ok(fix(k))`; None, gdy nie pomaga., _smallest(), Gniazdo regału: środek boku `bay_idx` (0..n-1) na poziomie `level` (1 =…, _slot(), _Agent, _kpi(), Layout, _manh() (+18 more)

### Community 8 - "twin/models.py"
Cohesion: 0.07
Nodes (27): Dekorator: wymaga zalogowania + członkostwa w grupie (superuser zawsze…, role_required(), demo_hall(), Hala z generatora z 3 dokami paletowymi IN (preset ma 1 — przy 16+ autach…, Symulacja dnia w aplikacji (S3a): uruchomienie, wynik na ekranie scenariusza,…, Ekrany studia: role, szkic z szablonu, edycja tylko w szkicu, akceptacja, szkic…, Lektor w aplikacji: nagrywanie po akceptacji, cache po hashu, statusy, SRT. TTS…, Migration (+19 more)

### Community 9 - "masterdata/services.py"
Cohesion: 0.11
Nodes (22): Command, BaseCommand, import_file(), _level_of(), load_demo(), Zapis importów do bazy + odczyt danych dla bliźniaka (stany do sceny, grupy do…, Nowy aktywny master lokalizacji (poprzednie nieaktywne) — ten sam, którego…, Plik → ImportLog z raportem. ImportFileError, gdy pliku nie da się czytać albo… (+14 more)

### Community 10 - "design_kpi.py"
Cohesion: 0.13
Nodes (18): rack_axes(), (u_w, u_d) — jednostkowe osie szerokości i głębokości regału w układzie hali., anchor_count(), anchors(), _center(), clean_elements(), equipment_capacity(), Wskaźniki wariantu projektu magazynu (czysty Python — testowalny bez bazy i… (+10 more)

### Community 11 - "blender_scene.py"
Cohesion: 0.09
Nodes (40): Item, Ładunek: paleta albo karton. `appear`/`vanish` sterują widocznością w Blenderze., _at(), container_inbound(), Przyjęcie kontenera z kartonami luzem (plan 2026-10-02, etap 2b) — czysty…, docks: [(środek doku kontenerowego)], stations: [(środek stanowiska…, heading_deg(), rack_point() (+32 more)

### Community 12 - "Material"
Cohesion: 0.08
Nodes (20): PureTestCase, Carrier, ImportLog, Material, Meta, PalletClass, Dane podstawowe bliźniaka: materiały, stany w lokalizacjach i dziennik…, Jeden import pliku: rodzaj, wynik i próbka odrzuconych wierszy. Import stanów… (+12 more)

### Community 13 - "layout.py"
Cohesion: 0.05
Nodes (73): skipUnless, overlap_depth(), Głębokość nachodzenia dwóch obróconych prostokątów (narożniki w kolejności…, analyze(), check_layout(), clean_columns(), clean_layout(), clean_underlay() (+65 more)

### Community 14 - "design_catalog.py"
Cohesion: 0.15
Nodes (19): _geometry(), near_pairs(), Pary (i, j), i < j, których obrysy osiowe poszerzone o `pad` się stykają —…, check_aisles(), element_summary(), footprint(), height(), pallet_positions() (+11 more)

### Community 15 - "test_ewm_service.py"
Cohesion: 0.14
Nodes (12): LocationOverride, Wyjątek adresu: nadpisuje wynik szablonu dla jednego miejsca albo całego…, One import of location master data (height, volume, weight, type)., WarehouseLocationMasterBatch, load_sample(), Syntetyczna próbka mastera lokalizacji (hala B0) dla testów „Wykryj z EWM” i…, [(kod, typ EWM)] — kod B0-<rząd>-<gniazdo><pozycja palety><litera poziomu>., make_model_and_master() (+4 more)

### Community 16 - "ml/views.py"
Cohesion: 0.25
Nodes (8): detail(), home(), _int(), any_role, designer, require_POST, run(), segments_csv()

### Community 17 - "test_design_sim_scene.py"
Cohesion: 0.08
Nodes (17): build_sim_scene(), CorridorRouter, _pick_time(), Animacja godziny z symulacji dnia (plan 2026-10-02, etap 3b) — czysty Python.…, Trasa „jak w magazynie”: wzdłuż korytarza do przejazdu poprzecznego, nim do…, Chwila przejęcia ładunku: kombi rusza wcześniej niż AGV, ale paletę bierze po…, Przebiegi rozpoczęte w godzinie `hour` (zegar 5–21). Zwraca (przebiegi, ile…, window_legs() (+9 more)

### Community 18 - "twinema_design_kit.py"
Cohesion: 0.19
Nodes (21): add(), add_block(), _clear(), _coll(), elements(), export_variant(), load_variant(), _make() (+13 more)

### Community 19 - "importers.py"
Cohesion: 0.09
Nodes (36): _bool(), _cell(), _code(), _date(), ImportFileError, map_columns(), missing_required(), norm() (+28 more)

### Community 21 - "test_voice.py"
Cohesion: 0.10
Nodes (26): align(), AlignmentTests, CueTests, TestCase, Czysta logika lektora: hash cache, długość, słowa, plansze napisów, SRT., Sztuczne wyrównanie: każdy znak trwa per_char sekund., SrtTests, VoiceKeyTests (+18 more)

### Community 22 - "ewm_levels.py"
Cohesion: 0.13
Nodes (20): NamedTuple, code_slot(), is_hall_a(), letter_level(), letter_slot(), LetterSlot, level_height_keys(), level_height_mm() (+12 more)

### Community 23 - "WorkerApiTests"
Cohesion: 0.16
Nodes (4): override_settings, TestCase, RenderScreenTests, WorkerApiTests

### Community 24 - "twinema_montage.py"
Cohesion: 0.06
Nodes (32): Api, find_blender(), main(), Worker renderów TWINEMA — uruchamiany na komputerze z Blenderem (np. z GPU).…, Montaż filmu: pobierz ujęcia i nagrania, wykonaj komendy z…, BLENDER_BIN / --blender → PATH → typowe katalogi instalacji (najnowsza wersja)., run_job(), run_montage() (+24 more)

### Community 25 - "test_addressing.py"
Cohesion: 0.23
Nodes (9): expand_row(), Rząd + szablon domyślny + wyjątki → lista miejsc (dict). Klucze: code, bay,…, codes(), ExpandModelTests, ExpandRowTests, ov(), SimpleTestCase, Generator adresów modelu magazynu: szablon gniazda + reguła rzędu + wyjątki… (+1 more)

### Community 26 - "test_design_forecast.py"
Cohesion: 0.20
Nodes (12): backtest(), fit(), forecast(), series: [(dzień porządkowy, wartość)] → (nachylenie log/tydzień, wyraz wolny,…, MAPE [%] prognozy ostatnich `weeks` tygodni z modelu uczonego bez nich (None —…, Wzrost per strumień: roczne tempo P50/P90, mnożnik na `years` lat, MAPE testu…, _daily(), ForecastTests (+4 more)

### Community 27 - "studio/models.py"
Cohesion: 0.09
Nodes (19): Meta, Zlecenia renderu: aplikacja kolejkuje, worker z Blenderem (poza serwerem)…, RenderJob, Kolejka renderów: API workera (token, przejęcie, scena, wynik) i ekran zleceń., create(), delete(), jobs(), Meta (+11 more)

### Community 28 - "TasksEndpointAndImportTests"
Cohesion: 0.15
Nodes (4): override_settings, TestCase, Duży plik → import w wątku w tle (bez blokowania żądania), partia kończy się…, TasksEndpointAndImportTests

### Community 29 - "WarehouseModelViewTests"
Cohesion: 0.11
Nodes (9): InstancingGuardTests, TestCase, UX #5: widok 3D nie może cicho paść czarnym ekranem — spinner + guard WebGL +…, Regresja bezpieczeństwa: wolny tekst pól regału/elementu (zone/rack_id/label)…, Regresja: FLOOR_W/FLOOR_D w JS muszą mieć KROPKĘ dziesiętną, nie polski…, R1: stal regałów renderowana przez InstancedMesh (3 draw calle), nie per-mesh.…, StoredXSSGuardTests, ViewFloatLocalizationTests (+1 more)

### Community 30 - "Agent"
Cohesion: 0.14
Nodes (11): Agent, _r(), Osie czasu agentów (wózki widłowe, ludzie) i ładunków (palety, kartony) dla…, Postój do chwili `t` (realny znacznik zadania); zajęty agent nie cofa się w…, Przejęcie ładunku: klatka „na miejscu" → po `handling` s ładunek jest na…, Odłożenie ładunku w `pos` na wysokości `z` (np. gniazdo regału albo dok)., Agent z osią czasu ruchu: rodzaj z `SPEED` (wózek, pracownik, kombi, AGV, EPT)., Jazda/przejście trasą A* do `target`; trasa trafia też do mapy przepływów. (+3 more)

### Community 31 - "design_day.py"
Cohesion: 0.11
Nodes (18): _abc_xyz(), build_profile(), _groups(), _order_profile(), percentile(), Profil ruchów i dzień projektowy z zadań EWM (spec projektowania magazynu, krok…, daily: {data: {rodzaj: n, "orders": n}}; hourly: {(data, godzina): {rodzaj:…, Percentyl z interpolacją liniową (jak numpy/Excel PERCENTILE.INC); pusta lista… (+10 more)

### Community 32 - "forecast.py"
Cohesion: 0.16
Nodes (13): candidates(), _demo(), evaluate(), fit(), _grid(), mape(), ML1 — prognoza tygodniowych wolumenów: kilka modeli wygładzania wykładniczego…, Najlepsze parametry modelu na serii `y` → (params, fitted, prognoza h→v, sd… (+5 more)

### Community 33 - "layout-panels.js"
Cohesion: 0.17
Nodes (28): makeBlock(), mode(), nextRackIds(), addItems(), change(), deleteSelected(), duplicateSelected(), keyOf() (+20 more)

### Community 34 - "kpi_facts"
Cohesion: 0.11
Nodes (18): clean_draft(), estimate_seconds(), _get(), kpi_facts(), _num(), Scenariusz prezentacji (czysty Python — bez Django i bez sieci). • `kpi_facts`…, Liczba po polsku: spacja tysięcy, przecinek dziesiętny., Zdania z liczbami wariantu. Brak wartości → zdanie pominięte (nie zgadujemy). (+10 more)

### Community 35 - "TWINEMA — zakres i plan"
Cohesion: 0.08
Nodes (23): Następny krok: F6 — szlif (wg burzy mózgów, `docs/PLAN.md` §2.2 i §6), Po stronie właściciela (zanim pierwszy prawdziwy film), Przekazanie — stan projektu i następny krok (F6), Stan, Zasady repo (skrót — pełne w `CLAUDE.md`), 1. Decyzje, 2.1 MVP, 2.2 Po MVP (wsad do burzy mózgów) (+15 more)

### Community 36 - "BayTemplate"
Cohesion: 0.16
Nodes (7): BayTemplate, Szablon gniazda (słupa regału): belka, palety na belce, poziomy od podłogi w…, BayTemplateTests, levels(), TestCase, RackRuleAndOverrideTests, Modele części 1: szablon gniazda (walidacja), reguła rzędu, wyjątki…

### Community 37 - "ParseTests"
Cohesion: 0.11
Nodes (6): MapColumnsTests, ParseTests, SimpleTestCase, Wzór pliku z ekranu Dane musi się importować bez ręcznych poprawek., ReadTableTests, _xlsx()

### Community 38 - "warehouse_compare.py"
Cohesion: 0.14
Nodes (18): _is_shelf(), model_floor(), Hala co najmniej tak duża, jak obrys regałów (dane bywają „poza halą")., capacity(), comparison(), Porównanie wariantów hali na tym samym dniu projektowym (plan 2026-10-02, etap…, Miejsca paletowe (regały nie-półkowe), lokalizacje kartonowe (półki K1), bramy,…, Symulacja z flotą sugerowaną przez poprzedni przebieg, aż flota się ustali (≤… (+10 more)

### Community 39 - "ewm_service.py"
Cohesion: 0.10
Nodes (30): active_master(), apply_proposal(), compliance_for_model(), detect_for_model(), master_rows(), plan_for_model(), atomic, Warstwa ORM nad czystymi modułami adresowania: master EWM, plan modelu, zapis… (+22 more)

### Community 40 - "warehouse_variants.py"
Cohesion: 0.24
Nodes (13): _comparison(), _get(), _md_role, _planner, require_POST, Wariant jako twinema.design-variant — do dalszej edycji w Blenderze…, Wiersze tabeli: wartości per wariant + oznaczenie najlepszej + różnica do…, _save_variant() (+5 more)

### Community 41 - "StudioViewTests"
Cohesion: 0.23
Nodes (3): override_settings, TestCase, StudioViewTests

### Community 42 - "draft_script"
Cohesion: 0.19
Nodes (16): BaseModel, draft_script(), enabled(), Exception, Szkic scenariusza z Claude API. Do modelu trafiają WYŁĄCZNIE zdania z…, Błąd do pokazania użytkownikowi (bez szczegółów technicznych)., facts: lista zdań z liczbami → (shots, ostrzeżenia). Rzuca ScriptAIError., ScriptAIError (+8 more)

### Community 43 - "scenario/views.py"
Cohesion: 0.13
Nodes (28): has_role(), True dla superusera albo członka którejś z grup., [(kartonów/paletę, waga)] → średnia ważona (np. liczbą palet na stanie). None,…, weighted_cartons_per_pallet(), cartons_per_pallet_hint(), Podpowiedź do normy scenariusza „kartonów na paletę”: średnia ważona liczbą…, _arrival_rows(), day_save() (+20 more)

### Community 44 - "day-timeline.js"
Cohesion: 0.05
Nodes (58): COLOR, createDayPlayer(), instanced(), SIZE, buildTracks(), countersAt(), dayRange(), hashId() (+50 more)

### Community 45 - "BayTemplateViewTests"
Cohesion: 0.20
Nodes (4): BayTemplateViewTests, CoordsRuleColumnsTests, level_post(), TestCase

### Community 46 - "EquipmentAgentsTests"
Cohesion: 0.22
Nodes (6): EquipmentAgentsTests, SimpleTestCase, _rack(), Paleta przechodzi AGV → kombi w jednym miejscu: między klatkami nie skacze…, Czas klatek palety rośnie: kombi czeka (wait_until), zamiast „cofać" paletę w…, _scene()

### Community 47 - "middleware.py"
Cohesion: 0.13
Nodes (9): client_ip(), Middleware przekrojowe: identyfikator żądania (korelacja logów) + nagłówki…, Dopisuje `record.request_id` z bieżącego żądania ("-" poza żądaniem)., Bierze X-Request-ID od proxy albo nadaje nowy; odsyła go w odpowiedzi., Permissions-Policy + Content-Security-Policy (domyślnie report-only)., IP klienta dla django-axes za jednym zaufanym proxy (Traefik/Coolify): ostatni…, RequestIDLogFilter, RequestIDMiddleware (+1 more)

### Community 48 - "Scenario"
Cohesion: 0.13
Nodes (23): Scenariusz referencyjny (syntetyczny, anonimowy): centrum dystrybucyjne z…, check_triples(), InboundStream, Meta, OutboundStream, Scenariusz: założenia wolumenów niezależne od layoutu (ten sam scenariusz…, Dzień typowy i szczytowy; nowe dostają domyślne strumienie i profil (szczyt:…, Auta wyjazdowe — jak przyjęcia. Koniec okna = cut-off (odjazd / odbiór kuriera). (+15 more)

### Community 49 - "._scene"
Cohesion: 0.24
Nodes (5): SimpleTestCase, _racks(), ResolveMovesTests, _row(), SceneFromTasksTests

### Community 50 - "Scan"
Cohesion: 0.23
Nodes (5): Przebieg po pliku: nagłówek → mapowanie kolumn → wiersze sparsowane albo błędy,…, Poprawne, nieanulowane zadania (dicty pól modelu)., [(etykieta pola, nagłówek z pliku)] w kolejności pól., Scan, ScanFileTests

### Community 51 - "layout-core.js"
Cohesion: 0.15
Nodes (15): axes(), BACK_GAP_M, bbox(), center(), corners(), History, rad(), rotateAround() (+7 more)

### Community 52 - "studio/views.py"
Cohesion: 0.12
Nodes (33): approve(), deck_pdf(), _draft_or_back(), film_file(), model_kpi(), montage_create(), montage_input_key(), montage_ready() (+25 more)

### Community 53 - "CLAUDE.md — TWINEMA"
Cohesion: 0.33
Nodes (5): CLAUDE.md — TWINEMA, Git, Graphify query-first, Testy (przed każdym PR), Zasady

### Community 55 - "build_deck"
Cohesion: 0.11
Nodes (14): FPDF, PlainTestCase, build_deck(), _Deck, Deck PDF prezentacji (czysty Python — fpdf2, bez Django i bez bazy). Strony…, „Etykieta: wartość.” → (etykieta, wartość) do kafla; zdanie bez dwukropka →…, slides: [{"label": "Przelot nad halą", "text": kwestia, "image": bytes PNG albo…, split_fact() (+6 more)

### Community 56 - "ADR-0001: Kopia kodu modelowania magazynu, nie przeniesienie"
Cohesion: 0.40
Nodes (4): ADR-0001: Kopia kodu modelowania magazynu, nie przeniesienie, Decyzja, Kontekst, Skutki

### Community 57 - "RenderMontageTests"
Cohesion: 0.18
Nodes (4): override_settings, TestCase, RenderMontageTests, _voice()

### Community 58 - "layout-editor.js"
Cohesion: 0.13
Nodes (25): svgTransform(), applyIssues(), CFG, check(), drawItem(), el(), fit(), fullscreen (+17 more)

### Community 59 - "test_dane.py"
Cohesion: 0.10
Nodes (15): demo_materials(), demo_stock(), material_codes(), Dane demonstracyjne (syntetyczne): materiały zgodne z `tools/ewm_demo_tasks.py`…, Wiersze materiałów (dicty pól Material) z losowymi, ale wiarygodnymi wymiarami:…, Pozycje stanu dla regałów modelu: ~`fill` miejsc zajętych, materiały wg rotacji…, _csv(), DaneViewTests (+7 more)

### Community 60 - "test_sim.py"
Cohesion: 0.22
Nodes (12): Symulacja dnia scenariusza na layoucie hali (S3a) — czysty Python, bez Django.…, Zwroty przychodzą w godzinach zmian obsługi zwrotów (bez ostatniej godziny)., returns_window(), run_day(), run_many(), _trouble(), Kopia miejsc z k dodatkowymi dokami danej roli (do podpowiedzi „+N doków”)., with_extra_docks() (+4 more)

### Community 61 - "VoiceViewTests"
Cohesion: 0.10
Nodes (18): FakeResp, opener_err(), opener_ok(), override_settings, SimpleTestCase, Klient ElevenLabs — zawsze z podstawionym `opener` (bez sieci)., SynthesizeTests, fake_tts() (+10 more)

### Community 62 - "views_sim.py"
Cohesion: 0.13
Nodes (13): Wynik symulacji dnia scenariusza na modelu hali (S3a): KPI średnia/najgorszy,…, ScenarioRun, Klej Django ↔ symulacja dnia (`scenario.sim` jest czystym Pythonem)., _cell(), any_role, designer, require_POST, Symulacja dnia scenariusza na modelu hali (S3a): uruchomienie, karta KPI,… (+5 more)

### Community 64 - "ForecastTests"
Cohesion: 0.17
Nodes (3): ForecastTests, SimpleTestCase, SegmentationTests

### Community 65 - "WarehouseHallFeatureTests"
Cohesion: 0.23
Nodes (3): TestCase, rows: lista dictów pól równoległych → payload z listami., WarehouseHallFeatureTests

### Community 66 - "LayoutApiTests"
Cohesion: 0.15
Nodes (5): LayoutApiTests, LayoutEditorPageTests, TestCase, Ekran edytora (E2): tylko Projektant/Administratorzy, konfiguracja dla modułu…, E3: podgląd 3D obok planu — three.js z vendora (importmap, bez CDN),…

### Community 67 - "layout-hall.js"
Cohesion: 0.29
Nodes (15): render(), status(), viewCenter(), CFG, deleteSelectedColumn(), drawColumns(), drawUnderlay(), el() (+7 more)

### Community 68 - "compliance"
Cohesion: 0.40
Nodes (4): compliance(), rows: [{"zone", "rack_id", "has_template"}]; locations/duplicates: wynik…, CompliancePureTests, SimpleTestCase

### Community 69 - "EwmTasksPollingTests"
Cohesion: 0.25
Nodes (3): EwmTasksPollingTests, TestCase, Import „w tle” ponad STALE_AFTER = proces padł — polling ma się zatrzymać.

### Community 70 - "blender_route.py"
Cohesion: 0.18
Nodes (8): _dedupe(), FloorGrid, Geometria i trasowanie dla eksportu animacji przepływów do Blendera. Czysty…, Najbliższa wolna komórka (BFS od komórki punktu) albo None, gdy hala zapchana., Trasa A* (8-sąsiedztwo, bez ścinania narożników regałów) z punktu a do b.…, Usuwa węzły leżące na prostej (zostają tylko zakręty)., Siatka zajętości posadzki: komórka zablokowana, jeśli leży w obrysie regału.…, _simplify()

### Community 71 - "FlowSceneEndpointTests"
Cohesion: 0.24
Nodes (3): FlowPlayerPanelTests, FlowSceneEndpointTests, TestCase

### Community 72 - "bay_templates.py"
Cohesion: 0.19
Nodes (12): Named location type template — dimensions apply to all locations with matching…, WarehouseRackType, bay_template_delete(), bay_template_form(), bay_template_list(), _int(), _levels_from_post(), _md_role (+4 more)

### Community 73 - "ewm_demo_tasks.py"
Cohesion: 0.31
Nodes (9): bin_code(), day_tasks(), main(), Demonstracyjny eksport zadań magazynowych EWM (/SCWM/MON) do importu w TWINEMA.…, Zadania jednego dnia: [(rodzaj, materiał, dokument)] w kolejności do rozdania…, `n` chwil potwierdzeń jednego zasobu w zmianie: start + odstępy ~ mean_gap,…, row(), rows_for_day() (+1 more)

### Community 74 - "masterdata/views.py"
Cohesion: 0.11
Nodes (25): cartons_per_pallet(), classify(), pallet_height_cm(), pallet_weight_kg(), Hierarchia opakowań sztuka → karton → paleta (czysty Python, bez Django).…, Kartonów/warstwę × warstw/paletę, gdy oba znane; inaczej wartość wpisana., Wpisana wysokość palety z towarem albo warstwy × wys. kartonu + wys. nośnika., Najmniejsza klasa z limitem ≥ wartość: classes = [(id, limit)]. Ponad… (+17 more)

### Community 75 - "RackTypeWeightsTests"
Cohesion: 0.20
Nodes (3): TestCase, RackTypeWeightsTests, Typy regałów A/B/C/D: nośność per poziom (level_weights) — zapis w edytorze,…

### Community 77 - "CalibrationTests"
Cohesion: 0.14
Nodes (7): CalibrationTests, CalibrationViewTests, SimpleTestCase, TestCase, Wózek przewozi palety między dwoma gniazdami co `gap_s` sekund., Ten sam ruch co 2 min vs co 4 min → współczynnik rośnie dwukrotnie., _rows()

### Community 79 - "ScenarioViewTests"
Cohesion: 0.19
Nodes (3): hhmm(), TestCase, ScenarioViewTests

### Community 80 - "Shot"
Cohesion: 0.11
Nodes (12): Meta, MontageJob, Presentation, Nagranie pasuje do obecnego tekstu i głosu (po poprawce kwestii — nieaktualne)., Długość klipu: nagranie + zapas 0,5 s, w granicach kolejki renderów (2–60 s)., Render pasuje do obecnego presetu i długości kwestii (stan zlecenia osobno)., Montaż filmu (ffmpeg w workerze na PC). Cache: ten sam `input_key` i gotowe →…, Nagranie lektora — cache po hashu (tekst + głos + model), współdzielony między… (+4 more)

### Community 82 - "addressing.py"
Cohesion: 0.14
Nodes (21): _bay_locations(), format_bay_numbers(), letter_rank(), parse_code(), Adresy miejsc paletowych modelu magazynu: szablon gniazda + reguła rzędu +…, Klucz sortowania liter poziomów: znane litery wg LETTER_ORDER, obce na końcu., Kod EWM → (strefa, przejście, gniazdo, pozycja, litera, połówka) albo None., [10, …, 47, 50] → „10-47,50” (odwrotność parse_bay_numbers). (+13 more)

### Community 83 - "segmentation.py"
Cohesion: 0.23
Nodes (12): _demo(), _dist2(), features(), kmeans(), _name(), ML2 — segmentacja materiałów pod rozmieszczenie (slotting): k-means na profilu…, {materiał: {hits, cv, active, volume?}} — tylko materiały z ruchem., k-means++ → (przypisania, centroidy, inercja). Deterministyczne dla danego… (+4 more)

### Community 85 - "icon"
Cohesion: 0.40
Nodes (4): simple_tag, icon(), Tagi szablonów modułu: ikony Lucide ze sprite'a static/twin/icons/lucide.svg., {% icon "package" %} → dekoracyjna (aria-hidden); z label → role=img + aria-…

### Community 86 - "warehouse_model.py"
Cohesion: 0.09
Nodes (33): rack_corners(), Meta, WarehouseModelForm, _column_corners(), floor_size(), is_geometry_csv(), _num(), parse_geometry_csv() (+25 more)

### Community 95 - "warehouse_blender.py"
Cohesion: 0.06
Nodes (52): _activity_picks(), build_scene_for_model(), model_racks(), Aktywność pickerów (picker, kod, materiał; kolejność = confirmed_at) → trasy.…, Regały WarehouseModel jako dicty w formacie sceny (x, y, width, depth,…, Scena dla `WarehouseModel`. `batch` = PickerActivityBatch (None → demo…, load_master_levels(), load_stock_inputs() (+44 more)

### Community 117 - "map_columns"
Cohesion: 0.24
Nodes (7): map_columns(), missing_required(), {pole: indeks kolumny}. Najpierw dokładne aliasy, potem nagłówek zaczynający…, DemoFileTests, SimpleTestCase, Zakładka „Projektowanie magazynu” w Magazyn 3D + plik demonstracyjny WT…, HeaderAliasTests

### Community 118 - "test_ewm_tasks_parser.py"
Cohesion: 0.22
Nodes (6): parse_number(), parse_stamp(), „1.234,5” / „1,234.5” / „1 234,5” / „5-” (minus SAP na końcu) / liczba → float;…, Data (+ osobny czas, jak w eksporcie SAP) → datetime ze strefą `tz` albo None., Parser eksportu zadań magazynowych EWM (WT): aliasy nagłówków, liczby, daty,…, ValueParsingTests

### Community 119 - "SlotLocator"
Cohesion: 0.17
Nodes (9): _inside(), Czy punkt leży w obrysie regału poszerzonym o `margin` [m]., _deg(), Kod lokalizacji → gniazdo w regale modelu (środek palety, wysokość, obrót).…, dict gniazda: x, y, z (dół palety), heading, rozmiar [w, d] (+ half 1/2) albo…, SlotLocator, parse_code(), Kod → (zone, rack_id, bay, col_idx, level) albo None. (+1 more)

### Community 120 - "parse_overrides"
Cohesion: 0.28
Nodes (6): map_kind(), parse_overrides(), „2010 = wydanie” (linia na proces) → ({proces: rodzaj}, [błędy])., Rodzaj procesu mag. → rodzaj ruchu. Kolejność: nadpisania → słownik wyjątków →…, KindMappingTests, SimpleTestCase

### Community 121 - "TWINEMA — założenia master daty i scenariuszy"
Cohesion: 0.17
Nodes (11): Cel i odbiorcy, Dodatkowe (runda 3, 9 pytań), Ludzie i czas, Materiał i nośniki, Przyjęcia, Scenariusz (niezależny od layoutu), Składowanie i kompletacja, TWINEMA — założenia master daty i scenariuszy (+3 more)

### Community 123 - "ml/services.py"
Cohesion: 0.31
Nodes (9): Przebiegi ML na imporcie zadań: dane z bliźniaka → czyste moduły…, run_forecast(), run_segmentation(), _user(), Dni z ruchem ≥ WORKDAY_SHARE mediany dni z jakimkolwiek ruchem (rosnąco)., working_days(), Prognoza wzrostu wolumenów z historii zadań EWM (plan 2026-10-02, etap 5) —…, [(poniedziałek tygodnia, suma)] — tylko pełne tygodnie (bez pierwszego i… (+1 more)

### Community 125 - "twinema_render.py"
Cohesion: 0.33
Nodes (8): apply_preset(), _key(), main(), TWINEMA → Blender: render ujęcia (preset kamery) ze sceny „twinema.scene”.…, FFmpeg H.264 w MP4 — Blender 5 przeniósł format wideo do `media_type`., Ustawia „Kamerę TWINEMA” i jej cel wg presetu na klatkach 1…frames., render(), _video_settings()

### Community 126 - "parse_bay_numbers"
Cohesion: 0.22
Nodes (7): parse_bay_numbers(), „10-47,50” → [10, …, 47, 50]. Pusty tekst → []. Błędny zapis → ValueError., Numery gniazd rzędu w kolejności fizycznej; pusta reguła = 1..n_bays; nadmiar…, row_bay_numbers(), Numeracja gniazd rzędu: zakresy „10-47,50”., validate_bay_numbers(), ParseTests

### Community 128 - "GeneratorTests"
Cohesion: 0.15
Nodes (6): Poziomy składowania z podłogą: góra najwyższej palety ≤ wysokość − tryskacze., vna_levels(), GeneratorTests, SimpleTestCase, Generator hali od parametrów (plan 2026-10-02, etap 1): pojemność, geometria,…, _rect()

### Community 133 - "blender_stock.py"
Cohesion: 0.15
Nodes (11): abc_by_hits(), build_pallets(), _half(), Rzeczywiste palety w lokalizacjach → scena Blendera („cyfrowe zdjęcie"…, 1/2 dla połówki miejsca (kod z końcówką -1/-2, np. B0-07-300C-1), inaczej 0.…, Klasa ABC wg udziału w pobraniach (ta sama reguła progów co…, Czysta funkcja: dane wejściowe jako proste krotki/dicty → (pallets, stats,…, BuildPalletsTests (+3 more)

### Community 134 - "layout-preview.js"
Cohesion: 0.33
Nodes (9): S, CFG, createViewer(), initPreview(), MODES, preview3d(), setMode(), stage (+1 more)

### Community 135 - "test_play.py"
Cohesion: 0.22
Nodes (3): PlayViewTests, TestCase, Animacja dnia (S4): miejsca z layoutu, wąskie gardła → miejsca i okna czasu,…

### Community 138 - "test_ml.py"
Cohesion: 0.33
Nodes (4): Meta, ModelRun, Przebiegi modeli ML: wersja algorytmu, dane wejściowe, parametry, miary i wynik…, ML1 prognoza + ML2 segmentacja: czyste moduły, zapis przebiegów, ekrany.

### Community 139 - ".handle"
Cohesion: 0.40
Nodes (4): Command, atomic, BaseCommand, _r()

### Community 141 - "test_container_inbound.py"
Cohesion: 0.22
Nodes (8): outward(), Kierunek „na zewnątrz hali” od elementu przy ścianie: normalna najbliższej…, ContainerInboundTests, _f(), _items(), SimpleTestCase, Przyjęcie kontenera w animacji (plan 2026-10-02, etap 2b): kontener przy doku →…, _scene()

### Community 148 - "StructureApiTests"
Cohesion: 0.23
Nodes (4): png(), override_settings, TestCase, StructureApiTests

### Community 149 - "ewm_tasks.py"
Cohesion: 0.18
Nodes (13): _delimiter(), _encoding(), is_cancelled(), iter_table(), kind_from_word(), norm_header(), _parse_dt(), _parse_time() (+5 more)

### Community 150 - "generate"
Cohesion: 0.42
Nodes (8): _docks(), _feature(), generate(), _pair_pitch(), _rack(), Generator hali od parametrów — nowy magazyn „od zera” (plan 2026-10-02, etap…, [korytarz][A|B][korytarz]… — y każdego rzędu; A patrzy na korytarz przed, B za., _row_pairs()

### Community 151 - "VariantEditViewTests"
Cohesion: 0.22
Nodes (3): TestCase, Kopia „przyszłego layoutu” niesie konstrukcję hali z E2b: wysokość, słupy,…, VariantEditViewTests

### Community 152 - "test_ewm_detect.py"
Cohesion: 0.23
Nodes (10): expand_model(), [(rząd, szablon, wyjątki), …] → (miejsca z kluczami zone/aisle, {kod: [„B0-07”,…, DetectHeightsTests, DetectIrregularBayTests, expand_proposal(), master_of(), SimpleTestCase, „Wykryj z EWM”: propozycja szablonów, numeracji i wyjątków z kodów; round-trip… (+2 more)

### Community 154 - "test_model_edit.py"
Cohesion: 0.17
Nodes (17): bbox(), apply_zone_edit(), _box(), collisions(), fit_floor(), Edycja wariantu hali blokami (plan 2026-10-02, etap 4) — czysty Python.…, {strefa: liczba rzędów, gniazd w rzędzie (maks.), poziomy (maks.)} dla…, Zmienia regały strefy w miejscu (dicty jak `model_racks`) i zwraca listę… (+9 more)

### Community 157 - "_save"
Cohesion: 0.31
Nodes (5): HallGeneratorForm, _initial(), _md_role, _save(), warehouse_model_generator()

### Community 158 - "views_play.py"
Cohesion: 0.13
Nodes (20): dock_role(), places_from_features(), Miejsca z layoutu hali dla symulacji: role doków i powierzchnia pól odkładczych…, features: dicty jak `twin.shared.hall_feature_dict` (kind, label, width, depth,…, staging_side(), PlacesTests, SimpleTestCase, bottleneck_focus() (+12 more)

### Community 159 - "report.py"
Cohesion: 0.29
Nodes (10): bottlenecks(), hhmm(), p95(), Wyniki przebiegu: oś czasu co 15 min, KPI dnia, agregacja wielu przebiegów…, Reguły wąskich gardeł. rerun(kind, *args) → kpi przebiegu reprezentatywnego ze…, Liczba przedziałów [s, e) aktywnych w chwili t = i·15 min., Surowy przebieg (`engine.simulate_plan`) → {kpi, timeline}., run_report() (+2 more)

### Community 160 - "0003_konstrukcja_hali.py"
Cohesion: 0.50
Nodes (3): Migration, Istniejące regały półkowe (poziom < 1 m, jak blender_scene.SHELF_LEVEL_M) →…, shelves()

### Community 162 - "build_plan"
Cohesion: 0.26
Nodes (8): build_plan(), count(), Plan dnia z założeń scenariusza (czysty Python): losowanie min/śr/max i rozkład…, n chwil w oknie [od, do): środki n odcinków ± rozrzut; posortowane., day: {inbound:[stream], outbound:[stream],…, times_in_window(), tri(), PlanTests

### Community 164 - "simulate_plan"
Cohesion: 0.22
Nodes (8): Docks, Fleet, plan: `plan.build_plan`; params: normy + flota; shifts: [{process, start_h,…, simulate_plan(), EngineTests, plan(), shifts(), truck()

### Community 166 - "VariantViewTests"
Cohesion: 0.24
Nodes (3): _el(), TestCase, VariantViewTests

### Community 167 - "load_groups"
Cohesion: 0.40
Nodes (4): groups_for(), {materiał: grupa towarowa} albo None, gdy materiałów jeszcze nie zaimportowano.…, load_groups(), {materiał z zadań: grupa towarowa} z modułu Dane; None, gdy materiałów jeszcze…

### Community 169 - "params_for"
Cohesion: 0.29
Nodes (5): block_rows(), params_for(), Rzędy bloku regałów: lista przesunięć „w głąb" [m] kolejnych rzędów.…, Parametry elementu: domyślne z katalogu + nadpisania (tylko znane klucze)., CatalogTests

### Community 170 - "design_calibration.py"
Cohesion: 0.21
Nodes (12): _feature_center(), Środek elementu hali (narożnik + obrót jak w three.js)., Wiersze WT (krotki ROW_FIELDS, rosnąco po potwierdzeniu) → (ruchy, pominięte).…, resolve_moves(), calibrate(), ideal_cycle(), _manh(), _point() (+4 more)

### Community 171 - "simulate"
Cohesion: 0.50
Nodes (3): simulate(), DemoSimTests, TestCase

### Community 172 - "WarehouseTask"
Cohesion: 0.14
Nodes (6): MlRunTests, TestCase, Meta, WarehouseTask, ForecastViewTests, TestCase

### Community 173 - "fullscreen.test.mjs"
Cohesion: 0.33
Nodes (3): bindFullscreenButton(), fullscreenController(), PSEUDO_CLASS

### Community 175 - "parse_row"
Cohesion: 0.46
Nodes (3): parse_row(), Wiersz → dict pól `WarehouseTask` (+ `cancelled`); None = pusty wiersz;…, RowTests

### Community 176 - "BuildSceneTests"
Cohesion: 0.19
Nodes (5): BuildSceneTests, SimpleTestCase, _rack(), RouteGeometryTests, _scene()

### Community 179 - "warehouse_model_copy"
Cohesion: 0.50
Nodes (4): _md_role, require_POST, Kopia modelu (hala ze słupami i podkładem, regały, elementy hali) — „przyszły…, warehouse_model_copy()

### Community 180 - "BlenderImportGuardTests"
Cohesion: 0.50
Nodes (3): BlenderImportGuardTests, SimpleTestCase, Blender importuje te moduły bez Django — żadnego importu Django na poziomie…

## Knowledge Gaps
- **85 isolated node(s):** `docker-entrypoint.sh script`, `Migration`, `Migration`, `Migration`, `Migration` (+80 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **40 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `WarehouseModel` connect `twin/models.py` to `shared.py`, `GeneratorTests`, `BayTemplate`, `test_play.py`, `masterdata/services.py`, `masterdata/views.py`, `test_dane.py`, `scenario/views.py`, `test_ewm_service.py`, `Scenario`, `studio/views.py`, `warehouse_model.py`, `test_model_edit.py`, `studio/models.py`, `views_sim.py`, `warehouse_blender.py`?**
  _High betweenness centrality (0.083) - this node is a cross-community bridge._
- **Why does `synthesize()` connect `VoiceViewTests` to `twinema_montage.py`, `studio/views.py`?**
  _High betweenness centrality (0.050) - this node is a cross-community bridge._
- **Why does `Api` connect `twinema_montage.py` to `VoiceViewTests`?**
  _High betweenness centrality (0.048) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `WarehouseModel` (e.g. with `Meta` and `WarehouseModelForm`) actually correct?**
  _`WarehouseModel` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Are the 8 inferred relationships involving `SlotLocator` (e.g. with `BuildPalletsTests` and `ParseCodeTests`) actually correct?**
  _`SlotLocator` has 8 INFERRED edges - model-reasoned connections that need verification._
- **Are the 9 inferred relationships involving `Scenario` (e.g. with `DayProfileForm` and `HourField`) actually correct?**
  _`Scenario` has 9 INFERRED edges - model-reasoned connections that need verification._
- **What connects `docker-entrypoint.sh script`, `Migration`, `Migration` to the rest of the system?**
  _85 weakly-connected nodes found - possible documentation gaps or missing edges._