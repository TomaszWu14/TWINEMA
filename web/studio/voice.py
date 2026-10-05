"""Lektor i napisy (czysty Python — bez Django i bez sieci).

  • `voice_key` — hash wejścia TTS (tekst + głos + model): ta sama kwestia = to samo audio z cache,
    poprawka jednego zdania nagrywa tylko tę kwestię.
  • `words` / `duration` — z wyrównania znaków ElevenLabs (character_start/end_times_seconds).
  • `cues` — podział kwestii na napisy: ≤ 2 linie po ≤ 42 znaki, ≤ 6 s na planszę.
  • `build_srt` — plik SRT z kwestii przesuniętych o początek ujęcia na osi filmu.
"""
import hashlib
import json

LINE_CHARS, MAX_LINES, MAX_CUE_S = 42, 2, 6.0


def voice_key(text, voice_id, model_id):
    raw = json.dumps([text.strip(), voice_id, model_id], ensure_ascii=False)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def duration(alignment):
    ends = (alignment or {}).get("character_end_times_seconds") or []
    return round(max(ends), 3) if ends else 0.0


def words(alignment):
    """[(słowo, start, koniec)] ze znaków; białe znaki rozdzielają słowa."""
    al = alignment or {}
    chars = al.get("characters") or []
    starts = al.get("character_start_times_seconds") or []
    ends = al.get("character_end_times_seconds") or []
    out, cur, t0, t1 = [], "", None, None
    for ch, s, e in zip(chars, starts, ends, strict=False):     # dane z API: nadmiar ucinamy
        if ch.isspace():
            if cur:
                out.append((cur, t0, t1))
            cur, t0 = "", None
            continue
        if t0 is None:
            t0 = s
        cur, t1 = cur + ch, e
    if cur:
        out.append((cur, t0, t1))
    return out


def _wrap(ws):
    """Słowa → linie po ≤ LINE_CHARS znaków."""
    lines = [""]
    for w in ws:
        if lines[-1] and len(lines[-1]) + 1 + len(w) > LINE_CHARS:
            lines.append(w)
        else:
            lines[-1] = f"{lines[-1]} {w}".strip()
    return lines


def cues(word_times):
    """Słowa z czasami → [(start, koniec, tekst z \\n)]. Nowa plansza, gdy przekroczony limit
    linii albo czasu; po kropce plansza się kończy, jeśli ma już ≥ 1 linię treści."""
    out, cur = [], []
    for w in word_times:
        trial = cur + [w]
        too_long = len(_wrap([x[0] for x in trial])) > MAX_LINES or (cur and w[2] - cur[0][1] > MAX_CUE_S)
        if cur and too_long:
            out.append(cur)
            cur = [w]
        else:
            cur = trial
        if cur and cur[-1][0].endswith((".", "!", "?")) and len(" ".join(x[0] for x in cur)) >= LINE_CHARS * 0.6:
            out.append(cur)
            cur = []
    if cur:
        out.append(cur)
    return [(c[0][1], c[-1][2], "\n".join(_wrap([x[0] for x in c]))) for c in out]


def srt_time(t):
    ms = int(round(max(t, 0) * 1000))
    h, ms = divmod(ms, 3_600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def build_srt(segments):
    """segments: [(przesunięcie_s, cues)] → tekst SRT (numeracja od 1, CRLF niepotrzebny)."""
    blocks = []
    for offset, cs in segments:
        for start, end, text in cs:
            blocks.append(f"{len(blocks) + 1}\n{srt_time(offset + start)} --> {srt_time(offset + end)}\n{text}\n")
    return "\n".join(blocks)


def offsets(durations, gap_s=0.0, start_s=0.0):
    """Początki kolejnych ujęć na osi filmu (gap = pauza między ujęciami)."""
    out, t = [], start_s
    for d in durations:
        out.append(round(t, 3))
        t += d + gap_s
    return out
