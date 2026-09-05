---
id: p3-s2-f
period: 3
section: 2
section_title: Properties of Metals
topic_letter: F
topic_title: Destructive Testing (DT)
hours: 4
weight_pct: 2
outcome: >
  Upon successful completion, learners will be able to identify and describe destructive
  testing methods used in welder qualification and procedure qualification.
objectives:
  - Identify types of DT used in welding qualification.
  - Describe DT methods including tensile, bend, impact, macroetch, and hardness tests.
red_seal_mapping:
  - A-5.01 (Performs quality inspection)
  - A-4.01 (Uses documentation and reference material)
  - D-13.04 (Performs weld using SMAW equipment)
citations:
  - source: ASME Boiler and Pressure Vessel Code Section IX — Welding Qualifications
    ref: QW-150 (tensile tests), QW-160 (bend tests), QW-170 (impact tests), QW-180 (fillet weld tests)
    url: https://www.asme.org/codes-standards/find-codes-standards/bpvc-ix-boiler-pressure-vessel-code-section-ix-welding-brazing
  - source: CSA W59 — Welded Steel Construction (2018)
    ref: Clause 12 (welder qualification test requirements), bend test acceptance criteria
    url: https://www.csagroup.org/store/product/CSA%20W59%3A18/
  - source: ASTM E8/E8M — Standard Test Methods for Tension Testing of Metallic Materials
    ref: Tensile test procedure, specimen geometry, yield and tensile strength measurement
    url: https://www.astm.org/e0008_e0008m-22.html
  - source: ASTM E23 — Standard Test Methods for Notched Bar Impact Testing
    ref: Charpy V-notch test procedure, specimen dimensions, test temperature requirements
    url: https://www.astm.org/e0023-23a.html
  - source: Lincoln Electric — Procedure Handbook of Arc Welding
    ref: Welder qualification test procedures, bend test interpretation, macroetch technique
    url: https://www.lincolnelectric.com/en/education-center/welding-education/procedure-handbook
---

# Destructive Testing (DT)

When you run a qualification test coupon, it gets cut up, bent, pulled apart, and hit with a hammer. That's destructive testing — the engineering proof that your procedure and your technique produce welds that meet minimum mechanical requirements. Understanding what each test measures helps you understand what failure modes exist in your welds, and why the WPS specifies what it specifies.

---

## Why Destructive Testing Exists

DT provides information that NDT cannot give:[^1]

| DT provides | NDT provides |
|---|---|
| Tensile strength measurement | Defect detection |
| Ductility (elongation, bend angle) | Defect location |
| Toughness (Charpy impact) | Defect characterization |
| Hardness (cracking risk indicator) | Surface/near-surface condition |
| Microstructure (macroetch) | Volumetric density of metal |

**DT always destroys the test piece.** The coupon used for DT cannot be returned to service. This is why qualification testing uses separate coupons welded under the same conditions as production, not samples cut from production welds.

---

## Tensile Test (Tension Test)

The tensile test measures the strength of the weld and base metal combination.[^3][^5]

### What is tested

A specimen is machined from the qualification coupon, usually transverse (perpendicular) to the weld axis. The specimen includes the weld metal, both HAZ zones, and base metal on each side.

The specimen is loaded in a tensile testing machine until fracture.

### Key measurements

| Measurement | Definition |
|---|---|
| **Yield strength** | The stress at which the specimen begins to deform plastically (permanently) — the "elastic limit" |
| **Ultimate tensile strength (UTS)** | The maximum stress the specimen bears before fracture |
| **Elongation** | The percentage increase in gauge length after fracture — a measure of ductility |
| **Reduction in area** | The percentage reduction in cross-sectional area at the fracture — another ductility measure |

### ASME Section IX tensile test acceptance[^1]

For welder performance qualification (QW-150):
- The minimum tensile strength of the test specimen must be **not less than the minimum specified tensile strength of the base metal being welded**
- If fracture occurs in the weld metal: the fracture must be ductile (not brittle) — tensile strength must still meet specification
- If fracture occurs in the base metal: the weld is accepted regardless of strength (base metal is the weakest point — the weld is stronger)

**Fracture location matters:** a brittle fracture in the weld metal at a value below minimum UTS = fail. A ductile fracture anywhere at or above minimum UTS = pass.[^1]

---

## Bend Test

The bend test is the most common welder qualification test. It assesses weld ductility and fusion.[^1][^2][^5]

### Types of bend test

| Test | Specimen orientation | What it stresses |
|---|---|---|
| **Root bend** | Root of weld on the tension (outer) side of the bend | Root penetration and root fusion |
| **Face bend** | Cap of weld on the tension side | Surface layer ductility and fusion |
| **Side bend** | Specimen bent "edge-on" (the cross-section of the weld is on the tension side) | Full weld section ductility, transverse fusion |

**Side bends are required for material > 19 mm (3/4") thick** because the root and face may only represent the outer layers of a thick weld. Side bends test the full cross-section.[^1]

### Bending procedure (guided bend test — ASME Section IX)[^1]

1. Machine the specimen to required dimensions (width, thickness, length per QW-462)
2. Remove weld reinforcement flush — the cap and root faces are ground flush with base metal
3. Place in a jig — the specimen is bent around a mandrel (a pin or die of specified diameter) using a guided wrap-around bending machine
4. Bend to 180° (or the required angle for the specific code)

### Acceptance criteria (ASME Section IX)[^1]

After bending, the tension (outer) surface of the specimen is examined:

- **No single crack or open defect greater than 3 mm (1/8") in any direction**
- **No aggregate of cracks/defects greater than 9 mm (3/8")** on the tension surface
- Corner cracks (at the edges of the specimen) are ignored **unless** they are accompanied by obvious porosity, slag inclusion, or other defect

**What a failed bend test looks like:**
- **Cold lap / overlap:** the cap face bends and the overlap at the toe tears open — the fusion wasn't there
- **Incomplete root penetration:** the root face opens up like a seam when the root-bend specimen is pulled on the tension side
- **Porosity clusters:** a line of pores becomes a crack when stressed
- **Slag inclusions:** rigid slag entrapped in the weld tears open when ductile weld metal deforms around it

### Bend die dimensions (ASME Section IX QW-466)[^1]

For P-1 (carbon steel) qualification coupons (t ≤ 19 mm):
- Mandrel diameter: 4t (4 × specimen thickness) for guided bend
- Specimen width: typically 38 mm (1-1/2") for face/root bend, or t + 25 mm for side bend

*Note: the actual mandrel diameter and jig dimensions are specified in ASME Section IX QW-466. Always verify for the applicable P-number and material.*

---

## Impact Test — Charpy V-Notch (CVN)

The Charpy V-notch test measures toughness — the ability of the material to absorb energy before fracturing, especially at low temperatures.[^4][^5]

### Why toughness matters

A weld may have adequate tensile strength but fracture in a brittle manner under impact loading, especially in cold weather. Brittle fracture in a pressurized pipeline or vessel is catastrophic. Low-temperature toughness requirements (CVN) are specified for Arctic service, low-temperature process equipment, and seismic structures.

### Charpy test procedure[^4]

1. A notched specimen (standard: 10 mm × 10 mm × 55 mm) is machined from the weld or HAZ
2. The notch is a V-shape machined to exact dimensions (2 mm deep, 45° angle, 0.25 mm root radius per ASTM E23)
3. The specimen is cooled to the test temperature (e.g., −30 °C, −46 °C, 0 °C, or as specified)
4. A pendulum hammer strikes the specimen at the opposite face of the notch
5. The absorbed energy (in joules) is read from the machine scale

### Acceptance criteria (typical)[^1]

For ASME pressure vessel applications with CVN requirements, the weld metal, HAZ, and base metal specimens must meet the minimum average energy absorbed (Joules) at the specified temperature. The WPS specifies the CVN requirements — they vary by application.

Example: Arctic pipeline typically requires 27 J minimum at −40 °C for the weld metal.

**Sub-size specimens:** if the material is too thin to machine a full 10 mm × 10 mm specimen, sub-size (7.5 × 10 or 5 × 10 mm) specimens may be used with adjusted acceptance criteria.[^4]

### Ductile vs. brittle fracture on Charpy specimens

After testing, the fracture surface reveals the mode:
- **Fibrous/ductile fracture:** dull, gray, torn appearance — high energy absorbed — good
- **Cleavage/brittle fracture:** bright, shiny, crystalline appearance — low energy absorbed — bad
- **Mixed:** percentage of each is reported as "% shear" or "% fibrous"

The DBTT (Ductile-Brittle Transition Temperature) is the temperature range over which the fracture mode shifts from ductile to brittle. Steel must be used above the DBTT for safe service.[^4]

---

## Macroetch Test (Macro Test)

The macroetch test reveals the weld cross-section, including penetration, fusion, and number of passes by etching a polished cross-section with acid.[^5]

### Procedure

1. Cut a cross-section of the weld (perpendicular to the weld axis) using an abrasive saw
2. Machine or grind the cut face flat and smooth — progressively finer grits to 120 or 180 grit
3. Apply etchant (5–10% nitric acid in water, or ammonium persulfate solution) to the polished surface
4. The acid attacks the grain boundaries and HAZ/weld interfaces preferentially, revealing:
   - **Number of weld passes** (each pass as a distinct zone)
   - **Penetration depth and root fusion**
   - **Fusion line shape**
   - **HAZ width**
   - **Porosity, slag inclusions** (visible as voids or light spots)
   - **Undercut, overlap, incorrect bead shape**

### Acceptance criteria (CSA W59)[^2]

No cracks, no lack of fusion, root penetration must be complete — the exact criteria depend on the application and joint category.

**Macroetch is required for:**
- Fillet weld qualification tests (no bend specimen can be taken)
- Procedure qualification plates when full-section evaluation is needed
- First-article production welds in some quality plans

---

## Hardness Testing — Vickers, Brinell, Rockwell

Hardness testing measures resistance to indentation — it correlates to strength, and more importantly, to cracking risk.[^5]

### Why hardness matters in welding

High hardness in the HAZ = high strength martensite = high risk of hydrogen-induced cracking and brittle fracture in service. Most codes limit maximum HAZ hardness:

| Application | Max HAZ hardness (typical) |
|---|---|
| General structural (CSA W59) | 350 HV (Vickers) |
| Pressure vessel (ASME VIII) | 200–248 HBW (Brinell) |
| Pipeline (API 1104) | 275–325 HV depending on sour service requirements |

### Hardness scales[^5]

| Scale | Method | Force / Indenter | Converts to |
|---|---|---|---|
| **Vickers (HV)** | Diamond pyramid indenter — measures diagonal of square impression | 1–120 kg force | Precise, used for weld/HAZ mapping |
| **Brinell (HBW)** | Tungsten carbide ball — measures diameter of round impression | 500 or 3000 kg | Large-area average, used for plate and forgings |
| **Rockwell (HRC, HRB)** | Diamond cone (C scale) or ball (B scale) | Variable preload + test load | Fast read on machine — HRC for hardened steel, HRB for softer materials |

**Vickers is the most useful for weld qualification** because the small indent allows measurements in the HAZ, weld metal, and base metal individually — mapping hardness across the weld cross-section.[^5]

### Hardness conversion (approximate)[^5]

| Vickers (HV) | Brinell (HBW) | Rockwell (HRC) |
|---|---|---|
| 200 | 190 | — (too soft for C scale) |
| 250 | 238 | 22 |
| 300 | 284 | 29 |
| 350 | 331 | 36 |
| 400 | 378 | 40 |

*Note: conversion tables are approximate — always refer to ASTM E140 for precise conversions.[^5]*

---

## Fillet Weld Break Test

For fillet weld qualification (instead of groove bend tests), the fillet weld is tested by bending or loading until fracture:[^1]

- The test piece is bent or loaded so the weld root is in tension
- Acceptance: the fracture should occur in the base metal (not through the weld) OR if through the weld, the fracture surface must show no cracks, lack of fusion, or incomplete penetration that exceeds code limits
- Macroetch of the cross-section is also required

---

## Numbers you need to memorize

- **Charpy V-notch specimen size (standard):** 10 mm × 10 mm × 55 mm[^4]
- **Charpy notch:** 2 mm deep, 45° angle, 0.25 mm root radius (ASTM E23)[^4]
- **Bend test acceptance (ASME IX):** no single crack > 3 mm; no aggregate > 9 mm[^1]
- **Side bends required:** for t > 19 mm (3/4")[^1]
- **Max HAZ hardness (general structural, CSA W59):** 350 HV[^2]
- **Max HAZ hardness (pressure vessel, ASME VIII):** ~248 HBW typical[^1]
- **Tensile test acceptance:** fracture must be at or above minimum specified UTS of base metal[^1]
- **Guided bend mandrel:** 4t for P-1 carbon steel qualification coupons[^1]

---

## What the textbook doesn't tell you

**The bend test reveals what the eye cannot.** A weld that looks perfect on the outside — smooth cap, no undercut, good color — can fail a face bend test by cracking at an overlap where the toe looked fused but wasn't. The bend test is a brutally honest mechanical inspector. If it cracks, it wasn't fused.[^5]

**Etch the macroetch slowly.** Too aggressive etching (strong acid, long time) destroys fine details. Etch gently, rinse, evaluate, re-etch if needed. A well-etched macrosection clearly shows each pass, the HAZ, and the fusion line. A over-etched surface shows nothing but a rough pit.[^5]

**High Vickers hardness on a HAZ = "check your preheat."** If a hardness traverse of the qualification coupon shows 380 HV in the CGHAZ and the WPS specified 93 °C preheat, something went wrong — either the preheat wasn't reached, cooling was too fast, or the CE is higher than expected. Investigate before the production welds crack in service.[^2]

**The Charpy test is temperature-specific.** A weld that absorbs 80 J at room temperature may absorb only 15 J at −30 °C. Arctic service equipment must be tested at the actual service temperature — not at room temperature. Never assume room-temperature toughness equals low-temperature toughness.[^4]

---

## Diagram

*(SVG to be added: `assets/diagrams/p3-s2-f-bend-test-types.svg` — three side-by-side diagrams showing: root bend (root in tension), face bend (face in tension), side bend (cross-section in tension) — each with arrows showing bend direction and the weld cross-section orientation)*

*(SVG to be added: `assets/diagrams/p3-s2-f-charpy-specimen.svg` — 3D diagram of Charpy V-notch specimen with dimensions: 55 mm length, 10×10 mm cross-section, 2 mm notch depth, V-notch geometry — also showing the pendulum strike direction)*

*(SVG to be added: `assets/diagrams/p3-s2-f-macroetch-cross-section.svg` — etched cross-section of a multi-pass groove weld showing: individual passes as distinct zones, HAZ outline, fusion line, base metal — correctly labeled)*

---

## Key terms

- **DT (Destructive Testing):** mechanical testing that destroys the test specimen to measure material properties
- **Tensile test:** test measuring yield strength, UTS, elongation — specimen pulled to fracture
- **UTS (Ultimate Tensile Strength):** the maximum stress the test specimen bears before fracture
- **Bend test:** test of weld ductility and fusion — specimen bent 180° on a mandrel and examined for cracks
- **Root bend:** bend test with the root of the weld on the tension (outer) side
- **Face bend:** bend test with the weld cap on the tension side
- **Side bend:** bend test with the weld cross-section on the tension side — for thick material
- **Charpy V-notch (CVN):** impact test measuring toughness (energy absorbed before fracture) at specified temperature
- **DBTT (Ductile-Brittle Transition Temperature):** the temperature range at which steel shifts from ductile to brittle fracture mode
- **Macroetch:** etching a polished weld cross-section with acid to reveal pass structure, fusion, and defects
- **Vickers hardness (HV):** hardness measured by diamond pyramid indentation — small, precise, maps across weld zones
- **Brinell hardness (HBW):** hardness measured by ball indentation — average over larger area
- **Rockwell hardness (HRC/HRB):** depth-based hardness test — fast readout, used in manufacturing QC

---

## Common exam trap

- **Root bend = root is in TENSION (on the outside of the bend)** — not compression. The tension side cracks if fusion is absent.
- **Side bends required for t > 19 mm** — not > 25 mm and not > 12 mm.
- **Bend test crack limit: 3 mm (1/8") single; 9 mm (3/8") aggregate** — these numbers appear exactly in ASME IX and the exam will test whether you know both limits.
- **Charpy tests a specific temperature** — the test temperature is part of the test, not just the impact value. A specimen tested at room temperature tells you nothing about service at −40 °C.
- **Vickers, not Brinell, is used for HAZ mapping** — Brinell's ball is too large to distinguish HAZ from weld metal from base metal in small regions.
- **Tensile test acceptance:** the specimen must fail AT OR ABOVE minimum specified UTS. Failing below minimum UTS = fail regardless of fracture location.

---

## Practice question preview

**Q:** A welder's 3G qualification test plate is cut into specimens for bend testing. The root bend specimen, after 180° bending, shows a single crack 4 mm long on the tension surface, centered in the weld metal. What is the test result?

A) Pass — corner cracks are exempt from the 3 mm limit  
B) Pass — the aggregate crack length must exceed 9 mm to fail  
C) Fail — a single crack exceeding 3 mm (1/8") in any direction is rejectable  
D) Pass — weld metal cracking is acceptable; only base metal cracks cause failure

**Correct: C**

**Explanation:** ASME Section IX QW-163 requires that no single crack or defect on the tension surface of a bend test specimen exceed 3 mm (1/8") in any direction. A 4 mm crack exceeds this limit regardless of whether it is in the weld metal, HAZ, or base metal. The 9 mm aggregate limit is a secondary criterion — ANY single defect exceeding 3 mm is a fail, even if it's the only crack. Option A is wrong — the corner crack exemption applies to cracks originating at the specimen edges, not to cracks in the weld metal interior.

**Red Seal mapping:** A-5.01 (Performs quality inspection)

---

[^1]: [ASME Boiler and Pressure Vessel Code Section IX — Welding Qualifications](https://www.asme.org/codes-standards/find-codes-standards/bpvc-ix-boiler-pressure-vessel-code-section-ix-welding-brazing); QW-150 (tensile tests, acceptance), QW-160 (bend tests, types, acceptance criteria), QW-163 (crack limits 3mm/9mm), QW-466 (guided bend dimensions, mandrel 4t)
[^2]: [CSA W59 — Welded Steel Construction (2018)](https://www.csagroup.org/store/product/CSA%20W59%3A18/); Clause 12 (welder qualification requirements), hardness limits 350 HV for structural
[^3]: [ASTM E8/E8M — Standard Test Methods for Tension Testing of Metallic Materials](https://www.astm.org/e0008_e0008m-22.html); tensile test procedure, specimen geometry, yield strength by offset method, UTS measurement
[^4]: [ASTM E23 — Standard Test Methods for Notched Bar Impact Testing](https://www.astm.org/e0023-23a.html); Charpy V-notch specimen dimensions (10×10×55 mm), notch geometry (2mm deep, 45°, 0.25mm radius), test temperature requirements, ductile-brittle fracture surface interpretation
[^5]: [Lincoln Electric — Procedure Handbook of Arc Welding](https://www.lincolnelectric.com/en/education-center/welding-education/procedure-handbook); macroetch technique, hardness scales (Vickers/Brinell/Rockwell), bend test interpretation, fillet break test
