import { test } from 'node:test';
import assert from 'node:assert/strict';
import { addPath, heatGrid, heatRGBA } from '../../static/twin/js/traffic-heat.js';

test('siatka pokrywa posadzkę; trasa poza posadzką pomijana', () => {
  const g = heatGrid({ width: 10.5, depth: 4 }, 1);
  assert.deepEqual([g.nx, g.ny], [11, 4]);
  addPath(g, [[2.7, 1.2], [2.1, 1.9]]);
  addPath(g, [[-3, 1], [-0.1, 1]]);
  addPath(g, [[11, 1], [12, 1]]);
  assert.equal(g.v[1 * 11 + 2], 1);
  assert.equal(g.v.reduce((a, b) => a + b, 0), 1);
});

test('RGBA: maksimum = czerwone i najbardziej kryjące, 1 przejazd słabiej, pusto = przezroczyste', () => {
  const g = heatGrid({ width: 3, depth: 1 });
  addPath(g, [[1.5, 0.5], [1.6, 0.5]]);
  for (let k = 0; k < 100; k++) addPath(g, [[2.5, 0.5], [2.6, 0.5]]);
  const px = heatRGBA(g);
  assert.equal(px[3], 0);
  assert.deepEqual([...px.slice(8, 12)], [220, 38, 38, 220]);
  assert.ok(px[7] > 70 && px[7] < 220);
});

test('pusta siatka → całość przezroczysta', () => {
  assert.ok(heatRGBA(heatGrid({ width: 2, depth: 2 })).every((x) => x === 0));
});

test('trasa: każda komórka po drodze raz na przejazd (także narożnik „L”), dwa przejazdy = 2', () => {
  const g = heatGrid({ width: 5, depth: 5 });
  addPath(g, [[0.5, 0.5], [3.5, 0.5], [3.5, 2.5]]);
  addPath(g, [[0.5, 0.5], [3.5, 0.5]]);
  assert.deepEqual([...g.v.slice(0, 5)], [2, 2, 2, 2, 0]);    // wiersz y=0: narożnik [3,0] raz z każdego przejazdu
  assert.deepEqual([g.v[1 * 5 + 3], g.v[2 * 5 + 3], g.v[1 * 5 + 2]], [1, 1, 0]);
});
