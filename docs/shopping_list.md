# Shopping List

Nuh's tracker of what still has to be bought. Change the **Status** as you go: **To buy → Ordered → Got it**.
Other statuses: **Deciding**, **Maybe**, **Optional**, **Check house** (buy only if it isn't already at home).

Why each part was chosen, and the alternatives, are in [buy_list.md](buy_list.md). When something arrives, tell the
agent so it can mark it On hand there too.

**Last updated:** 2026-11-10. Prices were seen on listings on 2026-11-08/09. A **~** means a typical price that has not
been checked. Tax and shipping are not included. Prices paid are not recorded unless stated.

| | Rough cost |
|---|---|
| Fan | $53.90 (VEVOR) or $99.00 (S6); **bought last** (owner, 2026-11-10), once the airspeed readout works |
| Everything else marked To buy | nothing: **everything is ordered** (2026-11-09/10) |
| "Check house" items, if none are at home | up to about $65–100 more (solder not priced) |
| PLA | 4 kg black ordered; about $15–20 per kg if more is needed |

## Fan (still deciding; buy last)

| Item | Qty | Price | Link | Status |
|---|---|---|---|---|
| AC Infinity CLOUDLINE S6, model AI-CLS6 (about 13 m/s) | 1 | $99.00 | [AC Infinity](https://acinfinity.com/cloudline-s6-quiet-inline-fan-6-with-speed-controller/) | Deciding |
| *or* VEVOR 6" inline fan, model VV-GDFJ-AC6 (about 11.3 m/s) | 1 | $53.90 | your VEVOR listing (search the model number) | Deciding |

The agent recommends the S6 (2026-11-09): about 2 m/s faster, makers' figures more trustworthy, likely steadier at low
speed. The VEVOR still works if the $45 matters. Reasons and worst cases: [buy_list.md](buy_list.md) §1. **Timing
(owner, 2026-11-10):** buy it when the prints are ready, so the 30-day return window covers the real test (top speed
and load-cell noise with the fan running). Choose the model before the fan stand is designed.

## Electronics

| Item | Qty | Price | Link | Status |
|---|---|---|---|---|
| Sensirion SDP810-125Pa pressure sensor (Mouser 403-SDP810-125PA, DigiKey 1649-1073-ND) | 1 | $29–35 | [Mouser](https://www.mouser.com/c/?q=403-SDP810-125PA) | **Ordered** (2026-11-09, Mouser; part number confirmed on the order 2026-11-10) |
| TAL221 mini load cell, **100 g** (SparkFun SEN-14727) | 2 | $15.95 each | [SparkFun](https://www.sparkfun.com/mini-load-cell-100g-straight-bar-tal221.html) | **Ordered** (2026-11-09, SparkFun) |
| SparkFun HX711 load-cell amplifier (SEN-13879) | 1 | $11.50 | [SparkFun](https://www.sparkfun.com/sparkfun-load-cell-amplifier-hx711.html) | **Ordered** (2026-11-09, SparkFun) |
| **Waveshare BME280 Environmental Sensor** (instead of the Adafruit 2652). On arrival, before wiring SDA/SCL to the Mega: with only 5 V and GND connected, SDA and SCL read about 5 V; then chip ID 0x60 | 1 | | [Waveshare](https://www.waveshare.com/product/modules/sensors/bme280-environmental-sensor.htm) | **Ordered** (2026-11-09) |
| Dupont jumper wires, female-male and female-female, ~20 cm | 1 pack each | ~$5–8 each | [Amazon search](https://www.amazon.com/s?k=dupont+jumper+wires+female+male+20cm) | **Ordered** (2026-11-09) |
| Header strips, male + female, 0.1 in. **Not needed yet** (2026-11-10): male pins only make the HX711 neater on the breadboard (a cut Dupont jumper soldered to each pad does the same); the female ones are sockets for the PCB, so buy them with it. Buy **long breakaway strips: 1 × 40, single row, straight, 2.54 mm**. Male strips snap cleanly between pins; female strips lose one pin per cut (cut through a pin, then file the end). **Bought: 40 tin-plated strips** (gold not needed: no microvolt signal goes through a header; keep tin pins with tin sockets) | 40 strips | $10 | [Amazon search](https://www.amazon.com/s?k=male+female+header+strip+assortment+2.54mm) | **Ordered** (2026-11-10) |
| 4-core cable, shielded if possible. **Maybe not needed:** four colours of the TUOFENG hook-up wire twisted together with the hand drill do the same job | ~3 m | ~$5–10 | [Amazon search](https://www.amazon.com/s?k=4+conductor+shielded+cable+24awg) | Maybe |

## Hardware store

| Item | Qty | Price | Link | Status |
|---|---|---|---|---|
| Aluminium window screen: **Saint-Gobain ADFORS FCS9222-M, Bright**, 36 × 84 in (7 ft) roll; maker's spec 18 × 16 mesh, 0.011 in wire, so 66 % open. On arrival: count the wires per inch and check one wire is about 0.28 mm | 1 roll | about $10 | [Home Depot](https://www.homedepot.com/p/Saint-Gobain-ADFORS-36-in-x-84-in-Bright-Aluminum-Screen-Roll-for-Windows-and-Door-FCS9222-M/100397106) | **Ordered** (2026-11-09) |
| Foam weatherstrip tape, ~1/8 in thick, 1/4–3/8 in wide, adhesive-backed | 1 roll | ~$5–8 | | **Ordered** (reported 2026-11-10) |
| Silicone tubing, 1/8 in inside diameter | ~10 ft | ~$8–12 | | **Ordered** (reported 2026-11-10) |
| Barbed connectors for 1/8 in tubing. On arrival, count at least **10 tees** (9 for the tap stations, 1 for the manometer) and 2 straight couplers | 1 assortment | ~$6–10 | | **Ordered** (reported 2026-11-10) |
| Clear vinyl tubing, 1/4 in inside diameter (water manometer) | ~2 m | ~$5–10 | | **Ordered** (reported 2026-11-10) |
| Barbed reducers, 1/4 in to 1/8 in | 2 | ~$3–6 | | **Ordered** (reported 2026-11-10) |
| Rubber bumper feet: **a 20-pack of stick-on polyurethane feet, 0.78 × 0.38 in (about 20 × 10 mm)** (owner, 2026-11-09). Covers the fan stand (4) and the pads under the tunnel's printed feet (6–8), with spares | 1 pack of 20 | ~$5–10 | | **Ordered** (reported 2026-11-10) |
| Stainless M3 + M4 screw, nut and washer assortment (also used at the load cell) | 1 | ~$10–15 | | **Ordered** (reported 2026-11-09) |
| Brass M3 screws (for near the load cell) | 1 small set | ~$8–10 | | **Not needed** (2026-11-09): the panel magnets are too small and too far away to pull on stainless or even steel screws at the balance ([buy_list.md](buy_list.md) §4) |
| Drill bits: a **0.7–3.0 mm set** (owner, 2026-11-09). Covers the 0.8–1.0 mm taps and the 3.0 mm ball press fit. Buy a single 3.1 mm or #31 bit only if 3.0 mm proves too tight on a spare ball | 1 set | | | **Ordered** (reported 2026-11-10) |
| Pin vise (wall pressure taps) | 1 | not checked | | **Ordered** (reported 2026-11-10) |
| **LR44** button cell for the calipers (replace it first if the digits jump or drift) | 1–2 | a few $ | | **Ordered** (reported 2026-11-10) |
| Wet/dry sandpaper, **220–600 grit** (sand PLA wet) | 1 pack | ~$10–15 | | **Ordered** (reported 2026-11-10) |
| Acrylic scoring knife | 1 | ~$5–10 | | **Ordered** (reported 2026-11-10) |
| Cloth duct tape | 1 roll | ~$5–10 | | **Ordered** (reported 2026-11-10) |

## Hobby store / brass (K&S)

| Item | Qty | Price | Link | Status |
|---|---|---|---|---|
| K&S round brass tube, 1/8 in OD × 0.014 in wall × 12 in (No. 8127): probe and tap stubs | 2 | $1.79–6.29 each | [Amazon search](https://www.amazon.com/s?k=K%26S+8127+brass+tube+1%2F8) | **Ordered** (reported 2026-11-10) |
| K&S round brass tube, 5/32 in OD × 12 in: sting sleeve | 1 | ~$2–3 | | **Not needed** (2026-11-09): each ball gets its own full-length sting from the 1/8 in rod |
| Solid brass rod, **true 1/8 in (0.125 in, 3.18 mm)**, 12 in: one full-length sting per ball plus the calibration hook. Two rods make up to six stings of about 85 mm: the two balls, the hook, and spares | 2 | ~$1–3 each | | **Ordered: 2** (reported 2026-11-10) |
| Small tube cutter (for example K&S) | 1 | ~$8–12 | | **Ordered** (reported 2026-11-10) |
| Spring tube bender, 1/8 in (only the probe needs a bend; a lever bender only if it lists 1/8 in / 3.18 mm; free option: a printed bending jig with the tube sand-filled). Wait for sizing: the probe may need no bend | 1 | ~$5–8 | | Optional |

## Other online stores

| Item | Qty | Price | Link | Status |
|---|---|---|---|---|
| Neoprene sheet 40A, 1/16 in, no adhesive. **Bought: 2 sheets of 12 × 12 in** (owner, 2026-11-09/10). No single 480 mm strip fits, so wrap the fan collar with two ~240 mm pieces butted end to end, not overlapped | 2 | | | **Ordered** (reported 2026-11-10) |
| Clear cast acrylic, 1/8 in. **Bought: four 8 × 12 in sheets** (owner, 2026-11-10); each gives one window panel of about 300 × 120 mm | 4 | | | **Ordered** (reported 2026-11-10) |
| Delrin (acetal) balls, 3/4 in, ±0.001 in. Sold only in tens: the spares are for drilling practice and press-fit trials | 1 pack of 10 | ~$2.78 each (bulk price) | [McMaster](https://www.mcmaster.com/products/acetal-balls/) | **Ordered** (reported 2026-11-10) |
| Delrin (acetal) balls, 1 in, ±0.001 in. Sold only in tens | 1 pack of 10 | ~$4.42 each (bulk price) | [McMaster](https://www.mcmaster.com/products/acetal-balls/) | **Ordered** (reported 2026-11-10) |
| Brass M3 heat-set inserts. Send the agent their length and outside diameter: the printed holes are sized to them | 1 pack of 100 | $11–20 | | **Ordered** (reported 2026-11-10) |
| Calibration weight set, 10 mg–100 g, 17 pieces, with tweezers (hung in a light pan on a thread from the printed hook) | 1 | $20–40 | | **Ordered** (reported 2026-11-10) |

## Filament

| Item | Qty | Price | Link | Status |
|---|---|---|---|---|
| PLA, black | **4 kg** (the tunnel needs roughly 3–4 kg in all, a rough estimate firmed up at sizing; plus the spools on hand) | ~$15–20 per kg | [Bambu PLA Basic](https://us.store.bambulab.com/products/pla-basic-filament) | **Ordered** (reported 2026-11-10) |

The loaded parts (screen frames, sting mount, stops, load-cell base, drilling jig) are printed in the PETG-CF you
already have; they need roughly 0.5–1 kg (estimate). Weigh that spool too: buy plain PETG only if less than that is
left. Fit the hardened-steel nozzle before printing PETG-CF.

## Check the house first

| Item | Qty | Price | Link | Status |
|---|---|---|---|---|
| Power strip, UL or ETL listed, lighted on/off switch | 1 | $16–27 | | Check house |
| Clear silicone sealant | 1 tube | ~$6 | | Check house |
| Super glue and 5-minute epoxy | 1 each | ~$5–10 each | | Check house |
| Rubber pads under the tunnel's feet | 6–8 | | | Covered by the 20-pack of bumper feet (above) |
| Hook-up wire, **24 AWG stranded, silicone, about 6 colours**: TUOFENG, 6 colours × 30 ft, tinned copper. No solid wire needed: the ECE kit's jumpers cover the breadboard | 1 set | $15.79 | [Amazon search](https://www.amazon.com/s?k=TUOFENG+24+AWG+stranded+silicone+wire+6+colors) | **Ordered** (2026-11-09) |
| Heat-shrink tubing | 1 assortment | ~$5–8 | | Check house |
| Solder (0.6–0.8 mm rosin core), flux, desoldering wick | | not checked | | Check house |
| Steel rule, 300 mm / 12 in | 1 | a few $ | | Check house |
| Needle files or a deburring tool | 1 set | ~$5–10 | | Check house |
| Junior hacksaw | 1 | ~$5–10 | | Check house |
| Tin snips (old heavy scissors also work) | 1 | ~$10–15 | | Check house |
| Fine thread or fishing line, plus a small hook (calibration) | | a few $ | | Check house |
| Food colouring and dish soap (manometer) | | | | Check house |
| Coloured tape for labelling the tubes | | | | **Covered:** tape and Sharpies bought (reported 2026-11-10); write probe, M, S, E on tape flags |
| Sharpies: cut lines on acrylic and brass, magnet poles (one flipped magnet repels), tube labels | | | | **Ordered** (reported 2026-11-10) |
