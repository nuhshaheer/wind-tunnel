# 2026-11-09: Fan advice and screen order

- **Session ID:** c748d2ac-e6e6-4efd-a310-72cc5959c78c (Claude Code, from the scratchpad path)
- **Agent:** Claude Code (Opus 5.5), VS Code extension, Windows 11
- **Commit:** not committed yet

Advice and documentation only. **The owner ordered the first part (the aluminium window screen).** Nothing was built or
tested.

## 1. Starting state and objective

- `/catchup`: `UP_TO_DATE` at `507f71c` (the owner had committed and pushed the drawing-package session); working tree
  clean; `check_docs.py` 0 failures, 0 warnings; 20 tests OK in 10.2 s.
- Discrepancies found at `/catchup`:
  - the docs still called `507f71c` "not committed yet" (PROJECT_STATUS header, §6, §12, §13 and the `/wrap` list;
    SESSION_LOG; TODO Done). Expected backfill, fixed at this wrap;
  - [buy_list.md](../buy_list.md) §2 told the reader to print the load-cell mount "in PETG", while the same section says
    PETG-CF replaces PETG. Fixed;
  - TODO P1 still gave 230–300 mm for full-decay settling-chamber spacing; the drawing finding is about 380–390 mm.
    A pointer was added.
- No objective was set in advance. The owner asked questions as they came: the PETG-CF line in the shopping list, the
  fan choice, how the estimates are made, other experiments, and which screen to buy.

## 2. Work completed

1. **Explained a shopping-list line** the owner found unclear ("PETG-CF is on hand and covers the loaded parts. Buy
   plain PETG only if it runs short"). The loaded parts are those clamped or under steady load, where PLA creeps and
   softens at about 55–60 °C. PETG-CF (on hand) replaces the plain PETG first planned; plain PETG is bought only if
   the spool holds less than the roughly 0.5–1 kg those parts need. The line was reworded in
   [shopping_list.md](../shopping_list.md).
2. **Fan: the agent recommends the CLOUDLINE S6 over the VEVOR VV-GDFJ-AC6.** The owner had asked, "which one do you
   think I should take ... do I get about 2 m/s more?" Answer: yes, about 1.7–2.1 m/s on paper. The owner asked again
   ("so which would you do?") and was told the S6. The owner has **not** chosen; D-011 stays Tentative. Reasons, with
   numbers in §6:
   - about a third more drag force at top speed;
   - the S6's 503 Pa is the maker's figure; the VEVOR's 300 Pa is a seller's listing that also claims an implausible
     34 dB;
   - an EC motor is usually steadier at low speed than an AC fan on a knob controller (general behaviour, not
     checked for these models), and most validation runs are at 6.5–10 m/s;
   - a wider matched-Re range for the two-ball blockage check;
   - worst cases: if the VEVOR falls short, the S6 is likely bought anyway ($54 lost); the S6's worst case is about
     12.3 m/s. The VEVOR still validates if the $45 matters.

   Recorded in [buy_list.md](../buy_list.md) §1 ("Choosing between the two"), the shopping list, PROJECT_STATUS §3 and
   TODO P0.
3. **Explained how the estimates are made** (owner asked):
   - Top speed is where a straight-line fan curve (free-air CFM to maximum static pressure) meets the tunnel's need,
     1.55 × ½ρV². The 1.55 is about 1.0 for the open exit (Mehta1979's method), 0.07 for wall friction (Mehta1979's
     typical value) and about 0.48 for the screens and honeycomb (Wieghardt's formula, the window screen).
   - Worked check for the S6 at 13.4 m/s: the tunnel needs 167 Pa; at 167 Pa the fan line gives 425 × (1 − 167/503)
     = 284 CFM, and 13.4 m/s × 0.01 m² is also 284 CFM.
   - The "sag" case uses 90 % of the straight-line flow.
   - Drag: F = ½ρV² C_D (πd²/4), with C_D from Brown and Lawler Eq. (19); for the 3/4 in ball at 13 m/s, Re ≈ 16,400,
     C_D ≈ 0.43, F ≈ 1.27 gf.
   - Matched Re: Re ∝ V d.
   - Limits: the straight-line curve is the largest assumption; the 1.55 is computed, not measured; the fan figures
     are taken at face value; ρ is fixed at 1.20 kg/m³; leaks and swirl are ignored. The gap between the two fans is
     more robust than either top speed.
4. **Other experiments the tunnel could do** (owner asked; ideas only, none chosen). Added to TODO P3 as one "ideas"
   item:
   1. **The fan's real curve:** printed exit plates with different holes; flow from the test-section speed × 0.01 m²;
      fan pressure from a tap just after the fan, with an upright water U-tube above the SDP810's 125 Pa (500 Pa is
      about 51 mm of water). Tests the straight-line estimate and the S6's 503 Pa.
   2. **Pressure around a cylinder:** a 3/8 in (about 9.5 mm) brass tube across the section, one 0.8 mm tap, one end
      sealed, the other out through the wall to the SDP810; turned in 10° steps with a printed dial. Compare with
      Cp = 1 − 4 sin²θ (matches at the front, fails behind separation at about 80°); integrating gives the pressure
      drag. Run at about 10 m/s or below, since the suction would exceed ±125 Pa at 13 m/s. About 9.5 % blockage:
      needs a correction.
   3. **The free jet at the open exit:** pitot traverses at several distances, showing the jet slow and spread
      (static pressure is atmospheric there); also a place to check a cheap handheld anemometer, within about one jet
      width of the exit.
   4. **A drag lineup of shapes** with the 3/4 in ball's 19 mm frontal size: a disc, a cup facing the wind and
      reversed, a cone and a teardrop. Textbook C_D (agent's memory, not checked): disc about 1.2, open cup about 1.4,
      reversed cup about 0.4, teardrop about 0.05–0.1. At 13 m/s each 1.0 of C_D is about 3 gf. The teardrop's
      0.15–0.3 gf is about the size of the sting's drag (0.1–0.2 gf), so it may not be measurable.
   5. **Vortex-shedding tone of a 1/8 in rod** across the section: St ≈ 0.2 gives about 410 Hz at 6.5 m/s and 820 Hz
      at 13 m/s; record by phone or laptop and read the peak with Audacity's "Plot Spectrum". The SDP810 (τ63 < 3 ms,
      plus tubing) and the HX711 (10 or 80 samples/s) are too slow. Fan noise may hide the tone.

   Not possible here: the drag crisis (top Re about 2.2×10⁴ with the 1 in ball at 13 m/s; a smooth sphere's crisis is
   near 3×10⁵ and dimples bring it to roughly 5×10⁴–10⁵, agent's memory, not checked); turbulence intensity and
   boundary-layer detail (need a hot-wire; the 1/8 in probe is larger than the roughly 2 mm floor boundary layer);
   models wider than about 22 × 22 mm (5 % blockage).
5. **Three mesh listings checked** for the flow-conditioning screens (details in [buy_list.md](../buy_list.md) §3,
   "Listings checked 2026-11-09"):
   - **35 × 35 mesh, 0.011 in wire, 0.0176 in opening, 37.87 % open, 1 × 2 ft for $17: not suitable.** Below the
     57–58 % limit (patchy flow; Mehta1977, Scheiman1981), and four screens would lose about 177 Pa against about
     38 Pa. Effectively the McMaster 30 × 30 mesh rejected on 2026-11-08.
   - **New York Wire 18 × 16, 0.011 in wire, bright aluminium, 48 × 84 in (UPC 011646101075): suitable.** The listing
     gives no open area; computed 66.1 %.
   - **McNichols item 3796113610 (Insect Screen series 3366): suitable.** Woven plain weave, bright aluminium,
     18 × 16, 0.011 in wire, 66 % open, sold as 100 ft coils with cut sizes. The same screen; price decides.
   - A second check added to the quick rule: thin wire. The settling-chamber screens must stay below u₁d/(βν) = 85
     (Wieghardt1953 eq. (15)); at 66 % open and 2.1 m/s that is wire of 0.016 in or thinner, about 12 mesh or finer.
6. **The screen chosen and ordered.**
   - The agent found the Home Depot product page by web search (§5). Its page gives 18 × 16 and Bright but no wire
     diameter; the owner then pasted the maker's spec: 18 × 16, "yarn diameter" 0.011 in, in 7, 25 and 100 ft, in
     charcoal, black and bright.
   - The agent advised Bright (bare aluminium, no finish to flake) in the 7 ft (36 × 84 in) roll.
   - The owner then wrote "screen ordered". Recorded as the Saint-Gobain ADFORS FCS9222-M, Bright, 36 × 84 in roll.
     The owner did not restate the item; price paid not recorded.
   - With 0.011 in confirmed by the maker, two diffuser screens give K_sum 2.15 against the 2.1 needed. **Three are
     planned for margin**, as the buy list already proposed.
7. **Documentation:** the screen marked Ordered in the shopping list (product link in place of the search link) and
   the buy list (new status word "Ordered"); the doc updates listed in §3.

## 3. Files and equipment affected

- [docs/buy_list.md](../buy_list.md):
  - "Ordered" added to the status words;
  - §1: the S6-against-VEVOR comparison, and the agent's recommendation;
  - §2: the load-cell mount "in PETG-CF";
  - §3: the screens row Ordered; the wire now known (0.011 in), three diffuser screens planned; the thin-wire rule;
    the three listings checked;
  - the running total's §3 row.
- [docs/shopping_list.md](../shopping_list.md): the screen row Ordered with the product link; the to-buy total
  (about $245–350); a note under the fan rows; the PETG-CF line reworded.
- [PROJECT_STATUS.md](../../PROJECT_STATUS.md): `507f71c` backfilled (header, §4, §6, §13); the first order; the fan
  recommendation (header, §3, §9, §12); screens (§2, §3, open question 13); §6 and §8 entries.
- [TODO.md](../../TODO.md): P0 (fan recommendation, ordered so far, PETG-CF), P1 (screens task, settling-chamber
  pointer), P2 (screen arrival check), P3 (experiment ideas), Done (push of `507f71c`, screen ordered).
- [docs/experimental_setup.md](../experimental_setup.md): current configuration (one part ordered), the screens row, a
  change-history row.
- [docs/sessions/SESSION_LOG.md](SESSION_LOG.md): `507f71c` backfilled; this session's row.
- [2026-11-09-drawing-package.md](2026-11-09-drawing-package.md): commit field backfilled with `507f71c` (the only edit).
- **Equipment:** the window screen ordered (not yet arrived). Nothing else bought, built or changed.

## 4. Experimental procedures performed

None. No physical work this session.

## 5. Commands and scripts executed

```bash
python scripts/sync_status.py --fetch       # catchup: UP_TO_DATE at 507f71c; wrap: UP_TO_DATE
git status --short; git log --oneline -15; git diff --stat; git show --stat 507f71c
git log --format=%h -1 -- docs/sessions/2026-11-09-drawing-package.md    # 507f71c, for the backfill
python scripts/check_docs.py
python -m unittest discover -s tests        # catchup; -v at wrap (§7)
```

Web search (Claude Code WebSearch, standard mode, `allowed_domains: homedepot.com`): "Home Depot bright aluminum
screen 36 in x 84 in 18 x 16 roll". Found the Saint-Gobain ADFORS FCS9222-M page
(https://www.homedepot.com/p/Saint-Gobain-ADFORS-36-in-x-84-in-Bright-Aluminum-Screen-Roll-for-Windows-and-Door-FCS9222-M/100397106),
the charcoal FCS9370-M, and Phifer 3000043 (brite aluminium). Prices in the results ($8.98–10.98) came from cached
pages and may be stale.

Estimate scripts, run from the session scratchpad with `python -I <file>`. Same models as the buy-list session's
`s6speed.py`, `balance.py` and `screens.py` ([2026-11-09-buy-list.md](2026-11-09-buy-list.md) §5).

`fancompare.py` (fan comparison, forces, matched-Re ranges):

```python
rho, A, CFM, mu, g = 1.20, 0.01, 2118.88, 1.81e-5, 9.80665
def top(Qf, Pm, k=1.55, sag=1.0):
    lo, hi = 0.1, 40
    for _ in range(80):
        m = (lo+hi)/2
        lo, hi = (m, hi) if sag*Qf*(1 - k*0.5*rho*m*m/Pm) > A*m*CFM else (lo, m)
    return lo
cd = lambda Re: (24/Re)*(1 + 0.150*Re**0.681) + 0.407/(1 + 8710/Re)
F = lambda V, d: 0.5*rho*V**2*cd(rho*V*d/mu)*3.14159265*d*d/4/g*1000   # gf
d34, d1 = 0.01905, 0.0254
print("S6 425/503:", round(top(425,503),2), "(90%:", round(top(425,503,sag=0.9),2), ")")
print("S6 402/503:", round(top(402,503),2), "(90%:", round(top(402,503,sag=0.9),2), ")")
for P in (300, 250, 200):
    print(f"VEVOR 400/{P}:", round(top(400,P),2), "(90%:", round(top(400,P,sag=0.9),2), ")")
for V in (13.0, 11.3, 10.0, 9.4):
    print(f"V={V}: 3/4in {F(V,d34):.2f} gf, 1in {F(V,d1):.2f} gf; 0.05 g = {0.05/F(V,d34)*100:.1f}% of 3/4in drag")
lo = 6.5
for name, Vt in (("S6", 13.0), ("VEVOR", 11.3), ("VEVOR@250Pa", top(400,250))):
    hi1 = Vt*d34/d1     # matched Re: 3/4 in at V matches 1 in at V*d34/d1; 1 in floor 6.5 m/s
    rise = cd(rho*Vt*d1/mu)/cd(rho*lo*d34/mu)-1
    print(f"{name}: top {Vt:.1f}; 1in matched-Re range {lo}-{hi1:.2f} m/s (span {hi1-lo:.2f}); C_D rise 3/4@6.5->1@top {rise*100:.1f}%")
```

`sens.py` (top speed against the tunnel's loss factor, and the worked checks): the same `top()`, then

```python
for Qf, Pm in ((425,503),(402,503),(400,300)):
    print(Qf, Pm, [round(top(Qf,Pm,k),2) for k in (1.25,1.5,1.55,1.75)])
V=top(425,503); q=0.5*rho*V*V; need=1.55*q
print(f"S6 worked: V={V:.2f} q={q:.1f} need={need:.1f} Pa, fan flow at that P={425*(1-need/503):.1f} CFM, tunnel flow={V*A*CFM:.1f} CFM")
V=top(400,300); q=0.5*rho*V*V; need=1.55*q
print(f"VEVOR worked: V={V:.2f} q={q:.1f} need={need:.1f} Pa, fan flow={400*(1-need/300):.1f} CFM, tunnel flow={V*A*CFM:.1f} CFM")
```

`mesh35.py` (screen K and loss, and the top speed with each mesh):

```python
nu, rho = 1.5e-5, 1.20
def k(u, d_m, beta): return 6.5*(u*d_m/(beta*nu))**(-1/3)*(1-beta)/beta**2
q = lambda u: 0.5*rho*u*u
u_out, u_ch, q0 = 7.4, 2.08, q(13.0)
def four(mesh, wire_in):
    beta = (1 - mesh*wire_in)**2; d = wire_in*0.0254
    ki, kc = k(u_out, d, beta), k(u_ch, d, beta)
    loss = ki*q(u_out) + 3*kc*q(u_ch)          # one screen at the fan outlet, three at chamber speed
    return beta, ki, kc, loss
beta_w = (1-0.011*18)*(1-0.011*16); d=0.011*0.0254   # window screen, 18 x 16 rectangular
lw = k(u_out,d,beta_w)*q(u_out) + 3*k(u_ch,d,beta_w)*q(u_ch)
# ... printed K and losses for the window screen, McMaster 30x30x0.012 and the offered 35x35x0.011, then:
base = 1.55 - 48/q0     # the 1.55 budget included about 48 Pa of screens at 13 m/s
for name, L in (("window", lw), ("McMaster 30x30", four(30,0.012)[3]), ("offered 35x35", four(35,0.011)[3])):
    kk = base + L/q0     # top() as above, with this k
```

Inline arithmetic (our arithmetic):
- the open area of an 18 × 16 mesh with 0.011 in wire: 0.802 × 0.824 = 0.661;
- the wire at which it falls to 58 %: 288w² − 34w + 0.42 = 0, so w = 0.0140 in;
- the thickest settling-chamber wire at 66 % open: 85 × 0.66 × 1.5×10⁻⁵ / 2.08 = 4.05×10⁻⁴ m = 0.016 in, about
  11.7 mesh;
- an 8 × 8 × 0.023 in mesh: (1 − 0.184)² = 0.666 open, u₁d/(βν) ≈ 122;
- the rod's shedding frequency: f = 0.2 V/d with d = 3.175 mm.

## 6. Measurements and results

None measured. All numbers below are **estimates (our arithmetic) from listed fan figures, Mehta1979's loss method,
Wieghardt's screen formula and Brown and Lawler's Eq. (19), not results.**

Fan top speed (straight-line fan curve; tunnel needs 1.55 q₀; figure in brackets at 90 % of the straight-line flow):

| Fan (listed figures) | Top speed |
|---|---|
| S6, 425 CFM / 503 Pa | 13.40 m/s (12.68) |
| S6, 402 CFM / 503 Pa | 13.02 m/s (12.30) |
| VEVOR, 400 CFM / 300 Pa | 11.35 m/s (10.82) |
| VEVOR if really 250 Pa | 10.75 m/s (10.29) |
| VEVOR if really 200 Pa | 10.04 m/s (9.64) |

Top speed against the tunnel's loss factor k (needed fan pressure = k × q₀):

| Fan | k = 1.25 | 1.50 | 1.55 | 1.75 |
|---|---|---|---|---|
| S6, 425 CFM | 14.11 | 13.51 | 13.40 | 12.99 |
| S6, 402 CFM | 13.68 | 13.12 | 13.02 | 12.64 |
| VEVOR, 400 CFM / 300 Pa | 12.04 | 11.45 | 11.35 | 10.95 |

The S6 (425 CFM) leads by 2.04–2.07 m/s at every k.

Forces and the validation range:
- Drag at 13.0 / 11.3 / 10.0 / 9.4 m/s: 3/4 in ball 1.27 / 0.95 / 0.73 / 0.64 gf; 1 in ball 2.31 / 1.73 / 1.34 /
  1.17 gf. The TAL221's 0.05 g error figure is 3.9 / 5.3 / 6.8 / 7.8 % of the 3/4 in ball's drag.
- Matched-Re range of the 1 in ball (from 6.5 m/s): 6.5–9.75 m/s with the S6 at 13.0; 6.5–8.48 with the VEVOR at
  11.3; 6.5–8.07 with the VEVOR at 250 Pa.
- Predicted C_D rise (3/4 in at 6.5 m/s to 1 in at top speed): 9.2 %, 8.0 %, 7.5 % respectively.

Screens (four screens: one at the 7.4 m/s fan outlet, three at the 2.08 m/s chamber speed; 13 m/s in the test section):

| Mesh | Open | K at fan outlet / chamber | Loss of four | S6 top (90 %) | VEVOR top (90 %) |
|---|---|---|---|---|---|
| Window screen 18 × 16 × 0.011 in | 66.1 % | 0.85 / 1.30 | 38 Pa | 13.6 (12.9) | 11.6 (11.0) |
| McMaster 30 × 30 × 0.012 in (rejected 2026-11-08) | 41.0 % | 3.19 / 4.88 | 143 Pa | 11.8 (11.3) | 9.8 (9.4) |
| Offered 35 × 35 × 0.011 in | 37.8 % | 3.96 / 6.04 | 177 Pa | 11.4 (10.9) | 9.4 (9.1) |

The 13.6 m/s for the window screen is higher than the 13.4 elsewhere because this row swaps the 48 Pa in the 1.55
budget for the window screen's 38 Pa. The McMaster row reproduces the buy list's 11.8 (11.3).

## 7. Tests, calibration checks and validation

- **`python scripts/check_docs.py`:** 0 failures, 0 warnings at `/catchup` and after the shopping-list edit.
- **`python -m unittest discover -s tests -v`:** 20 tests OK in 12.6 s at the wrap (10.2 s at `/catchup`).
- **Estimate cross-checks:** the scripts reproduce the documented figures: VEVOR 11.3 (10.8), S6 13.4 (12.7) and
  13.0 (12.3), McMaster 11.8 (11.3), window-screen K 0.85 / 1.30 and 38 Pa, and 1.27 gf on the 3/4 in ball at 13 m/s.
  The worked S6 and VEVOR checks balance (284 CFM, 240 CFM).
- **McNichols listing self-consistency:** its openings and pitch give 66.1 %, matching its "66 %".
- **Not performed:** no physical check. The screen has not arrived; its wire count and diameter are unchecked.
- **`python scripts/check_docs.py` after the wrap edits:** 0 failures, 0 warnings; 12 session logs each indexed
  once, 578 links resolve, 90 committable files, none over 25 MiB, no obvious secrets.

## 8. Errors, failed approaches and troubleshooting

- **Overstated advice, corrected in the conversation:** the agent first said not to pick the charcoal screen
  because it is coated. The maker's spec then gave the same 0.011 in for all three colours, so charcoal or black would
  have been an acceptable second choice. Bright was still chosen.
- **The Home Depot page gives no wire diameter or open area** (only 18 × 16). Settled by the maker's spec, which the
  owner found. The page's "Package Quantity: 16" is probably a case count; not checked.
- **A mesh listing rejected:** the 35 × 35 × 0.011 in mesh (§2, item 5).
- **Minor, in an older log (not edited):** the buy-list log's `s6speed.py` comment `# 13.12-13.68; 13.51-14.11`
  shows only the k = 1.5 and 1.25 values of a loop that also prints k = 1.75 (12.64 and 12.99 m/s). The figures
  quoted in the docs are unaffected.
- A "file modified on disk" notice appeared for `docs/shopping_list.md` during the session. `git diff` showed only
  this session's edits, so it was probably OneDrive touching the file.

## 9. Decisions and reasoning

No new decision in [DECISIONS.md](../../DECISIONS.md).
- The fan stays open (D-011, Tentative). The agent's recommendation of the S6 is recorded in the buy list, not as a
  decision; the owner will record the choice as a new decision superseding D-011.
- The screen purchase follows the buy list's 2026-11-09 proposal (aluminium window screen, three diffuser screens);
  no decision changed.

## 10. Open questions and blockers

- The fan: S6 or VEVOR (owner, on budget).
- The screen order: the owner wrote "screen ordered" without restating the item. Recorded as FCS9222-M, Bright,
  36 × 84 in (what was being discussed); price paid and delivery date not recorded.
- Unchanged: the owner's 2026-11-10 report of household items and filament amounts (now including the PETG-CF spool);
  the electronics order; the sizing questions (open questions 13 and 15).

## 11. Remaining tasks

- Owner:
  - commit and push this session (§13);
  - choose the fan;
  - report the household items and filament amounts (2026-11-10);
  - order the electronics and small parts;
  - check the screen on arrival (wires per inch, one wire about 0.28 mm, Bright) and store it flat;
  - confirm the screen item and price paid if they differ from what is recorded.
- Agent: build step 1 (sizing), unchanged from the drawing-package log.

## 12. Recommended first task for the next agent

Unchanged from the [drawing-package log](2026-11-09-drawing-package.md#12-recommended-first-task-for-the-next-agent):
start build step 1 (sizing) with the settling-chamber spacing and how the 250 mm sections split in cross-section for
the 256 mm bed. Use three diffuser screens of the ordered window screen (0.011 in wire). Then update
`docs/drawings/wtdata.py` and rebuild. If the owner reports the fan choice first, record it as a new decision
superseding D-011.

## 13. Manual Git commands (as given to the owner)

State at the wrap: `UP_TO_DATE` at `507f71c`; nothing staged; 7 files modified and 1 new (this log).

```bash
cd "C:/Users/nuhbm/OneDrive/Desktop/nuhs projects/2 - Wind Tunnel"
python scripts/sync_status.py --fetch
# Expect UP_TO_DATE. If BEHIND: run  git pull --ff-only  first. If FETCH_FAILED: fix the network first.
git status
git diff
git add PROJECT_STATUS.md TODO.md docs/buy_list.md docs/shopping_list.md docs/experimental_setup.md
git add docs/sessions/SESSION_LOG.md docs/sessions/2026-11-09-drawing-package.md docs/sessions/2026-11-09-fan-advice-and-screen-order.md
git status
git diff --cached --stat
git commit -m "Record fan advice and the first order (window screen)" -m "Records the agent's recommendation of the S6 over the VEVOR with worst-case estimates (the owner has not chosen), checks of three mesh listings, experiment ideas for later, and the owner's order of the aluminium window screen (Saint-Gobain ADFORS FCS9222-M, 0.011 in wire, 66 % open). Backfills 507f71c."
git push origin HEAD
python scripts/sync_status.py --fetch
```

- **Staging:** `git status` should then show 8 paths under "Changes to be committed". Nothing else should be left.
- **Harmless warnings:** "LF will be replaced by CRLF" can be ignored.
- **If the push asks for credentials:** `gh auth status` or `gh auth login`, or sign in through Git Credential Manager.
- **If the push is rejected** ("fetch first" / "non-fast-forward"): do not force-push. Run
  `git pull --rebase origin main`, then `python -m unittest discover -s tests`, then `git push origin HEAD`.
- The last command should end with `STATE: UP_TO_DATE`.
