// Edytor layoutu — tryb „Działka” (D1): hala na działce, linie zabudowy, wjazdy, plac, parking, zieleń, drogi.
// Układ działki jak hali (x w prawo, y w dół planu), format i reguły: twin/site.py — walidacja tylko na serwerze.
// Elementami przeciąganymi są: hala (S.site.hall — narożnik + kąt jak element) i elementy terenu (S.site.areas).
// D2: granica-wielokąt (S.site.boundary [[x, y], …]) — wierzchołki przeciągane uchwytami, dodawane kliknięciem
// w trybie „Dodaj wierzchołki” albo w tabeli; geometria w site-geom.js (lustro twin/site.py).
import { S, change, render, setView, viewCenter } from './layout-editor.js';
import { snap, svgTransform } from './layout-core.js';
import { h, num } from './layout-hall.js';
import { edgeSetbacks, entryOnBoundary, insertIndex, insetPolygon, plotPolygon } from './site-geom.js';

const NS = 'http://www.w3.org/2000/svg';
const $ = (id) => document.getElementById(id);
const CFG = JSON.parse($('le-config').textContent);
export const AREA_COLORS = { yard: '#64748b', road: '#475569', parking: '#94a3b8', green: '#22c55e' };
const AREA_SIZE = { yard: [40, 60], road: [60, 8], parking: [40, 15], green: [30, 10] };
const SIDES = { S: 'Południe (dół planu)', N: 'Północ (góra planu)', W: 'Zachód (lewo)', E: 'Wschód (prawo)' };
let last = '', vdrag = null, addMode = false;
const MIN_V = 3, MAX_V = 64;

/** Obrys działki = obrys wierzchołków granicy (serwer liczy to samo); punkty ≥ 0. */
function fitBox() {
  const b = S.site.boundary;
  if (!b) return;
  S.site.width = Math.max(...b.map((p) => p[0]));
  S.site.depth = Math.max(...b.map((p) => p[1]));
}

/** Hala jako element działki: narożnik + kąt z S.site.hall, wymiary z podłogi (zawsze aktualne). */
export function hallItem() {
  return Object.assign(S.site.hall, { width: S.floor.width, depth: S.floor.depth, _hall: true });
}

export const siteItems = () => (S.site ? [hallItem(), ...S.site.areas] : []);

/** Działka do wysłania (bez pól pomocniczych edytora). */
export function siteOut() {
  if (!S.site) return {};
  fitBox();
  const { x, y, angle } = S.site.hall;
  return { ...S.site, hall: { x, y, angle }, areas: S.site.areas.map(({ _k, ...a }) => a) };   // eslint-disable-line no-unused-vars
}

function el(tag, attrs, parent) {
  const e = document.createElementNS(NS, tag);
  for (const [k, v] of Object.entries(attrs)) e.setAttribute(k, v);
  parent?.appendChild(e);
  return e;
}

function entryAt(e) {
  const { at, dir } = entryOnBoundary(S.site, e);
  return [at, dir];
}

/** Rysunek działki; `drawItem(g, it, color, label)` z edytora (zaznaczanie/przeciąganie jak na hali). */
export function drawSite(g, drawItem) {
  fitBox();
  const s = S.site, { width: W, depth: D } = s, plot = plotPolygon(s);
  const pts = (ps) => ps.map((p) => p.join(',')).join(' ');
  el('polygon', { class: `le-plot${addMode ? ' is-adding' : ''}`, points: pts(plot) }, g);
  const line = insetPolygon(plot, edgeSetbacks(s));
  if (line) el('polygon', { class: 'le-setback', points: pts(line) }, g);
  for (const a of s.areas) drawItem(g, a, AREA_COLORS[a.kind] || '#6b7280', a.label || CFG.areaKinds[a.kind] || a.kind);
  const hall = hallItem();
  drawItem(g, hall, '#0ea5e9', `Hala ${S.floor.width} × ${S.floor.depth} m`);
  const ghost = el('g', { transform: svgTransform(hall), class: 'le-ghost' }, g);    // regały w hali (podgląd)
  for (const r of S.racks) {
    el('rect', { width: r.n_bays * r.bay_width_cm / 100, height: r.depth_cm / 100, transform: svgTransform(r) }, ghost);
  }
  for (const e of s.entries) {
    const [[x, y], [dx, dy]] = entryAt(e), L = Math.max(6, Math.min(W, D) * 0.06);
    const cls = `le-entry${e.kind === 'car' ? ' is-car' : ''}`;
    el('line', { class: cls, x1: x - dx * 2, y1: y - dy * 2, x2: x + dx * L, y2: y + dy * L }, g);
    el('circle', { class: cls, cx: x, cy: y, r: e.width / 2 }, g);
    el('text', { class: 'le-axis', x: x + dx * (L + 2), y: y + dy * (L + 2), 'font-size': Math.max(1.5, W / 70),
      'text-anchor': 'middle', 'dominant-baseline': 'central' }, g).textContent = e.kind === 'car' ? 'Wjazd os.' : 'Wjazd tir';
  }
  if (s.boundary) {                                    // uchwyty wierzchołków granicy (przeciąganie)
    const r = Math.max(0.6, Math.max(W, D) / 120);
    s.boundary.forEach(([x, y], i) => {
      el('circle', { class: 'le-vertex', cx: x, cy: y, r, 'data-v': i }, g);
      el('text', { class: 'le-axis', x: x + r * 1.4, y: y - r * 1.4, 'font-size': r * 1.6 }, g).textContent = String(i + 1);
    });
  }
}

/** Mysz w trybie działki: true = obsłużone (dodanie wierzchołka kliknięciem albo start przeciągania uchwytu). */
export function sitePointer(e, [wx, wy]) {
  const s = S.site;
  if (!s?.boundary) return false;
  if (addMode && !e.target.closest('.le-vertex')) {
    if (s.boundary.length >= MAX_V) return true;
    change(() => { s.boundary.splice(insertIndex(s.boundary, [wx, wy]), 0, [snap(Math.max(0, wx)), snap(Math.max(0, wy))]); fitBox(); });
    return true;
  }
  const v = e.target.closest('.le-vertex');
  if (!v) return false;
  change(() => {});                                    // migawka przed przeciąganiem (cofnij = sprzed ruchu)
  vdrag = Number(v.dataset.v);
  return true;
}

/** Przeciąganie uchwytu wierzchołka; true = ruch obsłużony. */
export function siteDrag([wx, wy], e) {
  if (vdrag === null) return false;
  const snapTo = (v) => (e.altKey ? v : snap(v));
  S.site.boundary[vdrag] = [Math.max(0, snapTo(wx)), Math.max(0, snapTo(wy))];
  fitBox();
  render();
  return true;
}

export function siteDragEnd() {
  if (vdrag === null) return false;
  vdrag = null;
  change(() => {});                                    // sprawdzenie na serwerze po puszczeniu
  return true;
}

/** Właściwości zaznaczonego w trybie działki (hala: tylko położenie; teren: rodzaj, etykieta, wymiary). */
export function siteProps(items) {
  const pos = { step: 0.1 };
  if (items.length !== 1) {
    return h('p', { class: 'text-sm', style: 'margin:0' }, items.length ? `Zaznaczono ${items.length} elementów działki.`
      : 'Nic nie zaznaczono — kliknij halę albo element terenu; parametry działki są w panelu „Działka”.');
  }
  const it = items[0], get = () => it;
  if (it._hall) {
    return h('div', { class: 'le-form' },
      h('p', { class: 'text-sm le-wide', style: 'margin:0' }, 'Hala na działce — przeciągnij albo wpisz położenie narożnika.'),
      num('X [m]', get, 'x', pos), num('Y [m]', get, 'y', pos), num('Kąt [°]', get, 'angle', { min: -360, max: 360, step: 1 }));
  }
  const kind = h('select', { class: 'form-control', onchange: (e) => change(() => { it.kind = e.target.value; }) },
    ...Object.entries(CFG.areaKinds).map(([k, v]) => h('option', { value: k, selected: k === it.kind }, v)));
  return h('div', { class: 'le-form' }, h('label', { class: 'le-wide' }, 'Rodzaj', kind),
    h('label', { class: 'le-wide' }, 'Etykieta', h('input', { class: 'form-control', maxlength: 100, value: it.label || '',
      onchange: (e) => change(() => { it.label = e.target.value.trim(); }) })),
    num('Szerokość [m]', get, 'width', { min: 0.5, max: 10000, step: 0.5 }), num('Głębokość [m]', get, 'depth', { min: 0.5, max: 10000, step: 0.5 }),
    num('X [m]', get, 'x', pos), num('Y [m]', get, 'y', pos), num('Kąt [°]', get, 'angle', { min: -360, max: 360, step: 1 }));
}

/** Granica: prostokąt ↔ wielokąt; tabela wierzchołków (X, Y, usuń) i tryb dodawania kliknięciem na planie. */
function boundaryPanel() {
  const s = S.site;
  if (!s.boundary) {
    return [h('p', { class: 'text-sm', style: 'margin:0 0 6px' }, 'Granica: prostokąt. Działka o innym kształcie — zamień na wielokąt i przesuń wierzchołki.'),
      h('div', { class: 'le-acts' }, h('button', { type: 'button', class: 'btn btn-secondary btn-sm', onclick: () => change(() => {
        s.boundary = [[0, 0], [s.width, 0], [s.width, s.depth], [0, s.depth]];
      }) }, 'Granica dowolna (wielokąt)'))];
  }
  const rows = s.boundary.map((p, i) => h('div', { class: 'le-form le-vertex-row' },
    num(`${i + 1}: X [m]`, () => S.site.boundary[i], 0, { min: 0, max: 10000, step: 0.5, required: true }),
    num('Y [m]', () => S.site.boundary[i], 1, { min: 0, max: 10000, step: 0.5, required: true }),
    h('button', { type: 'button', class: 'btn btn-ghost btn-sm', disabled: s.boundary.length <= MIN_V,
      'aria-label': `Usuń wierzchołek ${i + 1}`, onclick: () => change(() => { S.site.boundary.splice(i, 1); fitBox(); }) }, 'Usuń')));
  const add = h('button', { type: 'button', class: 'btn btn-secondary btn-sm', 'aria-pressed': String(addMode), onclick: () => {
    addMode = !addMode;
    if (S.view !== 'site') setView('site');
    last = '';
    render();
  } }, addMode ? 'Zakończ dodawanie' : 'Dodaj wierzchołki kliknięciem');
  return [h('p', { class: 'text-sm', style: 'margin:0 0 6px' }, addMode
    ? 'Kliknij na planie — punkt trafi na najbliższą krawędź granicy. Uchwyty wierzchołków można przeciągać.'
    : 'Granica-wielokąt: przeciągnij uchwyty na planie albo wpisz współrzędne (np. z planu miejscowego).'),
  ...rows, h('div', { class: 'le-acts' }, add,
    h('button', { type: 'button', class: 'btn btn-ghost btn-sm', onclick: () => change(() => { addMode = false; delete S.site.boundary; }) },
      'Wróć do prostokąta'))];
}

function select(label, value, options, onchange, wide = false) {
  return h('label', wide ? { class: 'le-wide' } : {}, label, h('select', { class: 'form-control', onchange: (e) => onchange(e.target.value) },
    ...Object.entries(options).map(([k, v]) => h('option', { value: k, selected: k === value }, v))));
}

/** Panel „Działka”: wymiary, ograniczenia zabudowy, dojazd i wjazdy, dodawanie terenu. */
export function renderSitePanel() {
  const box = $('le-site');
  const sig = JSON.stringify([S.site && siteOut(), S.view]);
  const typing = box.contains(document.activeElement) && document.activeElement.matches('input, select, textarea');
  if (sig === last || typing) return;               // nie przebudowuj pod kursorem; kliknięty przycisk — tak
  last = sig;
  if (!S.site) {
    box.replaceChildren(h('p', { class: 'text-sm', style: 'margin:0 0 8px' },
      'Model nie ma działki. Dodaj działkę z placami przed dokami, drogą, parkingiem i zielenią — potem dopasuj wymiary i ograniczenia z planu miejscowego.'),
    h('button', { type: 'button', class: 'btn btn-secondary btn-sm', onclick: () => {
      change(() => { S.site = JSON.parse(JSON.stringify(CFG.defaultSite)); });
      setView('site');
    } }, 'Dodaj działkę wokół hali'));
    return;
  }
  const s = S.site, site = () => S.site, sb = () => S.site.setback;
  const dims = s.boundary
    ? [h('p', { class: 'text-sm le-wide', style: 'margin:0' }, `Obrys granicy: ${s.width} × ${s.depth} m`)]
    : [num('Szerokość działki [m]', site, 'width', { min: 5, max: 10000, step: 0.5, required: true }),
      num('Głębokość działki [m]', site, 'depth', { min: 5, max: 10000, step: 0.5, required: true })];
  const form = h('div', { class: 'le-form' }, ...dims,
    num('Maks. wysokość budynku [m]', site, 'max_height', { min: 2, max: 200, placeholder: 'brak' }),
    num('Maks. zabudowa [%]', site, 'max_coverage_pct', { min: 1, max: 100, step: 1, placeholder: 'brak' }),
    num('Min. biologicznie czynna [%]', site, 'min_bio_pct', { min: 0, max: 100, step: 1, placeholder: 'brak' }),
    num('Od drogi [m]', sb, 'road', { min: 0, max: 500, required: true }),
    num('Od pozostałych granic [m]', sb, 'other', { min: 0, max: 500, required: true }),
    select('Strona dojazdu', s.access_side, SIDES, (v) => change(() => { S.site.access_side = v; }), true));
  const entries = s.entries.map((e, i) => {
    const get = () => S.site.entries[i];
    return h('div', { class: 'le-form le-entry-row' },
      select(`Wjazd ${i + 1}`, e.kind, { truck: 'Tiry', car: 'Osobowe / kurier' }, (v) => change(() => { get().kind = v; })),
      select('Strona', e.side, SIDES, (v) => change(() => { get().side = v; })),
      num('Od początku boku [m]', get, 'pos', { min: 0, step: 0.5, required: true }),
      num('Szerokość [m]', get, 'width', { min: 3, max: 50, step: 0.5, required: true }),
      h('button', { type: 'button', class: 'btn btn-ghost btn-sm le-wide', onclick: () => change(() => S.site.entries.splice(i, 1)) },
        `Usuń wjazd ${i + 1}`));
  });
  const addEntry = h('button', { type: 'button', class: 'btn btn-secondary btn-sm', onclick: () => change(() => {
    S.site.entries.push({ kind: 'truck', side: S.site.access_side, pos: snap((S.site.access_side === 'W' || S.site.access_side === 'E'
      ? S.site.depth : S.site.width) / 2), width: 10 });
  }) }, 'Dodaj wjazd');
  const kind = h('select', { class: 'form-control', 'aria-label': 'Rodzaj elementu terenu' },
    ...Object.entries(CFG.areaKinds).map(([k, v]) => h('option', { value: k }, v)));
  const addArea = h('button', { type: 'button', class: 'btn btn-secondary btn-sm', onclick: () => {
    const [w, d] = AREA_SIZE[kind.value] || [20, 20];
    if (S.view !== 'site') setView('site');
    const [cx, cy] = viewCenter();
    change(() => S.site.areas.push({ kind: kind.value, label: CFG.areaKinds[kind.value], x: snap(cx - w / 2), y: snap(cy - d / 2),
      width: w, depth: d, angle: 0 }));
  } }, 'Dodaj na środku widoku');
  box.replaceChildren(form, h('hr', { class: 'le-hr' }), ...boundaryPanel(), h('hr', { class: 'le-hr' }), ...entries, h('div', { class: 'le-acts' }, addEntry),
    h('hr', { class: 'le-hr' }), h('div', { class: 'le-acts' }, h('label', {}, 'Teren', kind), addArea),
    h('div', { class: 'le-acts' }, h('button', { type: 'button', class: 'btn btn-ghost btn-sm', onclick: () => {
      change(() => { S.site = null; });
      setView('hall');
    } }, 'Usuń działkę')));
}

