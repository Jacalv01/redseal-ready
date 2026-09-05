---
id: p2-s1-h
period: 2
section: 1
section_title: Foundational Skills, Safety, Procedures and Properties of Metals
topic_letter: H
topic_title: Carbon and Alloy Steels and Alloy Steel Filler Metals
hours: 4
weight_pct: 2
outcome: >
  Upon successful completion, learners will be able to identify and describe carbon and alloy steels and their properties.
objectives:
  - Identify the carbon content and the uses for low, medium and high carbon steel.
  - Describe the effects of carbon content on the weldability of steel.
  - Identify the effects of elements in the properties of carbon steel.
  - Identify the alloying elements in alloy steels.
  - Identify the types, properties and weldability of low alloy steels.
  - Identify the properties and weldability of high strength low alloy steels.
  - Identify alloy steel filler material classifications using AWS and CSA specifications.
  - Identify low alloy steel filler metals and their applications.
red_seal_mapping:
  - A-5.05 (Selects welding processes and power source)
  - D-13.01 (Selects SMAW equipment and consumables)
  - A-5.03 (Controls temperature of weldments)
citations:
  - source: AWS A5.5 — Specification for Low-Alloy Steel Electrodes for Shielded Metal Arc Welding
    ref: E7018-A1, E8018-B2, E9018-B3, E8018-C3, E7018-G classifications, suffix codes
    url: https://pubs.aws.org/p/1144/a55a5-5m2014-specification-for-low-alloy-steel-electrodes-for-shielded-metal-arc-welding
  - source: Lincoln Electric — Welding of Alloy Steels, Procedure Handbook
    ref: Carbon equivalent, preheat tables, Cr-Mo and low-alloy steel welding procedures
    url: https://www.lincolnelectric.com/en/education-center/welding-education/procedure-handbook
  - source: CSA W59 — Welded Steel Construction (2018)
    ref: Table 5 (preheat requirements by carbon equivalent and thickness), Clause 5 and 11 (HSLA provisions)
    url: https://www.csagroup.org/store/product/CSA%20W59%3A18/
  - source: Modern Welding (Bowditch, Goodheart-Willcox, 12th ed.)
    ref: Chapter 21 — Carbon and Alloy Steels; alloying element effects, HSLA steels, CE formula, preheat determination
    url: https://www.g-w.com/modern-welding
  - source: CWB Group — Welder Certification Study Guide
    ref: Alloy steel filler classifications, CSA A5.5 equivalents, preheat for low-alloy steels
    url: https://www.cwbgroup.org/education/learning-resources
  - source: AIT Welder Curriculum Guide 012 (2026), Period 2 Section 1 Topic H
    ref: pp. 33–35
    url: https://tradesecrets.alberta.ca/SOURCES/PDFS/CURRICULUM_GUIDES/012_OUTLINE.PDF
---

# Carbon and Alloy Steels and Alloy Steel Filler Metals

Not all steel welds the same. A structural fabricator welding A36 mild steel plate follows completely different procedures from a pipefitter welding P91 chrome-molybdenum alloy in an oilfield high-temperature line. Understanding carbon content and alloying elements is what separates a welder who knows the rules from one who knows the *reasons behind the rules*.

---

## Carbon content and weldability

Carbon is the most important element in steel for welders. More carbon = harder steel = harder to weld.[^4]

| Category | Carbon content | Typical grade examples | Weldability |
|---|---|---|---|
| **Low carbon (mild steel)** | 0.05–0.25% | A36, 1018, A572-50 | Excellent — no preheat for typical thicknesses |
| **Medium carbon steel** | 0.25–0.60% | 1040, 1045, 1060 | Fair — preheat 100–200°C; low-hydrogen electrodes preferred |
| **High carbon steel** | 0.60–1.4% | 1080, 1095, spring steels | Poor — high preheat (200–350°C+); low-hydrogen mandatory; slow cooling |
| **Tool steel** | 0.60–2.3% | W1, D2, H13 | Very poor — specialist procedure required |

**Why carbon hurts weldability:**
1. Carbon raises the **hardenability** of steel — the tendency to form martensite when quenched
2. Martensite in the HAZ is hard and brittle → **hydrogen-induced cracking (HIC)** risk rises sharply above ~0.25% C
3. Martensite cracks can be invisible until the part is loaded or exposed to hydrogen (from moisture or process gases)
4. Preheat slows the cooling rate → less martensite → less HIC risk

---

## Effects of alloying elements on steel properties

Each element does something specific.[^1][^4]

| Element | Symbol | Effect on steel |
|---|---|---|
| **Carbon** | C | Increases hardness, tensile strength, hardenability; reduces ductility and weldability |
| **Manganese** | Mn | Increases strength and hardness; deoxidizer; improves hardenability; increases toughness |
| **Silicon** | Si | Deoxidizer; increases strength slightly; too much reduces ductility |
| **Chromium** | Cr | Increases hardness, wear resistance, corrosion resistance; key in stainless and Cr-Mo steels |
| **Molybdenum** | Mo | Increases hardenability and high-temperature strength; critical in Cr-Mo alloy steels |
| **Nickel** | Ni | Increases toughness (especially at low temperatures); improves impact strength; improves hardenability |
| **Vanadium** | V | Grain refiner; increases hardness and wear resistance; used in tool steels and some HSLA |
| **Phosphorus** | P | Increases strength slightly; but raises ductile-to-brittle transition temp; generally an impurity to minimize |
| **Sulfur** | S | Improves machinability (intentionally added in free-machining steels); but reduces toughness and weldability — minimize for weldable steels |
| **Boron** | B | Very small amounts (0.001–0.003%) dramatically increase hardenability; used in some HSLA |
| **Titanium / Niobium (Columbium)** | Ti / Nb | Microalloying elements; grain refiners and carbide/nitride formers in HSLA steels |

---

## Low alloy steels

Low alloy steels contain small amounts (<5% total) of alloying elements to achieve mechanical properties beyond plain carbon steel without sacrificing weldability significantly.[^2][^4]

### Key low alloy families relevant to welders:

**Chromium-Molybdenum (Cr-Mo) steels:**
Used extensively in oilfield piping, pressure vessels, and power generation boilers where elevated temperature service (up to 650°C) is required.

| Grade | Common designation | Cr content | Mo content | Application |
|---|---|---|---|---|
| ASTM A387 Gr.11 / P11 | 1.25Cr-0.5Mo | 1.0–1.5% | 0.44–0.65% | Refinery and petrochemical piping |
| ASTM A387 Gr.22 / P22 | 2.25Cr-1Mo | 2.0–2.5% | 0.87–1.13% | High-temp pressure vessels, boilers |
| ASTM A387 Gr.91 / P91 | 9Cr-1Mo-V | 8.0–9.5% | 0.85–1.05% | Ultra-high-temp power plant piping |

**Weldability of Cr-Mo steels:**
- All require **preheat** — minimum 200°C for P11; higher for P22 and P91[^2]
- **Post-Weld Heat Treatment (PWHT)** is mandatory for most Cr-Mo code applications — the martensite formed during welding must be tempered
- P91 is particularly demanding: requires precise preheat (200–250°C), interpass maximum (300°C), and PWHT (730–780°C)[^2]
- Low-hydrogen electrodes mandatory

**HSLA (High Strength Low Alloy) steels:**
- Common grades: A572 Grade 50, A992, CSA G40.21-350W, -480W, -700Q
- Carbon: typically 0.08–0.22% (similar to mild steel)
- Small additions of Nb, V, Ti refine grain size → higher yield strength
- **Excellent weldability** — CE is typically low despite higher strength
- A572 Grade 50 (350 MPa yield strength) is used for most structural beams, columns, and plates in modern Alberta construction

---

## Carbon equivalent (CE) and preheat determination

The **Carbon Equivalent formula** combines all the hardenability-contributing elements into a single number to predict whether preheat is needed.[^3]

> **CE = C + Mn/6 + (Cr + Mo + V)/5 + (Ni + Cu)/15**

**Using the formula:**
- **CE < 0.35:** Generally no preheat required for mild steel plate in ambient temperature, up to ~25 mm
- **CE 0.35–0.60:** Preheat required — amount depends on thickness and restraint (typically 50–200°C)
- **CE > 0.60:** High preheat (200°C+) required; PWHT likely required after welding

**Example — A36 mild steel:**
Typical CE of A36 (C=0.18%, Mn=0.80%):
CE = 0.18 + 0.80/6 + 0 + 0 = 0.18 + 0.13 = **0.31** → No preheat required for standard thicknesses.[^3]

**Example — 4140 (Cr-Mo alloy steel):**
Typical CE of 4140 (C=0.38%, Mn=0.85%, Cr=0.90%, Mo=0.20%):
CE = 0.38 + 0.85/6 + (0.90 + 0.20)/5 + 0 = 0.38 + 0.14 + 0.22 = **0.74** → High preheat required.[^4]

---

## Alloy steel filler metals: AWS A5.5 classification

AWS A5.5 covers SMAW electrodes for low-alloy steels. The classification system adds **suffix codes** after the standard E-number to identify the alloy type.[^1]

### Understanding the suffix:

**E8018-B2:**
- **E** = electrode
- **80** = minimum tensile strength 80,000 psi (550 MPa)
- **1** = all-position
- **8** = low-hydrogen, iron powder coating, DCEP or AC
- **-B2** = chromium-molybdenum type (1.25Cr-0.5Mo)

### Key low-alloy SMAW electrode classifications:

| Classification | Alloy type | C content | Cr | Mo | Ni | Application |
|---|---|---|---|---|---|---|
| **E7018-A1** | Carbon-molybdenum | Low | — | 0.40–0.65% | — | Mild carbon-Mo steel; some low-alloy plate |
| **E8018-B2** | 1.25Cr-0.5Mo | Low | 1.0–1.5% | 0.40–0.65% | — | P11 piping, A387 Gr.11 pressure vessels |
| **E9018-B3** | 2.25Cr-1Mo | Low | 2.0–2.5% | 0.90–1.20% | — | P22 piping, A387 Gr.22, high-temp service |
| **E8018-C1** | Nickel steel (2.5% Ni) | Low | — | — | 2.0–2.75% | Low-temperature service (-60°C to -73°C) |
| **E8018-C3** | Nickel steel (1% Ni) | Low | — | — | 0.80–1.10% | Low-temperature service (-46°C) |
| **E9018-M** | Military/high-toughness low-alloy | Low | Var | Var | Var | High-strength structural, military, bridges |
| **E11018-M** | Ultra-high-strength low-alloy | Low | Var | Var | Var | High-yield structural: offshore, bridges |

### Matching filler to base metal:

**Rule: match or overmatch tensile strength; match alloy chemistry for high-temperature service.**[^2][^4]

- For carbon steel (A36): E7018 (low alloy, plain mild — also covered by A5.1, but E7018-A1 overlaps)
- For P11 (1.25Cr-0.5Mo): E8018-B2 — must match chromium and molybdenum for elevated-temperature properties
- For P22 (2.25Cr-1Mo): E9018-B3 — must match both Cr and Mo for creep resistance
- For low-temperature impact applications: E8018-C1, E8018-C3, or E9018-M depending on design temperature

**Do NOT use E7018 plain mild steel electrode on Cr-Mo pressure piping** — the weld will not have the Cr-Mo content needed for creep resistance at elevated temperatures, even if short-term strength is acceptable.

---

## Numbers you need to memorize

- **Low carbon steel:** 0.05–0.25% C[^4]
- **Medium carbon steel:** 0.25–0.60% C[^4]
- **High carbon steel:** 0.60–1.4% C[^4]
- **CE formula:** CE = C + Mn/6 + (Cr+Mo+V)/5 + (Ni+Cu)/15[^3]
- **CE < 0.35:** No preheat (typical mild steel conditions)[^3]
- **CE > 0.60:** High preheat required[^3]
- **P11 composition:** 1.0–1.5% Cr + 0.44–0.65% Mo; filler = E8018-B2[^1][^2]
- **P22 composition:** 2.0–2.5% Cr + 0.90–1.20% Mo; filler = E9018-B3[^1][^2]
- **P91 preheat minimum:** 200°C; PWHT: 730–780°C[^2]
- **E7018-A1:** Carbon-Mo (0.40–0.65% Mo)[^1]
- **HSLA A572 Gr.50 yield strength:** 345 MPa (50 ksi)[^4]

---

## What the textbook doesn't tell you

**The "-M" suffix means toughness, not alloy.** E9018-M or E11018-M aren't a specific Cr-Mo alloy — the "M" stands for military/multi-alloy, indicating the electrode meets strict impact toughness requirements at low temperature (-40°C Charpy). It's used for bridges, offshore structures, and earthquake-resistant construction where cold-temperature fracture toughness is design-critical.

**Matching alloy chemistry on Cr-Mo is not optional for code work.** On a pressure vessel or piping system that runs at 450°C, the design relies on the Cr-Mo's creep resistance at that temperature. An E7018 deposit at that service temperature will creep (slowly deform under sustained load) at rates the design never intended. This is why ASME and CSA B51 specify the exact electrode classifications for Cr-Mo service — it's not bureaucracy, it's physics.

**HSLA steels surprise some welders.** A572 Grade 50 (350 MPa yield) and A992 (345–450 MPa) are the most common structural steels in Alberta construction, and they weld much like A36 mild steel despite their higher strength — because the strength comes from grain refinement, not high carbon. This is the HSLA trick: high strength, good weldability.

---

## Key terms

- **Carbon equivalent (CE):** single number combining C and alloying elements to predict preheat need and weldability
- **Hardenability:** tendency of steel to form hard phases (martensite) when cooled from welding temperature
- **Martensite:** hard, brittle microstructure formed by rapid cooling — enemy in the HAZ of high-carbon and alloy steels
- **HIC (Hydrogen-Induced Cracking):** weld cracking driven by hydrogen + residual stress + hard HAZ — prevented by low-hydrogen process and preheat
- **Preheat:** controlled heating of base metal before welding — slows cooling rate, reduces martensite formation, allows hydrogen to escape
- **PWHT (Post-Weld Heat Treatment):** controlled heating of the welded joint after welding — tempers martensite, relieves residual stress; required for Cr-Mo code welds
- **Cr-Mo steel:** chromium-molybdenum alloy steel for high-temperature service; weldable with correct procedure
- **HSLA (High Strength Low Alloy):** steel family using microalloying (Nb, V, Ti) for grain refinement → high strength + good weldability
- **Creep:** slow plastic deformation under sustained load at elevated temperatures — Cr-Mo steels resist it
- **E8018-B2:** SMAW low-alloy electrode for 1.25Cr-0.5Mo steels (P11)
- **E9018-B3:** SMAW low-alloy electrode for 2.25Cr-1Mo steels (P22)

---

## Common exam trap

- **CE formula — memorize the denominators:** C alone, Mn/6, (Cr+Mo+V)/5, (Ni+Cu)/15. Exam variants will use wrong denominators. The correct formula is exact.
- **E8018-B2 is for 1.25Cr-0.5Mo (P11); E9018-B3 is for 2.25Cr-1Mo (P22)** — don't flip them. The "B2" is the clue (lower alloy, lower number).
- **HSLA steels have LOW carbon but HIGH yield strength** — exam distractors say "HSLA steels have high carbon content for strength." Wrong. Their strength comes from microalloying and grain refinement.
- **PWHT is required for most Cr-Mo code welds** — "no PWHT is needed if the preheat is high enough" is false for pressure piping.
- **A572 Grade 50 welds like mild steel** — because its CE is typically low (0.30–0.38 depending on thickness). Exam might imply it needs special procedure because it's "50 ksi" strength. The strength is in the grain, not the carbon.

---

## Practice question preview

**Q:** A pipefitter is welding P22 chrome-molybdenum alloy piping (2.25% Cr, 1% Mo) for a high-temperature service application. Which SMAW electrode classification MUST be used to match the alloy chemistry?

A) E7018 — carbon steel low-hydrogen electrode
B) E8018-B2 — 1.25Cr-0.5Mo low-alloy electrode
C) E9018-B3 — 2.25Cr-1Mo low-alloy electrode
D) E6010 — cellulosic fast-freeze electrode

**Correct: C**

**Explanation:** P22 pipe requires a filler metal that matches both the chromium (2.25%) and molybdenum (1%) content — specifically E9018-B3 per AWS A5.5. This matching is required not just for short-term strength but for long-term creep resistance at elevated service temperatures. (A) E7018 has no Cr or Mo alloying — would be undermatched for elevated-temperature service and fail creep requirements. (B) E8018-B2 is for P11 (1.25Cr-0.5Mo) — too low in Cr and Mo for P22. (D) E6010 is a cellulosic electrode for root passes in mild steel and pipeline — not low-hydrogen, not alloy-matched, not appropriate for P22.

**Red Seal mapping:** D-13.01 (Selects SMAW equipment and consumables); A-5.05 (Selects welding processes and power source)

---

[^1]: [AWS A5.5 — Specification for Low-Alloy Steel Electrodes for SMAW](https://pubs.aws.org/p/1144/a55a5-5m2014-specification-for-low-alloy-steel-electrodes-for-shielded-metal-arc-welding); E7018-A1, E8018-B2, E9018-B3, E8018-C classifications, alloy compositions, mechanical properties
[^2]: [Lincoln Electric — Welding of Alloy Steels, Procedure Handbook](https://www.lincolnelectric.com/en/education-center/welding-education/procedure-handbook); Cr-Mo welding procedures, preheat requirements, PWHT temperatures for P11, P22, P91
[^3]: [CSA W59:18 — Welded Steel Construction](https://www.csagroup.org/store/product/CSA%20W59%3A18/), Table 5 — preheat requirements by carbon equivalent and plate thickness
[^4]: [Modern Welding, 12th ed. (Bowditch, Goodheart-Willcox)](https://www.g-w.com/modern-welding), Chapter 21 — Carbon and Alloy Steels; carbon content categories, alloying element effects, HSLA steels, CE formula application
[^5]: [CWB Group — Welder Certification Study Guide](https://www.cwbgroup.org/education/learning-resources); alloy steel filler classifications, CSA/AWS equivalents, preheat for low-alloy steels
[^6]: [AIT Welder Curriculum Guide 012 (2026), Period 2 Section 1 Topic H](https://tradesecrets.alberta.ca/SOURCES/PDFS/CURRICULUM_GUIDES/012_OUTLINE.PDF), pp. 33–35
