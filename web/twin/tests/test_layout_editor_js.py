"""Czyste funkcje JS edytora layoutu (static/twin/js/layout-core.js): testy `node --test` + zgodność
konwencji z Pythonem (narożniki jak blender_route, blok z „Dodaj blok” bez kolizji wg twin.layout).
Bez Node na maszynie testy są pomijane (CI na ubuntu-latest ma Node)."""
import json
import shutil
import subprocess
import unittest
from pathlib import Path

from twin.blender_route import rack_corners
from twin.layout import analyze, rack_geom

TWIN = Path(__file__).resolve().parent.parent
CORE = (TWIN / "static" / "twin" / "js" / "layout-core.js").as_uri()
NODE = shutil.which("node")


def node_eval(code):
    out = subprocess.run([NODE, "--input-type=module", "-e", code], capture_output=True, text=True,
                         timeout=60, check=True)
    return json.loads(out.stdout)


@unittest.skipUnless(NODE, "brak Node.js")
class LayoutCoreJsTests(unittest.TestCase):
    def test_node_unit_tests(self):
        proc = subprocess.run([NODE, "--test", str(TWIN / "tests" / "js" / "layout_core.test.mjs"),
                               str(TWIN / "tests" / "js" / "scene_data.test.mjs"),
                               str(TWIN / "tests" / "js" / "scene_look.test.mjs"),
                               str(TWIN / "tests" / "js" / "fullscreen.test.mjs"),
                               str(TWIN / "tests" / "js" / "day_timeline.test.mjs")],
                              capture_output=True, text=True, timeout=120)
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)

    def test_corners_match_python(self):
        racks = [{"zone": "A", "rack_id": f"{i:03d}", "x": 3.0 + i, "y": 4.0, "angle": a, "n_bays": 5,
                  "n_levels": 3, "bay_width_cm": 270, "depth_cm": 110, "level_height_cm": 180}
                 for i, a in enumerate((0, 30, 90, 135, 270))]
        js = node_eval(f"import {{corners}} from '{CORE}'; "
                       f"console.log(JSON.stringify({json.dumps(racks)}.map(corners)))")
        for r, c in zip(racks, js, strict=True):
            for (px, py), (jx, jy) in zip(rack_corners(rack_geom(r)), c, strict=True):
                self.assertAlmostEqual(px, jx, places=9)
                self.assertAlmostEqual(py, jy, places=9)

    def test_js_block_has_no_collisions_in_python(self):
        racks = node_eval(
            f"import {{makeBlock}} from '{CORE}'; console.log(JSON.stringify(makeBlock({{x: 2, y: 2, rows: 6, "
            "bays: 10, levels: 5, bayWidthCm: 270, depthCm: 110, levelHeightCm: 180, aisle: 3.0, zone: 'V', "
            "ids: ['001','002','003','004','005','006']})))")
        layout = {"floor": {"width": 40, "depth": 30}, "racks": racks, "features": [], "version": ""}
        _, issues = analyze(layout)
        self.assertEqual([i for i in issues if i["severity"] == "error"], [])
        self.assertEqual([i for i in issues if i["code"] == "aisle"], [])   # 3 m = alejka reach trucka
