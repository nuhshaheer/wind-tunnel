"""Tests for scripts/check_mesh.py on small synthetic 3MF files (solids of revolution and boxes)."""
import contextlib
import io
import math
import shutil
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import check_mesh  # noqa: E402

N = 96  # segments around each solid of revolution (divisible by 4, so the bounding box is exact)


def revolve(profile, n=N):
    """Closed mesh of a profile [(r, z), ...] (a closed polygon, every r > 0) turned about the z axis."""
    verts = [(r * math.cos(2 * math.pi * j / n), r * math.sin(2 * math.pi * j / n), z)
             for r, z in profile for j in range(n)]
    m = len(profile)
    tris = []
    for i in range(m):
        for j in range(n):
            a, b = i * n + j, ((i + 1) % m) * n + j
            c, d = ((i + 1) % m) * n + (j + 1) % n, i * n + (j + 1) % n
            tris += [(a, b, c), (a, c, d)]
    return verts, tris


def box(x0, y0, z0, x1, y1, z1):
    v = [(x0, y0, z0), (x1, y0, z0), (x1, y1, z0), (x0, y1, z0), (x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)]
    t = [(0, 2, 1), (0, 3, 2), (4, 5, 6), (4, 6, 7), (0, 1, 5), (0, 5, 4),
         (1, 2, 6), (1, 6, 5), (2, 3, 7), (2, 7, 6), (3, 0, 4), (3, 4, 7)]
    return v, t


def write_3mf(path, bodies, item_transform=None, as_component=False):
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<model unit="millimeter" xmlns="http://schemas.microsoft.com/3dmanufacturing/core/2015/02"><resources>']
    for k, (vs, ts) in enumerate(bodies, start=1):
        out.append(f'<object id="{k}" type="model" name="Body{k}"><mesh><vertices>')
        out += [f'<vertex x="{x!r}" y="{y!r}" z="{z!r}"/>' for x, y, z in vs]
        out.append('</vertices><triangles>')
        out += [f'<triangle v1="{a}" v2="{b}" v3="{c}"/>' for a, b, c in ts]
        out.append('</triangles></mesh></object>')
    ids = list(range(1, len(bodies) + 1))
    if as_component:
        out.append(f'<object id="{len(bodies) + 1}" type="model"><components>')
        out += [f'<component objectid="{k}" transform="{item_transform}"/>' for k in ids]
        out.append('</components></object>')
        items = [f'<item objectid="{len(bodies) + 1}"/>']
    else:
        tr = f' transform="{item_transform}"' if item_transform else ""
        items = [f'<item objectid="{k}"{tr}/>' for k in ids]
    out.append('</resources><build>' + "".join(items) + '</build></model>')
    with zipfile.ZipFile(path, "w") as z:
        z.writestr("3D/3dmodel.model", "\n".join(out))


# A tube with a flange at the bottom and a 45-degree chamfer under it: bore D30, flange D50 for z 0-4,
# chamfer from D50 at z 4 to D34 at z 12, then the D34 tube to z 30.
FLANGED_TUBE = [(15, 0), (25, 0), (25, 4), (17, 12), (17, 30), (15, 30)]


class CheckMeshTest(unittest.TestCase):
    def setUp(self):
        self.dir = Path(tempfile.mkdtemp(prefix="check_mesh_test_"))

    def tearDown(self):
        shutil.rmtree(self.dir, ignore_errors=True)

    def make(self, bodies, name="part.3mf", **kw):
        path = self.dir / name
        write_3mf(path, bodies, **kw)
        return str(path)

    def run_main(self, argv):
        out = io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(out):
            code = check_mesh.main(argv)
        return code, out.getvalue()

    # ---- loading and solid checks

    def test_closed_tube_volume(self):
        unit, bodies = check_mesh.load_3mf(self.make([revolve([(15, 0), (25, 0), (25, 30), (15, 30)])]))
        self.assertEqual(unit, "millimeter")
        stats = check_mesh.mesh_stats(bodies[0])
        self.assertTrue(stats["closed"])
        self.assertEqual(stats["pieces"], 1)
        polygon = N / 2 * math.sin(2 * math.pi / N)  # area of an N-gon of unit radius
        self.assertAlmostEqual(abs(stats["volume"]), polygon * (25 ** 2 - 15 ** 2) * 30, places=3)

    def test_bodies_and_pieces_counted(self):
        a, b = box(0, 0, 0, 10, 10, 10), box(20, 0, 0, 30, 10, 10)
        _, bodies = check_mesh.load_3mf(self.make([a, b]))
        self.assertEqual(len(bodies), 2)
        joined = (a[0] + b[0], a[1] + [(i + 8, j + 8, k + 8) for i, j, k in b[1]])
        _, bodies = check_mesh.load_3mf(self.make([joined], "joined.3mf"))
        self.assertEqual(check_mesh.mesh_stats(bodies[0])["pieces"], 2)

    def test_open_mesh_detected(self):
        v, t = box(0, 0, 0, 10, 10, 10)
        _, bodies = check_mesh.load_3mf(self.make([(v, t[:-1])]))
        self.assertFalse(check_mesh.mesh_stats(bodies[0])["closed"])

    def test_transforms_applied(self):
        move = "1 0 0 0 1 0 0 0 1 0 0 100"
        for as_component in (False, True):
            _, bodies = check_mesh.load_3mf(self.make([box(0, 0, 0, 10, 10, 10)], f"m{as_component}.3mf",
                                                      item_transform=move, as_component=as_component))
            self.assertEqual(check_mesh.bounds(bodies)[2], (100.0, 110.0))

    def test_not_a_3mf(self):
        bad = self.dir / "part.f3d"
        bad.write_bytes(b"not a zip")
        code, out = self.run_main(["info", str(bad)])
        self.assertEqual(code, 2)
        self.assertIn("not a 3MF", out)

    # ---- sections

    def test_section_reads_true_hole_diameter(self):
        _, bodies = check_mesh.load_3mf(self.make([revolve([(2, 0), (6, 0), (6, 5), (2, 5)])]))
        loops, open_chains = check_mesh.section(bodies, "z", 2.5)
        self.assertEqual(open_chains, 0)
        kinds = sorted((L.kind, L.describe()) for L in loops)
        self.assertEqual(kinds, [("hole", "round D4.000"), ("outline", "round D12.000")])

    def test_square_tube_section_and_rays(self):
        outer, inner = box(-140, -140, 0, 140, 140, 6), box(-125, -125, 0, 125, 125, 6)
        flipped = (inner[0], [(a, c, b) for a, b, c in inner[1]])  # the bore's faces point inward
        _, bodies = check_mesh.load_3mf(self.make([(outer[0] + flipped[0],
                                                    outer[1] + [(a + 8, b + 8, c + 8) for a, b, c in flipped[1]])]))
        loops, _ = check_mesh.section(bodies, "z", 3)
        self.assertEqual([(L.kind, L.describe()) for L in loops],
                         [("outline", "rect 280.000 x 280.000"), ("opening", "rect 250.000 x 250.000")])
        hits = check_mesh.ray_hits(loops, (0, 0), 45)
        self.assertEqual(len(hits), 2)  # through the corners, each counted once
        self.assertAlmostEqual(hits[0], 125 * math.sqrt(2), places=6)

    def test_hexagon_described_across_flats(self):
        r = 6 / math.sqrt(3)  # corner radius of a hexagon 6 across the flats
        loop = check_mesh.Loop([(r * math.cos(math.pi / 3 * k), r * math.sin(math.pi / 3 * k)) for k in range(6)])
        self.assertEqual(loop.describe(), "hex 6.000 across flats")

    # ---- layers

    def test_layers_flange_chamfer_tube(self):
        _, bodies = check_mesh.load_3mf(self.make([revolve(FLANGED_TUBE)]))
        levels, runs = check_mesh.layers(bodies, "z")
        self.assertEqual(levels, [0, 4, 12, 30])
        self.assertEqual([(r.lo, r.hi, r.changing) for r in runs], [(0, 4, False), (4, 12, True), (12, 30, False)])
        chamfer = runs[1]
        self.assertTrue(chamfer.straight)
        self.assertAlmostEqual(chamfer.start_sizes[0], 50.0, places=3)
        self.assertAlmostEqual(chamfer.end_sizes[0], 34.0, places=3)
        self.assertEqual([L.describe() for L in runs[2].mid.outlines], ["round D34.000"])

    def test_layers_flags_a_fillet_as_curved(self):
        # The flanged tube with a radius-8 fillet (centre r 25, z 12) instead of the chamfer: (25, 4) round to (17, 12)
        fillet = [(25 - 8 * math.sin(math.pi / 2 * k / 12), 12 - 8 * math.cos(math.pi / 2 * k / 12)) for k in range(13)]
        profile = [(15, 0), (25, 0)] + fillet + [(17, 30), (15, 30)]
        _, bodies = check_mesh.load_3mf(self.make([revolve(profile)]))
        _, runs = check_mesh.layers(bodies, "z")
        changing = [r for r in runs if r.changing]
        self.assertEqual(len(changing), 1)
        self.assertFalse(changing[0].straight)
        self.assertGreater(changing[0].deviations[0], 1.0)

    def test_small_boss_on_a_flat_wall_starts_a_new_stretch(self):
        # A 6 wide boss standing 8 proud of a 256 square wall barely changes the area (Settling Chamber 3, 2026-11-27)
        def slice_of(outline_pts):
            outer, inner = check_mesh.Loop(outline_pts), check_mesh.Loop([(-125, -125), (125, -125), (125, 125), (-125, 125)])
            outer.depth, inner.depth = 0, 1
            return check_mesh.Slice([outer, inner], 0)
        plain = slice_of([(-128, -128), (128, -128), (128, 128), (-128, 128)])
        boss = slice_of([(-128, -128), (17, -128), (17, -136), (23, -136), (23, -128), (128, -128), (128, 128), (-128, 128)])
        self.assertNotEqual(plain.signature, boss.signature)
        self.assertLess(abs(plain.dsizes[0] - boss.dsizes[0]), check_mesh.NOISE * 1.5)  # area alone would miss it

    # ---- hole patterns and matching

    def test_pattern_symmetric_square(self):
        pts = [(sx * a, sy * b) for a, b in ((134, 134), (45, 134), (134, 45)) for sx in (1, -1) for sy in (1, -1)]
        self.assertEqual(check_mesh.describe_pattern(pts), "at (+-45, +-134), (+-134, +-45), (+-134, +-134)")

    def test_pattern_bolt_circle(self):
        pts = [(85 * math.cos(math.radians(a)), 85 * math.sin(math.radians(a))) for a in range(0, 360, 60)]
        self.assertEqual(check_mesh.describe_pattern(pts),
                         "on a D170.000 circle at 0, 60, 120, 180, 240, 300 deg")

    def test_match_holes(self):
        a = [(134, 134), (-134, 45), (0, 59)]
        b = [(134.02, 134), (-134, 45), (59, 0)]
        pairs, ua, ub = check_mesh.match_holes(a, b, tol=0.5)
        self.assertEqual(sorted((i, j) for i, j, _ in pairs), [(0, 0), (1, 1)])
        self.assertAlmostEqual(max(d for _, _, d in pairs), 0.02, places=6)
        self.assertEqual((ua, ub), ([2], [2]))

    # ---- command line

    def test_cli_runs(self):
        path = self.make([revolve(FLANGED_TUBE)])
        code, out = self.run_main(["info", path])
        self.assertEqual(code, 0, out)
        self.assertIn("closed solid", out)
        self.assertIn("fits", out)
        code, out = self.run_main(["layers", path])
        self.assertEqual(code, 0, out)
        self.assertIn("CHANGING: outline straight, opening unchanged", out)
        code, out = self.run_main(["cut", path, "20", "--rays", "0,90"])
        self.assertEqual(code, 0, out)
        self.assertIn("ray 0 deg from (0, 0): 15.000, 17.000", out)
        code, out = self.run_main(["match", path, "2", path, "2"])
        self.assertEqual(code, 1, out)  # no holes to match


if __name__ == "__main__":
    unittest.main()
