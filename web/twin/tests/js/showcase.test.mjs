// P1 — prezentacja 3D: przelot kamery, nawigacja, karty KPI, kolejność, kadry. `node --test`.
import assert from 'node:assert/strict';
import test from 'node:test';

import { camAt } from '../../static/twin/js/scene-data.js';
import { docksCam, moveItem, navigate, pickCards, siteBox, slideSeconds, zoneKeys } from '../../static/twin/js/showcase-core.js';

const near = (a, b) => a.every((x, i) => Math.abs(x - b[i]) < 1e-9);

test('camAt: końce przelotu, połowa drogi, łagodny start (smoothstep), clamp poza [0,1]', () => {
  const a = { pos: [0, 10, 0], target: [0, 0, 0] }, b = { pos: [100, 50, -20], target: [10, 0, 10] };
  assert.ok(near(camAt(a, b, 0).pos, a.pos) && near(camAt(a, b, 1).target, b.target));
  assert.ok(near(camAt(a, b, 0.5).pos, [50, 30, -10]));                       // symetria smoothstep
  assert.ok(camAt(a, b, 0.1).pos[0] < 10, 'start wolniej niż liniowo');
  assert.ok(near(camAt(a, b, 2).pos, b.pos) && near(camAt(a, b, -1).pos, a.pos));
});

test('navigate: dalej/wstecz z ograniczeniem, skok, początek, koniec, pusta lista', () => {
  assert.equal(navigate(0, 5, 'next'), 1);
  assert.equal(navigate(4, 5, 'next'), 4);
  assert.equal(navigate(0, 5, 'prev'), 0);
  assert.equal(navigate(2, 5, 'first'), 0);
  assert.equal(navigate(2, 5, 'last'), 4);
  assert.equal(navigate(1, 5, 3), 3);
  assert.equal(navigate(1, 5, 99), 4);
  assert.equal(navigate(1, 5, 'bzdura'), 1);
  assert.equal(navigate(0, 0, 'next'), 0);
});

test('pickCards: kolejność z slajdu, brakujące karty (np. bez działki) pominięte', () => {
  const cards = { throughput: { title: 'P', rows: [] }, capacity: { title: 'C', rows: [] } };
  assert.deepEqual(pickCards(cards, ['capacity', 'site', 'throughput']).map((c) => c.key), ['capacity', 'throughput']);
  assert.deepEqual(pickCards(null, ['capacity']), []);
});

test('moveItem: przeniesienie bez mutacji oryginału, granice', () => {
  const l = ['a', 'b', 'c', 'd'];
  assert.deepEqual(moveItem(l, 0, 2), ['b', 'c', 'a', 'd']);
  assert.deepEqual(moveItem(l, 3, 0), ['d', 'a', 'b', 'c']);
  assert.deepEqual(moveItem(l, 1, -5), ['b', 'a', 'c', 'd']);
  assert.deepEqual(moveItem(l, 9, 0), l);
  assert.deepEqual(l, ['a', 'b', 'c', 'd']);
});

test('slideSeconds: animacja trwa czas dnia ÷ prędkość (nie krócej niż bazowy), reszta bazowy', () => {
  assert.equal(slideSeconds({ type: 'anim', t0: 0, t1: 3600, speed: 60 }, 8), 60);
  assert.equal(slideSeconds({ type: 'anim', t0: 0, t1: 600, speed: 300 }, 8), 8);
  assert.equal(slideSeconds({ type: 'camera' }, 5), 5);
});

test('docksCam: kadr z zewnątrz doków przyjęć, cel w hali; bez doków null', () => {
  const docks = { 1: { role: 'out', out: [1, 0], wall: [80, 10] },
    2: { role: 'in_container', out: [0, 1], wall: [10, 50] }, 3: { role: 'in_pallet', out: [0, 1], wall: [20, 50] } };
  const c = docksCam(docks);
  assert.ok(c.pos[2] > 50 && c.target[2] < 50, 'kamera przed ścianą doków przyjęć (y>50), cel w hali');
  assert.ok(c.pos[1] > 0);
  assert.equal(docksCam({}), null);
});

test('siteBox: obrys działki w układzie hali (hala przesunięta na działce); bez działki null', () => {
  const b = siteBox({ width: 200, depth: 100, hall: { x: 50, y: 20, angle: 0 } });
  assert.ok(near([b.cx, b.cz, b.x, b.z], [50, 30, 200, 100]));
  assert.equal(siteBox({}), null);
});

test('zoneKeys: klucze regałów strefy', () => {
  const racks = [{ zone: 'V', _k: 'r0' }, { zone: 'K', _k: 'r1' }, { zone: 'V', _k: 'r2' }];
  assert.deepEqual(zoneKeys(racks, 'V'), ['r0', 'r2']);
});
