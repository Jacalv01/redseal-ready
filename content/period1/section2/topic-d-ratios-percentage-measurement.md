---
id: p1-s2-d
period: 1
section: 2
section_title: Drafting, Drawings and Specifications
topic_letter: D
topic_title: Ratios, Percentage and Measurement Systems
hours: 6
weight_pct: 3
outcome: >
  Upon successful completion, learners will be able to solve problems using ratios,
  proportions, and percentages; identify and convert between fractions, decimals,
  percentages, and units of measure.
objectives:
  - Convert between fractions, decimals and percentages.
  - Solve percentage problems.
  - Calculate ratio problems: two quantities in the form of a ratio and two ratios in the form of a proportion.
  - Identify metric units of measure.
  - Convert imperial units: feet to inches, square inches to square feet, and cubic measures to gallons.
  - Convert between units of measure.
red_seal_mapping:
  - B-7.02 (Transfers dimensions from drawings to materials)
  - B-8.01 (Prepares materials)
  - D-13.03 (Sets operating parameters for SMAW equipment)
  - D-14.03 (Sets operating parameters for FCAW, MCAW and GMAW)
citations:
  - source: AIT Welder Curriculum Guide 012 (2026), Period 1 Section 2 Topic D
    ref: pp. 57–65 (ratios, percentages, measurement systems)
    url: https://tradesecrets.alberta.ca/SOURCES/PDFS/CURRICULUM_GUIDES/012_OUTLINE.PDF
  - source: Modern Welding (Bowditch, Goodheart-Willcox, latest edition)
    ref: Appendix A (Math for Welders — ratios, proportions, unit conversion, percentage)
    url: https://www.goodheartwillcox.com/products/modern-welding
  - source: Miller Electric — Weld Setting Calculators (public)
    ref: Duty cycle percentage; wire feed speed ratio calculations
    url: https://www.millerwelds.com/resources/welding-calculators
  - source: Lincoln Electric — Procedure Handbook of Arc Welding (public)
    ref: Electrode efficiency, deposition rate, duty cycle discussions
    url: https://www.lincolnelectric.com/en/education-center/welding-education/procedure-handbook
  - source: CSA W117.2 — Safety in Welding, Cutting and Allied Processes (2019)
    ref: Exposure limits for welding fumes as mg/m³ and ppm — percentage and ratio concepts
    url: https://www.csagroup.org/store/product/CSA%20W117.2%3A19/
---

# Ratios, Percentage and Measurement Systems

These aren't abstract math concepts — they show up directly in welding work. Duty cycle is a percentage. Electrode deposition efficiency is a ratio. Shielding gas mixes are percentages (75/25 Ar/CO₂). Scale on a drawing is a ratio. Converting a measurement from metric to imperial is unit conversion. You will use every concept in this lesson before the end of your apprenticeship.

---

## Fractions, Decimals, and Percentages — the conversion triangle

These three are the same value expressed three different ways. Converting between them is a fundamental skill.[^2]

### Fraction → Decimal → Percentage

| Step | Operation | Example: 3/4 |
|---|---|---|
| Fraction → Decimal | Divide numerator by denominator | 3 ÷ 4 = **0.75** |
| Decimal → Percentage | Multiply by 100 (move decimal 2 places right) | 0.75 × 100 = **75%** |

### Percentage → Decimal → Fraction

| Step | Operation | Example: 60% |
|---|---|---|
| Percentage → Decimal | Divide by 100 (move decimal 2 places left) | 60 ÷ 100 = **0.60** |
| Decimal → Fraction | Write over power of 10, simplify | 60/100 = 3/5 |

**Quick reference table:**

| Fraction | Decimal | Percentage | Welding context |
|---|---|---|---|
| 1/4 | 0.25 | 25% | 25% CO₂ in 75/25 Ar/CO₂ mix |
| 3/4 | 0.75 | 75% | 75% Argon in 75/25 mix |
| 3/5 | 0.60 | 60% | Standard welder duty cycle |
| 1/10 | 0.10 | 10% | CO₂ in 90/10 Ar/CO₂ mix |
| 9/10 | 0.90 | 90% | Argon in 90/10 Ar/CO₂ mix |
| 1/2 | 0.50 | 50% | 50% duty cycle on some machines |

---

## Ratios — comparing two quantities

A ratio compares two quantities of the same type using the format A:B (read "A to B").[^2]

**Ratio examples in welding:**

| Situation | Ratio | Meaning |
|---|---|---|
| Shielding gas mix | 75:25 (Ar:CO₂) | For every 75 parts Argon, 25 parts CO₂ |
| Drawing scale | 1:10 | 1 mm on drawing = 10 mm on the actual part |
| Bevel angle | 1:2 | Rise to run ratio on a cut bevel |
| Deposition rate | 3:1 | For every 3 kg of electrode, 1 kg is losses (slag, spatter, stub) — remainder is deposited |
| Fillet weld leg ratio | 1:1 | Equal-leg fillet weld (45° throat line) |

### Reading a ratio correctly

A ratio of 3:1 does NOT mean 3 is 3× bigger than 1. It means: for every 1 unit of B, there are 3 units of A. In a 3:1 electrode-to-deposition ratio:
- Total = 3 + 1 = 4 parts
- 3 parts deposited, 1 part lost
- Deposition efficiency = 3/4 = **75%**[^4]

---

## Proportions — solving for an unknown in a ratio

A proportion states that two ratios are equal: A:B = C:D, or A/B = C/D.

**Cross-multiplication method:** A × D = B × C

**Welding example — scaling from drawing:**
A drawing at scale 1:20 shows a weld length of 12.5 mm on the drawing. What is the actual weld length?

Set up the proportion: 1/20 = 12.5/x

Cross multiply: 1 × x = 20 × 12.5 = 250

**Actual weld length = 250 mm**[^1]

**Welding example — amperage scaling:**
Your reference table shows that 3/8 inch thick mild steel welds well with E7018 at 140 A. You need to weld 1/2 inch thick material. If the required amperage scales proportionally with thickness, what would the estimated starting amperage be?

Set up proportion: 140/0.375 = x/0.500

Cross multiply: 140 × 0.500 = 0.375 × x

70 = 0.375x

x = 70/0.375 = **186.7 A**

Round to **185–190 A** (confirm with electrode manufacturer's data table).[^3]

Note: amperage scales roughly with thickness for the same electrode classification, but this is an estimate only — always verify with the electrode manufacturer's amperage table for the specific electrode diameter.

---

## Percentage problems — three types

Every percentage problem is one of three types. Know which question you're answering.[^2]

### Type 1: Find the percentage OF a number
**"What is X% of Y?"**
Formula: (X/100) × Y

**Example:** A 200 A welding machine has a 60% duty cycle. How many amperes is 60% of full capacity?
Already stated: the machine is rated at 200 A at 60% duty cycle — you use the full 200 A. Duty cycle affects time-on, not current level.

Better example: Argon makes up 75% of a shielding gas supply cylinder containing 40 cubic feet of gas. How many cubic feet is argon?
(75/100) × 40 = 0.75 × 40 = **30 cubic feet Argon**[^3]

### Type 2: Find what percentage one number is of another
**"X is what % of Y?"**
Formula: (X/Y) × 100

**Example:** A 300 A machine can weld continuously for 6 minutes out of every 10. What is the duty cycle?
(6/10) × 100 = **60% duty cycle**[^3]

### Type 3: Find the whole when a percentage and part are known
**"X is Y% of what?"**
Formula: Whole = Part / (Y/100)

**Example:** You deposited 15 kg of weld metal. This represents 80% of the total electrode weight consumed (20% went to slag, spatter, and stub ends). How many kg of electrode was consumed?
Whole = 15 / 0.80 = **18.75 kg of electrode**[^4]

---

## Duty cycle — the critical percentage for power sources

Duty cycle is expressed as a percentage of a 10-minute period.[^3] [^4]

**Formula:**

```
Duty Cycle % = (Minutes welding per 10 minutes) × 10
```

Or equivalently:

```
Minutes on (per 10 min) = Duty Cycle % / 10
```

**Example — 60% duty cycle:**
- Weld: 6 minutes
- Rest/cool: 4 minutes
- Then repeat

**Important:** Duty cycle is rated at a specific amperage. If you reduce the amperage below the rating, duty cycle improves. If you increase the amperage above the rating, duty cycle drops (you risk overheating the machine).[^3]

**The "constant × duty cycle formula" for amperage change:**

The relationship between amperage and duty cycle (approximately): (I₁)² × D₁ = (I₂)² × D₂

Where I = amperage and D = duty cycle as a decimal.

**Example:** A machine is rated 300 A at 60% duty cycle. What is the available duty cycle at 260 A?

(300)² × 0.60 = (260)² × D₂

90,000 × 0.60 = 67,600 × D₂

54,000 = 67,600 × D₂

D₂ = 54,000 / 67,600 = **0.799 = ~80% duty cycle**

At lower amperage, duty cycle improves significantly.[^3]

---

## Metric units of measure

The SI (metric) system is used in most Canadian industry, codes, and engineering drawings alongside imperial.[^1]

### Length

| Unit | Symbol | Relationship |
|---|---|---|
| Millimetre | mm | Base unit for welding dimensions |
| Centimetre | cm | 10 mm = 1 cm |
| Metre | m | 1000 mm = 1 m |
| Kilometre | km | 1000 m = 1 km |

**Common welding dimensions in metric:**
- Weld size: mm (6 mm fillet, 10 mm throat)
- Plate thickness: mm (6 mm, 10 mm, 12.5 mm, 25 mm)
- Root opening: mm (2 mm typical groove root)
- Electrode diameter: mm (2.5 mm, 3.2 mm, 4.0 mm, 4.8 mm)

### Mass / weight

| Unit | Symbol | Notes |
|---|---|---|
| Gram | g | Small amounts — electrode stub weight |
| Kilogram | kg | Electrode spools, weld metal deposition |
| Tonne (metric) | t | 1000 kg — structural steel quantities |

### Temperature

- **Celsius (°C):** standard in Canada
- **Kelvin (K):** scientific; 0°C = 273.15 K
- **Preheat and interpass temperatures in welding:** always in °C[^5]

### Pressure (for gases)

- **kPa:** kilopascals (cylinder pressures, regulator output)
- **Bar:** 1 bar ≈ 100 kPa ≈ 14.5 psi
- **Flow rates:** L/min (metric) or CFH/CFM (imperial)

---

## Unit conversions — imperial

### Length conversions

| To convert | Multiply by | Example |
|---|---|---|
| Feet → Inches | × 12 | 3 ft × 12 = 36 in |
| Inches → Feet | ÷ 12 | 18 in ÷ 12 = 1.5 ft |
| Inches → mm | × 25.4 | 1/4 in × 25.4 = 6.35 mm |
| mm → Inches | ÷ 25.4 | 10 mm ÷ 25.4 = 0.394 in |
| Feet → Metres | × 0.3048 | 10 ft × 0.3048 = 3.048 m |

### Area conversions

| To convert | Multiply by |
|---|---|
| Square inches → Square feet | ÷ 144 |
| Square feet → Square inches | × 144 |
| Square inches → cm² | × 6.452 |

**Example:** A plate is 36 in × 96 in. What is its area in square feet?
Area = 36 × 96 = 3,456 sq in ÷ 144 = **24 square feet**[^2]

### Volume and liquid measure

| To convert | Multiply by |
|---|---|
| Cubic inches → Gallons (US) | ÷ 231 |
| Gallons (US) → Cubic inches | × 231 |
| Cubic feet → Gallons (US) | × 7.481 |
| Litres → Gallons (US) | × 0.2642 |
| Gallons (US) → Litres | × 3.785 |

**Example:** A coolant reservoir holds 2,772 cubic inches. What is its capacity in US gallons?
2,772 ÷ 231 = **12 US gallons**[^2]

---

## Metric/imperial quick-conversion shortcuts for the field

| Imperial | Metric (approx.) | Note |
|---|---|---|
| 1 inch | 25.4 mm | Exact |
| 1 foot | 305 mm | Approx (exact: 304.8 mm) |
| 1 lb | 0.454 kg | Exact to 3 sig figs |
| 1 kg | 2.205 lb | Exact to 4 sig figs |
| 1 US gallon | 3.785 L | Exact |
| 1 CFH (cubic foot/hour) | 0.472 L/min | For gas flow rates |
| 1 psi | 6.895 kPa | For pressure conversion |

---

## Numbers you need to memorize

- **Fraction → %:** divide numerator by denominator × 100[^2]
- **% → decimal:** divide by 100[^2]
- **Duty cycle:** weld minutes / 10 minutes × 100%; standard rating period = 10 minutes[^3]
- **Standard duty cycle for many MIG machines: 60% at rated amperage**[^3]
- **1 inch = 25.4 mm exactly**[^2]
- **1 foot = 12 inches; 1 square foot = 144 square inches; 1 cubic foot = 1,728 cubic inches**[^2]
- **1 US gallon = 231 cubic inches**[^2]
- **1 CFH = 0.472 L/min** (for shielding gas flow conversion)[^2]
- **75/25 Ar/CO₂ = 75% Argon + 25% CO₂ — most common GMAW shielding gas**[^3]

---

## What the textbook doesn't tell you

**Duty cycle ratings are conservative — most modern inverters far exceed them.** The 60% duty cycle at 300 A is a minimum guarantee. In practice, many inverter-based machines (Miller Deltaweld, Lincoln PowerWave series) can sustain far higher duty cycles at lower amperages. However, running at rated amperage continuously on an underpowered extension cord is the fastest way to overheat a machine and void the warranty.[^3]

**Metric drawings with imperial fasteners are common in Canadian fabrication** — especially in oil and gas. You'll see a metric structural drawing with ANSI/ASME 3/8-16 UNC bolt holes. Know both systems and never assume a drawing is purely one or the other. If it says "M12" it's metric; if it says "1/2 dia." it's imperial; if it says "Ø 13.5" it could be a metric hole for an imperial bolt (clearance hole). Ask before drilling.[^1]

**Shielding gas mix percentages affect weld characteristics significantly.** This isn't just a math concept — changing from 75/25 to 90/10 Ar/CO₂ reduces spatter and changes the arc characteristics at the same parameters. When your welding engineer specifies a shielding gas percentage, they've chosen it for a reason — verify your cylinder label before connecting.[^4]

---

## Key terms

- **Ratio:** a comparison of two quantities (A:B or A/B)
- **Proportion:** a statement that two ratios are equal (A:B = C:D)
- **Cross-multiplication:** solving a proportion by multiplying across (A × D = B × C)
- **Percentage:** a ratio expressed as parts per 100; indicated by the % symbol
- **Duty cycle:** the percentage of a 10-minute period that a machine can weld at its rated amperage without overheating
- **SI (Système International):** the metric system — mm, kg, °C, Pa, L
- **Imperial system:** inches, feet, pounds, Fahrenheit, gallons
- **Unit conversion:** multiplying a measurement by a conversion factor to express it in different units while keeping the same value

---

## Common exam trap

- **"Duty cycle means the machine welds 60% of the time all day"** — wrong. Duty cycle is based on a 10-minute cycle, not an 8-hour shift. A 60% machine welds 6 of every 10 minutes, then needs 4 minutes to cool.
- **"75/25 means 75% CO₂ and 25% Argon"** — wrong. The convention in North America is Argon listed first, then CO₂. 75/25 Ar/CO₂ = 75% Argon, 25% CO₂. Reversing this is an exam trap and a real-world gas mix error.
- **"1 foot = 10 inches"** — a decimal-system confusion. In metric, 10 units make the next unit. In imperial, 12 inches = 1 foot. 144 sq in = 1 sq ft. 1,728 cubic inches = 1 cubic foot.
- **Proportion cross-multiplication direction:** "A/B = C/D → A×C = B×D" is wrong. Cross-multiplication is A×D = B×C (opposite corners multiply).

---

## Practice question preview

**Q:** A welding power source is rated at 250 A at 60% duty cycle. A welder runs this machine continuously at 250 A for 8 minutes, then takes a 2-minute break. Is this within the duty cycle rating?

A) Yes — the machine is rated at 60% and 8 out of 10 minutes = 80%  
B) No — 8 minutes on is 80% duty cycle, which exceeds the 60% rating  
C) Yes — total time in the hour is within limit  
D) No — the machine should never exceed 6 minutes of welding without checking  

**Correct: B**

**Explanation:** Duty cycle is based on a 10-minute cycle. 8 minutes on / 10 minutes total = 80% duty cycle. This exceeds the 60% rating at 250 A, which allows only 6 minutes on / 4 minutes off. Running at 80% duty cycle on a 60%-rated machine risks overheating the transformer or inverter. The correct operation is 6 minutes welding, 4 minutes cooling, then repeat. Option A correctly identifies 80% but incorrectly says this is within the 60% rating. Option C is irrelevant — duty cycle isn't calculated per hour. Option D is the correct action (6 minutes is the max) but is stated misleadingly.

**Red Seal mapping:** D-13.03 (Sets operating parameters for SMAW equipment — understands duty cycle limitations of welding power sources)

---

[^1]: [AIT Welder Curriculum Guide 012 (2026)](https://tradesecrets.alberta.ca/SOURCES/PDFS/CURRICULUM_GUIDES/012_OUTLINE.PDF), Period 1 Section 2 Topic D: metric and imperial units, unit conversion in welding layout, drawing scale as a ratio, proportion problems for layout
[^2]: [Modern Welding (Bowditch, Goodheart-Willcox)](https://www.goodheartwillcox.com/products/modern-welding), Appendix A "Math for Welders": fraction/decimal/percentage conversions, ratio and proportion, unit conversion tables (length, area, volume, mass), worked examples in fabrication context
[^3]: [Miller Electric — Weld Setting Calculators](https://www.millerwelds.com/resources/welding-calculators), duty cycle definition and percentage basis (10-minute cycle), shielding gas mix percentages, wire feed speed ratios; [Miller Electric — Owner's Manuals]: rated amperage and duty cycle specifications
[^4]: [Lincoln Electric — Procedure Handbook of Arc Welding](https://www.lincolnelectric.com/en/education-center/welding-education/procedure-handbook), electrode deposition efficiency ratios, deposition rate calculations, duty cycle at various amperages, shielding gas mix selection
[^5]: [CSA W117.2 — Safety in Welding, Cutting and Allied Processes (2019)](https://www.csagroup.org/store/product/CSA%20W117.2%3A19/), exposure limits for welding fumes expressed as mg/m³ (ppm ratios), ventilation requirements
