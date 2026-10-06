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

test('G4: trasa wózka w hali omija regały (także obrócone), wynik z pamięci podręcznej', async () => {
  const { hallRouter } = await import('../../static/twin/js/site-route.js');
  const floor = { width: 40, depth: 30 };
  // ściana regałów w poprzek hali z przejściem przy górnej krawędzi; drugi regał obrócony o 90°
  const racks = [{ x: 18, y: 0, width: 2, depth: 24, angle: 0 }, { x: 28, y: 20, width: 8, depth: 1.2, angle: 90 }];
  const inRack = ([x, y]) => racks.some((r) => {
    const t = (r.angle * Math.PI) / 180, dx = x - r.x, dy = y - r.y;
    const u = dx * Math.cos(t) - dy * Math.sin(t), v = dx * Math.sin(t) + dy * Math.cos(t);
    return u > 0 && u < r.width && v > 0 && v < r.depth;
  });
  const route = hallRouter(racks, floor);
  const p = route([5, 5], [35, 5]);
  assert.ok(p && p.length > 2, 'objazd zamiast prostej');
  assert.ok(sampled(p, (q) => !inRack(q)));
  assert.ok(Math.max(...p.map((q) => q[1])) > 24);                 // przez przejście przy górnej ścianie
  assert.equal(route([5, 5], [35, 5]), p);                          // ta sama tablica z pamięci
  assert.deepEqual(hallRouter([], floor)([5, 5], [35, 5]), [[5, 5], [35, 5]]);
});
