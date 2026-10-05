// Animacja dnia scenariusza (S4): obiekty ze zdarzeń S3a na scenie hali (createViewer).
// Pojazdy, palety i paczki = InstancedMesh (po jednej siatce na rodzaj, aktualizowane tylko aktywne).
// Render: pętla tylko w trakcie odtwarzania; po przewinięciu jedna klatka (renderNow).
import * as THREE from 'three';
import { TRAVEL_S, VEHICLES, buildTracks, countersAt, dayRange, hhmm, lPath, palletAt, rackFront, rectCenter,
  rectSlot, seriesAt, vehicleAt } from './day-timeline.js';

const MAX_PARCEL_STACK = 120;

// Pojazdy i ładunki z prostych brył (bez cudzych modeli): [długość, wysokość, szerokość, x środka, y dołu, kolor].
// Oś +x pojazdu = od doku na zewnątrz (kabina z dala od hali), środek naczepy jak dotąd ~7 m przed dokiem.
const WHEEL = 0x1f2329, CHASSIS = 0x30353a;
const axles = (xs) => xs.map((x) => [1.0, 1.0, 2.6, x, 0, WHEEL]);
const PARTS = {
  truck: [[13.6, 2.75, 2.55, 0, 1.25, 0xe5e7eb], [0.06, 0.5, 2.57, 0, 2.6, 0x1d4ed8], [15.6, 0.35, 2.2, 0.9, 0.85, CHASSIS],
    [2.3, 2.9, 2.5, 8.15, 0.75, 0x1d4ed8], [0.05, 1.0, 2.2, 9.32, 2.2, 0x0f172a], ...axles([-4.6, -3.3, -2.0, 7.4, 8.8])],
  container: [[12.2, 2.6, 2.45, 0, 1.25, 0xb45309], [14.0, 0.35, 2.2, 0.8, 0.85, CHASSIS],
    [2.3, 2.9, 2.5, 7.45, 0.75, 0x374151], [0.05, 1.0, 2.2, 8.62, 2.2, 0x0f172a], ...axles([-4.2, -2.9, -1.6, 6.7, 8.1])],
  courier: [[4.0, 2.2, 2.0, -0.8, 0.45, 0xf8fafc], [1.7, 1.75, 2.0, 2.05, 0.45, 0xf8fafc], [0.05, 0.8, 1.8, 2.92, 1.25, 0x0f172a],
    [0.8, 0.75, 2.1, -1.9, 0, WHEEL], [0.8, 0.75, 2.1, 1.9, 0, WHEEL]],
  pallet: [[1.2, 0.144, 0.8, 0, 0, 0xa87d4a], [1.16, 1.1, 0.76, 0, 0.144, 0xb4874f]],
  parcel: [[0.6, 0.4, 0.4, 0, 0, 0x92400e]],
};

/** Jeden rodzaj obiektu = po jednej siatce instancyjnej na część; wspólny licznik `count`. */
function fleet(scene, kind, n) {
  const parts = PARTS[kind].map(([l, h, w, x, y, color]) => {
    const mesh = new THREE.InstancedMesh(new THREE.BoxGeometry(l, h, w).translate(x, y + h / 2, 0),
      new THREE.MeshStandardMaterial({ color, roughness: color === 0x0f172a ? 0.15 : 0.6, metalness: color === 0x0f172a ? 0.6 : 0.15 }),
      Math.max(1, n));
    mesh.count = 0;
    mesh.castShadow = kind !== 'parcel';
    mesh.frustumCulled = false;
    scene.add(mesh);
    return mesh;
  });
  return {
    parts, count: 0,
    reset() { this.count = 0; parts.forEach((p) => { p.count = 0; }); },
    push(m) { parts.forEach((p) => { p.setMatrixAt(this.count, m); p.count = this.count + 1; }); this.count++; },
    flush() { parts.forEach((p) => { p.instanceMatrix.needsUpdate = true; }); },
  };
}

/**
 * createDayPlayer({viewer, data, events, ui}) — data z widoku (floor, racks, places, bottlenecks, timeline,
 * peak_t), events = `twinema.scenario-events`.events. ui: elementy DOM (opcjonalne). → {seek, play, pause, …}
 */
export function createDayPlayer({ viewer, data, events, ui = {} }) {
  const { places, racks } = data;
  const tracks = buildTracks(events);
  const [tMin, tMax] = dayRange(events);
  const all = [...tracks.values()];
  const byKind = (k) => all.filter((tr) => tr.kind === k);
  const vehicles = all.filter((tr) => VEHICLES.has(tr.kind)), pallets = byKind('pallet');
  const mesh = {
    container: fleet(viewer.scene, 'container', byKind('container').length),
    truck: fleet(viewer.scene, 'truck', byKind('truck').length),
    courier: fleet(viewer.scene, 'courier', byKind('courier').length),
    pallet: fleet(viewer.scene, 'pallet', pallets.length),
    parcel: fleet(viewer.scene, 'parcel', MAX_PARCEL_STACK),
  };
  const M = new THREE.Matrix4(), Q = new THREE.Quaternion(), P = new THREE.Vector3(), S1 = new THREE.Vector3(1, 1, 1);
  const UP = new THREE.Vector3(0, 1, 0);
  const put = (m, x, y, z, yaw = 0) => {
    Q.setFromAxisAngle(UP, yaw);
    m.push(M.compose(P.set(x, z, y), Q, S1));
  };

  // ── Miejsca → punkty w hali ────────────────────────────────────────────────────────────────
  const dockPt = (id, k = 0) => {
    const d = places.docks[id];
    if (!d) return null;
    const len = 7 + k;                                           // auto stoi przed doku, przodem do hali
    return { x: d.x + d.out[0] * len, y: d.y + d.out[1] * len, yaw: Math.atan2(-d.out[1], d.out[0]) };
  };
  const gate = places.gate;
  const rectList = (key) => places[key] || [];
  const anchor = (key, id) => {
    if (key === 'rack' || key === 'pick') return rackFront(racks, id) || gate;
    if (key.startsWith('dock:')) { const p = dockPt(key.slice(5), -6); return p ? [p.x, p.y] : gate; }
    const rs = rectList(key);
    if (rs.length) return rectCenter(rs[0]);
    // brak pola/stanowiska w layoucie → przy dokach odpowiedniej strony
    const side = key.endsWith('_out') || key === 'pack' ? 'out' : 'in_container';
    const d = Object.entries(places.docks).find(([, v]) => v.role === side || v.role === 'shared');
    return d ? [d[1].x - d[1].out[0] * 8, d[1].y - d[1].out[1] * 8] : gate;
  };

  // ── Klatka ─────────────────────────────────────────────────────────────────────────────────
  const hi = new THREE.Group();
  viewer.scene.add(hi);
  const hiMat = new THREE.MeshBasicMaterial({ color: 0xef4444, transparent: true, opacity: 0.45, depthWrite: false });
  let shownBn = '';

  function placeBox(key) {
    if (key.startsWith('dock:')) {
      const d = places.docks[key.slice(5)];
      return d ? [d.x, d.y, 5, 5] : null;
    }
    const r = rectList(key)[0];
    if (!r) return null;
    const [cx, cy] = rectCenter(r);
    return [cx, cy, r.w, r.d];
  }
  function highlight(t) {
    const act = (data.bottlenecks || []).filter((b) => b.t0 !== null && t >= b.t0 && t < b.t1);
    const sig = act.map((b) => b.area).join('|');
    if (sig !== shownBn) {
      shownBn = sig;
      hi.children.forEach((c) => c.geometry.dispose());
      hi.clear();
      for (const b of act) {
        for (const k of b.keys) {
          const box = placeBox(k);
          if (!box) continue;
          const m = new THREE.Mesh(new THREE.BoxGeometry(box[2] + 1, 3, box[3] + 1), hiMat);
          m.position.set(box[0], 1.5, box[1]);
          hi.add(m);
        }
      }
      ui.onBottlenecks?.(act);
    }
  }

  let frameMs = 0;
  function update(t) {
    const t0 = performance.now();
    Object.values(mesh).forEach((m) => m.reset());
    // pojazdy: kolejka przy bramie (kolejne miejsca co 4 m), dojazd, postój w doku, odjazd
    const queue = [];
    for (const tr of vehicles) {
      if (t < tr.t0 - TRAVEL_S || t > tr.t1 + TRAVEL_S) continue;
      const v = vehicleAt(tr, t);
      if (!v) continue;
      const d = dockPt(v.dock) || { x: gate[0], y: gate[1], yaw: 0 };
      if (v.phase === 'queue') { queue.push([tr, d]); continue; }
      const p = v.phase === 'in' ? v.p : v.phase === 'out' ? 1 - v.p : 1;
      put(mesh[tr.kind], gate[0] + (d.x - gate[0]) * p, gate[1] + (d.y - gate[1]) * p, 0, d.yaw);
    }
    queue.forEach(([tr, d], i) => put(mesh[tr.kind], gate[0] + (i % 6) * 4, gate[1] + Math.floor(i / 6) * 16, 0, d.yaw));
    // palety: na stanowisku / polu (kolejne sloty), w przejeździe (L po alejkach)
    const slots = {};
    for (const tr of pallets) {
      if (t < tr.t0 || t > tr.t1 + 1) continue;
      const s = palletAt(tr, t);
      if (!s) continue;
      if (s.at) {
        const rs = rectList(s.at);
        if (rs.length && (s.at.startsWith('staging') || s.at === 'palletize')) {
          const k = (slots[s.at] = (slots[s.at] || 0) + 1) - 1;
          const [x, y, layer] = rectSlot(rs[k % rs.length], Math.floor(k / rs.length));
          put(mesh.pallet, x, y, layer * 1.35);
        } else {
          const [x, y] = anchor(s.at, tr.obj);
          put(mesh.pallet, x, y, 0);
        }
      } else {
        const [x, y] = lPath(anchor(s.from, tr.obj), anchor(s.to, tr.obj), s.p);
        put(mesh.pallet, x, y, 0.2);
      }
    }
    // paczki czekające na kuriera: stos przy stanowisku pakowania (1 kostka ≈ 20 paczek)
    const c = countersAt(tracks, t);
    const [px, py] = anchor('pack');
    for (let i = 0; i < Math.min(MAX_PARCEL_STACK, Math.ceil(c.pending / 20)); i++) {
      put(mesh.parcel, px + (i % 5) * 0.65, py + (Math.floor(i / 5) % 4) * 0.45, Math.floor(i / 20) * 0.42);
    }
    Object.values(mesh).forEach((m) => m.flush());
    highlight(t);
    c.fleet = seriesAt(data.timeline.fleet_busy, data.timeline.step_s, t);
    c.people = Object.fromEntries(Object.entries(data.timeline.people || {})
      .map(([p, s]) => [p, seriesAt(s, data.timeline.step_s, t)]));
    ui.onCounters?.(c, t);
    viewer.renderNow();
    frameMs = performance.now() - t0;
    return c;
  }

  // ── Zegar ──────────────────────────────────────────────────────────────────────────────────
  let t = tMin, speed = 60, playing = false, last = 0;
  function tick(now) {
    if (!playing) return;
    const dt = last ? (now - last) / 1000 : 0;
    last = now;
    t = Math.min(tMax, t + dt * speed);
    update(t);
    ui.onTime?.(t, playing);
    if (t >= tMax) { playing = false; ui.onTime?.(t, false); return; }
    requestAnimationFrame(tick);
  }
  const api = {
    tMin, tMax, tracks,
    seek(s) { t = Math.max(tMin, Math.min(tMax, s)); update(t); ui.onTime?.(t, playing); return t; },
    play() { if (playing) return; if (t >= tMax) t = tMin; playing = true; last = 0; ui.onTime?.(t, true); requestAnimationFrame(tick); },
    pause() { playing = false; ui.onTime?.(t, false); },
    toggle() { playing ? api.pause() : api.play(); },
    setSpeed(x) { speed = x; ui.onSpeed?.(x); },
    get t() { return t; }, get playing() { return playing; }, get speed() { return speed; },
    get frameMs() { return frameMs; },
    focus(keys) {
      const pts = keys.map((k) => placeBox(k)).filter(Boolean);
      if (!pts.length) return;
      const cx = pts.reduce((a, p) => a + p[0], 0) / pts.length, cy = pts.reduce((a, p) => a + p[1], 0) / pts.length;
      viewer.camera.position.set(cx + 28, 30, cy + 34);
      viewer.controls.target.set(cx, 0, cy);
      viewer.controls.update();
      viewer.renderNow();
    },
    hhmm,
  };
  update(t);
  return api;
}
