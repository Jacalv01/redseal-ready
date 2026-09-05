---
id: p1-s2-e
period: 1
section: 2
section_title: Drafting, Drawings and Specifications
topic_letter: E
topic_title: Geometric Formulas
hours: 12
weight_pct: 5
outcome: >
  Upon successful completion, learners will be able to apply geometric formulas and
  perform calculations to solve problems.
objectives:
  - Identify formulas and solve problems for perimeter, area and volume.
  - Calculate the weight of a solid.
  - Calculate the capacity of a container in gallons and liters.
red_seal_mapping:
  - B-7.02 (Transfers dimensions from drawings to materials)
  - B-8.01 (Prepares materials)
  - B-8.02 (Fits components for welding)
citations:
  - source: AIT Welder Curriculum Guide 012 (2026), Period 1 Section 2 Topic E
    ref: pp. 66–80 (geometric formulas — perimeter, area, volume, weight, capacity)
    url: https://tradesecrets.alberta.ca/SOURCES/PDFS/CURRICULUM_GUIDES/012_OUTLINE.PDF
  - source: Modern Welding (Bowditch, Goodheart-Willcox, latest edition)
    ref: Appendix A (Math for Welders — geometry, perimeter, area, volume formulas with welding examples)
    url: https://www.goodheartwillcox.com/products/modern-welding
  - source: Lincoln Electric — Procedure Handbook of Arc Welding (public)
    ref: Weld cross-section area calculations, weight of deposited metal calculations
    url: https://www.lincolnelectric.com/en/education-center/welding-education/procedure-handbook
  - source: Miller Electric — Welding Reference (public)
    ref: Material weight and weld volume reference charts for mild steel
    url: https://www.millerwelds.com/resources/article-library
---

# Geometric Formulas

A welder without geometry is guessing at material quantities, weld metal weights, and container capacities. Can you calculate how much steel you need to order? Can you figure out how many kilos of filler metal a groove weld will consume? Can you determine if a tank has enough capacity? All of those use the formulas in this lesson. The 12 hours allocated to this topic in the AIT curriculum reflects how heavily it's used in real fabrication work.

---

## Perimeter — the distance around the outside

Perimeter is the total length of all sides of a flat shape. You use it for estimating weld run length, cutting lengths, and material requirements.[^1]

### Perimeter formulas

| Shape | Formula | Variables |
|---|---|---|
| **Rectangle** | P = 2(L + W) | L = length, W = width |
| **Square** | P = 4s | s = side length |
| **Triangle** | P = a + b + c | a, b, c = all three sides |
| **Circle (Circumference)** | C = π × d = 2πr | d = diameter, r = radius, π ≈ 3.1416 |
| **Regular polygon** | P = n × s | n = number of sides, s = side length |

**Welding example — total weld length on a frame:**

A rectangular steel frame is 1,200 mm × 800 mm. You need to weld all four corners and along the full perimeter of the top cap plate. How long is the continuous weld run?

P = 2(1,200 + 800) = 2(2,000) = **4,000 mm = 4.0 m** of weld[^1]

**Welding example — pipe circumference:**

A 4-inch nominal pipe (4.5 inch OD = 114.3 mm OD) requires a full circumferential weld. How long is the weld bead?

C = π × d = 3.1416 × 114.3 mm = **358.9 mm ≈ 359 mm of weld**

---

## Area — the space enclosed by a 2D shape

Area calculations tell you material quantity (plate area to order), weld cross-section (to calculate weld metal volume), and opening sizes.[^1] [^2]

### Area formulas

| Shape | Formula | Variables |
|---|---|---|
| **Rectangle** | A = L × W | L = length, W = width |
| **Square** | A = s² | s = side length |
| **Triangle** | A = (b × h) / 2 | b = base, h = height (perpendicular to base) |
| **Circle** | A = π × r² | r = radius (= diameter/2) |
| **Trapezoid** | A = (a + b)/2 × h | a, b = parallel sides, h = height between them |
| **Parallelogram** | A = b × h | b = base, h = perpendicular height |
| **Ring (annulus)** | A = π(R² − r²) | R = outer radius, r = inner radius |

**π = 3.14159… Use 3.1416 unless you need more precision.**

---

### Worked example 1 — plate area for material order

**Scenario:** You need to cut 12 gusset plates, each one a right triangle with a base of 150 mm and height of 150 mm. How much total plate area do you need (in mm²)?

Area of one triangle = (150 × 150) / 2 = 22,500 / 2 = **11,250 mm²**

Total for 12 pieces = 12 × 11,250 = **135,000 mm²**

Convert to m²: 135,000 / 1,000,000 = **0.135 m²**

In practice, you'd add 10–15% for saw kerf and waste → order at least 0.155 m² of plate.[^1]

---

### Worked example 2 — cross-section area of a fillet weld

**Scenario:** Calculating weld metal volume (and later weight) for a 10 mm equal-leg fillet weld.

The cross-section of an equal-leg fillet weld is a right isosceles triangle with legs equal to the fillet size.

Area = (leg × leg) / 2 = (10 mm × 10 mm) / 2 = **50 mm²**

For a 500 mm long fillet weld:
Volume = 50 mm² × 500 mm = **25,000 mm³** = 25 cm³ of weld metal[^3]

---

### Worked example 3 — circular plate area

A circular cover plate has a 400 mm diameter. What is its area?

r = 400/2 = 200 mm

A = π × r² = 3.1416 × (200)² = 3.1416 × 40,000 = **125,664 mm²** ≈ 125,700 mm² ≈ **0.126 m²**

---

## Volume — the space inside a 3D shape

Volume tells you the capacity of a container, the quantity of concrete or fill material, or the volume of weld metal to be deposited.[^1] [^2]

### Volume formulas

| Shape | Formula | Variables |
|---|---|---|
| **Rectangular prism (box)** | V = L × W × H | L = length, W = width, H = height |
| **Cube** | V = s³ | s = side length |
| **Cylinder** | V = π × r² × h | r = radius, h = height/length |
| **Cone** | V = (π × r² × h) / 3 | r = base radius, h = height |
| **Sphere** | V = (4/3) × π × r³ | r = radius |
| **Triangular prism** | V = (b × h / 2) × L | b = triangle base, h = triangle height, L = prism length |

---

### Worked example 4 — volume of weld metal in a groove weld

**Scenario:** You're welding a V-groove joint in 20 mm thick plate. The groove is a 60° included angle, with a 2 mm root opening and 1 mm root face. The weld is 1,200 mm long.

Step 1: Find the cross-sectional area of the groove.

The groove above the root face is essentially a triangle. Root opening = 2 mm; plate depth used by groove = 20 − 1 = 19 mm. At 60° included angle (30° per side), the groove width at the top = 2 × (19 × tan 30°) + root opening.

tan 30° = 0.5774

Width at top = 2 × (19 × 0.5774) + 2 = 2 × 10.97 + 2 = 21.94 + 2 = **23.94 mm at top**

Cross-section area ≈ trapezoid: (top width + root opening)/2 × groove depth = (23.94 + 2)/2 × 19 = 12.97 × 19 = **246.4 mm²**

Step 2: Volume = area × length = 246.4 × 1,200 = **295,680 mm³ ≈ 296 cm³**

This is the volume of weld metal needed to fill the groove (before efficiency losses).[^3]

---

## Weight of a solid — the most important calculation for material estimating

**Weight = Volume × Density**[^1] [^2]

For **mild steel:** density = **7.85 g/cm³ = 7,850 kg/m³**[^2]

This is the number welders and fabricators use constantly for material takeoffs. It's safe to memorize.

### Unit conversions needed:

- mm³ → cm³: divide by 1,000
- cm³ → m³: divide by 1,000,000
- kg/m³ → g/cm³: same number value divided by 1,000 (7,850 kg/m³ = 7.85 g/cm³)

### Worked example 5 — weight of a steel plate

**Scenario:** How much does a 1,200 mm × 600 mm × 10 mm mild steel plate weigh?

Step 1: Volume in cm³:
Convert dimensions to cm: 120 cm × 60 cm × 1 cm = **7,200 cm³**

Step 2: Weight = Volume × Density:
7,200 cm³ × 7.85 g/cm³ = 56,520 g = **56.52 kg**

So a standard 1.2 m × 0.6 m × 10 mm plate weighs roughly **56.5 kg**.[^2]

---

### Worked example 6 — weight of weld metal deposited

Using the V-groove from Example 4 (296 cm³ of weld volume):

Weight = 296 cm³ × 7.85 g/cm³ = 2,324 g = **2.32 kg of weld metal**

Now apply electrode deposition efficiency. SMAW E7018 has approximately 65% deposition efficiency (the rest is slag, stub, and spatter).[^3]

Electrode consumed = weld metal weight / efficiency = 2.32 / 0.65 = **3.57 kg of electrode needed**

This is how estimators calculate electrode consumption for a job.[^3]

---

### Worked example 7 — weight of a round bar (cylinder)

**Scenario:** A 50 mm diameter × 3,000 mm long mild steel round bar. How much does it weigh?

Step 1: Volume of cylinder in cm³:
r = 2.5 cm; h = 300 cm
V = π × r² × h = 3.1416 × 6.25 × 300 = 3.1416 × 1,875 = **5,890.5 cm³**

Step 2: Weight = 5,890.5 × 7.85 = 46,240 g = **46.2 kg**[^2]

---

## Capacity of a container — gallons and litres

**Capacity** tells you how much liquid a vessel can hold. This matters for tank fabrication, coolant reservoir sizing, and hydrotest fill calculations.[^1]

### Rectangular tank capacity

**Scenario:** A rectangular steel tank is 800 mm × 500 mm × 600 mm (L × W × H). What is its capacity in litres and US gallons?

Step 1: Volume in mm³ = 800 × 500 × 600 = 240,000,000 mm³

Step 2: Convert to litres: 1 litre = 1,000 cm³ = 1,000,000 mm³
240,000,000 mm³ ÷ 1,000,000 = **240 litres**

Step 3: Convert to US gallons: 1 US gallon = 3.785 litres
240 ÷ 3.785 = **63.4 US gallons**[^1]

### Cylindrical tank capacity

**Scenario:** A cylindrical tank is 1,000 mm diameter × 2,000 mm long (horizontal axis). What is its capacity?

r = 500 mm = 50 cm; h = 200 cm
V = π × r² × h = 3.1416 × 2,500 × 200 = **1,570,800 cm³ = 1,570.8 litres = 414.8 US gallons**

---

## Key formulas summary table

| Calculation | Formula | Unit result |
|---|---|---|
| Perimeter — rectangle | P = 2(L+W) | mm, m, or in |
| Circumference — circle | C = πd | mm, m, or in |
| Area — rectangle | A = L×W | mm², m², in², ft² |
| Area — triangle | A = bh/2 | mm², in² |
| Area — circle | A = πr² | mm², in² |
| Volume — rectangular prism | V = LWH | mm³, cm³, in³ |
| Volume — cylinder | V = πr²h | mm³, cm³, in³ |
| Weight — steel | W = V × 7.85 g/cm³ | grams → kg |
| Capacity — litres | C = V(mm³) ÷ 1,000,000 | litres |
| Capacity — US gallons | C(L) ÷ 3.785 | US gallons |

---

## Numbers you need to memorize

- **π = 3.1416** (to 4 decimal places — sufficient for all welding calculations)[^2]
- **Density of mild steel = 7.85 g/cm³ = 7,850 kg/m³**[^2]
- **1 litre = 1,000 cm³ = 1,000,000 mm³**[^1]
- **1 US gallon = 3.785 litres = 231 cubic inches**[^1]
- **1 Canadian (Imperial) gallon = 4.546 litres** (different from US gallon — know which is specified)[^1]
- **Triangle area = base × height / 2** — the height must be perpendicular to the base[^2]
- **Cylinder volume = πr²h** — radius squared, not diameter squared[^2]
- **SMAW E7018 deposition efficiency ≈ 65%** — used in weld metal weight estimates[^3]

---

## What the textbook doesn't tell you

**Deposition efficiency varies significantly by process.** E7018 SMAW runs about 65%. E6010 is lower, around 60–65%, because of the aggressive dig and spatter. GMAW solid wire is 90–98% efficient (almost no slag, minimal spatter). FCAW gas-shielded is 85–90%. Knowing these ratios lets you estimate consumable costs accurately on a bid.[^3]

**Steel density varies slightly with alloying.** 7.85 g/cm³ is correct for low-carbon mild steel (A36/S275). Stainless steel is approximately 7.93–8.0 g/cm³ depending on grade. Aluminum is 2.70 g/cm³ — approximately 1/3 the weight of steel. High-strength low-alloy steels are close enough to 7.85 for estimating purposes.[^2]

**Tank capacity calculations must account for the shell and head thickness.** When you calculate the internal volume of a fabricated tank, you need the INSIDE dimensions — not the outside. A 1,000 mm OD tank with 10 mm wall thickness has an inside diameter of 980 mm and inside radius of 490 mm. The difference in volume: π × (490)² vs. π × (500)² = 754,296 vs. 785,398 mm² cross-section — about a 4% difference. For a precision capacity calculation, always use inside dimensions.[^3]

---

## Key terms

- **Perimeter:** the total length around the outside of a 2D shape
- **Circumference:** the perimeter of a circle (C = πd)
- **Area:** the 2D space enclosed by a shape — measured in square units (mm², m², in²)
- **Volume:** the 3D space enclosed by a solid — measured in cubic units (mm³, cm³, m³, in³)
- **π (pi):** the ratio of a circle's circumference to its diameter; ≈ 3.1416
- **Density:** mass per unit volume — for mild steel: 7.85 g/cm³
- **Deposition efficiency:** the percentage of electrode weight that becomes actual weld metal; the remainder is slag, spatter, and stub
- **Capacity:** the volume of liquid a container can hold, expressed in litres or gallons

---

## Common exam trap

- **"Cylinder volume = π × d² × h"** — wrong. The formula uses radius squared: V = π × r². If you use diameter without halving it first, your answer is 4× too large.
- **"Density of steel = 7.85 kg/cm³"** — the units are wrong. Steel density is 7.85 g/cm³ (grams per cubic centimetre) or 7,850 kg/m³. Using kg/cm³ would give an answer 1,000 times smaller.
- **"1 Canadian gallon = 1 US gallon"** — false. A Canadian (Imperial) gallon = 4.546 L; a US gallon = 3.785 L. The difference is about 20%. When a drawing says "gallon," check the origin of the drawing.
- **"Area of a fillet weld cross-section = leg × leg"** — this is the full square, not the triangle. The fillet cross-section is a right triangle: A = (leg × leg) / 2.
- **Triangle area height:** must be the perpendicular height, not the hypotenuse. A = base × perpendicular height / 2.

---

## Practice question preview

**Q:** A fabricator needs to calculate the weight of a mild steel rectangular pad plate measuring 300 mm × 200 mm × 20 mm. Using a steel density of 7.85 g/cm³, what is the approximate weight?

A) 9.42 kg  
B) 12.57 kg  
C) 94.2 kg  
D) 3.14 kg  

**Correct: A**

**Explanation:**
Step 1: Volume = 30 cm × 20 cm × 2 cm = 1,200 cm³
Step 2: Weight = 1,200 × 7.85 = 9,420 g = **9.42 kg**

Option B (12.57 kg) results from forgetting to convert mm to cm (leaving dimensions as 300×200×20 = 1,200,000 but then misapplying density). Option C (94.2 kg) is 10× too large — an error from not converting mm to cm before cubing. Option D (3.14 kg) appears to use π incorrectly.

**Red Seal mapping:** B-7.02 (Transfers dimensions from drawings to materials — calculates material weight and volume for fabrication takeoffs)

---

[^1]: [AIT Welder Curriculum Guide 012 (2026)](https://tradesecrets.alberta.ca/SOURCES/PDFS/CURRICULUM_GUIDES/012_OUTLINE.PDF), Period 1 Section 2 Topic E: perimeter, area and volume formulas, container capacity in gallons and litres, weight of a solid
[^2]: [Modern Welding (Bowditch, Goodheart-Willcox)](https://www.goodheartwillcox.com/products/modern-welding), Appendix A "Math for Welders": π = 3.1416, steel density = 7.85 g/cm³, area and volume formula tables with worked examples for plates, rounds, and cylinders
[^3]: [Lincoln Electric — Procedure Handbook of Arc Welding](https://www.lincolnelectric.com/en/education-center/welding-education/procedure-handbook), weld cross-section area for volume and weight calculations, electrode deposition efficiency by process (SMAW E7018 ≈65%, GMAW ≈95%), groove weld volume estimation method
[^4]: [Miller Electric — Welding Reference](https://www.millerwelds.com/resources/article-library), material weight charts for mild steel plate and structural shapes, weld metal volume estimation tools
