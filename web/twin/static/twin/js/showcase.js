// Prezentacja 3D (P1): jedna scena dla całego pokazu (bez przebudowy między slajdami), przeloty kamery,
// plansze KPI, fragmenty animacji dnia (odtwarzacz S4 ładowany leniwie przy pierwszym slajdzie animacji)
// i edytor slajdów dla Projektanta (dodaj bieżące ujęcie, kolejność, podpisy, zapis).
import { createViewer } from './scene-builder.js';
import { bindFullscreenButton } from './fullscreen.js';
import { isoView } from './scene-data.js';
import { docksCam, moveItem, navigate, pickCards, siteBox, slideSeconds, zoneKeys } from './showcase-core.js';

const TYPE_LABEL = { camera: 'Ujęcie', kpi: 'Plansza KPI', bottleneck: 'Wąskie gardło', anim: 'Animacja dnia', text: 'Tekst' };
const hhmm = (s) => `${String(Math.floor(s / 3600) % 24).padStart(2, '0')}:${String(Math.floor(s % 3600 / 60)).padStart(2, '0')}`;

export async function startShowcase({ cfg, el, editable, csrf }) {
  const D = await (await fetch(cfg.data, { credentials: 'same-origin' })).json();
  D.racks.forEach((r, i) => { r._k = `r${i}`; });
  const viewer = createViewer({ canvas: el.canvas, wrap: el.wrap, labels: D.racks.length <= 400, fill: false });
  viewer.setData({ floor: D.floor, racks: D.racks, features: D.features, site: D.site }, { frame: true });
  viewer.setFlyMs(1400);

  let slides = D.slides, i = 0, dirty = false, autoTimer = null, stopAt = null, playerP = null, player = null;

  // ── animacja dnia (leniwie) ──────────────────────────────────────────────────────────────
  function getPlayer() {
    if (!cfg.events || !D.has_events) return Promise.resolve(null);
    playerP ??= (async () => {
      el.status.textContent = 'Ładuję animację dnia…';
      const ev = (await (await fetch(cfg.events, { credentials: 'same-origin' })).json()).events;
      const { createDayPlayer } = await import('./day-player.js');
      player = createDayPlayer({ viewer, data: D, events: ev, ui: {
        onTime(t, playing) {
          el.clock.textContent = hhmm(t);
          if (playing && stopAt !== null && t >= stopAt) { stopAt = null; player.pause(); }
        },
      } });
      el.status.textContent = '';
      return player;
    })();
    return playerP;
  }
  function hideAnim() {
    if (!player) return;
    player.pause();
    player.setVisible(false);
    el.clock.textContent = '';
  }

  // ── kamera ───────────────────────────────────────────────────────────────────────────────
  function goCam(cam) {
    const p = cam?.preset;
    viewer.highlight(p?.startsWith('zone:') ? zoneKeys(D.racks, p.slice(5)) : []);
    if (!p) return viewer.look(...cam.pos, ...cam.target, true);
    if (p.startsWith('zone:')) return viewer.view('sel');
    if (p === 'top') return viewer.view('top');
    const c = p === 'docks' ? docksCam(D.places.docks) : p === 'site' && siteBox(D.site)
      ? isoView(siteBox(D.site), viewer.camera.fov, viewer.camera.aspect) : null;
    return c ? viewer.look(...c.pos, ...c.target, true) : viewer.view('iso');
  }

  // ── slajd ────────────────────────────────────────────────────────────────────────────────
  function renderCards(s) {
    el.kpi.innerHTML = '';
    el.kpi.hidden = s.type !== 'kpi';
    for (const c of s.type === 'kpi' ? pickCards(D.cards, s.cards) : []) {
      const card = document.createElement('section');
      card.className = 'sh-card';
      const h = document.createElement('h3');
      h.textContent = c.title;
      const dl = document.createElement('dl');
      for (const r of c.rows) {
        const dt = document.createElement('dt'), dd = document.createElement('dd');
        dt.textContent = r.label;
        dd.textContent = `${r.value}${r.unit ? ` ${r.unit}` : ''}`;
        if (r.worst && r.worst !== r.value) {
          const w = document.createElement('small');
          w.textContent = `najgorzej ${r.worst}`;
          dd.appendChild(w);
        }
        dl.append(dt, dd);
      }
      card.append(h, dl);
      el.kpi.appendChild(card);
    }
  }
  async function show(k) {
    i = navigate(i, slides.length, k);
    const s = slides[i];
    if (!s) { el.title.textContent = 'Brak slajdów'; return; }
    el.title.textContent = s.title;
    el.caption.textContent = s.caption;
    el.overlay.classList.toggle('is-text', s.type === 'text');
    el.counter.textContent = `${i + 1} / ${slides.length}`;
    el.live.textContent = `Slajd ${i + 1} z ${slides.length}: ${s.title}`;
    el.progress.querySelectorAll('button').forEach((b, j) => b.setAttribute('aria-current', j === i ? 'step' : 'false'));
    el.list?.querySelectorAll('li').forEach((li, j) => li.classList.toggle('is-current', j === i));
    renderCards(s);
    if (s.type === 'anim' || s.type === 'bottleneck') {
      const p = await getPlayer();
      if (slides[i] !== s) return;                          // użytkownik przeszedł dalej w czasie ładowania
      if (!p) { el.caption.textContent = `${s.caption} (ten wynik nie ma zapisanej animacji dnia)`; return; }
      p.setVisible(true);
      if (s.type === 'anim') {
        p.seek(s.t0); p.setSpeed(s.speed); stopAt = s.t1;
        const c = docksCam(D.places.docks);
        if (c) goCam(c);
        p.play();
      } else {
        const b = D.bottlenecks[s.index];
        if (!b) return;
        stopAt = null; p.pause();
        p.seek(b.t0 + Math.min(1800, (b.t1 - b.t0) / 2));
        viewer.highlight([]);
        p.focus(b.keys);
      }
    } else {
      stopAt = null;
      hideAnim();
      if (s.cam) goCam(s.cam);
    }
    if (autoTimer !== null) schedule();
  }

  // ── auto-odtwarzanie ─────────────────────────────────────────────────────────────────────
  function schedule() {
    clearTimeout(autoTimer);
    autoTimer = setTimeout(() => (i < slides.length - 1 ? show('next') : setAuto(false)),
      slideSeconds(slides[i] || {}, +el.autoSec.value || 8) * 1000);
  }
  function setAuto(on) {
    clearTimeout(autoTimer);
    autoTimer = on ? 0 : null;
    el.auto.setAttribute('aria-pressed', String(on));
    el.auto.textContent = on ? 'Zatrzymaj pokaz' : 'Odtwarzaj automatycznie';
    if (on) schedule();
  }

  // ── pasek postępu i edytor ───────────────────────────────────────────────────────────────
  function renderProgress() {
    el.progress.innerHTML = '';
    slides.forEach((s, j) => {
      const b = document.createElement('button');
      b.type = 'button';
      b.title = `${j + 1}. ${s.title}`;
      b.setAttribute('aria-label', `Slajd ${j + 1}: ${s.title}`);
      b.addEventListener('click', () => show(j));
      el.progress.appendChild(b);
    });
  }
  function markDirty(on = true) {
    dirty = on;
    if (el.saveState) el.saveState.textContent = on ? 'Niezapisane zmiany' : 'Zapisano';
  }
  function setSlides(next, focus = i) {
    slides = next;
    renderProgress();
    renderList();
    markDirty();
    return show(Math.min(focus, slides.length - 1));
  }
  function renderList() {
    if (!el.list) return;
    el.list.innerHTML = '';
    slides.forEach((s, j) => {
      const li = document.createElement('li');
      li.draggable = true;
      li.dataset.j = j;
      li.innerHTML = `<div class="sh-row"><span class="sh-type"></span>
        <button type="button" class="btn btn-ghost btn-sm" data-a="show">Pokaż</button>
        <button type="button" class="btn btn-ghost btn-sm" data-a="up" aria-label="Wyżej">↑</button>
        <button type="button" class="btn btn-ghost btn-sm" data-a="down" aria-label="Niżej">↓</button>
        <button type="button" class="btn btn-ghost btn-sm" data-a="cam" title="Zapisz bieżący widok kamery w tym slajdzie">Ujęcie ←</button>
        <button type="button" class="btn btn-ghost btn-sm" data-a="del" aria-label="Usuń slajd">✕</button></div>
        <label>Tytuł <input class="form-control" maxlength="120" data-f="title"></label>
        <label>Podpis <textarea class="form-control" rows="2" maxlength="400" data-f="caption"></textarea></label>`;
      li.querySelector('.sh-type').textContent = `${j + 1}. ${TYPE_LABEL[s.type]}`;
      li.querySelector('[data-a="cam"]').hidden = !(s.type === 'camera' || s.type === 'kpi');
      li.querySelector('[data-f="title"]').value = s.title;
      li.querySelector('[data-f="caption"]').value = s.caption;
      el.list.appendChild(li);
    });
    el.list.querySelectorAll('li').forEach((li, j) => li.classList.toggle('is-current', j === i));
  }
  if (editable && el.list) {
    el.list.addEventListener('click', (e) => {
      const a = e.target.closest('[data-a]')?.dataset.a, j = +e.target.closest('li')?.dataset.j;
      if (!a) return;
      if (a === 'show') show(j);
      else if (a === 'up' || a === 'down') setSlides(moveItem(slides, j, j + (a === 'up' ? -1 : 1)), j + (a === 'up' ? -1 : 1));
      else if (a === 'del') setSlides(slides.filter((_, x) => x !== j), Math.max(0, j - 1));
      else if (a === 'cam') { slides[j] = { ...slides[j], cam: viewer.pose() }; markDirty(); }
    });
    el.list.addEventListener('input', (e) => {
      const f = e.target.dataset.f, j = +e.target.closest('li').dataset.j;
      if (!f) return;
      slides[j] = { ...slides[j], [f]: e.target.value };
      if (j === i) el[f === 'title' ? 'title' : 'caption'].textContent = e.target.value;
      renderProgress();
      markDirty();
    });
    let dragFrom = null;
    el.list.addEventListener('dragstart', (e) => { dragFrom = +e.target.closest('li').dataset.j; });
    el.list.addEventListener('dragover', (e) => e.preventDefault());
    el.list.addEventListener('drop', (e) => {
      e.preventDefault();
      const to = +e.target.closest('li')?.dataset.j;
      if (dragFrom !== null && Number.isFinite(to) && to !== dragFrom) setSlides(moveItem(slides, dragFrom, to), to);
      dragFrom = null;
    });
    el.addCam.addEventListener('click', () => setSlides([...slides.slice(0, i + 1),
      { type: 'camera', title: 'Nowe ujęcie', caption: '', cam: viewer.pose() }, ...slides.slice(i + 1)], i + 1));
    el.addText.addEventListener('click', () => setSlides([...slides.slice(0, i + 1),
      { type: 'text', title: 'Wnioski', caption: '' }, ...slides.slice(i + 1)], i + 1));
    el.save.addEventListener('click', async () => {
      el.saveState.textContent = 'Zapisuję…';
      try {
        const r = await fetch(cfg.save, { method: 'POST', credentials: 'same-origin',
          headers: { 'Content-Type': 'application/json', 'X-CSRFToken': csrf }, body: JSON.stringify({ slides }) });
        const d = await r.json();
        if (!r.ok) { el.saveState.textContent = d.error || `Błąd zapisu (${r.status}).`; return; }
        slides = d.slides;
        renderList();
        markDirty(false);
      } catch {
        el.saveState.textContent = 'Brak połączenia z serwerem — zmiany nie zostały zapisane.';
      }
    });
  }

  // ── sterowanie ───────────────────────────────────────────────────────────────────────────
  el.prev.addEventListener('click', () => show('prev'));
  el.next.addEventListener('click', () => show('next'));
  el.auto.addEventListener('click', () => setAuto(autoTimer === null));
  const fs = bindFullscreenButton(el.fs, el.stage, { live: el.fsLive, onChange: () => { viewer.resize(); viewer.renderNow(); } });
  let down = null;                                            // klik w scenę = dalej (przeciągnięcie = obrót)
  el.canvas.addEventListener('pointerdown', (e) => { down = [e.clientX, e.clientY]; });
  el.canvas.addEventListener('pointerup', (e) => {
    if (down && Math.hypot(e.clientX - down[0], e.clientY - down[1]) < 5) show('next');
    down = null;
  });
  document.addEventListener('keydown', (e) => {
    if (e.ctrlKey || e.metaKey || e.altKey || e.target.closest('input, textarea, select')) return;
    const k = e.key;
    if (k === 'ArrowRight' || k === 'PageDown' || (k === ' ' && !e.target.closest('button'))) { e.preventDefault(); show('next'); }
    else if (k === 'ArrowLeft' || k === 'PageUp') { e.preventDefault(); show('prev'); }
    else if (k === 'Home') show('first');
    else if (k === 'End') show('last');
    else if (k.toLowerCase() === 'f') fs.toggle();
  });
  window.addEventListener('beforeunload', (e) => { if (dirty) e.preventDefault(); });

  renderProgress();
  renderList();
  await show(0);
  window.tw3dReady();
  if (new URLSearchParams(location.search).has('debug3d')) window.__twShow = { show, viewer, getPlayer, get i() { return i; } };
}
