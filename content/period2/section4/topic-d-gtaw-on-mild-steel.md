---
id: p2-s4-d
period: 2
section: 4
section_title: Gas Tungsten Arc Welding (GTAW)
topic_letter: D
topic_title: GTAW on Mild Steel
hours: 30
weight_pct: 12
outcome: >
  Upon successful completion, learners will be able to perform GTAW on mild steel
  in flat, horizontal, vertical positions on plate and pipe (2G, 5G positions).
objectives:
  - Perform touch start, lift start and high frequency (HF) methods to initiate the arc.
  - Perform stringer beads in the flat position on mild steel gauge plate.
  - Perform joint preparation for GTAW on mild steel gauge plate.
  - Perform 1F, 2F, 3F welds on mild steel gauge plate.
  - Perform 1G, 2G, 3G welds on plate and 2G, 5G welds on pipe.
red_seal_mapping:
  - D-15.02 (Sets up GTAW equipment)
  - D-15.03 (Sets operating parameters for GTAW)
  - D-15.04 (Performs weld using GTAW equipment)
citations:
  - source: Miller Electric — Guidelines for Gas Tungsten Arc Welding (GTAW)
    ref: DC vs AC selection, amperage tables, technique
    url: https://www.millerwelds.com/resources/article-library/gas-tungsten-arc-welding-gtaw-guidelines
  - source: Lincoln Electric — TIG Handbook / Procedure Handbook of Arc Welding
    ref: Torch angle, filler dip technique, pipe welding positions
    url: https://www.lincolnelectric.com/en/education-center/welding-education/procedure-handbook
  - source: AWS A5.18 — Carbon Steel Electrodes and Rods for Gas Shielded Arc Welding
    ref: ER70S-2, ER70S-6 classifications for GTAW filler on mild steel
    url: https://pubs.aws.org/p/1141/a518a518m2005-specification-for-carbon-steel-electrodes-and-rods-for-gas-shielded-arc-welding
  - source: AWS A5.12 — Specification for Tungsten and Oxide Dispersed Tungsten Electrodes for Arc Welding and Cutting
    ref: EWTh-2 (thoriated), EWCe-2 (ceriated), EWLa-1.5 (lanthanated) selection and prep
    url: https://pubs.aws.org/p/1046/a512a512m2009-specification-for-tungsten-and-oxide-dispersed-tungsten-electrodes-for-arc-welding-and-cutting
  - source: CSA W59 — Welded Steel Construction (2018)
    ref: Clause 12 welder qualification positions (1G-6G plate/pipe)
    url: https://www.csagroup.org/store/product/CSA%20W59%3A18/
  - source: AIT Welder Curriculum Guide 012 (2026), Period 2 Section 4 Topic D
    ref: pp. 27-29
    url: https://tradesecrets.alberta.ca/SOURCES/PDFS/CURRICULUM_GUIDES/012_OUTLINE.PDF
---

# GTAW on Mild Steel

GTAW (TIG) on mild steel isn't the fastest process, and no one runs production mild steel with it in a shop that has GMAW available. But **every good welder can TIG mild steel** — because pipe root passes, thin sheet metal work, code repairs, and any weld that needs to look surgical all live here. Master it on plate first; then the same fundamentals let you run 2G/5G roots on pipe that pass X-ray.

---

## Setup: polarity, gas, tungsten, filler

For mild steel GTAW, the choices are simple:[^1]

| Setting | Value | Why |
|---|---|---|
| **Polarity** | DCEN (Direct Current Electrode Negative / "straight polarity") | 2/3 of the heat goes into the workpiece, 1/3 into the tungsten. Deep penetration, tungsten stays sharp. |
| **Shielding gas** | 100% argon | Standard for DC GTAW on carbon steel. Cheap, stable arc, excellent coverage. |
| **Gas flow rate** | 15-25 CFH (7-12 L/min) | Enough for full coverage without turbulence. Higher = wasted gas + risk of aspiration. |
| **Cup size** | #7 (7/16") for typical work | Larger cups (#8, #10) improve shielding but need more gas |
| **Tungsten** | 2% ceriated (grey) or 2% thoriated (red), 3/32" for most plate work | Ceriated is now preferred (non-radioactive alternative to thoriated with equal performance) |
| **Tungsten prep** | Grind to a POINT (2-2.5× diameter length), grind marks LENGTHWISE (parallel to electrode axis) | Cross-hatched grind marks cause arc wander |
| **Filler rod** | ER70S-2 (deoxidized, best for rusty/dirty) or ER70S-6 (highest deoxidizers, most tolerant) | 1/16" filler for 1/8" plate; 3/32" filler for 3/16"–1/4" |

---

## Arc initiation — three ways, know when to use each

1. **High-Frequency (HF) start** — the machine sends a high-voltage, high-frequency spark that jumps the gap between tungsten and workpiece without contact. Preferred for all production work. No tungsten contamination.[^1]
2. **Lift-arc start** — touch tungsten to workpiece with pedal down, then lift. Machine detects the lift and starts the arc without HF. Cleaner than scratch start, works in areas where HF could interfere with electronics (inverters near pacemakers, PLCs, sensitive equipment).[^1]
3. **Scratch start** — touch tungsten to work and drag like a match. Contaminates the tungsten (bit of steel welded to the tip). Only for old transformer machines with no HF. Avoid.[^2]

**On production mild steel, HF start is standard. Learn lift-arc as backup.**

---

## Amperage — the golden rule

**Rule of thumb: 1 amp per 0.001" of material thickness** for mild steel DC GTAW.[^1]

| Material thickness | Approximate amperage |
|---|---|
| 1/16" (0.062") | 60-80 A |
| 3/32" (0.093") | 90-110 A |
| 1/8" (0.125") | 110-130 A |
| 3/16" (0.187") | 140-170 A |
| 1/4" (0.250") | 170-220 A |

**Adjust for position:** vertical up → reduce ~10-15%. Overhead → reduce ~15-20%. Pipe root passes → depends on gap and land, typically 80-110 A for a 1/8" root gap.

**Foot pedal control matters.** You'll ramp up amperage at the start to establish the puddle, then modulate as you travel (add filler → puddle cools → add more heat). A foot pedal (or torch-mounted amperage control) is essential for real GTAW work.

---

## Torch and filler technique

For a stringer bead, flat position, right-handed welder:[^2]

- **Torch angle:** 10-15° push (leading angle — opposite of stick and FCAW). Tungsten pointed slightly ahead of travel direction.
- **Work angle:** 90° for bead-on-plate, 45° for fillet
- **Arc length:** approximately 1× tungsten diameter (3/32" tungsten → 3/32" arc). Short arc = cleaner weld, more heat concentration.
- **Filler angle:** 15-20° from workpiece surface, approaching the leading edge of the puddle from the front
- **Filler dip:** dip filler into the LEADING edge of the puddle (not the arc — never touch the tungsten with the filler). Withdraw after each dip but keep the hot end inside the gas shield to prevent oxidation.
- **Travel speed:** slow. Watch the puddle. When it flows to the intended width, dip, then advance ~1 puddle width and repeat.

**Left hand does the filler dance, right hand holds the torch steady.** This is why GTAW takes months to master — it's two-handed coordination.

---

## Positions on plate: 1F, 2F, 3F fillet — and 1G, 2G, 3G groove

| Position | AWS designation | Technique notes |
|---|---|---|
| Flat fillet | 1F | Torch tilted into the joint corner ~45°, slight push angle |
| Horizontal fillet | 2F | Torch aimed slightly upward (5-10°) to counter puddle sag |
| Vertical up fillet | 3F | REDUCE amperage 10-15%. Slow travel. Slight weave at wide gap, stringer at tight fit-up. |
| Flat groove | 1G | Root pass with keyhole technique OR open root with backing; fill/cap standard technique |
| Horizontal groove | 2G | Push angle slightly upward on the top bevel; multiple stringer beads (do NOT weave — puddle drops out) |
| Vertical up groove | 3G | Slight side-to-side weave with pause at toes to prevent undercut |

---

## Pipe: 2G and 5G positions

Pipe positions are where GTAW becomes essential — root passes on carbon steel pipe (especially in refinery, pipeline, and pressure vessel work) are TIG territory.[^5]

| Position | Description | Technique |
|---|---|---|
| **2G** | Pipe axis vertical, weld horizontal (like a belt around a standing post) | Rotate the pipe if possible (2G-R). If fixed, run stringer beads uphill on the top half of the joint, then continue on the bottom. |
| **5G** | Pipe axis horizontal, pipe fixed (weld runs around the fixed pipe) | Uphill from 6 o'clock to 12 o'clock on each side. Bottom (6 o'clock) is where fusion is toughest — slow down, tilt torch slightly toward the puddle. |

**Root pass on pipe** — the definitive GTAW skill:
- **Open root, no backing:** typical root gap 3/32" (2.4 mm), land 1/16" (1.6 mm) or feather to zero, 60° included angle bevel
- **Filler technique:** ER70S-2 filler, walk-the-cup or free-hand
- **Purge:** for high-quality work, back-purge the pipe with argon (5-10 minutes flush before starting, then 5-10 CFH maintain during root)
- **Look for the "keyhole":** the arc melts through the root faces creating a small keyhole in the joint. You dip filler into the trailing edge, keeping the keyhole open. Lose the keyhole = incomplete penetration.

---

## Joint preparation — cleanliness is everything

GTAW is completely intolerant of surface contamination. Before you strike an arc:[^2]

1. **Grind mill scale off both sides of the joint** (2" back from weld area minimum)
2. **Wire brush with a CLEAN stainless-steel brush** (dedicated to mild steel — never use one that's been on aluminum or stainless)
3. **Wipe with acetone or lacquer thinner** to remove oil/cutting fluid
4. **Bevel prep:** 30° per side (60° included) for open root; 37.5° per side (75° included) for pipe root
5. **Land / root face:** 0 to 1/16" (feathered or slight land depending on skill and pipe size)
6. **Root gap:** typically 3/32" (2.4 mm) for pipe root with 3/32" ER70S-2 filler

**Any oil, rust, paint, or mill scale left in the joint will cause porosity. Every time.**

---

## Numbers you need to memorize

- **Polarity for GTAW on mild steel:** DCEN[^1]
- **Shielding gas:** 100% argon[^1]
- **Gas flow rate:** 15-25 CFH (7-12 L/min)[^1]
- **Tungsten choice:** 2% ceriated (grey) or 2% thoriated (red), pointed[^4]
- **Tungsten point length:** 2 to 2.5× tungsten diameter[^4]
- **Amperage rule:** ~1 A per 0.001" of material thickness[^1]
- **Arc length:** ≈ 1× tungsten diameter[^2]
- **Filler ER70S-2:** best for dirty/rusty; ER70S-6 = most tolerant with highest Mn/Si deoxidizers[^3]
- **Cup size #7:** 7/16" ID — standard for plate work[^1]
- **Pipe root gap:** typically 3/32" (2.4 mm) with 3/32" filler[^5]
- **Pipe bevel:** 37.5° per side = 75° included angle for pipe; 30° per side = 60° included for plate[^5]
- **Back-purge argon flow:** 5-10 CFH maintained during root pass[^2]
- **Vertical up amperage reduction:** 10-15% below flat setting[^1]
- **Torch angle for push technique:** 10-15° leading[^2]

---

## What the textbook doesn't tell you

**Never touch the tungsten to the puddle or the filler.** The instant it happens: kill the pedal, back off, cut the tungsten below the contamination (or regrind), and restart. Trying to weld through a contaminated tungsten wastes the whole coupon.[^4]

**Grind marks matter.** When you sharpen the tungsten on a bench grinder, the grind marks MUST run lengthwise (parallel to the axis of the electrode). Circumferential grind marks (grinding perpendicular to the axis) create arc wander — the arc jumps between the ridges. Use a dedicated tungsten grinder or a fine wheel with lengthwise strokes.[^4]

**On mild steel with 100% argon, you can see the puddle clearly.** Don't try to weld like you would GMAW. The puddle looks like a shiny mercury pool. Add filler when the puddle spreads to your desired bead width, not before.[^2]

**Filler rod dipping is a rhythm.** Beginners tap the filler into the arc; that's wrong. **Dip, count 1-2, dip, count 1-2.** The puddle needs time to absorb heat before you feed it filler. Rush the dips = cold fusion.[^2]

**Foot pedals aren't just on/off.** Use the pedal to modulate heat as you weld. When you dip filler, ease off the pedal briefly (the puddle grows and you don't want it to sag). When you're between dips, ease back on. Real GTAW welders are constantly working the pedal.[^1]

**Back-purging matters more than you think.** On code work (pipe, pressure vessels), missing back-purge = sugared/oxidized root that fails inspection. Cheap purge dam kits (paper + water-soluble tape) are worth it if you can't purge the whole pipe. Argon is denser than air — flush from the bottom, vent from the top.[^2]

**Pipe root walk-the-cup vs free-hand.** Walk-the-cup (rest the ceramic cup on both sides of the bevel and "walk" it around the pipe) gives you consistent arc length and travel speed on 3" pipe and up. Free-hand is faster and more flexible but requires steady hands. Learn both; every code shop expects them.[^5]

**When you struggle on 5G pipe root:** 90% of failures are (1) too much amperage at 6 o'clock — burns through, (2) too little at 12 o'clock — lack of fusion, (3) losing the keyhole. Fix the amperage by working the pedal, fix the keyhole by slowing down when it starts to close.[^5]

---

## Diagram

*(SVG to be added: `assets/diagrams/p2-s4-d-gtaw-torch-technique.svg` — torch at 10-15° push angle, tungsten with proper 2× diameter point, filler rod entering leading edge of puddle at 15-20°, arc length shown = 1× tungsten diameter)*

*(SVG to be added: `assets/diagrams/p2-s4-d-pipe-positions.svg` — four pipe orientations showing 1G rolled, 2G vertical pipe, 5G fixed horizontal, 6G at 45°, with weld progression arrows)*

*(SVG to be added: `assets/diagrams/p2-s4-d-pipe-joint-prep.svg` — cross-section of pipe root prep showing 75° included angle bevel, 1/16" land, 3/32" root gap, with filler rod entering)*

---

## Key terms

- **DCEN:** Direct Current Electrode Negative (straight polarity) — standard for GTAW on mild steel
- **HF start:** High-Frequency arc initiation — no tungsten contact
- **Lift-arc start:** touch and lift arc initiation — clean, no HF interference
- **Keyhole:** open molten pool at the root of an open-root pipe weld
- **Back-purge:** flowing inert gas inside a closed pipe to protect the underside of the root weld
- **Walk-the-cup:** technique of resting the ceramic cup on the bevel walls and walking it around the joint
- **Free-hand:** GTAW without cup contact — steady hand technique
- **1G-6G:** groove weld position designations (1G=flat, 6G=45° fixed pipe)
- **Land / root face:** the flat portion of a beveled edge at the root of the joint
- **Sugaring:** severe oxidation of the underside of a root weld (looks like sugar crystals) — caused by missing back-purge

---

## Common exam trap

- **GTAW polarity on mild steel is DCEN, NOT DCEP.** GMAW and FCAW-G use DCEP, GTAW uses DCEN. Distractors love to reverse them.
- **Tungsten grind marks must run LENGTHWISE (parallel to axis), not perpendicular.**
- **Never touch the tungsten to the filler or puddle** — contaminates the tungsten and the weld.
- **HF start does NOT touch the workpiece to initiate.** Lift-arc requires touch-then-lift. Scratch start requires drag contact.
- **100% argon** is the shielding gas for DC GTAW on mild steel. Ar/CO2 mixes are for GMAW/FCAW; they will destroy the tungsten instantly on GTAW.
- **5G pipe means the pipe is HORIZONTAL and FIXED** (weld progresses around it). 2G means pipe VERTICAL and fixed with weld going horizontally around it.
- **Cup #7 = 7/16" opening.** Cup number = 1/16" increments.
- **Vertical up amperage:** REDUCE 10-15% from flat setting (same rule as SMAW and FCAW).

---

## Practice question preview

**Q:** A welder is preparing to run a 5G root pass on 6" schedule 80 mild steel pipe using GTAW. The pipe has been beveled to a 75° included angle with a 1/16" land. The welder has selected 3/32" ER70S-2 filler and 3/32" ceriated tungsten. Which of the following is the MOST appropriate root gap for this joint?

A) 0" (tight fit, no gap)
B) 3/32" (2.4 mm)
C) 3/16" (4.8 mm)
D) 1/4" (6.4 mm)

**Correct: B**

**Explanation:** For a GTAW open-root pipe joint on mild steel, the standard root gap matches the filler rod diameter — 3/32" filler = 3/32" gap. This gap allows the keyhole to form and progress consistently as the welder feeds filler. A) A tight fit prevents the keyhole from forming and results in incomplete root penetration; C-D) Too wide a gap causes burn-through on the root pass and excess filler consumption. Land is separately specified (1/16" here), which controls the amount of material to melt through.

**Red Seal mapping:** D-15.03 (Sets operating parameters for GTAW), D-15.04 (Performs weld using GTAW equipment)

---

[^1]: [Miller Electric — Guidelines for Gas Tungsten Arc Welding (GTAW)](https://www.millerwelds.com/resources/article-library/gas-tungsten-arc-welding-gtaw-guidelines); DC selection, amperage/thickness rule, gas flow, foot pedal use
[^2]: [Lincoln Electric — Procedure Handbook of Arc Welding](https://www.lincolnelectric.com/en/education-center/welding-education/procedure-handbook), GTAW chapter — torch angles, filler technique, joint prep, cleanliness requirements
[^3]: [AWS A5.18 — Carbon Steel Electrodes and Rods for Gas Shielded Arc Welding](https://pubs.aws.org/p/1141/a518a518m2005-specification-for-carbon-steel-electrodes-and-rods-for-gas-shielded-arc-welding); ER70S-2 vs ER70S-6 chemistry differences
[^4]: [AWS A5.12 — Specification for Tungsten and Oxide Dispersed Tungsten Electrodes](https://pubs.aws.org/p/1046/a512a512m2009-specification-for-tungsten-and-oxide-dispersed-tungsten-electrodes-for-arc-welding-and-cutting); tungsten classifications (EWTh-2, EWCe-2, EWLa-1.5), preparation
[^5]: [CSA W59:18 — Welded Steel Construction](https://www.csagroup.org/store/product/CSA%20W59%3A18/), Clause 12 (welder qualification positions 1G-6G plate/pipe including 5G fixed pipe procedure requirements)
