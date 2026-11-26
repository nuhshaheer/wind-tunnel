"""Points files for Fusion 360: the diffuser's two loft rails and the sting shield's cross-section.

Inputs (see cad/sizing/diffuser.md and cad/sizing/balance.md; all Proposed):
    Diffuser (D-026): round inlet, inside diameter 152 mm (6 in fan outlet; check against the S6's collar on arrival),
    to a 250 mm square exit, 175 mm long. The half-width grows along a smooth S-curve (zero slope at both ends):
        h(x) = h0 + (h1 - h0) * (3u^2 - 2u^3),  u = x / 175,
    across the flats (h0 = 76 -> h1 = 125) and along the diagonal (h0 = 76 -> h1 = 125*sqrt(2) = 176.78).
    Sting shield: a symmetric NACA 4-digit section, chord 22.5 mm, thickness 7.5 mm (t/c = 1/3), bore centred at
    30 % chord (6.75 mm behind the nose), where the half-thickness is 3.75 mm.

Outputs (written next to this file; units in the names; Fusion's ImportSplineCSV sample reads centimetres):
    diffuser_rail_flats_cm.csv     x, y, z in cm, no header: the top-centre rail (y = half-width, z = 0)
    diffuser_rail_diagonal_cm.csv  x, y, z in cm, no header: the corner rail (y = z = diagonal half-width / sqrt 2)
    shield_section_cm.csv          x, y, z in cm, no header: the closed shield outline in the floor plane
                                   (x along the flow from the nose, y across), trailing edge cut blunt at 0.8 mm
    profiles_mm.csv                the same diffuser numbers in mm with a header, for reading

Run from the repository root:  python cad/sizing/profiles.py
Standard library only.
"""

import csv
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))

L_DIFF = 175.0
H0 = 76.0
H1_FLAT = 125.0
H1_DIAG = 125.0 * math.sqrt(2)

CHORD = 22.5
T_C = 7.5 / 22.5
TE_MIN = 0.8          # mm, thinnest trailing edge that prints with a 0.4 mm nozzle


def smooth(u):
    return u * u * (3 - 2 * u)


def naca_half(xc):
    """Half-thickness (mm) at x/c = xc for the shield's NACA 4-digit section."""
    return 5 * T_C * CHORD * (0.2969 * math.sqrt(xc) - 0.1260 * xc - 0.3516 * xc ** 2
                              + 0.2843 * xc ** 3 - 0.1036 * xc ** 4)


def main():
    xs = [i * 175.0 / 35 for i in range(36)]           # every 5 mm
    flats, diag, rows = [], [], []
    for x in xs:
        u = x / L_DIFF
        hf = H0 + (H1_FLAT - H0) * smooth(u)
        hd = H0 + (H1_DIAG - H0) * smooth(u)
        flats.append((x, hf, 0.0))
        diag.append((x, hd / math.sqrt(2), hd / math.sqrt(2)))
        rows.append((x, hf, hd))
    for name, pts in (('diffuser_rail_flats_cm.csv', flats), ('diffuser_rail_diagonal_cm.csv', diag)):
        with open(os.path.join(HERE, name), 'w', newline='') as f:
            for x, y, z in pts:
                f.write(f'{x / 10:.5f},{y / 10:.5f},{z / 10:.5f}\n')
    with open(os.path.join(HERE, 'profiles_mm.csv'), 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['diffuser_x_mm', 'half_width_flats_mm', 'half_width_diagonal_mm'])
        for x, hf, hd in rows:
            w.writerow([f'{x:.1f}', f'{hf:.3f}', f'{hd:.3f}'])

    # shield outline: cosine-spaced points, upper surface nose -> cut, then lower surface back to the nose
    n = 40
    xcs = [0.5 * (1 - math.cos(math.pi * i / n)) for i in range(n + 1)]
    xcut = next(xc for xc in xcs[::-1] if 2 * naca_half(xc) >= TE_MIN)
    xcs = [xc for xc in xcs if xc <= xcut]
    upper = [(xc * CHORD, naca_half(xc)) for xc in xcs]
    lower = [(x, -y) for x, y in reversed(upper)][1:-1]
    outline = upper + lower
    with open(os.path.join(HERE, 'shield_section_cm.csv'), 'w', newline='') as f:
        for x, y in outline:
            f.write(f'{x / 10:.5f},{y / 10:.5f},0\n')

    print(f'diffuser: {len(xs)} rail points each; flats 76 -> 125, diagonal 76 -> {H1_DIAG:.2f} mm')
    print(f'shield: max half-thickness {naca_half(0.3):.3f} mm at 30 % chord; cut at x = {xcut * CHORD:.2f} mm '
          f'(blunt edge {2 * naca_half(xcut):.2f} mm); bore Ø5 at x = {0.3 * CHORD:.2f} mm leaves '
          f'{naca_half(0.3) - 2.5:.2f} mm of wall each side; {len(outline)} outline points')


if __name__ == '__main__':
    main()
