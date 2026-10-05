# Graph Report - .  (2026-10-05)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 1659 nodes · 3296 edges · 117 communities (98 shown, 19 thin omitted)
- Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 97 edges (avg confidence: 0.59)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `12a48c22`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Community 0
- Community 1
- Community 2
- Community 3
- Community 4
- Community 5
- Community 6
- Community 7
- Community 8
- Community 9
- Community 10
- Community 11
- Community 12
- Community 13
- Community 14
- Community 15
- Community 16
- Community 17
- Community 18
- Community 19
- Community 20
- Community 21
- Community 22
- Community 23
- Community 24
- Community 25
- Community 26
- Community 27
- Community 28
- Community 29
- Community 30
- Community 31
- Community 32
- Community 33
- Community 34
- Community 35
- Community 36
- Community 37
- Community 38
- Community 39
- Community 40
- Community 41
- Community 42
- Community 43
- Community 44
- Community 45
- Community 46
- Community 47
- Community 48
- Community 49
- Community 50
- Community 51
- Community 52
- Community 53
- Community 54
- Community 55
- Community 56
- Community 57
- Community 58
- Community 59
- Community 60
- Community 61
- Community 62
- Community 63
- Community 64
- Community 65
- Community 66
- Community 67
- Community 68
- Community 69
- Community 70
- Community 71
- Community 72
- Community 73
- Community 74
- Community 75
- Community 76
- Community 77
- Community 78
- Community 79
- Community 80
- Community 81
- Community 82
- Community 83
- Community 84
- Community 85
- Community 86
- Community 87
- Community 88
- Community 89
- Community 90
- Community 91
- Community 92
- Community 93
- Community 94
- Community 95
- Community 96
- Community 97
- Community 98
- Community 99

## God Nodes (most connected - your core abstractions)
1. `SlotLocator` - 33 edges
2. `simulate()` - 29 edges
3. `WarehouseModel` - 26 edges
4. `build_scene()` - 24 edges
5. `Scan` - 23 edges
6. `Agent` - 22 edges
7. `WarehouseTaskBatch` - 22 edges
8. `FloorGrid` - 20 edges
9. `params_for()` - 20 edges
10. `WarehouseModelRack` - 20 edges

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

## Communities (117 total, 19 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.05
Nodes (69): model_floor(), model_racks(), Regały WarehouseModel jako dicty w formacie sceny (x, y, width, depth,…, Hala co najmniej tak duża, jak obrys regałów (dane bywają „poza halą")., load_master_levels(), {kod: poziom} z aktywnego mastera lokalizacji (pusty dict, gdy brak)., default_start(), load_window() (+61 more)

### Community 1 - "Community 1"
Cohesion: 0.07
Nodes (37): rack_corners(), active_master(), Aktywny (najnowszy) import mastera lokalizacji albo None., floor_size(), is_geometry_csv(), _num(), parse_geometry_csv(), Geometria regałów z pliku CSV (np. odczytana z rysunku hali) → regały modelu… (+29 more)

### Community 2 - "Community 2"
Cohesion: 0.07
Nodes (34): require_GET, claim(), _claimed_job(), fail(), _forbidden(), require_POST, API workera renderów. Uwierzytelnienie: nagłówek X-Worker-Token…, Zlecenia „w toku” dłużej niż RENDER_STALE_MIN (worker padł) wracają do kolejki. (+26 more)

### Community 3 - "Community 3"
Cohesion: 0.08
Nodes (14): _dedupe(), FloorGrid, Trasa A* (8-sąsiedztwo, bez ścinania narożników regałów) z punktu a do b.…, Usuwa węzły leżące na prostej (zostają tylko zakręty)., Siatka zajętości posadzki: komórka zablokowana, jeśli leży w obrysie regału.…, Najbliższa wolna komórka (BFS od komórki punktu) albo None, gdy hala zapchana., _simplify(), BlenderExportViewTests (+6 more)

### Community 4 - "Community 4"
Cohesion: 0.14
Nodes (37): _animate_agent(), _animate_item(), _bl(), _box_mesh(), build(), _build_feature(), _build_floor(), _build_pallets() (+29 more)

### Community 5 - "Community 5"
Cohesion: 0.07
Nodes (17): BaseSettings, login_required, model_validator, AccessTests, ConfigTests, GroupContractTests, HealthTests, SimpleTestCase (+9 more)

### Community 6 - "Community 6"
Cohesion: 0.11
Nodes (31): never_cache, location_report(), purge_stale(), Import zadań magazynowych EWM do bazy: `ewm_tasks.Scan` (strumień) →…, Lokalizacje z zadań partii vs regały modelu: ile trafia w gniazda, ile jest…, Porzucone podglądy (nikt nie kliknął „Importuj”) — kasowane po dobie., Zapis uploadu na dysk kawałkami → token (nazwa pliku) do podglądu i importu., Ścieżka pliku po tokenie z formularza — tylko nasz format nazwy (bez path… (+23 more)

### Community 7 - "Community 7"
Cohesion: 0.12
Nodes (18): _Agent, _kpi(), _p95(), Symulacja dnia projektowego na wariancie hali (plan 2026-10-02, etap 3a) —…, Mnożnik wzrostu: > 1 dokłada losowe kopie zadań (czas ±15 min), < 1 losowo…, Linie kompletacji → objazdy: per dokument (bez dokumentu — pojedynczo), max 20…, tasks: [(sekunda od DAY_START, rodzaj, materiał, dokument)]; fleet: {"agv": n,…, Praca od wyjazdu `t0` do końca `t1`; `idle` = postój w oczekiwaniu na ładunek… (+10 more)

### Community 8 - "Community 8"
Cohesion: 0.11
Nodes (16): Meta, WarehouseModelForm, Migration, Modele cyfrowego bliźniaka magazynu: typy regałów, master lokalizacji, szablony…, Element hali, którego siatka regałów nie odwzoruje: dok, brama, korytarz,…, WarehouseHallFeature, WarehouseModel, WarehouseModelRack (+8 more)

### Community 9 - "Community 9"
Cohesion: 0.13
Nodes (14): ImportLog, Material, Meta, Dane podstawowe bliźniaka: materiały, stany w lokalizacjach i dziennik…, Jeden import pliku: rodzaj, wynik i próbka odrzuconych wierszy. Import stanów…, Materiał (SKU): opakowanie zbiorcze i paletyzacja — wejście do rozmieszczenia i…, Pozycja stanu: materiał w lokalizacji (z jednego importu stanów)., StockItem (+6 more)

### Community 10 - "Community 10"
Cohesion: 0.12
Nodes (22): rack_axes(), (u_w, u_d) — jednostkowe osie szerokości i głębokości regału w układzie hali., anchor_count(), anchors(), _center(), clean_elements(), compute_kpi(), equipment_capacity() (+14 more)

### Community 11 - "Community 11"
Cohesion: 0.14
Nodes (22): _aisle_m(), build_scene(), _carry(), _container_flow(), _Ctx, _demo_picks(), _feature_center(), _forklift_task() (+14 more)

### Community 12 - "Community 12"
Cohesion: 0.12
Nodes (15): _docks(), _feature(), generate(), _pair_pitch(), _rack(), Generator hali od parametrów — nowy magazyn „od zera” (plan 2026-10-02, etap…, Poziomy składowania z podłogą: góra najwyższej palety ≤ wysokość − tryskacze., [korytarz][A|B][korytarz]… — y każdego rzędu; A patrzy na korytarz przed, B za. (+7 more)

### Community 13 - "Community 13"
Cohesion: 0.14
Nodes (19): apply_zone_edit(), _box(), collisions(), fit_floor(), Edycja wariantu hali blokami (plan 2026-10-02, etap 4) — czysty Python.…, {strefa: liczba rzędów, gniazd w rzędzie (maks.), poziomy (maks.)} dla…, Zmienia regały strefy w miejscu (dicty jak `model_racks`) i zwraca listę…, Pary regałów nachodzących na siebie (obrysy osiowe, tolerancja `tol` m) —… (+11 more)

### Community 14 - "Community 14"
Cohesion: 0.15
Nodes (18): _geometry(), block_rows(), element_summary(), footprint(), height(), pallet_positions(), params_for(), Katalog elementów do projektowania wariantów magazynu — JEDNO źródło prawdy.… (+10 more)

### Community 15 - "Community 15"
Cohesion: 0.12
Nodes (15): active_master_qs(), Kody lokalizacji magazynu — wspólna konwencja mapy 3D / eksportu SAP. Litera na…, Lokalizacje z aktywnej partii master-daty (pusty queryset, gdy brak partii).…, One import of location master data (height, volume, weight, type)., Master data for a single warehouse location., WarehouseLocationMaster, WarehouseLocationMasterBatch, load_sample() (+7 more)

### Community 16 - "Community 16"
Cohesion: 0.14
Nodes (17): Meta, ModelRun, Przebiegi modeli ML: wersja algorytmu, dane wejściowe, parametry, miary i wynik…, Przebiegi ML na imporcie zadań: dane z bliźniaka → czyste moduły…, run_forecast(), run_segmentation(), _user(), detail() (+9 more)

### Community 17 - "Community 17"
Cohesion: 0.11
Nodes (11): build_sim_scene(), CorridorRouter, _pick_time(), Animacja godziny z symulacji dnia (plan 2026-10-02, etap 3b) — czysty Python.…, Trasa „jak w magazynie”: wzdłuż korytarza do przejazdu poprzecznego, nim do…, Chwila przejęcia ładunku: kombi rusza wcześniej niż AGV, ale paletę bierze po…, Przebiegi rozpoczęte w godzinie `hour` (zegar 5–21). Zwraca (przebiegi, ile…, window_legs() (+3 more)

### Community 18 - "Community 18"
Cohesion: 0.19
Nodes (21): add(), add_block(), _clear(), _coll(), elements(), export_variant(), load_variant(), _make() (+13 more)

### Community 19 - "Community 19"
Cohesion: 0.18
Nodes (21): ValueError, _bool(), _cell(), _code(), _date(), ImportFileError, map_columns(), norm() (+13 more)

### Community 20 - "Community 20"
Cohesion: 0.09
Nodes (13): Flagi ról do szablonów — jedno zapytanie zamiast wielu has_role()., user_roles(), Command, BaseCommand, has_role(), True dla superusera albo członka którejś z grup., Dekorator: wymaga zalogowania + członkostwa w grupie (superuser zawsze…, role_required() (+5 more)

### Community 21 - "Community 21"
Cohesion: 0.13
Nodes (18): missing_required(), parse_rows(), → (poprawne dicty, odrzucone [{row, reason}] — próbka), liczba odrzuconych.…, Command, BaseCommand, import_file(), _level_of(), load_demo() (+10 more)

### Community 22 - "Community 22"
Cohesion: 0.13
Nodes (20): NamedTuple, code_slot(), is_hall_a(), letter_level(), letter_slot(), LetterSlot, level_height_keys(), level_height_mm() (+12 more)

### Community 23 - "Community 23"
Cohesion: 0.16
Nodes (4): override_settings, TestCase, RenderScreenTests, WorkerApiTests

### Community 24 - "Community 24"
Cohesion: 0.12
Nodes (7): MapColumnsTests, ParseTests, SimpleTestCase, Parser plików modułu Dane — czysty Python (bez bazy)., Wzór pliku z ekranu Dane musi się importować bez ręcznych poprawek., ReadTableTests, _xlsx()

### Community 25 - "Community 25"
Cohesion: 0.23
Nodes (9): expand_row(), Rząd + szablon domyślny + wyjątki → lista miejsc (dict). Klucze: code, bay,…, codes(), ExpandModelTests, ExpandRowTests, ov(), SimpleTestCase, Generator adresów modelu magazynu: szablon gniazda + reguła rzędu + wyjątki… (+1 more)

### Community 26 - "Community 26"
Cohesion: 0.20
Nodes (12): backtest(), fit(), forecast(), series: [(dzień porządkowy, wartość)] → (nachylenie log/tydzień, wyraz wolny,…, MAPE [%] prognozy ostatnich `weeks` tygodni z modelu uczonego bez nich (None —…, Wzrost per strumień: roczne tempo P50/P90, mnożnik na `years` lat, MAPE testu…, _daily(), ForecastTests (+4 more)

### Community 27 - "Community 27"
Cohesion: 0.10
Nodes (11): _e, FLOW_LABELS, FLOW_Y, _m, _p, _q, _s, SIM_KEYS (+3 more)

### Community 28 - "Community 28"
Cohesion: 0.15
Nodes (4): override_settings, TestCase, Duży plik → import w wątku w tle (bez blokowania żądania), partia kończy się…, TasksEndpointAndImportTests

### Community 29 - "Community 29"
Cohesion: 0.12
Nodes (10): InstancingGuardTests, TestCase, Regression: warehouse model 3D view used a non-existent `get_item` filter → 500., UX #5: widok 3D nie może cicho paść czarnym ekranem — spinner + guard WebGL +…, Regresja bezpieczeństwa: wolny tekst pól regału/elementu (zone/rack_id/label)…, Regresja: FLOOR_W/FLOOR_D w JS muszą mieć KROPKĘ dziesiętną, nie polski…, R1: stal regałów renderowana przez InstancedMesh (3 draw calle), nie per-mesh.…, StoredXSSGuardTests (+2 more)

### Community 30 - "Community 30"
Cohesion: 0.19
Nodes (7): Agent, _r(), Postój do chwili `t` (realny znacznik zadania); zajęty agent nie cofa się w…, Przejęcie ładunku: klatka „na miejscu" → po `handling` s ładunek jest na…, Odłożenie ładunku w `pos` na wysokości `z` (np. gniazdo regału albo dok)., Agent z osią czasu ruchu: rodzaj z `SPEED` (wózek, pracownik, kombi, AGV, EPT)., Jazda/przejście trasą A* do `target`; trasa trafia też do mapy przepływów.

### Community 31 - "Community 31"
Cohesion: 0.16
Nodes (8): percentile(), Percentyl z interpolacją liniową (jak numpy/Excel PERCENTILE.INC); pusta lista…, _daily(), PercentileTests, ProfileTests, SimpleTestCase, Profil ruchów i dzień projektowy (krok 3): percentyle, dni robocze, dzień…, WorkingDaysTests

### Community 32 - "Community 32"
Cohesion: 0.16
Nodes (13): candidates(), _demo(), evaluate(), fit(), _grid(), mape(), ML1 — prognoza tygodniowych wolumenów: kilka modeli wygładzania wykładniczego…, Najlepsze parametry modelu na serii `y` → (params, fitted, prognoza h→v, sd… (+5 more)

### Community 33 - "Community 33"
Cohesion: 0.14
Nodes (13): _bay_locations(), format_bay_numbers(), make_code(), parse_bay_numbers(), Adresy miejsc paletowych modelu magazynu: szablon gniazda + reguła rzędu +…, „10-47,50” → [10, …, 47, 50]. Pusty tekst → []. Błędny zapis → ValueError., [10, …, 47, 50] → „10-47,50” (odwrotność parse_bay_numbers)., Numery gniazd rzędu w kolejności fizycznej; pusta reguła = 1..n_bays; nadmiar… (+5 more)

### Community 34 - "Community 34"
Cohesion: 0.17
Nodes (13): Item, Osie czasu agentów (wózki widłowe, ludzie) i ładunków (palety, kartony) dla…, Ładunek: paleta albo karton. `appear`/`vanish` sterują widocznością w Blenderze., _at(), container_inbound(), Przyjęcie kontenera z kartonami luzem (plan 2026-10-02, etap 2b) — czysty…, docks: [(środek doku kontenerowego)], stations: [(środek stanowiska…, heading_deg() (+5 more)

### Community 35 - "Community 35"
Cohesion: 0.18
Nodes (17): rack_point(), Punkt hali: `along` [m] wzdłuż szerokości, `across` [m] wzdłuż głębokości…, _access(), _handover(), _picker_route(), _rack_end(), Koniec ruchu w gnieździe regału: (punkt dojazdu z alejki, środek gniazda,…, Przekazanie palety w przejeździe poprzecznym: przed tym czołem rzędu, które… (+9 more)

### Community 36 - "Community 36"
Cohesion: 0.16
Nodes (7): BayTemplate, Szablon gniazda (słupa regału): belka, palety na belce, poziomy od podłogi w…, BayTemplateTests, levels(), TestCase, RackRuleAndOverrideTests, Modele części 1: szablon gniazda (walidacja), reguła rzędu, wyjątki…

### Community 37 - "Community 37"
Cohesion: 0.22
Nodes (8): outward(), Kierunek „na zewnątrz hali” od elementu przy ścianie: normalna najbliższej…, ContainerInboundTests, _f(), _items(), SimpleTestCase, Przyjęcie kontenera w animacji (plan 2026-10-02, etap 2b): kontener przy doku →…, _scene()

### Community 38 - "Community 38"
Cohesion: 0.19
Nodes (11): capacity(), comparison(), Porównanie wariantów hali na tym samym dniu projektowym (plan 2026-10-02, etap…, Miejsca paletowe (regały nie-półkowe), lokalizacje kartonowe (półki K1), bramy,…, Symulacja z flotą sugerowaną przez poprzedni przebieg, aż flota się ustali (≤…, [{wiersz KPI z wartościami per wariant + najlepszy}] dla tabeli., required_fleet(), variant_row() (+3 more)

### Community 39 - "Community 39"
Cohesion: 0.18
Nodes (15): compliance_for_model(), Raport zgodności planu modelu z aktywnym masterem (batch=None → brak kodów EWM)., _compliance_xlsx(), _planner, „Wykryj z EWM” (podgląd propozycji → zapis) i raport zgodności modelu z EWM (+…, Ucieczka przed wstrzyknięciem formuły XLSX: string zaczynający się od =+-@…, _safe(), warehouse_model_compliance() (+7 more)

### Community 40 - "Community 40"
Cohesion: 0.15
Nodes (15): atomic, expand_model(), [(rząd, szablon, wyjątki), …] → (miejsca z kluczami zone/aisle, {kod: [„B0-07”,…, apply_proposal(), detect_for_model(), master_rows(), plan_for_model(), Warstwa ORM nad czystymi modułami adresowania: master EWM, plan modelu, zapis… (+7 more)

### Community 41 - "Community 41"
Cohesion: 0.17
Nodes (13): Wzór pliku: nagłówki (pierwszy alias = polska nazwa) — do pobrania z ekranu…, template_csv(), current_stock_log(), Najnowszy import stanów = aktualny stan magazynu (None, gdy brak)., demo(), home(), log_detail(), materials() (+5 more)

### Community 42 - "Community 42"
Cohesion: 0.13
Nodes (6): MlRunTests, TestCase, Meta, WarehouseTask, ForecastViewTests, TestCase

### Community 43 - "Community 43"
Cohesion: 0.21
Nodes (15): letter_rank(), parse_code(), Klucz sortowania liter poziomów: znane litery wg LETTER_ORDER, obce na końcu., Kod EWM → (strefa, przejście, gniazdo, pozycja, litera, połówka) albo None., detect(), _distance(), _grid(), _new_template() (+7 more)

### Community 44 - "Community 44"
Cohesion: 0.22
Nodes (13): _abc_xyz(), build_profile(), _groups(), _order_profile(), Profil ruchów i dzień projektowy z zadań EWM (spec projektowania magazynu, krok…, daily: {data: {rodzaj: n, "orders": n}}; hourly: {(data, godzina): {rodzaj:…, Dni z ruchem ≥ WORKDAY_SHARE mediany dni z jakimkolwiek ruchem (rosnąco)., ABC wg liczby pobrań (linie kompletacji + wydania), XYZ wg zmienności dziennej. (+5 more)

### Community 45 - "Community 45"
Cohesion: 0.20
Nodes (4): BayTemplateViewTests, CoordsRuleColumnsTests, level_post(), TestCase

### Community 46 - "Community 46"
Cohesion: 0.20
Nodes (7): EquipmentAgentsTests, SimpleTestCase, _rack(), Sprzęt nowego magazynu w animacji (plan 2026-10-02, etap 2): AGV + kombi w…, Paleta przechodzi AGV → kombi w jednym miejscu: między klatkami nie skacze…, Czas klatek palety rośnie: kombi czeka (wait_until), zamiast „cofać" paletę w…, _scene()

### Community 47 - "Community 47"
Cohesion: 0.13
Nodes (9): client_ip(), Middleware przekrojowe: identyfikator żądania (korelacja logów) + nagłówki…, Dopisuje `record.request_id` z bieżącego żądania ("-" poza żądaniem)., Bierze X-Request-ID od proxy albo nadaje nowy; odsyła go w odpowiedzi., Permissions-Policy + Content-Security-Policy (domyślnie report-only)., IP klienta dla django-axes za jednym zaufanym proxy (Traefik/Coolify): ostatni…, RequestIDLogFilter, RequestIDMiddleware (+1 more)

### Community 48 - "Community 48"
Cohesion: 0.18
Nodes (8): abc_by_hits(), build_pallets(), Klasa ABC wg udziału w pobraniach (ta sama reguła progów co…, Czysta funkcja: dane wejściowe jako proste krotki/dicty → (pallets, stats,…, BuildPalletsTests, ParseCodeTests, SimpleTestCase, Palety w lokalizacjach (stan magazynu) w scenie Blendera —…

### Community 49 - "Community 49"
Cohesion: 0.21
Nodes (9): calibrate(), ideal_cycle(), Czas cyklu wg fizyki symulacji: dojazd prev → src, chwyt, przewóz src → dst,…, rows: krotki `blender_tasks.ROW_FIELDS` jednego dnia (rosnąco po potwierdzeniu)., CalibrationTests, SimpleTestCase, Wózek przewozi palety między dwoma gniazdami co `gap_s` sekund., Ten sam ruch co 2 min vs co 4 min → współczynnik rośnie dwukrotnie. (+1 more)

### Community 50 - "Community 50"
Cohesion: 0.18
Nodes (13): _delimiter(), _encoding(), is_cancelled(), iter_table(), kind_from_word(), norm_header(), _parse_dt(), _parse_time() (+5 more)

### Community 51 - "Community 51"
Cohesion: 0.23
Nodes (5): Przebieg po pliku: nagłówek → mapowanie kolumn → wiersze sparsowane albo błędy,…, Poprawne, nieanulowane zadania (dicty pól modelu)., [(etykieta pola, nagłówek z pliku)] w kolejności pól., Scan, ScanFileTests

### Community 52 - "Community 52"
Cohesion: 0.24
Nodes (7): map_columns(), missing_required(), {pole: indeks kolumny}. Najpierw dokładne aliasy, potem nagłówek zaczynający…, DemoFileTests, SimpleTestCase, Zakładka „Projektowanie magazynu” w Magazyn 3D + plik demonstracyjny WT…, HeaderAliasTests

### Community 53 - "Community 53"
Cohesion: 0.22
Nodes (6): parse_number(), parse_stamp(), „1.234,5” / „1,234.5” / „1 234,5” / „5-” (minus SAP na końcu) / liczba → float;…, Data (+ osobny czas, jak w eksporcie SAP) → datetime ze strefą `tz` albo None., Parser eksportu zadań magazynowych EWM (WT): aliasy nagłówków, liczby, daty,…, ValueParsingTests

### Community 55 - "Community 55"
Cohesion: 0.23
Nodes (12): _demo(), _dist2(), features(), kmeans(), _name(), ML2 — segmentacja materiałów pod rozmieszczenie (slotting): k-means na profilu…, {materiał: {hits, cv, active, volume?}} — tylko materiały z ruchem., k-means++ → (przypisania, centroidy, inercja). Deterministyczne dla danego… (+4 more)

### Community 56 - "Community 56"
Cohesion: 0.28
Nodes (5): _inside(), Czy punkt leży w obrysie regału poszerzonym o `margin` [m]., Kod lokalizacji → gniazdo w regale modelu (środek palety, wysokość, obrót).…, SlotLocator, SlotLocatorTests

### Community 57 - "Community 57"
Cohesion: 0.22
Nodes (7): _is_shelf(), Layout, _manh(), _pick(), Agent, który najwcześniej stanie w `start` (nie wcześniej niż `release`)., Punkty obsługi i miejsca wariantu wyliczone z regałów i elementów hali., Miejsce palety dla materiału z czołówki `share` (0 = najczęstszy … 1) wg stref…

### Community 58 - "Community 58"
Cohesion: 0.29
Nodes (6): Wiersze WT (krotki ROW_FIELDS, rosnąco po potwierdzeniu) → (ruchy, pominięte).…, resolve_moves(), SimpleTestCase, ResolveMovesTests, _row(), SceneFromTasksTests

### Community 59 - "Community 59"
Cohesion: 0.24
Nodes (7): check_aisles(), Kontrola szerokości alejek między równoległymi elementami składowania.…, AisleCheckTests, BlenderImportGuardTests, SimpleTestCase, _rack(), Blender importuje te moduły bez Django — żadnego importu Django na poziomie…

### Community 60 - "Community 60"
Cohesion: 0.19
Nodes (7): CompareViewTests, TestCase, HallGeneratorForm, _initial(), _md_role, _save(), warehouse_model_generator()

### Community 61 - "Community 61"
Cohesion: 0.33
Nodes (6): Api, find_blender(), main(), Worker renderów TWINEMA — uruchamiany na komputerze z Blenderem (np. z GPU).…, BLENDER_BIN / --blender → PATH → typowe katalogi instalacji (najnowsza wersja)., run_job()

### Community 62 - "Community 62"
Cohesion: 0.18
Nodes (11): Pozycje stanu jako dicty `build_pallets`: location, hu, sku, name, lot, expiry,…, stock_for_scene(), _activity_picks(), build_scene_for_model(), Aktywność pickerów (picker, kod, materiał; kolejność = confirmed_at) → trasy.…, Scena dla `WarehouseModel`. `batch` = PickerActivityBatch (None → demo…, load_stock_inputs(), Rzeczywiste palety w lokalizacjach → scena Blendera („cyfrowe zdjęcie"… (+3 more)

### Community 63 - "Community 63"
Cohesion: 0.17
Nodes (3): ForecastTests, SimpleTestCase, SegmentationTests

### Community 64 - "Community 64"
Cohesion: 0.17
Nodes (4): TestCase, TestCase, SimSceneViewTests, SimulationViewTests

### Community 65 - "Community 65"
Cohesion: 0.23
Nodes (3): TestCase, rows: lista dictów pól równoległych → payload z listami., WarehouseHallFeatureTests

### Community 66 - "Community 66"
Cohesion: 0.24
Nodes (8): demo_materials(), demo_stock(), material_codes(), Dane demonstracyjne (syntetyczne): materiały zgodne z `tools/ewm_demo_tasks.py`…, Wiersze materiałów (dicty pól Material) z losowymi, ale wiarygodnymi wymiarami., Pozycje stanu dla regałów modelu: ~`fill` miejsc zajętych, materiały wg rotacji…, DemoStockTests, SimpleTestCase

### Community 68 - "Community 68"
Cohesion: 0.27
Nodes (8): DetectHeightsTests, DetectIrregularBayTests, expand_proposal(), master_of(), SimpleTestCase, „Wykryj z EWM”: propozycja szablonów, numeracji i wyjątków z kodów; round-trip…, Propozycja → obiekty jak z bazy → rozwinięte kody per przejście., rows_of()

### Community 69 - "Community 69"
Cohesion: 0.25
Nodes (3): EwmTasksPollingTests, TestCase, Import „w tle” ponad STALE_AFTER = proces padł — polling ma się zatrzymać.

### Community 71 - "Community 71"
Cohesion: 0.24
Nodes (3): FlowPlayerPanelTests, FlowSceneEndpointTests, TestCase

### Community 72 - "Community 72"
Cohesion: 0.25
Nodes (10): bay_template_delete(), bay_template_form(), bay_template_list(), _int(), _levels_from_post(), _md_role, _planner, require_POST (+2 more)

### Community 73 - "Community 73"
Cohesion: 0.31
Nodes (9): bin_code(), day_tasks(), main(), Demonstracyjny eksport zadań magazynowych EWM (/SCWM/MON) do importu w TWINEMA.…, Zadania jednego dnia: [(rodzaj, materiał, dokument)] w kolejności do rozdania…, `n` chwil potwierdzeń jednego zasobu w zmianie: start + odstępy ~ mean_gap,…, row(), rows_for_day() (+1 more)

### Community 74 - "Community 74"
Cohesion: 0.24
Nodes (6): _deg(), _half(), 1/2 dla połówki miejsca (kod z końcówką -1/-2, np. B0-07-300C-1), inaczej 0.…, dict gniazda: x, y, z (dół palety), heading, rozmiar [w, d] (+ half 1/2) albo…, parse_code(), Kod → (zone, rack_id, bay, col_idx, level) albo None.

### Community 75 - "Community 75"
Cohesion: 0.20
Nodes (3): TestCase, RackTypeWeightsTests, Typy regałów A/B/C/D: nośność per poziom (level_weights) — zapis w edytorze,…

### Community 76 - "Community 76"
Cohesion: 0.20
Nodes (7): LocationOverride, Meta, Named location type template — dimensions apply to all locations with matching…, Wyjątek adresu: nadpisuje wynik szablonu dla jednego miejsca albo całego…, Wariant projektu magazynu: elementy z katalogu `twin.design_catalog` (regały,…, WarehouseDesignVariant, WarehouseRackType

### Community 77 - "Community 77"
Cohesion: 0.33
Nodes (8): apply_preset(), _key(), main(), TWINEMA → Blender: render ujęcia (preset kamery) ze sceny „twinema.scene”.…, FFmpeg H.264 w MP4 — Blender 5 przeniósł format wideo do `media_type`., Ustawia „Kamerę TWINEMA” i jej cel wg presetu na klatkach 1…frames., render(), _video_settings()

### Community 78 - "Community 78"
Cohesion: 0.28
Nodes (6): map_kind(), parse_overrides(), „2010 = wydanie” (linia na proces) → ({proces: rodzaj}, [błędy])., Rodzaj procesu mag. → rodzaj ruchu. Kolejność: nadpisania → słownik wyjątków →…, KindMappingTests, SimpleTestCase

### Community 79 - "Community 79"
Cohesion: 0.22
Nodes (3): CalibrationViewTests, TestCase, _racks()

### Community 80 - "Community 80"
Cohesion: 0.46
Nodes (3): parse_row(), Wiersz → dict pól `WarehouseTask` (+ `cancelled`); None = pusty wiersz;…, RowTests

### Community 84 - "Community 84"
Cohesion: 0.29
Nodes (5): compliance(), Raport zgodności modelu z EWM: kody z planu (expand_model) vs kody z mastera,…, rows: [{"zone", "rack_id", "has_template"}]; locations/duplicates: wynik…, CompliancePureTests, SimpleTestCase

### Community 85 - "Community 85"
Cohesion: 0.40
Nodes (4): simple_tag, icon(), Tagi szablonów modułu: ikony Lucide ze sprite'a static/twin/icons/lucide.svg., {% icon "package" %} → dekoracyjna (aria-hidden); z label → role=img + aria-…

### Community 86 - "Community 86"
Cohesion: 0.40
Nodes (4): groups_for(), {materiał: grupa towarowa} albo None, gdy materiałów jeszcze nie zaimportowano.…, load_groups(), {materiał z zadań: grupa towarowa} z modułu Dane; None, gdy materiałów jeszcze…

## Knowledge Gaps
- **18 isolated node(s):** `docker-entrypoint.sh script`, `Migration`, `Migration`, `Meta`, `Migration` (+13 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **19 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `WarehouseModel` connect `Community 8` to `Community 0`, `Community 1`, `Community 2`, `Community 36`, `Community 9`, `Community 41`, `Community 76`, `Community 12`, `Community 15`, `Community 20`, `Community 21`, `Community 29`?**
  _High betweenness centrality (0.053) - this node is a cross-community bridge._
- **Why does `parse_bay_numbers()` connect `Community 33` to `Community 8`, `Community 25`, `Community 19`, `Community 1`?**
  _High betweenness centrality (0.041) - this node is a cross-community bridge._
- **Why does `SlotLocator` connect `Community 56` to `Community 0`, `Community 6`, `Community 8`, `Community 74`, `Community 79`, `Community 48`, `Community 49`, `Community 58`, `Community 28`, `Community 62`?**
  _High betweenness centrality (0.040) - this node is a cross-community bridge._
- **Are the 8 inferred relationships involving `SlotLocator` (e.g. with `BuildPalletsTests` and `ParseCodeTests`) actually correct?**
  _`SlotLocator` has 8 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `WarehouseModel` (e.g. with `Meta` and `WarehouseModelForm`) actually correct?**
  _`WarehouseModel` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Are the 5 inferred relationships involving `Scan` (e.g. with `HeaderAliasTests` and `KindMappingTests`) actually correct?**
  _`Scan` has 5 INFERRED edges - model-reasoned connections that need verification._
- **What connects `docker-entrypoint.sh script`, `Migration`, `Migration` to the rest of the system?**
  _18 weakly-connected nodes found - possible documentation gaps or missing edges._