// Przełącznik pełnego ekranu (fullscreen.js): Fullscreen API i obejście CSS. Uruchamia
// twin/tests/test_layout_editor_js.py (`node --test`).
import assert from 'node:assert/strict';
import test from 'node:test';

import { PSEUDO_CLASS, bindFullscreenButton, fullscreenController } from '../../static/twin/js/fullscreen.js';

function fakeDoc({ enabled = true } = {}) {
  const listeners = {};
  return {
    fullscreenEnabled: enabled, fullscreenElement: null, activeElement: null,
    addEventListener(t, f) { (listeners[t] ||= new Set()).add(f); },
    removeEventListener(t, f) { listeners[t]?.delete(f); },
    fire(t, e = {}) { [...(listeners[t] || [])].forEach((f) => f({ preventDefault() {}, ...e })); },
    has(t) { return (listeners[t]?.size || 0) > 0; },
    async exitFullscreen() { this.fullscreenElement = null; this.fire('fullscreenchange'); },
  };
}
function fakeEl(doc, { native = true, reject = false } = {}) {
  const cls = new Set();
  return {
    classList: { toggle: (c, on) => (on ? cls.add(c) : cls.delete(c)), contains: (c) => cls.has(c) },
    contains: () => false,
    ...(native && { async requestFullscreen() {
      if (reject) throw new Error('denied');
      doc.fullscreenElement = this; doc.fire('fullscreenchange');
    } }),
  };
}

test('Fullscreen API: wejście/wyjście, onChange przy każdej zmianie (także systemowe Esc)', async () => {
  const doc = fakeDoc(), el = fakeEl(doc), seen = [];
  const fs = fullscreenController(el, { doc, onChange: (on) => seen.push(on) });
  await fs.toggle();
  assert.equal(fs.active(), true);
  assert.equal(el.classList.contains(PSEUDO_CLASS), false);   // natywnie — bez klasy obejścia
  doc.fullscreenElement = null; doc.fire('fullscreenchange');  // Esc obsłużone przez przeglądarkę
  assert.deepEqual(seen, [true, false]);
  assert.equal(fs.active(), false);
});

test('brak Fullscreen API (iOS) → pseudo-pełny ekran, Esc wychodzi i zdejmuje nasłuch', async () => {
  const doc = fakeDoc({ enabled: false }), el = fakeEl(doc, { native: false }), seen = [];
  const fs = fullscreenController(el, { doc, onChange: (on) => seen.push(on) });
  await fs.enter();
  assert.equal(el.classList.contains(PSEUDO_CLASS), true);
  assert.equal(doc.has('keydown'), true);
  doc.fire('keydown', { key: 'Escape' });
  assert.equal(fs.active(), false);
  assert.equal(el.classList.contains(PSEUDO_CLASS), false);
  assert.equal(doc.has('keydown'), false);
  assert.deepEqual(seen, [true, false]);
});

test('odrzucone requestFullscreen (iframe) → obejście CSS zamiast błędu', async () => {
  const doc = fakeDoc(), el = fakeEl(doc, { reject: true });
  const fs = fullscreenController(el, { doc });
  await fs.toggle();
  assert.equal(el.classList.contains(PSEUDO_CLASS), true);
  await fs.toggle();
  assert.equal(fs.active(), false);
});

test('przycisk: aria-pressed, etykieta i komunikat aria-live', async () => {
  const doc = fakeDoc({ enabled: false }), el = fakeEl(doc, { native: false });
  const attrs = {}, handlers = {};
  const button = { textContent: '', focus() {}, setAttribute: (k, v) => { attrs[k] = v; },
    addEventListener: (t, f) => { handlers[t] = f; } };
  const live = { textContent: '' };
  bindFullscreenButton(button, el, { doc, live });
  assert.equal(attrs['aria-pressed'], 'false');
  await handlers.click();
  assert.deepEqual([attrs['aria-pressed'], button.textContent, live.textContent],
    ['true', 'Zamknij pełny ekran', 'Tryb pełnoekranowy włączony.']);
  await handlers.click();
  assert.equal(live.textContent, 'Tryb pełnoekranowy wyłączony.');
});
