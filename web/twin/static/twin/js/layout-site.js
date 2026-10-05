// Edytor layoutu — tryb „Działka” (D1): hala na działce, linie zabudowy, wjazdy, plac, parking, zieleń, drogi.
// Układ działki jak hali (x w prawo, y w dół planu), format i reguły: twin/site.py — walidacja tylko na serwerze.
// Elementami przeciąganymi są: hala (S.site.hall — narożnik + kąt jak element) i elementy terenu (S.site.areas).
import { S, change, setView, viewCenter } from './layout-editor.js';
import { snap, svgTransform } from './layout-core.js';
import { h, num } from './layout-hall.js';

const NS = 'http://www.w3.org/2000/svg';
const $ = (id) => document.getElementById(id);
const CFG = JSON.parse($('le-config').textContent);
export const AREA_COLORS = { yard: '#64748b', road: '#475569', parking: '#94a3b8', green: '#22c55e' };
const AREA_SIZE = { yard: [40, 60], road: [60, 8], parking: [40, 15], green: [30, 10] };
const SIDES = { S: 'Południe (dół planu)', N: 'Północ (góra planu)', W: 'Zachód (lewo)', E: 'Wschód (prawo)' };
let last = '';

/** Hala jako element działki: narożnik + kąt z S.site.hall, wymiary z podłogi (zawsze aktualne). */
export function hallItem() {
  return Object.assign(S.site.hall, { width: S.floor.width, depth: S.floor.depth, _hall: true });
}

export const siteItems = () => (S.site ? [hallItem(), ...S.site.areas] : []);

/** Działka do wysłania (bez pól pomocniczych edytora). */
export function siteOut() {
  if (!S.site) return {};
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
  const { width: W, depth: D } = S.site;
  return { N: [[e.pos, 0], [0, 1]], S: [[e.pos, D], [0, -1]], W: [[0, e.pos], [1, 0]], E: [[W, e.pos], [-1, 0]] }[e.side];
}

/** Rysunek działki; `drawItem(g, it, color, label)` z edytora (zaznaczanie/przeciąganie jak na hali). */
export function drawSite(g, drawItem) {
  const s = S.site, { width: W, depth: D } = s, sb = s.setback || {};
  el('rect', { class: 'le-plot', x: 0, y: 0, width: W, height: D }, g);
  const off = (k) => (k === s.access_side ? sb.road : sb.other) || 0;
  const bx = off('W'), by = off('N'), bw = W - off('E') - bx, bh = D - off('S') - by;
  if (bw > 0 && bh > 0) el('rect', { class: 'le-setback', x: bx, y: by, width: bw, height: bh }, g);
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

function select(label, value, options, onchange, wide = false) {
  return h('label', wide ? { class: 'le-wide' } : {}, label, h('select', { class: 'form-control', onchange: (e) => onchange(e.target.value) },
    ...Object.entries(options).map(([k, v]) => h('option', { value: k, selected: k === value }, v))));
}

/** Panel „Działka”: wymiary, ograniczenia zabudowy, dojazd i wjazdy, dodawanie terenu. */
export function renderSitePanel() {
  const box = $('le-site');
  const sig = JSON.stringify([S.site && siteOut(), S.view]);
  if (sig === last || box.contains(document.activeElement)) return;
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
  const form = h('div', { class: 'le-form' },
    num('Szerokość działki [m]', site, 'width', { min: 5, max: 10000, step: 0.5, required: true }),
    num('Głębokość działki [m]', site, 'depth', { min: 5, max: 10000, step: 0.5, required: true }),
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
  box.replaceChildren(form, h('hr', { class: 'le-hr' }), ...entries, h('div', { class: 'le-acts' }, addEntry),
    h('hr', { class: 'le-hr' }), h('div', { class: 'le-acts' }, h('label', {}, 'Teren', kind), addArea),
    h('div', { class: 'le-acts' }, h('button', { type: 'button', class: 'btn btn-ghost btn-sm', onclick: () => {
      change(() => { S.site = null; });
      setView('hall');
    } }, 'Usuń działkę')));
}

