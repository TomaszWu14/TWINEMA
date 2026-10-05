"""TWINEMA → Blender: render ujęcia (preset kamery) ze sceny „twinema.scene”.

Buduje scenę skryptem `twinema_warehouse_anim.py`, ustawia kamerę wg presetu i renderuje
kadr PNG albo klip MP4. Używa go worker renderów (`tools/render_worker.py`), da się też ręcznie:

  blender -b -P tools/blender/twinema_render.py -- scena.json wynik.mp4 \
      [--preset przelot|orbita|przejazd|plan|ogolny] [--seconds 12] [--res 1280x720] \
      [--engine eevee|cycles|workbench] [--samples 16] [--fps 24] [--speed 4] [--no-agents]

Rozszerzenie pliku wyniku decyduje: .png = jeden kadr (środek klipu), .mp4 = klip.
Kamera ma klatki kluczowe na całym klipie, więc ujęcie „jedzie” razem z animacją przepływów.
"""
import math
import os
import runpy
import sys

import bpy

HERE = os.path.dirname(os.path.abspath(globals().get("__file__", "twinema_render.py")))
ANIM = runpy.run_path(os.path.join(HERE, "twinema_warehouse_anim.py"), run_name="twinema_lib")

PRESETS = {
    "ogolny": "Widok ogólny — statyczna kamera z narożnika hali",
    "przelot": "Przelot nad halą — od jednego krańca do drugiego",
    "orbita": "Orbita — pełny obrót wokół środka hali",
    "przejazd": "Przejazd nisko wzdłuż hali — perspektywa operatora",
    "plan": "Plan z góry — rzut ortogonalny całej hali",
}


def _key(ob, frame, loc):
    ob.location = loc
    ob.keyframe_insert("location", frame=frame)


def apply_preset(preset, floor, frames):
    """Ustawia „Kamerę TWINEMA” i jej cel wg presetu na klatkach 1…frames."""
    cam = bpy.data.objects["Kamera TWINEMA"]
    target = bpy.data.objects["Cel kamery"]
    w, d = floor["width"], floor["depth"]
    bl = ANIM["_bl"]
    cx, cy = bl(w / 2, d / 2)[:2]
    diag = math.hypot(w, d)
    span_x = bl(w, 0)[0] - bl(0, 0)[0]                   # znak osi X w układzie Blendera
    span_y = bl(0, d)[1] - bl(0, 0)[1]
    if preset == "plan":
        cam.data.type = "ORTHO"
        cam.data.ortho_scale = max(w, d * 16 / 9) * 1.08
        _key(cam, 1, (cx, cy, diag))
        _key(target, 1, (cx, cy, 0))
        return
    cam.data.type = "PERSP"
    if preset == "ogolny":
        return                                            # kamera z twinema_warehouse_anim
    if preset == "przelot":
        h = max(8.0, diag * 0.28)
        _key(cam, 1, (cx - span_x * 0.55, cy - span_y * 0.75, h))
        _key(cam, frames, (cx + span_x * 0.55, cy - span_y * 0.35, h * 0.8))
        _key(target, 1, (cx - span_x * 0.2, cy, 0))
        _key(target, frames, (cx + span_x * 0.3, cy, 0))
    elif preset == "orbita":
        r, h = diag * 0.62, diag * 0.32
        steps = 12
        for i in range(steps + 1):
            a = -math.pi / 2 + 2 * math.pi * i / steps
            _key(cam, 1 + round((frames - 1) * i / steps), (cx + r * math.cos(a), cy + r * math.sin(a), h))
        _key(target, 1, (cx, cy, 0))
    elif preset == "przejazd":
        y = cy - span_y * 0.52                            # tuż przed czołem regałów, od strony doków
        _key(cam, 1, (cx - span_x * 0.48, y, 3.2))
        _key(cam, frames, (cx + span_x * 0.48, y, 3.2))
        _key(target, 1, (cx - span_x * 0.3, cy, 1.2))
        _key(target, frames, (cx + span_x * 0.6, cy, 1.2))
        cam.data.lens = 24
    else:
        raise ValueError(f"Nieznany preset kamery: {preset} (dostępne: {', '.join(PRESETS)})")
    mode = "LINEAR" if preset == "orbita" else "BEZIER"     # orbita równo, przeloty z łagodnym startem
    ANIM["_interp"](cam, mode)
    ANIM["_interp"](target, mode)


def render(scene_path, out, *, preset="przelot", seconds=12, res=(1280, 720), engine="eevee",
           samples=16, fps=24, speed=4.0, agents=True):
    stats = ANIM["build"](scene_path, fps=fps, speed=speed, agents=agents)
    sc = bpy.context.scene
    frames = max(2, min(sc.frame_end, round(seconds * fps)))
    sc.frame_start, sc.frame_end = 1, frames
    floor = dict(ANIM["_FLOOR"])
    apply_preset(preset, floor, frames)
    ANIM["_set_engine"](sc, engine, samples)
    sc.render.resolution_x, sc.render.resolution_y = res
    sc.render.resolution_percentage = 100
    out = os.path.abspath(out)
    if out.lower().endswith(".png"):
        sc.frame_set(max(1, frames // 2))
        sc.render.image_settings.file_format = "PNG"
        sc.render.filepath = out
        bpy.ops.render.render(write_still=True)
    elif out.lower().endswith(".mp4"):
        _video_settings(sc)
        sc.render.filepath = out
        bpy.ops.render.render(animation=True)
    else:
        raise ValueError("Wynik musi być .png albo .mp4")
    return {**stats, "frames": frames, "preset": preset, "out": out}


def _video_settings(sc):
    """FFmpeg H.264 w MP4 — Blender 5 przeniósł format wideo do `media_type`."""
    ims = sc.render.image_settings
    if hasattr(ims, "media_type"):
        ims.media_type = "VIDEO"
    ims.file_format = "FFMPEG"
    sc.render.ffmpeg.format = "MPEG4"
    sc.render.ffmpeg.codec = "H264"
    sc.render.ffmpeg.constant_rate_factor = "MEDIUM"


def main(argv):
    import argparse
    p = argparse.ArgumentParser(description="TWINEMA → Blender: render ujęcia")
    p.add_argument("scene")
    p.add_argument("out", help="wynik: .png (kadr) albo .mp4 (klip)")
    p.add_argument("--preset", default="przelot", choices=list(PRESETS))
    p.add_argument("--seconds", type=float, default=12)
    p.add_argument("--res", default="1280x720")
    p.add_argument("--engine", default="eevee", choices=["eevee", "cycles", "workbench"])
    p.add_argument("--samples", type=int, default=16)
    p.add_argument("--fps", type=int, default=24)
    p.add_argument("--speed", type=float, default=4.0)
    p.add_argument("--no-agents", action="store_true")
    a = p.parse_args(argv)
    w, h = (int(v) for v in a.res.lower().split("x"))
    info = render(a.scene, a.out, preset=a.preset, seconds=a.seconds, res=(w, h), engine=a.engine,
                  samples=a.samples, fps=a.fps, speed=a.speed, agents=not a.no_agents)
    print("TWINEMA_RENDER_OK", info)


if __name__ == "__main__":
    main(sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else [])
