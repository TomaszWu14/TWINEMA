// Czyste funkcje edytora layoutu. Uruchamia twin/tests/test_layout_editor_js.py (`node --test`).
import assert from 'node:assert/strict';
import test from 'node:test';

import { History, corners, makeBlock, mode, nextRackIds, rotateGroup, snap, svgTransform, zoneColors }
  from '../../static/twin/js/layout-core.js';

const near = (a, b) => assert.ok(Math.abs(a - b) < 1e-9, `${a} ≈ ${b}`);
const rack = (o) => ({ zone: 'A', rack_id: '001', x: 0, y: 0, angle: 0, n_bays: 4, n_levels: 3,
  bay_width_cm: 270, depth_cm: 110, level_height_cm: 180, ...o });

test('narożniki: 90° obraca szerokość w −y (jak blender_route.rack_axes)', () => {
  const c = corners(rack({ x: 10, y: 20, angle: 90 }));
  near(c[1][0], 10); near(c[1][1], 20 - 10.8);           // szerokość 4 × 2,7 m
  near(c[3][0], 10 + 1.1); near(c[3][1], 20);
});

test('SVG: rotate(−θ) — ta sama oś szerokości co w hali', () => {
  assert.equal(svgTransform({ x: 1, y: 2, angle: 30 }), 'translate(1 2) rotate(-30)');
});

test('przyciąganie do 0,1 m', () => {
  assert.equal(snap(1.04), 1);
  assert.equal(snap(1.06), 1.1);
  assert.equal(snap(-0.26), -0.3);
});

test('obrót grupy o 90° dwa razy = 180°, środek obrysu bez zmian', () => {
  const items = [rack({ x: 0, y: 0 }), rack({ x: 0, y: 3, rack_id: '002' })];
  rotateGroup(items, 90);
  rotateGroup(items, 90);
  assert.deepEqual(items.map((r) => r.angle), [180, 180]);
  const xs = items.flatMap(corners).map((p) => p[0]);
  near(Math.min(...xs), 0); near(Math.max(...xs), 10.8);
});

test('kolory stref alfabetycznie jak w widoku 3D', () => {
  assert.deepEqual(zoneColors([{ zone: 'K' }, { zone: 'B' }]), { B: '#3b82f6', K: '#10b981' });
});

test('kolejne numery regałów w strefie z wiodącymi zerami', () => {
  const racks = [rack({ rack_id: '001' }), rack({ rack_id: '007' }), rack({ zone: 'B', rack_id: '050' })];
  assert.deepEqual(nextRackIds(racks, 'A', 2), ['008', '009']);
  assert.deepEqual(nextRackIds(racks, 'Z', 1), ['001']);
});

test('blok: pary plecami (szczelina z konfiguracji), alejka między parami, drugi w parze obrócony', () => {
  const b = makeBlock({ x: 2, y: 5, rows: 3, bays: 10, levels: 5, bayWidthCm: 270, depthCm: 110,
    levelHeightCm: 180, aisle: 3, zone: 'V', ids: ['001', '002', '003'], backGap: 0.2 });
  assert.deepEqual(b.map((r) => r.angle), [0, 180, 0]);
  near(b[1].x, 2 + 27); near(b[1].y, 5 + 1.1 + 0.2 + 1.1);
  near(b[2].y, 5 + 1.1 + 0.2 + 1.1 + 3);
});

test('historia: cofnij i ponów, nowa zmiana czyści ponów', () => {
  const h = new History(2);
  h.push('a'); h.push('b'); h.push('c');
  assert.equal(h.past.length, 2);                         // limit
  assert.equal(h.undo('d'), 'c');
  assert.equal(h.redo('c'), 'd');
  h.undo('d'); h.push('e');
  assert.equal(h.redo('x'), null);
});

test('wartość najczęstsza', () => {
  assert.equal(mode([270, 270, 180], 100), 270);
  assert.equal(mode([], 100), 100);
});
