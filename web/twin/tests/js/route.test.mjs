// D3: trasy aut po działce — omijanie zieleni i hali, brak przejazdu, punkt na łamanej.
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { alongPath, routePath, walkable } from '../../static/twin/js/site-route.js';

const rect = (x, y, w, d) => [[x, y], [x + w, y], [x + w, y + d], [x, y + d]];
const FLOOR = { width: 40, depth: 20 };
// Działka wokół hali (hala = [0,40]×[0,20] w układzie hali); pas zieleni na wprost od wjazdu do doku.
const PLAN = { plot: rect(-30, -30, 100, 80), entries: [],
  areas: [{ kind: 'green', pts: rect(-30, 30, 60, 6) }] };
const ENTRY = [0, 49], DOCK_LANE = [-6, 25];               // wjazd od dołu planu, pas przed dokiem zachodnim

function sampled(path, ok) {
  for (let i = 1; i < path.length; i++) {
    const [a, b] = [path[i - 1], path[i]], n = Math.ceil(Math.hypot(b[0] - a[0], b[1] - a[1]));
    for (let k = 1; k < n; k++) if (!ok([a[0] + ((b[0] - a[0]) * k) / n, a[1] + ((b[1] - a[1]) * k) / n])) return false;
  }
  return true;
}

test('trasa omija pas zieleni i halę (prosta linia przecina zieleń)', () => {
  const ok = walkable(PLAN, FLOOR);
  assert.equal(ok([0, 33]), false);                       // zieleń na wprost
  const path = routePath(PLAN, FLOOR, ENTRY, DOCK_LANE);
  assert.ok(path && path.length >= 3, 'trasa z objazdem');
  assert.deepEqual(path[0], ENTRY);
  assert.deepEqual(path[path.length - 1], DOCK_LANE);
  assert.ok(sampled(path.slice(1, -1), ok), 'środek trasy po przejezdnym terenie');
  assert.ok(path.some(([x]) => x >= 30), 'objazd prawą stroną pasa zieleni (lewą blokuje granica)');
});

test('drogi/place narysowane — jazda tylko po nich', () => {
  // droga wzdłuż dołu planu i plac przy ścianie zachodniej; zieleń poza nimi (między drogą a halą)
  const plan = { ...PLAN, areas: [{ kind: 'green', pts: rect(0, 30, 30, 6) }, { kind: 'road', pts: rect(-30, 36, 100, 14) },
    { kind: 'yard', pts: rect(-30, -30, 30, 66) }] };
  const ok = walkable(plan, FLOOR);
  assert.equal(ok([20, 25]), false);                      // trawa poza drogami
  const path = routePath(plan, FLOOR, ENTRY, DOCK_LANE);
  assert.ok(path && sampled(path.slice(1, -1), ok));
});

test('brak przejazdu → null (animacja jedzie wtedy odcinkiem prostym)', () => {
  const walled = { ...PLAN, areas: [{ kind: 'green', pts: rect(-30, 30, 100, 6) }] };
  assert.equal(routePath(walled, FLOOR, ENTRY, DOCK_LANE), null);
});

test('alongPath: końce, połowa długości, kierunek odcinka', () => {
  const pts = [[0, 0], [10, 0], [10, 10]];
  assert.deepEqual(alongPath(pts, 0), { x: 0, y: 0, yaw: -0 });
  const mid = alongPath(pts, 0.5);
  assert.deepEqual([mid.x, mid.y], [10, 0]);
  const end = alongPath(pts, 1);
  assert.deepEqual([end.x, end.y], [10, 10]);
  assert.ok(Math.abs(alongPath(pts, 0.75).yaw + Math.PI / 2) < 1e-9);   // w dół planu (+y) = yaw −π/2
});
