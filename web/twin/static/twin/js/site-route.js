// Trasy aut po działce (D3) — czyste funkcje (bez three.js i DOM), testowane `node --test` (tests/js/route.test.mjs).
// Układ HALI (jak scene-data.sitePlan): siatka co CELL_M, przejezdne = w granicy działki, poza halą, poza zielenią
// i parkingiem, a gdy narysowano drogi/place — tylko po nich (ta sama reguła co twin/site.py `_dock_issues.ok`).
// A* po 8 sąsiadach, potem wygładzenie „widać bez przeszkód”. Brak trasy → null (animacja jedzie odcinkiem prostym).
export const CELL_M = 2;
const SQRT2 = Math.SQRT2;

export function inPolygon(pts, [x, y]) {
  let inside = false;
  for (let i = 0, j = pts.length - 1; i < pts.length; j = i++) {
    const [xi, yi] = pts[i], [xj, yj] = pts[j];
    if ((yi > y) !== (yj > y) && x < xi + ((y - yi) * (xj - xi)) / (yj - yi)) inside = !inside;
  }
  return inside;
}

/** Predykat przejezdności punktu hali dla planu działki i podłogi hali. */
export function walkable(plan, floor) {
  const blocked = plan.areas.filter((a) => a.kind === 'green' || a.kind === 'parking').map((a) => a.pts);
  const paved = plan.areas.filter((a) => a.kind === 'yard' || a.kind === 'road').map((a) => a.pts);
  const inHall = ([x, y]) => x > 0.01 && y > 0.01 && x < floor.width - 0.01 && y < floor.depth - 0.01;
  return (p) => inPolygon(plan.plot, p) && !inHall(p) && !blocked.some((b) => inPolygon(b, p))
    && (!paved.length || paved.some((r) => inPolygon(r, p)));
}

function grid(plan) {
  const xs = plan.plot.map((p) => p[0]), ys = plan.plot.map((p) => p[1]);
  const x0 = Math.min(...xs), y0 = Math.min(...ys);
  return { x0, y0, nx: Math.ceil((Math.max(...xs) - x0) / CELL_M) + 1, ny: Math.ceil((Math.max(...ys) - y0) / CELL_M) + 1 };
}

/** Trasa a → b (punkty hali) po przejezdnym terenie: [a, …, b] albo null. */
export function routePath(plan, floor, a, b) {
  const ok = walkable(plan, floor), g = grid(plan), N = g.nx * g.ny;
  const at = (i) => [g.x0 + (i % g.nx) * CELL_M, g.y0 + Math.floor(i / g.nx) * CELL_M];
  const free = new Uint8Array(N);
  for (let i = 0; i < N; i++) free[i] = ok(at(i)) ? 1 : 0;
  const cellOf = ([x, y]) => {                         // najbliższa wolna komórka (punkt bywa na granicy / w bramie)
    const cx = Math.round((x - g.x0) / CELL_M), cy = Math.round((y - g.y0) / CELL_M);
    let best = -1, bd = Infinity;
    for (let r = 0; r <= 6 && best < 0; r++) {
      for (let dy = -r; dy <= r; dy++) {
        for (let dx = -r; dx <= r; dx++) {
          const ix = cx + dx, iy = cy + dy;
          if (ix < 0 || iy < 0 || ix >= g.nx || iy >= g.ny || !free[iy * g.nx + ix]) continue;
          const d = dx * dx + dy * dy;
          if (d < bd) { bd = d; best = iy * g.nx + ix; }
        }
      }
    }
    return best;
  };
  const s = cellOf(a), t = cellOf(b);
  if (s < 0 || t < 0) return null;
  const gScore = new Float64Array(N).fill(Infinity), from = new Int32Array(N).fill(-1), closed = new Uint8Array(N);
  const [tx, ty] = [t % g.nx, Math.floor(t / g.nx)];
  const h = (i) => Math.hypot((i % g.nx) - tx, Math.floor(i / g.nx) - ty);
  const open = [[h(s), s]];
  gScore[s] = 0;
  // ponytail: kolejka priorytetowa jako tablica sortowana wstawianiem — wystarcza dla siatki ~30 tys. komórek
  // (jedna trasa na dok przy wczytaniu); kopiec binarny, gdy działki zaczną mieć setki tysięcy komórek.
  while (open.length) {
    const [, i] = open.shift();
    if (i === t) break;
    if (closed[i]) continue;
    closed[i] = 1;
    const ix = i % g.nx, iy = Math.floor(i / g.nx);
    for (let dy = -1; dy <= 1; dy++) {
      for (let dx = -1; dx <= 1; dx++) {
        if (!dx && !dy) continue;
        const jx = ix + dx, jy = iy + dy, j = jy * g.nx + jx;
        if (jx < 0 || jy < 0 || jx >= g.nx || jy >= g.ny || !free[j] || closed[j]) continue;
        if (dx && dy && (!free[iy * g.nx + jx] || !free[jy * g.nx + ix])) continue;   // bez ścinania narożników
        const ng = gScore[i] + (dx && dy ? SQRT2 : 1);
        if (ng >= gScore[j]) continue;
        gScore[j] = ng; from[j] = i;
        const f = ng + h(j);
        let k = open.length;
        while (k > 0 && open[k - 1][0] > f) k--;
        open.splice(k, 0, [f, j]);
      }
    }
  }
  if (from[t] < 0 && s !== t) return null;
  const cells = [];
  for (let i = t; i >= 0; i = i === s ? -1 : from[i]) cells.push(at(i));
  return smooth([a, ...cells.reverse(), b], ok);
}

/** Wygładzenie: z każdego punktu skok do najdalszego widocznego (odcinek próbkowany co 1 m po terenie). */
export function smooth(pts, ok) {
  const clear = (p, q) => {
    const n = Math.max(1, Math.ceil(Math.hypot(q[0] - p[0], q[1] - p[1])));
    for (let k = 1; k < n; k++) if (!ok([p[0] + ((q[0] - p[0]) * k) / n, p[1] + ((q[1] - p[1]) * k) / n])) return false;
    return true;
  };
  const out = [pts[0]];
  let i = 0;
  while (i < pts.length - 1) {
    let j = pts.length - 1;
    while (j > i + 1 && !clear(pts[i], pts[j])) j--;
    out.push(pts[j]);
    i = j;
  }
  return out;
}

/** Punkt i kierunek na łamanej w ułamku p długości → {x, y, yaw} (yaw jak w day-timeline: atan2(−dy, dx)). */
export function alongPath(pts, p) {
  const seg = pts.slice(1).map((q, i) => Math.hypot(q[0] - pts[i][0], q[1] - pts[i][1]));
  let left = Math.max(0, Math.min(1, p)) * seg.reduce((s, v) => s + v, 0);
  for (let i = 0; i < seg.length; i++) {
    const [a, b] = [pts[i], pts[i + 1]];
    if (left <= seg[i] || i === seg.length - 1) {
      const k = seg[i] ? Math.min(1, left / seg[i]) : 0;
      return { x: a[0] + (b[0] - a[0]) * k, y: a[1] + (b[1] - a[1]) * k, yaw: Math.atan2(-(b[1] - a[1]), b[0] - a[0]) };
    }
    left -= seg[i];
  }
  return { x: pts[0][0], y: pts[0][1], yaw: 0 };
}
