---
id: p2-s4-a
period: 2
section: 4
section_title: Gas Tungsten Arc Welding (GTAW)
topic_letter: A
topic_title: The GTAW Process
hours: 5
weight_pct: 2
outcome: >
  Upon successful completion, learners will be able to identify and describe GTAW procedures and fundamentals.
objectives:
  - Describe the GTAW process and applications.
  - Describe advantages and disadvantages of the GTAW process.
  - Identify hazards and protective measures associated with GTAW.
  - Describe single-phase and three-phase power.
  - Identify components of a GTAW workstation.
  - Describe types of GTAW power sources.
  - Identify AC, DC, and high frequency welding currents used in GTAW.
  - Describe torch assemblies.
  - Describe gas regulators and flow meters.
red_seal_mapping:
  - D-15.01 (Selects GTAW gas, equipment and consumables)
  - D-15.02 (Sets up GTAW equipment)
  - A-3.03 (Uses personal protective equipment and safety equipment)
citations:
  - source: Miller Electric — GTAW (TIG) Welding Guide
    ref: Process description, torch assemblies, power source types, AC/DC/HF current descriptions, workstation setup
    url: https://www.millerwelds.com/resources/article-library/tig-welding-guide
  - source: Lincoln Electric — The TIG Welding Process
    ref: Process fundamentals, advantages and disadvantages, shielding gas, AC balance, equipment components
    url: https://www.lincolnelectric.com/en/education-center/welding-education/tig-welding
  - source: AWS D1.1 — Structural Welding Code — Steel (2020)
    ref: GTAW process qualifications, position designations (1F/2F/3F, 1G/2G/3G), groove weld requirements
    url: https://pubs.aws.org/p/2056/d1-12020-structural-welding-code-steel
  - source: CSA W117.2 — Safety in Welding, Cutting, and Allied Processes (2019)
    ref: Clause 8 — GTAW specific hazards, ozone formation, HF arc start, UV radiation
    url: https://www.csagroup.org/store/product/CSA%20W117.2/
  - source: Modern Welding (Bowditch, Goodheart-Willcox, 12th ed.)
    ref: Chapter 13 — Gas Tungsten Arc Welding; process description, equipment, AC/DC polarity effects, torch anatomy
    url: https://www.g-w.com/modern-welding
  - source: AIT Welder Curriculum Guide 012 (2026), Period 2 Section 4 Topic A
    ref: pp. 51–55
    url: https://tradesecrets.alberta.ca/SOURCES/PDFS/CURRICULUM_GUIDES/012_OUTLINE.PDF
---

# The GTAW Process

Gas Tungsten Arc Welding (GTAW) — called TIG (Tungsten Inert Gas) on the shop floor — is the precision process. The tungsten electrode doesn't melt; you control how much filler goes in; the weld pool is clean and fully visible. That precision makes GTAW the right process for thin material, aluminum, stainless steel, exotic alloys, and any application where weld quality cannot be compromised and appearance matters. It's also the most demanding process to learn — it requires two hands working independently, consistent torch coordination, and patience. Mastering GTAW adds the widest range of work to your qualifications.

---

## The GTAW process: fundamentals

GTAW is an arc welding process that uses:[^1][^2]

1. **A non-consumable tungsten electrode** — the electrode carries the current but does not melt into the weld (in normal operation). It creates the arc; it does not supply filler metal.
2. **A separate filler rod** — manually fed into the leading edge of the weld pool by the welder's free hand (or left out entirely on thin material — autogenous weld)
3. **An inert shielding gas** (argon, or argon-helium mixtures) — flows continuously through the torch to protect the tungsten and weld pool from atmospheric contamination

**The arc forms between the tungsten tip and the base metal.** The extremely high temperature (~11,000°C at the arc centre) melts the base metal. The welder dips the filler rod into the leading edge of the puddle to add material.

### Comparison to other processes

| Feature | SMAW | GMAW | GTAW |
|---|---|---|---|
| Electrode consumable? | Yes (electrode melts) | Yes (wire melts) | **No (tungsten doesn't melt)** |
| Filler metal source | Electrode coating + core | Continuous wire | Separate rod, fed by hand |
| Shielding | Flux/slag | Gas | Gas (inert only) |
| Deposition rate | Moderate | High | **Low** |
| Arc visibility | Obscured by flux | Good | **Excellent — fully visible puddle** |
| Typical applications | Structural, heavy fabrication | Production, thin-medium plate | **Thin, critical, exotic alloys, root passes** |
| Welder skill demand | Moderate | Low-moderate | **High** |

---

## Advantages of GTAW

**Why you'd choose GTAW over other processes:**[^1][^2]

- **Cleanest welds:** No flux, no slag, no spatter — the inert shielding gas provides complete protection without byproducts
- **No filler required (autogenous):** Thin material (< 1.5 mm) can be fusion-welded without filler metal by melting the base edges together
- **Precision control:** Foot pedal or finger-control adjusts amperage dynamically while welding — you can reduce heat at the end of a pass to prevent craters, or ramp up through a thick section
- **All metals:** GTAW welds carbon steel, stainless steel, aluminum, titanium, nickel alloys, copper, brass, and most exotic alloys — it's the most versatile process in terms of material capability
- **X-ray quality:** With correct technique and preparation, GTAW consistently produces the highest radiographic quality welds of any arc process
- **Root pass on pipe:** GTAW is frequently used for the root pass on critical pipe welds (pressure piping, nuclear, aerospace) because of its precise penetration control

---

## Disadvantages of GTAW

**Why you'd NOT always use GTAW:**[^1][^2]

- **Slow:** Deposition rate 0.5–2 kg/hr vs FCAW 4–10+ kg/hr — not competitive for heavy production
- **Skill-intensive:** Requires two-hand coordination, foot pedal control, and a stable torch hold. Takes significantly more training than GMAW to reach production quality
- **Expensive per metre:** Lower deposition rate + higher skill level = higher cost per unit of weld deposited
- **Sensitive to contamination:** Even small amounts of oil, moisture, or mill scale cause porosity and tungsten inclusions. Base metal and filler must be chemically clean.
- **Limited to clean environments:** Wind, drafts, or contaminated shielding gas immediately cause porosity. Not suitable for outdoor field work without windshield/shelter.
- **Slower on thick material:** The low deposition rate becomes economically prohibitive on plate thicker than ~12 mm (unless root pass by GTAW, then other process for fill/cap)

---

## GTAW hazards and protective measures

GTAW has specific hazards beyond standard arc welding:[^4]

### Ozone (O₃) formation
**Hazard:** The UV radiation from the GTAW arc — more intense than SMAW or GMAW arcs — photolyzes oxygen in the shielding zone, producing ozone. Ozone irritates the respiratory system, eyes, and skin. Chronic exposure damages lungs.[^4]

**Control:** Local exhaust ventilation (LEV) at the weld zone; general ventilation; keep the welder's face behind or to the side of the torch to minimize exposure. Alberta OHS TLV for ozone: 0.1 ppm (8-hr TWA)[^4]

### High-frequency (HF) arc start interference
**Hazard:** HF arc starts produce electromagnetic interference (EMI) that can interfere with pacemakers, hearing aids, and electronic equipment nearby.[^4]

**Control:** Workers with pacemakers should NOT work near GTAW equipment using HF arc start. Post warnings. Shield HF from electronic equipment.

### Intense UV radiation
**Hazard:** GTAW arc UV output is higher than SMAW or GMAW for the same amperage — the unobstructed arc and inert gas produce more UV.[^4]

**Shade selection for GTAW (per CSA Z94.3):**[^4]

| GTAW amperage | Minimum lens shade |
|---|---|
| < 50 A | Shade 8 |
| 50–150 A | Shade 10 |
| 150–250 A | Shade 12 |
| > 250 A | Shade 14 |

---

## Power sources for GTAW

GTAW requires a **constant-current (CC)** power source — also called a "drooping characteristic" power source.[^1][^5]

**Why CC and not CV (constant voltage)?**
- The welder manually adjusts arc length while welding
- If arc length increases slightly (as it will), a CC source holds the amperage approximately constant and the voltage adjusts — arc stays stable
- A CV source would reduce amperage as arc length increases → arc extinguishes. CV is for wire-feed processes where arc length is controlled by wire feed rate.

**Types of GTAW power sources:**[^1][^5]

| Type | Output | Best for |
|---|---|---|
| **Transformer** | AC only | Basic aluminum GTAW (AC required for cathodic cleaning) |
| **Transformer-rectifier** | DC or AC (switched) | All metals; DC for steel/stainless, AC for aluminum |
| **Inverter** | DC or AC (inverter-based AC) | Most modern machines; lightweight; precise control; frequency-adjustable AC for aluminum |

**Single-phase vs three-phase input:**[^5]
- **Single-phase (120V or 240V):** Common for smaller shop/home GTAW machines; limited output amperage
- **Three-phase (208V, 480V):** Commercial machines; higher output capacity; more efficient; required for machines above ~400A

---

## Current types used in GTAW

This is one of the most tested topics in GTAW theory.[^1][^2][^5]

### DCEN (DC Electrode Negative / Straight Polarity)
- **Electrons flow from workpiece to tungsten (electrode negative)**
- ~70% of heat generated at the workpiece
- **Deep, narrow penetration profile** — excellent for steel, stainless, copper, titanium
- Tungsten remains **pointed** — correct geometry for DCEN
- **No cathodic cleaning** — oxide layer on aluminum is NOT broken up → not suitable for aluminum

### DCEP (DC Electrode Positive / Reverse Polarity)
- Electrons flow from tungsten to workpiece
- ~70% of heat generated at the tungsten → extreme tungsten heating → tungsten forms a ball, may melt
- **Cathodic cleaning action** — positive ion bombardment of the workpiece breaks up oxide layers → useful for aluminum
- **Shallow penetration** — because less heat at workpiece
- **Rarely used for GTAW** (used for very thin aluminum sometimes) — AC is preferred for aluminum because AC gives cathodic cleaning on the electrode-positive half-cycle without melting the tungsten

### AC (Alternating Current)
- Current alternates each half-cycle
- **Electrode-negative half-cycle:** deep penetration
- **Electrode-positive half-cycle:** cathodic cleaning of the oxide layer
- **Net effect:** moderate penetration + aluminum oxide removal → **AC is standard for aluminum GTAW**[^1]
- Tungsten forms a **ball** on the electrode-positive half — correct for AC
- **AC balance control** (on modern inverter machines): adjusts the ratio of EN to EP half-cycles
  - More EN (penetration) = deeper weld, less cleaning, more pointed tungsten (electrode slightly tapers)
  - More EP (cleaning) = shallower weld, better oxide cleaning, larger tungsten ball

### High Frequency (HF) Arc Start
Three methods for starting the GTAW arc:[^1]

| Method | How it works | Best for |
|---|---|---|
| **HF start** | HF spark bridges the gap without touching tungsten to workpiece | Aluminum AC GTAW; any application where arc start must not contaminate tungsten |
| **Lift arc** | Tungsten briefly touches workpiece, lifts; arc established at low amperage without HF | When HF is problematic (sensitive electronics); available on some DC machines |
| **Scratch start** | Scratch tungsten across workpiece like a match | Only on basic machines with no HF or lift arc; risk of tungsten contamination and tungsten inclusions in weld |

---

## GTAW torch anatomy

The torch is the welder's hand tool — understanding its parts allows field maintenance and troubleshooting.[^1][^5]

**Components from inside out:**
1. **Power cable** — conducts welding current from the power source
2. **Gas hose** — conducts shielding gas from the regulator to the torch
3. **Torch body** — insulated handle; contains the collet body and gas passages
4. **Collet body** — holds the collet; channels shielding gas to the gas lens or cup
5. **Collet** — the precision-machined split tube that grips the tungsten electrode; sized to match tungsten diameter (1.6 mm, 2.4 mm, 3.2 mm, etc.)
6. **Gas lens** — optional screen-type insert that smooths shielding gas flow into laminar flow; dramatically improves gas coverage; HIGHLY RECOMMENDED for critical work
7. **Ceramic gas cup (nozzle)** — channels shielding gas around the arc; larger cups = better coverage; cup size selected based on current and material
8. **Tungsten electrode** — extends 3–6 mm beyond the end of the cup (typically)

**Back cap:** Closes the back of the torch; holds the tungsten in place from the rear.

---

## Gas regulators and flow meters

GTAW uses **inert shielding gas only** — argon (Ar) or argon-helium (Ar-He) mixtures.[^1]

**Regulator function:** Reduces cylinder pressure (e.g., 200 bar / 2900 psi) to working pressure (~70–200 kPa / 10–30 psi delivery pressure).

**Flow meter types:**
- **Ball float (rotameter):** Vertical tube with scale; ball height = flow rate. Read the ball at eye level to the middle of the ball. More common in smaller shops.
- **Pressure-compensated flow meter:** More accurate; better for long gas hose runs.
- **Digital flow meter:** Most accurate; displays actual flow rate; used in precision shops.

**GTAW gas flow rate:** typically **8–15 L/min (15–30 CFH)** for most mild steel GTAW.[^1] Lower than FCAW because argon is denser and the torch angle is closer to perpendicular (better coverage without high flow).

---

## Numbers you need to memorize

- **GTAW electrode:** non-consumable tungsten — does NOT melt into weld (in normal operation)[^1]
- **DCEN:** ~70% heat at workpiece — used for steel, stainless, titanium[^1]
- **AC:** cathodic cleaning + moderate penetration — required for aluminum GTAW[^1]
- **DCEP:** heat at tungsten — rarely used for GTAW (overheats tungsten)[^1]
- **HF start:** no contact required — protects tungsten from contamination[^1]
- **GTAW shade for 50–150 A:** Shade 10[^4]
- **GTAW ozone exposure limit:** 0.1 ppm (8-hr TWA)[^4]
- **Standard GTAW gas flow:** 8–15 L/min (15–30 CFH)[^1]
- **Tungsten stick-out:** 3–6 mm beyond cup[^1]
- **Gas lens:** improves laminar flow, extends gas coverage — use for critical work[^1]
- **AC balance more EP:** better oxide cleaning, larger tungsten ball, shallower penetration[^1]
- **AC balance more EN:** deeper penetration, less cleaning, tungsten stays more pointed[^1]

---

## What the textbook doesn't tell you

**The gas lens is not optional for serious GTAW.** Standard collet bodies produce turbulent gas flow that limits coverage. A gas lens creates smooth laminar flow around the arc — better coverage with the same or lower flow rate, and you can extend the tungsten farther from the cup for better visibility in tight joints. Once you've welded with a gas lens, you won't go back. Always have one in your kit.

**Lift arc is often better than HF for shop DC work.** HF arc start is required for AC aluminum (you can't touch aluminum with the tungsten without contaminating it with oxide). But for DC steel/stainless GTAW, lift arc start is cleaner, produces no electromagnetic interference, and doesn't require the HF generator to be maintained. Many experienced TIG welders prefer lift arc for routine steel work.

**The tungsten stick-out determines your working envelope.** More stick-out gives you better visibility and access to tight joints (inside corners, pipe bores). But more stick-out also means the tungsten is less supported and more likely to flex into the puddle if you lose concentration. 3–6 mm stick-out is the standard range — use less for general work, more for access in tight spots.

---

## Diagram

*(SVG to be added: `assets/diagrams/p2-s4-a-gtaw-torch.svg` — cutaway view of a GTAW torch showing: torch body, collet body, collet gripping tungsten, gas lens (if installed), ceramic cup, tungsten electrode with stick-out labeled, gas flow arrows through gas lens, shielding gas stream around arc.)*

*(SVG to be added: `assets/diagrams/p2-s4-a-current-comparison.svg` — three-panel diagram showing: (1) DCEN — electron flow arrows from workpiece to tungsten, heat concentration at workpiece (70%), narrow deep penetration profile; (2) DCEP — electron flow from tungsten, tungsten overheats, shallow penetration; (3) AC — both half-cycles labeled, moderate penetration, cleaning action arrows on surface.)*

---

## Key terms

- **GTAW (TIG):** Gas Tungsten Arc Welding — arc welding process using a non-consumable tungsten electrode and inert shielding gas, with separate filler rod
- **Non-consumable electrode:** electrode that carries current but does not melt into the weld — tungsten in GTAW
- **DCEN (Straight polarity):** DC Electrode Negative — electrons from workpiece to tungsten; deep penetration; no cathodic cleaning
- **DCEP (Reverse polarity):** DC Electrode Positive — electrons from tungsten to workpiece; cathodic cleaning; overheats tungsten; rarely used in GTAW
- **AC (Alternating Current):** alternates each half-cycle; combines penetration (EN half) with cathodic cleaning (EP half); standard for aluminum GTAW
- **Cathodic cleaning:** electrode-positive half-cycle action that breaks up aluminum oxide by positive ion bombardment
- **AC balance control:** adjustment of EN-to-EP ratio in AC GTAW — affects penetration vs cleaning balance
- **HF (High Frequency) arc start:** spark that bridges the arc gap without contact — protects tungsten from contamination
- **Lift arc start:** brief tungsten-to-workpiece contact at very low amperage, then lift; arc established without HF
- **Gas lens:** screen insert in torch collet body that converts turbulent to laminar gas flow; improves shielding coverage
- **Collet:** split-tube clamp that grips and holds the tungsten electrode in the torch
- **Ozone:** O₃ produced by UV photolysis in GTAW arc area — respiratory hazard; control with LEV
- **Constant-current (CC):** power source characteristic that holds amperage approximately constant regardless of arc length changes — required for GTAW

---

## Common exam trap

- **GTAW uses DCEN for steel and stainless — NOT DCEP** — DCEP overheats the tungsten. Exam distractors will flip these.
- **AC is required for aluminum** — not DCEN, not DCEP. The cathodic cleaning half-cycle of AC is what makes aluminum GTAW work.
- **The tungsten does NOT melt into the weld** in normal GTAW operation. Tungsten inclusions are a defect, not a design feature. If tungsten enters the weld pool, it's a problem — not the process working correctly.
- **Gas lens is OPTIONAL** — it's an accessory that improves coverage but is not part of standard torch assembly. Exam may imply it's mandatory.
- **HF start is required for AC aluminum GTAW** — you cannot touch the tungsten to aluminum (it picks up aluminum oxide and contaminates the tungsten). HF allows non-contact arc starting.
- **Ozone is produced by GTAW UV** — not by the electrode coating or flux. GTAW produces more ozone per unit of welding than SMAW because of its more intense UV output.

---

## Practice question preview

**Q:** A welder is setting up a GTAW machine to weld 3 mm aluminum plate. Which current type and arc start method is CORRECT?

A) DCEN (straight polarity), HF arc start
B) DCEP (reverse polarity), scratch start
C) AC, HF arc start
D) DCEN (straight polarity), lift arc start

**Correct: C**

**Explanation:** Aluminum GTAW requires AC current to provide the cathodic cleaning action (electrode-positive half-cycle) that breaks up the aluminum oxide layer. HF arc start is required for aluminum AC GTAW because touching the tungsten to aluminum before arc establishment contaminates the tungsten with aluminum oxide, ruining its geometry and causing inclusions. (A) DCEN provides no cathodic cleaning — the oxide layer on aluminum is not broken up, causing oxide inclusions and lack of fusion. (B) DCEP overheats and melts the tungsten; scratch start would contaminate it further; aluminum doesn't respond well to either. (D) DCEN with lift arc = no oxide cleaning, and for AC aluminum welding, HF is standard, not lift arc.

**Red Seal mapping:** D-15.01 (Selects GTAW gas, equipment and consumables); D-15.02 (Sets up GTAW equipment)

---

[^1]: [Miller Electric — GTAW (TIG) Welding Guide](https://www.millerwelds.com/resources/article-library/tig-welding-guide); process description, torch assembly anatomy, AC/DC/HF current types and applications, gas lens function, shielding gas flow rates, advantages/disadvantages
[^2]: [Lincoln Electric — The TIG Welding Process](https://www.lincolnelectric.com/en/education-center/welding-education/tig-welding); GTAW fundamentals, AC balance control, electrode polarity effects, process comparison to SMAW/GMAW
[^3]: [AWS D1.1:2020 — Structural Welding Code — Steel](https://pubs.aws.org/p/2056/d1-12020-structural-welding-code-steel); GTAW process qualifications, position designations
[^4]: [CSA W117.2:19 — Safety in Welding, Cutting, and Allied Processes](https://www.csagroup.org/store/product/CSA%20W117.2/), Clause 8 — GTAW hazards including ozone formation, HF interference, UV radiation; shade number requirements by amperage range
[^5]: [Modern Welding, 12th ed. (Bowditch, Goodheart-Willcox)](https://www.g-w.com/modern-welding), Chapter 13 — Gas Tungsten Arc Welding; power source types, single-phase vs three-phase, CC vs CV, torch components, flow meters
[^6]: [AIT Welder Curriculum Guide 012 (2026), Period 2 Section 4 Topic A](https://tradesecrets.alberta.ca/SOURCES/PDFS/CURRICULUM_GUIDES/012_OUTLINE.PDF), pp. 51–55
