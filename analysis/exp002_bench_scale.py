"""EXP-002: TAL221 load cell + SparkFun HX711 on the printed bench scale, 2026-11-26 (bench characterisation).

Finds the steady stretches ("plateaus") in the raw HX711 log, matches them to the known sequence of calibration
masses, and reports the sensitivity (counts per gram), straightness (residuals of a straight-line fit), hysteresis
(down minus up), return to zero, creep under 50 g, zero drift and noise.

Inputs
  data/raw/2026-11-26_EXP-002_tal221-bench-scale/run02.csv
      written by scripts/serial_capture.ps1 from firmware/hx711_raw_counts with AVERAGE_OVER = 1:
      pc_time (PC local time, ISO 8601), time_ms (ms since the Mega reset), counts (raw HX711 ADC counts,
      channel A, gain 128). Lines before the header are serial-buffer leftovers from before the reset; '#' lines
      are messages. run01.csv in the same folder is an empty failed start and is not read.
  Masses: the measured means from EXP-001 (docs/data_catalog.md#exp-001-calibration-mass-weighing), in g, each
      about +/-0.01 g relative to the school balance (whose own accuracy is unknown).
  Load sequence: as placed by the owner and logged live in the session (docs/sessions/, 2026-11-26).

Outputs
  data/processed/2026-11-26_EXP-002_plateaus.csv  one row per load state: index, load_g, pieces on the pan,
      start/end PC time, duration_s, n_used, level_counts (mean of the last USE_LAST_S seconds), sd_counts,
      sem_counts, full_mean_counts, fit residual in counts and in g
  results/2026-11-26_EXP-002_bench-scale-summary.txt  the numbers below, with units

Units: counts are raw HX711 ADC counts; masses in g (grams of mass loaded on the pan at local gravity); forces in N
use g = 9.81 m/s^2 (assumed; within about 0.2 % of local gravity at latitudes 25-60 deg, Barlow1999 notes).

Usage (repository root):  python analysis/exp002_bench_scale.py
Python 3 standard library only.
"""
import csv
import os
import statistics as st
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, "data", "raw", "2026-11-26_EXP-002_tal221-bench-scale", "run02.csv")
OUT_PLATEAUS = os.path.join(ROOT, "data", "processed", "2026-11-26_EXP-002_plateaus.csv")
OUT_SUMMARY = os.path.join(ROOT, "results", "2026-11-26_EXP-002_bench-scale-summary.txt")

# EXP-001 measured masses (g), docs/data_catalog.md#exp-001-calibration-mass-weighing
MASS = {
    "50g": 50.097, "20g#1": 19.763, "20g#2": 19.787,
    "10g#1": 9.940, "10g#2": 10.043, "10g#3": 9.967, "10g#4": 9.940,
    "5g#1": 5.057, "2g#1": 1.983, "2g#2": 1.950, "2g#3": 1.973,
}

# The load states in the order they happened (pieces on the pan), as logged in the session.
SEQUENCE = [
    [],                                                        # 0  empty: warm-up and zero drift
    ["2g#1"], ["2g#1", "2g#2"], ["2g#1", "2g#2", "2g#3"],       # 1-3 low range up
    ["2g#1", "2g#2", "2g#3", "5g#1"],                          # 4  (5 g stacked on the 2 g pieces)
    ["2g#1", "2g#2", "2g#3"], ["2g#1", "2g#2"], ["2g#1"],       # 5-7 low range down
    [],                                                        # 8  empty
    ["10g#1"], ["10g#1", "10g#2"], ["10g#1", "10g#2", "10g#3"],  # 9-11 full range up
    ["10g#1", "10g#2", "10g#3", "20g#1"],
    ["10g#1", "10g#2", "10g#3", "20g#1", "20g#2"],
    ["10g#1", "10g#2", "10g#3", "20g#1", "20g#2", "10g#4"],    # 14 top, 79.44 g
    ["10g#1", "10g#2", "10g#3", "20g#1", "20g#2"],              # 15-19 full range down
    ["10g#1", "10g#2", "10g#3", "20g#1"],
    ["10g#1", "10g#2", "10g#3"], ["10g#1", "10g#2"], ["10g#1"],
    [],                                                        # 20 empty
    ["50g"],                                                   # 21 creep, about 5 min
    [],                                                        # 22 empty, recovery
]

JUMP = 1500          # counts between consecutive readings that mark a disturbance (about 0.11 g; noise sd ~40-100)
PAD = 10             # readings (about 1 s) excluded either side of a disturbance
MIN_LEN = 50         # readings (about 4.8 s): shortest stretch counted as a plateau
MERGE = 3000         # counts: neighbouring plateaus closer than this are one load state split by a bump
USE_LAST_S = 20.0    # s: each state's level is the mean of its last 20 s (all of it if shorter)
G = 9.81             # m/s^2, assumed


def read_raw(path):
    rows, started = [], False
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if line.startswith("pc_time,"):
                started = True
                continue
            if not started:
                continue
            p = line.split(",")
            if len(p) != 3 or p[1].startswith("#"):
                continue
            rows.append((p[0], int(p[1]) / 1000.0, int(p[2])))
    return [r for r in rows if r[1] >= 1.0]   # the sketch: ignore the first second (settling)


def find_plateaus(rows):
    n = len(rows)
    bad = [False] * n
    for i in range(1, n):
        if abs(rows[i][2] - rows[i - 1][2]) > JUMP:
            for j in range(max(0, i - PAD), min(n, i + PAD + 1)):
                bad[j] = True
    runs, i = [], 0
    while i < n:
        if bad[i]:
            i += 1
            continue
        j = i
        while j < n and not bad[j]:
            j += 1
        if j - i >= MIN_LEN:
            runs.append(rows[i:j])
        i = j
    merged = []
    for r in runs:
        if merged and abs(st.mean(c for _, _, c in r) - st.mean(c for _, _, c in merged[-1][-1])) < MERGE:
            merged[-1].append(r)
        else:
            merged.append([r])
    return merged


def level(segments):
    """Mean of the last USE_LAST_S seconds of a state's final segment (all of it if shorter)."""
    last = segments[-1]
    t_end = last[-1][1]
    use = [c for _, t, c in last if t >= t_end - USE_LAST_S]
    return st.mean(use), st.pstdev(use), len(use)


def linfit(x, y):
    mx, my = st.mean(x), st.mean(y)
    sxx = sum((a - mx) ** 2 for a in x)
    b = sum((a - mx) * (c - my) for a, c in zip(x, y)) / sxx
    a = my - b * mx
    res = [c - (a + b * xi) for xi, c in zip(x, y)]
    s = (sum(r * r for r in res) / (len(x) - 2)) ** 0.5
    return a, b, s / sxx ** 0.5, res


def main():
    rows = read_raw(RAW)
    states = find_plateaus(rows)
    if len(states) != len(SEQUENCE):
        for k, s in enumerate(states):
            print(k, s[0][0][0], s[-1][-1][0], round(st.mean(c for seg in s for _, _, c in seg)))
        sys.exit(f"found {len(states)} load states, expected {len(SEQUENCE)}: check JUMP/PAD/MIN_LEN/MERGE")

    loads = [round(sum(MASS[p] for p in pieces), 3) for pieces in SEQUENCE]
    lev = [level(s) for s in states]
    y = [L[0] for L in lev]

    # Sanity check against a rough sensitivity before fitting: every state must be within 0.5 g of expectation.
    rough = (y[14] - y[8]) / (loads[14] - loads[8])
    for k, (m, v) in enumerate(zip(loads, y)):
        if abs(v - (y[0] + rough * m)) > 0.5 * rough:
            sys.exit(f"state {k} ({m} g) reads {v:.0f}, not near the expected {y[0] + rough * m:.0f}")

    a, b, se_b, res = linfit(loads, y)
    lo = list(range(0, 9))
    a_lo, b_lo, se_lo, res_lo = linfit([loads[k] for k in lo], [y[k] for k in lo])
    fu = list(range(8, 21))
    a_fu, b_fu, se_fu, res_fu = linfit([loads[k] for k in fu], [y[k] for k in fu])

    os.makedirs(os.path.dirname(OUT_PLATEAUS), exist_ok=True)
    with open(OUT_PLATEAUS, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["state", "load_g", "pieces", "start_pc_time", "end_pc_time", "duration_s", "n_used",
                    "level_counts", "sd_counts", "sem_counts", "full_mean_counts", "residual_counts", "residual_g"])
        for k, s in enumerate(states):
            allc = [c for seg in s for _, _, c in seg]
            m, sd, nu = lev[k]
            w.writerow([k, f"{loads[k]:.3f}", "+".join(SEQUENCE[k]) or "empty", s[0][0][0], s[-1][-1][0],
                        f"{s[-1][-1][1] - s[0][0][1]:.1f}", nu, f"{m:.1f}", f"{sd:.1f}", f"{sd / nu ** 0.5:.1f}",
                        f"{st.mean(allc):.1f}", f"{res[k]:.1f}", f"{res[k] / b:.4f}"])

    def g(counts, slope=b):
        return counts / slope

    out = []
    p = out.append
    p("EXP-002 bench scale: TAL221 100 g + SparkFun HX711 (gain 128, 10 SPS), printed scale, 2026-11-26")
    p(f"raw: {os.path.relpath(RAW, ROOT)}  ({len(rows)} readings after the first second)")
    p(f"script: analysis/exp002_bench_scale.py; level of each state = mean of its last {USE_LAST_S:.0f} s")
    p("")
    p(f"Straight-line fit, all {len(loads)} states (0 to 79.440 g, up and down):")
    p(f"  sensitivity  {b:.1f} counts/g  (standard error {se_b:.1f}, {100 * se_b / b:.3f} %)")
    p(f"               {b / (G / 1000):.4g} counts/N with g = {G} m/s^2")
    p(f"  intercept    {a:.0f} counts (empty pan, including the printed pan's own weight)")
    p(f"  residuals    max |r| {g(max(abs(r) for r in res)):.4f} g, rms {g((sum(r * r for r in res) / len(res)) ** 0.5):.4f} g"
      f"  ({100 * g(max(abs(r) for r in res)) / 100:.3f} % of the 100 g rating)")
    p(f"Low range only (states 0-8, 0 to 10.963 g): {b_lo:.1f} counts/g (se {se_lo:.1f}); "
      f"max |r| {g(max(abs(r) for r in res_lo), b_lo):.4f} g")
    p(f"Full range only (states 8-20, 0 to 79.440 g): {b_fu:.1f} counts/g (se {se_fu:.1f}); "
      f"max |r| {g(max(abs(r) for r in res_fu), b_fu):.4f} g")
    p(f"Low-range slope minus full-range slope: {100 * (b_lo - b_fu) / b_fu:+.3f} %")
    p("")
    p("Each state (g): load, level, residual from the all-states fit")
    for k in range(len(loads)):
        p(f"  {k:2d}  {loads[k]:7.3f} g  {y[k]:12.1f}  {g(res[k]):+.4f} g   {'+'.join(SEQUENCE[k]) or 'empty'}")
    p("")
    p("Hysteresis (down minus up, same load), g:")
    for up, dn in [(1, 7), (2, 6), (3, 5), (9, 19), (10, 18), (11, 17), (12, 16), (13, 15)]:
        p(f"  {loads[up]:7.3f} g: {g(y[dn] - y[up]):+.4f} g")
    p("Return to zero, g:")
    p(f"  after the low-range cycle (state 8 - state 0):   {g(y[8] - y[0]):+.4f} g")
    p(f"  after the full-range cycle (state 20 - state 8): {g(y[20] - y[8]):+.4f} g")
    p(f"  after 5 min at 50 g (state 22 - state 20):       {g(y[22] - y[20]):+.4f} g")
    p(f"  whole run (state 22 - state 0):                  {g(y[22] - y[0]):+.4f} g")

    # Creep under 50 g: 30 s means across state 21.
    c21 = [(t, c) for seg in states[21] for _, t, c in seg]
    t0 = c21[0][0]
    bins = {}
    for t, c in c21:
        bins.setdefault(int((t - t0) // 30), []).append(c)
    means = [st.mean(v) for k, v in sorted(bins.items()) if len(v) > 200]
    p("")
    p(f"Creep at 50.097 g ({c21[-1][0] - t0:.0f} s steady): 30 s means span {g(max(means) - min(means)):.4f} g; "
      f"last minus first {g(means[-1] - means[0]):+.4f} g")
    # Zero drift and noise on the first empty plateau.
    z = [(t, c) for seg in states[0] for _, t, c in seg]
    zb = {}
    for t, c in z:
        zb.setdefault(int((t - z[0][0]) // 10), []).append(c)
    zm = [st.mean(v) for k, v in sorted(zb.items()) if len(v) > 80]
    zc = [c for _, c in z]
    w15 = [st.pstdev(zc[i:i + 15]) for i in range(0, len(zc) - 15, 15)]
    p(f"Zero, first empty stretch ({z[-1][0] - z[0][0]:.0f} s): 10 s means span {g(max(zm) - min(zm)):.4f} g, "
      f"sd {g(st.pstdev(zm)):.4f} g; first-to-last {g(zm[-1] - zm[0]):+.4f} g")
    zm3 = zm[18:]
    p(f"  after the first 3 min: 10 s means sd {g(st.pstdev(zm3)):.4f} g, span {g(max(zm3) - min(zm3)):.4f} g")
    p(f"Noise: reading-to-reading sd within 1.4 s windows (median) {st.median(w15):.0f} counts = {g(st.median(w15)):.4f} g")
    p("")
    # Ratiometric sensitivity: counts = S * Vexc/AVDD * (m / 100 g) * 128 * 2^24, with Vexc = AVDD on this board.
    s_mvv = b * 100 / (128 * 2 ** 24) * 1000
    p(f"Implied cell output {s_mvv:.3f} mV/V at 100 g (assumes excitation = the HX711's AVDD reference; "
      "TAL221 datasheet 0.6 +/- 0.15 mV/V)")
    p(f"2026-11-23 penny step (about 33,300 counts) at this sensitivity: {33300 / b:.2f} g")

    os.makedirs(os.path.dirname(OUT_SUMMARY), exist_ok=True)
    with open(OUT_SUMMARY, "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()
