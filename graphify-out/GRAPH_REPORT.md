# Graph Report - agent-aaf0351c7af9732b8  (2026-10-05)

## Corpus Check
- 278 files · ~178,029 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 3136 nodes · 6661 edges · 197 communities (151 shown, 46 thin omitted)
- Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 205 edges (avg confidence: 0.54)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `b1f09d01`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- load_groups
- day_demand
- equipment/models.py
- views_compare.py
- twinema_warehouse_anim.py
- test_foundation.py
- warehouse_tasks.py
- simulate
- twin/models.py
- masterdata/services.py
- check_site
- blender_scene.py
- test_master_data.py
- analyze
- twinema_design_kit.py
- test_ewm_service.py
- ml/services.py
- test_design_sim_scene.py
- scene-builder.js
- importers.py
- scene-data.js
- test_voice.py
- blender_stock.py
- WorkerApiTests
- twinema_montage.py
- RenderJob
- test_design_forecast.py
- flow-player.js
- TasksEndpointAndImportTests
- ViewFloatLocalizationTests
- Agent
- design_day.py
- forecast.py
- layout-panels.js
- kpi_facts
- TWINEMA — zakres i plan
- BayTemplate
- ParseTests
- detect
- ewm_service.py
- scenario/services.py
- Fleet
- StudioViewTests
- scenario/views.py
- day-timeline.js
- BayTemplateViewTests
- EquipmentAgentsTests
- middleware.py
- Scenario
- resolve_moves
- warehouse_blender.py
- layout-core.js
- studio/views.py
- CLAUDE.md — TWINEMA
- WarehouseModelPasteTests
- build_deck
- ADR-0001: Kopia kodu modelowania magazynu, nie przeniesienie
- RenderMontageTests
- layout-editor.js
- DaneViewTests
- test_dane.py
- VoiceViewTests
- views_sim.py
- pre-push
- ForecastTests
- WarehouseHallFeatureTests
- LayoutApiTests
- layout-hall.js
- staffing
- EwmTasksPollingTests
- FloorGrid
- FlowSceneEndpointTests
- SiteApiTests
- ewm_demo_tasks.py
- packaging.py
- RackTypeWeightsTests
- BlenderExportViewTests
- calibrate
- Pochodzenie kodu
- ScenarioViewTests
- studio/models.py
- LoadAndViewTests
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
- addressing.py
- rack_corners
- TWINEMA — założenia master daty i scenariuszy
- 0002_lektor.py
- test_placement.py
- 0002_pole_odkladcze.py
- twinema_render.py
- Equipment
- StudioConfig
- test_design_compare.py
- studio/migrations/0001_initial.py
- WarehouseTask
- SlotLocator
- layout-preview.js
- test_costs.py
- bay_templates.py
- 0003_render_montaz.py
- warehouse_layout.py
- .slot
- ScenarioConfig
- segmentation.py
- scenario/migrations/0001_initial.py
- 0004_kadry.py
- StructureApiTests
- VariantViewTests
- CostViewsTests
- layout-site.js
- test_ewm_detect.py
- Scan
- test_model_edit.py
- 0002_wydania_obsada.py
- generate
- VariantEditViewTests
- views_play.py
- CalibrationViewTests
- 0003_konstrukcja_hali.py
- 0003_symulacja_dnia.py
- test_sim.py
- 0003_domyslne_nosniki_klasy.py
- compare.py
- 0002_opakowania_nosniki.py
- GeneratorViewTests
- BuildSceneTests
- MasterDataViewTests
- scene-site.js
- 0005_dzialka.py
- params_for
- LayoutCoreJsTests
- fullscreen.test.mjs
- WarehouseLocationMasterBatch
- .as_dict
- masterdata/views.py
- layout.py
- GeometryUploadTests
- .handle
- CatalogViewTests
- context_processors.py
- test_s3b_views.py
- Command
- LayoutEquipmentSaveTests
- 0006_sprzet_z_katalogu.py
- blender_route.py
- 0004_rola_doku_nosnosc.py
- BlenderImportGuardTests
- EquipmentConfig
- 0002_klasy_systemowe.py
- 0004_stawki_domyslne.py
- equipment/migrations/0001_initial.py
- 0003_koszty.py
- 0004_flota_z_katalogu.py

## God Nodes (most connected - your core abstractions)
1. `WarehouseModel` - 43 edges
2. `SlotLocator` - 33 edges
3. `generate()` - 30 edges
4. `simulate()` - 29 edges
5. `LayoutError` - 29 edges
6. `analyze()` - 29 edges
7. `Scenario` - 28 edges
8. `rack_corners()` - 26 edges
9. `clean_layout()` - 26 edges
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

## Communities (197 total, 46 thin omitted)

### Community 0 - "load_groups"
Cohesion: 0.29
Nodes (6): groups_for(), {materiał: grupa towarowa} albo None, gdy materiałów jeszcze nie zaimportowano.…, load_groups(), {materiał z zadań: grupa towarowa} z modułu Dane; None, gdy materiałów jeszcze…, ewm_tasks_profile(), _planner

### Community 1 - "day_demand"
Cohesion: 0.12
Nodes (19): arrivals_count(), day_demand(), peak_concurrency(), _pick(), Plan przyjęć → zapotrzebowanie dnia (czysty Python — bez Django, testowalny bez…, Liczba przyjazdów po wzroście — zaokrąglenie w górę (auto albo jest, albo go…, n przyjazdów równomiernie w oknie [od, do): środki n równych odcinków., Maks. liczba jednoczesnych przedziałów [start, koniec) i moment szczytu. (+11 more)

### Community 2 - "equipment/models.py"
Cohesion: 0.13
Nodes (14): move_minutes(), Katalog sprzętu (K1) — czysty Python, bez Django. • `KINDS` — typy sprzętu;…, Ruch palety: dojazd pusty + jazda z ładunkiem (po `dist_m` w jedną stronę),…, Katalog sprzętu (K1): klasy systemowe (anonimowe, z migracji) i własne modele…, assign_classes(), pick_class(), Dobór klasy sprzętu do regałów (generator hali, dane demo) — ta sama reguła co…, Dicty regałów generatora (pola modelu) → ustawia `equipment_model` po kategorii… (+6 more)

### Community 3 - "views_compare.py"
Cohesion: 0.19
Nodes (17): compare_columns(), results: [ScenarioRun.result] w kolejności kolumn (pierwsza = punkt…, _bytes(), compare_workbook(), Eksport wyników symulacji do xlsx (E8): założenia, KPI, wąskie gardła, obsada,…, run: ScenarioRun; day: ScenarioDay tego wyniku (do obsady z założeń)., columns: [nagłówek kolumny]; rows: `compare.compare_columns`., run_workbook() (+9 more)

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
Cohesion: 0.10
Nodes (24): Najmniejsze k ∈ 1..limit, dla którego `ok(fix(k))`; None, gdy nie pomaga., _smallest(), _Agent, _kpi(), Layout, _manh(), _p95(), _pick() (+16 more)

### Community 8 - "twin/models.py"
Cohesion: 0.06
Nodes (30): Dekorator: wymaga zalogowania + członkostwa w grupie (superuser zawsze…, role_required(), ML1 prognoza + ML2 segmentacja: czyste moduły, zapis przebiegów, ekrany., Kolejka renderów: API workera (token, przejęcie, scena, wynik) i ekran zleceń., demo_hall(), Hala z generatora z 3 dokami paletowymi IN (preset ma 1 — przy 16+ autach…, Ekrany studia: role, szkic z szablonu, edycja tylko w szkicu, akceptacja, szkic…, Migration (+22 more)

### Community 9 - "masterdata/services.py"
Cohesion: 0.10
Nodes (24): missing_required(), parse_rows(), → (poprawne dicty, odrzucone [{row, reason}] — próbka), liczba odrzuconych.…, Command, BaseCommand, current_stock_log(), import_file(), _level_of() (+16 more)

### Community 10 - "check_site"
Cohesion: 0.08
Nodes (34): rack_axes(), (u_w, u_d) — jednostkowe osie szerokości i głębokości regału w układzie hali., _area_m2(), building_height(), building_rect(), check_site(), default_site(), _dock_issues() (+26 more)

### Community 11 - "blender_scene.py"
Cohesion: 0.07
Nodes (51): Item, Osie czasu agentów (wózki widłowe, ludzie) i ładunków (palety, kartony) dla…, Ładunek: paleta albo karton. `appear`/`vanish` sterują widocznością w Blenderze., _at(), container_inbound(), Przyjęcie kontenera z kartonami luzem (plan 2026-10-02, etap 2b) — czysty…, docks: [(środek doku kontenerowego)], stations: [(środek stanowiska…, heading_deg() (+43 more)

### Community 12 - "test_master_data.py"
Cohesion: 0.14
Nodes (13): Carrier, ImportLog, Material, Meta, PalletClass, Dane podstawowe bliźniaka: materiały, stany w lokalizacjach i dziennik…, Jeden import pliku: rodzaj, wynik i próbka odrzuconych wierszy. Import stanów…, Nośnik (paleta): EUR 120×80 domyślnie, reszta edytowalna. (+5 more)

### Community 13 - "analyze"
Cohesion: 0.09
Nodes (29): analyze(), check_equipment(), check_layout(), _column_corners(), _fname(), _issue(), _name(), rack_geom() (+21 more)

### Community 14 - "twinema_design_kit.py"
Cohesion: 0.19
Nodes (21): add(), add_block(), _clear(), _coll(), elements(), export_variant(), load_variant(), _make() (+13 more)

### Community 15 - "test_ewm_service.py"
Cohesion: 0.09
Nodes (14): LocationOverride, Wyjątek adresu: nadpisuje wynik szablonu dla jednego miejsca albo całego…, Master data for a single warehouse location., WarehouseLocationMaster, load_sample(), Syntetyczna próbka mastera lokalizacji (hala B0) dla testów „Wykryj z EWM” i…, [(kod, typ EWM)] — kod B0-<rząd>-<gniazdo><pozycja palety><litera poziomu>., make_model_and_master() (+6 more)

### Community 16 - "ml/services.py"
Cohesion: 0.12
Nodes (21): Meta, ModelRun, Przebiegi modeli ML: wersja algorytmu, dane wejściowe, parametry, miary i wynik…, Przebiegi ML na imporcie zadań: dane z bliźniaka → czyste moduły…, run_forecast(), run_segmentation(), _user(), detail() (+13 more)

### Community 17 - "test_design_sim_scene.py"
Cohesion: 0.08
Nodes (17): build_sim_scene(), CorridorRouter, _pick_time(), Animacja godziny z symulacji dnia (plan 2026-10-02, etap 3b) — czysty Python.…, Trasa „jak w magazynie”: wzdłuż korytarza do przejazdu poprzecznego, nim do…, Chwila przejęcia ładunku: kombi rusza wcześniej niż AGV, ale paletę bierze po…, Przebiegi rozpoczęte w godzinie `hour` (zegar 5–21). Zwraca (przebiegi, ile…, window_legs() (+9 more)

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

### Community 22 - "blender_stock.py"
Cohesion: 0.11
Nodes (25): NamedTuple, Pozycje stanu jako dicty `build_pallets`: location, hu, sku, name, lot, expiry,…, stock_for_scene(), load_stock_inputs(), Rzeczywiste palety w lokalizacjach → scena Blendera („cyfrowe zdjęcie"…, Dane do `build_pallets`: (wiersze migawki, stany, aktywność). Stany = najnowszy…, code_slot(), is_hall_a() (+17 more)

### Community 23 - "WorkerApiTests"
Cohesion: 0.15
Nodes (4): override_settings, TestCase, RenderScreenTests, WorkerApiTests

### Community 24 - "twinema_montage.py"
Cohesion: 0.06
Nodes (32): Api, find_blender(), main(), Worker renderów TWINEMA — uruchamiany na komputerze z Blenderem (np. z GPU).…, Montaż filmu: pobierz ujęcia i nagrania, wykonaj komendy z…, BLENDER_BIN / --blender → PATH → typowe katalogi instalacji (najnowsza wersja)., run_job(), run_montage() (+24 more)

### Community 25 - "RenderJob"
Cohesion: 0.13
Nodes (14): Meta, RenderJob, create(), delete(), jobs(), Meta, any_role, designer (+6 more)

### Community 26 - "test_design_forecast.py"
Cohesion: 0.18
Nodes (15): backtest(), fit(), forecast(), Prognoza wzrostu wolumenów z historii zadań EWM (plan 2026-10-02, etap 5) —…, [(poniedziałek tygodnia, suma)] — tylko pełne tygodnie (bez pierwszego i…, series: [(dzień porządkowy, wartość)] → (nachylenie log/tydzień, wyraz wolny,…, MAPE [%] prognozy ostatnich `weeks` tygodni z modelu uczonego bez nich (None —…, Wzrost per strumień: roczne tempo P50/P90, mnożnik na `years` lat, MAPE testu… (+7 more)

### Community 27 - "flow-player.js"
Cohesion: 0.11
Nodes (10): createFlowPlayer(), _e, FLOW_LABELS, FLOW_Y, _p, _s, SIM_KEYS, SKU_PALETTE (+2 more)

### Community 28 - "TasksEndpointAndImportTests"
Cohesion: 0.15
Nodes (4): override_settings, TestCase, Duży plik → import w wątku w tle (bez blokowania żądania), partia kończy się…, TasksEndpointAndImportTests

### Community 29 - "ViewFloatLocalizationTests"
Cohesion: 0.10
Nodes (10): InstancingGuardTests, TestCase, UX #5: widok 3D nie może cicho paść czarnym ekranem — spinner + guard WebGL +…, Regresja bezpieczeństwa: wolny tekst pól regału/elementu (zone/rack_id/label)…, Regresja: FLOOR_W/FLOOR_D w JS muszą mieć KROPKĘ dziesiętną, nie polski…, G1: prawdziwy stan HU z odtwarzacza przepływów chowa palety poglądowe (bez…, R1: stal regałów renderowana przez InstancedMesh (3 draw calle), nie per-mesh.…, StoredXSSGuardTests (+2 more)

### Community 30 - "Agent"
Cohesion: 0.14
Nodes (9): Agent, _r(), Postój do chwili `t` (realny znacznik zadania); zajęty agent nie cofa się w…, Przejęcie ładunku: klatka „na miejscu" → po `handling` s ładunek jest na…, Odłożenie ładunku w `pos` na wysokości `z` (np. gniazdo regału albo dok)., Agent z osią czasu ruchu: rodzaj z `SPEED` (wózek, pracownik, kombi, AGV, EPT)., Jazda/przejście trasą A* do `target`; trasa trafia też do mapy przepływów., Najbliższy `new` ± 360° względem `prev` — bez obrotów o 350° między klatkami. (+1 more)

### Community 31 - "design_day.py"
Cohesion: 0.11
Nodes (20): _abc_xyz(), build_profile(), _groups(), _order_profile(), percentile(), Profil ruchów i dzień projektowy z zadań EWM (spec projektowania magazynu, krok…, daily: {data: {rodzaj: n, "orders": n}}; hourly: {(data, godzina): {rodzaj:…, Percentyl z interpolacją liniową (jak numpy/Excel PERCENTILE.INC); pusta lista… (+12 more)

### Community 32 - "forecast.py"
Cohesion: 0.16
Nodes (13): candidates(), _demo(), evaluate(), fit(), _grid(), mape(), ML1 — prognoza tygodniowych wolumenów: kilka modeli wygładzania wykładniczego…, Najlepsze parametry modelu na serii `y` → (params, fitted, prognoza h→v, sd… (+5 more)

### Community 33 - "layout-panels.js"
Cohesion: 0.17
Nodes (29): addItems(), change(), deleteSelected(), duplicateSelected(), keyOf(), keysAt(), moveSelected(), rotateSelected() (+21 more)

### Community 34 - "kpi_facts"
Cohesion: 0.13
Nodes (15): estimate_seconds(), _get(), kpi_facts(), _num(), Scenariusz prezentacji (czysty Python — bez Django i bez sieci). • `kpi_facts`…, Liczba po polsku: spacja tysięcy, przecinek dziesiętny., Zdania z liczbami wariantu. Brak wartości → zdanie pominięte (nie zgadujemy)., Szkic bez AI — działa zawsze, także bez klucza API. Do edycji przez projektanta. (+7 more)

### Community 35 - "TWINEMA — zakres i plan"
Cohesion: 0.08
Nodes (23): Następny krok: F6 — szlif (wg burzy mózgów, `docs/PLAN.md` §2.2 i §6), Po stronie właściciela (zanim pierwszy prawdziwy film), Przekazanie — stan projektu i następny krok (F6), Stan, Zasady repo (skrót — pełne w `CLAUDE.md`), 1. Decyzje, 2.1 MVP, 2.2 Po MVP (wsad do burzy mózgów) (+15 more)

### Community 36 - "BayTemplate"
Cohesion: 0.16
Nodes (7): BayTemplate, Szablon gniazda (słupa regału): belka, palety na belce, poziomy od podłogi w…, BayTemplateTests, levels(), TestCase, RackRuleAndOverrideTests, Modele części 1: szablon gniazda (walidacja), reguła rzędu, wyjątki…

### Community 37 - "ParseTests"
Cohesion: 0.12
Nodes (7): MapColumnsTests, ParseTests, SimpleTestCase, Parser plików modułu Dane — czysty Python (bez bazy)., Wzór pliku z ekranu Dane musi się importować bez ręcznych poprawek., ReadTableTests, _xlsx()

### Community 38 - "detect"
Cohesion: 0.21
Nodes (15): format_bay_numbers(), letter_rank(), Klucz sortowania liter poziomów: znane litery wg LETTER_ORDER, obce na końcu., [10, …, 47, 50] → „10-47,50” (odwrotność parse_bay_numbers)., detect(), _distance(), _grid(), _new_template() (+7 more)

### Community 39 - "ewm_service.py"
Cohesion: 0.10
Nodes (30): active_master(), apply_proposal(), compliance_for_model(), detect_for_model(), master_rows(), plan_for_model(), atomic, Warstwa ORM nad czystymi modułami adresowania: master EWM, plan modelu, zapis… (+22 more)

### Community 40 - "scenario/services.py"
Cohesion: 0.09
Nodes (36): [(kartonów/paletę, waga)] → średnia ważona (np. liczbą palet na stanie). None,…, weighted_cartons_per_pallet(), cartons_per_pallet_distribution(), cartons_per_pallet_hint(), [(kartonów/paletę, waga)] z master daty: waga = palet na stanie (albo 1 na…, Podpowiedź do normy scenariusza „kartonów na paletę”: średnia ważona liczbą…, fleet_from_catalog(), placement_bottlenecks() (+28 more)

### Community 41 - "Fleet"
Cohesion: 0.24
Nodes (4): Fleet, FleetCatalogTests, FleetChargingTests, TestCase

### Community 42 - "StudioViewTests"
Cohesion: 0.09
Nodes (22): BaseModel, draft_script(), enabled(), Exception, Szkic scenariusza z Claude API. Do modelu trafiają WYŁĄCZNIE zdania z…, Błąd do pokazania użytkownikowi (bez szczegółów technicznych)., facts: lista zdań z liczbami → (shots, ostrzeżenia). Rzuca ScriptAIError., ScriptAIError (+14 more)

### Community 43 - "scenario/views.py"
Cohesion: 0.15
Nodes (25): has_role(), True dla superusera albo członka którejś z grup., _arrival_rows(), day_save(), _errors(), _fc(), _hours_rows(), _num() (+17 more)

### Community 44 - "day-timeline.js"
Cohesion: 0.09
Nodes (49): createDayPlayer(), fleet(), NO_SHADOW, PARTS, along(), buildTracks(), countersAt(), crewAt() (+41 more)

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
Cohesion: 0.12
Nodes (25): demo_zones(), Scenariusz referencyjny (syntetyczny, anonimowy): centrum dystrybucyjne z…, Strefy specjalne demo nad dwiema parami rzędów VNA: ADR (rzędy 1–2) i…, check_triples(), InboundStream, Meta, OutboundStream, Scenariusz: założenia wolumenów niezależne od layoutu (ten sam scenariusz… (+17 more)

### Community 49 - "resolve_moves"
Cohesion: 0.29
Nodes (6): Wiersze WT (krotki ROW_FIELDS, rosnąco po potwierdzeniu) → (ruchy, pominięte).…, resolve_moves(), SimpleTestCase, ResolveMovesTests, _row(), SceneFromTasksTests

### Community 50 - "warehouse_blender.py"
Cohesion: 0.11
Nodes (26): _activity_picks(), build_scene_for_model(), Aktywność pickerów (picker, kod, materiał; kolejność = confirmed_at) → trasy.…, Scena dla `WarehouseModel`. `batch` = PickerActivityBatch (None → demo…, default_start(), load_window(), parse_start(), Wózki w animacji z realnych zadań magazynowych EWM (WT) zamiast symulacji demo.… (+18 more)

### Community 51 - "layout-core.js"
Cohesion: 0.14
Nodes (17): axes(), BACK_GAP_M, bbox(), center(), corners(), History, makeBlock(), mode() (+9 more)

### Community 52 - "studio/views.py"
Cohesion: 0.13
Nodes (30): approve(), deck_pdf(), _draft_or_back(), film_file(), montage_create(), montage_input_key(), montage_ready(), presentation_create() (+22 more)

### Community 53 - "CLAUDE.md — TWINEMA"
Cohesion: 0.33
Nodes (5): CLAUDE.md — TWINEMA, Git, Graphify query-first, Testy (przed każdym PR), Zasady

### Community 55 - "build_deck"
Cohesion: 0.11
Nodes (14): FPDF, build_deck(), _Deck, Deck PDF prezentacji (czysty Python — fpdf2, bez Django i bez bazy). Strony…, „Etykieta: wartość.” → (etykieta, wartość) do kafla; zdanie bez dwukropka →…, slides: [{"label": "Przelot nad halą", "text": kwestia, "image": bytes PNG albo…, split_fact(), BuildDeckTests (+6 more)

### Community 56 - "ADR-0001: Kopia kodu modelowania magazynu, nie przeniesienie"
Cohesion: 0.40
Nodes (4): ADR-0001: Kopia kodu modelowania magazynu, nie przeniesienie, Decyzja, Kontekst, Skutki

### Community 57 - "RenderMontageTests"
Cohesion: 0.19
Nodes (3): override_settings, TestCase, RenderMontageTests

### Community 58 - "layout-editor.js"
Cohesion: 0.16
Nodes (17): all(), CFG, fit(), fullscreen, history, redo(), restore(), scheduleCheck() (+9 more)

### Community 59 - "DaneViewTests"
Cohesion: 0.18
Nodes (5): _csv(), DaneViewTests, DemoAndSceneTests, ImportServiceTests, TestCase

### Community 60 - "test_dane.py"
Cohesion: 0.13
Nodes (11): PureTestCase, demo_materials(), demo_stock(), material_codes(), Dane demonstracyjne (syntetyczne): materiały zgodne z `tools/ewm_demo_tasks.py`…, Wiersze materiałów (dicty pól Material) z losowymi, ale wiarygodnymi wymiarami:…, Pozycje stanu dla regałów modelu: ~`fill` miejsc zajętych, materiały wg rotacji…, DemoStockTests (+3 more)

### Community 61 - "VoiceViewTests"
Cohesion: 0.10
Nodes (18): FakeResp, opener_err(), opener_ok(), override_settings, SimpleTestCase, Klient ElevenLabs — zawsze z podstawionym `opener` (bez sieci)., SynthesizeTests, fake_tts() (+10 more)

### Community 62 - "views_sim.py"
Cohesion: 0.12
Nodes (13): Wynik symulacji dnia scenariusza na modelu hali (S3a): KPI średnia/najgorszy,…, ScenarioRun, Flota scenariusza z katalogu sprzętu (K1): czas ruchu palety z parametrów,…, _cell(), any_role, designer, require_POST, Symulacja dnia scenariusza na modelu hali (S3a): uruchomienie, karta KPI,… (+5 more)

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
Cohesion: 0.19
Nodes (22): applyIssues(), check(), drawHall(), drawItem(), el(), load(), payload(), post() (+14 more)

### Community 68 - "staffing"
Cohesion: 0.25
Nodes (4): → [{process, label, hours, shifts:[{…, needed, gap}], needed, assumed, short}]…, staffing(), TestCase, StaffingTests

### Community 69 - "EwmTasksPollingTests"
Cohesion: 0.25
Nodes (3): EwmTasksPollingTests, TestCase, Import „w tle” ponad STALE_AFTER = proces padł — polling ma się zatrzymać.

### Community 70 - "FloorGrid"
Cohesion: 0.18
Nodes (7): FloorGrid, Najbliższa wolna komórka (BFS od komórki punktu) albo None, gdy hala zapchana., Trasa A* (8-sąsiedztwo, bez ścinania narożników regałów) z punktu a do b.…, Siatka zajętości posadzki: komórka zablokowana, jeśli leży w obrysie regału.…, SimpleTestCase, _rack(), RouteGeometryTests

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
Cohesion: 0.18
Nodes (18): cartons_per_pallet(), classify(), pallet_height_cm(), pallet_weight_kg(), Hierarchia opakowań sztuka → karton → paleta (czysty Python, bez Django).…, Kartonów/warstwę × warstw/paletę, gdy oba znane; inaczej wartość wpisana., Wpisana wysokość palety z towarem albo warstwy × wys. kartonu + wys. nośnika., Najmniejsza klasa z limitem ≥ wartość: classes = [(id, limit)]. Ponad… (+10 more)

### Community 75 - "RackTypeWeightsTests"
Cohesion: 0.20
Nodes (3): TestCase, RackTypeWeightsTests, Typy regałów A/B/C/D: nośność per poziom (level_weights) — zapis w edytorze,…

### Community 77 - "calibrate"
Cohesion: 0.21
Nodes (9): calibrate(), ideal_cycle(), Czas cyklu wg fizyki symulacji: dojazd prev → src, chwyt, przewóz src → dst,…, rows: krotki `blender_tasks.ROW_FIELDS` jednego dnia (rosnąco po potwierdzeniu)., CalibrationTests, SimpleTestCase, Wózek przewozi palety między dwoma gniazdami co `gap_s` sekund., Ten sam ruch co 2 min vs co 4 min → współczynnik rośnie dwukrotnie. (+1 more)

### Community 79 - "ScenarioViewTests"
Cohesion: 0.19
Nodes (3): hhmm(), TestCase, ScenarioViewTests

### Community 80 - "studio/models.py"
Cohesion: 0.09
Nodes (18): Zlecenia renderu: aplikacja kolejkuje, worker z Blenderem (poza serwerem)…, Meta, MontageJob, Presentation, Studio prezentacji: film o modelu hali składany z ujęć (preset kamery + kwestia…, Nagranie pasuje do obecnego tekstu i głosu (po poprawce kwestii — nieaktualne)., Długość klipu: nagranie + zapas 0,5 s, w granicach kolejki renderów (2–60 s)., Render pasuje do obecnego presetu i długości kwestii (stan zlecenia osobno). (+10 more)

### Community 82 - "test_addressing.py"
Cohesion: 0.17
Nodes (12): expand_row(), Rząd + szablon domyślny + wyjątki → lista miejsc (dict). Klucze: code, bay,…, Numery gniazd rzędu w kolejności fizycznej; pusta reguła = 1..n_bays; nadmiar…, row_bay_numbers(), codes(), ExpandModelTests, ExpandRowTests, ov() (+4 more)

### Community 83 - "equipment/views.py"
Cohesion: 0.15
Nodes (16): capacity_at(), Udźwig [kg] na wysokości: nominalny do pierwszego punktu krzywej, potem…, _can_edit(), catalog_copy(), catalog_delete(), catalog_detail(), catalog_form(), catalog_list() (+8 more)

### Community 84 - "SimViewTests"
Cohesion: 0.20
Nodes (4): DemoSimTests, TestCase, Symulacja dnia w aplikacji (S3a): uruchomienie, wynik na ekranie scenariusza,…, SimViewTests

### Community 85 - "icon"
Cohesion: 0.40
Nodes (4): simple_tag, icon(), Tagi szablonów modułu: ikony Lucide ze sprite'a static/twin/icons/lucide.svg., {% icon "package" %} → dekoracyjna (aria-hidden); z label → role=img + aria-…

### Community 86 - "warehouse_model.py"
Cohesion: 0.12
Nodes (23): parse_bay_numbers(), „10-47,50” → [10, …, 47, 50]. Pusty tekst → []. Błędny zapis → ValueError., Meta, WarehouseModelForm, Numeracja gniazd rzędu: zakresy „10-47,50”., validate_bay_numbers(), _parse_location_code(), Zapis edytowalnej tabeli elementów hali z równoległych list POST + deleted_ids. (+15 more)

### Community 87 - "studio/api.py"
Cohesion: 0.16
Nodes (24): claim(), _claimed_job(), fail(), _forbidden(), require_GET, require_POST, API workera renderów. Uwierzytelnienie: nagłówek X-Worker-Token…, Zlecenia „w toku” dłużej niż RENDER_STALE_MIN (worker padł) wracają do kolejki. (+16 more)

### Community 95 - "shared.py"
Cohesion: 0.07
Nodes (40): load_master_levels(), {kod: poziom} z aktywnego mastera lokalizacji (pusty dict, gdy brak)., load_day_tasks(), Zadania potwierdzone w dniu `day` (czas lokalny) jako sekundy od DAY_START_H., Zadania magazynowe EWM (WT) — import z monitora magazynu (/SCWM/MON) do…, WarehouseTaskBatch, hall_feature_dict(), model_columns() (+32 more)

### Community 117 - "design_catalog.py"
Cohesion: 0.17
Nodes (17): _geometry(), check_aisles(), element_summary(), footprint(), height(), pallet_positions(), Katalog elementów do projektowania wariantów magazynu — JEDNO źródło prawdy.…, Liczba miejsc paletowych elementu (0 dla transportu/kompletacji). (+9 more)

### Community 118 - "design_kpi.py"
Cohesion: 0.14
Nodes (18): anchor_count(), anchors(), _center(), clean_elements(), compute_kpi(), equipment_capacity(), Wskaźniki wariantu projektu magazynu (czysty Python — testowalny bez bazy i…, Walidacja elementów z pliku: znany rodzaj, liczby, parametry przez params_for.… (+10 more)

### Community 119 - "addressing.py"
Cohesion: 0.16
Nodes (11): _bay_locations(), make_code(), parse_code(), Adresy miejsc paletowych modelu magazynu: szablon gniazda + reguła rzędu +…, Kod EWM → (strefa, przejście, gniazdo, pozycja, litera, połówka) albo None., Miejsca jednego gniazda (numer `bay`, fizyczny indeks `slot`) wg szablonu i…, compliance(), Raport zgodności modelu z EWM: kody z planu (expand_model) vs kody z mastera,… (+3 more)

### Community 120 - "rack_corners"
Cohesion: 0.17
Nodes (14): rack_corners(), floor_size(), is_geometry_csv(), _num(), parse_geometry_csv(), Geometria regałów z pliku CSV (np. odczytana z rysunku hali) → regały modelu…, Plik geometrii poznajemy po nagłówku (plik kodów lokalizacji go nie ma)., Tekst CSV → (racks, errors). Wiersz z błędem trafia do `errors` (nr linii +… (+6 more)

### Community 121 - "TWINEMA — założenia master daty i scenariuszy"
Cohesion: 0.15
Nodes (12): Cel i odbiorcy, Dodatkowe (runda 3, 9 pytań), Ludzie i czas, Materiał i nośniki, Przyjęcia, Runda 4 — grafika, działka, katalog sprzętu, Scenariusz (niezależny od layoutu), Składowanie i kompletacja (+4 more)

### Community 123 - "test_placement.py"
Cohesion: 0.15
Nodes (20): _center(), check_placement(), _inside(), _issue(), _poly(), positions(), Pojemność layoutu vs potrzeba i reguły rozmieszczenia (S3b) — czysty Python,…, Miejsca paletowe regału (jak w KPI wariantów: palet w gnieździe ≈ szerokość /… (+12 more)

### Community 125 - "twinema_render.py"
Cohesion: 0.33
Nodes (8): apply_preset(), _key(), main(), TWINEMA → Blender: render ujęcia (preset kamery) ze sceny „twinema.scene”.…, FFmpeg H.264 w MP4 — Blender 5 przeniósł format wideo do `media_type`., Ustawia „Kamerę TWINEMA” i jej cel wg presetu na klatkach 1…frames., render(), _video_settings()

### Community 126 - "Equipment"
Cohesion: 0.16
Nodes (9): CostRate, Equipment, Meta, (od, do) jako float; brak „do” = „od”; brak obu = None., Stawka kosztowa (C1) jako widełki min–max — wartości domyślne syntetyczne,…, _check_range(), EquipmentForm, Meta (+1 more)

### Community 128 - "test_design_compare.py"
Cohesion: 0.17
Nodes (14): _is_shelf(), capacity(), comparison(), Porównanie wariantów hali na tym samym dniu projektowym (plan 2026-10-02, etap…, Miejsca paletowe (regały nie-półkowe), lokalizacje kartonowe (półki K1), bramy,…, Symulacja z flotą sugerowaną przez poprzedni przebieg, aż flota się ustali (≤…, [{wiersz KPI z wartościami per wariant + najlepszy}] dla tabeli., required_fleet() (+6 more)

### Community 132 - "WarehouseTask"
Cohesion: 0.14
Nodes (6): MlRunTests, TestCase, Meta, WarehouseTask, ForecastViewTests, TestCase

### Community 133 - "SlotLocator"
Cohesion: 0.14
Nodes (11): _inside(), Czy punkt leży w obrysie regału poszerzonym o `margin` [m]., build_pallets(), Czysta funkcja: dane wejściowe jako proste krotki/dicty → (pallets, stats,…, Kod lokalizacji → gniazdo w regale modelu (środek palety, wysokość, obrót).…, SlotLocator, BuildPalletsTests, ParseCodeTests (+3 more)

### Community 134 - "layout-preview.js"
Cohesion: 0.27
Nodes (11): zoneColors(), S, CFG, createViewer(), initPreview(), MODES, preview3d(), setMode() (+3 more)

### Community 135 - "test_costs.py"
Cohesion: 0.22
Nodes (8): compute(), _item(), Koszty wariantu (C1) — czysty Python: CAPEX layoutu i floty, OPEX roczny pracy…, rates: {klucz: (od, do)} — `CostRate`; layout: {positions: {reach|vna|shelf:…, _total(), ComputeTests, PlainTestCase, C1: koszty CAPEX/OPEX — czysta kalkulacja (ręczne przykłady), koszty wyniku…

### Community 136 - "bay_templates.py"
Cohesion: 0.19
Nodes (12): Named location type template — dimensions apply to all locations with matching…, WarehouseRackType, bay_template_delete(), bay_template_form(), bay_template_list(), _int(), _levels_from_post(), _md_role (+4 more)

### Community 138 - "warehouse_layout.py"
Cohesion: 0.12
Nodes (29): placement_for(), Pojemność vs potrzeba i reguły rozmieszczenia na aktualnym layoucie i stanie…, column_list(), feature_row(), rack_row(), [{x, y, size, ref}] — środki słupów. `ref` = [i, j] dla siatki, ["e", k] dla…, hall_feature_kinds(), _analyze() (+21 more)

### Community 139 - ".slot"
Cohesion: 0.24
Nodes (6): _deg(), _half(), 1/2 dla połówki miejsca (kod z końcówką -1/-2, np. B0-07-300C-1), inaczej 0.…, dict gniazda: x, y, z (dół palety), heading, rozmiar [w, d] (+ half 1/2) albo…, parse_code(), Kod → (zone, rack_id, bay, col_idx, level) albo None.

### Community 141 - "segmentation.py"
Cohesion: 0.23
Nodes (12): _demo(), _dist2(), features(), kmeans(), _name(), ML2 — segmentacja materiałów pod rozmieszczenie (slotting): k-means na profilu…, {materiał: {hits, cv, active, volume?}} — tylko materiały z ruchem., k-means++ → (przypisania, centroidy, inercja). Deterministyczne dla danego… (+4 more)

### Community 148 - "StructureApiTests"
Cohesion: 0.20
Nodes (5): png(), override_settings, TestCase, E2b — API edytora: zapis wysokości, słupów i sprzętu; podkład (upload,…, StructureApiTests

### Community 151 - "layout-site.js"
Cohesion: 0.20
Nodes (17): snap(), svgTransform(), setView(), viewCenter(), h(), num(), AREA_COLORS, AREA_SIZE (+9 more)

### Community 152 - "test_ewm_detect.py"
Cohesion: 0.23
Nodes (10): expand_model(), [(rząd, szablon, wyjątki), …] → (miejsca z kluczami zone/aisle, {kod: [„B0-07”,…, DetectHeightsTests, DetectIrregularBayTests, expand_proposal(), master_of(), SimpleTestCase, „Wykryj z EWM”: propozycja szablonów, numeracji i wyjątków z kodów; round-trip… (+2 more)

### Community 153 - "Scan"
Cohesion: 0.06
Nodes (37): _delimiter(), _encoding(), is_cancelled(), iter_table(), kind_from_word(), map_columns(), map_kind(), missing_required() (+29 more)

### Community 154 - "test_model_edit.py"
Cohesion: 0.13
Nodes (23): bbox(), overlap_depth(), Głębokość nachodzenia dwóch obróconych prostokątów (narożniki w kolejności…, apply_zone_edit(), _box(), collisions(), fit_floor(), Edycja wariantu hali blokami (plan 2026-10-02, etap 4) — czysty Python.… (+15 more)

### Community 156 - "generate"
Cohesion: 0.07
Nodes (23): _docks(), _feature(), generate(), _pair_pitch(), _rack(), Generator hali od parametrów — nowy magazyn „od zera” (plan 2026-10-02, etap…, Poziomy składowania z podłogą: góra najwyższej palety ≤ wysokość − tryskacze., [korytarz][A|B][korytarz]… — y każdego rzędu; A patrzy na korytarz przed, B za. (+15 more)

### Community 157 - "VariantEditViewTests"
Cohesion: 0.22
Nodes (3): TestCase, Kopia „przyszłego layoutu” niesie konstrukcję hali z E2b: wysokość, słupy,…, VariantEditViewTests

### Community 158 - "views_play.py"
Cohesion: 0.07
Nodes (27): staging_side(), PlacesTests, PlayViewTests, SimpleTestCase, TestCase, Animacja dnia (S4): miejsca z layoutu, wąskie gardła → miejsca i okna czasu,…, bottleneck_focus(), layout_places() (+19 more)

### Community 159 - "CalibrationViewTests"
Cohesion: 0.22
Nodes (3): CalibrationViewTests, TestCase, _racks()

### Community 160 - "0003_konstrukcja_hali.py"
Cohesion: 0.50
Nodes (3): Migration, Istniejące regały półkowe (poziom < 1 m, jak blender_scene.SHELF_LEVEL_M) →…, shelves()

### Community 162 - "test_sim.py"
Cohesion: 0.05
Nodes (55): Docks, Pool, Silnik zdarzeniowy dnia scenariusza (czysty Python, czas w godzinach od 0:00).…, plan: `plan.build_plan`; params: normy + flota; shifts: [{process, start_h,…, Ludzie procesu: jeden „slot” na osobę na zmianę, dostępny [początek, koniec).…, simulate_plan(), Symulacja dnia scenariusza na layoucie hali (S3a) — czysty Python, bez Django.…, Zwroty przychodzą w godzinach zmian obsługi zwrotów (bez ostatniej godziny). (+47 more)

### Community 168 - "MasterDataViewTests"
Cohesion: 0.17
Nodes (3): MasterDataViewTests, TestCase, SeedAndImportTests

### Community 169 - "scene-site.js"
Cohesion: 0.60
Nodes (4): buildSite(), flat(), GROUND, posts()

### Community 171 - "params_for"
Cohesion: 0.29
Nodes (5): block_rows(), params_for(), Rzędy bloku regałów: lista przesunięć „w głąb" [m] kolejnych rzędów.…, Parametry elementu: domyślne z katalogu + nadpisania (tylko znane klucze)., CatalogTests

### Community 172 - "LayoutCoreJsTests"
Cohesion: 0.38
Nodes (3): skipUnless, LayoutCoreJsTests, node_eval()

### Community 173 - "fullscreen.test.mjs"
Cohesion: 0.33
Nodes (3): bindFullscreenButton(), fullscreenController(), PSEUDO_CLASS

### Community 174 - "WarehouseLocationMasterBatch"
Cohesion: 0.29
Nodes (5): active_master_qs(), Kody lokalizacji magazynu — wspólna konwencja mapy 3D / eksportu SAP. Litera na…, Lokalizacje z aktywnej partii master-daty (pusty queryset, gdy brak partii).…, One import of location master data (height, volume, weight, type)., WarehouseLocationMasterBatch

### Community 176 - "masterdata/views.py"
Cohesion: 0.16
Nodes (15): Wzór pliku: nagłówki (pierwszy alias = polska nazwa) — do pobrania z ekranu…, template_csv(), catalog(), _counts(), demo(), home(), log_detail(), materials() (+7 more)

### Community 177 - "layout.py"
Cohesion: 0.14
Nodes (27): attach_equipment(), clean_columns(), clean_layout(), clean_underlay(), _dock_role(), guess_dock_role(), height_kpi(), _id() (+19 more)

### Community 179 - ".handle"
Cohesion: 0.40
Nodes (4): Command, atomic, BaseCommand, _r()

### Community 182 - "test_s3b_views.py"
Cohesion: 0.14
Nodes (6): Pozycja stanu: materiał w lokalizacji (z jednego importu stanów)., StockItem, DockRoleTests, TestCase, S3b w aplikacji: rola doku (pole, migracja, generator, edytor, symulacja),…, SimS3bTests

### Community 185 - "0006_sprzet_z_katalogu.py"
Cohesion: 0.50
Nodes (3): assign(), Migration, Dotychczasowa kategoria regału (reach/vna) → najmniejsza klasa systemowa, która…

### Community 186 - "blender_route.py"
Cohesion: 0.15
Nodes (8): _dedupe(), near_pairs(), Geometria i trasowanie dla eksportu animacji przepływów do Blendera. Czysty…, Usuwa węzły leżące na prostej (zostają tylko zakręty)., Pary (i, j), i < j, których obrysy osiowe poszerzone o `pad` się stykają —…, _simplify(), Czyste funkcje JS edytora layoutu (static/twin/js/layout-core.js): testy `node…, GeometryTests

### Community 187 - "0004_rola_doku_nosnosc.py"
Cohesion: 0.50
Nodes (4): fill_roles(), _guess(), Migration, Kopia heurystyki z etykiety (z S3a) z chwili migracji — migracje mają być…

### Community 188 - "BlenderImportGuardTests"
Cohesion: 0.50
Nodes (3): BlenderImportGuardTests, SimpleTestCase, Blender importuje te moduły bez Django — żadnego importu Django na poziomie…

## Knowledge Gaps
- **107 isolated node(s):** `docker-entrypoint.sh script`, `Migration`, `Migration`, `Migration`, `Migration` (+102 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **46 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `WarehouseModel` connect `twin/models.py` to `test_costs.py`, `masterdata/services.py`, `blender_scene.py`, `test_ewm_service.py`, `StructureApiTests`, `RenderJob`, `test_model_edit.py`, `generate`, `views_play.py`, `BayTemplate`, `scenario/views.py`, `masterdata/views.py`, `Scenario`, `studio/views.py`, `test_s3b_views.py`, `test_dane.py`, `views_sim.py`, `studio/models.py`, `SimViewTests`, `warehouse_model.py`, `shared.py`, `rack_corners`?**
  _High betweenness centrality (0.085) - this node is a cross-community bridge._
- **Why does `model_racks()` connect `scenario/services.py` to `test_design_compare.py`, `warehouse_tasks.py`, `masterdata/services.py`, `blender_scene.py`, `warehouse_blender.py`, `studio/views.py`, `test_model_edit.py`, `shared.py`?**
  _High betweenness centrality (0.025) - this node is a cross-community bridge._
- **Why does `ScenarioViewTests` connect `ScenarioViewTests` to `Scenario`?**
  _High betweenness centrality (0.021) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `WarehouseModel` (e.g. with `Meta` and `WarehouseModelForm`) actually correct?**
  _`WarehouseModel` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Are the 8 inferred relationships involving `SlotLocator` (e.g. with `BuildPalletsTests` and `ParseCodeTests`) actually correct?**
  _`SlotLocator` has 8 INFERRED edges - model-reasoned connections that need verification._
- **Are the 12 inferred relationships involving `LayoutError` (e.g. with `CheckLayoutTests` and `CleanLayoutTests`) actually correct?**
  _`LayoutError` has 12 INFERRED edges - model-reasoned connections that need verification._
- **What connects `docker-entrypoint.sh script`, `Migration`, `Migration` to the rest of the system?**
  _107 weakly-connected nodes found - possible documentation gaps or missing edges._