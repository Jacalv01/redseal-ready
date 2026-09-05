---
id: p2-s4-f
period: 2
section: 4
section_title: Gas Tungsten Arc Welding (GTAW)
topic_letter: F
topic_title: GTAW on Stainless Steel
hours: 5
weight_pct: 2
outcome: >
  Upon successful completion, learners will be able to perform GTAW on stainless
  steel in 2F and 3F fillet positions on gauge plate, understanding the metallurgy
  and shielding requirements specific to austenitic stainless.
objectives:
  - Perform 2F and 3F welds on stainless steel gauge plate.
  - Select correct filler metals for austenitic stainless (ER308L, ER316L).
  - Identify and prevent carbide precipitation (sensitization).
  - Apply back-purge requirements for stainless root passes.
red_seal_mapping:
  - D-15.01 (Selects GTAW gas, equipment and consumables)
  - D-15.03 (Sets operating parameters for GTAW)
  - D-15.04 (Performs weld using GTAW equipment)
citations:
  - source: Miller Electric — Guidelines for Stainless Steel GTAW
    ref: DC selection, amperage tables, back-purging for stainless
    url: https://www.millerwelds.com/resources/article-library/how-to-tig-weld-stainless-steel
  - source: Lincoln Electric — Stainless Steel Welding Guide
    ref: Filler selection, heat input control, sensitization prevention
    url: https://www.lincolnelectric.com/en/education-center/welding-education/stainless-steel-welding-guide
  - source: AWS A5.9 — Specification for Bare Stainless Steel Welding Electrodes and Rods
    ref: ER308L, ER316L, ER309L classifications and applications
    url: https://pubs.aws.org/p/1044/a59a59m2017-specification-for-bare-stainless-steel-welding-electrodes-and-rods
  - source: TWI Global — Welding of Austenitic Stainless Steels
    ref: Carbide precipitation (sensitization), heat input, cleaning, discoloration
    url: https://www.twi-global.com/technical-knowledge/job-knowledge/welding-of-austenitic-stainless-steel-part-1-103
  - source: ESAB — Welding of Stainless Steels Handbook
    ref: Back-purge requirements, discoloration acceptance, brush contamination
    url: https://esab.com/us/nam_en/education/blog/stainless-steel-welding/
  - source: AIT Welder Curriculum Guide 012 (2026), Period 2 Section 4 Topic F
    ref: p. 29
    url: https://tradesecrets.alberta.ca/SOURCES/PDFS/CURRICULUM_GUIDES/012_OUTLINE.PDF
---

# GTAW on Stainless Steel

Stainless is where craftsmanship shows. A good stainless TIG weld is the calling card of a skilled welder — even, straw-colored, no discoloration past a certain point, no sugar on the back side. In food/pharma/pressure vessel work, "clean stainless" is worth $70+/hr in Alberta. Sloppy stainless welds fail sanitary inspection or worse, corrode from the inside out on the very equipment they're supposed to protect.

---

## The stainless family (know these three)

For AIT training and Red Seal purposes, three grades cover most work:[^3]

| Grade | Common name | Composition | Where used |
|---|---|---|---|
| **304 / 304L** | 18-8 stainless | 18% Cr, 8% Ni, 0.03% max C (L = low carbon) | Food equipment, sinks, tanks, general fab |
| **316 / 316L** | Marine grade | 16% Cr, 10% Ni, 2% Mo, 0.03% max C | Marine, chemical, pharma (Mo adds pitting resistance) |
| **309** | Transition | 22% Cr, 12% Ni | Buffer layer when joining stainless to mild steel, or hardfacing repairs |

**L (low carbon) versions matter.** 304L (0.03% max C) is preferred over 304 (0.08% max C) for welded structures because it resists carbide precipitation during welding.

---

## The killer problem: carbide precipitation (sensitization)

When austenitic stainless is heated between ~425-870 °C (800-1600 °F) for too long, **chromium carbides precipitate at grain boundaries**. This "steals" chromium from adjacent metal, dropping the local Cr below 10.5% — the level needed for stainless corrosion resistance.[^4]

**Result:** the weld looks fine but the heat-affected zone (HAZ) rusts out from the inside within months of service (intergranular corrosion).

**Three ways to prevent it:**
1. **Use L-grade filler and base metal** (0.03% max C) — the killer approach: low carbon = no carbides to precipitate
2. **Use stabilized grades** (321 with Ti, 347 with Nb) — these grades tie up carbon with something other than chromium
3. **Control heat input:** low amperage, fast travel, minimize time in the sensitizing temperature range

**Rule of thumb: never use standard 304 or 316 filler on welded stainless. Always specify L-grade.**

---

## Setup for stainless GTAW

| Setting | Value | Why |
|---|---|---|
| **Polarity** | DCEN (same as mild steel) | Concentrates heat in the workpiece |
| **Shielding gas** | 100% argon (some shops use 98% Ar / 2% H₂ for austenitic only) | Standard argon works for all stainless; H₂ mix on 300-series only, adds heat and cleans |
| **Gas flow rate** | 15-25 CFH | Same as mild steel |
| **Cup size** | #7 to #8 (bigger cup = better coverage = less oxidation of adjacent metal) | Some prefer gas lens setups for critical work |
| **Tungsten** | 2% ceriated (grey) or 2% lanthanated (blue), pointed — 2× diameter length | Same as mild steel DC |
| **Amperage** | ~1 A per 0.001" thickness × 0.85 (LESS heat than mild steel) | Stainless has ~1/2 the thermal conductivity of steel — heat concentrates in the weld area |
| **Travel speed** | Slightly FASTER than mild steel at same thickness | Minimize time in sensitizing range |

---

## Filler selection — matching L-grade to base metal

Match filler to base metal chemistry, always specifying L (low carbon):[^3]

| Base metal | Correct filler |
|---|---|
| 304 / 304L | **ER308L** (matches Cr-Ni content, low C) |
| 316 / 316L | **ER316L** (matches Cr-Ni-Mo content, low C) |
| 309 | **ER309L** (or use ER309L when joining 304-to-304 for extra safety margin) |
| Stainless to mild steel | **ER309L** (buffer chemistry handles dilution) |

**Common mistake:** using ER308L on 316L. It works but you lose the molybdenum in the weld → weld area becomes the corrosion weak point in marine/chemical service.

---

## Back-purging — non-negotiable for pipe, welcome for plate

Molten stainless will **oxidize (sugar) instantly on the underside** if not shielded. Sugaring destroys corrosion resistance and is visible as a black, crystalline crust on the root side.[^5]

**Rules:**
- **Pipe roots (any GTAW open root on stainless):** back-purge with argon, ALWAYS
  - Purge 5-10 minutes to displace air before starting
  - Maintain 5-10 CFH during welding
  - Continue purge until root pass has cooled below 400 °F
- **Plate welds:** back-purge if service requires corrosion resistance on the back side (pressure vessels, sanitary tanks, food equipment)
- **Purge dams:** paper + water-soluble tape (dissolves during hydrotest) for pipes you can't purge end-to-end

**Acceptable heat-tint / discoloration levels** (AWS D18.1 for sanitary work, industrial less strict):[^4]
- Silver / straw yellow: acceptable (Cr-oxide film still intact)
- Dark straw / blue: borderline — some codes reject
- Purple / black: reject — Cr depletion in the surface, will corrode

If you get past dark straw, you have a heat-input problem: too hot, too slow, or insufficient purge.

---

## Amperage for stainless — LESS than mild steel

Stainless has ~half the thermal conductivity of mild steel — heat doesn't run away as fast. **Use ~85% of the mild-steel amperage for the same thickness.**[^1]

| Thickness | Stainless amperage (DCEN, 100% Ar) |
|---|---|
| 1/16" (0.062") | 50-70 A |
| 3/32" (0.093") | 75-95 A |
| 1/8" (0.125") | 95-120 A |
| 3/16" (0.187") | 120-150 A |
| 1/4" (0.250") | 150-190 A |

**Travel faster than you would on steel** to minimize sensitizing-range dwell time.

---

## Cleanliness — separate everything

Cross-contamination is the enemy:[^5]

1. **Dedicated stainless-only tools:** wire brushes, grinding wheels, files, layout markers
2. **No contact with carbon steel or aluminum** — a stainless brush that has touched carbon steel embeds iron particles → these become rust spots that eat into the stainless (called "rouge" in food/pharma industries)
3. **Marker choice:** use only stainless-approved markers (chlorine-free, sulfur-free) — regular Sharpies contain chlorides that cause stress-corrosion cracking
4. **Layout with a scribe or dedicated soapstone** — never carbon steel scribes
5. **Wipe with clean acetone** before welding — no petroleum-based solvents

---

## Torch and filler technique for stainless

Very similar to mild steel with three differences:[^1][^2]

- **Faster travel** to reduce heat input
- **Smaller filler dips, more frequent** — smaller puddle means less filler goes in per dip
- **Watch the color trail behind the bead:** silver → straw yellow is your target. Watch it in real time; back off if it darkens.
- **Torch angle:** 10-15° push, same as steel
- **Arc length:** slightly SHORTER than mild steel (~0.75× tungsten diameter) — tighter arc concentrates heat where you want it

---

## Positions expected in AIT training

For P2 GTAW stainless, apprentices are tested on:[^6]

- **2F horizontal fillet:** tilt torch slightly upward (5-10°), stringer bead technique
- **3F vertical up fillet:** REDUCE amperage 10-15% below flat; slow travel; watch heat build-up carefully

**3F on stainless is a good skill test** — mistakes in heat control show up immediately as discoloration.

---

## Numbers you need to memorize

- **Polarity for stainless GTAW:** DCEN[^1]
- **Shielding gas:** 100% argon (standard); 98% Ar / 2% H₂ for austenitic 300-series only[^1]
- **Amperage:** ~85% of mild-steel amperage for same thickness[^1]
- **Filler for 304/304L:** ER308L[^3]
- **Filler for 316/316L:** ER316L[^3]
- **Filler for dissimilar (SS to CS):** ER309L[^3]
- **Sensitization temp range:** 425-870 °C (800-1600 °F)[^4]
- **Back-purge flow:** 5-10 CFH maintained during root pass[^5]
- **Back-purge pre-flush:** 5-10 minutes before striking arc[^5]
- **Acceptable heat tint (industrial):** silver to straw yellow; dark straw borderline; purple/black REJECT[^4]
- **Cr content needed for stainless behavior:** ≥10.5% Cr in solid solution[^4]
- **304 composition:** 18% Cr, 8% Ni, 0.08% max C[^3]
- **304L composition:** same as 304 with 0.03% max C[^3]
- **316 composition:** 16% Cr, 10% Ni, 2% Mo, 0.08% max C[^3]
- **Never use:** regular Sharpie (chlorides), carbon steel scribe, mixed-metal wire brush

---

## What the textbook doesn't tell you

**Rouge is a real thing.** If you use a wire brush that touched carbon steel on your stainless work, the microscopic iron particles embedded in the surface will oxidize (rust) — this leaves visible orange stains called "rouge." In food processing plants, rouge is a rejection issue and requires acid passivation to remove. Cheap brush = expensive rework.[^5]

**"Sugar" isn't just cosmetic.** The black crystalline oxide on an unpurged root looks bad, but it also destroys corrosion resistance on the process side of the weld — exactly where the pipe contents will attack. In pharmaceutical or food service, sugared root = fail.[^5]

**Straw yellow is fine; dark straw is a warning; blue means slow down.** Learn to read the trail behind your bead. As you weld, glance back at the color — if it's darkening beyond straw, either speed up, reduce amperage, or you need better purge.[^4]

**Argon-hydrogen (98/2) gas for stainless is a pro trick.** The hydrogen makes the arc hotter and cleaner, gives you a wider puddle at the same amperage, and reduces oxidation. **BUT it can ONLY be used on austenitic (300-series) stainless.** On martensitic, ferritic, or duplex stainless, hydrogen causes cracking. Read the fine print before switching gas.[^1]

**No back-purge = short-cut for weekend welding, career-ender for code work.** On any welding you want to do professionally in pipe, pressure vessel, or sanitary work, back-purge is not optional. Learn to set up purge dams cheaply (paper + soluble tape) if you can't purge the whole system.[^5]

**Modern lanthanated tungsten works on both DC (mild steel, stainless) and AC (aluminum).** If your shop has one tungsten to buy, 2% lanthanated (blue) is it — sharpens the same way for all three applications.[^1]

**When welding to code, discoloration standards vary.** ASME sanitary standards (BPE, food/pharma) reject anything past light straw. Structural stainless (ASME B31.1, B31.3) tolerates darker heat tint. Ask which spec applies before you start.[^4]

---

## Diagram

*(SVG to be added: `assets/diagrams/p2-s4-f-stainless-heat-tint-scale.svg` — color chart showing acceptable heat-tint levels: silver / light straw / dark straw / blue / purple / black with "OK / borderline / REJECT" labels)*

*(SVG to be added: `assets/diagrams/p2-s4-f-stainless-back-purge.svg` — cross-section of pipe with purge dam, argon flowing through, weld root protected on underside)*

---

## Key terms

- **Austenitic stainless:** 300-series (Cr-Ni) — most common, non-magnetic, most weldable
- **Sensitization / carbide precipitation:** chromium loss at grain boundaries from prolonged 425-870 °C exposure
- **L-grade (low carbon):** 0.03% max C — resists sensitization
- **Sugaring:** severe root-side oxidation of unpurged stainless welds
- **Back-purge:** inert gas coverage on the underside of a root weld
- **Heat tint / discoloration:** oxide colors on the top surface indicating heat input level
- **Rouge:** iron-particle contamination causing rust stains on stainless surfaces
- **Passivation:** acid treatment to restore the chromium-oxide protective film
- **304 / 316 / 309:** the three main stainless grades apprentices encounter
- **ER308L / ER316L / ER309L:** matching low-carbon fillers

---

## Common exam trap

- **304L is preferred over 304 for welded structures** (lower carbon = less sensitization risk).
- **Sensitization range: 425-870 °C (800-1600 °F).** Questions may give a temperature range and ask if it's in the sensitization zone.
- **ER309L for dissimilar joints (stainless to mild steel), NOT ER308L.** 308L will crack.
- **Back-purge is required for stainless pipe root passes.** "Optional" is wrong.
- **100% argon for standard stainless GTAW.** CO2 or Ar/CO2 mixes are for GMAW/FCAW — they carburize stainless.
- **Cr content for "stainless" behavior:** minimum 10.5% in solid solution.
- **Argon-hydrogen mixes work ONLY on austenitic (300-series) stainless.** Any question that says H₂ mix on martensitic/ferritic/duplex is wrong.
- **Amperage for stainless is LESS than mild steel at same thickness** (~85%). Distractors will say "same" or "higher."
- **Never use a regular Sharpie on stainless** — chlorides cause stress-corrosion cracking.

---

## Practice question preview

**Q:** A welder is fitting up 316L stainless pipe for a pharmaceutical process line. Which of the following practices is REQUIRED for the root pass?

A) Use ER308L filler for better fluidity
B) Back-purge the pipe interior with argon before and during welding
C) Use 100% CO2 shielding gas for deeper penetration
D) Post-heat the weld to 800 °C to relieve stresses

**Correct: B**

**Explanation:** Stainless steel pipe root passes require back-purging with argon to prevent oxidation ("sugaring") of the root, which destroys corrosion resistance on the process-contact surface — critical for pharmaceutical service. A) ER308L is the WRONG filler for 316L — you lose the molybdenum content critical for corrosion resistance; must use ER316L; C) 100% CO2 is NEVER used on stainless — it carburizes the weld and destroys stainless behavior; D) Post-heating to 800 °C would put the metal squarely in the sensitization range (425-870 °C), causing chromium carbide precipitation and intergranular corrosion.

**Red Seal mapping:** D-15.01 (Selects GTAW gas, equipment and consumables), D-15.04 (Performs weld using GTAW equipment)

---

[^1]: [Miller Electric — Guidelines for Stainless Steel GTAW](https://www.millerwelds.com/resources/article-library/how-to-tig-weld-stainless-steel); DC selection, amperage tables, argon-hydrogen mix guidance
[^2]: [Lincoln Electric — Stainless Steel Welding Guide](https://www.lincolnelectric.com/en/education-center/welding-education/stainless-steel-welding-guide); filler selection, heat input control, technique
[^3]: [AWS A5.9 — Specification for Bare Stainless Steel Welding Electrodes and Rods](https://pubs.aws.org/p/1044/a59a59m2017-specification-for-bare-stainless-steel-welding-electrodes-and-rods); ER308L, ER316L, ER309L classifications, chemistry, application matching
[^4]: [TWI Global — Welding of Austenitic Stainless Steels](https://www.twi-global.com/technical-knowledge/job-knowledge/welding-of-austenitic-stainless-steel-part-1-103); carbide precipitation mechanism, heat-tint acceptance, sensitization prevention strategies
[^5]: [ESAB — Welding of Stainless Steels Handbook](https://esab.com/us/nam_en/education/blog/stainless-steel-welding/); back-purge procedures, sugaring prevention, cross-contamination and rouge
[^6]: [AIT Welder Curriculum Guide 012 (2026)](https://tradesecrets.alberta.ca/SOURCES/PDFS/CURRICULUM_GUIDES/012_OUTLINE.PDF), Period 2 Section 4 Topic F — 2F and 3F positions on stainless steel gauge plate
