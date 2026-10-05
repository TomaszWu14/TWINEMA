// Panele edytora layoutu: strefy, właściwości zaznaczenia, KPI na żywo, problemy, formularze dodawania.
// Panele z polami/przyciskami przebudowujemy tylko, gdy zmieniła się ich treść — fokus klawiatury zostaje.
import { makeBlock, mode, nextRackIds, snap, zoneColors } from './layout-core.js';
import { S, addItems, change, deleteSelected, duplicateSelected, keysAt, rotateSelected, selectZone, selected,
  showKeys, viewCenter } from './layout-editor.js';

const $ = (id) => document.getElementById(id);
const CFG = JSON.parse($('le-config').textContent);
const fmt = (v, d = 0) => (typeof v === 'number' ? v.toLocaleString('pl-PL', { maximumFractionDigits: d }) : '—');
const last = {};
// Domyślne wymiary nowych elementów hali [m] (szer. × głęb.) — do poprawienia w panelu właściwości.
const FEATURE_SIZE = { dock: [3.5, 2], gate: [4, 0.5], staging: [10, 6], station: [3, 3], leader: [3, 3],
  corridor: [20, 3], block_zone: [10, 10], returns: [6, 6], other: [5, 5] };

function h(tag, attrs = {}, ...children) {
  const e = document.createElement(tag);
  for (const [k, v] of Object.entries(attrs)) {
    if (k.startsWith('on')) e.addEventListener(k.slice(2), v);
    else if (v !== false && v !== null && v !== undefined) e.setAttribute(k, v === true ? '' : v);
  }
  e.append(...children.filter((c) => c !== null && c !== undefined));
  return e;
}

/** Zmienił się podpis panelu? (i nie piszesz akurat w jego polu — wtedy nie przerywamy) */
function stale(name, sig, box) {
  if (last[name] === sig) return false;
  if (box.contains(document.activeElement) && last[`${name}:sel`] === S.sel.size + [...S.sel].join()) return false;
  last[name] = sig;
  last[`${name}:sel`] = S.sel.size + [...S.sel].join();
  return true;
}

function renderZones() {
  const box = $('le-zones'), counts = {};
  S.racks.forEach((r) => { counts[r.zone] = (counts[r.zone] || 0) + 1; });
  const colors = zoneColors(S.racks);
  const sig = JSON.stringify(counts);
  if (!stale('zones', sig, box)) return;
  box.replaceChildren(...Object.keys(colors).map((z) => h('li', {},
    h('button', { type: 'button', class: 'btn btn-ghost btn-sm', onclick: () => selectZone(z) },
      h('span', { class: 'le-swatch', style: `background:${colors[z]}`, 'aria-hidden': 'true' }),
      `Strefa ${z} · ${counts[z]} regałów`))));
  if (!S.racks.length) box.replaceChildren(h('li', { class: 'text-muted text-sm' }, 'Brak regałów — dodaj blok.'));
}

/** Pole liczbowe/tekstowe zmieniające jedną właściwość elementu (z walidacją przeglądarki). */
function field(label, item, key, { wide, ...attrs }, parse = Number) {
  const input = h('input', { class: 'form-control', value: item[key], ...attrs,
    onchange: (e) => {
      if (!e.target.checkValidity()) { e.target.reportValidity(); return; }
      const v = parse(e.target.value);
      if (v !== item[key]) change(() => { item[key] = v; });
    } });
  return h('label', wide ? { class: 'le-wide' } : {}, label, input);
}

function renderProps() {
  const box = $('le-props'), items = selected();
  const sig = JSON.stringify([S.floor, items]);
  if (!stale('props', sig, box)) return;
  const L = CFG.limits;
  const num = (k) => ({ type: 'number', required: true, min: L[k][0], max: L[k][1], step: 1 });
  const pos = { type: 'number', required: true, step: 0.1 };
  const txt = (max) => ({ required: true, maxlength: max });
  const text = (v) => v.trim();
  let form;
  if (!items.length) {
    form = h('div', { class: 'le-form' },
      field('Szerokość hali [m]', S.floor, 'width', { ...pos, min: 1, max: 5000 }),
      field('Głębokość hali [m]', S.floor, 'depth', { ...pos, min: 1, max: 5000 }),
      h('p', { class: 'text-muted text-sm le-wide', style: 'margin:0' }, 'Nic nie zaznaczono — kliknij regał albo element hali.'));
  } else if (items.length === 1 && items[0].n_bays !== undefined) {
    const r = items[0];
    form = h('div', { class: 'le-form' },
      field('Strefa', r, 'zone', txt(20), text), field('Numer', r, 'rack_id', txt(20), text),
      field('Gniazda', r, 'n_bays', num('n_bays')), field('Poziomy', r, 'n_levels', num('n_levels')),
      field('Szer. gniazda [cm]', r, 'bay_width_cm', num('bay_width_cm')), field('Głębokość [cm]', r, 'depth_cm', num('depth_cm')),
      field('Wys. poziomu [cm]', r, 'level_height_cm', num('level_height_cm')), field('Kąt [°]', r, 'angle', { ...pos, min: -360, max: 360 }),
      field('X [m]', r, 'x', pos), field('Y [m]', r, 'y', pos));
  } else if (items.length === 1) {
    const f = items[0];
    const kind = h('select', { class: 'form-control', onchange: (e) => change(() => { f.kind = e.target.value; }) },
      ...Object.entries(S.kinds).map(([k, v]) => h('option', { value: k, selected: k === f.kind }, v)));
    form = h('div', { class: 'le-form' }, h('label', { class: 'le-wide' }, 'Rodzaj', kind),
      field('Etykieta', f, 'label', { maxlength: 100, wide: true }, text),
      field('Szerokość [m]', f, 'width', { ...pos, min: 0.1, max: 5000 }), field('Głębokość [m]', f, 'depth', { ...pos, min: 0.1, max: 5000 }),
      field('X [m]', f, 'x', pos), field('Y [m]', f, 'y', pos), field('Kąt [°]', f, 'angle', { ...pos, min: -360, max: 360 }));
  } else {
    form = h('p', { class: 'text-sm', style: 'margin:0 0 8px' }, `Zaznaczono ${items.length} elementów.`);
  }
  const actions = items.length ? h('div', { style: 'display:flex;flex-wrap:wrap;gap:6px;margin-top:10px' },
    h('button', { type: 'button', class: 'btn btn-secondary btn-sm', onclick: () => rotateSelected(90) }, 'Obróć 90°'),
    h('button', { type: 'button', class: 'btn btn-secondary btn-sm', onclick: () => rotateSelected(-90) }, 'Obróć −90°'),
    h('button', { type: 'button', class: 'btn btn-secondary btn-sm', onclick: duplicateSelected }, 'Duplikuj'),
    h('button', { type: 'button', class: 'btn btn-ghost btn-sm', onclick: deleteSelected }, 'Usuń')) : null;
  box.replaceChildren(form, ...(actions ? [actions] : []));
}

function renderKpi() {
  const k = S.kpi || {}, t = k.travel || {};
  const rows = [['Miejsca paletowe', fmt(k.pallet_positions)], ['Miejsca na m² hali', fmt(k.positions_per_m2, 2)],
    ['Powierzchnia hali', `${fmt(k.floor_area_m2)} m²`], ['Zabudowa', `${fmt(k.built_area_m2)} m²`],
    ['Śr. droga do miejsca', `${fmt(t.avg_m, 1)} m`], ['Śr. droga — strefa A', `${fmt(t.a_zone_avg_m, 1)} m`],
    ['Regały', fmt(S.racks.length)], ['Elementy hali', fmt(S.features.length)]];
  $('le-kpi').replaceChildren(...rows.flatMap(([a, b]) => [h('dt', {}, a), h('dd', {}, b)]));
}

function renderIssues() {
  const box = $('le-issues');
  if (last.issues === S.issues) return;
  last.issues = S.issues;
  const e = S.issues.filter((i) => i.severity === 'error').length;
  $('le-issue-count').textContent = S.issues.length ? `Problemy · błędy ${e}, ostrzeżenia ${S.issues.length - e}` : 'Problemy';
  box.replaceChildren(...(S.issues.length ? S.issues.map((it) => h('li', {},
    h('button', { type: 'button', class: `is-${it.severity}`, onclick: () => showKeys(keysAt(it.racks, it.features)) },
      `${it.severity === 'error' ? 'Błąd' : 'Ostrzeżenie'}: ${it.message}`)))
    : [h('li', { class: 'text-muted text-sm' }, 'Brak problemów.')]));
}

function initForms() {
  if (last.forms || !Object.keys(S.kinds).length) return;
  last.forms = true;
  const b = $('le-block').elements;
  b.bay_width_cm.value = mode(S.racks.map((r) => r.bay_width_cm), 270);
  b.depth_cm.value = mode(S.racks.map((r) => r.depth_cm), 110);
  b.level_height_cm.value = mode(S.racks.map((r) => r.level_height_cm), 180);
  b.levels.value = mode(S.racks.map((r) => r.n_levels), 5);
  b.aisle.value = CFG.aisle;
  $('le-block').addEventListener('submit', (e) => {
    e.preventDefault();
    const v = Object.fromEntries(['rows', 'bays', 'levels', 'bay_width_cm', 'depth_cm', 'level_height_cm', 'aisle']
      .map((k) => [k, Number(b[k].value)]));
    const zone = b.zone.value.trim(), [cx, cy] = viewCenter();
    const w = v.bays * v.bay_width_cm / 100, d = v.rows * (v.depth_cm / 100 + v.aisle);
    addItems(makeBlock({ x: snap(cx - w / 2), y: snap(cy - d / 2), rows: v.rows, bays: v.bays, levels: v.levels,
      bayWidthCm: v.bay_width_cm, depthCm: v.depth_cm, levelHeightCm: v.level_height_cm, aisle: v.aisle, zone,
      ids: nextRackIds(S.racks, zone, v.rows), backToBack: b.back.checked }).map((r) => ({ id: null, ...r })), S.racks);
  });
  const fk = $('le-feature-kind'), f = $('le-feature').elements;
  fk.replaceChildren(...Object.entries(S.kinds).map(([k, v]) => h('option', { value: k }, v)));
  fk.value = 'staging' in S.kinds ? 'staging' : fk.options[0]?.value;
  const sizes = () => { [f.width.value, f.depth.value] = FEATURE_SIZE[fk.value] || [5, 5]; };
  fk.addEventListener('change', sizes);
  sizes();
  $('le-feature').addEventListener('submit', (e) => {
    e.preventDefault();
    const [cx, cy] = viewCenter(), w = Number(f.width.value), d = Number(f.depth.value);
    addItems([{ id: null, kind: fk.value, label: S.kinds[fk.value], x: snap(cx - w / 2), y: snap(cy - d / 2),
      width: w, depth: d, angle: 0 }], S.features);
  });
}

export function renderPanels() {
  initForms();
  renderZones();
  renderProps();
  renderKpi();
  renderIssues();
}
