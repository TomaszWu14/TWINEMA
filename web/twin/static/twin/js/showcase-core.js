// Prezentacja 3D (P1) — czyste funkcje odtwarzacza i edytora slajdów (testy: tests/js/showcase.test.mjs).
import { sitePlan } from './scene-data.js';

/** Prostokąt kadru działki w osiach sceny (x, z = y hali) — do `isoView`. null bez działki. */
export function siteBox(site) {
  const plan = sitePlan(site);
  if (!plan) return null;
  const xs = plan.plot.map((p) => p[0]), zs = plan.plot.map((p) => p[1]);
  const x0 = Math.min(...xs), x1 = Math.max(...xs), z0 = Math.min(...zs), z1 = Math.max(...zs);
  return { cx: (x0 + x1) / 2, cz: (z0 + z1) / 2, x: x1 - x0, z: z1 - z0 };
}

/** Kadr doków (jak `frameDocks` animacji dnia): z placu, z boku, cel w hali za dokami. Najpierw doki przyjęć. */
export function docksCam(docks) {
  const all = Object.values(docks || {});
  const ins = all.filter((d) => d.role.startsWith('in_'));
  const base = ins.length ? ins : all;
  if (!base.length) return null;
  const o = base[0].out, ds = base.filter((d) => d.out[0] === o[0] && d.out[1] === o[1]);
  const cx = ds.reduce((a, d) => a + d.wall[0], 0) / ds.length, cy = ds.reduce((a, d) => a + d.wall[1], 0) / ds.length;
  const span = Math.max(20, ...ds.map((d) => Math.hypot(d.wall[0] - cx, d.wall[1] - cy) * 2)), k = span * 0.6 + 30;
  const tg = [Math.abs(o[1]), Math.abs(o[0])];
  return { pos: [cx + o[0] * k + tg[0] * k * 0.55, k * 0.55, cy + o[1] * k + tg[1] * k * 0.55],
    target: [cx - o[0] * 18, 0, cy - o[1] * 18] };
}

/** Klucze regałów strefy (regały mają `_k` = `r<indeks>` nadane przez odtwarzacz). */
export function zoneKeys(racks, zone) {
  return racks.filter((r) => r.zone === zone).map((r) => r._k);
}

/** Nawigacja: 'next' | 'prev' | 'first' | 'last' | liczba (skok) → nowy indeks w [0, n-1]. */
export function navigate(i, n, action) {
  if (!n) return 0;
  const to = { next: i + 1, prev: i - 1, first: 0, last: n - 1 }[action] ?? Number(action);
  return Math.max(0, Math.min(n - 1, Number.isFinite(to) ? to : i));
}

/** Karty KPI slajdu w kolejności z `keys`, pomijając niedostępne (np. bez działki). */
export function pickCards(cards, keys) {
  return (keys || []).filter((k) => cards && cards[k]).map((k) => ({ key: k, ...cards[k] }));
}

/** Czas slajdu przy auto-odtwarzaniu [s]: fragment animacji trwa tyle, ile jego czas dnia ÷ prędkość. */
export function slideSeconds(slide, base = 8) {
  if (slide.type === 'anim') return Math.max(base, (slide.t1 - slide.t0) / slide.speed);
  return base;
}

/** Przeniesienie slajdu (przeciąganie, ↑ ↓) — nowa lista, oryginał bez zmian. */
export function moveItem(list, from, to) {
  const out = list.slice();
  if (from < 0 || from >= out.length) return out;
  const [x] = out.splice(from, 1);
  out.splice(Math.max(0, Math.min(out.length, to)), 0, x);
  return out;
}
