// Edytor layoutu — podgląd 3D obok planu (E3): ta sama scena co widok modelu (scene-builder.js),
// budowana ze stanu edytora. Przebudowa 300 ms po ostatniej zmianie danych; zaznaczenie podświetla od razu.
// Viewer tworzony leniwie przy pierwszym pokazaniu panelu 3D (tryb „2D” nie płaci za WebGL).
import { S } from './layout-editor.js';
import { editorScene } from './scene-data.js';

const $ = (id) => document.getElementById(id);
const CFG = JSON.parse($('le-config').textContent);
const MODES = ['2d', 'split', '3d'];
const MODE_KEY = 'twinema.le.mode';
const stage = $('le-stage');
let viewer = null, loading = false, timer = null, lastData = '', lastSel = '', framed = false;

function createViewer() {
  if (window.__tw3dNoWebGL) { window.tw3dFail('Przeglądarka nie obsługuje grafiki 3D (WebGL) — plan 2D działa bez niej.'); return; }
  loading = true;
  import('./scene-builder.js').then(({ createViewer: create }) => {
    // ponytail: numery regałów i etykiety wyłączone > 400 regałów (tysiące sprite'ów przy każdej przebudowie).
    viewer = create({ canvas: $('le-3d-canvas'), wrap: $('le-3d-wrap'), fill: false, labels: S.racks.length <= 400 });
    window.tw3dReady();
    sync(true);
  }).catch((err) => { console.error(err); window.tw3dFail('Nie udało się załadować podglądu 3D.'); });
}

/** Przebudowa sceny, gdy zmieniły się dane (nie samo zaznaczenie); potem podświetlenie zaznaczenia. */
function sync(now = false) {
  const data = JSON.stringify([S.floor, S.racks, S.features, S.colList]);
  if (data !== lastData) {
    if (!now) { clearTimeout(timer); timer = setTimeout(() => sync(true), 300); return; }
    lastData = data;
    const ms = viewer.setData(editorScene(S, CFG.featureColors), { frame: !framed && S.racks.length > 0 });
    framed ||= S.racks.length > 0;
    $('le-3d-wrap').dataset.buildMs = Math.round(ms);   // diagnostyka: czas przebudowy sceny [ms]
    lastSel = null;
  }
  const sel = [...S.sel].join(',');
  if (sel !== lastSel) { lastSel = sel; viewer.highlight([...S.sel]); }
}

/** Wołane z render() edytora (po każdej zmianie) — gdy panel 3D widoczny: odroczona synchronizacja. */
export function preview3d() {
  if (stage.dataset.mode === '2d' || !S.version) return;     // ukryty albo plan jeszcze niewczytany
  if (viewer) sync();
  else if (!loading) createViewer();
}

function setMode(mode) {
  stage.dataset.mode = mode;
  document.querySelectorAll('[data-le-mode]').forEach((b) => b.setAttribute('aria-pressed', String(b.dataset.leMode === mode)));
  try { localStorage.setItem(MODE_KEY, mode); } catch { /* prywatne okno — tryb tylko na tę wizytę */ }
  viewer?.resize();
  preview3d();
}

/** Start po inicjalizacji edytora (import cykliczny: przy ewaluacji tego modułu `S` jeszcze nie istnieje). */
export function initPreview() {
  document.querySelectorAll('[data-le-mode]').forEach((b) => b.addEventListener('click', () => setMode(b.dataset.leMode)));
  $('le-3d-top').addEventListener('click', () => viewer?.view('top'));
  $('le-3d-iso').addEventListener('click', () => viewer?.view('iso'));
  $('le-3d-sel').addEventListener('click', () => viewer?.view('sel'));
  let saved = null;
  try { saved = localStorage.getItem(MODE_KEY); } catch { /* jw. */ }
  setMode(MODES.includes(saved) ? saved : (window.innerWidth >= 1400 ? 'split' : '2d'));
}
