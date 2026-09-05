---
id: p3-s2-c
period: 3
section: 2
section_title: Properties of Metals
topic_letter: C
topic_title: Nickel Alloys and Clad Steels
hours: 4
weight_pct: 1
outcome: >
  Upon successful completion, learners will be able to describe nickel alloys and clad
  steels, select appropriate filler metals, and describe preparation and welding procedures.
objectives:
  - Describe nickel and its alloys.
  - Describe clad steels and their advantages.
  - Select filler metals per AWS specifications.
  - Describe preparation and welding procedures for clad steels.
red_seal_mapping:
  - D-13.01 (Selects SMAW equipment and consumables)
  - D-15.01 (Selects GTAW gas, equipment and consumables)
  - A-4.01 (Uses documentation and reference material)
  - B-8.01 (Prepares materials)
citations:
  - source: AWS A5.11 — Nickel and Nickel-Alloy Welding Electrodes for SMAW
    ref: ENi, ENiCrFe, ENiMo electrode classifications, chemistry requirements
    url: https://pubs.aws.org/p/1136/a511-a511m2010-specification-for-nickel-and-nickel-alloy-welding-electrodes-for-shielded-metal-arc-welding
  - source: AWS A5.14 — Nickel and Nickel-Alloy Bare Welding Electrodes and Rods
    ref: ERNi, ERNiCrMo filler rod classifications, shielding gas selection
    url: https://pubs.aws.org/p/1152/a514-a514m-2018-specification-for-nickel-and-nickel-alloy-bare-welding-electrodes-and-rods
  - source: Lincoln Electric — Welding Nickel Alloys Guide
    ref: Inconel, Monel, Hastelloy welding procedures, filler metal matching, heat input control
    url: https://www.lincolnelectric.com/en/education-center/welding-education
  - source: TWI Global — Welding Nickel and Nickel Alloys (Job Knowledge)
    ref: Nickel alloy families, clad steel welding procedure, interpass temperature, joint prep
    url: https://www.twi-global.com/technical-knowledge/job-knowledge/welding-nickel-alloys-part-1-090
  - source: ESAB — Welding of Clad and Lined Vessels
    ref: Clad steel construction, sequence of welding, filler metal selection for backing and cladding welds
    url: https://www.esab.com/us/nam_en/education/blog/welding-clad-steel/
---

# Nickel Alloys and Clad Steels

Nickel alloys are the exotic end of the trade — Inconel, Monel, Hastelloy. They show up in chemical plants, refineries, power generation, and offshore platforms where stainless steel isn't corrosion-resistant enough. Clad steels are a cost-effective alternative: a carbon steel structural shell with a stainless or nickel alloy bonded to the wetted surface. Understanding these materials separates welders who work in process industries from welders who work in structural fab only.

---

## Nickel and Its Properties

Pure nickel (Ni) is a silvery, ductile, magnetic metal with excellent corrosion resistance and high-temperature stability.[^3][^4]

| Property | Pure Nickel | Note |
|---|---|---|
| Melting point | 1455 °C (2651 °F) | Higher than carbon steel (1538 °C is iron, but steel melts ~1370–1530 °C) |
| Crystal structure | FCC (face-centered cubic) | Like austenite — no phase transformation on cooling |
| Magnetic | Yes (but many Ni alloys are not magnetic) | Depends on alloy composition |
| Corrosion resistance | Excellent in reducing environments | Complements Cr (oxidizing) resistance |
| Thermal conductivity | Lower than carbon steel | Weld puddles are more sluggish — different feel than steel |
| Thermal expansion | Higher than carbon steel | More distortion potential per degree of heat input |

**Key insight:** Because nickel has FCC structure (like austenite), nickel alloys do NOT form martensite on quenching — there is NO hardening transformation. This eliminates hydrogen-induced cracking (HIC) risk, but other cracking mechanisms (hot cracking, sulfur contamination) are relevant.[^4]

---

## Nickel Alloy Families

### Commercially Pure Nickel — Alloy 200 / 201

- **Composition:** >99% Ni
- **Applications:** food processing, caustic (NaOH) service, specialized electronics
- **SMAW filler:** ENi-1 (AWS A5.11)[^1]
- **GTAW filler:** ERNi-1 (AWS A5.14)[^2]
- **Alloy 201:** low-carbon version (0.02% C max) for elevated temperature caustic service

### Monel — Nickel-Copper Alloys (Alloy 400, K-500)

- **Composition:** 63–70% Ni, balance Cu
- **Applications:** seawater service, hydrofluoric acid, marine hardware, pump components
- **Resistance to hydrofluoric acid (HF):** one of very few materials that resists HF — a critical industrial need
- **SMAW filler:** ENiCu-7 (AWS A5.11)[^1]
- **GTAW filler:** ERNiCu-7 (AWS A5.14)[^2]
- **Welding note:** highly susceptible to sulfur-induced hot cracking. Any sulfur contamination on the surface (oils, lubricants, marking materials) can cause cracking in the weld. Clean aggressively with acetone before welding.

### Inconel — Nickel-Chromium Alloys (Alloy 600, 625, 718)

- **Composition varies:** typically 58–76% Ni, 14–23% Cr, with Fe, Mo, Nb additions
- **Applications:** furnaces, jet engines, heat exchangers, chemical reactors at elevated temperatures (up to 1100 °C service)
- **Key advantage:** maintains strength and oxidation resistance at temperatures where stainless steel fails
- **Alloy 625:** ERNiCrMo-3 filler — used for both base metal 625 and as a versatile overlay filler on carbon steel
- **Alloy 718:** precipitation-hardenable (can be age-hardened) — used in aerospace and oil & gas pressure vessels
- **SMAW filler:** ENiCrFe-2 or ENiCrFe-3 (AWS A5.11)[^1]
- **GTAW filler:** ERNiCrMo-3 (for Alloy 625), ERNiCrMo-6 (for Alloy C276) (AWS A5.14)[^2]

### Hastelloy — Nickel-Molybdenum-Chromium Alloys (Alloy C-276, B-3)

- **Composition:** typically 50–65% Ni, 15–28% Mo, 14–22% Cr (C-276 specific)
- **Applications:** most aggressive chemical environments — sulfuric acid, hydrochloric acid, chlorinated solvents, oxidizing and reducing acids simultaneously
- **Alloy C-276 (Hastelloy C-276):** considered the most universal corrosion-resistant alloy in common industrial use
- **GTAW filler:** ERNiCrMo-4 (for C-276) (AWS A5.14)[^2]
- **SMAW filler:** ENiCrMo-4 (AWS A5.11)[^1]

---

## AWS Filler Metal Classification — Nickel Alloys

### AWS A5.11 SMAW electrode classification format[^1]

**E - Ni - [chemistry symbol(s)] - [sequential number]**

| Part | Meaning |
|---|---|
| E | Electrode (SMAW) |
| Ni | Nickel base |
| Cr, Cu, Mo, Fe | Major alloying elements in the deposit |
| -1, -2, -3, -7 | Sequential number differentiating similar compositions |

Examples:
- **ENi-1:** pure nickel — for Alloy 200/201
- **ENiCu-7:** Ni-Cu — for Monel 400
- **ENiCrFe-3:** Ni-Cr-Fe — for Inconel 600/182
- **ENiCrMo-3:** Ni-Cr-Mo — for Inconel 625

### AWS A5.14 GTAW filler rod classification format[^2]

**ER - Ni - [chemistry symbol(s)] - [sequential number]**

Same logic as A5.11, but ER prefix for rods used in GTAW or GMAW.

---

## General Welding Principles for Nickel Alloys

Nickel alloys behave very differently from steel during welding:[^3][^4]

| Characteristic | Effect on welding |
|---|---|
| **Sluggish, viscous weld pool** | Puddle does not flow freely — doesn't "wet" into corners easily |
| **Low thermal conductivity** | Heat stays concentrated in weld zone — interpass temperature climbs quickly |
| **High hot-cracking susceptibility** | Sulfur, phosphorus, lead, zinc, and bismuth all cause hot cracking (liquation cracking) |
| **No martensite** | No hydrogen-induced cold cracking risk — but hot cracking replaces it |
| **Porosity from nitrogen** | Avoid nitrogen-contaminated argon; use 99.99% pure argon shielding |

### Critical rules for nickel alloy welding

1. **Cleanliness is everything:** remove all oil, grease, sulfur-containing compounds (cutting fluid, marking ink, oil-based lubricants) with acetone or MEK. Any sulfur contamination → hot cracking.[^3]
2. **Control heat input:** stringer beads only — NO weaving. Wide weave beads = more time in the solidification temperature range = more hot cracking risk.[^4]
3. **Maximum interpass temperature: 93 °C (200 °F)** for most nickel alloys — much lower than steel.[^3]
4. **Do not use carbon steel wire brushes:** contamination from iron particles. Dedicated stainless steel or nickel alloy wire brushes only.
5. **Shielding gas:** pure argon (99.99%) for GTAW. Never use CO₂ or air-contaminated gas.[^2]
6. **Use convex (slightly crowned) weld beads** — flat or concave beads in nickel alloys are prone to centerline hot cracking.

---

## Clad Steels

### What is clad steel?

Clad steel (also called bimetal or composite plate) is a structural carbon steel plate with a thin layer of corrosion-resistant alloy bonded to one or both faces.[^5]

**Construction method:**
- **Roll bonding:** the two metals are rolled together at elevated temperature and pressure — metallurgical bond
- **Explosion bonding:** explosive detonation creates a mechanical/metallurgical interlocked bond — used for very dissimilar metals
- **Weld overlay (cladding):** a corrosion-resistant weld deposit is applied to the base plate by SAW or strip cladding

### Why clad steel?

A 50 mm carbon steel vessel shell with 3 mm 316L stainless cladding is MUCH cheaper than a 53 mm solid 316L vessel while providing the same corrosion resistance on the process side. Carbon steel carries the structural load; stainless protects the wetted surface.[^5]

**Common clad combinations:**

| Backing (structural) | Cladding (corrosion-resistant) |
|---|---|
| Carbon steel (A516 Gr. 70) | 304L, 316L, 321, 347 stainless |
| Carbon steel | Alloy 825 (Incoloy) |
| Carbon steel | Alloy 625 (Inconel 625) |
| Carbon steel | Titanium (Ti Gr. 2) |

---

## Welding Clad Steel — The Critical Sequence

The welding sequence for clad steel is CRITICAL because the wrong sequence causes dilution problems:[^5]

### Scenario: butt joint in clad plate (carbon steel back, stainless clad face)

The joint preparation is typically a full-penetration groove from the carbon steel side, leaving the cladding intact on the opposite face.

**Correct sequence:**

**Step 1 — Weld the backing side (carbon steel side) with carbon steel filler**
- Use AWS A5.1 E7018 or equivalent carbon steel electrode for SMAW
- Fill 80–90% of the joint from the carbon steel side
- This is standard structural welding — no complications

**Step 2 — Remove the cladding at the joint area (from the cladding side)**
- Use a carbide burr, grind, or carefully use air carbon arc gouging
- Remove enough cladding material to expose clean metal for the transition weld
- Clean thoroughly — remove any carbon from CAC-A gouging

**Step 3 — Weld a "butter" layer (transition layer) at the carbon steel / cladding interface**
- **Use E309L or ER309L** (not E308L) — the 309 grade bridges the composition gap between carbon steel and 308-type stainless
- Deposit a full transition layer over the carbon steel surface
- This layer "dilutes" into carbon steel on one side but presents a stainless composition on the other side

**Step 4 — Weld the cladding layer**
- **Use E308L or ER308L** (matching the 304L cladding composition)
- Weld over the butter layer, completing the cladding side of the joint

**Why this sequence?** If you weld the cladding layer directly onto carbon steel with E308L, the dilution of carbon steel into the 308L weld metal drives the composition out of specification — particularly chromium and nickel are diluted, and the deposit may not achieve the required corrosion resistance. The 309L butter layer provides a compatible intermediate composition.[^5]

---

## Numbers you need to memorize

- **Maximum interpass temperature for nickel alloys:** 93 °C (200 °F)[^3]
- **Shielding gas for GTAW nickel alloys:** 99.99% pure argon[^2]
- **Monel base alloy:** ~66% Ni, balance Cu — filler ENiCu-7 / ERNiCu-7[^1][^2]
- **Inconel 625 filler (GTAW):** ERNiCrMo-3[^2]
- **Hastelloy C-276 filler (GTAW):** ERNiCrMo-4[^2]
- **Transition layer electrode for clad steel:** E309L or ER309L[^5]
- **Minimum clad thickness (typical):** 3 mm (1/8")[^5]
- **Hot cracking contaminant:** sulfur, phosphorus, lead, zinc, bismuth[^3]

---

## What the textbook doesn't tell you

**The viscous puddle of nickel alloys will surprise you.** Steel welders expect the puddle to flow and wet into corners. Nickel alloy puddles are thick and slow. You'll feel like you're not getting fusion — but you are. Reduce travel speed and use a slight side-to-side motion to ensure toe fusion without weaving.[^4]

**Sulfur is the enemy.** A few ppm of sulfur from a cutting fluid, marker, or even a smudge of grease can cause hot cracking in the centerline of a Monel weld. In a professional nickel alloy shop, welders clean with acetone, wear clean gloves when handling material, and verify there's no sulfur-containing cutting oil anywhere near the joint. This is not overcautious — it's the job.[^3]

**The butter layer technique extends beyond clad steel.** Any time you're welding dissimilar metals — carbon steel to stainless, stainless to nickel alloy — the butter layer provides compositional bridging. This is a fundamental repair and fabrication technique in chemical and power industries.[^5]

**Nickel alloys can be plasma-cut — with the right gases.** Standard oxyfuel cutting doesn't work (no oxidation reaction). Plasma with argon-H₂ or pure argon is used for nickel alloy cutting. Grinding is the most common shop method for small sections.[^4]

---

## Diagram

*(SVG to be added: `assets/diagrams/p3-s2-c-clad-steel-weld-sequence.svg` — four-step sequence cross-sections showing: Step 1 (carbon steel SMAW fill from backing side), Step 2 (gouging/grinding to remove cladding at joint), Step 3 (E309L butter layer), Step 4 (E308L cladding weld) — each step with filler metal and process labeled)*

---

## Key terms

- **Nickel alloy:** a metal with nickel as the primary element, often alloyed with Cr, Cu, Mo, Fe for specific properties
- **Monel:** Ni-Cu alloy resistant to seawater and HF acid — filler ENiCu-7
- **Inconel:** Ni-Cr-Fe/Mo alloy for high-temperature and corrosive service — filler ERNiCrMo-3 (for 625)
- **Hastelloy:** Ni-Mo-Cr alloy for the most severe chemical environments — filler ERNiCrMo-4 (for C-276)
- **Clad steel:** carbon steel structural plate bonded to a corrosion-resistant alloy layer (stainless, nickel, titanium)
- **Butter layer:** a transition weld deposit applied to bridge the composition between dissimilar metals before joining
- **Hot cracking (solidification cracking):** cracking in the weld during solidification — caused by sulfur, phosphorus or other low-melting contaminants in nickel alloys
- **Dilution:** the mixing of base metal into the weld deposit — too much dilution in clad welds destroys the corrosion-resistant composition
- **Explosion bonding:** a method of manufacturing clad plate using explosive energy to create a metallurgical bond between layers

---

## Common exam trap

- **E309L is for the butter layer (transition weld) in clad steel** — NOT E308L for the transition. E308L goes OVER the butter layer for the final cladding weld.
- **Interpass temperature for nickel alloys is 93 °C (200 °F)** — far lower than the 260 °C for mild steel. The exam will test whether students know this distinction.
- **Nickel alloys do NOT form martensite** — so cold cracking/HIC is not a concern. Hot cracking (sulfur/phosphorus) is the main weld defect risk.
- **Hastelloy C-276 filler is ERNiCrMo-4** — not ERNiCrMo-3 (which is for Inconel 625). The numbers differ.
- **Clad steel weld sequence:** backing side first with carbon steel filler, THEN transition layer (E309L), THEN cladding layer (E308L). The sequence cannot be reversed.

---

## Practice question preview

**Q:** A welder is making a butt weld in 304L stainless clad A516 Grade 70 carbon steel plate (12 mm CS backing + 3 mm 304L cladding). After completing the carbon steel backing weld with E7018, which filler metal should be used for the transition (butter) layer on the cladding side?

A) E308L-16 — matching the 304L cladding composition  
B) E7018 — continuing with carbon steel filler for the transition zone  
C) E309L-16 — dissimilar joint transition electrode  
D) ENiCrFe-3 — Inconel electrode for high-alloy transitions

**Correct: C**

**Explanation:** The butter (transition) layer bridges between the carbon steel backing and the 304L stainless cladding. E309L-16 is specifically designed for dissimilar metal joints involving austenitic stainless and carbon or low-alloy steels. It provides sufficient chromium and nickel content to "bridge" the composition even with significant dilution from the carbon steel side. Using E308L directly (Option A) would result in unacceptable dilution reducing Cr and Ni below specification when mixed with carbon steel. E7018 (B) cannot provide corrosion resistance. ENiCrFe-3 (D) is a nickel alloy electrode used for different dissimilar combinations, not this specific clad application.

**Red Seal mapping:** D-13.01 (Selects SMAW equipment and consumables)

---

[^1]: [AWS A5.11 — Nickel and Nickel-Alloy Welding Electrodes for SMAW](https://pubs.aws.org/p/1136/a511-a511m2010-specification-for-nickel-and-nickel-alloy-welding-electrodes-for-shielded-metal-arc-welding); ENi-1, ENiCu-7, ENiCrFe-3, ENiCrMo-3, ENiCrMo-4 classifications and chemistry requirements
[^2]: [AWS A5.14 — Nickel and Nickel-Alloy Bare Welding Electrodes and Rods](https://pubs.aws.org/p/1152/a514-a514m-2018-specification-for-nickel-and-nickel-alloy-bare-welding-electrodes-and-rods); ERNi-1, ERNiCu-7, ERNiCrMo-3, ERNiCrMo-4 filler rod classifications; argon shielding requirement
[^3]: [Lincoln Electric — Welding Nickel Alloys Guide](https://www.lincolnelectric.com/en/education-center/welding-education); interpass temperature (93°C max), sulfur contamination hot cracking, stringer bead requirement, cleanliness protocols
[^4]: [TWI Global — Welding Nickel and Nickel Alloys (Job Knowledge)](https://www.twi-global.com/technical-knowledge/job-knowledge/welding-nickel-alloys-part-1-090); nickel alloy families, viscous puddle characteristics, no martensite formation, convex bead shape
[^5]: [ESAB — Welding of Clad and Lined Vessels](https://www.esab.com/us/nam_en/education/blog/welding-clad-steel/); clad steel construction, weld sequence (backing then butter E309L then cladding E308L), dilution effects, explosion bonding vs. roll bonding
