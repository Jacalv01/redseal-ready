---
id: p2-s2-d
period: 2
section: 2
section_title: Drafting, Drawings and Specifications
topic_letter: D
topic_title: Estimating Principles
hours: 6
weight_pct: 3
outcome: >
  Upon successful completion, learners will be able to demonstrate skills related to estimating.
objectives:
  - Convert angular measurements to linear dimensions.
  - Calculate the cost of steel.
red_seal_mapping:
  - A-4.03 (Plans job tasks)
  - A-4.04 (Organizes materials)
  - B-8.01 (Prepares materials)
citations:
  - source: Modern Welding (Bowditch, Goodheart-Willcox, 12th ed.)
    ref: Chapter 9 — Estimating and Costing; material weight calculations, angular-to-linear conversion, steel cost estimation
    url: https://www.g-w.com/modern-welding
  - source: CWB Group — Welder Certification Study Guide
    ref: Estimation fundamentals, weld joint cost, filler metal consumption
    url: https://www.cwbgroup.org/education/learning-resources
  - source: Lincoln Electric — Weld Cost Calculator Guide
    ref: Deposition rate, weld metal volume calculation, filler metal consumption per unit length
    url: https://www.lincolnelectric.com/en/tools-and-calculators/welding-calculator
  - source: AIT Welder Curriculum Guide 012 (2026), Period 2 Section 2 Topic D
    ref: pp. 43–44
    url: https://tradesecrets.alberta.ca/SOURCES/PDFS/CURRICULUM_GUIDES/012_OUTLINE.PDF
---

# Estimating Principles

Before you buy a piece of steel or quote a job, you need numbers. How heavy is this plate? How much filler metal does this weld use? How do you turn an angle dimension into a length? These calculations are what estimating is built from. They appear on the Red Seal exam and they appear every time a shop foreman asks "how many pounds of wire do we need for this contract?"

---

## Converting angular measurements to linear dimensions

Angular dimensions describe direction and shape; linear dimensions describe length. You need to convert between them constantly in layout and fabrication.[^1]

### The fundamental relationship: tangent of the angle

For a right triangle where you know one leg and the angle:[^1]
> **opposite = adjacent × tan(θ)**
> **adjacent = opposite / tan(θ)**
> **hypotenuse = adjacent / cos(θ)** or **opposite / sin(θ)**

### Example 1: bevel depth from bevel angle and plate thickness

A plate 25 mm thick has a 37.5° bevel (single bevel V-groove). How far from the top face does the bevel cut reach horizontally (root face already removed)?

- θ = 37.5°, adjacent = plate thickness (25 mm for a full bevel — less root face)
- horizontal bevel depth = 25 × tan(37.5°) = 25 × 0.7673 = **19.2 mm**

This tells you how far the bevel face extends horizontally — important for plate utilization and material allowance calculations.[^1]

### Example 2: rise per unit run (slope to distance)

A weld run travels up a slope of 30° from horizontal. The horizontal run is 1200 mm. What is the actual weld length along the slope?

- actual length = horizontal / cos(θ) = 1200 / cos(30°) = 1200 / 0.866 = **1385 mm**

**This matters for filler metal estimates.** The weld is 1385 mm long, not 1200 mm. Using the horizontal distance underestimates filler consumption by 15%.

### Example 3: converting degrees to radians (arc length calculation)

Arc length = radius × angle in radians
Angle in radians = angle in degrees × (π / 180)

For a 250 mm radius arc swept through 120°:
- Radians = 120 × (π / 180) = 2.094 rad
- Arc length = 250 × 2.094 = **523.6 mm**

This is used in pattern development when calculating the arc of a cone's flat sector.[^1]

---

## Calculating the cost of steel

Steel is priced by weight ($/kg or $/tonne). To calculate cost, you need the weight, which comes from the volume and density of steel.[^1]

### Steel density
**Mild steel density = 7.85 g/cm³ = 7850 kg/m³**[^1]

This is the value that must be memorized.

### Volume calculations

**Rectangular plate:**
V (cm³) = length (cm) × width (cm) × thickness (cm)
W (kg) = V × 7.85 g/cm³ ÷ 1000

**Example:** A plate 1200 mm × 600 mm × 12 mm thick:
- V = 120 cm × 60 cm × 1.2 cm = 8640 cm³
- W = 8640 × 7.85 / 1000 = **67.8 kg**
- At $2.50/kg: Cost = 67.8 × $2.50 = **$169.50**

**Round bar:**
V = π × r² × L (same units)

**Example:** 25 mm diameter bar, 3000 mm long:
- r = 1.25 cm; L = 300 cm
- V = π × 1.25² × 300 = π × 1.5625 × 300 = **1472.6 cm³**
- W = 1472.6 × 7.85 / 1000 = **11.56 kg**

**Hollow section (HSS / pipe):**
V = π × (OD² - ID²) / 4 × L

**Example:** NPS 4 Sch 40 pipe (OD = 114.3 mm, wall = 6.02 mm):
- ID = 114.3 - 2(6.02) = 102.26 mm
- V per meter = π × (114.3² - 102.26²) / 4 × 1000 mm = π × (13064.5 - 10457.1) / 4 × 1000 mm
- = π × 2607.4 / 4 × 1000 = 2045780 mm³ = 2045.8 cm³
- W per meter = 2045.8 × 7.85 / 1000 = **16.1 kg/m**[^1]

(Note: published pipe weight tables are more precise — use them when available. Hand calculation is a verification method.)

### Standard plate weights for estimation

| Plate thickness | Weight (kg/m²) |
|---|---|
| 6 mm | 47.1 kg/m² |
| 10 mm | 78.5 kg/m² |
| 12 mm | 94.2 kg/m² |
| 16 mm | 125.6 kg/m² |
| 20 mm | 157.0 kg/m² |
| 25 mm | 196.3 kg/m² |

*Formula: kg/m² = thickness (mm) × 7.85*[^1]

---

## Filler metal consumption estimation

### Weld volume method

Filler metal consumed = volume of weld joint × (density of filler metal / deposition efficiency)[^3]

For steel filler metals, density ≈ 7.85 g/cm³ (same as base metal)
Deposition efficiency for SMAW: ~65%[^3] (the rest becomes spatter, slag, and stub end)
Deposition efficiency for GMAW: ~90–95%[^3]
Deposition efficiency for FCAW: ~82–87%[^3]

### Weld cross-sectional areas for common joints (approximate)[^3]

| Joint type | Weld area (mm²) |
|---|---|
| 6 mm fillet | 18 mm² |
| 8 mm fillet | 32 mm² |
| 10 mm fillet | 50 mm² |
| Single V-groove (60°, 6 mm plate, full pen) | ~21 mm² |
| Single V-groove (60°, 12 mm plate, full pen) | ~55 mm² |
| Single V-groove (60°, 20 mm plate, full pen) | ~115 mm² |

**Calculation example:**
A fabricator needs to estimate filler metal for 50 metres of 8 mm fillet weld using FCAW (85% efficiency):

1. Cross-section area = 32 mm² = 0.32 cm²
2. Volume = 0.32 cm² × 5000 cm (50 m) = **1600 cm³**
3. Weight of weld metal = 1600 × 7.85 / 1000 = **12.56 kg**
4. Filler consumed = 12.56 / 0.85 = **14.78 kg** of wire (purchase ~15 kg, plus allowance for startup waste)

---

## Oxygen and acetylene consumption per cut (estimation awareness)

For completeness, shop estimating often includes cutting gas consumption.[^1]

**Rules of thumb (from ESAB oxyfuel handbook):**
- **Oxygen:** approximately 1.0–1.5 m³ of O₂ per metre of cut on 10 mm plate (varies with tip size and speed)
- **Acetylene:** approximately 0.35–0.50 m³ of C₂H₂ per metre of cut on 10 mm plate
- **Propane:** approximately 0.20–0.30 m³ of C₃H₈ per metre (different combustion chemistry)

For estimating purposes at Period 2 level, use the manufacturer's gas consumption data for the specific tip size and plate thickness.[^1]

---

## Labour cost estimation (awareness only)

Labour hour estimates require:[^1]
- Travel speed (mm/min or in/min) for the process and position
- Number of passes required
- Positioning and handling time (typically 30–50% added to pure weld time)
- Overhead factor (shop rate per hour: typically $65–$120/hr in Alberta fabrication shops)

At Period 2 level, know the concept. Detailed labour hour calculation is Period 3 / journeyperson territory.

---

## Numbers you need to memorize

- **Mild steel density:** 7.85 g/cm³ = 7850 kg/m³[^1]
- **Plate weight formula:** kg/m² = thickness (mm) × 7.85[^1]
- **10 mm plate weight:** 78.5 kg/m²[^1]
- **SMAW deposition efficiency:** ~65%[^3]
- **GMAW deposition efficiency:** ~90–95%[^3]
- **FCAW deposition efficiency:** ~82–87%[^3]
- **8 mm fillet weld cross-section:** ~32 mm²[^3]
- **10 mm fillet cross-section:** ~50 mm²[^3]
- **tan(30°) = 0.577; tan(45°) = 1.000; tan(37.5°) ≈ 0.767** — useful for bevel geometry[^1]

---

## What the textbook doesn't tell you

**Deposition efficiency is the number fabricators forget when ordering wire.** You need 10 kg of weld metal in the joint. That means you order 10 / 0.85 = 11.76 kg of FCAW wire — not 10 kg. Ordering the weld metal weight instead of the consumed wire weight is a consistent junior estimator mistake. Order 10–15% more than the calculated weld metal weight for FCAW; 35–40% more for SMAW.

**Plate weight tables are faster and good enough.** Professional estimators don't recalculate density × volume every time. They memorize or reference the kg/m² for each common thickness. Tape measure × kg/m² table = weight in seconds. Use the formula to verify the table or calculate unusual thicknesses.

**Fillet weld size ≠ fillet weld throat.** A 10 mm fillet weld has legs of 10 mm but the effective throat is only 10 × 0.707 = 7.07 mm. The cross-sectional area used for volume calculation is the actual deposited area — the triangle of weld metal, which is 0.5 × leg × leg = 0.5 × 10 × 10 = 50 mm². Some estimating references calculate differently — make sure you know which definition your reference is using.

---

## Key terms

- **Density (steel):** mass per unit volume = 7.85 g/cm³ — the key constant for steel weight calculation
- **Deposition efficiency:** fraction of purchased filler metal that actually ends up as weld metal in the joint (remainder = spatter, slag, stub loss)
- **Weld cross-sectional area:** the cross-sectional area of the weld deposit, used to calculate volume of filler metal
- **Volume of weld:** cross-sectional area × weld length — tells you total weld metal volume needed
- **Tangent (tan θ):** trigonometric ratio of opposite to adjacent in a right triangle — used for angular-to-linear conversion
- **Slope correction:** actual weld length = horizontal length / cos(θ) — accounts for the extra material consumed on inclined welds
- **Arc length:** radius × angle in radians — used for curved weld seam length estimates
- **Labour rate:** cost per hour charged for welding work, including overhead — typically $65–$120/hr in Alberta fabrication[^1]

---

## Common exam trap

- **Deposition efficiency for SMAW is ~65%, not 100%** — stub loss + slag + spatter removes ~35% of the electrode. Exam may offer "95%" (GMAW) as the value for SMAW.
- **Steel density = 7.85 g/cm³** — not 8.0, not 7.5. This number must be right or every weight calculation is wrong.
- **Actual weld length on inclined surfaces is LONGER than horizontal run** — divide by cos(θ). Exam may ask for filler consumption on an inclined weld and list the horizontal distance as a distractor answer.
- **Fillet weld area = 0.5 × leg²** (for equal leg fillets) — not leg × leg (that's the full square, not the triangle).
- **Plate weight per m²:** 12 mm plate ≠ 12 × 7.85 = 94.2 kg/m², NOT 94.2 g/m². Units must be consistent — if thickness is in mm, multiply by 7.85 and the result is kg/m² if you've used the weight formula correctly.

---

## Practice question preview

**Q:** A welder needs to estimate filler wire required for 30 metres of 10 mm fillet welds using GMAW at 92% deposition efficiency. The cross-sectional area of a 10 mm fillet weld is approximately 50 mm². Steel density = 7.85 g/cm³. How much GMAW wire must be purchased?

A) Approximately 11.8 kg
B) Approximately 12.8 kg
C) Approximately 14.0 kg
D) Approximately 17.7 kg

**Correct: B**

**Explanation:**
1. Volume of weld = 50 mm² × 30,000 mm = 1,500,000 mm³ = 1500 cm³
2. Weight of weld metal = 1500 cm³ × 7.85 g/cm³ = 11,775 g = 11.78 kg
3. Wire consumed = weld metal weight / deposition efficiency = 11.78 / 0.92 = **12.8 kg**

(A) 11.8 kg is the weld metal weight only — doesn't account for deposition efficiency losses. (C) 14.0 kg would suggest lower deposition efficiency (~84%, more typical of FCAW). (D) 17.7 kg would represent SMAW deposition efficiency (~65%), which is incorrect for GMAW.

**Red Seal mapping:** A-4.03 (Plans job tasks); A-4.04 (Organizes materials)

---

[^1]: [Modern Welding, 12th ed. (Bowditch, Goodheart-Willcox)](https://www.g-w.com/modern-welding), Chapter 9 — Estimating and Costing; material weight calculation, steel density, angular-to-linear conversion, gas consumption rules of thumb
[^2]: [CWB Group — Welder Certification Study Guide](https://www.cwbgroup.org/education/learning-resources); estimation fundamentals, filler metal consumption approach, weld joint cost concepts
[^3]: [Lincoln Electric — Weld Cost Calculator Guide](https://www.lincolnelectric.com/en/tools-and-calculators/welding-calculator); deposition efficiency by process (SMAW ~65%, GMAW ~93%, FCAW ~85%), weld volume method for filler consumption
[^4]: [AIT Welder Curriculum Guide 012 (2026), Period 2 Section 2 Topic D](https://tradesecrets.alberta.ca/SOURCES/PDFS/CURRICULUM_GUIDES/012_OUTLINE.PDF), pp. 43–44
