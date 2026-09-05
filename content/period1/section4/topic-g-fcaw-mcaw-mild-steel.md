---
id: p1-s4-g
period: 1
section: 4
section_title: Gas Metal Arc Welding (GMAW), Flux-Cored Arc Welding (FCAW), Metal Cored Arc Welding (MCAW), and Submerged Arc Welding (SAW)
topic_letter: G
topic_title: FCAW and MCAW on Mild Steel
hours: 30
weight_pct: 12
outcome: >
  Upon successful completion, learners will be able to perform FCAW and demonstrate
  MCAW welding on mild steel in flat, horizontal, and vertical positions.
objectives:
  - Perform stringer and weave beads in the flat and horizontal positions using FCAW on mild steel plate.
  - Perform 1F, 2F, 3F, and 4F fillet welds on mild steel using FCAW.
  - Demonstrate MCAW technique on mild steel and describe how it differs from FCAW and GMAW.
  - Identify FCAW/MCAW-specific defects and their causes.
red_seal_mapping:
  - D-14.01 (Selects FCAW, MCAW and GMAW gas, equipment and consumables)
  - D-14.02 (Sets up FCAW, MCAW and GMAW equipment)
  - D-14.03 (Sets operating parameters for FCAW, MCAW and GMAW)
  - D-14.04 (Performs weld using FCAW, MCAW and GMAW equipment)
citations:
  - source: AWS A5.20 — Specification for Carbon Steel Electrodes for Flux Cored Arc Welding
    ref: E71T-1, E71T-11 classification, mechanical properties, shielding requirements
    url: https://pubs.aws.org/p/1147/a520a5-20m2015-specification-for-carbon-steel-electrodes-for-flux-cored-arc-welding
  - source: AWS A5.18 — Specification for Carbon Steel Electrodes and Rods for Gas Shielded Arc Welding
    ref: E70C (metal-cored) classification
    url: https://pubs.aws.org/p/1141/a518a518m2005-specification-for-carbon-steel-electrodes-and-rods-for-gas-shielded-arc-welding
  - source: Lincoln Electric — Innershield NR-211-MP data sheet & Procedure Handbook of Arc Welding
    ref: Self-shielded FCAW parameters, DCEN polarity, technique
    url: https://www.lincolnelectric.com/en/education-center/welding-education/procedure-handbook
  - source: ESAB — Dual Shield II 71 Ultra data sheet
    ref: Gas-shielded FCAW parameters, DCEP polarity, 75/25 or 100% CO2
    url: https://esab.com/us/nam_en/products-solutions/filler-metals/mild-steel-wires/dual-shield-ii-71-ultra/
  - source: Miller Electric — Guidelines for Flux Cored Arc Welding
    ref: FCAW-G vs FCAW-S parameter selection, deposition rates
    url: https://www.millerwelds.com/resources/article-library/flux-cored-arc-welding-fcaw-guidelines
  - source: CSA W59 — Welded Steel Construction (2018)
    ref: Clause 4 (workmanship for FCAW/MCAW), Clause 12 (welder qualification, positions)
    url: https://www.csagroup.org/store/product/CSA%20W59%3A18/
  - source: AIT Welder Curriculum Guide 012 (2026), Period 1 Section 4 Topic G
    ref: pp. 22-24
    url: https://tradesecrets.alberta.ca/SOURCES/PDFS/CURRICULUM_GUIDES/012_OUTLINE.PDF
---

# FCAW and MCAW on Mild Steel

FCAW is what puts food on a lot of structural welders' tables. It deposits metal 2-3× faster than SMAW at similar quality, works outdoors in wind (self-shielded), and can be run all-position with the right wire. If you plan to work structural steel, pipeline tie-ins, or heavy fabrication in Alberta, you'll spend more time behind an FCAW gun than any other process.

---

## FCAW vs GMAW vs MCAW — the family

All three are wire-fed processes. What makes them different is what's inside the wire:[^1]

| Process | Wire | Shielding | Slag | Typical use |
|---|---|---|---|---|
| **GMAW** | Solid | Gas (Ar/CO2 mixes) | None | Sheet metal, thin plate, clean shop conditions |
| **FCAW-G** (gas-shielded) | Tubular w/ flux | Gas + flux | Yes | Structural, pipe, heavy plate (indoors) |
| **FCAW-S** (self-shielded) | Tubular w/ flux | Flux only | Yes | Structural in wind/outdoors, field work |
| **MCAW** | Tubular w/ metal powder | Gas (Ar/CO2 mixes) | Minimal | High deposition on clean steel, robotic applications |

**Key insight:** FCAW's tubular wire lets you cram more into the electrode than solid wire — deoxidizers, arc stabilizers, alloy additions, gas-forming compounds. That's why FCAW is more forgiving of dirty steel than GMAW.

---

## Polarity — get this wrong and you'll wonder why nothing works

This trips apprentices constantly:[^3][^4]

| Process | Polarity | Why |
|---|---|---|
| GMAW (all) | **DCEP** (electrode positive / reverse polarity) | Cathodic cleaning of workpiece, stable arc |
| FCAW-G (E71T-1) | **DCEP** | Same as GMAW — flux formulated for it |
| FCAW-S (E71T-11) | **DCEN** (electrode negative / straight polarity) | Flux compounds engineered for negative electrode |
| MCAW (E70C-6M) | **DCEP** | Same as GMAW |

**Read the wire's data sheet. Some specialty FCAW wires break these rules.**

---

## Common mild-steel FCAW/MCAW wires you'll actually use

### E71T-1 (gas-shielded, most common structural)[^1][^4]
- **Meaning:** E71**T**-1 → E = electrode, 71 = 70 000 psi tensile, T = tubular, 1 = designator (all-position, gas-shielded, rutile flux)
- **Shielding gas:** 75/25 Ar/CO2 (better bead, less spatter) OR 100% CO2 (deeper penetration, more spatter, cheaper)
- **Polarity:** DCEP
- **Typical amperage:** 150-280 A for 0.045" wire; 200-350 A for 1/16"
- **Typical voltage:** 22-28 V for short arc, 24-32 V for spray-like transfer
- **Best for:** structural steel, all-position, indoor/shop work

### E71T-11 (self-shielded, field work)[^3]
- **Meaning:** Same tensile/all-position, but "11" designator = self-shielded, no CO2 gas required
- **Shielding gas:** NONE — the flux does it all
- **Polarity:** DCEN
- **Typical amperage:** 150-250 A for 0.068"; 200-300 A for 5/64"
- **Best for:** field welding in wind, structural repair, situations where a gas cylinder isn't practical

### E70C-6M (MCAW, high deposition on clean steel)[^2]
- **Meaning:** E = electrode, 70 = 70 000 psi tensile, C = composite (metal-cored), 6 = weldability designator, M = mixed gas required
- **Shielding gas:** Ar/CO2 mix (75/25 or 90/10) — REQUIRED
- **Polarity:** DCEP
- **Best for:** high-productivity fillet welds on clean steel, robotic welding
- **Watch out:** intolerant of mill scale and rust — clean the steel first

---

## The gun angles that make or break your weld

For a typical FCAW-G stringer bead on plate (flat position, right-handed welder):[^5]

- **Travel angle:** 5-15° drag (electrode angled back toward the weld you just made). FCAW is a **drag process** — pull don't push. Pushing traps slag under the puddle → inclusions.
- **Work angle:** 90° for a butt joint bead-on-plate, 45° for a T-joint fillet
- **Contact-tip-to-work distance (CTWD):** 3/4" (19 mm) is the standard for 0.045" wire. Too short = spatter/burnback. Too long = poor gas coverage + porosity + arc wander.
- **Travel speed:** slow enough that the arc stays at the leading edge of the puddle. If you see the arc riding on top of the puddle, speed up.

For **E71T-11 (self-shielded, DCEN)**, use a slightly steeper drag angle (15-25°) and a longer CTWD (3/4" to 1-1/4" depending on wire diameter) — the longer stick-out preheats the wire and improves the flux column.[^3]

---

## Positions: 1F, 2F, 3F, 4F (fillet welds)

FCAW is genuinely all-position with the right wire. The technique changes:[^6]

| Position | AWS designation | Technique notes |
|---|---|---|
| Flat | 1F | Drag angle, stringer or slight weave, easy — start here to dial in parameters |
| Horizontal | 2F | Point gun slightly upward (10-15° above horizontal) to counter puddle sag; back-step technique on second pass helps |
| Vertical up | 3F | **REDUCE amperage 10-15%** vs flat. Weave triangular pattern, pause at the toes to prevent undercut. Slow travel. |
| Overhead | 4F | Reduce amperage 15-20%. Tight stringer beads. Puddle stays small (surface tension holds it). Keep the arc short. |

**Vertical up is where E71T-1 shines.** Its flux is engineered so the slag freezes fast, supporting the puddle. You cannot do this cleanly with GMAW short-arc — the slag support is what makes FCAW all-position practical.

---

## Numbers you need to memorize

- **E71T-1 tensile strength:** 70 000 psi (min)[^1]
- **E71T-1 polarity:** DCEP[^1]
- **E71T-11 polarity:** DCEN[^3]
- **E71T-1 shielding gas:** 100% CO2 OR 75/25 Ar/CO2[^1][^4]
- **E71T-11 shielding gas:** NONE (self-shielded)[^3]
- **MCAW polarity:** DCEP[^2]
- **Standard CTWD for 0.045" FCAW-G:** 3/4" (19 mm)[^5]
- **Standard CTWD for FCAW-S:** 3/4" to 1-1/4" (19-32 mm)[^3]
- **Gas flow rate (FCAW-G):** 35-50 CFH (higher than GMAW because larger gun nozzle & drag angle disrupts coverage)[^4][^5]
- **Vertical up amperage reduction:** 10-15% from flat position setting[^5]
- **Deposition rate (FCAW):** typically 2-3× SMAW at similar quality[^5]
- **FCAW drag angle (backhand):** 5-15° for FCAW-G, 15-25° for FCAW-S[^3][^5]

---

## What the textbook doesn't tell you

**"Push or drag" is not optional with FCAW.** Push angle on any flux-cored wire dumps slag ahead of the puddle where the next weld metal traps it. You'll pass visual inspection maybe, but bend or MT/PT the coupon and you'll find slag inclusions every time. **FCAW = drag. Always.**[^5]

**Wire feed problems trace to the drive rolls first.** For solid GMAW wire → V-groove smooth rolls. For all cored wire (FCAW/MCAW) → **U-groove knurled rolls**. Cored wire is softer (it's a tube with powder inside). Smooth V-groove rolls flatten the wire → bird's-nest at the drive.[^4]

**Self-shielded (FCAW-S) doesn't like joint prep angles that are too tight.** The flux column needs room to establish. Open your bevels a bit wider than you would for GMAW/FCAW-G — typically 45-60° included angle for FCAW-S, vs. 30-45° for GMAW.[^3]

**FCAW-S in confined spaces is a fume nightmare.** Self-shielded wires produce more visible smoke than gas-shielded because the flux is doing all the work. Use LEV (local exhaust ventilation) or supplied-air respirators. Manganese and CO exposure limits get exceeded fast.[^7]

**When you can't figure out why beads look bad**, check in this order:
1. Polarity (E71T-1 = DCEP, E71T-11 = DCEN — swap and you'll get a snarly, spattery, useless arc)
2. Drive rolls (wrong type, worn, tension incorrect)
3. Liner (kinked or full of debris)
4. CTWD (usually too long → porosity/undercut, or too short → burnback)
5. Voltage-amperage relationship (too low volts for the amps → sputtery, too high → wide flat bead + spatter)

---

## Diagram

*(SVG to be added: `assets/diagrams/p1-s4-g-fcaw-gun-angle.svg` — cutaway showing gun at 15° drag angle, CTWD labeled 3/4", nozzle-to-work distance labeled, wire stick-out visible past contact tip, weld puddle behind arc with slag forming on top)*

*(SVG to be added: `assets/diagrams/p1-s4-g-fcaw-positions.svg` — four small figures showing 1F/2F/3F/4F fillet weld positions with gun orientation for each)*

---

## Common FCAW/MCAW defects and their causes

| Defect | Likely cause | Fix |
|---|---|---|
| **Porosity (surface + subsurface)** | Insufficient gas coverage; wind; dirty steel; CTWD too long; contaminated shielding gas | Increase gas flow to 40+ CFH; shield from wind; clean base metal; reduce CTWD; check gas line for leaks |
| **Slag inclusions** | Push angle (should be drag); previous bead not cleaned; travel too fast | Switch to drag angle; wire brush/grind between passes; slow down |
| **Worm tracks (surface porosity trails)** | Trapped moisture in flux; excessive voltage; wet wire | Store wire in dry area; reduce voltage; dry the wire (some manufacturers allow oven at 250°F max — check data sheet) |
| **Lack of fusion (sidewall)** | Amperage/voltage too low; travel too fast; wrong gun angle; joint too tight | Increase parameters per data sheet; slow down; verify 5-15° drag; open the joint |
| **Excessive spatter** | Voltage too high for amperage; CTWD too short; wrong polarity | Lower voltage 1-2 V; increase CTWD to 3/4"; verify polarity matches wire |
| **Burnback (wire fuses to contact tip)** | CTWD too short; wire feed stalled; worn contact tip | Increase CTWD; check drive tension and liner; replace contact tip |

---

## Key terms

- **FCAW-G:** Flux-Cored Arc Welding, Gas-shielded (uses external shielding gas + flux)
- **FCAW-S:** Flux-Cored Arc Welding, Self-shielded (flux does all shielding — no gas)
- **MCAW:** Metal-Cored Arc Welding (tubular wire filled with metal powder; requires gas)
- **DCEP:** Direct Current Electrode Positive (reverse polarity)
- **DCEN:** Direct Current Electrode Negative (straight polarity)
- **CTWD:** Contact Tip to Work Distance
- **Drag (backhand) angle:** electrode tilted so the arc trails behind the direction of travel
- **Push (forehand) angle:** electrode tilted so the arc leads the direction of travel
- **Slag:** solidified flux residue on top of the weld
- **Worm tracks:** surface porosity trails caused by moisture in flux
- **Rutile flux:** titanium-oxide-based flux giving smooth arc + easy slag removal (E71T-1)
- **Bird's nest:** wire tangling at the drive rolls (usually from wrong roll type or excessive tension)

---

## Common exam trap

- **E71T-1 polarity is DCEP; E71T-11 polarity is DCEN.** Test writers reverse these constantly. If you memorize nothing else, memorize this pair.
- **FCAW is a drag process.** Any answer that says "push" or "forehand" for FCAW is wrong.
- **MCAW is NOT the same as FCAW.** MCAW wire has *metal* powder, not flux. It requires shielding gas (like GMAW) and produces minimal slag. Answers that lump MCAW in with "cored wires require no gas" are wrong.
- **Vertical up = reduce amperage.** Distractors will offer "increase amperage for better penetration on vertical up" — wrong. Reduce amperage 10-15% and let the arc do the work.
- **U-groove knurled rolls for cored wire; V-groove smooth rolls for solid wire.** Reversing them ruins the wire feed.
- **CTWD for FCAW-S is LONGER than FCAW-G** — the extra stick-out preheats the wire and improves the flux column.
- **Gas flow rate for FCAW is HIGHER than GMAW** (35-50 CFH vs 25-35 CFH) — larger nozzle, drag angle disrupts coverage.

---

## Practice question preview

**Q:** A structural welder is running vertical-up fillet welds outdoors on a windy job site using 0.068" self-shielded flux-cored wire. Which of the following parameter changes is MOST likely to prevent porosity?

A) Switch to 100% CO2 shielding gas
B) Increase amperage 15% above the flat-position setting
C) Reduce contact-tip-to-work distance to 1/2"
D) Verify the wire is E71T-11 (self-shielded) and running DCEN

**Correct: D**

**Explanation:** The scenario says "self-shielded flux-cored wire" outdoors — the correct wire is E71T-11 or similar self-shielded, which requires DCEN polarity. If the welder accidentally has DCEP set (correct for gas-shielded FCAW), the arc will be erratic and porosity is virtually guaranteed regardless of other settings. (A) Adding CO2 to a self-shielded wire is wasted — the flux is doing the shielding; (B) You REDUCE amperage on vertical up, not increase; (C) Reducing CTWD on FCAW-S actually WORSENS things — self-shielded wires need longer stick-out (3/4"-1-1/4") for the flux column to establish properly.

**Red Seal mapping:** D-14.03 (Sets operating parameters for FCAW, MCAW and GMAW)

---

[^1]: [AWS A5.20 — Specification for Carbon Steel Electrodes for Flux Cored Arc Welding](https://pubs.aws.org/p/1147/a520a5-20m2015-specification-for-carbon-steel-electrodes-for-flux-cored-arc-welding); E71T-1 classification details, mechanical property requirements
[^2]: [AWS A5.18 — Carbon Steel Electrodes and Rods for Gas Shielded Arc Welding](https://pubs.aws.org/p/1141/a518a518m2005-specification-for-carbon-steel-electrodes-and-rods-for-gas-shielded-arc-welding); E70C-6M metal-cored classification
[^3]: [Lincoln Electric — Innershield NR-211-MP data sheet](https://www.lincolnelectric.com/en/education-center/welding-education/procedure-handbook) and Procedure Handbook of Arc Welding, self-shielded FCAW section; DCEN polarity requirement and stick-out guidance
[^4]: [ESAB — Dual Shield II 71 Ultra data sheet](https://esab.com/us/nam_en/products-solutions/filler-metals/mild-steel-wires/dual-shield-ii-71-ultra/); gas-shielded FCAW parameter selection, DCEP polarity, drive roll requirements
[^5]: [Miller Electric — Guidelines for Flux Cored Arc Welding](https://www.millerwelds.com/resources/article-library/flux-cored-arc-welding-fcaw-guidelines); technique guidance including drag angle, CTWD, deposition rate comparisons
[^6]: [CSA W59:18 — Welded Steel Construction](https://www.csagroup.org/store/product/CSA%20W59%3A18/), Clause 12 (welder qualification, positions 1F-4F, 1G-4G), Clause 4 (workmanship for FCAW/MCAW)
[^7]: [Alberta OHS Code, Part 4 (Chemical Hazards) and Part 8 (Entry into Confined Space)](https://open.alberta.ca/publications/occupational-health-and-safety-code); FCAW-S fume exposure considerations, Mn and CO limits per Schedule 1 Table 2
