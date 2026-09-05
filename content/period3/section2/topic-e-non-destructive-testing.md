---
id: p3-s2-e
period: 3
section: 2
section_title: Properties of Metals
topic_letter: E
topic_title: Non-Destructive Testing (NDT)
hours: 4
weight_pct: 2
outcome: >
  Upon successful completion, learners will be able to identify and describe NDT methods,
  their uses, strengths, and limitations in welding inspection.
objectives:
  - Identify NDT methods used in welding inspection.
  - Describe visual inspection techniques.
  - Describe penetrant testing (PT) principles and applications.
  - Describe magnetic particle testing (MT) principles and applications.
  - Describe ultrasonic testing (UT) principles and applications.
  - Describe radiographic testing (RT) principles and applications.
red_seal_mapping:
  - A-5.01 (Performs quality inspection)
  - A-4.01 (Uses documentation and reference material)
  - A-4.03 (Plans job tasks)
citations:
  - source: CWB Group — Introduction to Welding Inspection
    ref: NDT method overview, welder responsibilities in inspection, visual inspection requirements
    url: https://www.cwbgroup.org/education
  - source: TWI Global — Job Knowledge: Non-Destructive Testing Methods
    ref: VT, PT, MT, UT, RT — principles, applications, limitations
    url: https://www.twi-global.com/technical-knowledge/job-knowledge/ndt-inspection-methods-overview
  - source: CSA W59 — Welded Steel Construction (2018)
    ref: Clause 6 (inspection requirements), acceptance criteria for VT, RT, UT
    url: https://www.csagroup.org/store/product/CSA%20W59%3A18/
  - source: ASME Boiler and Pressure Vessel Code Section V — Nondestructive Examination
    ref: Article 1 (general), Article 2 (RT), Article 4 (UT), Article 6 (PT), Article 7 (MT)
    url: https://www.asme.org/codes-standards/find-codes-standards/bpvc-v-boiler-pressure-vessel-code-section-v-nondestructive-examination
  - source: Lincoln Electric — Non-Destructive Testing in Welding Guide
    ref: Weld defect types and corresponding NDT method selection, welder awareness of inspection requirements
    url: https://www.lincolnelectric.com/en/education-center/welding-education
---

# Non-Destructive Testing (NDT)

Every weld you make will be inspected. At a minimum, it gets visual examination. On pressure vessels, it gets RT or UT. On structural welds in critical service, it gets MT. Understanding what the inspector is looking for — and what each method can and cannot find — makes you a better welder. Welders who know NDT make fewer defects because they think like the inspector before they strike the arc.

---

## What NDT Means

Non-Destructive Testing (NDT) — also called Non-Destructive Examination (NDE) or Non-Destructive Evaluation (NDE) — is any method of testing a weld or component that leaves the part intact and serviceable afterward.[^1][^2]

**Contrast with Destructive Testing (DT):** bend tests, tensile tests, Charpy impact, macroetch — all require cutting a sample from the weld. DT provides better information about mechanical properties but destroys the test piece.

**The fundamental NDT tradeoff:** NDT is less precise than DT but can be applied to production welds. Every production weld on a pressure vessel or critical structural joint gets NDT. Representative coupons from the welding procedure qualification get DT.

---

## Visual Testing (VT) — The Foundation

Visual testing is required before, during, and after EVERY weld on code work.[^1][^3]

### What VT can detect

- **Surface defects only:** undercut, overlap, cracks, porosity (at the surface), crater cracks, incorrect reinforcement height, incorrect bead size, spatter, arc strikes
- **Joint preparation:** root gap, bevel angle, land height before welding
- **Distortion and dimensional accuracy:** after welding

### VT tools and requirements

| Tool | Use |
|---|---|
| **Weld gauge (fillet gauge)** | Measure fillet weld leg size and throat — verify against drawing requirements |
| **Hi-lo gauge** | Measure hi-lo (misalignment) at pipe joints — typically max 1.6 mm (1/16") for code pipe |
| **Flashlight** | Adequate lighting is REQUIRED — CSA W59 requires minimum 160 lux (15 foot-candles) at the inspection surface[^3] |
| **Mirror on a stick** | Inspect inside corners, backing bars, inaccessible areas |
| **Magnifying glass (10× or less)** | VT does NOT use high magnification; 10× is the accepted limit for standard VT — beyond 10× is considered "enhanced VT" |
| **AWS weld profile gauges** | Check convexity, concavity, and crown height against acceptance criteria |

### VT acceptance criteria (CSA W59 examples)[^3]

| Defect | Acceptable limit |
|---|---|
| Undercut | ≤ 1 mm (1/16") depth, not more than 10% of base metal thickness |
| Weld reinforcement (groove) | ≤ 3 mm (1/8") for t ≤ 25 mm |
| Overlap | Not acceptable — no cold lap at toes |
| Cracks | None acceptable |
| Porosity | Not to exceed limits of Figure 6.1 in W59 (area and pore size limits) |
| Arc strikes | Not acceptable in notch-tough or fracture-critical applications |

### When to do VT

- **Before welding:** check joint fit-up, cleanliness, preheat temperature, tack weld quality
- **Between passes:** check for cracks, incomplete fusion, slag traps before covering with the next pass
- **After welding:** final inspection before the part goes to the next operation

---

## Penetrant Testing (PT / LPT) — Liquid Dye Penetrant

PT finds surface-breaking defects in non-magnetic, non-porous materials (all metals, ceramics, plastics).[^2][^4]

### How PT works

1. **Pre-clean:** remove all oil, paint, scale, rust. The surface must be bare and clean — contaminants block penetrant from entering cracks.
2. **Apply penetrant:** spray or brush a red dye (visible) or fluorescent dye onto the surface. Let it **dwell** (penetration time) — typically **10–15 minutes** minimum for most cracks[^4]
3. **Remove excess penetrant:** wipe or wash off surface penetrant according to the penetrant type (solvent-removable, water-washable, or post-emulsifiable). Do NOT remove from inside the crack.
4. **Apply developer:** spray a white developer powder (or solution) over the surface. Developer acts as a "blotter" that draws the penetrant out of cracks and stains the white background red (or shows fluorescent pink under UV for fluorescent PT).
5. **Inspect:** under adequate white light (>1000 lux) or UV light (>1000 μW/cm²). Visible indications are red on white background.

### PT strengths

- Works on ALL metals (ferrous and non-ferrous), ceramics, plastics
- Inexpensive equipment
- Sensitive to tight, fine surface cracks
- Fluorescent PT is extremely sensitive (used for aerospace work)

### PT limitations

- **Surface-only** — cannot detect subsurface defects
- **Surface must be clean and accessible**
- **Porous materials cannot be tested** (the penetrant soaks in everywhere)
- **Temperature sensitive:** standard PT works between 10 °C and 52 °C (50 °F and 125 °F). High-temperature or low-temperature PT formulations exist for special applications[^4]

### PT applications in welding

- Final inspection of austenitic stainless and nickel alloy welds (where MT won't work — non-magnetic)
- Root inspection after back-gouging
- Inspection of cast fittings and machined components

---

## Magnetic Particle Testing (MT) — For Ferromagnetic Materials Only

MT finds surface and near-surface defects in magnetic (ferromagnetic) materials — carbon steel, alloy steel, ferritic stainless.[^2][^4]

### How MT works

1. **Magnetize the part:** apply a magnetic field using a yoke (AC or DC), prods, coil, or direct contact. The magnetic field travels through the part.
2. **Apply magnetic particles:** iron oxide powder (dry or wet suspension) is applied to the surface while magnetized. The particles are attracted to **flux leakage** at defects — where the magnetic field "leaks" out at discontinuities.
3. **Inspect:** particles gather in a pattern that reveals the defect shape. Fluorescent wet particles under UV light (BWMT or MPI) give the best sensitivity.
4. **Demagnetize:** required for parts that will carry electrical current or be used with precision equipment.

### MT strengths

- Detects surface AND near-surface defects (up to ~6 mm depth for DC, ~3 mm for AC current)[^2]
- Fast — can inspect large areas quickly
- Extremely good for detecting transverse cracks (perpendicular to weld axis) and linear indications
- Sensitive to tight, fine cracks that PT might miss when combined with UV particles

### MT limitations

- **Only works on ferromagnetic materials** — useless on austenitic stainless, aluminum, copper, nickel alloys
- Requires magnetization in **two directions** (perpendicular to each other) to detect defects in all orientations — a defect running parallel to the field direction will not produce leakage
- Surface must be relatively clean (scale and thick coatings reduce sensitivity)
- Demagnetization required after inspection in some applications

### Yoke pull test

The AC/DC yoke must be tested before use to verify adequate magnetic field strength. For AC yoke: minimum lifting force **45 N (10 lb)**. For DC permanent magnet yoke: **180 N (40 lb)**.[^4]

---

## Ultrasonic Testing (UT) — Volumetric Inspection

UT uses high-frequency sound waves to detect internal defects.[^2][^4]

### How UT works

1. **Apply couplant:** a liquid (gel, oil, or glycerin) is applied to the surface to transmit sound from the probe into the metal
2. **Transmit ultrasonic pulses:** a transducer (probe) converts electrical pulses to sound waves (typically 1–10 MHz). The wave travels into the material.
3. **Detect echoes:** when the sound wave hits a boundary (defect, back wall), it reflects. The reflected echo returns to the transducer.
4. **Display:** a screen shows time-of-flight (distance to reflector) and amplitude (size of the reflector) — the UT operator interprets the pattern.

### UT methods

- **Pulse-echo (conventional UT):** a single probe transmits and receives — most common
- **Phased array UT (PAUT):** electronically steers the beam in multiple angles simultaneously — faster, more coverage
- **Time-of-flight diffraction (TOFD):** two probes placed on opposite sides of the weld — very accurate for sizing defect height

### UT strengths

- **Volumetric inspection** — detects internal defects (inclusions, lack of fusion, hydrogen cracks, laminations)
- Detects defects that RT misses (planar defects perpendicular to the X-ray beam, like lack of fusion)
- Portable — can be done in the field on large structures
- Results are immediate (no film processing)
- Can accurately size defect depth and height

### UT limitations

- **Operator-dependent:** UT interpretation requires significant skill and CGSB Level II or III certification[^1]
- **Rough surfaces reduce sensitivity** — grinding may be required
- **Does not produce a permanent visual record** unless PAUT or TOFD data is stored digitally
- **Near-surface dead zone:** a short distance from the surface is "blind" to UT (depending on probe configuration)

---

## Radiographic Testing (RT) — Permanent Volumetric Record

RT uses X-rays or gamma rays to produce a film or digital image of the internal structure of the weld.[^4]

### How RT works

1. **Position the radiation source** on one side of the weld, film or detector on the other
2. **Expose:** radiation passes through the metal. Thicker areas absorb more radiation; thinner areas or voids (defects) transmit more radiation.
3. **Process film (or read digital image):** defects appear as darker areas on the radiograph (more radiation passed through where there was less metal = void, slag, porosity)
4. **Interpret:** a certified RT Level II interpreter reads the radiograph against acceptance criteria

### Radiation sources

| Source | Type | Penetrating power | Application |
|---|---|---|---|
| **X-ray machine** | X-rays (generated) | Adjustable (up to ~400 kV) | Shop use, best image quality |
| **Iridium-192 (Ir-192)** | Gamma rays (radioactive isotope) | Up to ~75 mm steel | Field use, flexible positioning |
| **Cobalt-60 (Co-60)** | Gamma rays | Up to ~200 mm steel | Very thick sections |
| **Selenium-75 (Se-75)** | Gamma rays | Lower penetration | Fine-grained image for pipe welds |

### RT strengths

- **Permanent visual record** (film or digital) that can be reviewed and stored
- Excellent for detecting volumetric defects: porosity, slag inclusions, incomplete penetration, burn-through
- Detects both surface and internal defects
- Interpretable by multiple parties

### RT limitations

- **Planar defects (cracks, lack of fusion) may be missed** if they are perpendicular to the radiation beam and very tight
- **Requires access to both sides** of the weld (source one side, film the other)
- **Radiation safety requirements:** exclusion zone, dosimetry badges, licensed operator (CGSB RT Level II minimum)[^1]
- **Slow process:** film exposure, processing, and interpretation take more time than UT
- **Not suitable for all geometries** — complex shapes are difficult to radiograph without geometric unsharpness distortion

### RT acceptance criteria (CSA W59 example)[^3]

| Defect | Acceptance |
|---|---|
| Porosity (rounded) | ≤ per aggregate area limits in W59 Table 6.1 (depends on t) |
| Linear porosity | No more than 6 pores in any 25 mm of weld |
| Slag inclusions | Max length 2/3 t; total length ≤ t in any 12t of weld |
| Incomplete penetration | Not acceptable (structural Category B welds) |
| Cracks | None acceptable |

---

## Choosing the Right NDT Method

| What you're looking for | Best method | Why |
|---|---|---|
| **Surface cracks — all metals** | PT | Works on ferrous and non-ferrous |
| **Surface and near-surface — ferrous** | MT | More sensitive than PT for magnetic materials |
| **Internal volumetric defects** | RT or UT | Both are volumetric methods |
| **Planar defects (cracks, LOF)** | UT | RT can miss tight planar defects |
| **Permanent record required** | RT | Film or digital image is reviewable |
| **Field piping joints** | RT (Ir-192) or UT | Both are field-portable |
| **Austenitic stainless, nickel alloy** | PT (not MT) | These materials are non-magnetic |

---

## Numbers you need to memorize

- **VT minimum lighting:** 160 lux (15 foot-candles) at the weld surface[^3]
- **PT dwell time:** 10–15 minutes minimum[^4]
- **PT temperature range (standard):** 10–52 °C (50–125 °F)[^4]
- **AC yoke minimum lift force:** 45 N (10 lb)[^4]
- **DC permanent yoke minimum lift force:** 180 N (40 lb)[^4]
- **MT near-surface depth:** up to ~6 mm (DC); ~3 mm (AC)[^2]
- **VT maximum magnification for standard VT:** 10×[^1]
- **Ir-192 thickness range:** up to ~75 mm steel[^4]
- **Co-60 thickness range:** up to ~200 mm steel[^4]

---

## What the textbook doesn't tell you

**VT is the most important NDT — not because it's fancy, but because it's used first.** A weld that fails visual inspection never gets to RT or UT. A weld that passes visual but fails on RT is a process problem. Most production failures caught by RT or UT would have been caught earlier by careful between-pass VT. Inspect between passes. Every time.[^1]

**Radiation exclusion zones are real safety hazards.** On a construction site, Ir-192 shots happen in marked exclusion zones and require posted signage, monitoring personnel, and dosimetry. As a welder on that site, you need to know where the RT zone is and stay out of it during exposure. RT coordinators will brief the crew — pay attention.[^4]

**UT is the inspector's secret weapon against planar defects.** A lack-of-fusion plane running along the sidewall of a groove weld is perpendicular to the RT beam in the classic double-wall technique and may be virtually invisible on film. The same defect produces a strong UT echo because the flat defect reflects sound efficiently. This is why ASME Section VIII pressure vessels often use both RT and UT.[^4]

**The welder creates traceability.** On code jobs, each weld is numbered and the welder's ID is stamped or marked at the end of the weld. When RT finds a defect, the record tracks back to the welder, WPS, preheat records, and consumable batch. This is how code quality systems work — and why good welders keep good records.[^1]

---

## Diagram

*(SVG to be added: `assets/diagrams/p3-s2-e-ndt-method-comparison.svg` — horizontal bar chart or table diagram comparing 5 NDT methods (VT, PT, MT, UT, RT) across 5 dimensions: detection depth, material applicability, portability, cost, record type — visual comparison matrix)*

*(SVG to be added: `assets/diagrams/p3-s2-e-pt-steps.svg` — five-step process diagram: pre-clean → apply penetrant → dwell → remove excess → apply developer → inspect, with red indication on white developer background)*

*(SVG to be added: `assets/diagrams/p3-s2-e-mt-flux-leakage.svg` — cross-section showing magnetic field lines flowing through steel, deflecting around a surface crack (flux leakage), magnetic particles gathering at the crack indication)*

---

## Key terms

- **NDT (Non-Destructive Testing):** testing methods that leave the part intact — no material is removed or destroyed
- **VT (Visual Testing):** inspection with the naked eye (±10× magnification) — the most fundamental NDT method
- **PT (Penetrant Testing):** dye penetrant method for surface defects in any material
- **MT (Magnetic Particle Testing):** magnetic flux leakage method for surface and near-surface defects in ferromagnetic materials
- **UT (Ultrasonic Testing):** high-frequency sound method for internal volumetric defects
- **RT (Radiographic Testing):** ionizing radiation method producing a permanent image of internal weld structure
- **Dwell time:** the time penetrant is left on the surface before removal — allows penetration into defects
- **Flux leakage:** the deflection of magnetic field lines at a surface discontinuity — attracts MT particles
- **Ir-192:** Iridium-192, a radioactive isotope used as a gamma-ray source for field RT of pipe welds
- **PAUT (Phased Array UT):** electronically steerable UT that covers multiple angles simultaneously
- **CGSB:** Canadian General Standards Board — certifies NDT personnel to defined levels (Level I, II, III)

---

## Common exam trap

- **PT works on ALL materials; MT works only on MAGNETIC materials.** Austenitic stainless, aluminum, nickel alloys → PT only, not MT.
- **MT requires two magnetization directions** to detect defects in all orientations — a single magnetization pass misses parallel defects.
- **RT is poor at detecting tight planar defects** (cracks, lack of fusion perpendicular to beam). UT is BETTER for planar defects. This is a classic exam distinguisher.
- **VT maximum magnification is 10×** — beyond that is enhanced VT with different qualification requirements.
- **Radiographs show dense areas as LIGHTER (white)** and voids as DARKER (black). Denser metal absorbs more radiation; voids/slag transmit more. Don't get confused — the film is an attenuation map.
- **Dwell time (PT):** minimum 10–15 minutes for most applications. Not 2 minutes (too short) or 60 minutes (unnecessary for most applications).

---

## Practice question preview

**Q:** A welder has completed a groove weld on 316L austenitic stainless steel pipe. The inspector needs to perform surface NDT on the root pass after back-gouging. Which method should be specified?

A) Magnetic Particle Testing (MT) — most sensitive surface method  
B) Radiographic Testing (RT) — produces a permanent record  
C) Liquid Penetrant Testing (PT) — works on non-magnetic stainless steel  
D) Ultrasonic Testing (UT) — detects near-surface discontinuities

**Correct: C**

**Explanation:** Austenitic stainless steel is non-magnetic. MT requires ferromagnetism — it will NOT work on 316L. PT works on any solid, non-porous material regardless of magnetic properties — it is the standard surface NDT method for stainless steel and nickel alloys. RT (option B) is a volumetric method, not a surface method, and requires access to both sides for a film. UT (option D) is volumetric and detects near-surface defects, but PT is the appropriate and code-referenced surface method for stainless.

**Red Seal mapping:** A-5.01 (Performs quality inspection)

---

[^1]: [CWB Group — Introduction to Welding Inspection](https://www.cwbgroup.org/education); NDT method overview, welder responsibilities, VT requirements (lighting, magnification), traceability in code work
[^2]: [TWI Global — NDT Inspection Methods Overview](https://www.twi-global.com/technical-knowledge/job-knowledge/ndt-inspection-methods-overview); VT/PT/MT/UT/RT principles, detection capabilities and limitations, method selection guidance
[^3]: [CSA W59 — Welded Steel Construction (2018)](https://www.csagroup.org/store/product/CSA%20W59%3A18/); Clause 6 (inspection requirements, acceptance criteria for VT, RT, UT); Table 6.1 (porosity limits); lighting requirement 160 lux
[^4]: [ASME Boiler and Pressure Vessel Code Section V — Nondestructive Examination](https://www.asme.org/codes-standards/find-codes-standards/bpvc-v-boiler-pressure-vessel-code-section-v-nondestructive-examination); Article 2 (RT — exposure, film, Ir-192/Co-60), Article 4 (UT — pulse echo), Article 6 (PT — dwell time, temperature range), Article 7 (MT — yoke lift test 45N AC/180N DC)
[^5]: [Lincoln Electric — Non-Destructive Testing in Welding Guide](https://www.lincolnelectric.com/en/education-center/welding-education); weld defect types and corresponding NDT method selection
