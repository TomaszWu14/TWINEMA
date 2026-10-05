// Animacja dnia scenariusza (S4) — czyste funkcje (bez three.js i DOM), testowane `node --test`
// (twin/tests/js/day_timeline.test.mjs). Wejście: zdarzenia `twinema.scenario-events` v1
// [t_s, obj, kind, what, place, n?] posortowane po czasie (opis: scenario/sim/__init__.py).
import { localToWorld } from './scene-data.js';

export const VEHICLES = new Set(['container', 'truck', 'courier']);
export const TRAVEL_S = 90;          // dojazd brama → dok / odjazd dok → brama
export const MOVE_MAX_S = 120;       // przejazd palety regał → pole wydań (koniec ruchu znamy, początku nie)
export const SLOT_M = 1.4;           // pitch palety na polu odkładczym (EUR 1,2 × 0,8 + odstęp)

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

/** Pojazd w chwili t → null (poza sceną) | {phase: 'queue'|'in'|'dock'|'out', dock, p}. */
export function vehicleAt(tr, t) {
  const tArr = tr.t[tr.what.indexOf('arrive')] ?? tr.t0;
  const iDock = tr.what.indexOf('dock'), iDep = tr.what.indexOf('depart');
  if (t < tArr || iDock < 0) return null;
  const dock = tr.place[iDock].slice(5), tDock = tr.t[iDock];
  const tDep = iDep >= 0 ? tr.t[iDep] : tDock + 1800;          // kurier bez „depart” (stary format): 30 min
  if (t < tDock - TRAVEL_S && t >= tArr) return { phase: 'queue', dock, p: 0 };
  if (t < tDock) return { phase: 'in', dock, p: 1 - (tDock - t) / TRAVEL_S };
  if (t < tDep) return { phase: 'dock', dock, p: 0 };
  if (t < tDep + TRAVEL_S) return { phase: 'out', dock, p: (t - tDep) / TRAVEL_S };
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
