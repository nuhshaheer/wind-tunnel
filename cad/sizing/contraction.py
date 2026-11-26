"""Contraction inner wall: points for Fusion 360 and the numbers for the dimension sheet.

Inputs (all Proposed, see cad/sizing/contraction.md):
    inlet 250 mm square (settling chamber), exit 100 mm square (test section, D-008), so the contraction ratio is 6.25;
    length 250 mm (1.0 x inlet height, Bell1988 notes); 5th-order polynomial wall (Bell1988 notes, p. 14):
        y(x) = h_i - (h_i - h_e) * (6 s^5 - 15 s^4 + 10 s^3),  s = x / L,
    applied to the half-width of every wall, so each cross-section is a square of side 2 y(x).
    Wall thickness 3 mm and flange widths 10-14 mm are planning values only (the flange waits on the heat-set inserts).

Outputs (written next to this file; units in the names):
    contraction_wall_fusion_cm.csv  x,y,z in CENTIMETRES, no header: for Fusion 360's ImportSplineCSV sample script,
                                    which reads values as cm (Fusion's internal unit). x along the flow, y half-width.
    contraction_wall_mm.csv         the same curve in mm with a header and extra columns, for people.
    It also prints the station table, slopes, curvature, joint positions and a filament estimate (stdout), and the
    6 control points of a degree-5 control point spline that IS this curve (a Bezier curve, checked against the
    equation), for drawing it in Fusion without importing points.

Run from the repository root:  python cad/sizing/contraction.py
Standard library only.
"""

import csv
import math
import os

H_I = 125.0     # mm, inlet half-width (250 mm square)
H_E = 50.0      # mm, exit half-width (100 mm square)
L = 250.0       # mm, length
STEP = 5.0      # mm, point spacing for the spline (51 points)
T_WALL = 3.0    # mm, planning value
BED = 256.0     # mm, Bambu Lab P1S bed (manufacturer spec)
MARGIN = 3.0    # mm, kept clear on each side of the bed
PLA_DENSITY = 1.24  # g/cm^3, typical PLA (assumed)

HERE = os.path.dirname(os.path.abspath(__file__))


def y(x):
    s = x / L
    return H_I - (H_I - H_E) * (6 * s**5 - 15 * s**4 + 10 * s**3)


def dy(x):
    s = x / L
    return -(H_I - H_E) / L * 30 * s**2 * (1 - s) ** 2


def d2y(x):
    s = x / L
    return -(H_I - H_E) / L**2 * 60 * s * (1 - s) * (1 - 2 * s)


def bezier(cps, t):
    """Point at parameter t on the Bezier curve with control points cps (de Casteljau)."""
    pts = [tuple(p) for p in cps]
    while len(pts) > 1:
        pts = [((1 - t) * a[0] + t * b[0], (1 - t) * a[1] + t * b[1]) for a, b in zip(pts, pts[1:])]
    return pts[0]


def bisect(f, a, b, n=80):
    fa = f(a)
    for _ in range(n):
        m = 0.5 * (a + b)
        fm = f(m)
        if (fm > 0) == (fa > 0):
            a, fa = m, fm
        else:
            b = m
    return 0.5 * (a + b)


def main():
    xs = [i * STEP for i in range(int(round(L / STEP)) + 1)]

    with open(os.path.join(HERE, 'contraction_wall_fusion_cm.csv'), 'w', newline='') as f:
        for x in xs:
            f.write(f'{x / 10:.5f},{y(x) / 10:.5f},0\n')

    with open(os.path.join(HERE, 'contraction_wall_mm.csv'), 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['x_mm', 'half_width_mm', 'inside_side_mm', 'wall_angle_deg', 'velocity_ratio_U_over_Uexit'])
        for x in xs:
            w.writerow([f'{x:.1f}', f'{y(x):.4f}', f'{2 * y(x):.3f}',
                        f'{math.degrees(math.atan(-dy(x))):.2f}', f'{(H_E / y(x)) ** 2:.4f}'])

    # checks
    assert abs(y(0) - H_I) < 1e-9 and abs(y(L) - H_E) < 1e-9
    assert abs(dy(0)) < 1e-12 and abs(dy(L)) < 1e-12 and abs(d2y(0)) < 1e-12 and abs(d2y(L)) < 1e-12
    assert all(y(a) > y(a + 0.1) for a in [i * 0.1 for i in range(2500)])

    print('Station table (every 25 mm)')
    print(' x_mm  inside_mm  wall_angle_deg  U/U_exit  q/q_exit')
    for x in [i * 25.0 for i in range(11)]:
        vr = (H_E / y(x)) ** 2
        print(f'{x:5.0f}  {2 * y(x):9.2f}  {math.degrees(math.atan(-dy(x))):14.2f}  {vr:8.3f}  {vr * vr:8.4f}')

    s_curv = [(3 - math.sqrt(3)) / 6, (3 + math.sqrt(3)) / 6]   # where |y''| peaks
    print(f'\nSteepest wall: {math.degrees(math.atan(-dy(L / 2))):.2f} deg from the flow axis at x = {L / 2:.0f} mm '
          f'(inflection point, y = {y(L / 2):.2f} mm)')
    for s in s_curv:
        x = s * L
        r = (1 + dy(x) ** 2) ** 1.5 / abs(d2y(x))
        kind = 'concave (inlet side)' if s < 0.5 else 'convex (exit side)'
        print(f'Tightest bend, {kind}: radius {r:.0f} mm at x = {x:.1f} mm')

    print('\nWhere a one-piece downstream part starts (its upstream flange must fit the bed with the margin):')
    print(' flange_mm  x_joint_mm  inside_there_mm  part_length_mm  U/U_exit  q/q_exit')
    for wf in (10.0, 12.0, 14.0):
        y_max = (BED - 2 * MARGIN) / 2 - T_WALL - wf
        xj = bisect(lambda x: y(x) - y_max, 0.0, L / 2)
        vr = (H_E / y(xj)) ** 2
        print(f'{wf:10.0f}  {xj:10.1f}  {2 * y(xj):15.1f}  {L - xj:14.1f}  {vr:8.3f}  {vr * vr:8.4f}')

    # shell volume: four walls, each 2y wide, along the curve; corners counted once (outer offset ignored)
    n = 5000
    area = 0.0
    for i in range(n):
        x = (i + 0.5) * L / n
        area += 4 * 2 * y(x) * math.sqrt(1 + dy(x) ** 2) * (L / n)
    vol_cm3 = area * T_WALL / 1000
    print(f'\nInside surface {area / 100:.0f} cm^2; a solid {T_WALL:.1f} mm shell is about {vol_cm3:.0f} cm^3, '
          f'{vol_cm3 * PLA_DENSITY:.0f} g of PLA (estimate; flanges not included)')

    # The same curve as a degree-5 Bezier: 6s^5 - 15s^4 + 10s^3 is B3 + B4 + B5 in the Bernstein basis, so the control
    # points sit every L/5 along the flow, the first three at the inlet half-width and the last three at the exit's.
    cps = [(L * k / 5, H_I if k < 3 else H_E) for k in range(6)]
    err = max(abs(bezier(cps, i / 2000)[1] - y(bezier(cps, i / 2000)[0])) for i in range(2001))
    print()
    print('Control point spline, degree 5 (exact): ' + ', '.join(f'({cx:.1f}, {cy:.1f})' for cx, cy in cps)
          + f' mm; largest difference from the equation {err:.1e} mm over 2001 points')
    print(f'\nWrote {len(xs)} points: contraction_wall_fusion_cm.csv (cm) and contraction_wall_mm.csv (mm)')


if __name__ == '__main__':
    main()
