---
id: p2-s2-e
period: 2
section: 2
section_title: Drafting, Drawings and Specifications
topic_letter: E
topic_title: Project Estimating
hours: 9
weight_pct: 4
outcome: >
  Upon successful completion, learners will be able to develop a project estimate.
objectives:
  - Determine total costs for a project.
  - Develop a project estimate.
red_seal_mapping:
  - A-4.03 (Plans job tasks)
  - A-4.04 (Organizes materials)
  - B-8.01 (Prepares materials)
citations:
  - source: Modern Welding (Bowditch, Goodheart-Willcox, 12th ed.)
    ref: Chapter 9 — Estimating; project cost breakdown, bill of materials, labour estimation, overhead and markup
    url: https://www.g-w.com/modern-welding
  - source: CWB Group — Welder Certification Study Guide
    ref: Project cost components, takeoff process, estimate structure for welded fabrications
    url: https://www.cwbgroup.org/education/learning-resources
  - source: Lincoln Electric — Weld Cost Calculator Guide
    ref: Weld travel speed data, deposition rates, cost-per-metre calculation methodology
    url: https://www.lincolnelectric.com/en/tools-and-calculators/welding-calculator
  - source: AIT Welder Curriculum Guide 012 (2026), Period 2 Section 2 Topic E
    ref: pp. 44–46
    url: https://tradesecrets.alberta.ca/SOURCES/PDFS/CURRICULUM_GUIDES/012_OUTLINE.PDF
---

# Project Estimating

A project estimate is what separates a shop that makes money from one that doesn't. The estimate tells the customer what it will cost, tells the shop what resources to reserve, and tells the foreman how long each step should take. A welder who understands estimating is worth more to any employer — they can run a job instead of just executing tasks. And on the Red Seal exam, project estimating questions test whether you can work through a multi-step cost calculation without getting lost.

---

## The components of a project estimate

Every project cost has the same structure.[^1][^2]

### 1. Material costs

**Structural steel and plate:**
- Take off quantities from drawings: lengths, widths, thicknesses
- Calculate weight (kg) using density formula: kg = volume (cm³) × 7.85 / 1000
- Apply current steel price ($/kg) — varies by grade, section type, market
- Add 5–10% waste allowance for cuts, ends, and nesting scrap

**Pipe:**
- Quantify by length (metres) and size (NPS + schedule)
- Use published pipe weight tables (kg/m per size/schedule)
- Calculate from purchased length, not just weld length

**Filler metals:**
- Calculate weld volume (area × length) for each joint type
- Apply filler density (7.85 g/cm³)
- Divide by deposition efficiency (SMAW ~65%, GMAW ~92%, FCAW ~85%)
- Price filler by kg from current supplier quote

**Shielding gas:**
- Calculate gas consumption from flow rate (L/min) × arc-on time (minutes)
- For GMAW: typically 25–35 CFH (12–17 L/min); for FCAW-G: 35–50 CFH (17–24 L/min)
- Price by cylinder (T-cylinder ≈ 9 m³; Q-cylinder ≈ 10 m³) or by m³ from bulk

**Consumables:**
- Grinding discs, contact tips, nozzles, tungsten, wire liners
- Rule of thumb: consumables = 10–15% of total filler cost[^1]

### 2. Labour costs

Labour is typically the largest cost component in custom fabrication.[^3]

**Labour calculation:**
> Labour hours = Weld length (m) ÷ Travel speed (m/hr) + Handling time

**Travel speeds (approximate, arc-on only):[^3]**
| Process | Position | Typical travel speed |
|---|---|---|
| SMAW | Flat | 200–350 mm/min |
| SMAW | Vertical up | 100–150 mm/min |
| GMAW | Flat | 400–600 mm/min |
| FCAW | Flat | 300–500 mm/min |
| GTAW | Flat | 100–200 mm/min |

**Operator factor / duty cycle:**
A welder is not welding 100% of the time. Setup, tacks, slag removal, inspection, repositioning — all add time. The **operator factor** is arc-on time ÷ total work time.[^1]

Typical operator factors:
- SMAW production welding: 25–35% arc-on time
- GMAW production welding: 40–55% arc-on time
- FCAW production: 40–55% arc-on time

**Total labour hours = arc-on hours ÷ operator factor**

**Labour cost = total labour hours × shop rate ($/hr)**

Alberta fabrication shop rates (2026 approximate): $85–$120/hr for journeyperson welding, depending on certification, shop overhead, and job type.[^1]

### 3. Equipment costs

- Welding machine: usually absorbed into shop rate (overhead)
- Specialized equipment rentals: crane, positioner, stress-relief furnace — quoted separately
- Consumable tooling: grinding wheels, saw blades — estimate from quantities

### 4. Overhead costs

Overhead is the cost of keeping the shop running that's not directly in the weld: rent, utilities, management salaries, insurance, tooling maintenance. Applied as a **percentage of direct costs** or as part of the shop rate.[^1]

Typical overhead rates in fabrication shops: 100–200% of direct labour cost.

### 5. Profit margin

Added on top of all costs: typically 10–20% for competitive contract work; higher for specialized or emergency work.

---

## Developing a project estimate: step by step

### Step 1: Material takeoff

From the drawings:
1. List all structural shapes, plates, pipes, fittings by type and size
2. Calculate total lengths and weights
3. Note material specifications (A36, A572-50, Grade B pipe, etc.) — affects price
4. Add waste factor (5–10% for plate; 2–5% for structural shapes)

### Step 2: Weld schedule

From the drawings:
1. Identify every weld joint: type (fillet, groove), size (6 mm fillet, single V groove full pen), length
2. Identify welding positions required (1F, 2F, 3G, 5G etc.)
3. Note special requirements: preheat, PWHT, non-destructive testing (RT, UT, MT, PT)
4. Calculate total weld length per joint type and position

### Step 3: Calculate filler metal

For each joint type:
1. Cross-sectional area of weld
2. × weld length = volume
3. × density / deposition efficiency = wire/rod required (kg)
4. × unit cost = filler cost ($)

### Step 4: Calculate arc-on time

For each joint type + position:
1. Total weld length ÷ travel speed = arc-on time
2. Sum all arc-on times

### Step 5: Apply operator factor → total labour hours

Total arc-on time ÷ operator factor = total direct labour hours

### Step 6: Add setup, fit-up, and inspection time

Rule of thumb: 30–50% of weld arc-on time for setup, fit-up, tacking, and visual inspection.
More for complex assemblies; less for simple, repetitive work.[^1]

### Step 7: Calculate labour cost

Total labour hours × shop rate = labour cost

### Step 8: Sum all costs and apply overhead + profit

Total project cost = materials + labour + equipment + overhead + profit

---

## Worked example: small bracket fabrication

**Job:** 10 steel angle brackets, each made from two pieces of 50×50×6 mm angle iron, 300 mm long, joined with a 6 mm fillet weld on two sides (150 mm each side). Process: SMAW.

**Step 1 — Material:**
- Each bracket: 2 pieces × 300 mm = 600 mm per bracket
- 10 brackets: 6000 mm = 6.0 m of 50×50×6 mm angle
- 50×50×6 angle weight: approximately 4.47 kg/m
- Total steel: 6.0 × 4.47 = **26.8 kg**
- At $2.80/kg: material = **$75**

**Step 2 — Weld schedule:**
- Each bracket: 2 sides × 150 mm = 300 mm of 6 mm fillet weld
- 10 brackets: 3000 mm = 3.0 m total weld

**Step 3 — Filler metal:**
- 6 mm fillet area ≈ 18 mm²
- Volume = 18 mm² × 3000 mm = 54,000 mm³ = 54 cm³
- Weight = 54 × 7.85 / 1000 = 0.424 kg weld metal
- SMAW deposition efficiency = 65%: wire required = 0.424 / 0.65 = **0.65 kg** of electrode
- At $7.00/kg for E7018: filler cost = **$4.55**

**Step 4 — Arc-on time:**
- SMAW flat position: 250 mm/min average
- Arc-on = 3000 mm / 250 mm/min = **12 minutes = 0.20 hours**

**Step 5 — Operator factor → labour hours:**
- SMAW operator factor: 30%
- Direct labour hours = 0.20 / 0.30 = **0.67 hours**
- Setup + fit-up: 40% of arc time = 0.08 hrs → 0.75 hrs total

**Step 6 — Labour cost:**
- 0.75 hrs × $90/hr = **$67.50**

**Step 7 — Summary:**
| Cost item | Amount |
|---|---|
| Material (steel) | $75.00 |
| Filler metal | $4.55 |
| Consumables (15% of filler) | $0.68 |
| Labour (direct) | $67.50 |
| Overhead (100% of labour) | $67.50 |
| Subtotal | $215.23 |
| Profit (15%) | $32.28 |
| **Total** | **$247.51** |
| **Per bracket** | **$24.75** |

---

## Numbers you need to memorize

- **SMAW operator factor:** 25–35% arc-on[^1][^3]
- **GMAW operator factor:** 40–55% arc-on[^1][^3]
- **SMAW deposition efficiency:** ~65%[^3]
- **GMAW deposition efficiency:** ~92%[^3]
- **FCAW deposition efficiency:** ~85%[^3]
- **SMAW flat travel speed:** 200–350 mm/min[^3]
- **GMAW flat travel speed:** 400–600 mm/min[^3]
- **Material waste allowance:** 5–10% for plate[^1]
- **Overhead factor (typical):** 100–200% of direct labour[^1]
- **Profit margin (typical competitive fab):** 10–20%[^1]

---

## What the textbook doesn't tell you

**Operator factor is the most commonly underestimated variable.** Students (and inexperienced estimators) assume the welder is welding 80% of the day. Real production welders, even efficient ones, are at 40-55% arc-on for semi-automatic processes — and much less for SMAW. Underestimating operator factor is the fastest way to lose money on a contract.

**Build your estimate from the weld schedule, not the intuition.** Every bid that gets submitted without a weld schedule — a line-by-line list of every joint — is a guess. Experienced fabricators count every metre of weld on the drawing before pricing. One missed significant weld can eliminate the profit on the whole job.

**The estimate becomes the job traveller.** Once the job is won, the estimate's weld schedule turns into a production plan: what gets welded first, by which process, in which position. Shops that track actual hours against estimated hours improve every bid after that. Shops that don't track never know where they made money or where they lost it.

---

## Key terms

- **Material takeoff:** systematic counting and measuring of all materials from drawings to create a material list
- **Bill of Materials (BOM):** complete list of all parts, materials, and quantities required for a job
- **Operator factor:** ratio of arc-on time to total work time; accounts for all non-welding work (setup, cleanup, inspection)
- **Deposition efficiency:** fraction of purchased electrode/wire that becomes weld metal (remainder = spatter, slag, stub)
- **Arc-on time:** time the welding arc is actually burning — does not include setup, slag removal, repositioning
- **Shop rate:** cost per hour for the shop's welding work, including overhead (typically $85–$120/hr in Alberta)
- **Overhead:** indirect costs (rent, utilities, management, insurance) applied as a percentage of direct costs
- **Profit margin:** added percentage above total cost to provide business return (10–20% typical in competitive fabrication)
- **Weld schedule:** comprehensive list of every weld in the job, including type, size, position, and length
- **Waste allowance:** percentage added to material quantities to account for cutting waste, nesting scrap, and offcuts

---

## Common exam trap

- **Operator factor for SMAW is 25–35%, not 80–100%** — "a welder welds 80% of the day" is a common misconception and a common exam distractor.
- **Deposition efficiency must be applied to get PURCHASED filler, not weld metal** — if you calculate weld metal weight and stop there, you've underestimated wire purchase by 15–35%.
- **Labour is calculated from arc-on time ÷ operator factor** — not from arc-on time directly.
- **Overhead is a percentage of DIRECT costs, not of materials alone** — overhead covers all indirect shop expenses, applied proportionally to labour or total direct cost.
- **Profit is added AFTER overhead** — not before. Profit is the last item added, applied to the full cost including overhead.

---

## Practice question preview

**Q:** A welder estimates 45 minutes of arc-on time using GMAW for a job. The operator factor for GMAW is 45%. How many total direct labour hours should be budgeted for this job?

A) 0.75 hours (45 minutes)
B) 1.0 hours
C) 1.67 hours
D) 3.0 hours

**Correct: C**

**Explanation:** Arc-on time = 45 minutes = 0.75 hours. Total labour hours = arc-on hours ÷ operator factor = 0.75 ÷ 0.45 = **1.67 hours**. The operator factor accounts for the fact that a GMAW welder spends only 45% of their time with the arc actually burning — the rest is setup, fit-up, slag/spatter cleanup, repositioning, and inspection. (A) Uses only arc-on time — ignores all non-welding time. (B) Doesn't match the calculation. (D) Would require operator factor of ~25%, which is typical of SMAW, not GMAW.

**Red Seal mapping:** A-4.03 (Plans job tasks)

---

[^1]: [Modern Welding, 12th ed. (Bowditch, Goodheart-Willcox)](https://www.g-w.com/modern-welding), Chapter 9 — Estimating; project cost breakdown, overhead application, profit margin, waste allowance, operator factor concepts
[^2]: [CWB Group — Welder Certification Study Guide](https://www.cwbgroup.org/education/learning-resources); project cost components, takeoff process, estimate structure for welded fabrications
[^3]: [Lincoln Electric — Weld Cost Calculator Guide](https://www.lincolnelectric.com/en/tools-and-calculators/welding-calculator); travel speed data by process and position, deposition efficiency values, operator factor by process
[^4]: [AIT Welder Curriculum Guide 012 (2026), Period 2 Section 2 Topic E](https://tradesecrets.alberta.ca/SOURCES/PDFS/CURRICULUM_GUIDES/012_OUTLINE.PDF), pp. 44–46
