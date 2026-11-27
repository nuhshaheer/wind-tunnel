#!/usr/bin/env python3
"""Measure a 3MF mesh exported from Fusion 360, to check the owner's CAD against the sizing sheets. Read-only.

    python scripts/check_mesh.py info FILE [FILE ...]
    python scripts/check_mesh.py layers FILE [--axis z]
    python scripts/check_mesh.py cut FILE AT [AT ...] [--axis z] [--rays 0,45] [--centre X,Y] [--list]
    python scripts/check_mesh.py match FILE_A AT_A FILE_B AT_B [--axis z] [--rotate DEG] [--mirror x|y] [--tol 0.5]

Used by the /check-cad skill (.claude/skills/check-cad/SKILL.md). Standard library only.

Input: a .3mf file (a zip holding XML: vertices, triangles, build transforms). Lengths are in the file's unit, which is
millimetres for Fusion's 3MF exports; volumes in cm^3. AXIS is the part's length direction (x, y or z; default z).
Positions in a cut are model coordinates in the other two axes (z: x,y; y: x,z; x: y,z).

info    for each body: closed solid or not, connected pieces, triangles, volume; the overall size; whether it fits the
        P1S bed (256 mm cube, axis-aligned); the mass if printed solid in PLA (1.24 g/cm^3, an upper bound).
layers  every plane along AXIS where the shape changes, and the cross-section between them: the outline (outside),
        any opening (a large void such as the duct), and the holes (count, size, bolt pattern). A stretch whose size
        changes (chamfer, fillet, loft) is reported from start to end with its middle value, and as "straight" (a
        chamfer or a cone) or "curved" (a fillet or a loft) with its largest departure from a straight line.
cut     the full section at chosen planes: every outline, opening and hole, with centres; --rays gives the distances
        at which rays from the centre cross the walls (inside and outside radii); --list prints every hole.
match   compares the hole centres on two mating faces, one section in each file, after an optional mirror and
        rotation of the second.

How sizes are read: a loop with 4 right-angled corners is "rect W x H"; a regular hexagon is "hex F across flats";
12 or more vertices all at one distance from the centre is "round D", taken from the vertices, which lie on the
true circle (the area would read about 0.5 % small); anything else is "N-sided W x H" (its bounding box).
"""
from __future__ import annotations

import argparse
import math
import sys
import zipfile
import xml.etree.ElementTree as ET

CORE = "{http://schemas.microsoft.com/3dmanufacturing/core/2015/02}"
PROD = "{http://schemas.microsoft.com/3dmanufacturing/production/2015/06}"
AXES = "xyz"
BED_MM = 256.0            # Bambu Lab P1S build volume per side (manufacturer spec)
PLA_G_PER_CM3 = 1.24      # typical PLA density, for an upper-bound mass
HOLE_MAX_D = 16.0         # a void up to this size (area-equivalent diameter, mm) is a "hole"; larger is an "opening"
SIZE_TOL = 1e-3           # sizes closer than this (mm) count as equal
NOISE = 0.1               # a loop's area-equivalent size must change by more than this (mm) to count as changing:
#                           curved faces are drawn with slanted triangles, so sections jitter by a few hundredths
STRAIGHT_TOL = 0.05       # a changing stretch within this (mm) of a straight line is "straight" (chamfer, cone)
SLIVER = 0.05             # stretches shorter than this (mm) between vertex planes are merged into their neighbour
SHORT = 1.0               # a nearly flat stretch shorter than this (mm) between two stretches changing the same way
#                           is part of one curve (lofts leave such slices); longer flat stretches are kept as lands
PATTERN_MAX = 24          # list a hole pattern only up to this many holes
FLAT_MAX = 40             # loops with fewer corners than this are straight-sided: a change in their corner count
#                           (a boss on a flat wall, a notch) starts a new stretch even when the area hardly changes
BOX_TOL = 0.5             # bounding-box sizes must also agree within this (mm) for a stretch to count as constant


# --------------------------------------------------------------------------- loading

class Body:
    """One mesh object: vertices welded by position, triangles as vertex-index triples."""

    def __init__(self, name, verts, tris):
        self.name = name
        self.verts = verts
        self.tris = tris
        self._index = None

    def triangles_crossing(self, ai, c):
        """Triangles whose extent along axis ai contains c (bucketed, so long parts cut quickly)."""
        if self._index is None or self._index[0] != ai:
            lo = min(p[ai] for p in self.verts)
            hi = max(p[ai] for p in self.verts)
            n = max(1, min(256, len(self.tris) // 64))
            width = (hi - lo) / n or 1.0
            buckets = [[] for _ in range(n)]
            for t in self.tris:
                zs = [self.verts[k][ai] for k in t]
                b0 = min(n - 1, int((min(zs) - lo) / width))
                b1 = min(n - 1, int((max(zs) - lo) / width))
                for b in range(b0, b1 + 1):
                    buckets[b].append(t)
            self._index = (ai, lo, width, n, buckets)
        _, lo, width, n, buckets = self._index
        b = int((c - lo) / width)
        if b < 0 or b >= n + 1:
            return []
        return buckets[min(n - 1, b)]


def _transform(text):
    if not text:
        return None
    m = [float(t) for t in text.split()]
    if len(m) != 12:
        raise ValueError(f"bad 3MF transform: {text!r}")
    return m


def _apply(m, p):
    if m is None:
        return p
    x, y, z = p
    return (x * m[0] + y * m[3] + z * m[6] + m[9],
            x * m[1] + y * m[4] + z * m[7] + m[10],
            x * m[2] + y * m[5] + z * m[8] + m[11])


def _compose(first, then):
    """The transform that applies `first`, then `then` (3MF uses row vectors: p' = p M)."""
    if first is None:
        return then
    if then is None:
        return first

    def full(m):
        return [[m[0], m[1], m[2], 0.0], [m[3], m[4], m[5], 0.0], [m[6], m[7], m[8], 0.0], [m[9], m[10], m[11], 1.0]]
    a, b = full(first), full(then)
    c = [[sum(a[i][k] * b[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
    return [c[0][0], c[0][1], c[0][2], c[1][0], c[1][1], c[1][2], c[2][0], c[2][1], c[2][2], c[3][0], c[3][1], c[3][2]]


def _norm_path(path):
    return "/" + path.lstrip("/")


def load_3mf(path):
    """Return (unit, [Body]) with every build item and component transform applied."""
    try:
        with zipfile.ZipFile(path) as z:
            docs = {_norm_path(n): ET.fromstring(z.read(n)) for n in z.namelist() if n.lower().endswith(".model")}
    except zipfile.BadZipFile:
        raise ValueError(f"{path}: not a 3MF (not a zip file)")
    except NotImplementedError:
        raise ValueError(f"{path}: not a 3MF (unsupported compression; a Fusion .f3d archive?)")
    if not docs:
        raise ValueError(f"{path}: no 3D model inside; export the body as 3MF")
    root = "/3D/3dmodel.model" if "/3D/3dmodel.model" in docs else sorted(docs)[0]
    unit = docs[root].get("unit", "millimeter")
    objects = {(dn, o.get("id")): o for dn, d in docs.items() for o in d.iter(CORE + "object")}
    bodies = []

    def walk(dn, oid, m, name, depth):
        if depth > 20:
            raise ValueError(f"{path}: components nested too deep")
        obj = objects[(dn, oid)]
        name = obj.get("name") or name or f"object {oid}"
        mesh = obj.find(CORE + "mesh")
        if mesh is not None:
            weld, verts, remap = {}, [], []
            for v in mesh.find(CORE + "vertices").iter(CORE + "vertex"):
                p = _apply(m, (float(v.get("x")), float(v.get("y")), float(v.get("z"))))
                key = (round(p[0], 6), round(p[1], 6), round(p[2], 6))
                if key not in weld:
                    weld[key] = len(verts)
                    verts.append(p)
                remap.append(weld[key])
            tris = []
            for t in mesh.find(CORE + "triangles").iter(CORE + "triangle"):
                a, b, c = (remap[int(t.get(k))] for k in ("v1", "v2", "v3"))
                if a != b and b != c and a != c:
                    tris.append((a, b, c))
            bodies.append(Body(name, verts, tris))
        comps = obj.find(CORE + "components")
        if comps is not None:
            for comp in comps.iter(CORE + "component"):
                cpath = _norm_path(comp.get(PROD + "path")) if comp.get(PROD + "path") else dn
                walk(cpath, comp.get("objectid"), _compose(_transform(comp.get("transform")), m), name, depth + 1)

    build = docs[root].find(CORE + "build")
    if build is None:
        raise ValueError(f"{path}: the 3MF has no build items")
    for item in build.iter(CORE + "item"):
        ipath = _norm_path(item.get(PROD + "path")) if item.get(PROD + "path") else root
        walk(ipath, item.get("objectid"), _transform(item.get("transform")), None, 0)
    if not bodies:
        raise ValueError(f"{path}: no mesh found")
    return unit, bodies


# --------------------------------------------------------------------------- solid checks

def mesh_stats(body):
    """Volume (mm^3, signed: negative means the faces point inward), closed-solid check and connected pieces."""
    vs = body.verts
    vol = 0.0
    directed = {}
    for a, b, c in body.tris:
        (x1, y1, z1), (x2, y2, z2), (x3, y3, z3) = vs[a], vs[b], vs[c]
        vol += (x1 * (y2 * z3 - z2 * y3) - y1 * (x2 * z3 - z2 * x3) + z1 * (x2 * y3 - y2 * x3)) / 6.0
        for e in ((a, b), (b, c), (c, a)):
            directed[e] = directed.get(e, 0) + 1
    repeated = sum(1 for n in directed.values() if n > 1)
    unpaired = sum(1 for (a, b) in directed if (b, a) not in directed)
    parent = list(range(len(vs)))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    for a, b, c in body.tris:
        ra = find(a)
        parent[find(b)] = ra
        parent[find(c)] = ra
    pieces = len({find(t[0]) for t in body.tris})
    return {"volume": vol, "closed": repeated == 0 and unpaired == 0, "repeated": repeated,
            "unpaired": unpaired, "pieces": pieces}


def bounds(bodies):
    pts = [p for b in bodies for p in b.verts]
    return [(min(p[i] for p in pts), max(p[i] for p in pts)) for i in range(3)]


# --------------------------------------------------------------------------- sections

def _simplify(pts, tol=1e-6):
    """Drop repeated points and points on a straight line between their neighbours."""
    out = []
    for p in pts:
        if not out or math.dist(out[-1], p) > 1e-7:
            out.append(p)
    if len(out) > 1 and math.dist(out[0], out[-1]) <= 1e-7:
        out.pop()
    while len(out) > 3:
        n = len(out)
        keep = []
        for i in range(n):
            a, b, c = out[i - 1], out[i], out[(i + 1) % n]
            ab = (b[0] - a[0], b[1] - a[1])
            bc = (c[0] - b[0], c[1] - b[1])
            la, lb = math.hypot(*ab), math.hypot(*bc)
            cross = ab[0] * bc[1] - ab[1] * bc[0]
            if la * lb == 0 or (abs(cross) <= tol * la * lb and ab[0] * bc[0] + ab[1] * bc[1] > 0):
                continue
            keep.append(b)
        if len(keep) == n or len(keep) < 3:
            break
        out = keep
    return out


class Loop:
    """A closed section loop in the cut plane, with its nesting depth (even: outline of material; odd: a void)."""

    def __init__(self, pts):
        self.pts = _simplify(pts)
        p = self.pts
        n = len(p)
        a = cx = cy = per = 0.0
        for i in range(n):
            x1, y1 = p[i]
            x2, y2 = p[(i + 1) % n]
            cr = x1 * y2 - x2 * y1
            a += cr
            cx += (x1 + x2) * cr
            cy += (y1 + y2) * cr
            per += math.hypot(x2 - x1, y2 - y1)
        a /= 2.0
        self.area = abs(a)
        self.centre = (cx / (6 * a), cy / (6 * a)) if a else (p[0] if p else (0.0, 0.0))
        xs = [q[0] for q in p] or [0.0]
        ys = [q[1] for q in p] or [0.0]
        self.box = (min(xs), min(ys), max(xs), max(ys))
        self.width = self.box[2] - self.box[0]
        self.height = self.box[3] - self.box[1]
        self.perimeter = per
        self.depth = 0

    @property
    def eq_diameter(self):
        return 2.0 * math.sqrt(self.area / math.pi)

    @property
    def kind(self):
        if self.depth % 2 == 0:
            return "outline"
        return "hole" if self.eq_diameter <= HOLE_MAX_D else "opening"

    def contains(self, q):
        x, y = q
        b = self.box
        if not (b[0] <= x <= b[2] and b[1] <= y <= b[3]):
            return False
        inside = False
        p = self.pts
        j = len(p) - 1
        for i in range(len(p)):
            xi, yi = p[i]
            xj, yj = p[j]
            if (yi > y) != (yj > y) and x < (xj - xi) * (y - yi) / (yj - yi) + xi:
                inside = not inside
            j = i
        return inside

    def describe(self):
        p = self.pts
        n = len(p)
        c = self.centre
        radii = [math.dist(c, q) for q in p]
        rmean = sum(radii) / n if n else 0.0
        if n == 4:
            right = True
            for i in range(4):
                a, b, d = p[i - 1], p[i], p[(i + 1) % 4]
                u = (b[0] - a[0], b[1] - a[1])
                v = (d[0] - b[0], d[1] - b[1])
                if abs(u[0] * v[0] + u[1] * v[1]) > 1e-4 * math.hypot(*u) * math.hypot(*v):
                    right = False
            if right:
                s1 = math.dist(p[0], p[1])
                s2 = math.dist(p[1], p[2])
                if abs(s1 * s2 - self.width * self.height) <= 1e-6 * max(1.0, self.area):
                    return f"rect {self.width:.3f} x {self.height:.3f}"
                return f"rect {s1:.3f} x {s2:.3f} (turned)"
        if n == 6 and max(radii) - min(radii) <= 0.01 * rmean:
            apothem = sum(math.dist(c, ((p[i][0] + p[i - 1][0]) / 2, (p[i][1] + p[i - 1][1]) / 2))
                          for i in range(6)) / 6
            return f"hex {2 * apothem:.3f} across flats"
        if n >= 12 and max(radii) - min(radii) <= 0.005 * rmean:
            return f"round D{2 * rmean:.3f}"
        return f"{n}-sided {self.width:.3f} x {self.height:.3f}"


def section(bodies, axis, c):
    """Loops cut by the plane AXIS = c, with nesting depths set. Returns (loops, open_chain_count).

    A vertex lying exactly on the plane counts as below it, so a cut at a face plane is taken just above that face.
    """
    ai = AXES.index(axis)
    u, v = [i for i in range(3) if i != ai]
    loops = []
    open_chains = 0
    for body in bodies:
        vs = body.verts
        nbr, coord = {}, {}
        for tri in body.triangles_crossing(ai, c):
            keys = []
            for p, q in ((tri[0], tri[1]), (tri[1], tri[2]), (tri[2], tri[0])):
                dp, dq = vs[p][ai] - c, vs[q][ai] - c
                if (dp > 0) != (dq > 0):
                    key = (p, q) if p < q else (q, p)
                    if key not in coord:
                        t = dp / (dp - dq)
                        P, Q = vs[p], vs[q]
                        coord[key] = (P[u] + t * (Q[u] - P[u]), P[v] + t * (Q[v] - P[v]))
                    keys.append(key)
            if len(keys) == 2:
                nbr.setdefault(keys[0], []).append(keys[1])
                nbr.setdefault(keys[1], []).append(keys[0])
        seen = set()
        for start in nbr:
            if start in seen:
                continue
            chain = [start]
            seen.add(start)
            prev, cur = None, start
            while True:
                nxt = [k for k in nbr[cur] if k != prev and k not in seen]
                if not nxt:
                    break
                prev, cur = cur, nxt[0]
                seen.add(cur)
                chain.append(cur)
            if len(chain) > 2 and start in nbr[cur]:
                loop = Loop([coord[k] for k in chain])
                if len(loop.pts) >= 3 and loop.area > 1e-9:
                    loops.append(loop)
            else:
                open_chains += 1
    loops.sort(key=lambda L: -L.area)
    for i, L in enumerate(loops):
        q = L.pts[0]
        L.depth = sum(1 for M in loops[:i] if M.area > L.area and M.contains(q))
    return loops, open_chains


def ray_hits(loops, centre, angle_deg):
    """Distances from centre at which a ray at angle_deg (from the first cut axis) crosses any loop."""
    th = math.radians(angle_deg)
    dx, dy = math.cos(th), math.sin(th)
    cx, cy = centre
    hits = []
    for L in loops:
        p = L.pts
        for i in range(len(p)):
            (x1, y1), (x2, y2) = p[i], p[(i + 1) % len(p)]
            ex, ey = x2 - x1, y2 - y1
            den = dx * ey - dy * ex
            if abs(den) < 1e-15:
                continue
            t = ((x1 - cx) * ey - (y1 - cy) * ex) / den
            s = ((x1 - cx) * dy - (y1 - cy) * dx) / den
            if t > 1e-9 and -1e-9 <= s <= 1 + 1e-9:
                hits.append(t)
    out = []
    for t in sorted(hits):          # a ray through a corner meets both edges there: count it once
        if not out or t - out[-1] > 1e-6:
            out.append(t)
    return out


# --------------------------------------------------------------------------- hole patterns

def describe_pattern(points, centre=(0.0, 0.0)):
    """A short description of hole centres: a bolt circle, a pattern symmetric about both axes, or a list."""
    if not points:
        return ""
    cx, cy = centre
    if len(points) == 1:
        return f"at ({points[0][0]:.3f}, {points[0][1]:.3f})"
    radii = [math.hypot(x - cx, y - cy) for x, y in points]
    rmean = sum(radii) / len(radii)
    if rmean > 0.01 and max(radii) - min(radii) <= 0.01:
        angles = sorted(round(math.degrees(math.atan2(y - cy, x - cx)) % 360.0, 2) % 360.0 for x, y in points)
        return f"on a D{2 * rmean:.3f} circle at " + ", ".join(f"{a:g}" for a in angles) + " deg"
    grid = {(round(x - cx, 2), round(y - cy, 2)) for x, y in points}
    if len(grid) == len(points) and all((-a, b) in grid and (a, -b) in grid and (-a, -b) in grid for a, b in grid):
        def fmt(a):
            return "0" if a == 0 else f"+-{abs(a):g}"
        pairs = sorted({(abs(a), abs(b)) for a, b in grid}, key=lambda t: (max(t), min(t), t))
        about = "" if (cx, cy) == (0.0, 0.0) else f" about ({cx:.3f}, {cy:.3f})"
        return "at " + ", ".join(f"({fmt(a)}, {fmt(b)})" for a, b in pairs) + about
    return "at " + ", ".join(f"({x:.3f}, {y:.3f})" for x, y in sorted(points))


def nearest_spacing(points):
    """Median distance from each point to its nearest neighbour (grid search)."""
    if len(points) < 2:
        return None
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    cell = max(max(xs) - min(xs), max(ys) - min(ys)) / max(1.0, math.sqrt(len(points))) or 1.0
    grid = {}
    for i, (x, y) in enumerate(points):
        grid.setdefault((int(x // cell), int(y // cell)), []).append(i)
    best = []
    for i, (x, y) in enumerate(points):
        gx, gy = int(x // cell), int(y // cell)
        d = math.inf
        ring = 1
        while d == math.inf or ring <= 2:
            for ix in range(gx - ring, gx + ring + 1):
                for iy in range(gy - ring, gy + ring + 1):
                    for j in grid.get((ix, iy), ()):
                        if j != i:
                            d = min(d, math.dist(points[i], points[j]))
            ring += 1
            if ring > 50:
                break
        best.append(d)
    best.sort()
    return best[len(best) // 2]


def match_holes(a_points, b_points, tol=0.5):
    """Pair each hole in A with the nearest unused hole in B within tol. Returns (pairs, unmatched_a, unmatched_b)."""
    cand = sorted((math.dist(p, q), i, j) for i, p in enumerate(a_points) for j, q in enumerate(b_points)
                  if math.dist(p, q) <= tol)
    used_a, used_b, pairs = set(), set(), []
    for d, i, j in cand:
        if i not in used_a and j not in used_b:
            used_a.add(i)
            used_b.add(j)
            pairs.append((i, j, d))
    return (pairs, [i for i in range(len(a_points)) if i not in used_a],
            [j for j in range(len(b_points)) if j not in used_b])


def _hole_summary(holes):
    groups = {}
    for h in holes:
        groups.setdefault(h.describe(), []).append(h)
    ordered = sorted(groups.items(), key=lambda kv: -len(kv[1]))
    shown = [f"{len(hs)} x {d}" for d, hs in ordered[:4]]
    rest = [h for _, hs in ordered[4:] for h in hs]
    if rest:
        ds = [h.eq_diameter for h in rest]
        shown.append(f"{len(rest)} others (equivalent D{min(ds):.2f} to D{max(ds):.2f}, cut or odd shapes)")
    text = " + ".join(shown)
    pts = [h.centre for h in holes]
    if len(holes) <= PATTERN_MAX:
        text += " " + describe_pattern(pts)
    else:
        sp = nearest_spacing(pts)
        text += (f"; the holes reach {min(h.box[0] for h in holes):.3f} to {max(h.box[2] for h in holes):.3f} and "
                 f"{min(h.box[1] for h in holes):.3f} to {max(h.box[3] for h in holes):.3f}; "
                 f"nearest-neighbour spacing {sp:.3f}")
    return text


# --------------------------------------------------------------------------- layers

class Slice:
    """One section: a signature (loop counts and the hole set) plus the sizes of its outlines and openings."""

    def __init__(self, loops, open_chains):
        self.loops = loops
        self.open_chains = open_chains
        self.outlines = [L for L in loops if L.kind == "outline"]
        self.openings = [L for L in loops if L.kind == "opening"]
        self.holes = [L for L in loops if L.kind == "hole"]
        hole_sig = tuple(sorted((h.describe(), round(h.centre[0], 2), round(h.centre[1], 2)) for h in self.holes))
        big = self.outlines + self.openings
        corners = tuple(len(L.pts) if len(L.pts) < FLAT_MAX else 0 for L in big)
        self.signature = (len(self.outlines), len(self.openings), corners, hole_sig, open_chains)
        self.sizes = tuple(s for L in big for s in (L.width, L.height))    # bounding boxes, for printing
        self.dsizes = tuple(L.eq_diameter for L in big)                     # area-equivalent, for decisions


def _close(a, b, tol):
    return len(a) == len(b) and all(abs(x - y) <= tol for x, y in zip(a, b))


def _direction(a, b):
    if len(a) != len(b):
        return None
    return tuple(0 if abs(y - x) <= NOISE else (1 if y > x else -1) for x, y in zip(a, b))


def _compatible(d1, d2):
    """Directions agree in every component; 0 (no real change) agrees with anything."""
    return d1 is not None and d2 is not None and len(d1) == len(d2) and         all(x == 0 or y == 0 or x == y for x, y in zip(d1, d2))


class Interval:
    """The part between two neighbouring vertex planes; sampled just inside each end."""

    def __init__(self, lo, hi, e, a, b):
        self.lo, self.hi, self.e, self.a, self.b = lo, hi, e, a, b
        self.direction = _direction(a.dsizes, b.dsizes) if a.signature == b.signature else None
        self.changing = self.direction is None or any(self.direction)
        self.sliver = hi - lo < SLIVER

    def extend(self, attr, at_end):
        """Sizes change linearly between vertex planes, so extend the samples to the interval's exact ends."""
        x, y = getattr(self.a, attr), getattr(self.b, attr)
        if len(x) != len(y):
            return y if at_end else x
        k = self.e / max(self.hi - self.lo - 2 * self.e, 1e-12)
        if at_end:
            return tuple(q + (q - p) * k for p, q in zip(x, y))
        return tuple(p - (q - p) * k for p, q in zip(x, y))


class Run:
    """A stretch of constant or steadily changing cross-section."""

    def __init__(self, iv):
        self.ivs = [iv]
        self.changing = iv.changing
        self.direction = iv.direction
        self.mid = None
        self.deviations = []

    lo = property(lambda self: self.ivs[0].lo)
    hi = property(lambda self: self.ivs[-1].hi)
    signature = property(lambda self: self.ivs[0].a.signature)
    all_sliver = property(lambda self: all(iv.sliver for iv in self.ivs))

    @property
    def deviation(self):
        return max(self.deviations, default=0.0)

    @property
    def straight(self):
        return self.deviation <= STRAIGHT_TOL

    def accepts(self, iv):
        if not (iv.a.signature == iv.b.signature == self.signature):
            return False
        if iv.sliver or self.all_sliver:
            return True
        if not self.changing and not iv.changing:
            return _close(self.ivs[0].a.dsizes, iv.b.dsizes, NOISE) and                 _close(self.ivs[0].a.sizes, iv.b.sizes, BOX_TOL)
        if self.changing and iv.changing:
            return _compatible(self.direction, iv.direction)
        return False

    def add(self, iv):
        if self.all_sliver and not iv.sliver:
            self.changing, self.direction = iv.changing, iv.direction
        elif self.changing and iv.changing and not iv.sliver:
            self.direction = tuple(x or y for x, y in zip(self.direction, iv.direction))
        self.ivs.append(iv)

    def absorb(self, other):
        if other.changing:
            self.direction = tuple(x or y for x, y in zip(self.direction, other.direction))
        self.ivs.extend(other.ivs)


def _join_curves(runs):
    """Join changing stretches separated only by short, nearly flat slices, when they change the same way."""
    out = []
    i = 0
    while i < len(runs):
        if out and out[-1].changing:
            j = i
            while j < len(runs) and not runs[j].changing and runs[j].hi - runs[j].lo < SHORT                     and runs[j].signature == out[-1].signature:
                j += 1
            if j < len(runs) and runs[j].changing and runs[j].signature == out[-1].signature                     and _compatible(out[-1].direction, runs[j].direction):
                for k in range(i, j + 1):
                    out[-1].absorb(runs[k])
                i = j + 1
                continue
        out.append(runs[i])
        i += 1
    return out


def layers(bodies, axis):
    """Split the part along AXIS into stretches of constant or steadily changing cross-section."""
    ai = AXES.index(axis)
    levels = sorted({round(p[ai], 4) for b in bodies for p in b.verts})
    cache = {}

    def at(c):
        if c not in cache:
            cache[c] = Slice(*section(bodies, axis, c))
        return cache[c]

    runs = []
    for lo, hi in zip(levels, levels[1:]):
        e = min(SIZE_TOL, (hi - lo) / 10)
        iv = Interval(lo, hi, e, at(lo + e), at(hi - e))
        if runs and runs[-1].accepts(iv):
            runs[-1].add(iv)
        else:
            runs.append(Run(iv))
    runs = _join_curves(runs)

    for r in runs:
        r.mid = at((r.lo + r.hi) / 2 + 1e-7)
        if not r.changing:
            continue
        body = [iv for iv in r.ivs if not iv.sliver] or r.ivs
        r.start_sizes = body[0].extend("sizes", False)
        r.end_sizes = body[-1].extend("sizes", True)
        d0, d1 = body[0].extend("dsizes", False), body[-1].extend("dsizes", True)
        r.d0, r.d1 = d0, d1
        lo, hi = body[0].lo, body[-1].hi
        r.deviations = [0.0] * len(d0)
        for f in (0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875):
            s = at(lo + f * (hi - lo) + 1e-7).dsizes
            if len(s) == len(d0) == len(d1):
                r.deviations = [max(m, abs(p - (x + f * (y - x))))
                                for m, p, x, y in zip(r.deviations, s, d0, d1)]
    return levels, runs


# --------------------------------------------------------------------------- printing

def _fmt_sizes(sizes, n_out):
    parts = []
    for i in range(0, len(sizes), 2):
        label = "outline" if i // 2 < n_out else "opening"
        parts.append(f"{label} {sizes[i]:.3f} x {sizes[i + 1]:.3f}")
    return ", ".join(parts)


def print_info(path):
    unit, bodies = load_3mf(path)
    print(f"{path}  (unit: {unit})")
    total = 0.0
    for b in bodies:
        s = mesh_stats(b)
        total += abs(s["volume"])
        solid = "closed solid" if s["closed"] else \
            f"NOT CLOSED ({s['unpaired']} unpaired, {s['repeated']} repeated edges)"
        inward = "; faces point inward" if s["volume"] < 0 else ""
        print(f"  body {b.name!r}: {solid}, {s['pieces']} piece(s), {len(b.tris)} triangles, "
              f"volume {abs(s['volume']) / 1000:.3f} cm3{inward}")
    print(f"  bodies: {len(bodies)}")
    bx = bounds(bodies)
    size = [hi - lo for lo, hi in bx]
    print(f"  size {size[0]:.3f} x {size[1]:.3f} x {size[2]:.3f} (x y z); "
          + ", ".join(f"{AXES[i]} {bx[i][0]:.3f} to {bx[i][1]:.3f}" for i in range(3)))
    fits = all(d <= BED_MM for d in size)
    print(f"  P1S bed ({BED_MM:g} mm cube, axis-aligned): {'fits' if fits else 'does not fit'}"
          + ("" if fits else f" (largest side {max(size):.3f})"))
    print(f"  printed solid in PLA: at most {total / 1000 * PLA_G_PER_CM3:.0f} g")


def print_layers(path, axis):
    _, bodies = load_3mf(path)
    levels, runs = layers(bodies, axis)
    print(f"{path}: along {axis} from {levels[0]:.3f} to {levels[-1]:.3f} ({levels[-1] - levels[0]:.3f}); "
          f"{len(levels)} planes where vertices lie, {len(runs)} stretch(es)")
    for r in runs:
        s = r.mid
        head = f"  {axis} {r.lo:9.3f} to {r.hi:9.3f} ({r.hi - r.lo:7.3f}): "
        shape = "; ".join([f"outline {L.describe()}" for L in s.outlines]
                          + [f"opening {L.describe()}" for L in s.openings]) or "empty"
        if not r.changing:
            print(head + shape)
        else:
            n_out = len(s.outlines)
            hows = []
            for k, dev in enumerate(r.deviations):
                label = "outline" if k < n_out else "opening"
                if abs(r.d1[k] - r.d0[k]) <= NOISE and dev <= STRAIGHT_TOL:
                    hows.append(f"{label} unchanged")
                else:
                    hows.append(f"{label} straight" if dev <= STRAIGHT_TOL
                                else f"{label} curved (up to {dev:.3f} off a straight line)")
            print(head + "CHANGING: " + ", ".join(hows))
            print(f"      start  {_fmt_sizes(r.start_sizes, n_out)}")
            print(f"      middle {shape}")
            print(f"      end    {_fmt_sizes(r.end_sizes, n_out)}")
        if s.holes:
            print(f"      holes {_hole_summary(s.holes)}")
        if s.open_chains:
            print(f"      WARNING: {s.open_chains} open chain(s) in the section (mesh not closed here)")


def print_cut(path, axis, positions, rays, centre, list_all):
    _, bodies = load_3mf(path)
    ai = AXES.index(axis)
    u, v = [AXES[i] for i in range(3) if i != ai]
    levels = {round(p[ai], 4) for b in bodies for p in b.verts}
    for c in positions:
        loops, open_chains = section(bodies, axis, c)
        note = "  (a face plane: section taken just above it)" if round(c, 4) in levels else ""
        print(f"{axis} = {c:g}: {len(loops)} loop(s), coordinates ({u}, {v}){note}")
        for L in loops:
            if L.kind != "hole":
                print(f"  {L.kind:8s} {L.describe()}, centre ({L.centre[0]:.3f}, {L.centre[1]:.3f}), "
                      f"spans {u} {L.box[0]:.3f} to {L.box[2]:.3f}, {v} {L.box[1]:.3f} to {L.box[3]:.3f}")
        holes = [L for L in loops if L.kind == "hole"]
        if holes:
            print(f"  holes    {_hole_summary(holes)}")
            if list_all:
                for h in sorted(holes, key=lambda h: (round(h.centre[0], 2), round(h.centre[1], 2))):
                    print(f"           {h.describe()} at ({h.centre[0]:.3f}, {h.centre[1]:.3f})")
        if open_chains:
            print(f"  WARNING: {open_chains} open chain(s) (mesh not closed here)")
        for ang in rays:
            hits = ray_hits(loops, centre, ang)
            print(f"  ray {ang:g} deg from ({centre[0]:g}, {centre[1]:g}): "
                  + (", ".join(f"{h:.3f}" for h in hits) or "no walls"))


def print_match(path_a, at_a, path_b, at_b, axis, rotate, mirror, tol):
    def holes_of(path, c):
        _, bodies = load_3mf(path)
        loops, _ = section(bodies, axis, c)
        return [L for L in loops if L.kind == "hole"]
    ha, hb = holes_of(path_a, at_a), holes_of(path_b, at_b)
    pa = [h.centre for h in ha]
    th = math.radians(rotate)
    pb = []
    for x, y in (h.centre for h in hb):
        if mirror == "x":
            x = -x
        elif mirror == "y":
            y = -y
        pb.append((x * math.cos(th) - y * math.sin(th), x * math.sin(th) + y * math.cos(th)))
    print(f"A: {path_a} at {axis} = {at_a:g}: {len(ha)} hole(s)" + (f", {_hole_summary(ha)}" if ha else ""))
    print(f"B: {path_b} at {axis} = {at_b:g}: {len(hb)} hole(s)" + (f", {_hole_summary(hb)}" if hb else "")
          + (f" (mirrored in {mirror})" if mirror else "") + (f" (turned {rotate:g} deg)" if rotate else ""))
    pairs, ua, ub = match_holes(pa, pb, tol)
    worst = max(pairs, key=lambda t: t[2]) if pairs else None
    print(f"matched {len(pairs)} of {len(ha)} (A) and {len(hb)} (B) within {tol:g}"
          + (f"; largest centre offset {worst[2]:.3f} at ({pa[worst[0]][0]:.3f}, {pa[worst[0]][1]:.3f})"
             if worst else ""))
    for label, idx, pts in (("A", ua, pa), ("B", ub, pb)):
        if idx:
            print(f"unmatched in {label}: " + ", ".join(f"({pts[i][0]:.3f}, {pts[i][1]:.3f})" for i in idx))
    return 0 if pairs and not ua and not ub else 1


def main(argv=None):
    ap = argparse.ArgumentParser(description="Measure a 3MF export (read-only).")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("info")
    p.add_argument("files", nargs="+")
    p = sub.add_parser("layers")
    p.add_argument("file")
    p.add_argument("--axis", default="z", choices=list(AXES))
    p = sub.add_parser("cut")
    p.add_argument("file")
    p.add_argument("at", nargs="+", type=float)
    p.add_argument("--axis", default="z", choices=list(AXES))
    p.add_argument("--rays", default="", help="comma-separated angles in degrees, e.g. 0,45")
    p.add_argument("--centre", default="0,0", help="ray origin X,Y in the cut plane (default 0,0)")
    p.add_argument("--list", action="store_true", help="print every hole")
    p = sub.add_parser("match")
    p.add_argument("file_a")
    p.add_argument("at_a", type=float)
    p.add_argument("file_b")
    p.add_argument("at_b", type=float)
    p.add_argument("--axis", default="z", choices=list(AXES))
    p.add_argument("--rotate", type=float, default=0.0)
    p.add_argument("--mirror", choices=["x", "y"])
    p.add_argument("--tol", type=float, default=0.5)
    args = ap.parse_args(argv)
    try:
        if args.cmd == "info":
            for i, f in enumerate(args.files):
                if i:
                    print()
                print_info(f)
            return 0
        if args.cmd == "layers":
            print_layers(args.file, args.axis)
            return 0
        if args.cmd == "cut":
            rays = [float(a) for a in args.rays.split(",") if a.strip()]
            centre = tuple(float(a) for a in args.centre.split(","))
            print_cut(args.file, args.axis, args.at, rays, centre, args.list)
            return 0
        return print_match(args.file_a, args.at_a, args.file_b, args.at_b, args.axis, args.rotate, args.mirror,
                           args.tol)
    except (OSError, ValueError, KeyError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
