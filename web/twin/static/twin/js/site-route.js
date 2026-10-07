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

/** Trasa a → b (punkty hali) po przejezdnym terenie działki: [a, …, b] albo null. */
export function routePath(plan, floor, a, b) {
  const xs = plan.plot.map((p) => p[0]), ys = plan.plot.map((p) => p[1]);
  return gridRoute(walkable(plan, floor), [Math.min(...xs), Math.min(...ys), Math.max(...xs), Math.max(...ys)], CELL_M, a, b);
}

/** G4: trasy wózków w hali — po posadzce, z ominięciem rzutów regałów (z zapasem `pad` m); wyniki w pamięci
 *  podręcznej per para punktów (te same miejsca odkładcze i fronty regałów powtarzają się przez cały dzień).
 *  → route(a, b) = [a, …, b] albo null (wtedy przejazd w L jak dotąd). */
export function hallRouter(racks, floor, { cell = 1, pad = 0.3 } = {}) {
  const nx = Math.ceil(floor.width / cell) + 1, ny = Math.ceil(floor.depth / cell) + 1;
  const blocked = new Uint8Array(nx * ny);
  for (const r of racks) {                              // rasteryzacja obróconego prostokąta regału
    const t = ((r.angle || 0) * Math.PI) / 180, c = Math.cos(t), sn = Math.sin(t);
    const corners = [[0, 0], [r.width, 0], [0, r.depth], [r.width, r.depth]]
      .map(([u, v]) => [r.x + u * c + v * sn, r.y - u * sn + v * c]);
    const [x0, x1] = [Math.min(...corners.map((q) => q[0])) - pad, Math.max(...corners.map((q) => q[0])) + pad];
    const [y0, y1] = [Math.min(...corners.map((q) => q[1])) - pad, Math.max(...corners.map((q) => q[1])) + pad];
    for (let iy = Math.max(0, Math.floor(y0 / cell)); iy <= Math.min(ny - 1, Math.ceil(y1 / cell)); iy++) {
      for (let ix = Math.max(0, Math.floor(x0 / cell)); ix <= Math.min(nx - 1, Math.ceil(x1 / cell)); ix++) {
        const dx = ix * cell - r.x, dy = iy * cell - r.y, u = dx * c - dy * sn, v = dx * sn + dy * c;
        if (u >= -pad && u <= r.width + pad && v >= -pad && v <= r.depth + pad) blocked[iy * nx + ix] = 1;
      }
    }
  }
  const ok = ([x, y]) => {
    const ix = Math.round(x / cell), iy = Math.round(y / cell);
    return x >= 0 && y >= 0 && x <= floor.width && y <= floor.depth && !blocked[iy * nx + ix];
  };
  const cache = new Map();
  let free = null;                                      // siatka wolnych pól liczona raz (trasa na każdą paletę, G9)
  return (a, b) => {
    const key = `${a[0].toFixed(1)},${a[1].toFixed(1)}>${b[0].toFixed(1)},${b[1].toFixed(1)}`;
    free ??= freeCells(ok, [0, 0, floor.width, floor.depth], cell);
    if (!cache.has(key)) cache.set(key, gridRoute(ok, [0, 0, floor.width, floor.depth], cell, a, b, free));
    return cache.get(key);
  };
}

/** Wolne pola siatki `cell` w prostokącie (1 = `ok`) — ten sam układ co w gridRoute. */
export function freeCells(ok, [bx0, by0, bx1, by1], cell) {
  const nx = Math.ceil((bx1 - bx0) / cell) + 1, ny = Math.ceil((by1 - by0) / cell) + 1, free = new Uint8Array(nx * ny);
  for (let i = 0; i < nx * ny; i++) free[i] = ok([bx0 + (i % nx) * cell, by0 + Math.floor(i / nx) * cell]) ? 1 : 0;
  return free;
}

/** A* po siatce `cell` w prostokącie [x0, y0, x1, y1] po punktach spełniających `ok` → [a, …, b] albo null.
 *  `free` = gotowe freeCells dla tego prostokąta (wiele tras po tym samym terenie). */
export function gridRoute(ok, [bx0, by0, bx1, by1], cell, a, b, free = freeCells(ok, [bx0, by0, bx1, by1], cell)) {
  const g = { x0: bx0, y0: by0, nx: Math.ceil((bx1 - bx0) / cell) + 1, ny: Math.ceil((by1 - by0) / cell) + 1 }, N = g.nx * g.ny;
  const at = (i) => [g.x0 + (i % g.nx) * cell, g.y0 + Math.floor(i / g.nx) * cell];
  const cellOf = ([x, y]) => {                         // najbliższa wolna komórka (punkt bywa na granicy / w bramie)
    const cx = Math.round((x - g.x0) / cell), cy = Math.round((y - g.y0) / cell);
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
  const open = heap();
  open.push(h(s), s);
  gScore[s] = 0;
  while (open.size) {
    const i = open.pop();
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
        open.push(ng + h(j), j);
      }
    }
  }
  if (from[t] < 0 && s !== t) return null;
  const cells = [];
  for (let i = t; i >= 0; i = i === s ? -1 : from[i]) cells.push(at(i));
  return smooth([a, ...cells.reverse(), b], ok);
}

/** Kopiec binarny (min po f) na [f, i] — kolejka A* (trasa na każdą paletę, nie tylko na dok). */
function heap() {
  const f = [], v = [];
  return {
    get size() { return v.length; },
    push(k, x) {
      let i = v.length;
      f.push(k); v.push(x);
      while (i > 0) {
        const p = (i - 1) >> 1;
        if (f[p] <= f[i]) break;
        [f[p], f[i]] = [f[i], f[p]]; [v[p], v[i]] = [v[i], v[p]];
        i = p;
      }
    },
    pop() {
      const top = v[0], lf = f.pop(), lv = v.pop();
      if (v.length) {
        f[0] = lf; v[0] = lv;
        for (let i = 0; ;) {
          const l = 2 * i + 1, r = l + 1;
          let m = i;
          if (l < v.length && f[l] < f[m]) m = l;
          if (r < v.length && f[r] < f[m]) m = r;
          if (m === i) break;
          [f[m], f[i]] = [f[i], f[m]]; [v[m], v[i]] = [v[i], v[m]];
          i = m;
        }
      }
      return top;
    },
  };
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
