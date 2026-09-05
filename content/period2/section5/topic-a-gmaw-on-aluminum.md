---
id: p2-s5-a
period: 2
section: 5
section_title: Gas Metal Arc Welding (GMAW), Flux-Cored Arc Welding (FCAW), Metal Cored Arc Welding (MCAW), and Submerged Arc Welding (SAW)
topic_letter: A
topic_title: GMAW on Aluminum
hours: 2
weight_pct: 1
outcome: >
  Upon successful completion, learners will be able to perform GMAW on aluminum
  gauge plate in flat and horizontal positions with correct equipment configuration.
objectives:
  - Perform stringer and weave beads in the flat and horizontal positions on aluminum.
  - Perform 1F, 2F, 3F fillet welds on aluminum plate.
  - Select appropriate spool gun or push-pull system for aluminum.
  - Identify aluminum-specific defects and troubleshooting.
red_seal_mapping:
  - D-14.01 (Selects FCAW, MCAW and GMAW gas, equipment and consumables)
  - D-14.02 (Sets up FCAW, MCAW and GMAW equipment)
  - D-14.03 (Sets operating parameters for FCAW, MCAW and GMAW)
  - D-14.04 (Performs weld using FCAW, MCAW and GMAW equipment)
citations:
  - source: Miller Electric — Aluminum GMAW / MIG Welding Guide
    ref: Spool gun vs push-pull, spray transfer parameters, aluminum-specific setup
    url: https://www.millerwelds.com/resources/article-library/mig-welding-aluminum
  - source: Lincoln Electric — Aluminum MIG Welding
    ref: Wire selection, drive rolls, gun length limitations
    url: https://www.lincolnelectric.com/en/education-center/welding-education/aluminum-mig-welding
  - source: AWS A5.10 — Bare Aluminum Welding Electrodes and Rods
    ref: ER4043, ER5356 wire classifications for GMAW
    url: https://pubs.aws.org/p/1039/a510a510m2017-specification-for-bare-aluminum-and-aluminum-alloy-welding-electrodes-and-rods
  - source: ESAB — Welding Handbook, Aluminum GMAW chapter
    ref: Push angle, transfer modes, gun cooling, drive roll requirements
    url: https://esab.com/us/nam_en/education/blog/aluminum-welding-guide/
  - source: AIT Welder Curriculum Guide 012 (2026), Period 2 Section 5 Topic A
    ref: p. 30
    url: https://tradesecrets.alberta.ca/SOURCES/PDFS/CURRICULUM_GUIDES/012_OUTLINE.PDF
---

# GMAW on Aluminum

GMAW on aluminum is faster than TIG by a factor of 5-10× for production work. It's used everywhere structural aluminum shows up: truck decks, boat hulls, trailer frames, ladder fabrication, aluminum tanks. But aluminum is soft and needs different equipment than steel — feed it wrong and you'll be picking bird's-nest wire out of the gun for the next hour.

---

## Why aluminum GMAW is different from steel GMAW

Three things you have to change from your steel GMAW setup:[^1][^2]

1. **Wire is soft** — aluminum wire crushes under normal drive-roll tension. Solutions: **spool gun** (short push distance) or **push-pull system** (dual drive).
2. **Wire is more conductive** — aluminum has 2× the electrical conductivity of steel. This causes higher wire feed heating → wire fuses to the contact tip if you don't watch amperage.
3. **Push angle, not drag** — you push the puddle forward on aluminum GMAW (opposite of steel drag). Push angle keeps the shielding gas ahead of the puddle and lets you see the joint.

---

## Feeding the wire — spool gun vs push-pull vs direct feed

This is the single biggest setup decision:[^1][^2]

| System | How it works | Best for | Cost |
|---|---|---|---|
| **Spool gun** | Wire spool mounted on the gun handle, drive motor 12" from arc | Small shops, thin aluminum, occasional aluminum work, 4 lb spools | Low |
| **Push-pull system** | Wire spool at machine, dual drive motors (one at feeder, one in gun) | Production work, longer gun cables (up to 25 ft), larger spools | Medium-High |
| **Direct feed** (short cable) | Standard wire feeder with special aluminum liner + soft drive rolls | Only OK for short cables (< 10 ft) with 0.045"+ wire | Free if you have it |

**For AIT training, expect spool gun.** In industry, push-pull for anything production.

**Never try aluminum on a standard steel GMAW gun with V-groove steel drive rolls.** The wire will bird's-nest in under 5 minutes.

---

## Drive rolls — critical for aluminum

Aluminum GMAW requires:[^2]
- **U-groove smooth drive rolls** (not V-groove, not knurled)
- **Reduced tension** — enough to feed, not enough to deform the wire (thumbnail-crush test: if you can dent the wire with your thumbnail, tension is too high)
- **Aluminum-specific gun liner** — Teflon (PTFE) or nylon liner, not the steel spring liner used for steel wire
- **Aluminum-specific contact tip** — slightly oversized (aluminum wire diameter varies more than steel; tight tip causes burnback)

Setting up steel gun with aluminum wire = frustration guaranteed.

---

## Filler wire — ER4043 vs ER5356 (same as GTAW)

Same rules as GTAW filler selection:[^3]

| Base metal | Wire selection |
|---|---|
| 6xxx-series (6061, 6063) | **ER4043** (5% Si) — smoother, easier |
| 5xxx-series (5052, 5086, 5083) | **ER5356** (5% Mg) — matches base, higher strength |
| Anodizing required | **ER5356** (ER4043 turns black) |
| Marine / structural | **ER5356** |
| Unknown / repair | **ER4043** (safer default) |

**Diameter:** 0.035" or 0.045" most common. Larger diameters (1/16") only with push-pull systems and heavier wire feeders.

---

## Shielding gas — argon, not CO2 mix

**100% argon** for aluminum GMAW.[^4]

**Argon-helium mix (25-75% He):** on thick material for extra heat, or high-production spray transfer. Expensive; use only when needed.

**NEVER use CO2 or Ar/CO2.** Carbon → aluminum carbide → cracks and brittleness.

**Flow rate:** 30-50 CFH (higher than steel GMAW because puddle is larger, nozzle bigger, gas needs to shield a wider area).

---

## Transfer modes — spray is the aluminum sweet spot

Aluminum GMAW works best in **spray transfer mode**:[^1]

| Transfer mode | Voltage / Amperage / Wire | Use for aluminum |
|---|---|---|
| **Short-circuit** | 15-22 V / 60-150 A | Poor for aluminum — cold lap, incomplete fusion. Avoid. |
| **Globular** | 22-25 V / 150-250 A | Transitional, high spatter. Skip. |
| **Spray** | 24-30 V / 180-300 A / 0.035"–0.045" | **The standard for aluminum GMAW.** Smooth fluid arc, deep penetration. |
| **Pulse** | Programmable pulse peaks up to 350 A | Better for thin/all-position; controls heat input. Requires inverter machine. |

**Standard technique: spray transfer, 0.045" ER4043 or ER5356, 24-28 V, 180-250 A depending on thickness. Argon shielding.**

---

## Push angle — the opposite of everything else

**GMAW-Al is a PUSH process.**[^4]

- Torch tilted 10-15° in the DIRECTION of travel (leading edge of the puddle leads)
- Why: aluminum's oxide skin forms instantly; pushing the arc scrubs the oxide off ahead of the puddle. Dragging traps oxide in the weld.
- Same push angle rule applies to any wire-feed aluminum (spool gun, push-pull, all machines).

**Steel is drag (backhand). FCAW is drag. Aluminum GMAW is push (forehand). Memorize.**

---

## Amperage for aluminum GMAW

Higher than steel at the same thickness (aluminum's thermal conductivity):[^1]

| Thickness | Wire diameter | Amperage / Voltage |
|---|---|---|
| 1/8" (0.125") | 0.035" | 140-170 A / 20-24 V |
| 3/16" (0.187") | 0.035" or 0.045" | 170-220 A / 22-26 V |
| 1/4" (0.250") | 0.045" | 200-250 A / 24-28 V |
| 3/8" (0.375") | 0.045" or 1/16" | 250-320 A / 26-30 V |

**Foot pedal / trigger control:** most spool guns have simple trigger; adjust amperage at the machine and let heat build up naturally.

---

## Positions on aluminum plate (AIT training expectations)

1F, 2F, 3F fillet welds on aluminum gauge plate:[^5]

| Position | Technique notes |
|---|---|
| **1F flat** | Push angle 15° in direction of travel, gun into corner 45°, straight travel |
| **2F horizontal** | Angle gun slightly upward (5-10°) to counter puddle sag; slower travel |
| **3F vertical up** | Reduce amperage 15-20%; slower travel; slight up-triangle weave at wider gaps |

**Aluminum vertical up is a real skill.** The puddle wants to run out and molten aluminum has poor surface tension compared to steel. Practice with plenty of scrap.

---

## Cleaning — same rules as GTAW aluminum

Aluminum GMAW is only marginally more tolerant of dirty material than GTAW. You still need:[^4]

1. Wire brush with a **stainless-steel brush dedicated to aluminum**
2. Wipe with acetone
3. Weld within 30 minutes of cleaning
4. Store aluminum wire in a **sealed spool container** — moisture absorption ruins it
5. Never leave a partial spool exposed overnight

---

## Numbers you need to memorize

- **Polarity for GMAW aluminum:** DCEP[^1]
- **Shielding gas:** 100% argon (Ar/He on thick material)[^4]
- **Gas flow rate:** 30-50 CFH[^4]
- **Drive rolls:** U-groove SMOOTH (not V-groove, not knurled)[^2]
- **Gun liner:** Teflon (PTFE) or nylon (not steel spring)[^2]
- **Best system:** spool gun (short work) or push-pull (production)[^1][^2]
- **Transfer mode:** SPRAY transfer (short-circuit is inadequate for aluminum)[^1]
- **Push angle:** 10-15° in DIRECTION of travel (opposite of steel drag)[^4]
- **Filler ER4043:** 5% Si, general purpose, 6xxx-series, easier[^3]
- **Filler ER5356:** 5% Mg, structural, marine, anodizing[^3]
- **Amperage:** ~30-50% higher than steel at same thickness (thermal conductivity)[^1]
- **Vertical up amperage reduction:** 15-20% from flat setting[^1]
- **Cleaning window:** weld within 30 min of cleaning[^4]

---

## What the textbook doesn't tell you

**If you're feeding aluminum from a spool gun and getting bird's-nesting or erratic feed:** check drive-roll tension first (should be minimum that still feeds), then contact tip size (aluminum tips are slightly oversized), then wire quality (open a fresh spool if the current one is > 6 months old and exposed to humidity).[^2]

**Aluminum wire absorbs hydrogen from humidity.** A spool left exposed for a week can develop enough hydrogen absorption to cause pinhole porosity across every weld you run with it. Store spools in sealed containers with desiccant packs. Rotate stock.[^4]

**The "silver mercury look" in the puddle** is your signal for filler dip (in GTAW) — in GMAW it means you're in stable spray transfer. Watch for it. If the puddle looks matte or has visible spatter, you're not in spray — increase voltage or amperage.[^1]

**Aluminum guns get hot fast.** GMAW aluminum runs long durations at high amperage. Air-cooled guns are OK for 5-10 minute stitches; water-cooled guns needed for continuous production. If your spool gun starts feeling warm to the touch, take a break — burnback is imminent.[^2]

**Spray transfer is loud and hissy compared to steel short-arc.** First-timers think something's wrong. It's not — it's just the correct sound for spray-transfer aluminum GMAW. If you hear the crackle-pop of short-arc, your voltage is too low.[^1]

**Contact tip changes are more frequent on aluminum.** Aluminum wire wears the tip faster than steel wire (softer wire deforming through the same hole). Keep spares on hand. Feel for oval wear in the tip bore — that's when it's time to swap.[^2]

**Aluminum on stainless brushes:** the same rules apply as GTAW — dedicated stainless-only wire brush that has NEVER touched steel, brass, or another aluminum alloy that could contaminate the joint.[^4]

---

## Diagram

*(SVG to be added: `assets/diagrams/p2-s5-a-spool-gun-vs-pushpull.svg` — side-by-side illustration of spool gun (short cable, spool on gun) vs push-pull system (spool at machine, dual drive motors))*

*(SVG to be added: `assets/diagrams/p2-s5-a-push-vs-drag.svg` — comparison showing steel GMAW drag angle (backhand) vs aluminum GMAW push angle (forehand) with oxide-scrubbing indicated on aluminum diagram)*

---

## Key terms

- **Spool gun:** GMAW gun with wire spool integrated on the gun handle (short push distance for soft aluminum wire)
- **Push-pull system:** dual-drive wire feeding system (one motor at feeder, one at gun) for longer cable distances
- **U-groove smooth drive roll:** the correct drive roll type for aluminum wire
- **Push angle (forehand):** torch tilted in the direction of travel (correct for aluminum GMAW)
- **Spray transfer:** high-voltage, high-amperage GMAW mode where filler transfers as a fine spray of droplets
- **PTFE / Teflon liner:** the correct gun liner for aluminum GMAW (replaces the steel spring liner)
- **Bird's-nest:** wire tangling at the drive rolls (usually caused by wrong roll type or too much tension on aluminum)

---

## Common exam trap

- **GMAW aluminum is a PUSH process (forehand).** Distractors will offer drag/backhand — that's for steel GMAW and FCAW, wrong for aluminum.
- **Drive rolls: U-groove SMOOTH** (not V-groove, not knurled). Knurled rolls tear up soft aluminum wire.
- **Spool gun or push-pull, not standard steel gun.** Aluminum wire is too soft for long cable pushes with standard equipment.
- **100% argon shielding.** CO2 or Ar/CO2 mixes are wrong.
- **Spray transfer mode** — not short-circuit. Short-circuit on aluminum = cold lap and lack of fusion.
- **DCEP polarity** (same as steel GMAW, different from GTAW aluminum which is AC).
- **Amperage HIGHER than steel** at the same thickness (aluminum's thermal conductivity carries heat away).
- **Contact tip is slightly OVERSIZED** for aluminum, not undersized.
- **Aluminum wire storage:** sealed container with desiccant; hydrogen absorption from humidity ruins wire.

---

## Practice question preview

**Q:** A welder needs to run production GMAW on 1/4" 5083 aluminum plate for a marine fabrication shop. The plate will be exposed to saltwater and eventually anodized. Which combination of settings is correct?

A) ER4043 wire, 75% Ar / 25% CO2 shielding, drag angle
B) ER5356 wire, 100% argon shielding, push angle, spray transfer
C) ER4043 wire, 100% CO2 shielding, spray transfer, drag angle
D) ER5356 wire, 100% argon shielding, drag angle, short-circuit transfer

**Correct: B**

**Explanation:** For 5083 marine-grade aluminum destined for anodizing, the correct filler is ER5356 (5% Mg, matches base metal, anodizes to the same color as base). Aluminum GMAW requires 100% argon shielding (any CO2 causes carbide formation), push angle (not drag — the push scrubs oxide off the joint ahead of the puddle), and spray transfer for adequate fusion on 1/4" material. A) ER4043 turns dark when anodized (unacceptable for marine cosmetics); C) 100% CO2 destroys aluminum welds; D) Drag angle on aluminum traps oxide in the weld; short-circuit transfer on 1/4" aluminum causes cold lap and lack of fusion.

**Red Seal mapping:** D-14.01 (Selects FCAW, MCAW and GMAW gas, equipment and consumables), D-14.03 (Sets operating parameters)

---

[^1]: [Miller Electric — Aluminum GMAW / MIG Welding Guide](https://www.millerwelds.com/resources/article-library/mig-welding-aluminum); spool gun vs push-pull, spray transfer parameters, aluminum push angle
[^2]: [Lincoln Electric — Aluminum MIG Welding](https://www.lincolnelectric.com/en/education-center/welding-education/aluminum-mig-welding); drive roll requirements, liner selection, contact tip sizing
[^3]: [AWS A5.10 — Bare Aluminum Welding Electrodes and Rods](https://pubs.aws.org/p/1039/a510a510m2017-specification-for-bare-aluminum-and-aluminum-alloy-welding-electrodes-and-rods); ER4043 and ER5356 chemistry, application matching, anodizing compatibility
[^4]: [ESAB Welding Handbook — Aluminum GMAW chapter](https://esab.com/us/nam_en/education/blog/aluminum-welding-guide/); push angle, gas selection, drive rolls, wire storage
[^5]: [AIT Welder Curriculum Guide 012 (2026)](https://tradesecrets.alberta.ca/SOURCES/PDFS/CURRICULUM_GUIDES/012_OUTLINE.PDF), Period 2 Section 5 Topic A — 1F/2F/3F on aluminum
