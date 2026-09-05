---
id: p2-s4-e
period: 2
section: 4
section_title: Gas Tungsten Arc Welding (GTAW)
topic_letter: E
topic_title: GTAW on Aluminum
hours: 5
weight_pct: 2
outcome: >
  Upon successful completion, learners will be able to perform GTAW on aluminum
  in flat and horizontal positions on gauge plate.
objectives:
  - Perform stringer beads in the flat position on aluminum gauge plate.
  - Perform 1F, 2F, 3F welds on aluminum gauge plate.
  - Set up GTAW equipment for AC operation on aluminum (balance, frequency, tungsten prep).
  - Identify common aluminum defects and their causes.
red_seal_mapping:
  - D-15.01 (Selects GTAW gas, equipment and consumables)
  - D-15.02 (Sets up GTAW equipment)
  - D-15.03 (Sets operating parameters for GTAW)
  - D-15.04 (Performs weld using GTAW equipment)
citations:
  - source: Miller Electric — Guidelines for Aluminum GTAW / TIG Welding Aluminum
    ref: AC balance, frequency, amperage tables for aluminum thickness
    url: https://www.millerwelds.com/resources/article-library/how-to-tig-weld-aluminum
  - source: Lincoln Electric — TIG Welding Aluminum Fundamentals
    ref: AC current characteristics, tungsten prep for aluminum, filler selection
    url: https://www.lincolnelectric.com/en/education-center/welding-education/how-to-tig-weld-aluminum
  - source: AWS A5.10 — Specification for Bare Aluminum and Aluminum-Alloy Welding Electrodes and Rods
    ref: ER4043 (5% Si), ER5356 (Mg alloy) filler classifications
    url: https://pubs.aws.org/p/1039/a510a510m2017-specification-for-bare-aluminum-and-aluminum-alloy-welding-electrodes-and-rods
  - source: AWS A5.12 — Tungsten Electrode Specification
    ref: Pure tungsten (green), zirconiated (brown/white), 2% lanthanated (blue) for AC aluminum
    url: https://pubs.aws.org/p/1046/a512a512m2009-specification-for-tungsten-and-oxide-dispersed-tungsten-electrodes-for-arc-welding-and-cutting
  - source: ESAB — Welding Handbook, Aluminum & Aluminum Alloys chapter
    ref: Aluminum oxide behavior, hydrogen porosity control, cleaning requirements
    url: https://esab.com/us/nam_en/education/blog/aluminum-welding-guide/
  - source: AIT Welder Curriculum Guide 012 (2026), Period 2 Section 4 Topic E
    ref: p. 29
    url: https://tradesecrets.alberta.ca/SOURCES/PDFS/CURRICULUM_GUIDES/012_OUTLINE.PDF
---

# GTAW on Aluminum

Aluminum is where GTAW earns its reputation. AC current, tungsten balls up, the oxide layer melts at 3× the base metal temperature, and hydrogen porosity chases every weld. Get it right and you produce beautiful, structurally sound welds on everything from truck decks to boat hulls to aerospace parts. Get it wrong and it looks like a bird crapped molten metal on your workpiece.

---

## Why aluminum is different from steel

Three things make aluminum hard:[^5]

1. **Aluminum oxide (Al₂O₃) melts at ~2050 °C (3720 °F)** — but pure aluminum melts at only **660 °C (1220 °F)**. You have an oxide film with a melting point almost 3× the base metal's. If you don't break through that oxide, the arc will just skate on top.
2. **Aluminum has ~5× the thermal conductivity of steel.** Heat runs away from the weld puddle fast. You need more amperage per thickness than steel, AND you need to start hot and back off as the workpiece heats up.
3. **Molten aluminum absorbs hydrogen aggressively.** Any moisture (from cleaning solvents, humidity, contaminated filler) becomes porosity in the finished weld.

The AC current + oxide-cleaning behavior of TIG is what makes it the go-to process for aluminum.

---

## AC current — the whole reason we use it on aluminum

Standard AC (from a TIG machine) alternates between two half-cycles:[^1][^2]

- **EN (Electrode Negative) half-cycle:** heat concentrated on the workpiece → deep penetration, but no oxide cleaning
- **EP (Electrode Positive) half-cycle:** heat concentrated on the tungsten → **cleaning action** as electrons flow from workpiece to tungsten, blasting oxide off the surface (this is what creates the frosty "cleaning zone" around your weld bead)

**AC balance control** lets you dial the ratio:
- **More EN (65-80% EN)** → deeper penetration, cooler tungsten. Standard for most work on clean aluminum.
- **More EP (up to 50/50)** → aggressive cleaning. Use when the aluminum is dirty or oxidized (older machines default here).

**AC frequency control** (on inverter machines):
- **60 Hz (transformer default)** → wider arc, more heat spread
- **100-200 Hz (inverter setting)** → tighter, more focused arc, cleaner weld
- **200+ Hz** → very narrow arc for detailed work on thin material

**Most production aluminum: 70% EN balance, 100-150 Hz frequency, pointed tungsten.**

---

## Tungsten — the modern rule (this changed in the last 15 years)

**Old rule (transformer machines, 60 Hz AC):** pure tungsten (green), balled tip
**Modern rule (inverter machines):** **2% lanthanated (blue)** or **1.5% lanthanated (gold)**, sharpened to a point[^4]

Why the shift:
- Inverter machines can run tungsten cooler and more efficiently
- Pointed tungsten gives a tighter arc → cleaner bead profile
- Lanthanated works well on AC and DC → single tungsten choice for entire shop
- Ceriated (grey) is also acceptable for AC on modern machines

**Old-timer with a transformer TIG machine?** Green (pure) tungsten balled at the tip is still correct. On modern inverters, point the lanthanated.

---

## Filler metals — ER4043 vs ER5356

Two fillers cover 95% of aluminum welding:[^3]

### ER4043 (5% silicon)
- **Color code:** none / bare
- **Melting characteristics:** flows smoothly, sluggish puddle, easy for beginners
- **Best for:** general repair, 6xxx-series castings (6061, 6063), non-critical fillet welds
- **Watch out:** slightly lower strength; NOT recommended when the finished part will be anodized (turns black)

### ER5356 (5% magnesium)
- **Color code:** none / bare
- **Melting characteristics:** stiffer puddle, more "crackly" arc sound, more difficult for beginners
- **Best for:** 5xxx-series alloys (5052, 5086, 5083 — marine and structural), when strength matters, when anodizing is required
- **Higher strength**, better for load-bearing applications

**Rule of thumb:**
- 6061 base metal → ER4043 filler (or ER5356 if strength critical)
- 5052/5086/5083 base metal → ER5356 filler (matching magnesium content)
- Unknown alloy → ER4043 (safer default)

---

## Amperage — aluminum takes more current than steel

**Rule of thumb: 1 amp per 0.001" of thickness (same as steel base rule), BUT start 30-50% higher and let heat build up.**[^1]

| Material thickness | Starting amperage (AC) |
|---|---|
| 1/16" (0.062") | 60-100 A |
| 3/32" (0.093") | 100-140 A |
| 1/8" (0.125") | 140-180 A |
| 3/16" (0.187") | 180-230 A |
| 1/4" (0.250") | 220-275 A |

**Foot pedal is essential.** You'll start near max amperage to establish the puddle, then back off progressively as the base metal preheats. A weld that starts fine can burn through halfway through if you don't ease off the pedal.

---

## Shielding gas — argon almost always

**100% argon** is standard for GTAW aluminum.[^1][^2]

**Argon/helium mix (25-75% He):** sometimes used on thick aluminum (1/4"+) or fast production runs. Helium adds heat but is expensive and has a hotter, harder-to-control arc.

**Flow rate:** 20-30 CFH for aluminum (higher than mild steel — the puddle is larger and the wider cup you'll typically use needs more flow to maintain coverage).

**Never use CO2 or Ar/CO2 mixes.** CO2 introduces carbon → aluminum carbide inclusions → brittle weld.

---

## Cleaning — before you strike ANY arc

Aluminum requires more prep than steel:[^5]

1. **Degrease** with acetone or aluminum-safe solvent. Wipe with a lint-free cloth. Change cloths often.
2. **Wire brush** with a **STAINLESS STEEL brush dedicated to aluminum ONLY**. A brush that has touched steel or brass will embed contaminant particles that show up as porosity or dark inclusions in the weld.
3. **Do all cleaning within 30 minutes of welding.** Aluminum oxide regrows on the surface within minutes. If more than an hour passes between cleaning and welding, re-brush.
4. **Filler rod cleanliness:** wipe filler with a clean acetone rag before use. Store filler in a sealed tube; never handle with bare oily hands.
5. **Grinder wheels for aluminum only.** A wheel that has ground steel will embed iron particles.

**Any skipped step = porosity.** Aluminum is unforgiving.

---

## Torch and filler technique

Similar to steel but with adjustments:[^1]

- **Torch angle:** 10-15° push angle (leading — same as steel)
- **Arc length:** ~1× tungsten diameter (short, tight)
- **Puddle appearance:** aluminum turns SHINY like mercury when molten. That's your cue to start feeding filler.
- **Filler dip:** into the leading edge of the puddle, then withdraw slightly (keep in the argon shield). Same rhythm as steel but expect faster puddle response.
- **Watch for the cleaning halo:** the frosty white/grey ring around your bead is the oxide-cleaning action from EP half-cycles. If you don't see it, your EP balance is too low.
- **Travel speed:** faster than steel — aluminum's high thermal conductivity means you spread heat quickly

---

## Positions on aluminum plate

For AIT/NAIT training, expected positions on aluminum gauge plate are:[^6]

| Position | Notes |
|---|---|
| **1F flat fillet** | Standard technique, torch 45° into joint corner |
| **2F horizontal fillet** | Tilt torch upward 5-10° to counter puddle sag; REDUCE amperage ~15% from 1F setting |
| **3F vertical up fillet** | REDUCE amperage ~20%; slower travel; slight side-to-side motion at wider gaps |

**Vertical up on aluminum is tough.** The puddle wants to run out and gravity + surface tension are working against you. Practice on scrap before coupon.

---

## Numbers you need to memorize

- **Polarity for aluminum GTAW:** AC (Alternating Current)[^1]
- **Aluminum melting point:** 660 °C / 1220 °F[^5]
- **Aluminum oxide (Al₂O₃) melting point:** ~2050 °C / 3720 °F[^5]
- **AC balance typical:** 70% EN / 30% EP (dial toward more EP if aluminum is dirty)[^1]
- **AC frequency (inverter):** 100-200 Hz typical (higher = tighter arc)[^1]
- **Tungsten (modern inverter):** 2% lanthanated (blue) or 1.5% lanthanated (gold), POINTED[^4]
- **Tungsten (old transformer):** pure tungsten (green), BALLED[^4]
- **Shielding gas:** 100% argon (never CO2 or CO2 mix)[^1]
- **Gas flow rate:** 20-30 CFH for aluminum[^1]
- **Filler ER4043:** 5% silicon, general repair, easier for beginners[^3]
- **Filler ER5356:** 5% magnesium, structural, marine, anodizing OK[^3]
- **Amperage starting rule:** 1 A per 0.001" of thickness × 1.3-1.5 (higher than steel)[^1]
- **Cleaning window:** clean within 30 min of welding[^5]
- **Never use:** steel brush, brush that has touched other metals, CO2 gas, oily filler rods

---

## What the textbook doesn't tell you

**The clean rag habit is critical.** You'll go through more acetone and lint-free rags on an aluminum job than on any other process. Steel welders wipe once; aluminum welders wipe every 2-3 dips. Skip this and porosity finds you.[^5]

**Hydrogen porosity is aluminum's ghost.** Every drop of moisture — humidity on cold metal, condensation inside a hollow section, a fingerprint — becomes trapped H2 in the weld and shows up as pinhole or worm-track porosity. Preheat mildly (100-150 °F) on thick sections in humid conditions to drive off surface moisture.[^5]

**The "cleaning halo" tells you AC balance is right.** If you see NO frosty cleaning zone around your bead, you're running too much EN — increase EP. If the cleaning zone is huge (1/2" wide), you're running too much EP — decrease EP (heat is going into the tungsten instead of the workpiece → wandering arc, wide flat bead).[^1][^2]

**Aluminum sounds different.** ER4043 arc: smooth, quiet hum. ER5356 arc: crackly, snappy. If you're used to 4043 and switch to 5356 without adjusting expectations, you'll think something's wrong. Nothing's wrong — 5356 is just noisier.[^3]

**On thick aluminum, PREHEAT.** Anything over 1/4" benefits from 200-300 °F preheat to reduce the thermal-conductivity handicap. This lets you use lower welding amperage and get cleaner starts.[^2]

**When the tungsten balls up on modern inverters, something's wrong.** Modern lanthanated tungsten should stay pointed on AC aluminum work (unlike old pure tungsten on transformer machines). If it's balling, either your EP balance is too high (too much heat going to tungsten) or your amperage is too high for the tungsten diameter.[^4]

**Beginner mistake #1:** Filler rod hitting tungsten. On aluminum this contamination is worse than on steel because the AC current can't burn it clean. Result: erratic arc, contaminated tungsten, ruined weld. If it happens: kill pedal, cut/regrind tungsten, restart.

**Beginner mistake #2:** Not accounting for heat build-up. First 2 inches of the coupon look great; last 2 inches burn through. Ease off the pedal as you progress along the coupon.

---

## Diagram

*(SVG to be added: `assets/diagrams/p2-s4-e-ac-waveform.svg` — AC waveform showing EN and EP half-cycles with balance control (70/30) illustrated, cleaning halo shown around bead cross-section)*

*(SVG to be added: `assets/diagrams/p2-s4-e-aluminum-tungsten.svg` — comparison of modern pointed lanthanated tungsten (correct) vs old-style balled pure tungsten (only for transformer machines))*

---

## Key terms

- **AC (Alternating Current):** current that reverses direction 60+ times per second — required for aluminum GTAW
- **EN / EP half-cycles:** Electrode Negative (penetration) / Electrode Positive (cleaning) halves of the AC waveform
- **AC balance:** the ratio of EN to EP time in the AC cycle
- **AC frequency:** how many times per second the AC current reverses (60 Hz standard, 100-200 Hz on inverters)
- **Cleaning halo / cleaning zone:** the frosty ring around an aluminum weld showing where the AC oxide-cleaning action occurred
- **ER4043:** 5% silicon aluminum filler — general purpose
- **ER5356:** 5% magnesium aluminum filler — marine, structural, anodizable
- **Aluminum oxide (Al₂O₃):** the film that forms on aluminum surface, melts at 2050 °C
- **Hydrogen porosity:** pinhole porosity from moisture-derived hydrogen absorption

---

## Common exam trap

- **AC (not DC) for aluminum.** Distractors will offer DCEN or DCEP; both are wrong for standard aluminum GTAW.
- **Aluminum oxide melting point is HIGHER than the aluminum itself.** ~2050 °C oxide vs 660 °C aluminum. This is the key concept — questions will test whether you know why AC's cleaning action matters.
- **Modern lanthanated tungsten is POINTED on AC**, not balled. Pure tungsten balls on AC (transformer machines). Reverse this and you get the answer wrong.
- **ER5356 is for magnesium-content aluminum (5xxx series) and anodizing applications.** ER4043 turns black when anodized.
- **NEVER use CO2 or CO2 mixes on aluminum.** Carbon → aluminum carbide → brittle weld. Only argon (or Ar/He mix on thick material).
- **Aluminum wire brush must be dedicated to aluminum ONLY.** Mixed-use brushes cause contamination.
- **Cleaning halo present = correct AC balance.** No halo = too much EN; excessive halo = too much EP.

---

## Practice question preview

**Q:** A welder is preparing to GTAW-weld a 6061-T6 aluminum tank that will be anodized after fabrication. Which filler material is MOST appropriate?

A) ER70S-6 (mild steel filler)
B) ER4043 (5% silicon aluminum filler)
C) ER5356 (5% magnesium aluminum filler)
D) ER308L (stainless steel filler)

**Correct: C**

**Explanation:** For an aluminum tank that will be anodized, ER5356 (5% Mg) is the correct choice because it matches the alloying strategy for post-weld anodizing — the weld will anodize to the same color as the base metal. A) ER70S-6 is a mild steel filler, incompatible with aluminum; B) ER4043 (5% Si) welds aluminum but turns dark/black when anodized, creating a visible cosmetic defect at every weld bead; D) ER308L is a stainless filler, incompatible with aluminum. When anodizing is required OR the base is a 5xxx series alloy, ER5356 is the correct filler.

**Red Seal mapping:** D-15.01 (Selects GTAW gas, equipment and consumables)

---

[^1]: [Miller Electric — Guidelines for Aluminum GTAW / TIG Welding Aluminum](https://www.millerwelds.com/resources/article-library/how-to-tig-weld-aluminum); AC balance, frequency, amperage, foot pedal use, technique
[^2]: [Lincoln Electric — TIG Welding Aluminum Fundamentals](https://www.lincolnelectric.com/en/education-center/welding-education/how-to-tig-weld-aluminum); AC current characteristics, preheat guidance, joint prep
[^3]: [AWS A5.10 — Bare Aluminum and Aluminum-Alloy Welding Electrodes and Rods](https://pubs.aws.org/p/1039/a510a510m2017-specification-for-bare-aluminum-and-aluminum-alloy-welding-electrodes-and-rods); ER4043 and ER5356 chemistry, applications, anodizing compatibility
[^4]: [AWS A5.12 — Tungsten Electrode Specification](https://pubs.aws.org/p/1046/a512a512m2009-specification-for-tungsten-and-oxide-dispersed-tungsten-electrodes-for-arc-welding-and-cutting); tungsten selection for AC aluminum on modern vs transformer machines
[^5]: [ESAB Welding Handbook — Aluminum & Aluminum Alloys chapter](https://esab.com/us/nam_en/education/blog/aluminum-welding-guide/); aluminum oxide behavior, hydrogen porosity mechanisms, cleaning requirements
[^6]: [AIT Welder Curriculum Guide 012 (2026)](https://tradesecrets.alberta.ca/SOURCES/PDFS/CURRICULUM_GUIDES/012_OUTLINE.PDF), Period 2 Section 4 Topic E — positions 1F/2F/3F on aluminum gauge plate
