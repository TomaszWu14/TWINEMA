// Animacja dnia scenariusza (S4) — czyste funkcje (bez three.js i DOM), testowane `node --test`
// (twin/tests/js/day_timeline.test.mjs). Wejście: zdarzenia `twinema.scenario-events` v1
// [t_s, obj, kind, what, place, n?] posortowane po czasie (opis: scenario/sim/__init__.py).
import { localToWorld } from './scene-data.js';
import { alongPath } from './site-route.js';

export const VEHICLES = new Set(['container', 'truck', 'courier']);
export const TRAVEL_S = 90;          // dojazd brama → dok / odjazd dok → brama
export const MOVE_MAX_S = 120;       // przejazd palety regał → pole wydań (koniec ruchu znamy, początku nie)
export const SLOT_M = 1.4;
export const ENTER_S = 75;           // D1: przejazd od wjazdu działki do placu przed dokiem (i z powrotem)           // pitch palety na polu odkładczym (EUR 1,2 × 0,8 + odstęp)

/** Pierwszy indeks i, dla którego arr[i] > t (wyszukiwanie binarne po posortowanej tablicy liczb). */
export function upperBound(arr, t) {
  let lo = 0, hi = arr.length;
  while (lo < hi) {
    const mid = (lo + hi) >> 1;
    if (arr[mid] <= t) lo = mid + 1; else hi = mid;
  }
  return lo;
}

/** Zdarzenia → ścieżki obiektów: Map(obj → {obj, kind, t:[…], what:[…], place:[…], n:[…], t0, t1}). */
export function buildTracks(events) {
  const tracks = new Map();
  for (const [t, obj, kind, what, place, n] of events) {
    let tr = tracks.get(obj);
    if (!tr) tracks.set(obj, (tr = { obj, kind, t: [], what: [], place: [], n: [] }));
    tr.t.push(t); tr.what.push(what); tr.place.push(place); tr.n.push(n ?? 1);
  }
  for (const tr of tracks.values()) {
    tr.t0 = tr.t[0];
    tr.t1 = tr.t[tr.t.length - 1];
  }
  // Starsze przebiegi (bez „loaded”): paleta wydań znika z pola, gdy auto „outN” odjeżdża z doku.
  for (const tr of tracks.values()) {
    if (tr.kind !== 'pallet' || tr.what.includes('loaded') || !tr.what.includes('staging')) continue;
    const truck = tracks.get(tr.obj.split('-p')[0]);
    const i = truck ? truck.what.indexOf('dock') : -1;
    if (i >= 0 && truck.t[i] >= tr.t1 && tr.place[tr.place.length - 1] === 'staging_out') {
      tr.t.push(truck.t[i]); tr.what.push('loaded'); tr.place.push(truck.place[i]); tr.n.push(1);
      tr.t1 = truck.t[i];
    }
  }
  return tracks;
}

/** Indeks ostatniego zdarzenia ścieżki w chwili t (−1 = jeszcze nie zaczęła). */
export const stepAt = (tr, t) => upperBound(tr.t, t) - 1;

/** Pojazd w chwili t → null (poza sceną) | {phase: 'enter'|'queue'|'in'|'dock'|'out'|'leave', dock, p}.
 *  `enterS` > 0 (hala na działce): po przyjeździe dojazd od wjazdu działki, po odjeździe powrót do wjazdu. */
export function vehicleAt(tr, t, enterS = 0) {
  const tArr = tr.t[tr.what.indexOf('arrive')] ?? tr.t0;
  const iDock = tr.what.indexOf('dock'), iDep = tr.what.indexOf('depart');
  if (t < tArr || iDock < 0) return null;
  const dock = tr.place[iDock].slice(5), tDock = tr.t[iDock];
  const tDep = iDep >= 0 ? tr.t[iDep] : tDock + 1800;          // kurier bez „depart” (stary format): 30 min
  const tQ = tDock - TRAVEL_S;
  if (enterS && t < Math.min(tArr + enterS, tQ)) return { phase: 'enter', dock, p: (t - tArr) / Math.min(enterS, tQ - tArr) };
  if (t < tQ && t >= tArr) return { phase: 'queue', dock, p: 0 };
  if (t < tDock) return { phase: 'in', dock, p: 1 - (tDock - t) / TRAVEL_S };
  if (t < tDep) return { phase: 'dock', dock, p: 0 };
  if (t < tDep + TRAVEL_S) return { phase: 'out', dock, p: (t - tDep) / TRAVEL_S };
  if (enterS && t < tDep + TRAVEL_S + enterS) return { phase: 'leave', dock, p: (t - tDep - TRAVEL_S) / enterS };
  return null;
}

/** Paleta w chwili t → null | {at: miejsce} | {from, to, p} (przejazd). „rack”/„pick” = regał wg id palety. */
export function palletAt(tr, t) {
  const i = stepAt(tr, t);
  if (i < 0) return null;
  const what = tr.what[i], place = tr.place[i];
  if (what === 'stored' || what === 'loaded') return null;           // w regale / na aucie
  if (what === 'move') {
    const j = tr.what.indexOf('stored', i);
    if (j < 0) return { at: place };
    return { from: place, to: 'rack', p: Math.min(1, (t - tr.t[i]) / Math.max(1, tr.t[j] - tr.t[i])) };
  }
  if (what === 'retrieved' && i + 1 < tr.t.length) {
    const dt = tr.t[i + 1] - tr.t[i], start = tr.t[i + 1] - Math.min(dt, MOVE_MAX_S);
    if (t >= start) return { from: place, to: tr.place[i + 1], p: (t - start) / Math.max(1, tr.t[i + 1] - start) };
  }
  return { at: place };
}

/** Liczniki w chwili t (obiekty z buildTracks). */
export function countersAt(tracks, t) {
  const c = { palletsIn: 0, palletsOut: 0, parcels: 0, queue: 0, atDock: 0, stagingIn: 0, stagingOut: 0, pending: 0 };
  let lastPickup = -1;
  for (const tr of tracks.values()) {
    if (tr.kind === 'courier') {
      const i = tr.what.indexOf('dock');
      if (i >= 0 && tr.t[i] <= t) lastPickup = Math.max(lastPickup, tr.t[i]);
    }
  }
  for (const tr of tracks.values()) {
    if (tr.t0 > t) continue;
    if (VEHICLES.has(tr.kind)) {
      const v = vehicleAt(tr, t);
      if (v?.phase === 'queue' || v?.phase === 'in') c.queue++;
      else if (v?.phase === 'dock') c.atDock++;
    } else if (tr.kind === 'pallet') {
      const i = stepAt(tr, t);
      for (let k = 0; k <= i; k++) {
        if (tr.what[k] === 'staging' && tr.place[k] === 'staging_in') c.palletsIn++;
        if (tr.what[k] === 'loaded') c.palletsOut++;
      }
      const s = palletAt(tr, t);
      if (s?.at === 'staging_in') c.stagingIn++;
      else if (s?.at === 'staging_out') c.stagingOut++;
    } else if (tr.kind === 'parcel') {
      for (let k = 0; k < tr.t.length && tr.t[k] <= t; k++) {
        c.parcels += tr.n[k];
        if (tr.t[k] > lastPickup) c.pending += tr.n[k];   // ponytail: kurier zabiera wszystko gotowe do jego podjazdu
      }
    }
  }
  return c;
}

/** Wartość serii osi czasu S3a (krok step_s) w chwili t. */
export const seriesAt = (series, stepS, t) => (series?.length ? series[Math.min(series.length - 1, Math.max(0, Math.floor(t / stepS)))] : 0);

/** Zakres dnia do suwaka: od pierwszego do ostatniego zdarzenia, zaokrąglony do 15 min. */
export function dayRange(events) {
  if (!events.length) return [0, 24 * 3600];
  const q = 900;
  return [Math.floor(events[0][0] / q) * q, Math.ceil((events[events.length - 1][0] + TRAVEL_S) / q) * q];
}

export const hhmm = (s) => {
  const m = Math.floor(s / 60), h = Math.floor(m / 60) % 24;
  return `${String(h).padStart(2, '0')}:${String(m % 60).padStart(2, '0')}`;
};

// ── Geometria miejsc (hala: x w prawo, y w głąb; prostokąt = narożnik + kąt, jak elementy hali) ─────
/** k-ta kostka na prostokącie (rzędy wzdłuż szerokości, kolejne warstwy co pełne pole). → [x, y, warstwa] */
export function rectSlot(rect, k) {
  const cols = Math.max(1, Math.floor(rect.w / SLOT_M)), rows = Math.max(1, Math.floor(rect.d / SLOT_M));
  const per = cols * rows, layer = Math.floor(k / per), r = k % per;
  const [x, y] = localToWorld(rect, [(r % cols + 0.5) * Math.min(SLOT_M, rect.w), (Math.floor(r / cols) + 0.5) * Math.min(SLOT_M, rect.d)]);
  return [x, y, layer];
}

export const rectCenter = (rect) => localToWorld(rect, [rect.w / 2, rect.d / 2]);

/** Deterministyczny hash id (FNV-1a) — paleta trafia zawsze w ten sam regał. */
export function hashId(s) {
  let h = 0x811c9dc5;
  for (let i = 0; i < s.length; i++) h = Math.imul(h ^ s.charCodeAt(i), 0x01000193) >>> 0;
  return h;
}

/** Punkt przed frontem regału (alejka) dla palety o danym id. */
export function rackFront(racks, id) {
  if (!racks.length) return null;
  const r = racks[hashId(id) % racks.length];
  return localToWorld(r, [r.width / 2, -0.9]);
}

/** Przejazd „w L” po alejkach: najpierw wzdłuż x, potem wzdłuż y; p ∈ [0, 1]. */
export function lPath([ax, ay], [bx, by], p) {
  const dx = Math.abs(bx - ax), dy = Math.abs(by - ay), d = dx + dy || 1, s = Math.max(0, Math.min(1, p)) * d;
  return s <= dx ? [ax + Math.sign(bx - ax) * s, ay] : [bx, ay + Math.sign(by - ay) * (s - dx)];
}

/** Kierunek jazdy na `lPath` w chwili p → yaw sceny (lokalne +x pojazdu = kierunek jazdy). */
export function lPathYaw([ax, ay], [bx, by], p) {
  const dx = Math.abs(bx - ax), dy = Math.abs(by - ay), s = Math.max(0, Math.min(1, p)) * (dx + dy || 1);
  return s <= dx && dx > 0 ? (bx >= ax ? 0 : Math.PI) : (by >= ay ? -Math.PI / 2 : Math.PI / 2);
}

// ── Auta przy dokach (hala: x w prawo, y w głąb; dok = {wall: [x, y] na ścianie, out: [nx, ny]}) ─────
/** Połowa długości pojazdu + 0,3 m od ściany: tył naczepy przy bramie, nie w ścianie (G1b). */
export const STAND_M = { truck: 7.1, container: 6.4, courier: 3.1 };
export const QUEUE_M = 34;           // rząd czekających aut na placu (środek naczepy od ściany)
export const QUEUE_PITCH_M = 4.5;    // odstęp czekających aut (szerokość 2,55 m + przejście)

export const yawOut = (out) => Math.atan2(-out[1], out[0]);
const sideKey = (d) => `${d.out[0]},${d.out[1]}`;
const along = (d) => (d.out[0] ? d.wall[1] : d.wall[0]);            // współrzędna wzdłuż ściany

/** Pozycja na placu przed dokiem w odległości k od ściany (tyłem do bramy). */
export function dockPose(d, k) {
  return { x: d.wall[0] + d.out[0] * k, y: d.wall[1] + d.out[1] * k, yaw: yawOut(d.out) };
}

/** Strony z dokami: {klucz strony: {out, wall: wspólna współrzędna ściany, s0: początek rzędu kolejki}}. */
export function queueSides(docks) {
  const sides = {};
  for (const d of Object.values(docks)) {
    const k = sideKey(d), s = along(d);
    if (!sides[k]) sides[k] = { out: d.out, ref: d, s0: s };
    else sides[k].s0 = Math.min(sides[k].s0, s);
  }
  return sides;
}

/** i-te miejsce w rzędzie kolejki strony doku `d` (rząd równoległy do ściany, auta prostopadle). */
export function queuePose(sides, d, i) {
  const side = sides[sideKey(d)], s = side.s0 + i * QUEUE_PITCH_M;
  const base = side.out[0] ? { wall: [side.ref.wall[0], s], out: side.out } : { wall: [s, side.ref.wall[1]], out: side.out };
  return dockPose(base, QUEUE_M);
}

/** Pojazd z `vehicleAt` → {x, y, yaw}: kolejka = miejsce `slot` w rzędzie, dojazd/odjazd = pas przed dokiem,
 *  enter/leave = prosto między wjazdem działki `entry` ([x, y] w układzie hali) a początkiem pasa doku. */
export function vehiclePose(v, d, kind, sides, slot = 0, entry = null) {
  if ((v.phase === 'enter' || v.phase === 'leave') && Array.isArray(entry?.[0])) {
    // D3: trasa po drogach działki (site-route.routePath: wjazd → pas przed dokiem); wyjazd = ta sama wstecz
    return alongPath(v.phase === 'enter' ? entry : [...entry].reverse(), v.p);
  }
  if ((v.phase === 'enter' || v.phase === 'leave') && entry) {
    // bez trasy (brak przejazdu po terenie albo działka bez dróg) — odcinek prosty jak w D1
    const lane = dockPose(d, QUEUE_M), [a, b] = v.phase === 'enter' ? [entry, [lane.x, lane.y]] : [[lane.x, lane.y], entry];
    const p = Math.max(0, Math.min(1, v.p));
    return { x: a[0] + (b[0] - a[0]) * p, y: a[1] + (b[1] - a[1]) * p, yaw: Math.atan2(-(b[1] - a[1]), b[0] - a[0]) };
  }
  const stand = dockPose(d, STAND_M[kind] ?? STAND_M.truck);
  if (v.phase === 'queue') return queuePose(sides, d, slot);
  if (v.phase === 'dock') return stand;
  const lane = dockPose(d, QUEUE_M), p = v.phase === 'in' ? v.p : 1 - v.p;
  return { x: lane.x + (stand.x - lane.x) * p, y: lane.y + (stand.y - lane.y) * p, yaw: stand.yaw };
}

/** Miejsca pola odkładczego od najbliższego punktu `near` (np. środek doków) — palety rosną od doków. */
export function slotOrder(rect, near) {
  const cols = Math.max(1, Math.floor(rect.w / SLOT_M)), rows = Math.max(1, Math.floor(rect.d / SLOT_M));
  const pts = [];
  for (let r = 0; r < cols * rows; r++) {
    const [x, y] = rectSlot(rect, r);
    pts.push([r, (x - near[0]) ** 2 + (y - near[1]) ** 2]);
  }
  return pts.sort((a, b) => a[1] - b[1]).map(([r]) => r);
}

/** k-ta paleta na polu wg `order` (z warstwami po zapełnieniu) → [x, y, warstwa]. */
export function orderedSlot(rect, order, k) {
  const [x, y] = rectSlot(rect, order[k % order.length]);
  return [x, y, Math.floor(k / order.length)];
}

/** Obsada zajęta w chwili t per proces (oś czasu S3a co `stepS`): {unload, palletize, …}. */
export function crewAt(people, stepS, t) {
  return Object.fromEntries(Object.entries(people || {}).map(([p, s]) => [p, seriesAt(s, stepS, t)]));
}

/** n stanowisk pracy rozdzielonych po kolei na prostokątach (stoły) — po 4 miejsca wokół stołu. */
export function stationSpots(rects, n) {
  const out = [];
  for (let i = 0; i < n && rects.length; i++) {
    const r = rects[i % rects.length];
    const around = [[r.w / 2, -0.5], [-0.5, r.d / 2], [r.w / 2, r.d + 0.5], [r.w + 0.5, r.d / 2]];
    out.push(localToWorld(r, around[Math.floor(i / rects.length) % 4]));
  }
  return out;
}
