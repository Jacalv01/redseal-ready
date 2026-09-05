---
id: p2-s1-g
period: 2
section: 1
section_title: Foundational Skills, Safety, Procedures and Properties of Metals
topic_letter: G
topic_title: Production of Metals
hours: 3
weight_pct: 1
outcome: >
  Upon successful completion, learners will be able to describe the production processes and types of iron and steel.
objectives:
  - Describe the production processes for iron and steel.
  - Describe the types of iron and steel.
red_seal_mapping:
  - A-5.05 (Selects welding processes and power source)
  - A-4.04 (Organizes materials)
citations:
  - source: Modern Welding (Bowditch, Goodheart-Willcox, 12th ed.)
    ref: Chapter 17 — Iron and Steel Production; blast furnace, BOF, EAF, steelmaking processes, iron and steel types
    url: https://www.g-w.com/modern-welding
  - source: Lincoln Electric — The Procedure Handbook of Arc Welding
    ref: Steel types and their properties, iron classification, effect of carbon and alloying elements
    url: https://www.lincolnelectric.com/en/education-center/welding-education/procedure-handbook
  - source: CWB Group — Welder Certification Study Guide
    ref: Types of iron and steel for welders, metallurgical background
    url: https://www.cwbgroup.org/education/learning-resources
  - source: AIT Welder Curriculum Guide 012 (2026), Period 2 Section 1 Topic G
    ref: pp. 32–33
    url: https://tradesecrets.alberta.ca/SOURCES/PDFS/CURRICULUM_GUIDES/012_OUTLINE.PDF
---

# Production of Metals

Understanding how steel is made isn't just trivia — it tells you *why* steel behaves the way it does. Residual elements from production, grain size from rolling temperature, mill scale from cooling — all of these directly affect how the steel welds, how it responds to heat, and whether your weld will crack. A welder who knows where the metal came from is a welder who can predict problems before they happen.

---

## Iron ore to pig iron: the blast furnace

Steel starts as iron ore — primarily iron oxide (Fe₂O₃) — which must have its oxygen removed (reduced) to produce iron.[^1]

### Blast furnace process:
1. **Charge the furnace** from the top with alternating layers of:
   - **Iron ore** (Fe₂O₃ or Fe₃O₄)
   - **Coke** (purified coal — carbon source and fuel)
   - **Limestone** (CaCO₃ — flux to remove impurities)
2. **Blast pre-heated air** (and sometimes oxygen) upward through the bottom of the furnace — 1000°C+ air
3. **Coke combustion** produces carbon monoxide (CO), which rises and reduces the iron ore:
   > Fe₂O₃ + 3CO → 2Fe + 3CO₂
4. **Liquid iron** (and slag) collect at the bottom:
   - Iron sinks (denser) → drained off as **pig iron**
   - Slag (limestone + impurities) floats → removed separately
5. **Pig iron characteristics:** ~3.5–4.5% carbon, significant Si, Mn, P, S — too brittle and high in carbon for structural use as-is[^1]

### Pig iron = cast iron feedstock + steel feedstock
Pig iron itself is useful in some applications but must be further processed to make steel.

---

## Pig iron to steel: the two main routes

### Route 1: Basic Oxygen Furnace (BOF)

Used for primary steel production from a mix of pig iron + scrap steel.[^1]

**Process:**
1. A water-cooled oxygen lance is lowered into the molten pig iron
2. Pure oxygen (>99.5%) at high pressure oxidizes the carbon: C + O₂ → CO₂ (escapes as gas)
3. The carbon content drops from ~4% to the desired steel range (0.02–1.5% depending on grade)
4. Alloying elements (Mn, Si, etc.) are added
5. Liquid steel is tapped into a ladle

**Time:** A full BOF heat takes about 25–40 minutes[^1]
**Scale:** BOF processes 200–350 tonnes per heat — this is large-scale integrated steelmaking

### Route 2: Electric Arc Furnace (EAF)

Used for mini-mill production primarily from recycled scrap steel.[^1]

**Process:**
1. Scrap steel is loaded into the furnace
2. Graphite electrodes arc into the scrap, melting it — temperatures reach 1600°C+
3. The melt is refined (oxygen blown, additives made) to reach the desired chemistry
4. Steel is tapped into a ladle

**Advantages:**
- Can be run anywhere there's electrical power — no blast furnace or coke plant needed
- Faster startup/shutdown than BOF — more flexible production scheduling
- Uses recycled steel scrap — good for Alberta's abundant scrap supply
- Easier to produce specialty alloy steels in small heats

**Residual elements:** EAF steel can have higher residual tramp elements (Cu, Sn, Ni from scrap contamination) that affect some properties — worth knowing when welding high-quality EAF steel on critical applications.[^1]

---

## From liquid steel to solid shapes: casting and rolling

After steelmaking, liquid steel is shaped:[^1]

### Continuous casting (most common today)
Liquid steel pours into a water-cooled mold, solidifies as it's pulled through, and is cut into **slabs**, **blooms**, or **billets** — the starting shapes for subsequent rolling.

### Rolling (hot rolling vs cold rolling)
**Hot rolling:** Slabs/blooms/billets are reheated to ~1200°C and passed through rolls to produce structural shapes (I-beams, angles, plate, coil). The surface has a black **mill scale** (iron oxide) from cooling in air.

**Cold rolling:** Hot-rolled coil is rolled further at room temperature to produce thinner, tighter-tolerance sheet with a smoother, brighter surface. Cold rolling also **work-hardens** the steel slightly.

**Mill scale on hot-rolled plate is important for welders:**
- Mill scale is Fe₃O₄ — an oxide
- Mill scale does NOT cut cleanly with oxyfuel (although the cut starts through the steel itself)
- Mill scale traps moisture → porosity risk if not removed before GMAW
- SMAW and FCAW are more tolerant of mill scale than GMAW (the flux acts as a flux/slag to handle surface oxides)
- For GMAW and critical GTAW, **grind or blast the mill scale away** in the weld zone before welding[^2]

---

## Types of iron: from blast furnace to cast iron shop

### Pig iron
- ~3.5–4.5% C
- Brittle; not used structurally as-is
- Feedstock for BOF steelmaking or cast iron foundry work

### Grey cast iron
- 2.5–4.0% C (present as graphite flakes in the microstructure)
- Characteristic grey fracture face — graphite gives the grey colour
- **Excellent vibration damping** (used in machine bases, engine blocks)
- **Brittle** — does not deform plastically before fracture
- **Very hard to weld** — high carbon causes hard, brittle martensite in HAZ; graphite interferes with fusion[^2]
- Typical tensile strength: 100–350 MPa (much lower than structural steel)

### White cast iron
- ~2.0–3.5% C (present as iron carbide Fe₃C — cementite)
- White/silvery fracture face
- Extremely hard (HRC 65+) and extremely brittle
- Not weldable — used as-cast for wear surfaces

### Ductile (Nodular) cast iron
- Similar carbon to grey iron, but magnesium is added during casting → graphite forms as **spheroids** (nodules) instead of flakes
- Much better ductility and toughness than grey iron (elongation 10–20% vs <1% for grey)
- Weldable with proper procedure (lower preheat than grey iron, but still needs preheat)

### Malleable cast iron
- White cast iron that is heat-treated to convert cementite to rounded graphite nodules (temper carbon)
- Better ductility than grey iron; used for pipe fittings, agricultural equipment
- Can be welded with care

### Wrought iron
- Very low carbon (< 0.08%), slag inclusions in a fibrous pattern
- Historically used for gates, railings (before mild steel was cheap)
- Very weldable; rarely encountered in modern fabrication (look for older structures)

---

## Types of steel: summary for welders

| Type | Carbon content | Key properties | Weldability |
|---|---|---|---|
| **Low carbon (mild) steel** | 0.05–0.25% | Soft, ductile, easily formed | Excellent — no preheat for typical thicknesses |
| **Medium carbon steel** | 0.25–0.60% | Higher strength, less ductile | Good — preheat required for thick sections |
| **High carbon steel** | 0.60–1.4% | Very high strength, very hard | Poor — high preheat, low-hydrogen process, slow cooling |
| **Low alloy steel** | 0.05–0.25% C + alloying | High strength + toughness (HSLA) | Good — may require preheat depending on CE |
| **High alloy steel** | Varied C + major alloy content | Stainless, tool steel, heat-resistant | Varies widely by alloy type |

---

## Numbers you need to memorize

- **Pig iron carbon content:** ~3.5–4.5%[^1]
- **Grey cast iron carbon content:** 2.5–4.0%[^1]
- **BOF heat time:** ~25–40 minutes for 200–350 tonne heat[^1]
- **Hot rolling temperature:** ~1200°C starting temperature[^1]
- **Low carbon steel:** 0.05–0.25% C — excellent weldability[^1][^2]
- **Medium carbon steel:** 0.25–0.60% C — preheat required[^2]
- **High carbon steel:** 0.60–1.4% C — poor weldability[^2]
- **Grey cast iron tensile strength (typical):** 100–350 MPa — much weaker than structural steel in tension[^1]

---

## What the textbook doesn't tell you

**EAF mini-mill steel is now the majority of North American structural steel supply.** The old integrated mills (blast furnace + BOF) are fewer and farther away. When you receive a piece of W-shape or HSS from a local service centre, it almost certainly came from a mini-mill EAF. This generally makes no difference for standard structural welding, but is worth knowing when specifying materials for critical applications.

**Mill scale is your enemy on GMAW.** You can run a beautiful root pass with GMAW on cleaned steel, then hit a section with mill scale and watch porosity appear. SMAW and FCAW both have flux that handles minor scale. GMAW solid wire has no flux — it depends entirely on the deoxidizers in the wire (ER70S-6 has more Mn/Si than ER70S-3 for this reason), but neither grade tolerates heavy mill scale. Grind the weld zone.

**Grey cast iron is tricky to weld in the field precisely because of its carbon content.** The welding heat drives carbon out of the grey iron matrix into the HAZ. This carbon, combined with rapid cooling, creates martensite — a hard, brittle phase that cracks easily. Slow, controlled preheat (500–600°C), slow cooling (wrapped in insulation), or cold welding with nickel-iron electrodes (ENiFe-CI) and peening between passes are the main strategies. Period 3 covers this in detail.

---

## Key terms

- **Pig iron:** raw iron from the blast furnace; ~3.5–4.5% C; feedstock for steelmaking
- **Blast furnace:** smelting furnace that reduces iron ore to pig iron using coke and limestone
- **BOF (Basic Oxygen Furnace):** steelmaking process using pure oxygen jet to reduce carbon from pig iron
- **EAF (Electric Arc Furnace):** steelmaking process using electric arc to melt scrap steel; mini-mill production
- **Continuous casting:** solidifying liquid steel directly into slabs, blooms, or billets without ingot casting
- **Hot rolling:** deforming steel above its recrystallization temperature to produce structural shapes; leaves mill scale
- **Cold rolling:** deforming steel at room temperature; produces thinner, smoother, tighter-tolerance sheet; work-hardens
- **Mill scale:** iron oxide (Fe₃O₄) surface layer from hot rolling; must be removed for GMAW
- **Grey cast iron:** 2.5–4.0% C; graphite as flakes; brittle; vibration-damping; hard to weld
- **White cast iron:** carbon as iron carbide; very hard and brittle; not weldable
- **Ductile (nodular) cast iron:** graphite as spheroids (Mg addition); better ductility; weldable with care
- **Wrought iron:** very low C (<0.08%); fibrous slag inclusions; excellent weldability; historical material
- **Martensite:** very hard, brittle steel microstructure formed by rapid cooling from high temperature; the enemy in cast iron HAZ

---

## Common exam trap

- **Pig iron is NOT the same as cast iron** — pig iron is the raw product from the blast furnace; cast iron is a broad family of iron alloys with various microstructures (grey, white, ductile, malleable). All cast irons start from pig iron, but pig iron is not cast iron.
- **Grey cast iron is identified by its GREY FRACTURE FACE** — the grey comes from graphite flakes. White cast iron has a white/silvery fracture face.
- **BOF uses pure oxygen, not air** — exam distractors often say "air is blown in to reduce carbon." It's oxygen, not air. (Air is used in the *blast furnace*, not the BOF.)
- **EAF melts scrap, BOF melts pig iron** — the inputs are different. EAF can add alloys; BOF starts with liquid pig iron.
- **Mill scale should be removed before GMAW** — the exam may ask about causes of porosity in GMAW on plate stock. Mill scale is a valid answer.

---

## Practice question preview

**Q:** A welder is tasked with repairing a cracked machine base made of grey cast iron. What is the PRIMARY reason grey cast iron is difficult to weld?

A) Its low carbon content produces a very hard weld metal
B) Its high carbon content (2.5–4.0%) causes hard, brittle martensite to form in the HAZ during rapid cooling
C) It requires a pure argon shielding gas that is not compatible with SMAW electrodes
D) It melts at a higher temperature than structural steel, requiring higher amperage

**Correct: B**

**Explanation:** Grey cast iron's high carbon content (2.5–4.0%) means the HAZ receives a large carbon supply during welding. When the HAZ cools rapidly (as it would without preheat or controlled cooling), this carbon transforms with the iron to form martensite — an extremely hard, brittle phase that cracks readily under the residual stress of welding. This is why grey cast iron welding requires preheat (typically 150–300°C minimum, often higher), low-hydrogen or nickel-iron electrodes, peening between passes, and slow controlled cooling. (A) Grey iron has HIGH carbon, not low. (C) SMAW electrodes do not require shielding gas. (D) Grey iron melts at LOWER temperature than structural steel due to high carbon.

**Red Seal mapping:** A-5.05 (Selects welding processes and power source); A-5.03 (Controls temperature of weldments)

---

[^1]: [Modern Welding, 12th ed. (Bowditch, Goodheart-Willcox)](https://www.g-w.com/modern-welding), Chapter 17 — Iron and Steel Production; blast furnace chemistry, BOF and EAF processes, hot rolling, cast iron types
[^2]: [Lincoln Electric — The Procedure Handbook of Arc Welding](https://www.lincolnelectric.com/en/education-center/welding-education/procedure-handbook); steel types, carbon content ranges, weldability classification, mill scale effects on GMAW
[^3]: [CWB Group — Welder Certification Study Guide](https://www.cwbgroup.org/education/learning-resources); types of iron and steel, metallurgical background for welders
[^4]: [AIT Welder Curriculum Guide 012 (2026), Period 2 Section 1 Topic G](https://tradesecrets.alberta.ca/SOURCES/PDFS/CURRICULUM_GUIDES/012_OUTLINE.PDF), pp. 32–33
