// Działka w scenie 3D (D1): teren wokół hali — trawa, asfalt placów i dróg, parking z liniami, linie zabudowy,
// ogrodzenie po granicy z przerwami na wjazdy. Geometria w układzie hali liczona w scene-data.sitePlan.
import * as THREE from 'three';

import { stackLayer } from './scene-data.js';

const GROUND = { green: 0x6f9a52, yard: 0xe2e2e2, road: 0xcdcdcd, parking: 0xf2f2f2 };   // asfalt: mnożnik tekstury
const POST_M = 3.0;

/** Wielokąt (punkty hali [x, y]) → płaska siatka na wysokości h (płaszczyzna XZ, y hali = z sceny). */
function flat(pts, mat, h, track) {
  const shape = new THREE.Shape(pts.map(([x, y]) => new THREE.Vector2(x, -y)));
  const m = new THREE.Mesh(track(new THREE.ShapeGeometry(shape)), mat);
  m.rotation.x = -Math.PI / 2; m.position.y = h; m.receiveShadow = true;
  return m;
}

/** Odcinek a→b co `step` (bez końca) — słupki ogrodzenia. */
function posts(a, b, step) {
  const n = Math.max(1, Math.floor(Math.hypot(b[0] - a[0], b[1] - a[1]) / step)), out = [];
  for (let i = 0; i < n; i++) out.push([a[0] + ((b[0] - a[0]) * i) / n, a[1] + ((b[1] - a[1]) * i) / n]);
  return out;
}

/**
 * buildSite(group, plan, {track, asphalt}) — dodaje teren do grupy sceny. `plan` = scene-data.sitePlan(site),
 * `track(obj)` rejestruje geometrie/materiały do zwolnienia przy przebudowie, `asphalt` = tekstura asfaltu sceny.
 */
export function buildSite(group, plan, { track, asphalt }) {
  const mat = (color, map) => {
    const m = track(new THREE.MeshStandardMaterial({ color, roughness: 0.95, map: map || null }));
    if (map) { m.map = track(map.clone()); m.map.needsUpdate = true; m.map.repeat.set(1 / 8, 1 / 8); }
    return m;
  };
  const xs = plan.plot.map((p) => p[0]), ys = plan.plot.map((p) => p[1]);
  const cx = (Math.min(...xs) + Math.max(...xs)) / 2, cy = (Math.min(...ys) + Math.max(...ys)) / 2;
  const span = Math.max(Math.max(...xs) - Math.min(...xs), Math.max(...ys) - Math.min(...ys)) * 3 + 200;
  const outside = new THREE.Mesh(track(new THREE.PlaneGeometry(span, span)), mat(0x7c8f6a));
  outside.rotation.x = -Math.PI / 2; outside.position.set(cx, -0.06, cy); outside.receiveShadow = true;
  group.add(outside, flat(plan.plot, mat(GROUND.green), -0.04, track));
  for (const a of plan.areas) {                         // zieleń pod asfaltem: kolejność warstw = rodzaj
    const h = a.kind === 'green' ? -0.03 : -0.025;
    group.add(stackLayer(flat(a.pts, mat(GROUND[a.kind] ?? 0x888888, a.kind === 'green' ? null : asphalt), h, track), a.kind));
    if (a.kind === 'parking') {                         // miejsca postojowe co 2,5 m wzdłuż dłuższego boku
      const [p0, p1, , p3] = a.pts, long = a.w >= a.d, [u, v] = long ? [p1, p3] : [p3, p1];
      const L = Math.hypot(u[0] - p0[0], u[1] - p0[1]), M = Math.hypot(v[0] - p0[0], v[1] - p0[1]);
      const du = [(u[0] - p0[0]) / L, (u[1] - p0[1]) / L], dv = [(v[0] - p0[0]) / M, (v[1] - p0[1]) / M];
      const pts = [];
      for (let s = 2.5; s < L; s += 2.5) {
        for (const k of [0.4, M - 5.4]) {               // dwa rzędy stanowisk 5 m przy dłuższych krawędziach
          if (k < 0) continue;
          pts.push(new THREE.Vector3(p0[0] + du[0] * s + dv[0] * k, 0.01, p0[1] + du[1] * s + dv[1] * k),
            new THREE.Vector3(p0[0] + du[0] * s + dv[0] * (k + 5), 0.01, p0[1] + du[1] * s + dv[1] * (k + 5)));
        }
      }
      if (pts.length) group.add(new THREE.LineSegments(track(new THREE.BufferGeometry().setFromPoints(pts)),
        track(new THREE.LineBasicMaterial({ color: 0xf1f5f9 }))));
    }
  }
  if (plan.building) {                                  // linie zabudowy — przerywana, nad terenem
    const line = new THREE.LineLoop(track(new THREE.BufferGeometry().setFromPoints(
      plan.building.map(([x, y]) => new THREE.Vector3(x, 0.05, y)))),
    track(new THREE.LineDashedMaterial({ color: 0xfacc15, dashSize: 2, gapSize: 1.5 })));
    line.computeLineDistances();
    group.add(line);
  }
  // Ogrodzenie: słupki co 3 m (instancje) + górna linia; przerwy na wjazdach.
  const gaps = plan.entries.map((e) => ({ at: e.at, r: e.width / 2 + 0.5 }));
  const pts = [];
  for (let i = 0; i < plan.plot.length; i++) {             // D2: dowolny wielokąt granicy
    for (const p of posts(plan.plot[i], plan.plot[(i + 1) % plan.plot.length], POST_M)) {
      if (!gaps.some((g) => Math.hypot(p[0] - g.at[0], p[1] - g.at[1]) < g.r)) pts.push(p);
    }
  }
  const post = new THREE.InstancedMesh(track(new THREE.BoxGeometry(0.08, 2.0, 0.08).translate(0, 1.0, 0)),
    track(new THREE.MeshStandardMaterial({ color: 0x4b5563, roughness: 0.6, metalness: 0.4 })), Math.max(1, pts.length));
  const m4 = new THREE.Matrix4();
  pts.forEach(([x, y], i) => post.setMatrixAt(i, m4.makeTranslation(x, 0, y)));
  post.count = pts.length;
  post.castShadow = true;
  group.add(post);
  group.add(new THREE.LineLoop(track(new THREE.BufferGeometry().setFromPoints(plan.plot.map(([x, y]) => new THREE.Vector3(x, 1.95, y)))),
    track(new THREE.LineBasicMaterial({ color: 0x374151 }))));
  // Wjazdy: dwa słupki w biało-czerwone pasy po bokach przerwy.
  const gateMat = track(new THREE.MeshStandardMaterial({ color: 0xdc2626, roughness: 0.5 }));
  for (const e of plan.entries) {
    const l = Math.hypot(...e.dir) || 1, t = [-e.dir[1] / l, e.dir[0] / l];
    for (const s of [-1, 1]) {
      const g = new THREE.Mesh(track(new THREE.BoxGeometry(0.3, 2.4, 0.3)), gateMat);
      g.position.set(e.at[0] + t[0] * s * (e.width / 2 + 0.2), 1.2, e.at[1] + t[1] * s * (e.width / 2 + 0.2));
      g.castShadow = true;
      group.add(g);
    }
  }
}
