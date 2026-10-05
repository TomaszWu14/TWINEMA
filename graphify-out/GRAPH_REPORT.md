# Graph Report - agent-a33895230b4b2dd95  (2026-10-05)

## Corpus Check
- 289 files · ~187,443 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 3269 nodes · 6984 edges · 212 communities (165 shown, 47 thin omitted)
- Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 214 edges (avg confidence: 0.54)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `56941d2e`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- places.py
- day_demand
- equipment/models.py
- build_scene
- twinema_warehouse_anim.py
- test_foundation.py
- warehouse_tasks.py
- simulate
- twin/models.py
- showcase.py
- site.py
- blender_scene.py
- Material
- analyze
- twinema_design_kit.py
- test_ewm_service.py
- ml/services.py
- SimSceneTests
- scene-builder.js
- importers.py
- scene-data.js
- test_voice.py
- check_site
- WorkerApiTests
- twinema_montage.py
- StudioViewTests
- test_design_forecast.py
- flow-player.js
- TasksEndpointAndImportTests
- test_warehouse_model_view.py
- Agent
- design_day.py
- forecast.py
- layout-panels.js
- kpi_facts
- TWINEMA — zakres i plan
- BayTemplate
- ParseTests
- addressing.py
- ewm_service.py
- _comparison
- ewm_levels.py
- draft_script
- scenario/views.py
- day-timeline.js
- BayTemplateViewTests
- test_equipment_agents.py
- middleware.py
- scenario/models.py
- test_design_calibration.py
- warehouse_blender.py
- layout-core.js
- studio/views.py
- CLAUDE.md — TWINEMA
- WarehouseModelPasteTests
- test_deck.py
- ADR-0001: Kopia kodu modelowania magazynu, nie przeniesienie
- RenderMontageTests
- layout-hall.js
- test_dane.py
- views_showcase.py
- VoiceViewTests
- scenario/services.py
- pre-push
- ForecastTests
- WarehouseHallFeatureTests
- LayoutApiTests
- layout-editor.js
- blender_stock.py
- EwmTasksPollingTests
- blender_route.py
- FlowSceneEndpointTests
- SiteApiTests
- ewm_demo_tasks.py
- packaging.py
- RackTypeWeightsTests
- WarehouseHallFeature
- CalibrationTests
- Pochodzenie kodu
- ScenarioViewTests
- studio/models.py
- load_inputs
- test_addressing.py
- equipment/views.py
- SimViewTests
- icon
- warehouse_model.py
- studio/api.py
- CoreConfig
- health
- MasterdataConfig
- MlConfig
- RenderConfig
- fetch_vendor.sh
- TwinConfig
- shared.py
- docker-entrypoint.sh
- masterdata/migrations/0001_initial.py
- ml/migrations/0001_initial.py
- render/migrations/0001_initial.py
- design_catalog.py
- design_kpi.py
- test_ewm_tasks_parser.py
- ShowcaseViewTests
- TWINEMA — założenia master daty i scenariuszy
- 0002_lektor.py
- test_placement.py
- 0002_pole_odkladcze.py
- twinema_render.py
- Equipment
- StudioConfig
- warehouse_compare.py
- studio/migrations/0001_initial.py
- report.py
- SlotLocator
- layout-preview.js
- ComputeTests
- Scan
- 0003_render_montaz.py
- warehouse_layout.py
- masterdata/services.py
- ScenarioConfig
- segmentation.py
- scenario/migrations/0001_initial.py
- 0004_kadry.py
- StructureApiTests
- VariantViewTests
- EwmViewsTests
- layout-site.js
- test_ewm_detect.py
- ewm_tasks.py
- rack_corners
- 0002_wydania_obsada.py
- generate
- bay_templates.py
- views_play.py
- build_plan
- 0003_konstrukcja_hali.py
- 0003_symulacja_dnia.py
- sim/__init__.py
- 0003_domyslne_nosniki_klasy.py
- site.test.mjs
- 0002_opakowania_nosniki.py
- GeneratorViewTests
- CatalogMathTests
- test_master_data.py
- scene-site.js
- 0005_dzialka.py
- params_for
- test_aisles.py
- showcase.js
- 0006_prezentacja_3d.py
- ViewerRoleMatrixTests
- masterdata/views.py
- staffing
- CatalogViewTests
- test_sim.py
- BlenderExportViewTests
- ShowcaseForm
- DockRoleTests
- overlap_depth
- LayoutEquipmentSaveTests
- 0006_sprzet_z_katalogu.py
- parse_stamp
- 0004_rola_doku_nosnosc.py
- _save
- EquipmentConfig
- 0002_klasy_systemowe.py
- 0004_stawki_domyslne.py
- equipment/migrations/0001_initial.py
- 0003_koszty.py
- 0004_flota_z_katalogu.py
- views_compare.py
- load_groups
- test_container_inbound.py
- WarehouseTask
- parse_overrides
- parse_row
- PlayViewTests
- FleetHoursAndQueriesTests
- context_processors.py
- Command
- layout.py
- MetaRefreshGuardTests
- FormatTests
- run_events
- 0005_dni_szczytowe.py

## God Nodes (most connected - your core abstractions)
1. `WarehouseModel` - 47 edges
2. `SlotLocator` - 33 edges
3. `Scenario` - 30 edges
4. `generate()` - 30 edges
5. `simulate()` - 29 edges
6. `LayoutError` - 29 edges
7. `analyze()` - 29 edges
8. `rack_corners()` - 27 edges
9. `clean_layout()` - 27 edges
10. `Equipment` - 25 edges

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

## Communities (212 total, 47 thin omitted)

### Community 0 - "places.py"
Cohesion: 0.23
Nodes (8): dock_role(), needed_roles(), places_from_features(), Miejsca z layoutu hali dla symulacji: role doków i powierzchnia pól odkładczych…, Role doków, których wymaga dzień scenariusza (format `ScenarioDay.sim_day`)., features: dicty jak `twin.shared.hall_feature_dict` (kind, label, dock_role,…, staging_side(), PlacesTests

### Community 1 - "day_demand"
Cohesion: 0.12
Nodes (20): arrivals_count(), day_demand(), _hhmm(), peak_concurrency(), _pick(), Plan przyjęć → zapotrzebowanie dnia (czysty Python — bez Django, testowalny bez…, Liczba przyjazdów po wzroście — zaokrąglenie w górę (auto albo jest, albo go…, n przyjazdów równomiernie w oknie [od, do): środki n równych odcinków. (+12 more)

### Community 2 - "equipment/models.py"
Cohesion: 0.24
Nodes (8): Katalog sprzętu (K1) — czysty Python, bez Django. • `KINDS` — typy sprzętu;…, Katalog sprzętu (K1): klasy systemowe (anonimowe, z migracji) i własne modele…, assign_classes(), pick_class(), Dobór klasy sprzętu do regałów (generator hali, dane demo) — ta sama reguła co…, Dicty regałów generatora (pola modelu) → ustawia `equipment_model` po kategorii…, Najmniejsza klasa systemowa danej kategorii regału (reach/vna), która sięga…, Katalog sprzętu (K1): czyste funkcje, klasy systemowe z migracji, dobór klasy…

### Community 3 - "build_scene"
Cohesion: 0.16
Nodes (9): build_scene(), _demo_picks(), Składa scenę. `picks` = [(nazwa_pickera, [(rack, bay_idx, level, sku), …]), …]…, BuildSceneTests, SimpleTestCase, _rack(), Eksport modelu magazynu do animacji przepływów w Blenderze (tools/blender/)., RouteGeometryTests (+1 more)

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
Nodes (27): Najmniejsze k ∈ 1..limit, dla którego `ok(fix(k))`; None, gdy nie pomaga., _smallest(), _Agent, _kpi(), Layout, _manh(), _p95(), _pick() (+19 more)

### Community 8 - "twin/models.py"
Cohesion: 0.05
Nodes (38): Dekorator: wymaga zalogowania + członkostwa w grupie (superuser zawsze…, role_required(), Macierz ról: rola Podgląd nie zmienia danych i nie widzi danych źródłowych…, ML1 prognoza + ML2 segmentacja: czyste moduły, zapis przebiegów, ekrany., Kolejka renderów: API workera (token, przejęcie, scena, wynik) i ekran zleceń., Wynik symulacji dnia scenariusza na modelu hali (S3a): KPI średnia/najgorszy,…, ScenarioRun, C1: koszty CAPEX/OPEX — czysta kalkulacja (ręczne przykłady), koszty wyniku… (+30 more)

### Community 9 - "showcase.py"
Cohesion: 0.15
Nodes (19): _cam(), clean_slides(), _fmt(), _hhmm(), kpi_cards(), ValueError, Prezentacja 3D (P1) — czysty Python (bez Django): walidacja slajdów, karty KPI,…, Podsumowanie z liczb (bez AI). f: positions, need, fill_pct, day („typowym” /… (+11 more)

### Community 10 - "site.py"
Cohesion: 0.08
Nodes (30): skipUnless, rack_axes(), (u_w, u_d) — jednostkowe osie szerokości i głębokości regału w układzie hali., guess_dock_role(), rack_geom(), Rola doku z etykiety (dla doków bez jawnej roli): „kontener” → kontenery,…, Regał edytora → dict sceny (jak `blender_scene.model_racks`) dla geometrii i…, _area_m2() (+22 more)

### Community 11 - "blender_scene.py"
Cohesion: 0.07
Nodes (46): heading_deg(), rack_point(), Kierunek jazdy w układzie hali [°] (0 = +x, 90 = +y)., Punkt hali: `along` [m] wzdłuż szerokości, `across` [m] wzdłuż głębokości…, _access(), _activity_picks(), _aisle_m(), _carry() (+38 more)

### Community 12 - "Material"
Cohesion: 0.13
Nodes (14): Carrier, ImportLog, Material, Meta, PalletClass, Dane podstawowe bliźniaka: materiały, stany w lokalizacjach i dziennik…, Jeden import pliku: rodzaj, wynik i próbka odrzuconych wierszy. Import stanów…, Pozycja stanu: materiał w lokalizacji (z jednego importu stanów). (+6 more)

### Community 13 - "analyze"
Cohesion: 0.11
Nodes (23): analyze(), check_layout(), Lista problemów: error blokuje zapis, warning tylko ostrzega., (kpi, issues) — KPI tym samym wzorem co warianty (`design_kpi.compute_kpi`), a…, CheckLayoutTests, CleanLayoutTests, codes(), LayoutEquipmentTests (+15 more)

### Community 14 - "twinema_design_kit.py"
Cohesion: 0.19
Nodes (21): add(), add_block(), _clear(), _coll(), elements(), export_variant(), load_variant(), _make() (+13 more)

### Community 15 - "test_ewm_service.py"
Cohesion: 0.12
Nodes (15): compliance(), Raport zgodności modelu z EWM: kody z planu (expand_model) vs kody z mastera,…, rows: [{"zone", "rack_id", "has_template"}]; locations/duplicates: wynik…, Master data for a single warehouse location., WarehouseLocationMaster, load_sample(), Syntetyczna próbka mastera lokalizacji (hala B0) dla testów „Wykryj z EWM” i…, [(kod, typ EWM)] — kod B0-<rząd>-<gniazdo><pozycja palety><litera poziomu>. (+7 more)

### Community 16 - "ml/services.py"
Cohesion: 0.11
Nodes (22): Meta, ModelRun, Przebiegi modeli ML: wersja algorytmu, dane wejściowe, parametry, miary i wynik…, Przebiegi ML na imporcie zadań: dane z bliźniaka → czyste moduły…, run_forecast(), run_segmentation(), _user(), detail() (+14 more)

### Community 17 - "SimSceneTests"
Cohesion: 0.11
Nodes (6): CorridorRouter, Trasa „jak w magazynie”: wzdłuż korytarza do przejazdu poprzecznego, nim do…, SimpleTestCase, TestCase, SimSceneTests, SimSceneViewTests

### Community 18 - "scene-builder.js"
Cohesion: 0.17
Nodes (22): asphaltTex(), cartonTex(), createViewer(), doorTex(), HATCH, hatchTex(), hex2rgb(), _lblCache (+14 more)

### Community 19 - "importers.py"
Cohesion: 0.18
Nodes (22): _bool(), _cell(), _code(), _date(), ImportFileError, map_columns(), norm(), _num() (+14 more)

### Community 20 - "scene-data.js"
Cohesion: 0.13
Nodes (23): DECOR_FILL, decorParts(), DEFAULT_CLEAR_H, EDGE_KINDS, effectiveQuality(), extents(), FAST_ABOVE, FLAT_KINDS (+15 more)

### Community 21 - "test_voice.py"
Cohesion: 0.11
Nodes (24): align(), AlignmentTests, CueTests, TestCase, Czysta logika lektora: hash cache, długość, słowa, plansze napisów, SRT., Sztuczne wyrównanie: każdy znak trwa per_char sekund., SrtTests, VoiceKeyTests (+16 more)

### Community 22 - "check_site"
Cohesion: 0.14
Nodes (18): check_site(), clean_site(), default_site(), entry_point(), _opt(), Środek wjazdu na granicy (inset > 0 — tyle metrów w głąb działki)., Problemy działki (format `twin.layout`): linie zabudowy, % zabudowy, wysokość,…, Działka wokół hali: place 35 + 10 m przy ścianach z dokami (W/E), droga i… (+10 more)

### Community 23 - "WorkerApiTests"
Cohesion: 0.15
Nodes (4): override_settings, TestCase, RenderScreenTests, WorkerApiTests

### Community 24 - "twinema_montage.py"
Cohesion: 0.06
Nodes (32): Api, find_blender(), main(), Worker renderów TWINEMA — uruchamiany na komputerze z Blenderem (np. z GPU).…, Montaż filmu: pobierz ujęcia i nagrania, wykonaj komendy z…, BLENDER_BIN / --blender → PATH → typowe katalogi instalacji (najnowsza wersja)., run_job(), run_montage() (+24 more)

### Community 25 - "StudioViewTests"
Cohesion: 0.23
Nodes (3): override_settings, TestCase, StudioViewTests

### Community 26 - "test_design_forecast.py"
Cohesion: 0.20
Nodes (12): backtest(), fit(), forecast(), series: [(dzień porządkowy, wartość)] → (nachylenie log/tydzień, wyraz wolny,…, MAPE [%] prognozy ostatnich `weeks` tygodni z modelu uczonego bez nich (None —…, Wzrost per strumień: roczne tempo P50/P90, mnożnik na `years` lat, MAPE testu…, _daily(), ForecastTests (+4 more)

### Community 27 - "flow-player.js"
Cohesion: 0.11
Nodes (10): createFlowPlayer(), _e, FLOW_LABELS, FLOW_Y, _p, _s, SIM_KEYS, SKU_PALETTE (+2 more)

### Community 28 - "TasksEndpointAndImportTests"
Cohesion: 0.15
Nodes (4): override_settings, TestCase, Duży plik → import w wątku w tle (bez blokowania żądania), partia kończy się…, TasksEndpointAndImportTests

### Community 29 - "test_warehouse_model_view.py"
Cohesion: 0.10
Nodes (11): InstancingGuardTests, TestCase, Regression: warehouse model 3D view used a non-existent `get_item` filter → 500., UX #5: widok 3D nie może cicho paść czarnym ekranem — spinner + guard WebGL +…, Regresja bezpieczeństwa: wolny tekst pól regału/elementu (zone/rack_id/label)…, Regresja: FLOOR_W/FLOOR_D w JS muszą mieć KROPKĘ dziesiętną, nie polski…, G1: prawdziwy stan HU z odtwarzacza przepływów chowa palety poglądowe (bez…, R1: stal regałów renderowana przez InstancedMesh (3 draw calle), nie per-mesh.… (+3 more)

### Community 30 - "Agent"
Cohesion: 0.09
Nodes (23): Agent, Item, _r(), Osie czasu agentów (wózki widłowe, ludzie) i ładunków (palety, kartony) dla…, Postój do chwili `t` (realny znacznik zadania); zajęty agent nie cofa się w…, Przejęcie ładunku: klatka „na miejscu" → po `handling` s ładunek jest na…, Odłożenie ładunku w `pos` na wysokości `z` (np. gniazdo regału albo dok)., Ładunek: paleta albo karton. `appear`/`vanish` sterują widocznością w Blenderze. (+15 more)

### Community 31 - "design_day.py"
Cohesion: 0.11
Nodes (18): _abc_xyz(), build_profile(), _groups(), _order_profile(), percentile(), Profil ruchów i dzień projektowy z zadań EWM (spec projektowania magazynu, krok…, daily: {data: {rodzaj: n, "orders": n}}; hourly: {(data, godzina): {rodzaj:…, Percentyl z interpolacją liniową (jak numpy/Excel PERCENTILE.INC); pusta lista… (+10 more)

### Community 32 - "forecast.py"
Cohesion: 0.16
Nodes (13): candidates(), _demo(), evaluate(), fit(), _grid(), mape(), ML1 — prognoza tygodniowych wolumenów: kilka modeli wygładzania wykładniczego…, Najlepsze parametry modelu na serii `y` → (params, fitted, prognoza h→v, sd… (+5 more)

### Community 33 - "layout-panels.js"
Cohesion: 0.17
Nodes (29): zoneColors(), addItems(), change(), deleteSelected(), duplicateSelected(), keyOf(), keysAt(), moveSelected() (+21 more)

### Community 34 - "kpi_facts"
Cohesion: 0.13
Nodes (15): estimate_seconds(), _get(), kpi_facts(), _num(), Scenariusz prezentacji (czysty Python — bez Django i bez sieci). • `kpi_facts`…, Liczba po polsku: spacja tysięcy, przecinek dziesiętny., Zdania z liczbami wariantu. Brak wartości → zdanie pominięte (nie zgadujemy)., Szkic bez AI — działa zawsze, także bez klucza API. Do edycji przez projektanta. (+7 more)

### Community 35 - "TWINEMA — zakres i plan"
Cohesion: 0.07
Nodes (24): Następny krok, Po stronie właściciela (zanim pierwszy prawdziwy film), Przekazanie — stan projektu i następny krok (F6), Stan, Zasady repo (skrót — pełne w `CLAUDE.md`), 1. Decyzje, 2.1 MVP, 2.2 Po MVP (wsad do burzy mózgów) (+16 more)

### Community 36 - "BayTemplate"
Cohesion: 0.16
Nodes (6): BayTemplate, Szablon gniazda (słupa regału): belka, palety na belce, poziomy od podłogi w…, BayTemplateTests, levels(), TestCase, RackRuleAndOverrideTests

### Community 37 - "ParseTests"
Cohesion: 0.12
Nodes (7): MapColumnsTests, ParseTests, SimpleTestCase, Parser plików modułu Dane — czysty Python (bez bazy)., Wzór pliku z ekranu Dane musi się importować bez ręcznych poprawek., ReadTableTests, _xlsx()

### Community 38 - "addressing.py"
Cohesion: 0.14
Nodes (21): _bay_locations(), format_bay_numbers(), letter_rank(), make_code(), parse_code(), Adresy miejsc paletowych modelu magazynu: szablon gniazda + reguła rzędu +…, Klucz sortowania liter poziomów: znane litery wg LETTER_ORDER, obce na końcu., Kod EWM → (strefa, przejście, gniazdo, pozycja, litera, połówka) albo None. (+13 more)

### Community 39 - "ewm_service.py"
Cohesion: 0.11
Nodes (29): active_master(), apply_proposal(), compliance_for_model(), detect_for_model(), master_rows(), plan_for_model(), atomic, Warstwa ORM nad czystymi modułami adresowania: master EWM, plan modelu, zapis… (+21 more)

### Community 40 - "_comparison"
Cohesion: 0.29
Nodes (7): _comparison(), _get(), _planner, Wariant jako twinema.design-variant — do dalszej edycji w Blenderze…, Wiersze tabeli: wartości per wariant + oznaczenie najlepszej + różnica do…, warehouse_variant_json(), warehouse_variants()

### Community 41 - "ewm_levels.py"
Cohesion: 0.17
Nodes (16): NamedTuple, code_slot(), is_hall_a(), letter_level(), letter_slot(), LetterSlot, level_height_keys(), Litera kodu lokalizacji EWM → fizyczne miejsce w stosie (JEDNO źródło prawdy).… (+8 more)

### Community 42 - "draft_script"
Cohesion: 0.13
Nodes (20): BaseModel, draft_script(), enabled(), Exception, Szkic scenariusza z Claude API. Do modelu trafiają WYŁĄCZNIE zdania z…, Błąd do pokazania użytkownikowi (bez szczegółów technicznych)., facts: lista zdań z liczbami → (shots, ostrzeżenia). Rzuca ScriptAIError., ScriptAIError (+12 more)

### Community 43 - "scenario/views.py"
Cohesion: 0.15
Nodes (25): _arrival_rows(), day_save(), _errors(), _fc(), _hours_rows(), _num(), outbound_save(), any_role (+17 more)

### Community 44 - "day-timeline.js"
Cohesion: 0.10
Nodes (44): createDayPlayer(), fleet(), NO_SHADOW, PARTS, along(), buildTracks(), countersAt(), crewAt() (+36 more)

### Community 45 - "BayTemplateViewTests"
Cohesion: 0.20
Nodes (4): BayTemplateViewTests, CoordsRuleColumnsTests, level_post(), TestCase

### Community 46 - "test_equipment_agents.py"
Cohesion: 0.21
Nodes (7): EquipmentAgentsTests, SimpleTestCase, _rack(), Sprzęt nowego magazynu w animacji (plan 2026-10-02, etap 2): AGV + kombi w…, Paleta przechodzi AGV → kombi w jednym miejscu: między klatkami nie skacze…, Czas klatek palety rośnie: kombi czeka (wait_until), zamiast „cofać" paletę w…, _scene()

### Community 47 - "middleware.py"
Cohesion: 0.13
Nodes (9): client_ip(), Middleware przekrojowe: identyfikator żądania (korelacja logów) + nagłówki…, Dopisuje `record.request_id` z bieżącego żądania ("-" poza żądaniem)., Bierze X-Request-ID od proxy albo nadaje nowy; odsyła go w odpowiedzi., Permissions-Policy + Content-Security-Policy (domyślnie report-only)., IP klienta dla django-axes za jednym zaufanym proxy (Traefik/Coolify): ostatni…, RequestIDLogFilter, RequestIDMiddleware (+1 more)

### Community 48 - "scenario/models.py"
Cohesion: 0.10
Nodes (24): Scenariusz referencyjny (syntetyczny, anonimowy): centrum dystrybucyjne z…, check_triples(), InboundStream, Meta, OutboundStream, Scenariusz: założenia wolumenów niezależne od layoutu (ten sam scenariusz…, Dzień typowy i szczytowy; nowe dostają domyślne strumienie i profil (szczyt:…, Auta wyjazdowe — jak przyjęcia. Koniec okna = cut-off (odjazd / odbiór kuriera). (+16 more)

### Community 49 - "test_design_calibration.py"
Cohesion: 0.13
Nodes (9): CalibrationViewTests, TestCase, Kalibracja symulacji na obecnej hali (plan 2026-10-02, etap 6)., SimpleTestCase, _racks(), Zadania EWM (WT) w animacji przepływów: ruchy wózków z realnych zadań (agenci z…, ResolveMovesTests, _row() (+1 more)

### Community 50 - "warehouse_blender.py"
Cohesion: 0.08
Nodes (38): build_scene_for_model(), model_racks(), Regały WarehouseModel jako dicty w formacie sceny (x, y, width, depth,…, Scena dla `WarehouseModel`. `batch` = PickerActivityBatch (None → demo…, load_stock_inputs(), Dane do `build_pallets`: (wiersze migawki, stany, aktywność). Stany = najnowszy…, default_start(), load_window() (+30 more)

### Community 51 - "layout-core.js"
Cohesion: 0.14
Nodes (17): axes(), BACK_GAP_M, bbox(), center(), corners(), History, makeBlock(), mode() (+9 more)

### Community 52 - "studio/views.py"
Cohesion: 0.13
Nodes (32): approve(), deck_pdf(), _draft_or_back(), film_file(), model_kpi(), montage_create(), montage_input_key(), montage_ready() (+24 more)

### Community 53 - "CLAUDE.md — TWINEMA"
Cohesion: 0.33
Nodes (5): CLAUDE.md — TWINEMA, Git, Graphify query-first, Testy (przed każdym PR), Zasady

### Community 55 - "test_deck.py"
Cohesion: 0.11
Nodes (15): FPDF, build_deck(), _Deck, Deck PDF prezentacji (czysty Python — fpdf2, bez Django i bez bazy). Strony…, „Etykieta: wartość.” → (etykieta, wartość) do kafla; zdanie bez dwukropka →…, slides: [{"label": "Przelot nad halą", "text": kwestia, "image": bytes PNG albo…, split_fact(), BuildDeckTests (+7 more)

### Community 56 - "ADR-0001: Kopia kodu modelowania magazynu, nie przeniesienie"
Cohesion: 0.40
Nodes (4): ADR-0001: Kopia kodu modelowania magazynu, nie przeniesienie, Decyzja, Kontekst, Skutki

### Community 57 - "RenderMontageTests"
Cohesion: 0.19
Nodes (3): override_settings, TestCase, RenderMontageTests

### Community 58 - "layout-hall.js"
Cohesion: 0.27
Nodes (14): drawHall(), drawItem(), el(), render(), status(), CFG, deleteSelectedColumn(), drawColumns() (+6 more)

### Community 59 - "test_dane.py"
Cohesion: 0.13
Nodes (10): demo_stock(), Pozycje stanu dla regałów modelu: ~`fill` miejsc zajętych, materiały wg rotacji…, _csv(), DaneViewTests, DemoAndSceneTests, DemoStockTests, ImportServiceTests, SimpleTestCase (+2 more)

### Community 60 - "views_showcase.py"
Cohesion: 0.23
Nodes (16): _context(), any_role, designer, require_POST, Prezentacje 3D (P1): lista, tworzenie (ze szablonem startowym), odtwarzacz +…, Dane odtwarzacza: scena (layout + działka), miejsca, wyniki (karty KPI, wąskie…, Wszystko, czego potrzebuje odtwarzacz i szablon startowy (jedno źródło)., showcase_create() (+8 more)

### Community 61 - "VoiceViewTests"
Cohesion: 0.10
Nodes (18): FakeResp, opener_err(), opener_ok(), override_settings, SimpleTestCase, Klient ElevenLabs — zawsze z podstawionym `opener` (bez sieci)., SynthesizeTests, fake_tts() (+10 more)

### Community 62 - "scenario/services.py"
Cohesion: 0.07
Nodes (30): move_minutes(), Ruch palety: dojazd pusty + jazda z ładunkiem (po `dist_m` w jedną stronę),…, [(kartonów/paletę, waga)] → średnia ważona (np. liczbą palet na stanie). None,…, weighted_cartons_per_pallet(), cartons_per_pallet_distribution(), cartons_per_pallet_hint(), {materiał: palet na aktualnym stanie} — pozycja stanu = jedna paleta (jak w…, [(kartonów/paletę, waga)] z master daty: waga = palet na stanie (albo 1 na… (+22 more)

### Community 64 - "ForecastTests"
Cohesion: 0.17
Nodes (3): ForecastTests, SimpleTestCase, SegmentationTests

### Community 65 - "WarehouseHallFeatureTests"
Cohesion: 0.23
Nodes (3): TestCase, rows: lista dictów pól równoległych → payload z listami., WarehouseHallFeatureTests

### Community 66 - "LayoutApiTests"
Cohesion: 0.15
Nodes (5): LayoutApiTests, LayoutEditorPageTests, TestCase, Ekran edytora (E2): tylko Projektant/Administratorzy, konfiguracja dla modułu…, E3: podgląd 3D obok planu — three.js z vendora (importmap, bez CDN),…

### Community 67 - "layout-editor.js"
Cohesion: 0.14
Nodes (25): all(), applyIssues(), CFG, check(), fit(), fullscreen, history, load() (+17 more)

### Community 68 - "blender_stock.py"
Cohesion: 0.17
Nodes (10): _deg(), _half(), Rzeczywiste palety w lokalizacjach → scena Blendera („cyfrowe zdjęcie"…, 1/2 dla połówki miejsca (kod z końcówką -1/-2, np. B0-07-300C-1), inaczej 0.…, dict gniazda: x, y, z (dół palety), heading, rozmiar [w, d] (+ half 1/2) albo…, Na ile części (w pionie) dzielony jest otwór poziomu danej półki; całe miejsce…, shelves_in_opening(), parse_code() (+2 more)

### Community 69 - "EwmTasksPollingTests"
Cohesion: 0.25
Nodes (3): EwmTasksPollingTests, TestCase, Import „w tle” ponad STALE_AFTER = proces padł — polling ma się zatrzymać.

### Community 70 - "blender_route.py"
Cohesion: 0.17
Nodes (9): _dedupe(), FloorGrid, Geometria i trasowanie dla eksportu animacji przepływów do Blendera. Czysty…, Najbliższa wolna komórka (BFS od komórki punktu) albo None, gdy hala zapchana., Trasa A* (8-sąsiedztwo, bez ścinania narożników regałów) z punktu a do b.…, Usuwa węzły leżące na prostej (zostają tylko zakręty)., Siatka zajętości posadzki: komórka zablokowana, jeśli leży w obrysie regału.…, _simplify() (+1 more)

### Community 71 - "FlowSceneEndpointTests"
Cohesion: 0.24
Nodes (3): FlowPlayerPanelTests, FlowSceneEndpointTests, TestCase

### Community 72 - "SiteApiTests"
Cohesion: 0.27
Nodes (3): GeneratorSiteTests, TestCase, SiteApiTests

### Community 73 - "ewm_demo_tasks.py"
Cohesion: 0.31
Nodes (9): bin_code(), day_tasks(), main(), Demonstracyjny eksport zadań magazynowych EWM (/SCWM/MON) do importu w TWINEMA.…, Zadania jednego dnia: [(rodzaj, materiał, dokument)] w kolejności do rozdania…, `n` chwil potwierdzeń jednego zasobu w zmianie: start + odstępy ~ mean_gap,…, row(), rows_for_day() (+1 more)

### Community 74 - "packaging.py"
Cohesion: 0.20
Nodes (16): cartons_per_pallet(), classify(), pallet_height_cm(), pallet_weight_kg(), Hierarchia opakowań sztuka → karton → paleta (czysty Python, bez Django).…, Kartonów/warstwę × warstw/paletę, gdy oba znane; inaczej wartość wpisana., Wpisana wysokość palety z towarem albo warstwy × wys. kartonu + wys. nośnika., Najmniejsza klasa z limitem ≥ wartość: classes = [(id, limit)]. Ponad… (+8 more)

### Community 75 - "RackTypeWeightsTests"
Cohesion: 0.20
Nodes (3): TestCase, RackTypeWeightsTests, Typy regałów A/B/C/D: nośność per poziom (level_weights) — zapis w edytorze,…

### Community 76 - "WarehouseHallFeature"
Cohesion: 0.17
Nodes (10): Command, demo_hall(), demo_zones(), atomic, BaseCommand, _r(), Hala z generatora z 3 dokami paletowymi IN (preset ma 1 — przy 16+ autach…, Strefy specjalne demo nad dwiema parami rzędów VNA: ADR (rzędy 1–2) i… (+2 more)

### Community 77 - "CalibrationTests"
Cohesion: 0.24
Nodes (5): CalibrationTests, SimpleTestCase, Wózek przewozi palety między dwoma gniazdami co `gap_s` sekund., Ten sam ruch co 2 min vs co 4 min → współczynnik rośnie dwukrotnie., _rows()

### Community 79 - "ScenarioViewTests"
Cohesion: 0.19
Nodes (3): hhmm(), TestCase, ScenarioViewTests

### Community 80 - "studio/models.py"
Cohesion: 0.08
Nodes (19): Meta, Zlecenia renderu: aplikacja kolejkuje, worker z Blenderem (poza serwerem)…, RenderJob, Meta, MontageJob, Presentation, Studio prezentacji: film o modelu hali składany z ujęć (preset kamery + kwestia…, Nagranie pasuje do obecnego tekstu i głosu (po poprawce kwestii — nieaktualne). (+11 more)

### Community 81 - "load_inputs"
Cohesion: 0.17
Nodes (6): load_inputs(), Agregaty zadań potwierdzonych partii (czas lokalny) — liczone w bazie, nie w…, LoadAndViewTests, TestCase, ewm_tasks_forecast(), _planner

### Community 82 - "test_addressing.py"
Cohesion: 0.14
Nodes (16): expand_row(), parse_bay_numbers(), Rząd + szablon domyślny + wyjątki → lista miejsc (dict). Klucze: code, bay,…, „10-47,50” → [10, …, 47, 50]. Pusty tekst → []. Błędny zapis → ValueError., Numery gniazd rzędu w kolejności fizycznej; pusta reguła = 1..n_bays; nadmiar…, row_bay_numbers(), Numeracja gniazd rzędu: zakresy „10-47,50”., validate_bay_numbers() (+8 more)

### Community 83 - "equipment/views.py"
Cohesion: 0.16
Nodes (16): capacity_at(), Udźwig [kg] na wysokości: nominalny do pierwszego punktu krzywej, potem…, _can_edit(), catalog_copy(), catalog_delete(), catalog_detail(), catalog_form(), catalog_list() (+8 more)

### Community 85 - "icon"
Cohesion: 0.40
Nodes (4): simple_tag, icon(), Tagi szablonów modułu: ikony Lucide ze sprite'a static/twin/icons/lucide.svg., {% icon "package" %} → dekoracyjna (aria-hidden); z label → role=img + aria-…

### Community 86 - "warehouse_model.py"
Cohesion: 0.12
Nodes (24): rack_class(), Jeden predykat rodzaju regału dla KPI, rozmieszczenia, symulacji, animacji i…, model_columns(), _parse_location_code(), Słupy hali jako elementy „column” (format hall_feature_dict + `height`) dla…, Zapis edytowalnej tabeli elementów hali z równoległych list POST + deleted_ids., B0-01-300A → (zone, rack, bay, level_letter, level_num)., save_hall_features() (+16 more)

### Community 87 - "studio/api.py"
Cohesion: 0.09
Nodes (36): claim(), _claimed_job(), fail(), _forbidden(), require_GET, require_POST, API workera renderów. Uwierzytelnienie: nagłówek X-Worker-Token…, Zlecenia „w toku” dłużej niż RENDER_STALE_MIN (worker padł) wracają do kolejki. (+28 more)

### Community 95 - "shared.py"
Cohesion: 0.08
Nodes (32): load_master_levels(), {kod: poziom} z aktywnego mastera lokalizacji (pusty dict, gdy brak)., Zadania magazynowe EWM (WT) — import z monitora magazynu (/SCWM/MON) do…, WarehouseTaskBatch, Wspólne importy i pomocnicze widoków bliźniaka — odpowiednik jądra widoków ze…, JSON bezpieczny do osadzenia w <script> przez |safe (escapuje <, >, & i…, safe_json(), DemoFileTests (+24 more)

### Community 117 - "design_catalog.py"
Cohesion: 0.12
Nodes (25): _geometry(), near_pairs(), Pary (i, j), i < j, których obrysy osiowe poszerzone o `pad` się stykają —…, block_rows(), check_aisles(), element_summary(), footprint(), _front_to() (+17 more)

### Community 118 - "design_kpi.py"
Cohesion: 0.10
Nodes (26): anchor_count(), anchors(), clean_elements(), compute_kpi(), equipment_capacity(), rack_to_element(), Wskaźniki wariantu projektu magazynu (czysty Python — testowalny bez bazy i…, Regał modelu magazynu (dict jak w scenie: width/depth/level_h/n_bays/n_levels,… (+18 more)

### Community 119 - "test_ewm_tasks_parser.py"
Cohesion: 0.30
Nodes (5): map_columns(), missing_required(), {pole: indeks kolumny}. Najpierw dokładne aliasy, potem nagłówek zaczynający…, HeaderAliasTests, Parser eksportu zadań magazynowych EWM (WT): aliasy nagłówków, liczby, daty,…

### Community 121 - "TWINEMA — założenia master daty i scenariuszy"
Cohesion: 0.15
Nodes (12): Cel i odbiorcy, Dodatkowe (runda 3, 9 pytań), Ludzie i czas, Materiał i nośniki, Przyjęcia, Runda 4 — grafika, działka, katalog sprzętu, Scenariusz (niezależny od layoutu), Składowanie i kompletacja (+4 more)

### Community 123 - "test_placement.py"
Cohesion: 0.07
Nodes (25): compare_columns(), Tabela porównania layout × scenariusz (E7) — czysty Python na zapisanych…, results: [ScenarioRun.result] w kolejności kolumn (pierwsza = punkt…, _center(), check_placement(), _inside(), _issue(), _poly() (+17 more)

### Community 125 - "twinema_render.py"
Cohesion: 0.33
Nodes (8): apply_preset(), _key(), main(), TWINEMA → Blender: render ujęcia (preset kamery) ze sceny „twinema.scene”.…, FFmpeg H.264 w MP4 — Blender 5 przeniósł format wideo do `media_type`., Ustawia „Kamerę TWINEMA” i jej cel wg presetu na klatkach 1…frames., render(), _video_settings()

### Community 126 - "Equipment"
Cohesion: 0.16
Nodes (9): CostRate, Equipment, Meta, (od, do) jako float; brak „do” = „od”; brak obu = None., Stawka kosztowa (C1) jako widełki min–max — wartości domyślne syntetyczne,…, _check_range(), EquipmentForm, Meta (+1 more)

### Community 128 - "warehouse_compare.py"
Cohesion: 0.08
Nodes (26): has_role(), True dla superusera albo członka którejś z grup., _is_shelf(), model_floor(), Hala co najmniej tak duża, jak obrys regałów (dane bywają „poza halą")., capacity(), comparison(), Porównanie wariantów hali na tym samym dniu projektowym (plan 2026-10-02, etap… (+18 more)

### Community 132 - "report.py"
Cohesion: 0.19
Nodes (14): aggregate(), bottlenecks(), hhmm(), p95(), Wyniki przebiegu: oś czasu co 15 min, KPI dnia, agregacja wielu przebiegów…, [kpi przebiegu] → {klucz: {mean, worst}}; najgorszy = P95 (gdy złe „dużo”) albo…, Reguły wąskich gardeł. rerun(kind, *args) → kpi przebiegu reprezentatywnego ze…, Liczba przedziałów [s, e) aktywnych w chwili t = i·15 min. (+6 more)

### Community 133 - "SlotLocator"
Cohesion: 0.14
Nodes (11): _inside(), Czy punkt leży w obrysie regału poszerzonym o `margin` [m]., build_pallets(), Czysta funkcja: dane wejściowe jako proste krotki/dicty → (pallets, stats,…, Kod lokalizacji → gniazdo w regale modelu (środek palety, wysokość, obrót).…, SlotLocator, BuildPalletsTests, ParseCodeTests (+3 more)

### Community 134 - "layout-preview.js"
Cohesion: 0.31
Nodes (10): S, CFG, createViewer(), initPreview(), MODES, preview3d(), setMode(), stage (+2 more)

### Community 135 - "ComputeTests"
Cohesion: 0.18
Nodes (9): compute(), _item(), mix_days(), Koszty wariantu (C1) — czysty Python: CAPEX layoutu i floty, OPEX roczny pracy…, Dni w roku: [(typ dnia, liczba dni)]. Brak symulacji jednego typu → cały rok z…, rates: {klucz: (od, do)} — `CostRate`; layout: {positions: {reach|vna|shelf:…, _total(), ComputeTests (+1 more)

### Community 136 - "Scan"
Cohesion: 0.23
Nodes (5): Przebieg po pliku: nagłówek → mapowanie kolumn → wiersze sparsowane albo błędy,…, Poprawne, nieanulowane zadania (dicty pól modelu)., [(etykieta pola, nagłówek z pliku)] w kolejności pól., Scan, ScanFileTests

### Community 138 - "warehouse_layout.py"
Cohesion: 0.15
Nodes (26): column_list(), feature_row(), [{x, y, size, ref}] — środki słupów. `ref` = [i, j] dla siatki, ["e", k] dla…, hall_feature_kinds(), _analyze(), equipment_catalog(), _image_size(), _layout() (+18 more)

### Community 139 - "masterdata/services.py"
Cohesion: 0.10
Nodes (24): missing_required(), parse_rows(), → (poprawne dicty, odrzucone [{row, reason}] — próbka), liczba odrzuconych.…, Command, BaseCommand, current_stock_log(), import_file(), _level_of() (+16 more)

### Community 141 - "segmentation.py"
Cohesion: 0.23
Nodes (12): _demo(), _dist2(), features(), kmeans(), _name(), ML2 — segmentacja materiałów pod rozmieszczenie (slotting): k-means na profilu…, {materiał: {hits, cv, active, volume?}} — tylko materiały z ruchem., k-means++ → (przypisania, centroidy, inercja). Deterministyczne dla danego… (+4 more)

### Community 148 - "StructureApiTests"
Cohesion: 0.23
Nodes (4): png(), override_settings, TestCase, StructureApiTests

### Community 149 - "VariantViewTests"
Cohesion: 0.24
Nodes (3): _el(), TestCase, VariantViewTests

### Community 150 - "EwmViewsTests"
Cohesion: 0.15
Nodes (3): EwmViewsTests, TestCase, Kody lokalizacji z mastera EWM to dane źródłowe — Podgląd ich nie widzi…

### Community 151 - "layout-site.js"
Cohesion: 0.20
Nodes (18): snap(), svgTransform(), setView(), viewCenter(), h(), num(), renderHall(), AREA_COLORS (+10 more)

### Community 152 - "test_ewm_detect.py"
Cohesion: 0.23
Nodes (10): expand_model(), [(rząd, szablon, wyjątki), …] → (miejsca z kluczami zone/aisle, {kod: [„B0-07”,…, DetectHeightsTests, DetectIrregularBayTests, expand_proposal(), master_of(), SimpleTestCase, „Wykryj z EWM”: propozycja szablonów, numeracji i wyjątków z kodów; round-trip… (+2 more)

### Community 153 - "ewm_tasks.py"
Cohesion: 0.23
Nodes (10): _delimiter(), _encoding(), is_cancelled(), iter_table(), kind_from_word(), norm_header(), Parser eksportu zadań magazynowych EWM (WT) z monitora magazynu (/SCWM/MON) →…, Wiersze pliku jako listy wartości — strumieniowo, bez ładowania całości do… (+2 more)

### Community 154 - "rack_corners"
Cohesion: 0.05
Nodes (41): bbox(), rack_corners(), _column_corners(), apply_zone_edit(), _box(), collisions(), fit_floor(), Edycja wariantu hali blokami (plan 2026-10-02, etap 4) — czysty Python.… (+33 more)

### Community 156 - "generate"
Cohesion: 0.13
Nodes (14): _docks(), _feature(), generate(), _pair_pitch(), _rack(), Generator hali od parametrów — nowy magazyn „od zera” (plan 2026-10-02, etap…, Poziomy składowania z podłogą: góra najwyższej palety ≤ wysokość − tryskacze., [korytarz][A|B][korytarz]… — y każdego rzędu; A patrzy na korytarz przed, B za. (+6 more)

### Community 157 - "bay_templates.py"
Cohesion: 0.25
Nodes (10): bay_template_delete(), bay_template_form(), bay_template_list(), _int(), _levels_from_post(), _md_role, _planner, require_POST (+2 more)

### Community 158 - "views_play.py"
Cohesion: 0.14
Nodes (16): PlacesTests, SimpleTestCase, bottleneck_focus(), layout_places(), peak_index(), any_role, Animacja dnia scenariusza (S4): scena 3D hali + zdarzenia przebiegu…, features: dicty `hall_feature_dict` (+ słupy), floor {width, depth} → miejsca… (+8 more)

### Community 159 - "build_plan"
Cohesion: 0.17
Nodes (10): build_plan(), count(), Plan dnia z założeń scenariusza (czysty Python): losowanie min/śr/max i rozkład…, n chwil w oknie [od, do): środki n odcinków ± rozrzut; posortowane., day: {inbound:[stream], outbound:[stream],…, times_in_window(), tri(), ManyRunsTests (+2 more)

### Community 160 - "0003_konstrukcja_hali.py"
Cohesion: 0.50
Nodes (3): Migration, Istniejące regały półkowe (poziom < 1 m, jak blender_scene.SHELF_LEVEL_M) →…, shelves()

### Community 162 - "sim/__init__.py"
Cohesion: 0.14
Nodes (16): Pool, Silnik zdarzeniowy dnia scenariusza (czysty Python, czas w godzinach od 0:00).…, Ludzie procesu: jeden „slot” na osobę na zmianę, dostępny [początek, koniec).…, Symulacja dnia scenariusza na layoucie hali (S3a) — czysty Python, bez Django.…, Zwroty przychodzą w godzinach zmian obsługi zwrotów (bez ostatniej godziny)., returns_window(), run_day(), run_many() (+8 more)

### Community 164 - "site.test.mjs"
Cohesion: 0.33
Nodes (5): ENTER_S, TRAVEL_S, sitePlan(), siteToHall(), SITE

### Community 168 - "test_master_data.py"
Cohesion: 0.09
Nodes (10): demo_materials(), material_codes(), Dane demonstracyjne (syntetyczne): materiały zgodne z `tools/ewm_demo_tasks.py`…, Wiersze materiałów (dicty pól Material) z losowymi, ale wiarygodnymi wymiarami:…, MasterDataViewTests, PackagingTests, PureTestCase, TestCase (+2 more)

### Community 169 - "scene-site.js"
Cohesion: 0.60
Nodes (4): buildSite(), flat(), GROUND, posts()

### Community 171 - "params_for"
Cohesion: 0.24
Nodes (6): params_for(), Parametry elementu: domyślne z katalogu + nadpisania (tylko znane klucze)., BlenderImportGuardTests, CatalogTests, SimpleTestCase, Blender importuje te moduły bez Django — żadnego importu Django na poziomie…

### Community 172 - "test_aisles.py"
Cohesion: 0.29
Nodes (6): AisleTests, block(), TestCase, rack(), R2: alejki dla par 0°/180° (blok „Dodaj blok” — plecami / frontami), najbliższy…, Jak makeBlock w layout-core.js: 0° | 180° (narożnik w x+w, y+d) | alejka | 0°.

### Community 173 - "showcase.js"
Cohesion: 0.16
Nodes (13): bindFullscreenButton(), fullscreenController(), PSEUDO_CLASS, camAt(), docksCam(), moveItem(), navigate(), pickCards() (+5 more)

### Community 175 - "ViewerRoleMatrixTests"
Cohesion: 0.22
Nodes (6): TestCase, Widoki odczytu przyjmują POST jak GET (renderują) — liczy się, że nic nie…, _routes(), _url(), ViewerRoleMatrixTests, ViewerSceneTests

### Community 176 - "masterdata/views.py"
Cohesion: 0.13
Nodes (17): Wzór pliku: nagłówki (pierwszy alias = polska nazwa) — do pobrania z ekranu…, template_csv(), catalog(), _counts(), demo(), home(), log_detail(), materials() (+9 more)

### Community 177 - "staffing"
Cohesion: 0.25
Nodes (4): → [{process, label, hours, shifts:[{…, needed, gap}], needed, assumed, short}]…, staffing(), TestCase, StaffingTests

### Community 178 - "CatalogViewTests"
Cohesion: 0.22
Nodes (3): CatalogViewTests, TestCase, SystemClassesTests

### Community 179 - "test_sim.py"
Cohesion: 0.28
Nodes (8): Docks, plan: `plan.build_plan`; params: normy + flota; shifts: [{process, start_h,…, simulate_plan(), EngineTests, plan(), Symulacja dnia (S3a) — czysty Python: plan, kolejki doków, pole odkładcze, cut-…, shifts(), truck()

### Community 181 - "ShowcaseForm"
Cohesion: 0.33
Nodes (4): Prezentacja 3D dla zarządu (P1): model hali (+ działka) i opcjonalnie wynik…, Showcase, Meta, ShowcaseForm

### Community 182 - "DockRoleTests"
Cohesion: 0.19
Nodes (3): DockRoleTests, TestCase, SimS3bTests

### Community 183 - "overlap_depth"
Cohesion: 0.33
Nodes (3): overlap_depth(), Głębokość nachodzenia dwóch obróconych prostokątów (narożniki w kolejności…, GeometryTests

### Community 185 - "0006_sprzet_z_katalogu.py"
Cohesion: 0.50
Nodes (3): assign(), Migration, Dotychczasowa kategoria regału (reach/vna) → najmniejsza klasa systemowa, która…

### Community 186 - "parse_stamp"
Cohesion: 0.26
Nodes (6): _parse_dt(), parse_stamp(), _parse_time(), → (datetime naiwny, czy_ma_czas) albo None; ValueError przy nieczytelnym…, Data (+ osobny czas, jak w eksporcie SAP) → datetime ze strefą `tz` albo None., ValueParsingTests

### Community 187 - "0004_rola_doku_nosnosc.py"
Cohesion: 0.50
Nodes (4): fill_roles(), _guess(), Migration, Kopia heurystyki z etykiety (z S3a) z chwili migracji — migracje mają być…

### Community 188 - "_save"
Cohesion: 0.31
Nodes (5): HallGeneratorForm, _initial(), _md_role, _save(), warehouse_model_generator()

### Community 197 - "views_compare.py"
Cohesion: 0.20
Nodes (17): _bytes(), compare_workbook(), Eksport wyników symulacji do xlsx (E8): założenia, KPI, wąskie gardła, obsada,…, run: ScenarioRun; day: ScenarioDay tego wyniku (do obsady z założeń)., columns: [nagłówek kolumny]; rows: `compare.compare_columns`., run_workbook(), _sheet(), Koszty wyniku symulacji (C1) — liczone przy wyświetleniu, więc zmiana stawek… (+9 more)

### Community 198 - "load_groups"
Cohesion: 0.40
Nodes (4): groups_for(), {materiał: grupa towarowa} albo None, gdy materiałów jeszcze nie zaimportowano.…, load_groups(), {materiał z zadań: grupa towarowa} z modułu Dane; None, gdy materiałów jeszcze…

### Community 199 - "test_container_inbound.py"
Cohesion: 0.29
Nodes (6): ContainerInboundTests, _f(), _items(), SimpleTestCase, Przyjęcie kontenera w animacji (plan 2026-10-02, etap 2b): kontener przy doku →…, _scene()

### Community 200 - "WarehouseTask"
Cohesion: 0.14
Nodes (6): MlRunTests, TestCase, Meta, WarehouseTask, ForecastViewTests, TestCase

### Community 201 - "parse_overrides"
Cohesion: 0.28
Nodes (6): map_kind(), parse_overrides(), „2010 = wydanie” (linia na proces) → ({proces: rodzaj}, [błędy])., Rodzaj procesu mag. → rodzaj ruchu. Kolejność: nadpisania → słownik wyjątków →…, KindMappingTests, SimpleTestCase

### Community 202 - "parse_row"
Cohesion: 0.29
Nodes (5): parse_number(), parse_row(), „1.234,5” / „1,234.5” / „1 234,5” / „5-” (minus SAP na końcu) / liczba → float;…, Wiersz → dict pól `WarehouseTask` (+ `cancelled`); None = pusty wiersz;…, RowTests

### Community 207 - "layout.py"
Cohesion: 0.15
Nodes (24): attach_equipment(), check_equipment(), clean_columns(), clean_layout(), clean_underlay(), _dock_role(), _fname(), height_kpi() (+16 more)

### Community 210 - "run_events"
Cohesion: 0.67
Nodes (3): any_role, Zdarzenia przebiegu reprezentatywnego dla odtwarzacza 3D (format:…, run_events()

## Knowledge Gaps
- **111 isolated node(s):** `docker-entrypoint.sh script`, `Migration`, `Migration`, `Migration`, `Migration` (+106 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **47 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `WarehouseModel` connect `twin/models.py` to `build_scene`, `masterdata/services.py`, `analyze`, `test_ewm_service.py`, `rack_corners`, `generate`, `test_warehouse_model_view.py`, `draft_script`, `scenario/views.py`, `masterdata/views.py`, `scenario/models.py`, `test_design_calibration.py`, `studio/views.py`, `test_deck.py`, `test_dane.py`, `views_showcase.py`, `scenario/services.py`, `studio/models.py`, `studio/api.py`, `shared.py`?**
  _High betweenness centrality (0.074) - this node is a cross-community bridge._
- **Why does `Agent` connect `Agent` to `build_scene`, `SimSceneTests`, `blender_scene.py`, `blender_route.py`?**
  _High betweenness centrality (0.021) - this node is a cross-community bridge._
- **Why does `LayoutApiTests` connect `LayoutApiTests` to `twin/models.py`?**
  _High betweenness centrality (0.020) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `WarehouseModel` (e.g. with `Meta` and `WarehouseModelForm`) actually correct?**
  _`WarehouseModel` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Are the 8 inferred relationships involving `SlotLocator` (e.g. with `BuildPalletsTests` and `ParseCodeTests`) actually correct?**
  _`SlotLocator` has 8 INFERRED edges - model-reasoned connections that need verification._
- **Are the 9 inferred relationships involving `Scenario` (e.g. with `DayProfileForm` and `HourField`) actually correct?**
  _`Scenario` has 9 INFERRED edges - model-reasoned connections that need verification._
- **What connects `docker-entrypoint.sh script`, `Migration`, `Migration` to the rest of the system?**
  _111 weakly-connected nodes found - possible documentation gaps or missing edges._