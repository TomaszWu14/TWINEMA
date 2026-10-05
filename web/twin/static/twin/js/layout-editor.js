// Edytor layoutu hali (E2): plan z góry w SVG (1 jednostka = 1 m), API z E1:
// GET uklad.json → stan; POST uklad/sprawdz/ (300 ms po zmianie) → KPI + problemy; POST uklad/zapisz/.
// Problemy wskazują elementy po INDEKSIE list — kolejność list się nie zmienia poza dodaniem/usunięciem.
import { History, bbox, corners, rotateGroup, snap, svgTransform, zoneColors } from './layout-core.js';
import { renderPanels } from './layout-panels.js';
import { deleteSelectedColumn, drawColumns, drawUnderlay, hallPointer } from './layout-hall.js';
import { initPreview, preview3d } from './layout-preview.js';
import { bindFullscreenButton } from './fullscreen.js';

const NS = 'http://www.w3.org/2000/svg';
const CFG = JSON.parse(document.getElementById('le-config').textContent);
const CSRF = document.querySelector('[name=csrfmiddlewaretoken]').value;
const $ = (id) => document.getElementById(id);
const svg = $('le-svg');

export const S = { floor: { width: 50, depth: 30 }, racks: [], features: [], version: '', kinds: {},
  columns: {}, colList: [], underlay: null, selCol: null, calib: null,
  sel: new Set(), errK: new Set(), warnK: new Set(), issues: [], kpi: {}, dirty: false };
const history = new History();
let seq = 0, checkSeq = 0, checkTimer = null, checkAbort = null;
let vb = { x: 0, y: 0, w: 50, h: 30 };

const keyOf = (it) => (it._k ||= ++seq);
const all = () => [...S.features, ...S.racks];
export const selected = () => all().filter((it) => S.sel.has(keyOf(it)));
const snapshot = () => JSON.stringify({ floor: S.floor, racks: S.racks, features: S.features, columns: S.columns,
  underlay: S.underlay });
const strip = ({ _k, ...rest }) => rest;           // eslint-disable-line no-unused-vars

export function status(text, kind = '') {
  const el = $('le-status');
  el.textContent = text;
  el.className = `le-status${kind ? ` is-${kind}` : ''}`;
}

// ── zmiany stanu ───────────────────────────────────────────────────────────────────────────
/** Każda edycja przechodzi tędy: migawka do historii → zmiana → przerysowanie → sprawdzenie. */
export function change(fn) {
  const before = snapshot();
  fn();
  history.push(before);
  touched();
}

function touched() {
  S.dirty = true;
  scheduleCheck();
  render();
}

function restore(snap) {
  const s = JSON.parse(snap);
  Object.assign(S, { floor: s.floor, racks: s.racks, features: s.features, columns: s.columns, underlay: s.underlay });
  const keys = new Set(all().map(keyOf));
  S.sel = new Set([...S.sel].filter((k) => keys.has(k)));
  touched();
}

export function selectKeys(keys, add = false) {
  if (!add) S.sel.clear();
  keys.forEach((k) => S.sel.add(k));
  render();
}

export function selectZone(zone) {
  selectKeys(S.racks.filter((r) => r.zone === zone).map(keyOf));
}

/** Zaznacz elementy i — gdy są poza widokiem — wyśrodkuj na nich (lista problemów). */
export function showKeys(keys) {
  const items = all().filter((it) => keys.includes(keyOf(it)));
  if (items.length) {
    const [x0, y0, x1, y1] = bbox(items.flatMap(corners));
    if (x0 < vb.x || y0 < vb.y || x1 > vb.x + vb.w || y1 > vb.y + vb.h) {
      vb.x = (x0 + x1) / 2 - vb.w / 2; vb.y = (y0 + y1) / 2 - vb.h / 2;
      setViewBox();
    }
  }
  selectKeys(keys);
}

export const keysAt = (racks, features) => [...racks.map((i) => S.racks[i]), ...features.map((i) => S.features[i])]
  .filter(Boolean).map(keyOf);

export function viewCenter() {
  return [vb.x + vb.w / 2, vb.y + vb.h / 2];
}

export function addItems(list, target) {
  change(() => target.push(...list));
  selectKeys(list.map(keyOf));
}

function moveSelected(dx, dy) {
  if (!S.sel.size) return;
  change(() => selected().forEach((it) => { it.x = snap(it.x + dx, 0.001); it.y = snap(it.y + dy, 0.001); }));
}

export function rotateSelected(angle) {
  if (S.sel.size) change(() => rotateGroup(selected(), angle));
}

export function deleteSelected() {
  if (!S.sel.size) return;
  change(() => {
    S.racks = S.racks.filter((r) => !S.sel.has(keyOf(r)));
    S.features = S.features.filter((f) => !S.sel.has(keyOf(f)));
  });
  S.sel.clear();
  render();
}

export function duplicateSelected() {
  const items = selected();
  if (!items.length) return;
  const used = new Set(S.racks.map((r) => `${r.zone}|${r.rack_id}`));
  const copies = items.map((it) => {
    const c = { ...JSON.parse(JSON.stringify(strip(it))), id: null, x: it.x + 1, y: it.y + 1 };
    if (c.rack_id !== undefined) {
      let n = parseInt(c.rack_id, 10) || 0;
      do { c.rack_id = String(++n).padStart(Math.max(3, it.rack_id.length), '0'); } while (used.has(`${c.zone}|${c.rack_id}`));
      used.add(`${c.zone}|${c.rack_id}`);
    }
    return c;
  });
  change(() => copies.forEach((c) => (c.rack_id !== undefined ? S.racks : S.features).push(c)));
  selectKeys(copies.map(keyOf));
}

function undo() { const s = history.undo(snapshot()); if (s) restore(s); }
function redo() { const s = history.redo(snapshot()); if (s) restore(s); }

// ── API ────────────────────────────────────────────────────────────────────────────────────
const payload = () => JSON.stringify({ floor: S.floor, racks: S.racks.map(strip), features: S.features.map(strip),
  columns: S.columns, version: S.version,
  underlay: S.underlay && { scale: S.underlay.scale, x: S.underlay.x, y: S.underlay.y, opacity: S.underlay.opacity } });

async function post(url, body, signal) {
  const r = await fetch(url, { method: 'POST', body, signal, credentials: 'same-origin',
    headers: { 'Content-Type': 'application/json', 'X-CSRFToken': CSRF } });
  return [r.status, await r.json().catch(() => ({}))];
}

function applyIssues(issues) {
  S.issues = issues || [];
  S.errK.clear(); S.warnK.clear();
  for (const it of S.issues) {
    const bag = it.severity === 'error' ? S.errK : S.warnK;
    it.racks.forEach((i) => S.racks[i] && bag.add(keyOf(S.racks[i])));
    it.features.forEach((i) => S.features[i] && bag.add(keyOf(S.features[i])));
  }
}

function scheduleCheck() {
  clearTimeout(checkTimer);
  checkTimer = setTimeout(check, 300);
}

async function check() {
  const mine = ++checkSeq;
  checkAbort?.abort();
  checkAbort = new AbortController();
  try {
    const [code, data] = await post(CFG.urls.check, payload(), checkAbort.signal);
    if (mine !== checkSeq) return;                        // w międzyczasie kolejna zmiana
    if (code !== 200) { status(data.error || `Błąd sprawdzania (${code}).`, 'error'); return; }
    S.kpi = data.kpi || {};
    S.colList = data.column_list || [];
    applyIssues(data.issues);
    const e = S.issues.filter((i) => i.severity === 'error').length, w = S.issues.length - e;
    const head = S.dirty ? 'Niezapisane zmiany' : 'Plan zapisany';
    status(e ? `${head} · błędy: ${e}, ostrzeżenia: ${w}${S.dirty ? ' — popraw błędy, aby zapisać' : ''}.`
      : `${head} · bez błędów${w ? `, ostrzeżenia: ${w}` : ''}.`, e ? 'error' : '');
    render();
  } catch (err) {
    if (err.name !== 'AbortError') status('Brak połączenia z serwerem — sprawdzę ponownie po kolejnej zmianie.', 'error');
  }
}

function load(data) {
  Object.assign(S, { floor: data.floor, racks: data.racks, features: data.features, version: data.version,
    kinds: data.feature_kinds || S.kinds, columns: data.columns || {}, colList: data.column_list || [],
    underlay: data.underlay || null, selCol: null, calib: null, dirty: false });
  S.sel.clear();
  history.past = []; history.future = [];
}

async function save() {
  $('le-save').disabled = true;
  status('Zapisuję…');
  try {
    const [code, data] = await post(CFG.urls.save, payload());
    if (code === 200) {
      load(data);
      S.kpi = data.kpi || {};
      applyIssues(data.issues);
      status(`Zapisano ${new Date().toLocaleTimeString('pl-PL')}.`, 'ok');
    } else if (code === 422) {
      applyIssues(data.issues);
      status(data.error || 'Plan ma błędy — popraw je przed zapisem.', 'error');
    } else {
      status(data.error || `Nie zapisano (błąd ${code}).`, 'error');
      if (code === 409) $('le-reload').hidden = false;
    }
  } catch {
    status('Brak połączenia — plan nie został zapisany.', 'error');
  }
  render();
}

async function reload() {
  const r = await fetch(CFG.urls.layout, { credentials: 'same-origin' });
  load(await r.json());
  $('le-reload').hidden = true;
  fit();
  render();
  check();
}

// ── rysowanie ──────────────────────────────────────────────────────────────────────────────
function el(tag, attrs, parent) {
  const e = document.createElementNS(NS, tag);
  for (const [k, v] of Object.entries(attrs)) e.setAttribute(k, v);
  parent?.appendChild(e);
  return e;
}

function setViewBox() {
  svg.setAttribute('viewBox', `${vb.x} ${vb.y} ${vb.w} ${vb.h}`);
}

export function fit() {
  const pad = 3, W = S.floor.width + 2 * pad, D = S.floor.depth + 2 * pad;
  const ratio = (svg.clientWidth || 800) / (svg.clientHeight || 500);
  const w = Math.max(W, D * ratio);
  vb = { x: -pad - (w - W) / 2, y: -pad, w, h: w / ratio };
  setViewBox();
}

function drawItem(g, it, color, label) {
  const [w, d] = it.n_bays !== undefined ? [it.n_bays * it.bay_width_cm / 100, it.depth_cm / 100] : [it.width, it.depth];
  const k = keyOf(it);
  const cls = ['le-item', S.sel.has(k) && 'is-selected', S.errK.has(k) && 'has-error',
    !S.errK.has(k) && S.warnK.has(k) && 'has-warning'].filter(Boolean).join(' ');
  const ig = el('g', { class: cls, transform: svgTransform(it), 'data-k': k }, g);
  el('rect', { width: w, height: d, fill: color, 'fill-opacity': it.n_bays !== undefined ? 0.75 : 0.3, stroke: color }, ig);
  const fs = Math.max(0.25, Math.min(0.7, d * 0.55, w / Math.max(4, label.length) * 1.6));
  el('text', { x: w / 2, y: d / 2, 'font-size': fs, 'text-anchor': 'middle', 'dominant-baseline': 'central' }, ig)
    .textContent = label;
}

export function render() {
  svg.replaceChildren();
  const g = el('g', {}, svg);
  const { width: W, depth: D } = S.floor;
  el('rect', { class: 'le-floor', x: 0, y: 0, width: W, height: D }, g);
  drawUnderlay(g);
  if (vb.w < 160) {                                    // siatka 1 m tylko przy zbliżeniu
    for (let x = 1; x < W; x++) if (x % 5) el('line', { class: 'le-grid-1', x1: x, y1: 0, x2: x, y2: D }, g);
    for (let y = 1; y < D; y++) if (y % 5) el('line', { class: 'le-grid-1', x1: 0, y1: y, x2: W, y2: y }, g);
  }
  const fs = Math.max(0.4, vb.w / 90);
  const lab = [5, 10, 25, 50, 100].find((s) => vb.w / s <= 16) || 200;   // ≤ ~16 opisów na szerokość widoku
  for (let x = 0; x <= W; x += 5) {
    el('line', { class: 'le-grid-5', x1: x, y1: 0, x2: x, y2: D }, g);
    if (x % lab === 0) {
      el('text', { class: 'le-axis', x, y: -fs * 0.6, 'font-size': fs, 'text-anchor': 'middle' }, g).textContent = `${x} m`;
    }
  }
  for (let y = 5; y <= D; y += 5) {
    el('line', { class: 'le-grid-5', x1: 0, y1: y, x2: W, y2: y }, g);
    if (y % lab === 0) {
      el('text', { class: 'le-axis', x: -fs * 0.4, y, 'font-size': fs, 'text-anchor': 'end', 'dominant-baseline': 'central' }, g)
        .textContent = `${y}`;
    }
  }
  // ponytail: pełne przerysowanie przy każdej zmianie — płynne do kilkuset regałów; przy tysiącach
  // aktualizować tylko `transform` przeciąganych grup.
  for (const f of S.features) drawItem(g, f, CFG.featureColors[f.kind] || '#6b7280', f.label || S.kinds[f.kind] || f.kind);
  const colors = zoneColors(S.racks);
  for (const r of S.racks) drawItem(g, r, colors[r.zone], `${r.zone}-${r.rack_id}`);
  drawColumns(g);
  if (drag?.marquee) {
    const [x0, y0, x1, y1] = drag.marquee;
    el('rect', { class: 'le-marquee', x: Math.min(x0, x1), y: Math.min(y0, y1), width: Math.abs(x1 - x0),
      height: Math.abs(y1 - y0) }, svg);
  }
  $('le-save').disabled = !S.dirty || S.errK.size > 0;
  $('le-undo').disabled = !history.past.length;
  $('le-redo').disabled = !history.future.length;
  renderPanels();
  preview3d();
}

// ── mysz / dotyk ───────────────────────────────────────────────────────────────────────────
let drag = null, spaceDown = false;

function world(e) {
  const p = new DOMPoint(e.clientX, e.clientY).matrixTransform(svg.getScreenCTM().inverse());
  return [p.x, p.y];
}

svg.addEventListener('pointerdown', (e) => {
  svg.focus();
  const [wx, wy] = world(e);
  const hit = e.target.closest('.le-item');
  if (e.button === 0 && !spaceDown && hallPointer(e, [wx, wy])) return;   // słup albo punkt kalibracji
  svg.setPointerCapture(e.pointerId);
  if (e.button === 1 || spaceDown) {
    drag = { pan: [e.clientX, e.clientY, vb.x, vb.y] };
    svg.classList.add('is-panning');
  } else if (hit) {
    const k = Number(hit.dataset.k);
    if (e.shiftKey) { S.sel.has(k) ? S.sel.delete(k) : S.sel.add(k); render(); return; }
    if (!S.sel.has(k)) selectKeys([k]);
    const lead = all().find((it) => keyOf(it) === k);
    drag = { start: [wx, wy], lead: [lead.x, lead.y], before: snapshot(), moved: false,
      orig: new Map(selected().map((it) => [it, [it.x, it.y]])) };
  } else {
    drag = { marquee: [wx, wy, wx, wy], add: e.shiftKey };
  }
});

svg.addEventListener('pointermove', (e) => {
  if (!drag) return;
  if (drag.pan) {
    const [cx, cy, x0, y0] = drag.pan, s = vb.w / svg.clientWidth;
    vb.x = x0 - (e.clientX - cx) * s; vb.y = y0 - (e.clientY - cy) * s;
    setViewBox();
    return;
  }
  const [wx, wy] = world(e);
  if (drag.marquee) { drag.marquee[2] = wx; drag.marquee[3] = wy; render(); return; }
  let dx = wx - drag.start[0], dy = wy - drag.start[1];
  if (!e.altKey) { dx = snap(drag.lead[0] + dx) - drag.lead[0]; dy = snap(drag.lead[1] + dy) - drag.lead[1]; }
  if (!drag.moved && Math.hypot(dx, dy) < 0.05) return;
  drag.moved = true;
  for (const [it, [x, y]] of drag.orig) { it.x = snap(x + dx, 0.001); it.y = snap(y + dy, 0.001); }
  render();
});

svg.addEventListener('pointerup', () => {
  if (!drag) return;
  const d = drag;
  drag = null;
  svg.classList.remove('is-panning');
  if (d.marquee) {
    const [x0, y0, x1, y1] = d.marquee;
    const [ax, ay, bx, by] = [Math.min(x0, x1), Math.min(y0, y1), Math.max(x0, x1), Math.max(y0, y1)];
    const inside = all().filter((it) => {
      const [ix, iy, jx, jy] = bbox(corners(it));
      return ix >= ax && iy >= ay && jx <= bx && jy <= by;
    });
    selectKeys(inside.map(keyOf), d.add);
  } else if (d.moved) {
    history.push(d.before);
    touched();
  }
});

svg.addEventListener('dblclick', (e) => {
  const hit = e.target.closest('.le-item');
  const r = hit && S.racks.find((it) => keyOf(it) === Number(hit.dataset.k));
  if (r) selectZone(r.zone);
});

function zoom(f, [cx, cy] = viewCenter()) {
  const w = Math.min(5000, Math.max(5, vb.w * f)), k = w / vb.w;
  vb = { x: cx - (cx - vb.x) * k, y: cy - (cy - vb.y) * k, w, h: vb.h * k };
  setViewBox();
  render();
}

svg.addEventListener('wheel', (e) => { e.preventDefault(); zoom(e.deltaY > 0 ? 1.15 : 1 / 1.15, world(e)); },
  { passive: false });

// ── klawiatura ─────────────────────────────────────────────────────────────────────────────
document.addEventListener('keydown', (e) => {
  if (e.target.closest('input, select, textarea')) return;
  const ctrl = e.ctrlKey || e.metaKey, step = e.shiftKey ? 1 : 0.1, k = e.key.toLowerCase();
  const arrows = { arrowleft: [-step, 0], arrowright: [step, 0], arrowup: [0, -step], arrowdown: [0, step] };
  let handled = true;
  if (k === ' ' && e.target === svg) spaceDown = true;
  else if (arrows[k] && e.target === svg) moveSelected(...arrows[k]);
  else if (ctrl && k === 'z' && !e.shiftKey) undo();
  else if (ctrl && (k === 'y' || (k === 'z' && e.shiftKey))) redo();
  else if (ctrl && k === 'd') duplicateSelected();
  else if (ctrl && k === 'a' && e.target === svg) selectKeys(all().map(keyOf));
  else if (!ctrl && k === 'r' && e.target === svg) rotateSelected(90);
  else if (!ctrl && k === 'f') fullscreen.toggle();
  else if ((k === 'delete' || k === 'backspace') && e.target === svg) deleteSelectedColumn() || deleteSelected();
  else if (k === 'escape') { S.selCol = null; S.calib = null; selectKeys([]); }
  else handled = false;
  if (handled) e.preventDefault();
});
document.addEventListener('keyup', (e) => { if (e.key === ' ') spaceDown = false; });

window.addEventListener('beforeunload', (e) => { if (S.dirty) { e.preventDefault(); e.returnValue = ''; } });

$('le-undo').addEventListener('click', undo);
$('le-redo').addEventListener('click', redo);
$('le-save').addEventListener('click', save);
$('le-reload').addEventListener('click', reload);
$('le-fit').addEventListener('click', () => { fit(); render(); });
$('le-zoomin').addEventListener('click', () => zoom(1 / 1.3));
$('le-zoomout').addEventListener('click', () => zoom(1.3));
initPreview();
// Pełny ekran całego obszaru roboczego; po zmianie plan dopasowuje widok (3D przelicza się przez ResizeObserver).
const fullscreen = bindFullscreenButton($('le-fs'), $('le-work'), { live: $('le-fs-live'),
  onChange: () => requestAnimationFrame(() => { fit(); render(); }) });
reload().catch(() => status('Nie udało się wczytać planu — odśwież stronę.', 'error'));
