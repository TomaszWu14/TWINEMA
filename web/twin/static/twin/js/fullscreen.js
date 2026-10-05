// Tryb pełnoekranowy — wspólny dla edytora layoutu, widoku 3D / planu 2D modelu (a później trybu prezentacji
// i wykresów scenariusza). Fullscreen API, a gdy niedostępne (iframe, Safari iOS) albo odrzucone —
// „pseudo-pełny ekran”: klasa `is-pseudo-fs` (position:fixed; inset:0) + wyjście Esc.
// Logika bez DOM-owych założeń poza el/doc → testowana `node --test` (twin/tests/js/fullscreen.test.mjs).

export const PSEUDO_CLASS = 'is-pseudo-fs';
const PSEUDO_CSS = `.${PSEUDO_CLASS}{position:fixed!important;inset:0!important;z-index:1000!important;margin:0!important;
max-width:none!important;width:auto!important;height:auto!important;overflow:auto;background:var(--bg,#0b0f14)}`;

function ensureStyle(doc) {
  if (!doc.head || doc.getElementById?.('tw-pseudo-fs-css')) return;
  const s = doc.createElement('style');
  s.id = 'tw-pseudo-fs-css';
  s.textContent = PSEUDO_CSS;
  doc.head.appendChild(s);
}

/** Kontroler pełnego ekranu dla elementu `el`. onChange(aktywny) po każdej zmianie (też Esc / systemowe wyjście). */
export function fullscreenController(el, { doc = globalThis.document, onChange = () => {} } = {}) {
  let pseudo = false;
  const native = () => typeof el.requestFullscreen === 'function' && doc.fullscreenEnabled !== false;
  const active = () => pseudo || doc.fullscreenElement === el;
  const notify = () => onChange(active());

  function onKey(e) { if (e.key === 'Escape' && pseudo) { e.preventDefault(); exit(); } }
  function setPseudo(on) {
    if (on) ensureStyle(doc);
    pseudo = on;
    el.classList.toggle(PSEUDO_CLASS, on);
    doc[on ? 'addEventListener' : 'removeEventListener']('keydown', onKey);
    notify();
  }

  async function enter() {
    if (active()) return;
    if (native()) {
      try { await el.requestFullscreen(); return; } catch { /* odrzucone (np. iframe bez allowfullscreen) → pseudo */ }
    }
    setPseudo(true);
  }
  async function exit() {
    if (pseudo) { setPseudo(false); return; }
    if (doc.fullscreenElement === el && typeof doc.exitFullscreen === 'function') await doc.exitFullscreen();
  }
  const toggle = () => (active() ? exit() : enter());

  doc.addEventListener?.('fullscreenchange', notify);
  return { enter, exit, toggle, active };
}

/** Przycisk przełączający: aria-pressed, etykieta, komunikat aria-live; focus zostaje w obszarze. */
export function bindFullscreenButton(button, el, { live = null, onChange = () => {}, doc = globalThis.document,
  labels = ['Pełny ekran', 'Zamknij pełny ekran'] } = {}) {
  const fs = fullscreenController(el, { doc, onChange: (on) => {
    button.setAttribute('aria-pressed', String(on));
    button.textContent = labels[on ? 1 : 0];
    if (live) live.textContent = on ? 'Tryb pełnoekranowy włączony.' : 'Tryb pełnoekranowy wyłączony.';
    if (on && !el.contains(doc.activeElement)) button.focus();
    onChange(on);
  } });
  button.setAttribute('aria-pressed', 'false');
  button.addEventListener('click', () => fs.toggle());
  return fs;
}
