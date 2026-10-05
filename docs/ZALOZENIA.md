# TWINEMA — założenia master daty i scenariuszy

Wynik burzy mózgów z właścicielem (2026-10-05, 25 + 10 pytań). Dokument jest źródłem prawdy dla etapów
po F5: edytor layoutu, scenariusze (plan przyjęć/wydań), symulacja dnia i animacja „jak może wyglądać przyszły
layout”. Liczby mają odpowiadać realnej pracy magazynu — zawsze edytowalne, zwykle jako **min / średnio / max**.

Priorytet po F5: film i montaż odstawione; najważniejsze jest budowanie layoutu i jego animacja w przeglądarce.
Kolejność: **E1 silnik edytora → scenariusz (plan przyjęć i wydań) → E2 edytor 2D → E3 podgląd 3D → tryb
prezentacji 3D → katalog sprzętu (z kosztami)**. Porównanie „obecny vs przyszły” obok siebie — nie.

## Cel i odbiorcy
| # | Temat | Decyzja |
|---|---|---|
| 1 | Cel master daty | wszystko po równo: wymiarowanie hali, realistyczna animacja i uczciwe porównanie wariantów na tych samych danych |
| 25 | Rola Podgląd (zarząd, rekruter) | widzi wyniki i 3D (layout, animacja dnia, KPI, wąskie gardła, scenariusze), **bez danych źródłowych** i bez edycji |
| 24 | Dane demo | syntetyczne CD z importem kontenerowym: ~8 kontenerów 40'/dzień (~45 palet), 6–10 aut 33-pal. (17–32 palet), solówki/busy, ~2 000 SKU, kompletacja kartonowa, paczki i palety OUT; anonimowo |

## Materiał i nośniki
| # | Temat | Decyzja |
|---|---|---|
| 2 | Hierarchia opakowań | sztuka → karton → paleta: wymiary i waga każdego poziomu + przeliczniki (szt/karton, kartonów/warstwę, warstw/paletę) |
| 3 | Nośniki | katalog nośników: EUR 120×80 domyślnie + edytowalna lista (wymiary, waga, max wysokość); materiał wskazuje swój nośnik |
| 4 | Wysokość palety | **klasy wysokości** (np. do 1,0 / 1,4 / 1,8 m) przypisane do materiału |
| 5 | Waga | klasy wagi + nośność poziomu w typie regału → **ostrzeżenia** (ciężkie za wysoko / ponad nośność), bez twardej blokady |
| 6 | Rotacja (ABC) | z historii zadań (ABC×XYZ, k-means już są) + ręczna klasa A/B/C dla nowych materiałów bez historii |

## Scenariusz (niezależny od layoutu)
| # | Temat | Decyzja |
|---|---|---|
| 20 | Gdzie żyją parametry | obiekt **Scenariusz** (np. „Rok bazowy”, „Szczyt ×1,3”) wybierany do dowolnego modelu hali — ten sam scenariusz testuje różne layouty |
| 7 | Dni | **dzień typowy + dzień szczytowy** w każdym scenariuszu |
| 13 | Wzrost | **mnożnik ręczny** (np. ×1,3) na stan i wolumeny |
| 19 | Wprowadzanie | formularze z wartościami domyślnymi dla parametrów + import xlsx (z wzorem pliku) dla list |
| 10D | Losowość | ziarno zapisane w scenariuszu (powtarzalnie); KPI z kilkunastu przebiegów: średnia i najgorszy przypadek (P95) |

## Przyjęcia
| # | Temat | Decyzja |
|---|---|---|
| — | Typy dostaw v1 | **kontener 40' luzem**, **auto 33-paletowe**, **solówka / bus**; liczba przyjazdów/dzień (np. 8 kontenerów) |
| — | Wolumen | kontener 40': średnio ~45 palet po paletyzacji (kartonów zmiennie — duże/małe); auto 33-pal.: fizycznie np. 17–32 palet; wszystko min/śr/max |
| 8 | Rozkład w czasie | **okna awizacji** per typ (np. kontenery 6:00–14:00) — w oknie równomiernie z losowym rozrzutem |
| 9 | Czas rozładunku | z **norm wydajności**: kontener luzem — kartonów/h na osobę × liczba osób; auto paletowe — min na paletę |
| 10 | Paletyzacja z kontenera | **mono-SKU ręcznie** wg „kartonów/paletę” z master daty, resztki na paletę mieszaną; stanowiska przy dokach, kartonów/h na osobę |
| D1 | Palety z aut | mieszanka: **% mono-SKU** (na regał) vs **% mieszanych** (rozbicie/przepakowanie) — min/śr/max |
| D2 | Kontrola | **% kontrolowanych** jednostek + czas na jednostkę; zajmuje pole odkładcze i ludzi (KPI + animacja) |
| D6 | Doki | osobne IN i OUT (kontenerowe z przenośnikiem teleskopowym, paletowe) + opcja oznaczenia doku jako wspólnego |
| D8 | Pole odkładcze | potrzebna powierzchnia **z symulacji**: max palet naraz w szczycie × m² na paletę z alejkami vs pole narysowane w edytorze |

## Składowanie i kompletacja
| # | Temat | Decyzja |
|---|---|---|
| 12 | Potrzebne miejsca paletowe | **z importu stanów** (× mnożnik wzrostu) vs dostępne w layoucie |
| D3 | Kompletacja | **osobna strefa kompletacji** (półkowe/przepływowe lub poziom 0) zasilana z wysokiego składowania; ile SKU w pickingu, min/max w lokacji → uzupełnienia |
| D9 | Sprzęt od początku | reach truck + regały standard, VNA (kombi), AGV/AMR transport poziomy, wózki paletowe elektryczne |
| 15 | Koszty | **później** — razem z katalogiem sprzętu (CAPEX/OPEX) |

## Wydania i paczki
| # | Temat | Decyzja |
|---|---|---|
| 11 | Zamówienia | profil: zamówień/dzień, linii na zamówienie (min/śr/max), udział pełnych palet vs kompletacji kartonowej |
| D5 | Auta wyjazdowe | **jak przyjęcia**: typy (33-pal., solówka, bus, kurier po paczki), liczba/dzień, palet faktycznie na aucie min/śr/max, okna załadunku i cut-off |
| 16–17 | Pakowanie i nadanie | proces między kompletacją a wydaniem: stanowiska pakowania, etykieta/„nadanie” jako krok z czasem, sortowanie per przewoźnik, cut-off — **model procesu, bez integracji API** |
| 18 | Profil paczek | **tylko paczek/dzień** (min/śr/max) |
| D4 | Powstawanie paczki | **pakowanie wielu pozycji**: zamówienie z kilku linii → stanowisko → 1 paczka; czas na paczkę + na linię |

## Ludzie i czas
| # | Temat | Decyzja |
|---|---|---|
| 14 | Obsada | osoby per proces (rozładunek, paletyzacja, kontrola, kompletacja, pakowanie, załadunek) i zmiana + normy wydajności; KPI: potrzebna vs zakładana |
| D7 | Zmiany | **1–3 zmiany per proces** + przerwy; dni pracy w tygodniu |

## Wyniki, animacja, wąskie gardła
| # | Temat | Decyzja |
|---|---|---|
| 16 | Procesy w v1 | przyjęcie + paletyzacja, składowanie, kompletacja, **pakowanie i nadanie**, wydanie + załadunek |
| 21 | Karta KPI layoutu | pojemność vs potrzeba; doki i pole odkładcze (kolejka aut, m²); obsada i flota (wykorzystanie %); przepustowość dnia (palet IN/OUT, paczek, zamówień; opóźnienia po cut-off) |
| 22 | Wąskie gardła | **wskazać i podpowiedzieć**: czerwone miejsce w 3D + opis („brakuje 2 doków 10:00–12:00”) + podpowiedź; decyzja u użytkownika |
| 23 | Animacja dnia | **dokładna**: każdy kontener, auto, paleta i paczka ze scenariusza w prawdziwym czasie dnia; odtwarzanie ×10–×300 z zegarem, licznikami i skokiem do szczytu |

## Wynikające etapy (propozycja do potwierdzenia przed kodem)
1. **S1 Master data materiału** — opakowania szt→karton→paleta, katalog nośników, klasy wysokości i wagi, ręczna klasa ABC; import xlsx z wzorem.
2. **S2 Scenariusz** — obiekt Scenariusz (dzień typowy/szczyt, mnożnik, ziarno), plan przyjęć (3 typy dostaw, okna awizacji, normy, % mono/mix, % kontroli), plan wydań (zamówienia, auta OUT, paczki/dzień, cut-off), obsada i zmiany per proces; formularze + xlsx.
3. **S3 Symulacja scenariusza** — przebieg dnia na layoucie (czysty Python, wiele przebiegów, P95): kolejki przy dokach, pole odkładcze, obsada, flota, opóźnienia; karta KPI + wąskie gardła z podpowiedziami.
4. **S4 Animacja dnia** — odtwarzacz z zegarem i przyspieszeniem, każdy obiekt ze scenariusza, podświetlenie wąskich gardeł w 3D.
Etapy przeplatają się z edytorem (E1–E3) wg kolejności z góry; każdy = osobne PR-y.
