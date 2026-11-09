# Buy List

**Last updated:** 2026-11-09

Everything the tunnel needs, from the fan to the screws, with what is already on hand. Started 2026-11-08 with the
owner. It is worked through category by category; a section marked **Not reviewed yet** lists what is expected there,
without a chosen part.

- **Status words** (as in the parts inventory): **On hand**, **To buy**, **Unknown** (not known whether the owner has
  it). "Printed" means it comes off the P1S and costs only filament.
- **When:** **Now** = the choice does not depend on sizing; **After sizing** = the size or quantity comes from build step
  1 ([TODO.md](../TODO.md) P1); **Later** = build steps 2–7 or optional.
- **Prices** are what a listing showed on the date given. They are guides, not quotes, and exclude tax and shipping.
- When a part is bought, change it to On hand here and record its model and datasheet in
  [experimental_setup.md](experimental_setup.md) and [PROJECT_STATUS.md](../PROJECT_STATUS.md) §3.

## Running total

| Section | Status | Subtotal (to buy) |
|---|---|---|
| 1. Fan and air supply | Reviewed 2026-11-08/09; fan S6 or VEVOR (owner to choose) | about $118–123 with the S6, or $73–78 with the VEVOR, plus up to about $37 for duct tape and a power strip if not on hand |
| 2. Tunnel body | Reviewed 2026-11-09: PLA, PETG-CF and a hardened nozzle on hand; printed feet, no plywood | about $30–90, plus any PLA top-up |
| 3. Flow conditioning | Proposed 2026-11-09: aluminium insect screen (four or five screens); printed honeycomb (owner) | about $10 |
| 4. Test section and model access | Proposed 2026-11-09; magnets on hand (8 × 2 mm) | about $20–29 |
| 5. Airspeed | Reviewed 2026-11-08: make the probe, one sensor | about $47–70, plus $5–8 for the optional bender |
| 6. Force balance and models | Reviewed 2026-11-08: two load cells, 3/4 in and 1 in balls (owner) | about $61–64; balls may cost more in small quantities |
| 7. Ambient conditions | Proposed 2026-11-08 | $14.95 |
| 8. Electronics and wiring | Reviewed 2026-11-08/09: no display or knob (D-012); breadboard then PCB, no shield | about $15–23, plus about $20–30 if wire, heat-shrink and solder are not on hand |
| 9. Calibration | Reviewed 2026-11-08: home-made manometer, budget weights checked on a school lab balance | about $28–56, less what is in the house |
| 10. Tools (partly) | Calipers and hand drill on hand; battery, tube cutter, drill bits; files and hacksaw if not in the house | about $15–25, plus up to about $20 |
| 11. Later and optional | Reviewed 2026-11-09: PCB with sockets after the breadboard test; cars with mist, lift maybe never | nothing now |
| **Total, sections 1–10** | Estimate, 2026-11-09 | **about $315–505** before tax and shipping (the low end with the VEVOR fan), plus up to about $100 for items that may already be in the house, and about $15–20 per kg of PLA if the spools on hand run short |

## 1. Fan and air supply (reviewed 2026-11-08)

Decided: [D-010](../DECISIONS.md) (13 m/s target). **The fan is open between two ([D-011](../DECISIONS.md),
Tentative since 2026-11-09): the owner will choose on budget.** Nothing has been ordered yet.

| Item | What to buy | Qty | Price seen | Where | When | Status |
|---|---|---|---|---|---|---|
| Fan, **option 1** | **AC Infinity CLOUDLINE S6, model AI-CLS6**, with its 10-speed controller. EC motor; 425 CFM and 503 Pa (maker). About 13.0–13.4 m/s (estimate) | 1 | $99.00 (AC Infinity, 2026-11-08) | [acinfinity.com](https://acinfinity.com/hydroponics-growers/ventilation/inline-fan-systems/cloudline-pro-s6-quiet-inline-duct-fan-system-with-speed-controller-6-inch/) | Now | To buy, if chosen |
| Fan, **option 2** | **VEVOR 6-inch inline duct fan, model VV-GDFJ-AC6**, with its variable speed controller. AC motor, 60 W, 2600 rpm; 400 CFM and 300 Pa (seller's figures); 306 × 255 × 212 mm, 2.84 kg. About 11.3 m/s (estimate) | 1 | $53.90 (listing pasted by the owner, 2026-11-09) | VEVOR | Now | To buy, if chosen |
| Fan-to-tunnel joint | **Owner's design (2026-11-08):** a printed diffuser inlet about 25–30 mm deep, as small as possible: the fan's collar, wrapped in one layer of the neoprene, is a snug slide fit. Duct tape seals the outside of the joint | 1 | filament | Printed | After the fan arrives | Printed |
| Neoprene sheet | **40A (soft), 1/16 in (1.6 mm) × 12 × 24 in**, smooth, no adhesive backing (Rubber-Cal 30-004-062). For the collar wrap and the stand-foot pads, with plenty spare | 2 (sold in pairs) | $6.89 each, $13.78 a pair (Zoro, 2026-11-08) | [Zoro](https://www.zoro.com/rubber-cal-neoprene-sheet-40a-smooth-finish-no-backing-0062-thick-x-12-width-x-24-length-black-30-004-062/i/G3210068/) | Now | To buy |
| Duct tape | Cloth duct tape | 1 roll | about $5–10 (typical, not checked) | Hardware store | Now | Unknown (probably in the house) |
| Fan stand feet | 4 soft rubber or silicone bumper feet, about 20–25 mm, the softest available | 4 | about $5–10 (typical, not checked) | Hardware store | Now | To buy |
| Fan stand | A printed or plywood cradle, separate from the tunnel base | 1 | filament or scrap wood | Printed | After sizing | Printed |
| Inlet guard | A printed open grille over the fan inlet | 1 | filament | Printed | Later | Printed |
| Power switch | A UL- or ETL-listed power strip with a lighted on/off switch, within reach at the bench. **Buy it; do not build it** (see notes). The fan has a US NEMA 5-15 plug | 1 | about $16–27 for the listings seen (2026-11-08) | Any hardware store | Now | Unknown (check the house first) |

Notes:

- **Fan figures** (maker's page, read 2026-11-08): 425 CFM; 503 Pa (2.02 inH₂O) static pressure; 30 dBA;
  PWM-controlled EC motor; 10 speed levels; dual ball bearings; 100–240 V AC, 70 W maximum, 0.94 A; 7.87 × 12.60 ×
  8.35 in (32.0 cm long); mounting holes 80 × 60 mm, 6 mm diameter; 10 ft cord to the controller; mounts in any
  orientation. No fan curve, weight or collar diameter is given.
- **Buy model AI-CLS6.** Retailers call it the "CLOUDLINE PRO S6" and list 402 CFM. AC Infinity's other 6-inch fans
  (for example the CLOUDLINE A6, $89.99) have not been checked against 13 m/s.
- **Expected top speed** (estimate, straight-line fan curve): 13.5–14.1 m/s at 425 CFM. Real curves sag; at 80–90 %
  of the straight-line flow it is 12.0–13.3 m/s. The pitot will measure the real figure.
- **Low end:** an old forum post gives about 144 CFM free air at speed 1, which would be about 4.7–4.9 m/s in the
  tunnel (affinity-law estimate). So the 10 levels should cover the 6.5–13 m/s validation range in steps of roughly
  1 m/s. Not confirmed; the per-level airflow is not published.
- **Fan-to-tunnel joint (owner's design, 2026-11-08):** the fan's collar slides into a slightly larger printed inlet,
  and duct tape seals the joint. It replaced two earlier ideas the same day: AC Infinity's 6-inch Noise Reduction
  Clamp (about $17) and a home-made neoprene sleeve with printed clamps.
  - **The fan must never touch the print directly**, or it carries its vibration along the tunnel to the balance. The
    neoprene wrap around the collar, where it sits in the inlet, makes every contact rubber on plastic and centres the
    fan.
  - **Inlet size (owner: "the lowest possible value", 2026-11-08):** inside diameter = measured collar diameter +
    2 × 1.6 mm (one neoprene layer) + about 0.5 mm of print clearance, so the wrapped collar slides in snugly. For a
    150 mm collar that is about 153.7 mm (6.05 in). The owner's first figure was 6.25 in (158.75 mm).
  - **Print a short test ring first** (a 10 mm tall slice of the inlet, cheap and quick) and adjust the diameter until
    the wrapped collar slides in with a light push. The paper-strip measurement (§10) is good to about 0.3 mm, and
    printed holes come out a little under size, so the test ring settles it.
  - The fan's stand carries its weight; the tunnel does not hold the fan.
  - Losses: the step from the collar into the inlet is negligible. At 13 m/s it is about 0.4 Pa at 158.75 mm and
    under 0.1 Pa at 153.7 mm (sudden expansion, K = (1 − A₁/A₂)², collar q ≈ 32 Pa; our arithmetic), against the fan's
    roughly 150 Pa.
  - Leaks here blow outwards, upstream of all the flow conditioning, so they cost a little flow, not flow quality.
    Check the taped joint at full speed with a strip of tissue anyway.
  - Duct tape's adhesive ages, so expect to re-tape it now and then; cut the tape to remove the fan.
- **Stand feet:** the soft rubber sleeve does most of the isolating, and the stand is separate from the tunnel base.
  Avoid heavy-duty isolators rated tens of pounds each (for example 2-inch Sorbothane hemispheres, 25–38 lb each):
  under a fan of a few kilograms (weight not published) they barely compress, so they isolate little. Free fallback:
  stacked pads cut from the spare neoprene sheet. The real test comes later: load-cell noise with the fan on
  versus off.
- **Power switch: buy, do not build.** The ECE kit holds no mains-rated parts. A home-built mains switch box needs a
  switch rated for 120 V AC and 15 A, a closed enclosure, strain reliefs, a fuse and 14 AWG wire, and one wiring mistake
  can shock someone or start a fire. A listed strip costs less than those parts. Mains never goes on the breadboard,
  and the Arduino never switches it.
- **The controller remembers its last speed** when power is cut (maker's page), so the fan restarts at that speed when
  the strip is switched back on. Turn the controller down first if your hands are near the inlet.
- **Measure the fan's outlet collar when it arrives**, before printing the diffuser. That is one reason to buy the fan
  first. The owner's 6 in calipers may not span it; the paper-strip method in §10 works instead.
- **Speed control from the Arduino menu:** buy nothing for it yet. Hobbyists report a 10 V PWM signal on the UIS
  port, but no source found confirms the pinout (D-011, open question 11).
- Check the box for mounting brackets; the maker's page does not list the contents. Warranty: 2 years (site banner).

## 2. Tunnel body (proposed 2026-11-09; amounts firm up at sizing)

| Item | What to buy | Qty | Price seen | Where | When | Status |
|---|---|---|---|---|---|---|
| Filament, PLA | **PLA** for the shells (diffuser, settling chamber, contraction, test-section frame), the printed honeycomb, boxes, the fan stand and the base feet: stiffest and most accurate. **Black** for the test section and contraction, for contrast in any later mist visualization and less glare in photos | 2.5–3 kg | about $15–20/kg for any top-up (typical, not checked) | Bambu, Amazon | After sizing | **On hand** (owner, 2026-11-09; amount unknown) |
| Filament for loaded parts | For anything clamped or under steady load: screen frames, sting lock, overload stops, the load-cell mount, the ball-drilling jig. **PETG-CF is on hand** (owner, 2026-11-09; amount unknown): stiffer than PETG and creeps less, but abrasive. Use it only with a hardened-steel nozzle; otherwise buy plain PETG | 0.5–1 kg | | | After sizing | **On hand:** PETG-CF, and a hardened-steel nozzle (owner, 2026-11-09). Nothing to buy unless the PETG-CF runs short |
| Heat-set inserts | Brass, M3, for screws into printed parts | 1 pack of 100 | about $11–20 (listings) | Amazon, electronics distributors | Now | To buy |
| Screws, nuts, washers | An M3 and M4 assortment (stainless) for joining segments; a small **brass** M3 set for anything near the balance | 1 + 1 | about $10–15 + $8–10 (typical, not checked) | Hardware store, Amazon | Now | To buy |
| Gasket for joints | The foam tape from §4, between bolted flanges | | | | | §4 |
| Sealant | Clear silicone, for joints that never come apart | 1 tube | about $6 (typical, not checked) | Hardware store | After sizing | Unknown |
| Glue | Super glue and 5-minute epoxy (brass stubs into printed walls, small repairs). Neither bonds the Delrin balls (§6) | 1 each | about $5–10 each (typical, not checked) | Hardware store | Now | Unknown (may be in the house) |
| Contraction finish | Sandpaper, 220–600 grit; optional filler primer spray, for a smooth inside on the contraction | 1 set | about $10–15 (typical, not checked) | Hardware store | After sizing | Unknown |
| Base | **Printed feet under each section instead of a plywood board** (owner, 2026-11-09). The bolted, pinned box sections keep themselves in line; the balance module mounts to the test-section frame. The fan stands apart on its own feet | | filament | Printed | After sizing | Printed |
| Rubber pads | Under the printed feet, so the tunnel sits steady and table vibration is damped. Pads cut from the spare neoprene (§1) also work | 6–8 | about $5 (typical, not checked) | Hardware store | After sizing | Unknown |

**Subtotal:** about $30–90 (inserts, screws, glue, sealant, sandpaper, rubber pads), plus about $15–20 per kg of any
PLA to add; less what is on hand. The owner will check the house for these on 2026-11-10.

Notes:

- **Joints bolt together, not glue** (a refinement of D-005's "glue Tentative"): flanges with M3 screws into heat-set
  inserts, or M4 bolts, and foam tape between them, so the screen frames can come out for cleaning (Mehta1977 clamps
  frames with drawbolts). Keep joints away from the contraction exit (D-005 notes).
- **PLA or PETG** (owner asked which filament is best, 2026-11-09): PLA is stiffer and prints more precisely, but it
  creeps under steady load and softens at about 55–60 °C (a car or a sunny window). PETG is tougher and creeps less.
  So PLA for the shells, PETG wherever something is clamped or holds a load.
  - Carbon-fibre-filled filaments are abrasive and need a hardened-steel nozzle. The owner has PETG-CF and a
    hardened-steel nozzle (2026-11-09), so PETG-CF takes the place of plain PETG for the loaded parts: it is stiffer and
    creeps less. Fit the hardened nozzle before printing it.
  - Not recommended: ABS or ASA (large 250 mm parts tend to warp; the heat resistance is not needed).
  - **No plywood base** (owner, 2026-11-09): with printed feet, the long assembly relies on its flanges, pins and bolts
    to stay straight. PLA can sag slowly under steady load, so give each section its own feet, and check the alignment
    with the spirit level and a straight edge after assembly and now and then.
  - Bambu's own filament loads tuned P1S settings automatically; other brands work with some tuning.
  - The load-cell mount is the one printed part where long-term stability matters most. Make it thick, in PETG, and
    revisit a metal bracket at sizing if the wind-off zero drifts.
- **Filament estimate (rough, our arithmetic):** about 0.75 m² of tunnel wall at 2–3 mm thick is about 1.9–2.8 kg; the
  printed honeycomb about 0.5 kg; frames, boxes, stands and jigs about 0.5 kg; plus about 20 % for failed prints:
  about 3–4 kg. Recompute at sizing.

## 3. Flow conditioning (proposed 2026-11-08; owner to choose the honeycomb)

**How many screens: four.** Two in the fan-to-chamber diffuser and two in the settling chamber, behind the honeycomb.
What the reviewed papers say (from their notes):

| Source | Diffuser | Settling chamber |
|---|---|---|
| [Mehta1977](../resources/notes/Mehta1977.md), on exactly this layout (a blower with a wide-angle diffuser) | Two K ≈ 1.5 screens gave the best result in his tests with blower swirl. Fig. 5: with two screens, A = 3.44 allows a diffuser of about 115 mm (none: about 335 mm) | Honeycomb, then 2–3 screens of K ≈ 1.5: "normally enough when the wide-angle diffuser also has screens" |
| [Mehta1979](../resources/notes/Mehta1979.md), the design rules for small tunnels | Its worked example: two screens of K = 1.5 in the diffuser | Two more screens of K = 1.5, plus a K = 0.5 honeycomb (four screens in all) |
| [Scheiman1981](../resources/notes/Scheiman1981.md), NASA turbulence tests | not covered | A honeycomb plus one screen already cut the incoming turbulence to about 0.3; screens behind a honeycomb work "better than screens alone" |
| [Abdelhamed2014](../resources/notes/Abdelhamed2014.md), a contraction study | One screen between its two diffusers | One at the second diffuser's exit. Both 43–50 % open, below the 57 % limit; not a model to copy |
| [Weakly2024](../resources/notes/Weakly2024.md) | A commercial tunnel; its screens are not described | |

Design the settling chamber with room for two screens. If its length must be cut, one screen plus the honeycomb
still follows Scheiman1981, and a second can be added later because the frames are removable.

| Item | What to buy | Qty | Price seen | Where | When | Status |
|---|---|---|---|---|---|---|
| Screens (proposed 2026-11-09) | **Aluminium window insect screen, "bright aluminum" (uncoated), 18 × 16 mesh**, wire about 0.010–0.011 in: 66–69 % open. A real woven-wire mesh. Not fibreglass, pet screen or solar screen | One 36 × 84 in roll (about 20 squares of 12 in) | about $9.49–9.68 (Saint-Gobain ADFORS rolls at Home Depot); Phifer sells the same in brite aluminium | Home Depot, hardware stores | Now | To buy |
| Screens (dropped) | TWP 24 mesh T304 stainless, 0.0075 in wire, 67 % open (SKU 024X024S0075), or 30 mesh T316 0.0065 in (SKU 030X030T0065) | | The $10 "from" price is a 3 × 3 in piece; the owner's quote for the needed size came to about $200 (2026-11-09): too expensive | TWP | | Not chosen |
| Screens (alternative) | Stainless 24 × 24 mesh, 0.0075 in wire, 67.2 % open, one 48 × 48 in sheet (16 pieces of 12 × 12 in) | 1 | $65.59 (Zoro listing; its open area is given as both 67.2 % and 65 %); the owner finds it too expensive (2026-11-08) | Zoro | | Alternative |
| Honeycomb | **Printed (owner's choice, 2026-11-08):** for example 6 mm hexagonal cells, single 0.4 mm walls, about 48–50 mm long, about 250 × 250 mm (fits the P1S bed in one piece). Straws stay the upgrade if the flow map shows a problem (see below) | 1 | filament | Printed | After sizing | Printed |
| Screen frames | Printed two-part frames that clamp each screen taut and wrinkle-free, removable for cleaning (Mehta1977) | 4 | filament | Printed | After sizing | Printed |

**Screen K and pressure loss** (Wieghardt's formula; our arithmetic, 2026-11-08/09; 13 m/s in the test section, about
7.4 m/s at the 150 mm fan outlet, 2.1 m/s in the settling chamber; script in this session's log):

| Mesh | Open | K at diffuser inlet | K in settling chamber | Diffuser K_sum, 2 screens (needs ≥ 2.1) | Loss of four screens |
|---|---|---|---|---|---|
| 30 × 30 × 0.0065 in | 64.8 % | 1.09 (35 Pa) | 1.66 (4.3 Pa each) | 2.75 | 48 Pa |
| 24 × 24 × 0.0075 in | 67.2 % | 0.91 (30 Pa) | 1.39 (3.6 Pa each) | 2.29 | 40 Pa |
| **Aluminium insect screen 18 × 16 × 0.011 in** | 66.1 % | 0.85 (28 Pa) | 1.30 (3.4 Pa each) | 2.15 | 38 Pa |
| Aluminium insect screen 18 × 16 × 0.010 in (Phifer's figure) | 68.9 % | 0.75 (24 Pa) | 1.15 (3.0 Pa each) | **1.90: too low with two** | 33 Pa |
| McMaster 30 × 30 × 0.012 in | 41.0 % | 3.20 (104 Pa) | 4.88 (12.7 Pa each) | 8.08 | 142 Pa |

- **With the insect screen, plan three diffuser screens** (five in all): the 0.010 in version gives only 1.90 with
  two. A third, in the middle of the diffuser where the air moves at about 3.7 m/s, adds K ≈ 0.95 for about 8 Pa,
  bringing K_sum to about 2.85 (our arithmetic). Mehta1977 allows up to about 4–5 screens in a diffuser. With the 0.011 in version,
  two are just enough, if the diffuser stays at the planned 150–200 mm rather than the 115 mm minimum.
- Measure the delivered screen's wire with the calipers and count the wires per inch against the steel rule, then
  settle two or three.
- Insect screen is softer and less precise than wire cloth: handle it flat, avoid creases, and tension it evenly in
  the frame. Its wires at chamber speed (u₁d/βν about 51–59) are still below the eddy-shedding limit of 85.
- **What the McMaster 41 % mesh would cost** (owner asked "what's the worst that can happen?", 2026-11-09): nothing
  breaks, and the sphere validation still works at 11–12 m/s. But the S6's estimated top speed falls from about 13.5
  to about 11.8 m/s (11.3 if the real curve gives 90 %), short of D-010, and the flow behind each screen turns patchy.
  The 6.25 contraction evens out speed differences strongly, but the extra unsteadiness is not quantified. The insect
  screen avoids both for about the same money.

- Both meet Mehta1977's K_sum ≥ 2.1 and the 57 % open-area limit. The 30-mesh has more margin and matches the screens
  Scheiman tested; the 24-mesh costs about 8 Pa less fan pressure.
- The settling-chamber K values are extrapolated below Wieghardt's fitted range, so they are uncertain.
- **Fan pressure check:** four screens cost about 40–48 Pa at 13 m/s, against the 18 Pa (0.18 q₀) that the fan
  estimate took from Mehta1979's typical figures. Nearly all of it is the diffuser-inlet screen, which sits in the
  fast flow at the fan outlet. With these losses the fan must supply about 1.55 q₀ (about 157 Pa) instead of
  1.25–1.5 q₀. The straight-line estimate for the S6 then gives about 13.4 m/s (425 CFM) or 12.7 m/s if the real curve
  gives 90 % of it (our arithmetic). Recompute at sizing, and consider placing the first screen slightly into the
  diffuser, where the air has already slowed: at 1.5× the outlet area the loss roughly halves.
- Type 304 stainless can be slightly magnetic after weaving; the screens are far from the balance, so it does not
  matter.

**Checking a mesh listing** (the owner found two on 2026-11-08):

- "30 × 30 mesh" means 30 wires per inch in each direction: holes about 0.7 mm square, 900 of them per square inch.
  It says nothing about the sheet's size, which is listed separately (for example 12 × 12 in).
- What matters is the **wire diameter**, which sets the open area, β = (1 − wire × mesh)². Mehta1977 and Scheiman1981
  want at least 57–58 % open; more closed screens make uneven, unstable flow and cost much more fan pressure.
  - 30 × 30: wire **0.0075 in or thinner** (0.0065 in → 65 % open; 0.0075 → 60 %; 0.0085 → 56 %, too closed).
  - 24 × 24: wire **0.0095 in or thinner** (0.0075 → 67 %; 0.0095 → 60 %; 0.010 → 58 %, borderline).
- **Online Metals 24 × 24, 0.014 in wire (304):** about **44 % open, not suitable.** Its K at the diffuser inlet would
  be about 2.5, a loss of about 84 Pa for that one screen (our arithmetic).
- **McMaster 30 × 30 stainless (link from the owner):** its page could not be read from here. One McMaster 30 × 30
  stainless cloth seen in a search has 0.013 in wire and 37 % open: not suitable. Pick one with 0.0065–0.0075 in wire.
- **McMaster 30 × 30 filter-mesh discs (9317T series; table pasted by the owner, 2026-11-08): not suitable.** All have
  0.012 in wire, 40 % open, and the largest is 4 9/16 in across. They are filter screens for pipes and extruders.
  Look under woven wire cloth sheets ("bolting cloth" for fine wire) instead.
- **McMaster 30 × 30 stainless filter-mesh sheets and cut lengths (table pasted by the owner, 2026-11-08): not
  suitable.** Every one, 304 and 316, has 0.012 in wire (41 % open; for example 85385T79, 1 × 1 ft $8.99, 2 × 2 ft
  $32.36) or 0.013 in wire (37 % open; for example 85385T78). McMaster's "filter mesh" category seems to stock only
  these thick-wire meshes; its separate "bolting grade wire cloth" category is the one to check. What the 41 % mesh
  would cost (owner asked, 2026-11-08; script in this session's log; Wieghardt's formula, straight-line S6 curve):
  - four screens would lose about 142 Pa at 13 m/s (104 Pa in the diffuser-inlet screen alone), against about 40 Pa
    for the 67 % mesh;
  - the fan would need about 2.5 q₀ instead of about 1.5 q₀, so the S6's estimated top speed falls from about 13.6
    to about 11.8 m/s (11.3 if the real curve gives 90 %), short of D-010's 13 m/s;
  - below about 57 % open, the flow behind a screen turns patchy (Mehta1977), the opposite of what the screens are for.
- **McNichols perforated aluminium, item 17145163M1 (spec sheet found by the owner, 2026-11-08): not suitable.** It is
  a punched sheet, 0.063 in thick, 1/4 in round holes on 5/16 in staggered centres, 58 % open, 24 × 24 in. A punched
  sheet is not a woven screen: each 6.4 mm hole makes its own jet, adding turbulence of that size, which takes a long
  distance to die out, and the jets' contraction gives a higher pressure loss than a woven screen of the same open
  area (agent's reasoning, not from the reviewed papers).
- **Quick rule for any listing: woven wire cloth, about 20–30 mesh, with the open-area column reading 58 % or
  more.**
- **TWP's online form cuts discs** (owner's screenshot, 2026-11-09). Values proposed: 15 in discs × 3 (or 4) for the
  10.5 in squares, since a square that size needs a circle at least 14.9 in across; a 7 in disc × 1 (or 2) for the fan-outlet
  screen; tolerance 0.025 in, the loosest; no certifications; no add-ons (measurement $50, ultrasonic cleaning $85).
  Discs waste the corners, so compare the total with Zoro's $65.59 sheet, or ask TWP for a plain 24 × 24 in sheet.
- **Sizes needed:** the first diffuser screen is about the fan outlet's size (6 in round, about 150 mm) or a little
  more if it sits slightly into the diffuser; the other three are about 250 mm (10 in) square. **Buy squares, not
  discs** (owner asked, 2026-11-08): cut the round one from a square with tin snips; the margin is clamped in the frame. With a margin for the
  frames, that is four pieces of about 12 × 12 in, plus spares: for example one 24 × 36 in or two 12 × 24 in sheets
  plus one 12 × 12 in.
- Why the 30-mesh is proposed over the 24-mesh: not the count itself. With thin wire, the 30-mesh gives more pressure
  drop per screen (K ≈ 1.1–1.7 against 0.9–1.4), which leaves more margin for keeping the diffuser flow attached
  (K_sum 2.75 against 2.29, where 2.1 is needed). Its finer wires also leave smaller wakes. The 24-mesh with 0.0075 in
  wire is a sound alternative and costs the fan about 8 Pa less.

**Honeycomb options** (cells about 2–6 mm, 7–10 cell diameters long, at least 250 × 250 mm; **printed chosen by the
owner, 2026-11-08**):

- **Aluminium honeycomb core,** bare, 1/8–3/16 in cells, about 1 in thick. The standard choice: thin foil walls, about
  98 % open. Small bare pieces with small cells were not found (McMaster's bare cores have 1/2 in cells; its 1/8 in
  cores come skinned with carbon fibre; a UK supplier sells 3 mm cells only 10–20 mm thick). Price unknown.
- **Drinking straws** (Loehrke and Nagib's method, cited in Scheiman1981; the owner has seen coffee straws used the
  same way in laminar-flow water fountains). **The upgrade if the printed one disappoints.** Thin walls (similar to
  aluminium), cheap, easy to find.
  - Sizes (our arithmetic, hexagonal packing): 4 mm straws need about 4,500 pieces for 250 × 250 mm at 32 mm long;
    5 mm about 2,900 at 40 mm; 6 mm about 2,000 at 48 mm. Each length is 8 straw diameters (Mehta1977's 7–10).
    About 5 mm balances fineness against count.
  - Use round, single-bore straws. Some coffee stirrers have two bores in a figure-8, which pack badly. The small
    triangular gaps between round straws simply act as extra cells.
  - Cut them in bundles, not one by one: tape a tight bundle of whole straws, cut it into 40 mm slices with a
    fine-tooth saw or a sharp knife, and keep the slices taped while moving them into the frame.
  - Pack them tight in a printed frame. Friction holds them, and the screen downstream stops any from creeping. Check
    the cut ends are square: a ragged face disturbs the flow.
  - Leave about 50 straw diameters (about 250 mm at 5 mm) or at least 150 mm before the first screen
    (Scheiman1981 notes); settle at sizing.
- **Printed:** for example 6 mm hexagonal cells with 0.4 mm walls, 50 mm long; about 87 % open (our arithmetic); free
  and quick. Its walls are thicker and its cells fewer (about 42 across, against about 150 suggested by Mehta1977), so
  it straightens less finely. **Chosen (owner, 2026-11-08).** It is acceptable here because:
  - at the settling chamber's 2.1 m/s, the wakes of 0.4 mm walls are small and slow (Reynolds number about 56, our
    arithmetic) and die out in the 150 mm or more before the first screen;
  - the two settling-chamber screens and the 6.25 contraction do most of the smoothing;
  - the frame is removable, so straws can replace it if the flow map (build step 3) shows uneven flow.

## 4. Test section and model access (proposed 2026-11-09)

The owner's concept: one test chamber whose top and/or side clear panel comes off to swap the model, held by magnets
(PROJECT_STATUS §2).

| Item | What to buy | Qty | Price seen | Where | When | Status |
|---|---|---|---|---|---|---|
| Window acrylic | **Clear acrylic, 1/8 in (3.2 mm), 12 × 24 in.** Cast is clearer and cuts more cleanly; extruded also works. Gives four or five panels of about 300 × 120 mm (the test section is 270–290 mm long) | 1 | $10.45, cast (Online Metals); Home Depot sells extruded sheets | Online Metals, Home Depot | Now | To buy |
| Acrylic scoring knife | Cuts 1/8 in acrylic by scoring and snapping | 1 | about $5–10 (typical, not checked) | Hardware store | Now | Unknown (may be in the house) |
| Magnets | **On hand: round magnets 8 mm × 2 mm** (owner, 2026-11-09; probably neodymium, not confirmed), embedded in the printed panel frames. About 8 per panel (4 in the panel, 4 in the frame), so about 16 for two panels, plus spares | | | | | **On hand: 43** (owner, 2026-11-09). Enough; nothing to buy |
| Gasket | Thin closed-cell foam tape, about 1/8 in thick and 1/4–3/8 in wide, adhesive-backed (weatherstrip). Also seals the tunnel's bolted joints (§2) | 1 roll | about $5–8 (typical, not checked) | Hardware store | Now | To buy (owner: "need to buy this for sure", 2026-11-09) |
| Locating lips or pins | So each panel lands in the same place every time, flush inside | | filament | Printed | After sizing | Printed |
| Probe guide | A printed guide that holds the probe and lets it move across the section for the flow map; holes plugged when not in use | 1 | filament | Printed | After sizing | Printed |
| Mist port and cap | The capped port after the last screen, for optional visualization later | 1 | filament | Printed | After sizing | Printed |

**Subtotal:** about $20–29 (magnets on hand), less what else is on hand.

Notes:

- **Holding force is tiny.** The test section sits near room pressure (a blower with an open exit), so the air pushes
  on a 300 × 120 mm panel with well under 1 N. The magnets mainly hold the panel in place; the lips locate it.
- **Magnets and the balance:** the sting is brass, the load cell aluminium and the nearby screws brass, so the magnets
  have nothing to pull on. Keep steel parts away from the balance's measured side. Mark the poles before embedding:
  one flipped magnet repels.
- Pause the print to drop magnets into pockets, so they sit under a thin skin of plastic. For the owner's 8 × 2 mm
  magnets, start with pockets about 8.2–8.3 mm across and 2.2 mm deep, and adjust after a test print.
- **Inside faces flush:** a 1 mm step at the contraction-to-test-section joint disturbs the flow just ahead of the
  sphere.

## 5. Airspeed (proposed 2026-11-08; owner to choose the options below)

The sensor's facts are from its datasheet, filed 2026-11-08 ([SDP8xx notes](../resources/notes/SDP8xx.md)), and
Sensirion's compensation note ([Sensirion2024 notes](../resources/notes/Sensirion2024.md)).

**Proposed layout** (agent, 2026-11-08; open question 10; confirm the method in Barlow1999 ch. 4 and 6). **The owner
chose to make the probe rather than buy one (2026-11-08).**

```text
fan → diffuser → [ settling chamber ] → contraction → [ test section ............ sphere ] → open exit
                     S taps (4)                          E taps (4)          M taps (4)
                                                                             probe tip (empty tunnel only)

Sensor 2:  High ← S ring   Low ← E ring  → contraction pressure drop → airspeed during force runs
Sensor 1:  High ← probe    Low ← M ring  → q at the model position  → flow map, and calibrates sensor 2
```

- **Sensor 1, q at the model position (M)** = the total pressure from a small brass tube facing upstream, minus the
  static pressure from wall taps at the same station. In a closed test section the static pressure is the same across
  the section, so wall taps can stand in for the static holes of a pitot-static tube. Used to map the flow (build
  step 3) and to calibrate sensor 2.
- **Sensor 2, during force runs, with no probe in the flow** (a probe would put its wake on the sphere). By Bernoulli
  and continuity, the pressure drop from the settling chamber (S) to the test-section entrance (E) is
  Δp = q_test × (1 − 1/CR²), which is 0.974 q_test at contraction ratio 6.25. Wall boundary layers and slightly
  uneven flow make the real constant a little different from theory, so it is measured once against sensor 1 in the
  empty tunnel. The E taps sit at least 1.5√C (150 mm) upstream of the sphere (Cooper1998 rule).
- **Three stations of four taps**, one in each wall, each joined into one line, to average out one bad tap. Read each
  tap alone first as a check: they should agree.

| Item | What to buy | Qty | Price seen | Where | When | Status |
|---|---|---|---|---|---|---|
| Pressure sensor | **Sensirion SDP810-125Pa** (order number 1-101597-01; DigiKey 1649-1073-ND, Mouser 403-SDP810-125PA) | **1** (owner, 2026-11-08) | $29.39–33.88 (DigiKey), $32.21–34.72 (Mouser): search snapshots, 2026-11-08 | DigiKey or Mouser, in one order with the other electronics | Now | To buy |
| I²C multiplexer | A TCA9548A or PCA9548 8-channel breakout (for example Adafruit 2717 or 5626). Needed only if a second SDP810-125Pa is added: both answer at address 0x25. Check it runs at 5 V | 1 | Adafruit 5626 $9.15 at Jameco (2026-11-08) | Adafruit, DigiKey, Mouser | Only with a second sensor | Not needed now |
| Probe and tap tube | **K&S round brass tube, 1/8 in OD × 12 in** (No. 8127): the total-pressure probe (about 150 mm) and 12 wall-tap stubs (about 20 mm each); the rest is spare | 2 | $1.79 (Ace Hardware) to $6.29 (Zoro), 2026-11-08 | Hardware or hobby store | Now | To buy |
| Tubing | Silicone tubing, **1/8 in (3.2 mm) inside diameter**, about 1/16 in wall. Fits the brass tube directly, and stretches over the sensor's Ø3.5–5.2 mm barbs | about 10 ft (3 m) | about $8–12 (typical, not checked) | Hardware store, aquarium supply, Amazon | Now | To buy |
| Barbed connectors | An assortment for 1/8 in tubing with at least 9 tees (3 per station, to join each station's four taps into one line) and at least 2 straight couplers (the swap points, see notes) | 1 assortment | about $6–10 (typical, not checked) | Same | Now | To buy |
| Tube labels | Coloured tape or tags to mark the four lines: probe, M, S, E | | | | | Unknown (probably in the house) |
| Tube bender (optional) | A spring bender for 1/8 in tube, so the probe's 90° bend does not kink | 1 | about $5–8 (typical, not checked) | Hobby store | Now | To buy, optional |
| Sensor wiring | Four thin wires soldered to each sensor's pins (2 mm pitch: no perfboard, no breadboard). From the wiring in §8 | | | | | §8 |
| Standard pitot-static tube (alternative) | **Dwyer 166-6**: 1/8 in diameter, 6 in insertion, 3 in tip, stainless; a recognised standard design | 1 | $140.35–167.25 (Dwyer, distributors, 2026-11-08) | Dwyer, Transcat | | Not chosen: the owner chose to make the probe (2026-11-08) |

**Subtotal (one sensor, owner's choice 2026-11-08):** about $47–70, plus $5–8 for the optional bender. A second sensor
and the multiplexer would add about $40–45.

**Swapping the tubes with one sensor** (proposed):

- Fit a short tube, about 10 cm, permanently on each sensor barb, and end each one in a straight barbed coupler. These
  are the sensor's "High" and "Low" pigtails. Swaps happen at the couplers, so the sensor's barbs and its solder joints
  are never pulled.
- High pigtail takes either the probe line or the S line. Low pigtail takes either the M line or the E line. Mark the
  four lines.
- Force runs: S on High, E on Low, all the time.
- Calibrating the contraction factor, at each fan setting: read S − E, swap to probe − M, swap back and read S − E
  again. Use the average of the two S − E readings, which cancels a steady fan drift. Wait a few seconds after each
  swap for the reading to settle.
- After swapping, check with the wind off that the reading returns to zero (within about 0.1 Pa). If it does not, a
  joint is leaking.
- Upgrade if swapping gets tedious: two small 3-way valves, one per port. A second sensor and the multiplexer remain
  the other option.
- First drift test once the tunnel runs: hold one fan setting and log S − E for 10 minutes. If it barely moves, one
  sensor is all the project needs.

Notes:

- **Why make the probe instead of buying the Dwyer ($140–167):**
  - A plain tube facing the flow reads the total pressure almost regardless of its tip shape. Our understanding is
    within about 1 % of q for misalignment up to about ±10°; confirm in Barlow1999 ch. 4.
  - The wall taps are needed anyway for the force-run reference.
  - The larger error is the sensor's 3 % span, and the money is better spent on calibrating it (§9).
  - A cheap drone pitot-static probe is not a good middle way: its static holes are not a standard design, and its
    error is not published.
- **Sensor accuracy:** 0.08 Pa + 3 % of reading, so 3.3 % of q at 6.5 m/s and 3.1 % at 13 m/s. The 3 % is a gain
  error: it shifts every reading by the same factor, so it matters for the comparison with Eq. (19), not much for the
  trend check. Calibrating against a water manometer (§9) should reduce it toward the 0.5 % repeatability.
- **Ambient-pressure correction, every reading:** true Δp = reading × 966 mbar / ambient pressure (Sensirion2024).
  Near sea level the raw reading is about 5 % high. The BME280 (§7) supplies the ambient pressure.
- **One sensor or two** (owner chose one, 2026-11-08): force runs only ever use the S − E reading, so a second
  sensor would help only on calibration and flow-map days. It would read the probe and the reference at the same
  moment and be a spare. With one sensor the readings are taken one after the other (swap procedure above). The diagram
  above shows the two pairs of pressures, whichever sensor reads them.
- **Mounting the sensor:** solder four thin wires straight to the pins, with a quick joint and no flux near the ports
  (the datasheet covers only wave soldering). Screw the body to a printed bracket through its two Ø2.9 mm holes, and
  mount it above its tubing so condensation drains away. Alternative: Sensirion's SDP800 series cap (DigiKey
  1649-1042-ND), which takes a Molex DuraClik 502351-0400 plug. Its crimp terminals are not identified yet.
- **Tubing:** keep each line short (aim for 0.5 m or less) and the two lines of a sensor the same length. The sensor
  draws a tiny flow through its tubes, and its datasheet does not say how much tubing it tolerates. Calibrating with
  the real tubing in place covers that.
- **Wall taps:** drill each hole about 0.8–1.0 mm, square to the wall, after printing, and remove any burr inside. A
  printed boss outside holds a short brass stub for the tubing. Drill bits: §10. Design at sizing.
- Prices are search snapshots: check them, and order the sensors with the other electronics (load cell, HX711,
  BME280) to share one shipping charge.

## 6. Force balance and models (proposed 2026-11-08; owner to choose the options below)

Load-cell facts are from its datasheet, filed 2026-11-08 ([TAL221 notes](../resources/notes/TAL221.md)). Estimates
are from a short script (this session's log), with sphere drag from Eq. (19) and an assumed sting C_D of 1.1.

| Item | What to buy | Qty | Price seen | Where | When | Status |
|---|---|---|---|---|---|---|
| Load cell | **TAL221 100 g straight bar** (SparkFun SEN-14727): 0.6 mV/V, safe overload 150 g, M3 mounting. Buy the **100 g** model: the datasheet's "100~1500 g" is the range of models in the family, not one cell's range | **2** (owner, 2026-11-08, after first choosing 1): one in use, one spare that can later become the lift cell (open question 14) | $15.95 each (Electronics123 listing; check SparkFun's own price) | SparkFun, DigiKey | Now | To buy |
| Load-cell amplifier | **SparkFun HX711 breakout** (SEN-13879): separate analog and digital supplies, 10 or 80 SPS selectable, documented schematic | 1 (a second only when a lift cell is added) | $11.50 (SparkFun listing) | SparkFun | Now | To buy |
| Validation spheres | **Acetal (Delrin) balls, 3/4 in (19.05 mm) and 1 in (25.4 mm)**, ±0.001 in (sizes confirmed by the owner, 2026-11-08). Non-magnetic, smooth, easy to drill | 2 of each (spares for drilling mistakes) | about $2.78 (3/4 in) and $4.42 (1 in) each in packs of 100–250 at Zoro; small quantities from McMaster-Carr, price not seen | McMaster-Carr | After sizing | To buy |
| Sting | Non-magnetic rod, about 85 mm: **K&S solid brass rod, 1/8 in** proposed. Diameter and material fixed at sizing (stiffness against the sphere's 100–150 Hz vortex shedding) | 1–2 | about $1–3 (typical, not checked) | Hardware or hobby store | After sizing | To buy |
| Sting shield | A streamlined fairing fixed to the tunnel floor around the sting, not touching it, leaving about 5 mm of sting exposed below the sphere | 1 | filament | Printed | After sizing | Printed |
| Sting lock and overload stops | A printed clamp that holds the sting during model swaps, and stops that let it move only slightly past full scale; brass M3 screws from §2 | 1 set | filament | Printed | After sizing | Printed |
| Ball-to-sting joint | **Press fit**, not glue (acetal is hard to glue): a hole drilled to the ball's centre with a printed jig, slightly smaller than the rod (see notes) | | | | After sizing | Printed jig |
| Ball stems and sting socket | K&S round brass tube, 5/32 in OD × 12 in: a short sleeve at the top of the sting, into which each ball's own 1/8 in stem slides (1/8 in fits inside 5/32 in) | 1 | about $2–3 (typical, not checked) | Hardware or hobby store | After sizing | To buy |
| Load-cell screws | M3, **brass** (non-magnetic) near the balance | from §2 | | | | §2 |
| Wiring | The cell's four wires soldered straight to the HX711 (no breadboard in the bridge; Weakly2024 lesson), and four wires from the HX711 to the Arduino | | | | | §8 |

**Subtotal (2 load cells, 1 HX711, 4 balls, rod, sleeve tube; owner's choices 2026-11-08):** about $61–64 at the
prices seen, more if McMaster's small-quantity ball prices are higher than the bulk prices used here.

Notes:

- **The sting needs a shield.** Bare, a 1/8 in sting with 40 mm in the flow below a 3/4 in sphere has about 115 % of
  the sphere's own drag (1.46 gf against 1.27 gf at 13 m/s). A 2 mm sting has about 75 %. Subtracting a drag as big as
  the one being measured, with unknown interference between the two, is the weakest point of balances like
  Weakly2024's. A fixed shield around all but about 5 mm of the sting cuts its drag to about 0.1–0.2 gf.
  - The shield is fixed to the tunnel, so its own drag never reaches the load cell.
  - Its blockage is in place when the probe is calibrated at the sphere's position, so it is calibrated out.
  - It must never touch the sting. Check by tapping the shield with the wind off: the reading must not change.
  - **Proposed size** (owner asked, 2026-11-08; final at sizing): a 5 mm hole for the 1/8 in (3.18 mm) sting, which
    leaves about 0.9 mm all round for printing error and the sting's small movement up to the overload stops. Printed
    walls of about 1.2 mm (three lines of a 0.4 mm nozzle) make it about 7.5 mm wide. Teardrop or airfoil shape,
    rounded nose into the wind, about 20–25 mm long in the flow direction. Height: from the floor to about 5 mm
    below the ball (about 35 mm for the 3/4 in ball centred 50 mm up).
  - Its frontal area, about 7.5 × 35 mm, blocks about 2.6 % of the section, nearly as much as the 3/4 in ball (2.85 %).
    It is in place when the probe is calibrated, so its effect on the speed at the ball is included, but keep it as
    slim as the printer allows. A thinner sting would allow a thinner shield, at a large cost in stiffness (stiffness
    goes with diameter⁴).
- **What the load cell can resolve:**
  - Its errors are all given as % of full scale: 0.05 g for the 100 g cell. That is 4 % of the drag at 13 m/s and
    17 % at 6.5 m/s if those figures held at our loads. Creep and hysteresis usually shrink with the load, so at
    gram loads they should be far smaller. That is not specified, so the calibration (build step 5) measures it at
    0.2–3 g.
  - The zero drifts ±0.01 g per °C whatever the load. That is 0.8 % of the drag per °C at 13 m/s and 3.4 % at
    6.5 m/s, hence a wind-off zero before and after every run, and a closed load-cell box away from the fan motor.
  - The HX711's own noise is far below all this, about 0.002 g per sample ([HX711 notes](../resources/notes/HX711.md)).
  - A smaller cell with a datasheet was not found among cheap parts; 100 g is the smallest TAL221.
- **Overload:** the safe limit is 150 g, and a finger pushing a ball onto the sting can exceed it. Lock the sting
  before every model swap. The spare cell (owner chose two, 2026-11-08) means a broken cell costs an afternoon, not a
  week.
- **Keeping the load cell safe** (proposed):
  - Lock the sting before touching the ball, the sting or the shield. Unlock only to run.
  - Set the overload stops with a known mass so they catch the sting at about 120 g, below the 150 g safe limit.
  - Hold and clamp the cell only by its two end blocks, never the thin middle. Do not over-tighten the M3 screws in its
    aluminium threads, and use screws short enough not to reach the middle.
  - Tie the thin wires down near the cell so a tug pulls on the tie, not on the cell. Keep the soldering iron away
    from the cell body.
  - Calibration masses stay below 100 g. Keep the spare cell in its bag, in a box.
- **Knowing whether it is damaged:** record three baselines when each cell arrives, and compare with them after any
  knock (owner tasks; physical checks):
  1. **Wire resistances** with the multimeter, cell disconnected. Datasheet: red–black 1090 ± 10 Ω and green–white
     1000 ± 10 Ω. Also record the four cross pairs (red–green, red–white, black–green, black–white); in a healthy bridge
     they come in two near-equal pairs (our understanding of a standard bridge, not stated in the datasheet). A
     snapped wire or broken gauge shows as "OL" (open) or a value far off. Any wire to the metal body: OL.
  2. **The zero:** the raw HX711 reading with nothing loaded, after a few minutes' warm-up, written in the log. Bending
     the bar past its limit leaves a permanent shift much larger than the normal drift of about 0.01 g per °C.
  3. **A known small mass** (for example 2 g, hung in the drag direction): it must read the same as at calibration.
  If the zero has jumped, or the known mass reads differently, recalibrate. If the calibration then shows the reading
  not returning to zero after unloading, or creeping under a steady load, the cell is damaged: fit the spare.
- **Drilling each ball to its centre (owner's idea: a printed jig, 2026-11-08):**
  - A two-part printed clamshell: each half has a cup that fits the ball with about 0.2 mm clearance; two M3 screws
    clamp the halves. The top half has a guide hole straight down through the ball's centre.
  - Press a short piece of brass tube into the guide hole as a bushing (a drill bit chews a plastic hole and starts to
    wobble), and make the guide at least 3 bit diameters long so the bit cannot tilt.
  - Drill to about the ball's radius (9.5 mm for 3/4 in, 12.7 mm for 1 in); a tape flag on the bit marks the depth. A
    drill press is best; a hand drill works with the long guide. Go slowly and back out often to clear the chips.
  - Needed accuracy is modest: about 0.5 mm off-centre changes nothing measurable. A tilted hole matters more, because
    it tilts the sting where it meets the ball. Check by spinning the finished ball on its stem and watching for
    wobble.
  - Try it on a spare ball first: that is what the spares are for.
- **Fixing the ball on its stem:** acetal (Delrin) is one of the hardest plastics to glue; ordinary epoxy and super
  glue let go. Use a press fit: drill slightly smaller than the 1/8 in (3.18 mm) stem, for example 3.1 mm, and press the
  stem in. Find the right drill size on the spare ball. (Some special adhesives with primers do bond acetal; not
  needed with a press fit.)
- **Stems and socket (proposed):** each ball keeps its own short 1/8 in brass stem. The top of the sting is a short
  5/32 in brass sleeve, and the stem slides into it, held by friction or a small set screw. Balls are swapped with the
  sting locked, without twisting or pushing on the load cell. Design at sizing.
- **Why not a bigger cell for safety:** a 1 kg TAL221 would survive more abuse, but its errors, given as % of full
  scale, would be 10 times larger in grams (0.5 g against a 0.3–2.3 g drag), and the HX711 noise about 6 times larger
  ([HX711 notes](../resources/notes/HX711.md)). Protect the 100 g cell with the lock instead.
- **Sphere sizes:** 3/4 in (2.85 % blockage; 0.30–1.27 gf at 6.5–13 m/s) and 1 in (5.07 %; 0.54–2.31 gf). These
  replace the proposed 20 and 25 mm because inch balls are easier to buy in the US. The Re-matched pair for the
  two-size check (D-009): the 3/4 in sphere at 13 m/s matches the 1 in sphere at 9.75 m/s. The 1 in ball weighs about
  12 g; its weight acts along the upright load cell, not in the measured direction.
- Order the load cell and HX711 from SparkFun together, or with the SDP810 if a distributor carries all three, to
  share shipping.

## 7. Ambient conditions (proposed 2026-11-08)

| Item | What to buy | Qty | Price seen | Where | When | Status |
|---|---|---|---|---|---|---|
| Ambient sensor | **Adafruit BME280 breakout (product 2652)**: pressure, temperature and humidity, with a 3.3 V regulator and level shifting, so it works on the 5 V Mega | 1 | $14.95 (Adafruit listing) | Adafruit, DigiKey, Mouser | Now | To buy |

What it is for:

- **Air density,** ρ = p/(R·T), for the airspeed V = √(2q/ρ) and the Reynolds number that picks the reference C_D
  (D-009). C_D itself does not need ρ, because q is measured directly.
- **The SDP810 ambient-pressure correction**: Δp × 966 mbar / p_amb, on every reading (§5).

Notes:

- **Accuracy is not a worry.** Vendor pages give about ±1 hPa, which is 0.1 % in ρ and in the SDP810 correction.
  Humidity changes ρ by under about 1 %, so even a BMP280 (no humidity) would do. The Adafruit board is chosen for its
  5 V level shifting and because it is genuine.
- **Fake modules:** cheap "BME280" boards are often BMP280 chips. Check on arrival: chip-ID register 0xD0 reads 0x60
  for a BME280 and 0x58 for a BMP280. Then breathe on it (humidity should jump) and warm it with a finger
  (temperature should rise): a test must show a change you caused.
- **Placement:** in room air near the fan inlet, on a short cable, away from the Arduino, the display and the fan
  motor, whose heat would make it read warm.
- **I²C address:** 0x76 or 0x77; no clash with the SDP810 (0x25).

## 8. Electronics, controls and wiring (reviewed 2026-11-08)

**No display or knob ([D-012](../DECISIONS.md), owner, 2026-11-08):** all output goes to the laptop over USB. The
Arduino IDE's Serial Plotter gives a live graph to start with. The two display options below are kept for the
record.

On hand: the Elegoo Mega 2560 (working) and a USB A-to-B cable; the ECE kit, with a breadboard, a jumper-wire kit
(male ends, for the breadboard), a wire stripper, and resistors and capacitors for I²C pull-ups and decoupling.

| Item | What to buy | Qty | Price seen | Where | When | Status |
|---|---|---|---|---|---|---|
| Display and knob, option A | "Full Graphic Smart Controller" 12864: a 128×64 graphic LCD, push-button rotary encoder, buzzer and SD-card slot on one board | | about $15–24 new (several listings, undated) | | | Not needed (D-012) |
| Display and knob, option B | A 20×4 character LCD with an I²C backpack (PCF8574), plus a KY-040 push-button rotary encoder | | about $12–15 together (typical, not checked) | | | Not needed (D-012) |
| Dupont jumper wires | Female-to-male and female-to-female, about 20 cm: modules and the display adapter to the Mega's header pins while developing | 1 pack each | about $5–8 (typical, not checked) | Amazon, electronics shops | Now | To buy |
| Mega prototyping shield | A perfboard shield that plugs onto the Mega, as a soldered in-between board | | about $5–10 (typical, not checked) | | | **Not needed:** the owner's plan is breadboard → test → PCB (2026-11-09) |
| Header strips | Male and female, 0.1 in pitch | 1 assortment | about $5 (typical, not checked) | Same | Now | To buy |
| Sensor cables | 4-core cable, shielded if available, about 3 m in all: HX711 (in the load-cell box) to the control box, SDP810 to the control box, BME280 to the control box. Keep each I²C run under about 1 m | about 3 m | about $5–10 (typical, not checked) | Hardware or electronics shop | Now | To buy |
| Hook-up wire | Stranded 24–26 AWG in several colours (and 22 AWG solid for the breadboard) | 1 set | about $10–15 (typical, not checked) | Same | Now | Unknown (may be on hand) |
| Heat-shrink tubing | Assortment | 1 | about $5–8 (typical, not checked) | Same | Now | Unknown |
| Solder supplies | Rosin-core solder 0.6–0.8 mm, flux, desoldering wick | | | | Now | Unknown (the soldering station is on hand) |
| Enclosures | An Arduino box and the load-cell box (cell and HX711 only) | 2 | filament | Printed | After sizing | Printed |

**Subtotal:** about $15–23 to buy, plus about $20–30 if the hook-up wire, heat-shrink and solder are not on hand.

**Circuit plan (owner, 2026-11-09):** when the parts arrive, build the circuit on the ECE kit's breadboard, test it,
then order the PCB (§11). The breadboard carries only digital and I²C lines: the load cell's bridge wires are soldered
straight to the HX711 in the load-cell box (Weakly2024 lesson).

Notes:

- **Where things go:** the HX711 sits in the load-cell box, with the cell's wires soldered straight to it, and only its
  four digital wires run to the Arduino's box. The Arduino sits apart from the balance, so handling it does not shake
  the load cell and its heat does not warm it.
- **I²C over cables:** keep runs short, run the bus at 100 kHz, and put the pull-up resistors on the interface shield
  (values chosen at the circuit design, P2).
- **The laptop log over USB is the data record** and, with D-012, also the live view.
- **The Arduino never switches mains.** Fan speed stays on the fan's own controller.

## 9. Calibration (proposed 2026-11-08)

Two calibrations, both owner tasks with the hardware in hand: the load cell against known masses (build step 5), and
the pressure sensor's 3 % gain error against a water manometer (§5).

| Item | What to buy | Qty | Price seen | Where | When | Status |
|---|---|---|---|---|---|---|
| Calibration masses | A budget 17-piece set, 10 mg to 100 g, with tweezers. Sellers claim ±0.003 g; not certified | 1 | about $20–40 (listings, 2026-11-08) | Amazon, scale shops | Now | To buy |
| Thread and hook | Fine nylon thread or light fishing line, and a light hook (bent fine wire or printed) to hang masses at the ball's position | | a few dollars | | Now | Unknown (probably in the house) |
| Manometer tubing | Clear vinyl tubing, 1/4 in (6.4 mm) inside diameter, about 2 m, for a U-tube lying on a sloped ramp | 1 | about $5–10 (typical, not checked) | Hardware store | Now | To buy |
| Manometer fittings | Barbed reducers from 1/4 in to 1/8 in (2) to join the manometer to the 1/8 in pressure lines; one more 1/8 in tee (from the §5 assortment) | 2 | about $3–6 (typical, not checked) | Same | Now | To buy |
| Manometer ramp | A long, straight, rigid ramp at about 1 in 10, with the tubing taped flat along it and the steel rule (§10) beside it | 1 | filament or scrap wood | Printed or wood | Later | Printed |
| Spirit level | A small level, for the manometer ramp's base and for the tunnel and balance | | | | | On hand (owner, 2026-11-08) |
| Lab balance | A school lab analytical balance, used once to weigh every calibration piece | | | | | Access available (owner, 2026-11-08) |
| Water, food colouring, dish soap | A drop of colouring makes the water visible; a drop of soap makes the meniscus even | | | | | Probably in the house |

**Subtotal:** about $28–56 (weights, tubing, fittings), less whatever is already in the house.

Notes:

- **Lab-certified weight sets are out of reach:** about $500–2,700 for OIML class F1 sets (Rice Lake listings).
- **Using the budget set so its errors do not matter:**
  - Set the load cell's slope with the larger pieces (2–20 g), where a 3 mg error is 0.15 % or less.
  - Check the low end with the 200 mg–1 g pieces, and check the pieces against each other: on the load cell, the 1 g
    piece must read the same as 500 + 200 + 200 + 100 mg. A bad piece shows up as a mismatch.
  - The 10–50 mg pieces only show the resolution. One buyer found 20 mg pieces reading 23–24 mg.
  - **The owner can use a school lab balance (2026-11-08).** Weigh every piece once and record the true masses,
    with the balance's model, its readability and the date. The cheap set then becomes an accurate one. Those
    readings are calibration data: they go in `data/raw/` with a data-catalog entry, like any measurement.
- **Loading in the drag direction, with no pulley:** a pulley's friction is unknown and could be a large part of a 1 g
  load. Instead, design the balance (load cell, base and sting) as a module that comes out of the tunnel. Lay it on
  its side so gravity pulls along the drag direction (the load cell is then flat, the way it sits in a kitchen scale)
  and hang the masses from the ball's position. A pulley check in the tunnel can follow as a cross-check.
- **Not suitable: Dwyer's Mark II 25 manometer** ($57–86): ±3 % of a 0–3 inH₂O (0–747 Pa) range is ±22 Pa, far coarser
  than the 25–100 Pa being checked.
- **The home-made inclined manometer** (proposed): a water-filled U-tube lying flat on a ramp at about 1 in 10.
  - The pressure difference is Δp = ρ_water · g · Δs · sin θ, where Δs is the distance between the two water surfaces
    measured along the tube and sin θ = rise / run of the ramp.
  - At 1 in 10, 100 Pa moves the surfaces about 102 mm apart, against only 10 mm in a vertical U-tube. Reading each
    surface to about 0.5 mm, and the ramp's rise and run on a long base, gives roughly 1 % at 100 Pa (our estimate).
  - Both surfaces are in the same tube, so capillary rise cancels.
  - Calibrate near the top of the range (80–100 Pa), with the manometer and the sensor teed onto the same pair of taps
    and the tunnel running steadily. The sensor's 3 % error is a gain error, so fixing it at the top fixes it
    everywhere. Its zero (0.08 Pa) is checked with the wind off.
  - Use the water's density at its measured temperature (about 998 kg/m³ at 20 °C).

## 10. Tools and consumables (partly reviewed 2026-11-08)

On hand: multimeter, soldering station, bench power supply, workbench, the P1S printer. Unknown: drill bits, hex keys,
zip ties, tape. Needed for the wall pressure taps (§5): a pin vise with micro drill bits of about 0.8–1.0 mm.

| Item | What to buy | Qty | Price seen | Where | When | Status |
|---|---|---|---|---|---|---|
| Digital calipers | none: the owner has a pair, **6 in (150 mm) range** (2026-11-08). Model and accuracy not recorded | | | | | On hand (battery thought dead) |
| Steel rule or tape measure | For anything over 150 mm: the 250 mm settling chamber, the tunnel length, acrylic panels. A 300 mm (12 in) steel rule reads to about 0.5 mm | 1 | a few dollars (typical, not checked) | Hardware store | Now | Unknown (probably in the house) |
| Small tube cutter | A rotary cutter for small brass tube (for example K&S's): rolls a blade around the tube, giving a square end without crushing it. For the probe and the 12 tap stubs (§5) | 1 | about $8–12 (typical, not checked) | Hobby or hardware store | Now | To buy |
| Needle files or a deburring tool | To clean cut ends. The probe tip must be square and smooth; a burr inside a stub narrows it | 1 set | about $5–10 (typical, not checked) | Hardware store | Now | Unknown (may be in the house) |
| Junior hacksaw | For the solid brass sting rod (§6); the tube cutter is meant for tubes | 1 | about $5–10 (typical, not checked) | Hardware store | After sizing | Unknown (may be in the house) |
| Drill | A hand drill, for the balls' centre holes (§6), used with the printed jig's long guide | | | | | On hand (owner, 2026-11-08) |
| Tin snips | For cutting the stainless screen mesh (§3); old heavy scissors also work | 1 | about $10–15 (typical, not checked) | Hardware store | Now | Unknown (may be in the house) |
| Drill bits for the balls | About 3.0–3.1 mm (metric) for a press fit on the 1/8 in stems; settle the size on a spare ball | 1–2 | a few dollars each (typical, not checked) | Hardware store | After sizing | To buy |
| Caliper battery | A 1.55 V button cell, size 44: **SR44 (silver oxide; also sold as 357 or 303)** preferred, LR44 (alkaline; AG13, A76) also fits. Check the size printed on the old cell or in the battery cover first | 1–2 | a few dollars (typical, not checked) | Hardware store, pharmacy | Now | To buy, unless one is in the house |

Calipers notes:

- **Test the old cell with the multimeter before buying.** Our rule of thumb, not a datasheet figure: a fresh cell reads
  about 1.5–1.6 V, and below about 1.4 V calipers often flicker or jump.
- **Why SR44:** a silver-oxide cell holds its voltage nearly flat until it is empty. An alkaline LR44 sags gradually,
  and cheap calipers can read erratically as it does.
- **Cheap calipers often drain the cell even when switched "off"** (the button only blanks the display). If a new cell
  dies within weeks, take it out between uses.
- **Check the calipers once they work**, following the lesson that a test must show a change you caused. Close the
  jaws and zero; open, close and confirm it returns to 0.00; then measure something of known size, such as a drill
  bit's shank or a bearing ball, and record the error. A 0.03 mm error on a 20 mm sphere is 0.3 % in C_D, because area
  goes with d².
- **Range: 6 in (150 mm)** (owner, 2026-11-08). The things that need caliper accuracy are all well inside it: the
  20 mm and 25 mm spheres (D-009 depends on their diameter), the sting, pins, screws and test-print fits. Over 150 mm,
  use the steel rule, or one of these:
  - **The fan's outlet collar** (about 150 mm, at or past the limit): wrap a paper strip around it, mark the overlap,
    and divide its length by π. A 1 mm error in the strip's length is about 0.3 mm in diameter, plenty for this
    joint.
  - **Big printed parts:** design the critical fits (pins, collars, panel lips) as small features and measure those,
    or print a short test ring first.

## 11. Later and optional (reviewed 2026-11-09; nothing to buy now)

| Item | What it is | When | Status |
|---|---|---|---|
| Interface PCB | The owner's own board (P2), ordered from a PCB service after the breadboard test. Plug-in parts: **female header sockets** for the modules (HX711, BME280) and a connector for the SDP810's cable, so any module can be swapped without soldering; **DIP sockets** for any chips such as op-amps, if used (owner's idea, 2026-11-09). Price when designed | After the breadboard test | Later |
| Header sockets and DIP sockets | For the PCB: female 0.1 in headers (the §8 header strips) and DIP sockets if chips are used | With the PCB | Later; about $5 (typical, not checked) |
| Second HX711 | For a lift (vertical) load cell; the spare TAL221 (§6) can become that cell. $11.50 (SparkFun) | Only if lift is measured; the owner may skip it (2026-11-09) | Later |
| Floor plug | A printed plug to close the sting hole when no force is being measured | With the car tests | Printed |
| Mist maker | An ultrasonic mist maker for flow visualization (TODO P2, the agent's first choice); price not checked | Last (owner, 2026-10-31 and 2026-11-09) | Later, optional |
| Airfoil and preset-angle hub | Printed | P3 | Printed |
| Tufts | Short pieces of yarn taped to a model to show stall | P3 | Probably in the house |

**Owner's plan for model cars (2026-11-09):** if lift or downforce is not measured, close the sting hole with the
floor plug, set a model car on the floor, and watch the flow with mist: a visual study, not a force measurement. This
simplifies the 2026-11-02 downforce idea (TODO P3), which needed a second, vertical load cell.

**Considered and not bought:**

- **A golf ball** (owner asked, 2026-11-08). At 42.7 mm it would block 14.3 % of the 100 mm section; the blockage
  correction holds to about 5 % and fails past about 8.5 %. Its dimple-driven drag drop also needs a higher Reynolds
  number than this tunnel reaches: 3.7×10⁴ at 13 m/s, against roughly 4–10×10⁴ for the drop (agent's recollection;
  not checked against a source). It would need a section of about 170–200 mm at about 18–25 m/s, so it belongs to a
  possible follow-up tunnel.
