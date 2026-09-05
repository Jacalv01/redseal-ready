---
id: p3-s3-b
period: 3
section: 3
section_title: Drafting, Drawings and Specifications
topic_letter: B
topic_title: Pressure Vessel Drawings
hours: 16
weight_pct: 7
outcome: >
  Upon successful completion, learners will be able to analyze, identify, and interpret
  pressure vessel drawings including vessel components, code-required data, mill
  certifications, and vessel drawings.
objectives:
  - Identify external and internal vessel components.
  - Identify material compositions as per code requirements on mill certification.
  - Interpret vessel drawings.
red_seal_mapping:
  - A-4.01 (Uses documentation and reference material)
  - A-4.02 (Interprets drawings and welding symbols)
  - B-8.01 (Prepares materials)
  - B-8.02 (Fits components for welding)
citations:
  - source: ASME Boiler and Pressure Vessel Code Section VIII Division 1
    ref: UG-25 (vessel components), UG-77 to UG-90 (materials), UG-125 (required markings), Appendix 1 (nozzle design)
    url: https://www.asme.org/codes-standards/find-codes-standards/bpvc-viii-1-boiler-pressure-vessel-code-section-viii-division-1
  - source: CSA B51 — Boiler, Pressure Vessel and Pressure Piping Code
    ref: Registration requirements, Inspector obligations, Alberta-specific requirements
    url: https://www.csagroup.org/store/product/CSA%20B51/
  - source: Lincoln Electric — Procedure Handbook of Arc Welding
    ref: Pressure vessel fabrication sequences, joint efficiency, weld joint categories (A, B, C, D)
    url: https://www.lincolnelectric.com/en/education-center/welding-education/procedure-handbook
  - source: ASME B16.5 — Pipe Flanges and Flanged Fittings
    ref: Flange classes (150, 300, 600, 900, 1500, 2500), pressure-temperature ratings, facing types
    url: https://www.asme.org/codes-standards/find-codes-standards/b16-5-pipe-flanges-and-flanged-fittings-nps-through-nps-24-metric-inch-standard
  - source: TWI Global — Job Knowledge: Pressure Vessel Design and Construction
    ref: Vessel heads, nozzles, joint categories, MAWP and MDMT concepts
    url: https://www.twi-global.com/technical-knowledge/job-knowledge/pressure-vessels-043
---

# Pressure Vessel Drawings

Pressure vessels are the most code-regulated welded products in the industry. Every weld is tracked, every welder is qualified to a specific WPS, and every vessel is inspected and registered with provincial authorities before it goes into service. As a welder on pressure vessel work, you are not just welding — you are contributing to a legal safety document. Understanding the drawings is understanding what you're accountable for.

---

## What Makes a Pressure Vessel Different

A pressure vessel is a container designed to hold fluids (gas or liquid) at pressures substantially above or below atmospheric. Under ASME BPVC Section VIII and Alberta's CSA B51:[^1][^2]

- All vessels operating above **103 kPa (15 psi)** internal pressure are typically subject to code requirements
- **Registration:** in Alberta, all pressure vessels must be registered with a Safety Codes Officer (SCO) before being put into service — the vessel has a registration number on the nameplate
- **Inspector:** a commissioned inspector (AI — Authorized Inspector) witnesses key fabrication steps and signs off on the quality control records
- **Nameplate:** every ASME code vessel carries a stamped or welded nameplate (the "ASME U-stamp") with required data

---

## Vessel Components — What You'll See on a Drawing

### Shell

The cylindrical body of the vessel. Fabricated by rolling plate into a cylinder and welding the longitudinal seam (a Category A joint per ASME VIII).[^1]

- **Shell course:** a single rolled cylinder — long vessels may have multiple courses (sections) joined by circumferential (girth) seams
- **Shell thickness:** calculated from the design pressure, material allowable stress, and joint efficiency — the engineer determines this; the fabricator verifies the ordered plate meets spec

### Heads

Heads close the ends of the cylindrical shell. Different head types offer different strength-to-cost ratios:[^1][^5]

| Head type | Shape | Notes |
|---|---|---|
| **Hemispherical** | Perfect half-sphere | Highest pressure capacity per unit thickness — expensive to form |
| **Ellipsoidal (2:1 ellipsoidal)** | Ellipse with major-to-minor ratio of 2:1 | Standard for most ASME vessels — good pressure efficiency |
| **Torispherical (ASME flanged & dished, F&D)** | Spherical crown with a knuckle radius | Less efficient than ellipsoidal but cheaper to form — common in low-pressure service |
| **Flat head** | Flat plate | Simplest to fabricate but requires much thicker plate for the same pressure — used for low pressure, small diameter |
| **Conical** | Cone frustum | Used as transitions between different diameter shells (reducers) |

**Fitting heads to the shell:** head-to-shell joints are Category A (longitudinal) welds if the joint axis is along the vessel axis, or Category B (circumferential) welds if the head meets the shell at a girth seam. Most vessel heads are attached via a girth (circumferential) weld — Category B.[^1]

### Nozzles

Nozzles are openings through the shell or head for process connections — inlet, outlet, manways, pressure gauges, relief valves, thermocouples, etc.[^1]

- **Nozzle types:**
  - Set-in (inserted through a hole in the shell and welded at the shell outside surface — the most common, also called "set-through" or "full penetration")
  - Set-on (welded onto the outside of the shell — partial penetration, limited pressure service)
- **Nozzle reinforcement:** removing metal from the shell to create the nozzle hole reduces the shell's pressure capacity. Reinforcement (pad plate or built-in thickening of the shell or nozzle neck) is required per ASME VIII Appendix 1.
- **Reinforcement pad:** a donut-shaped plate welded around the nozzle on the shell OD. Has a 1/4" NPT telltale hole (visible on drawings) to allow pneumatic testing of the pad-to-shell fillet welds.

### Flanges

Flanges are used for demountable connections — anywhere the vessel needs to be opened for maintenance, or connected to piping that will be removed.[^4]

**ASME B16.5 flange classes and pressure ratings (approximate at 38 °C for carbon steel):**

| Class | Approximate max working pressure |
|---|---|
| **150** | ~1.9 MPa (275 psi) |
| **300** | ~5.1 MPa (740 psi) |
| **600** | ~10.2 MPa (1480 psi) |
| **900** | ~15.3 MPa (2220 psi) |
| **1500** | ~25.5 MPa (3705 psi) |
| **2500** | ~42.6 MPa (6170 psi) |

*Note: exact ratings depend on material and temperature — always verify against the specific B16.5 pressure-temperature table for the material and design temperature.[^4]*

**Flange facing types (shown on vessel and piping drawings):**

| Facing | Description | Use |
|---|---|---|
| **RF (Raised Face)** | Slightly raised ring on the face — the gasket seats on this ring | Most common for refinery and general process |
| **FF (Flat Face)** | Full face — the entire face is the same elevation | Used with cast iron equipment to prevent flange cracking |
| **RTJ (Ring Type Joint)** | Machined groove for a metal ring gasket | High-pressure, high-temperature service |

### Support Structures

- **Saddles:** two curved support structures that wrap around a horizontal vessel — like a cradle
- **Legs:** vertical supports welded to the bottom head of a small vertical vessel
- **Skirt:** a cylindrical shell extension below the bottom head of a large vertical vessel — the most common support for tall towers

---

## ASME VIII Weld Joint Categories

ASME Section VIII classifies welds by their location and orientation:[^1]

| Category | Location | Examples |
|---|---|---|
| **A** | Longitudinal joints in shell, nozzle, or head (running along the axis) | Shell longitudinal seam, nozzle longitudinal seam |
| **B** | Circumferential joints (girth seams) | Shell-to-head welds, shell course-to-course welds, nozzle flanges |
| **C** | Flange-to-shell or flange-to-nozzle joints | Flange attachment to nozzle neck |
| **D** | Nozzle-to-shell or nozzle-to-head connections | Nozzle insert weld, nozzle reinforcement pad welds |

**Why it matters:** joint categories determine the required examination methods, the joint efficiency "E" used in design calculations, and the type of weld (CJP, PJP, or fillet) allowed. Category A and B joints in high-pressure vessels must be CJP groove welds with RT or UT.[^1]

---

## Joint Efficiency (E)

Joint efficiency reflects how much confidence the code has in the weld quality:[^1][^3]

| Examination method | Joint efficiency (E) |
|---|---|
| Full radiographic examination | E = 1.0 |
| Spot radiographic examination | E = 0.85 |
| No radiographic examination | E = 0.70 |

**The design equation for shell thickness:** t = PD / (2SE - 0.2P)

Where:
- t = minimum required wall thickness (mm)
- P = design pressure (MPa)
- D = inside diameter (mm)
- S = allowable stress for the material at design temperature (MPa) — from ASME VIII material tables
- E = joint efficiency

**Higher joint efficiency = thinner wall required = cheaper vessel.** Full radiographic examination is specified to allow E = 1.0, not as a penalty. It saves material cost on large or high-pressure vessels.[^1]

---

## Code-Required Data on Vessel Drawings

Every pressure vessel drawing must include (per ASME VIII UG-125):[^1]

| Required data field | Description |
|---|---|
| **MAWP** | Maximum Allowable Working Pressure — the maximum pressure the vessel may operate at in service |
| **MDMT** | Minimum Allowable Design Metal Temperature — the minimum temperature at which the vessel may be pressurized |
| **Design temperature** | The maximum temperature the vessel is designed for |
| **Material specification** | ASME material spec (e.g., SA-516 Gr. 70 for shell plate) |
| **Shell thickness** | Actual ordered shell thickness (must meet or exceed calculated minimum) |
| **Joint efficiency** | The E value used in the design calculations |
| **Corrosion allowance** | Additional thickness added to account for wall thinning due to corrosion in service |
| **Volume** | Internal volume of the vessel |

**"SA" prefix vs "A" prefix:** ASME material specifications use the "SA" prefix (e.g., SA-516 Gr. 70). This is functionally the same material as ASTM A516 Gr. 70, but the "SA" designation indicates the material has been ordered to ASME requirements including additional testing certifications required for code vessels.[^1]

---

## Reading the Mill Certificate for Code Vessels

For pressure vessel plate, the Mill Test Certificate (MTC) must confirm:[^1]

1. **Heat number:** the traceable batch identifier
2. **Material specification:** must match the vessel drawing exactly — e.g., SA-516 Gr. 70, not A36
3. **Chemistry:** all specified elements (C, Mn, P, S, Si, etc.) within the spec limits
4. **Tensile properties:** actual yield and tensile strength must meet the spec minimums
5. **Impact properties (if required):** Charpy values at the specified temperature — required for MDMT below −29 °C on most carbon steels
6. **ASME certifying statement:** the mill must certify the material was produced and tested in conformance with the ASME material specification — this is the "ASME stamp" on the MTC

**If the MTC doesn't match the drawing specification:** the plate cannot be used for that vessel regardless of its physical appearance. Engineering must approve any substitution.

---

## Interpreting a Pressure Vessel Drawing

A typical pressure vessel drawing set includes:[^5]

### General Arrangement Drawing
Shows:
- Overall dimensions (length, diameter)
- Nozzle locations (with orientation angles from a reference — e.g., "Nozzle A at 0°, Nozzle B at 90°")
- Nozzle sizes and flange ratings (e.g., "N1: 6" 300# RF" = 6-inch nominal, Class 300, raised face)
- Support type and location
- Reference to detail drawings

### Detail Drawings
Show:
- Nozzle weld detail (set-in vs. set-on, weld joint geometry, reinforcement pad)
- Head-to-shell joint detail
- Support attachment details
- Internal component details (baffles, vortex breakers, distribution plates)

### Nozzle Schedule
A table listing every nozzle:
- Nozzle ID (N1, N2, M1 for manways, etc.)
- Service (e.g., "Inlet," "Outlet," "Steam in," "Relief valve")
- Size (NPS — Nominal Pipe Size)
- Rating (ASME B16.5 class)
- Facing (RF, FF, RTJ)
- Projection (how far the nozzle neck extends above the shell OD)

### Weld Map
A drawing (or table) showing:
- Every weld joint identified with a unique weld number
- The WPS that applies to each joint
- The inspection method required (VT, PT, RT, UT)
- The welder who made the weld (filled in during fabrication)

---

## Numbers you need to memorize

- **ASME B16.5 Class 150 approximate MAWP:** 1.9 MPa (275 psi) at 38 °C for carbon steel[^4]
- **ASME B16.5 Class 300 approximate MAWP:** 5.1 MPa (740 psi) at 38 °C[^4]
- **Shell thickness formula:** t = PD / (2SE − 0.2P)[^1]
- **Full RT joint efficiency:** E = 1.0[^1]
- **Spot RT joint efficiency:** E = 0.85[^1]
- **No RT joint efficiency:** E = 0.70[^1]
- **SA-516 Gr. 70:** the most common ASME shell plate specification — min yield 260 MPa, min UTS 485 MPa[^1]
- **ASME U-stamp:** the code nameplate marking indicating the vessel meets ASME Section VIII requirements[^1]

---

## What the textbook doesn't tell you

**The AI (Authorized Inspector) is not your enemy — they're your backup.** The AI witnesses critical inspections: post-weld heat treatment, final hydrostatic test, weld examination. They sign the Manufacturer's Data Report (MDR) that goes on file for the life of the vessel. A vessel that passes AI inspection is legally defensible if it ever fails in service — the records show it was built correctly. Cooperate with the AI; their oversight protects the welder as much as the owner.[^2]

**Nozzle layout angles on the vessel GA drawing are measured from a reference mark on the vessel** — typically the longitudinal seam. "Nozzle A at 0°, Nozzle B at 90°" means: Nozzle B is 90° around the circumference from the reference mark (the longitudinal seam). When fitting nozzles, the vessel must be positioned correctly relative to the reference mark and all nozzle locations verified before welding.[^1]

**MAWP and design pressure are NOT the same.** Design pressure is what the engineer used to calculate required wall thickness. MAWP is calculated from the actual (ordered) plate thickness, which is usually greater than the minimum required — so MAWP is typically HIGHER than design pressure. The nameplate shows MAWP. The relief valve is set at or below MAWP.[^1]

**Corrosion allowance disappears over time.** A vessel designed with 3 mm corrosion allowance starts its life with wall thickness t + 3 mm. As corrosion occurs in service, the 3 mm is consumed. Inspection during maintenance (UT thickness testing) verifies that remaining thickness is still above the minimum calculated value t. When the corrosion allowance is consumed, the vessel must be re-rated or retired.[^5]

---

## Diagram

*(SVG to be added: `assets/diagrams/p3-s3-b-vessel-components.svg` — cutaway isometric of a horizontal pressure vessel showing: shell courses, head types (ellipsoidal shown), nozzles (set-in), manway, reinforcement pad, saddle supports, nameplate location — all components labeled)*

*(SVG to be added: `assets/diagrams/p3-s3-b-head-types.svg` — side-by-side cross-sections of five head types: hemispherical, 2:1 ellipsoidal, torispherical (F&D), flat, conical — each with name, typical use, and relative pressure efficiency noted)*

*(SVG to be added: `assets/diagrams/p3-s3-b-weld-joint-categories.svg` — cylindrical vessel cross-section with: Category A (longitudinal seam), Category B (girth seam), Category C (flange attachment), Category D (nozzle-to-shell) — each labeled in color)*

*(SVG to be added: `assets/diagrams/p3-s3-b-flange-facing-types.svg` — three cross-section profiles of flange faces: RF (raised face), FF (flat face), RTJ (ring type joint groove) — with gasket seating shown on each)*

---

## Key terms

- **ASME BPVC Section VIII:** the ASME code governing pressure vessel design, fabrication, inspection, and testing
- **MAWP (Maximum Allowable Working Pressure):** the maximum pressure at which the vessel may operate in service
- **MDMT (Minimum Design Metal Temperature):** the lowest temperature at which the vessel may be pressurized
- **Shell:** the cylindrical body of the vessel
- **Head:** the end closure of a pressure vessel — hemispherical, ellipsoidal, torispherical, flat, or conical
- **Nozzle:** an opening through the shell or head for process connections
- **Reinforcement pad:** a plate around the nozzle opening compensating for the shell material removed
- **Flange class (ASME B16.5):** a pressure rating designation — 150, 300, 600, 900, 1500, 2500
- **Joint efficiency (E):** the fraction of theoretical stress the weld joint can carry — determined by level of radiographic examination
- **Weld joint category (A, B, C, D):** ASME VIII classification of weld location and orientation
- **SA-516 Gr. 70:** the most common ASME carbon steel plate specification for pressure vessels
- **ASME U-stamp:** the nameplate marking certifying ASME Section VIII compliance
- **Authorized Inspector (AI):** the ASME-commissioned inspector who witnesses fabrication and approves the vessel for code compliance
- **Corrosion allowance:** additional wall thickness added to the design minimum to account for service-life corrosion
- **Saddle:** a support structure for horizontal cylindrical vessels
- **Skirt:** a cylindrical support extension below the bottom head of a tall vertical vessel

---

## Common exam trap

- **MAWP is typically HIGHER than design pressure** — the actual plate thickness exceeds the calculated minimum, so the realized MAWP is higher. Exam questions may imply MAWP = design pressure. They are not the same.
- **"SA" prefix = ASME material spec — "A" prefix = ASTM material spec.** SA-516 Gr. 70 ≠ A516 Gr. 70 for code purposes (though mechanically equivalent). Only SA-designated materials are accepted on ASME code vessels.
- **Joint efficiency E = 1.0 requires FULL radiographic examination** — not spot RT (E = 0.85) and not no RT (E = 0.70). Spot RT does NOT give full credit.
- **Category A = longitudinal seams; Category B = circumferential (girth) seams.** These are frequently reversed in exam distractors.
- **Reinforcement pad telltale hole:** the small hole in the reinforcement pad is NOT for drainage — it's for pneumatic testing of the pad welds. The hole is left open (unplugged) after testing.
- **Flange class 150 is the LOWEST standard rating** — not the highest. Higher class numbers = higher pressure capability.

---

## Practice question preview

**Q:** A pressure vessel drawing specifies a nozzle marked "N3: 4" 600# RF." The nozzle will be attached to the shell using a set-in configuration. Which ASME weld joint category describes the nozzle-to-shell weld?

A) Category A — it is a longitudinal weld in the nozzle neck  
B) Category B — it is a circumferential weld at the nozzle-to-shell junction  
C) Category C — it is a flange-to-nozzle attachment weld  
D) Category D — it is a nozzle connection to the shell or head

**Correct: D**

**Explanation:** ASME BPVC Section VIII classifies the weld connecting a nozzle to the shell or head as Category D. Category A is longitudinal welds (running along the vessel axis) in shells, nozzles, or heads. Category B is circumferential welds (girth seams) joining shell courses, or head-to-shell welds. Category C is welds connecting flanges to nozzle necks. Category D specifically covers the connection of nozzles to shells or heads — whether set-in or set-on configurations.

**Red Seal mapping:** A-4.02 (Interprets drawings and welding symbols)

---

[^1]: [ASME Boiler and Pressure Vessel Code Section VIII Division 1](https://www.asme.org/codes-standards/find-codes-standards/bpvc-viii-1-boiler-pressure-vessel-code-section-viii-division-1); UG-25 (vessel components), UG-77 to UG-90 (material requirements, SA vs A prefix), UG-125 (required nameplate markings: MAWP, MDMT), Appendix 1 (nozzle reinforcement), weld joint categories A/B/C/D, joint efficiency E=1.0/0.85/0.70, shell thickness formula
[^2]: [CSA B51 — Boiler, Pressure Vessel and Pressure Piping Code](https://www.csagroup.org/store/product/CSA%20B51/); registration requirements, Authorized Inspector requirements, Alberta provincial enforcement
[^3]: [Lincoln Electric — Procedure Handbook of Arc Welding](https://www.lincolnelectric.com/en/education-center/welding-education/procedure-handbook); pressure vessel fabrication sequences, joint categories, joint efficiency explanation, weld maps
[^4]: [ASME B16.5 — Pipe Flanges and Flanged Fittings](https://www.asme.org/codes-standards/find-codes-standards/b16-5-pipe-flanges-and-flanged-fittings-nps-through-nps-24-metric-inch-standard); flange classes (150/300/600/900/1500/2500), pressure-temperature ratings, RF/FF/RTJ facing descriptions
[^5]: [TWI Global — Pressure Vessel Design and Construction](https://www.twi-global.com/technical-knowledge/job-knowledge/pressure-vessels-043); head types, nozzle types, corrosion allowance concept, MAWP vs design pressure, inspection in service
