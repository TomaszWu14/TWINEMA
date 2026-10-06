// Animacja dnia scenariusza (S4): obiekty ze zdarzeń S3a na scenie hali (createViewer).
// Pojazdy, palety i paczki = InstancedMesh (po jednej siatce na rodzaj, aktualizowane tylko aktywne).
// Render: pętla tylko w trakcie odtwarzania; po przewinięciu jedna klatka (renderNow).
import * as THREE from 'three';
import { QUEUE_M, QUEUE_PITCH_M, TRAVEL_S, VEHICLES, buildTracks, countersAt, crewAt, dayRange, dockPose, hashId,
  hhmm, lPath, lPathYaw, orderedSlot, palletAt, queueSides, rackFront, rectCenter, seriesAt, slotOrder,
  stationSpots, vehicleAt, vehiclePose, yawOut, ENTER_S } from './day-timeline.js';
import { localToWorld, nearestEntry, sitePlan } from './scene-data.js';
import { routePath } from './site-route.js';
import { CARRY, modelForEquipment, modelParts } from './equipment-models.js';

const MAX_PARCEL_STACK = 120;

// Pojazdy i ładunki z prostych brył (bez cudzych modeli): [długość, wysokość, szerokość, x środka, y dołu, kolor, z].
// Sprzęt magazynowy (reach, VNA, paletowy, AGV…) — equipment-models.js.
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
  // Ludzie (kamizelka odblaskowa) — low-poly z brył, przód = +x.
  person: [[0.28, 0.85, 0.4, 0, 0, 0x1f2937], [0.32, 0.62, 0.5, 0, 0.85, 0xf97316], [0.24, 0.24, 0.24, 0, 1.5, 0xe0b48a],
    [0.27, 0.1, 0.27, 0, 1.74, 0xfacc15]],
  conveyor: [[8.0, 0.18, 0.75, 1.0, 0.95, 0x9ca3af], [3.0, 0.95, 0.85, -1.6, 0, 0x6b7280]],
};
const NO_SHADOW = new Set(['parcel', 'conveyor']);

/** Jeden rodzaj obiektu = po jednej siatce instancyjnej na część; wspólny licznik `count`. */
function fleet(scene, kind, n) {
  const parts = (PARTS[kind] || modelParts(kind)).map(([l, h, w, x, y, color, z = 0]) => {
    const mesh = new THREE.InstancedMesh(new THREE.BoxGeometry(l, h, w).translate(x, y + h / 2, z),
      new THREE.MeshStandardMaterial({ color, roughness: color === 0x0f172a ? 0.15 : 0.6, metalness: color === 0x0f172a ? 0.6 : 0.15 }),
      Math.max(1, n));
    mesh.count = 0;
    mesh.castShadow = !NO_SHADOW.has(kind);
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
  const step = data.timeline.step_s || 900, people = data.timeline.people || {};
  const crewMax = Object.values(people).reduce((a, s) => a + Math.max(0, ...s), 0);
  const nDocks = Object.keys(places.docks).length;
  const plan = sitePlan(data.site), enterS = plan?.entries.length ? ENTER_S : 0;      // D1: wjazd z bramy działki
  const entryOf = {};
  // D3: trasa wjazd → pas przed dokiem po drogach działki (raz na dok i rodzaj auta); brak trasy → punkt wjazdu
  // (vehiclePose jedzie wtedy odcinkiem prostym jak w D1)
  const entryFor = (d, kind) => (entryOf[`${d.wall}:${kind}`] ??= (() => {
    const at = nearestEntry(plan, d.wall, kind === 'courier' ? 'car' : 'truck')?.at;
    if (!at) return null;
    const lane = dockPose(d, QUEUE_M);
    return routePath(plan, data.floor, at, [lane.x, lane.y]) || at;
  })());
  const mesh = {
    container: fleet(viewer.scene, 'container', byKind('container').length),
    truck: fleet(viewer.scene, 'truck', byKind('truck').length),
    courier: fleet(viewer.scene, 'courier', byKind('courier').length),
    pallet: fleet(viewer.scene, 'pallet', pallets.length),
    parcel: fleet(viewer.scene, 'parcel', MAX_PARCEL_STACK),
    person: fleet(viewer.scene, 'person', crewMax + 8),
    conveyor: fleet(viewer.scene, 'conveyor', nDocks),
  };
  // Sprzęt przy regałach: VNA w regałach VNA, poza nimi flota scenariusza z katalogu (AGV, AMR, czołowy…), domyślnie reach.
  // `?sprzet=<typ z katalogu>` w adresie podmienia flotę — podgląd modelu bez zmiany scenariusza.
  // K3 flota mieszana (`fleet_kinds` per rola): regały paletowe — grupa „rack” (albo transport), a przy AGV/AMR + VNA
  // paleta do regału VNA jedzie pierwszą połowę drogi pojazdem transportowym, resztę VNA (przekazanie).
  const asked = new URLSearchParams(globalThis.location?.search).get('sprzet'), fk = asked ? {} : (data.fleet_kinds || {});
  const carrier = modelForEquipment(asked || fk.rack || fk.transport || data.fleet_kind) || 'reach';
  const shuttle = fk.vna && fk.transport ? modelForEquipment(fk.transport) : null;
  const need = { ptruck: nDocks * 2, vna: pallets.length };
  for (const k of [carrier, shuttle]) if (k) need[k] = (need[k] || 0) + pallets.length;
  for (const [k, n] of Object.entries(need)) mesh[k] = fleet(viewer.scene, k, n);
  const M = new THREE.Matrix4(), Q = new THREE.Quaternion(), P = new THREE.Vector3(), S1 = new THREE.Vector3(1, 1, 1);
  const UP = new THREE.Vector3(0, 1, 0);
  const put = (m, x, y, z, yaw = 0) => {
    Q.setFromAxisAngle(UP, yaw);
    m.push(M.compose(P.set(x, z, y), Q, S1));
  };

  // ── Miejsca → punkty w hali ────────────────────────────────────────────────────────────────
  const sides = queueSides(places.docks);
  const inside = (d, k, side = 0) => {             // punkt w hali za dokiem (k m od ściany, przesunięcie wzdłuż)
    const p = dockPose(d, -k);
    return [p.x + Math.abs(d.out[1]) * side, p.y + Math.abs(d.out[0]) * side];
  };
  const gate = places.gate;
  const rectList = (key) => places[key] || [];
  const near = (role) => {                         // środek doków danej strony (palety na polu rosną od doków)
    const ds = Object.values(places.docks).filter((d) => role.includes(d.role));
    return ds.length ? [ds.reduce((a, d) => a + d.x, 0) / ds.length, ds.reduce((a, d) => a + d.y, 0) / ds.length] : null;
  };
  const NEAR = { staging_in: near(['in_container', 'in_pallet', 'shared']), staging_out: near(['out', 'shared', 'courier']) };
  const orders = {};
  const slotFor = (key, rect, ri, k) => {
    const id = `${key}:${ri}`;
    if (!orders[id]) orders[id] = slotOrder(rect, NEAR[key] || rectCenter(rect));
    return orderedSlot(rect, orders[id], k);
  };
  const anchor = (key, id) => {
    if (key === 'rack' || key === 'pick') return rackFront(racks, id) || gate;
    if (key.startsWith('dock:')) { const d = places.docks[key.slice(5)]; return d ? inside(d, 4) : gate; }
    const rs = rectList(key);
    if (rs.length) return key.startsWith('staging') ? slotFor(key, rs[0], 0, 0).slice(0, 2) : rectCenter(rs[0]);
    // brak pola/stanowiska w layoucie → przy dokach odpowiedniej strony
    const side = key.endsWith('_out') || key === 'pack' ? 'out' : 'in_container';
    const d = Object.values(places.docks).find((v) => v.role === side || v.role === 'shared');
    return d ? inside(d, 8) : gate;
  };
  const rackOf = (id) => (racks.length ? racks[hashId(id) % racks.length] : null);

  // ── Plac przed dokami: asfalt do rzędu kolejki + malowane linie pasów i miejsc oczekiwania ──────
  const yard = new THREE.Group();
  viewer.scene.add(yard);
  const lineMat = new THREE.MeshBasicMaterial({ color: 0xf1f5f9 }), apronMat = new THREE.MeshStandardMaterial({ color: 0x4b4f54, roughness: 0.95 });
  const flat = (mat, x, y, w, d, yaw, h = 0.01) => {
    const m = new THREE.Mesh(new THREE.PlaneGeometry(w, d), mat);
    m.rotation.set(-Math.PI / 2, 0, yaw); m.position.set(x, h, y); m.receiveShadow = true;
    yard.add(m);
  };
  for (const side of Object.values(sides)) {
    const ds = Object.values(places.docks).filter((d) => d.out[0] === side.out[0] && d.out[1] === side.out[1]);
    const ss = ds.map((d) => (side.out[0] ? d.wall[1] : d.wall[0])), s1 = Math.max(...ss, side.s0 + 12 * QUEUE_PITCH_M);
    const depth = QUEUE_M + 12, len = s1 - side.s0 + 16, mid = (side.s0 + s1) / 2, yaw = side.out[0] ? Math.PI / 2 : 0;
    const at = (s, k) => dockPose(side.out[0] ? { wall: [side.ref.wall[0], s], out: side.out } : { wall: [s, side.ref.wall[1]], out: side.out }, k);
    const c = at(mid, depth / 2);
    if (!plan) flat(apronMat, c.x, c.y, len, depth, yaw, -0.005);   // z działką asfalt rysuje teren działki
    for (const d of ds) {                          // pas dojazdu do doku: dwie linie co 4 m
      for (const sg of [-1.9, 1.9]) {
        const p = at((side.out[0] ? d.wall[1] : d.wall[0]) + sg, 9);
        flat(lineMat, p.x, p.y, 0.12, 16, yaw);
      }
    }
    for (let i = 0; i <= 12; i++) {                // miejsca oczekiwania w rzędzie kolejki
      const p = at(side.s0 - QUEUE_PITCH_M / 2 + i * QUEUE_PITCH_M, QUEUE_M);
      flat(lineMat, p.x, p.y, 0.12, 15, yaw);
    }
  }

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
          // Płaska plama na posadzce/placu (wysoki prostopadłościan zasłaniał ludzi i auta w doku).
          const m = new THREE.Mesh(new THREE.BoxGeometry(box[2] + 1, 0.12, box[3] + 1), hiMat);
          m.position.set(box[0], 0.07, box[1]);
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
    // pojazdy: rząd kolejki na placu swojej strony, pas dojazdu, postój tyłem do bramy, odjazd
    const queued = {}, docked = [];
    for (const tr of vehicles) {
      if (t < tr.t0 - TRAVEL_S || t > tr.t1 + TRAVEL_S + enterS) continue;
      const v = vehicleAt(tr, t, enterS), d = v && places.docks[v.dock];
      if (!d) continue;
      const key = `${d.out}`, slot = v.phase === 'queue' ? (queued[key] = (queued[key] ?? -1) + 1) : 0;
      const pose = vehiclePose(v, d, tr.kind, sides, slot, entryFor(d, tr.kind));
      put(mesh[tr.kind], pose.x, pose.y, 0, pose.yaw);
      if (v.phase === 'dock') docked.push({ d, kind: tr.kind });
    }
    // palety: na stanowisku / polu (od strony doków), w przejeździe (L po alejkach) na wózku
    const slots = {};
    for (const tr of pallets) {
      if (t < tr.t0 || t > tr.t1 + 1) continue;
      const s = palletAt(tr, t);
      if (!s) continue;
      if (s.at) {
        const rs = rectList(s.at);
        if (rs.length && (s.at.startsWith('staging') || s.at === 'palletize')) {
          const k = (slots[s.at] = (slots[s.at] || 0) + 1) - 1;
          const ri = k % rs.length, [x, y, layer] = s.at === 'palletize'
            ? [...rectCenter(rs[ri]), Math.floor(k / rs.length)] : slotFor(s.at, rs[ri], ri, Math.floor(k / rs.length));
          put(mesh.pallet, x, y, layer * 1.35);
        } else {
          const [x, y] = anchor(s.at, tr.obj);
          put(mesh.pallet, x, y, 0);
        }
      } else {
        const a = anchor(s.from, tr.obj), b = anchor(s.to, tr.obj), [x, y] = lPath(a, b, s.p), yaw = lPathYaw(a, b, s.p);
        const r = rackOf(tr.obj), onShuttle = s.from === 'rack' ? s.p >= 0.5 : s.p < 0.5;   // połowa drogi po stronie pola = pojazd transportowy
        const kind = (r?.rack_class ?? r?.equipment) !== 'vna' ? carrier : shuttle && onShuttle ? shuttle : 'vna', c = CARRY[kind];
        put(mesh.pallet, x, y, c.z, yaw);
        put(mesh[kind], x - Math.cos(yaw) * c.dx, y + Math.sin(yaw) * c.dx, 0, yaw);
      }
    }
    // ludzie i wózki paletowe: zajęci w tej chwili wg osi czasu obsady S3a (co 15 min)
    const crew = crewAt(people, step, t);
    const man = ([x, y], yaw = 0) => put(mesh.person, x, y, 0, yaw);
    const atDocks = (n, list) => list.forEach((it, i) => {
      for (let j = i; j < n; j += list.length) man(inside(it.d, 2.2 + Math.floor(j / list.length) * 1.3, j % 2 ? 0.9 : -0.9), yawOut(it.d.out));
      if (it.kind === 'container') put(mesh.conveyor, it.d.wall[0], it.d.wall[1], 0, yawOut(it.d.out));
      else if (i < n) { const [x, y] = inside(it.d, 4.5, 1.6); put(mesh.ptruck, x, y, 0, yawOut(it.d.out)); }
    });
    const isIn = (it) => it.d.role.startsWith('in_') || (it.d.role === 'shared' && it.kind !== 'truck');
    atDocks(crew.unload || 0, docked.filter(isIn));
    atDocks(crew.load || 0, docked.filter((it) => !isIn(it)));
    stationSpots(rectList('palletize'), crew.palletize || 0).forEach((p) => man(p));
    stationSpots(rectList('pack'), crew.pack || 0).forEach((p) => man(p));
    stationSpots(rectList('returns'), crew.returns || 0).forEach((p) => man(p));
    const si = rectList('staging_in');
    for (let i = 0; i < (crew.inspect || 0) && si.length; i++) { const [x, y] = slotFor('staging_in', si[0], 0, i * 3); man([x + 0.8, y]); }
    for (let i = 0; i < (crew.pick || 0) && racks.length; i++) {   // kompletujący idą wzdłuż frontu regału
      const r = racks[hashId(`picker${i}`) % racks.length], k = 0.5 + 0.42 * Math.sin(t / 150 + i * 1.7);
      man(localToWorld(r, [r.width * k, -1.1]), ((r.angle || 0) * Math.PI) / 180);
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
    /** Prezentacja (P1): obiekty animacji (auta, ludzie, palety, plac, podświetlenia) ukryte poza jej slajdami. */
    setVisible(on) {
      [yard, hi, ...Object.values(mesh).flatMap((m) => m.parts)].forEach((o) => { o.visible = on; });
      viewer.requestRender();
    },
    focus(keys) {
      const ds = keys.filter((k) => k.startsWith('dock:')).map((k) => places.docks[k.slice(5)]).filter(Boolean);
      if (ds.length) { frameDocks(ds); return; }
      const pts = keys.map((k) => placeBox(k)).filter(Boolean);
      if (!pts.length) return;
      const cx = pts.reduce((a, p) => a + p[0], 0) / pts.length, cy = pts.reduce((a, p) => a + p[1], 0) / pts.length;
      look(cx + 28, 30, cy + 34, cx, 0, cy);
    },
    home,
    hhmm,
  };
  function look(px, py, pz, tx, ty, tz) {
    viewer.camera.position.set(px, py, pz);
    viewer.controls.target.set(tx, ty, tz);
    viewer.controls.update();
    viewer.renderNow();
  }
  // Doki z placu: kamera na zewnątrz i z boku, cel w hali za dokami — auta, ludzie i wnętrze w jednym kadrze.
  function frameDocks(ds) {
    const o = ds[0].out, cx = ds.reduce((a, d) => a + d.wall[0], 0) / ds.length, cy = ds.reduce((a, d) => a + d.wall[1], 0) / ds.length;
    const span = Math.max(20, ...ds.map((d) => Math.hypot(d.wall[0] - cx, d.wall[1] - cy) * 2)), k = span * 0.6 + 30;
    const tg = [Math.abs(o[1]), Math.abs(o[0])];
    look(cx + o[0] * k + tg[0] * k * 0.55, k * 0.55, cy + o[1] * k + tg[1] * k * 0.55, cx - o[0] * 18, 0, cy - o[1] * 18);
  }
  /** Kadr startowy: doki przyjęć (kontenery i auta) — nie cały plac z daleka. */
  function home() {
    const ins = Object.values(places.docks).filter((d) => d.role.startsWith('in_'));
    const ds = ins.length ? ins : Object.values(places.docks);
    if (!ds.length) return;
    const side = ds.filter((d) => d.out[0] === ds[0].out[0] && d.out[1] === ds[0].out[1]);
    frameDocks(side);
  }
  update(t);
  home();
  return api;
}
