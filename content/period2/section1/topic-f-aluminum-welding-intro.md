---
id: p2-s1-f
period: 2
section: 1
section_title: Foundational Skills, Safety, Procedures and Properties of Metals
topic_letter: F
topic_title: Aluminum and Aluminum Welding
hours: 3
weight_pct: 1
outcome: >
  Upon successful completion, learners will be able to describe aluminum properties and welding principles, including alloy designations.
objectives:
  - Describe the physical and chemical properties of aluminum versus steel.
  - Describe how physical and chemical properties affect the welding of aluminum.
  - Describe the Aluminum Association numerical designation for casting alloys and wrought aluminum.
  - Describe the effects of welding on heat treatable and non-heat treatable alloys.
  - Identify the filler metals used for welding aluminum.
red_seal_mapping:
  - A-5.05 (Selects welding processes and power source)
  - D-14.01 (Selects FCAW, MCAW and GMAW gas, equipment and consumables)
  - D-15.01 (Selects GTAW gas, equipment and consumables)
citations:
  - source: Lincoln Electric — Aluminum Welding Guide
    ref: Alloy designation system, filler selection, cleaning procedure, heat-treatable vs non-heat-treatable alloys
    url: https://www.lincolnelectric.com/en/education-center/welding-education/aluminum-welding
  - source: ESAB — Aluminum Welding Handbook
    ref: Physical and mechanical properties, oxide layer, thermal expansion, weld cracking susceptibility, ER4043 vs ER5356 selection
    url: https://www.esab.com/us/nam_en/education/aluminum-welding.cfm
  - source: AWS A5.10 — Specification for Bare Aluminum and Aluminum Alloy Welding Electrodes and Rods
    ref: ER4043, ER4047, ER5356, ER5183, ER5556 filler metal classifications
    url: https://pubs.aws.org/p/1139/a510a5-10a5-10m2012-specification-for-bare-aluminum-and-aluminum-alloy-welding-electrodes-and-rods
  - source: Modern Welding (Bowditch, Goodheart-Willcox, 12th ed.)
    ref: Chapter 20 — Aluminum and Aluminum Alloys; properties, designation system, welding considerations
    url: https://www.g-w.com/modern-welding
  - source: AIT Welder Curriculum Guide 012 (2026), Period 2 Section 1 Topic F
    ref: pp. 31–32
    url: https://tradesecrets.alberta.ca/SOURCES/PDFS/CURRICULUM_GUIDES/012_OUTLINE.PDF
---

# Aluminum and Aluminum Welding

Aluminum is the second-most-welded metal in Alberta fabrication shops after steel. Oilfield equipment, trailers, boats, architectural components, automotive parts — the list is long. It behaves completely differently from steel in every respect that matters to a welder: it melts at less than half the temperature, expands twice as fast, conducts heat three times faster, and is covered by an oxide layer that needs to be broken up before you can weld. Learn to think about aluminum on its own terms, not as "weird steel."

---

## Aluminum vs steel: the key differences

| Property | Mild Steel | Aluminum | Consequence for welding |
|---|---|---|---|
| **Melting point** | ~1510°C | ~660°C | Aluminum melts quickly and without visual warning (no colour change before melting) |
| **Density** | 7.85 g/cm³ | 2.7 g/cm³ | Aluminum is ~1/3 the weight; requires different handling |
| **Thermal conductivity** | ~50 W/m·K | ~230 W/m·K | Aluminum dissipates heat ~4-5× faster — needs more amperage per mm of thickness |
| **Thermal expansion** | 12 × 10⁻⁶/°C | 23 × 10⁻⁶/°C | Aluminum distorts nearly twice as much for the same heat input |
| **Oxide melting point** | ~1530°C (FeO) | ~2050°C (Al₂O₃) | Aluminum's oxide melts at 3× the temperature of the base metal — must be removed before welding |
| **Electrical conductivity** | Low | High | GTAW AC current's cathodic cleaning action removes the oxide; GMAW requires mechanical cleaning |
| **Colour before melting** | Glows red/orange | No colour change | Easy to overheat and melt through without visual warning |
| **Magnetism** | Magnetic | Non-magnetic | Useful for identification |

---

## The aluminum oxide problem

This is the most important concept in aluminum welding.[^1][^2]

Aluminum forms a thin, tightly-adherent oxide layer (Al₂O₃) immediately on exposure to air. This oxide:
- **Melts at ~2050°C** — versus the base metal's 660°C
- **Is invisible** — it looks like shiny aluminum
- **Reforms within seconds** after removal
- **Is denser and harder than the base metal**

**When you weld without removing the oxide:**
- The oxide remains solid while the base metal melts beneath it → the oxide sinks into the molten pool → **oxide inclusions** in the weld
- The oxide prevents proper fusion along the toes → **lack of fusion**
- If moisture is trapped in the oxide layer → **porosity**

**How oxide is removed:**
1. **GTAW with AC current:** The cathodic cleaning half-cycle (electrode positive half of AC) bombards the oxide surface with argon ions, shattering and displacing the oxide. This is why AC is used for aluminum GTAW — the cleaning action is essential.
2. **Mechanical cleaning (GMAW and GTAW):** Use a **stainless steel brush dedicated solely to aluminum** (never used on steel or stainless). Brush in one direction immediately before welding. Do NOT use a carbon steel brush — it embeds iron particles that cause porosity.
3. **Chemical cleaning:** Wipe with acetone or a purpose-formulated aluminum cleaner to remove oil and grease *first*, then brush.

**The cleaning sequence:** Degrease → brush → weld. Do NOT reverse. Brushing before degreasing pushes contamination deeper.[^1]

---

## The Aluminum Association designation system

### Wrought aluminum alloys (4-digit system)[^3]

| Series | Main alloying element | Common grades | Notes |
|---|---|---|---|
| **1xxx** | Commercially pure (99%+ Al) | 1100 | Soft, ductile, excellent corrosion resistance; food/chemical equipment |
| **2xxx** | Copper | 2024 | High strength; aerospace; poor corrosion resistance; NOT recommended for welding |
| **3xxx** | Manganese | 3003 | Good formability; cooking utensils, fuel tanks |
| **4xxx** | Silicon | 4043 (filler metal) | Lower melting point; used as filler rather than structural base |
| **5xxx** | Magnesium | 5052, 5083, 5086 | Excellent corrosion resistance; marine, structural; most common weldable |
| **6xxx** | Magnesium + Silicon | 6061, 6063 | Medium-high strength; heat-treatable; structural (extrusions, tube, plate) |
| **7xxx** | Zinc | 7075 | Very high strength; aerospace; NOT recommended for welding (hot cracking) |
| **8xxx** | Other elements | 8001 (Li alloy) | Special purpose |

### Casting alloys (3-digit + decimal system)[^3]
Casting alloys use a different system:
- **1xx.x:** Pure aluminum castings
- **3xx.x:** Aluminum-Silicon + Copper or Mg (most common; A356.0 is the most used structural casting)
- **4xx.x:** Aluminum-Silicon
- **5xx.x:** Aluminum-Magnesium
- **.0 suffix:** for castings; **.1 or .2 suffix:** for ingot

---

## Heat-treatable vs non-heat-treatable alloys

This distinction is critical for welding.[^1][^4]

### Non-heat-treatable alloys (1xxx, 3xxx, 5xxx)
- Strength comes from **cold-working** (strain hardening) — designations include O (annealed), H12, H32, H34, etc.
- Welding **does not significantly alter mechanical properties** — the heat-affected zone (HAZ) may soften slightly, but no dramatic strength loss
- These are the easiest alloys to weld

### Heat-treatable alloys (2xxx, 6xxx, 7xxx)
- Strength comes from **precipitation hardening** — a heat treatment cycle that produces fine alloy precipitates within the aluminum matrix
- Welding destroys the precipitation hardening in the HAZ — the HAZ **softens dramatically** (returns to annealed condition locally)[^1][^4]
- **6061-T6** is the most common example: T6 temper means peak-aged to full strength. Welding the HAZ region reduces it from ~276 MPa yield strength back to ~103 MPa — a ~60% strength reduction in the HAZ[^4]
- After welding, 6xxx alloys can be re-heat-treated to restore some strength, but field welded assemblies rarely get this treatment
- **Design implication:** Joint efficiency for welded 6061-T6 is typically 50–60% of parent metal. Design engineers must account for this.

---

## Filler metal selection for aluminum

Filler selection is driven by: base metal alloy, service environment (marine = corrosion resistance needed), and post-weld heat treatment requirements.[^3]

### ER4043 (Silicon 4.5–6.0%)[^3]
- **Best for:** Welding 6xxx alloys (6061, 6063) and dissimilar aluminum combinations; castings (A356)
- **Advantages:** Low cracking susceptibility; good fluidity; easy to feed (harder wire)
- **Disadvantages:** Poor response to anodizing (turns grey-black); lower ductility than 5xxx fillers
- **Not for:** 5xxx base metals (causes hot cracking) or color-matched applications

### ER5356 (Magnesium 4.5–5.5%)[^3]
- **Best for:** 5xxx alloys (5052, 5083, 5086), 6xxx alloys with color matching requirement
- **Advantages:** Higher tensile strength than 4043; matches anodized color of 5xxx; good corrosion resistance in marine environments
- **Disadvantages:** Slightly harder to feed (stiffer wire); higher cracking susceptibility than 4043 on 6xxx; not for service above 65°C (sensitization risk with high Mg content over time)

### ER4047 (Silicon ~12%)[^3]
- **Best for:** Brazing and hard-to-weld casting alloys; excellent for automotive heat exchangers
- **Characteristics:** Very low melting point (lower than 4043); flows well

### ER5183 / ER5556[^3]
- **Best for:** High-strength 5xxx base metals (5083, 5086, 5456); structural applications requiring highest possible joint strength
- **Marine and pressure vessel work**

### Quick filler selection guide

| Base metal | First choice | Alternative |
|---|---|---|
| 1100 | ER1100 | ER4043 |
| 3003 | ER4043 | ER1100 |
| 5052 | ER5356 | ER4043 |
| 5083, 5086 | ER5356 or ER5183 | — |
| 6061, 6063 | ER4043 | ER5356 (color) |
| Castings (A356) | ER4043 | ER4047 |
| 2024, 7075 | NOT RECOMMENDED FOR WELDING | — |

---

## Numbers you need to memorize

- **Aluminum melting point:** ~660°C[^1]
- **Aluminum oxide (Al₂O₃) melting point:** ~2050°C[^1]
- **Aluminum thermal expansion:** ~23 × 10⁻⁶/°C (vs ~12 × 10⁻⁶/°C for steel)[^1]
- **Aluminum thermal conductivity:** ~230 W/m·K (vs ~50 W/m·K for steel) — ~4-5× faster heat dissipation[^1]
- **6061-T6 yield strength reduction in welded HAZ:** ~60% drop from T6 condition[^4]
- **ER4043 Si content:** 4.5–6.0%[^3]
- **ER5356 Mg content:** 4.5–5.5%[^3]
- **ER5356 service temperature limit:** do not use above 65°C for sustained loading (sensitization risk)[^3]
- **GTAW on aluminum uses AC current** — cathodic cleaning action removes oxide[^1]
- **Aluminum color change before melting:** NONE — unlike steel which glows red[^1]

---

## What the textbook doesn't tell you

**Aluminum is a "dumb metal" for hand GTAW — it gives you no warning.** With steel, you see the colour change and can back off. Aluminum stays shiny silver until it suddenly collapses into a hole. New GTAW welders on aluminum need to: keep amperage conservative, use a foot pedal to reduce heat as the puddle heats up, and watch the puddle, not the electrode tip.

**Dedicated tools are non-negotiable.** A stainless steel brush that has touched steel, even once, will contaminate every aluminum weld it touches afterward. Mark your aluminum brushes with yellow tape, store them separately, and if someone borrows one without asking, throw it out and start fresh. This isn't paranoia — it's basic quality control.

**5356 filler should not be used above 65°C in marine environments.** At high magnesium content (>3%) and elevated temperatures, the beta-phase (Mg₂Al₃) can precipitate at grain boundaries in the HAZ — making those grain boundaries susceptible to stress corrosion cracking over time. For boat fuel tanks or trailers that regularly see temperatures above 65°C, use 4043.[^2]

---

## Key terms

- **Al₂O₃ (aluminum oxide):** tough oxide layer forming instantly on aluminum surface; melting point ~2050°C
- **Cathodic cleaning:** the electrode-positive half-cycle of AC GTAW that shatters the aluminum oxide layer with argon ion bombardment
- **Heat-treatable alloy:** aluminum alloy (2xxx, 6xxx, 7xxx) that can be strengthened by precipitation heat treatment — but welding destroys this temper locally
- **Non-heat-treatable alloy:** aluminum alloy (1xxx, 3xxx, 5xxx) strengthened by cold working — welding has minimal effect on strength
- **T6 temper:** peak aged condition (solution heat treated + artificially aged) — the strongest common temper for 6061
- **HAZ softening:** reduction in strength of heat-treatable alloys in the heat-affected zone after welding
- **ER4043:** 4-5% Si aluminum filler; most common for 6xxx and casting base metals
- **ER5356:** 4.5-5.5% Mg aluminum filler; preferred for 5xxx base metals and color-match applications
- **Sensitization:** grain-boundary precipitation that makes Mg-rich alloys susceptible to stress corrosion at elevated temperatures

---

## Common exam trap

- **GTAW on aluminum REQUIRES AC current** — not DCEP, not DCEN. DCEN on aluminum means no cathodic cleaning → oxide inclusions guaranteed. Some exam distractors offer DCEP as the correct option (that's for steel GTAW).
- **ER4043 and ER5356 are NOT interchangeable** — using 4043 on 5083 base metal risks hot cracking. Using 5356 above 65°C in marine service risks sensitization.
- **Aluminum does NOT change colour before melting** — "watch for the red glow" is correct technique for steel, deadly for aluminum.
- **7075 and 2024 should NOT be welded** — they have severe hot cracking susceptibility. If the exam asks which alloy is NOT recommended for fusion welding, 7075 and 2024 are the answers.
- **The brush must be STAINLESS STEEL, not carbon steel** — a carbon steel brush embeds iron particles → porosity in aluminum weld.

---

## Practice question preview

**Q:** A welder is preparing to GTAW-weld a 6061-T6 aluminum structure. Which of the following filler metals and current types is CORRECT?

A) ER5356 filler, DCEN polarity
B) ER4043 filler, AC current
C) ER70S-6 filler, DCEP polarity
D) ER4043 filler, DCEN polarity

**Correct: B**

**Explanation:** 6061 aluminum is best welded with ER4043 filler (low cracking susceptibility, good fluidity, preferred for 6xxx series). GTAW on aluminum REQUIRES AC current to provide the cathodic cleaning action that breaks up the aluminum oxide layer. (A) ER5356 is acceptable for 6061 but DCEN does not provide cathodic cleaning. (C) ER70S-6 is a steel filler — it has no application to aluminum welding. (D) ER4043 is the right filler but DCEN polarity lacks the cathodic cleaning needed for aluminum.

**Red Seal mapping:** D-15.01 (Selects GTAW gas, equipment and consumables)

---

[^1]: [Lincoln Electric — Aluminum Welding Guide](https://www.lincolnelectric.com/en/education-center/welding-education/aluminum-welding); physical property comparisons, oxide removal procedure, cleaning sequence, AC current requirement, HAZ softening explanation
[^2]: [ESAB — Aluminum Welding Handbook](https://www.esab.com/us/nam_en/education/aluminum-welding.cfm); ER4043 vs ER5356 selection criteria, sensitization risk, crack susceptibility of alloy families
[^3]: [AWS A5.10 — Specification for Bare Aluminum and Aluminum Alloy Welding Electrodes and Rods](https://pubs.aws.org/p/1139/a510a5-10a5-10m2012-specification-for-bare-aluminum-and-aluminum-alloy-welding-electrodes-and-rods); ER4043, ER5356, ER4047, ER5183 filler classifications, composition, and application guidance
[^4]: [Modern Welding, 12th ed. (Bowditch, Goodheart-Willcox)](https://www.g-w.com/modern-welding), Chapter 20 — Aluminum and Aluminum Alloys; Aluminum Association designation system, heat-treatable vs non-heat-treatable, HAZ mechanical property effects
[^5]: [AIT Welder Curriculum Guide 012 (2026), Period 2 Section 1 Topic F](https://tradesecrets.alberta.ca/SOURCES/PDFS/CURRICULUM_GUIDES/012_OUTLINE.PDF), pp. 31–32
