---
id: p1-s1-j
period: 1
section: 1
section_title: Foundational Skills, Safety and Procedures
topic_letter: J
topic_title: Arc Cutting and Gouging
hours: 6
weight_pct: 3
outcome: >
  Upon successful completion, learners will be able to apply safe work practices during
  cutting operations to identify hazards, select and use PPE, apply controls for welding
  fumes and gases, use electrical safety precautions, and follow procedures for work in
  confined spaces or potentially dangerous enclosures.
objectives:
  - Describe the plasma arc cutting process and equipment.
  - Demonstrate plasma arc cutting.
  - Describe the carbon arc cutting process and equipment.
  - Demonstrate carbon arc cutting.
red_seal_mapping:
  - C-11.01 (Sets up plasma arc cutting equipment)
  - C-11.02 (Performs plasma arc cutting)
  - C-12.01 (Sets up air carbon arc cutting equipment)
  - C-12.02 (Performs air carbon arc cutting)
citations:
  - source: CSA W117.2 — Safety in Welding, Cutting, and Allied Processes (2019)
    ref: Clause 6 (electrical safety — PAC and CAC-A), Clause 10 (confined space cutting operations)
    url: https://www.csagroup.org/store/product/CSA%20W117.2%3A19/
  - source: Hypertherm — Plasma Arc Cutting Handbook (public)
    ref: System overview, consumable life, cut quality parameters, safety
    url: https://www.hypertherm.com/en-US/learn/education/resources/
  - source: Lincoln Electric — Air Carbon Arc Cutting and Gouging Guide (public)
    ref: Process description, DC electrode positive, amperage selection, carbon electrode types
    url: https://www.lincolnelectric.com/en/education-center/welding-education/air-carbon-arc-cutting
  - source: Modern Welding (Bowditch, Goodheart-Willcox, latest edition)
    ref: Chapter 16 (Plasma Arc Cutting) and Chapter 17 (Air Carbon Arc Cutting and Gouging)
    url: https://www.goodheartwillcox.com/products/modern-welding
  - source: Red Seal Occupational Standard — Welder (2024), Block C, Tasks C-11 and C-12
    ref: C-11.01–C-11.02 (PAC), C-12.01–C-12.02 (CAC-A) performance criteria
    url: https://red-seal.ca/_conf/assets/custom/docms/welder/rsos-eng.pdf
  - source: Alberta OHS Code 2023, Part 18 (PPE) and Part 4 (Chemical Hazards)
    ref: Shade selection (OHS Code s.230 + CSA Z94.3); fume controls for arc cutting processes
    url: https://open.alberta.ca/publications/occupational-health-and-safety-code
  - source: AIT Welder Curriculum Guide 012 (2026), Period 1 Section 1 Topic J
    ref: pp. 45–48
    url: https://tradesecrets.alberta.ca/SOURCES/PDFS/CURRICULUM_GUIDES/012_OUTLINE.PDF
---

# Arc Cutting and Gouging

Plasma arc cutting (PAC) and air carbon arc cutting and gouging (CAC-A) are the two arc-based cutting processes you'll use constantly in the trade. PAC cuts faster and cleaner than oxyfuel on thin material. CAC-A removes weld metal, back-gouges roots, and gouges defects for repair — no other process does that job as efficiently.

---

## Plasma arc cutting (PAC)

### How PAC works

Plasma arc cutting uses a high-velocity, high-temperature jet of ionized gas (plasma) to cut any electrically conductive material. The process has no practical limitation based on metallurgy — it cuts mild steel, stainless steel, aluminum, copper, cast iron, and high-strength steel with equal ease. This is the fundamental advantage over oxyfuel, which is limited to metals that oxidize at lower temperature than their base (effectively, only mild steel).[^4]

**The physics:**

1. A pilot arc is struck between the electrode (inside the torch) and the nozzle — this ionizes the gas in the nozzle bore.
2. The transferred arc moves from the electrode to the workpiece (work return).
3. The plasma gas (air, nitrogen, oxygen, argon-hydrogen) is forced through the constricting nozzle orifice — the constriction raises the gas temperature to **8 000–25 000°C** and velocity to near-supersonic.[^2]
4. The plasma jet melts the metal and the high-velocity gas mechanically ejects molten material from the kerf.

**The result:** a fast, clean cut on any conductive metal, with a very narrow kerf (2–4 mm), minimal heat-affected zone (HAZ) compared to oxyfuel, and dross that is generally easy to remove.

### PAC equipment components

## Diagram
*(SVG to be added: `assets/diagrams/p1-s1-j-pac-torch-components.svg` — cross-section of a plasma torch head showing: electrode (hafnium or copper tip), nozzle (copper), swirl ring/gas distributor, shield cup, gas inlet, work return cable connection, and the plasma jet exiting the nozzle, with labels for each part and arrows showing gas flow direction)*

| Component | Function |
|---|---|
| **Power supply** | DC constant-current, typically 20–120 A for portable units; up to 400+ A for production. Output is DC (direct current) |
| **Torch body** | Houses the electrode and nozzle; connects to power supply and gas supply |
| **Electrode** | Hafnium or zirconium tip (for air/O₂ plasma) or pure tungsten (for inert gas plasma). Carries the negative (DCEN) current |
| **Nozzle (cutting tip)** | Constricts the plasma gas to a high-velocity jet; determines kerf width. The nozzle is a consumable |
| **Shield cup** | Protects the nozzle; in some designs routes secondary shielding gas |
| **Plasma gas supply** | Air (from a compressor) for most portable units; nitrogen, oxygen, or argon-hydrogen for specific applications |
| **Work return cable (ground)** | Returns current from the workpiece back to the power supply — must be clamped directly to the workpiece |

### PAC gases and their applications

| Gas | Use | Notes |
|---|---|---|
| **Air (compressed)** | Mild steel, stainless, aluminum | Most common — lowest cost; compressor required (clean, dry air); slightly reduced cut quality on stainless vs nitrogen |
| **Nitrogen** | Stainless steel, aluminum | Better cut quality on stainless than air — no oxidation of cut face |
| **Oxygen** | Mild steel only | Highest cut speed on mild steel; not suitable for stainless or aluminum (oxidizes aggressively) |
| **Argon-hydrogen** | Aluminum, stainless (thick) | Best cut quality; higher operating cost |

For Period 1, most classroom PAC work will be done with air plasma.[^2]

### PAC settings and cut quality

**Key variables:**[^2] [^4]

- **Amperage (current):** primary control for cutting capacity. Higher current = more heat = thicker material cut capability. Set per the machine's chart for the material and thickness.
- **Travel speed:** too fast → incomplete cut (pierces but doesn't fully sever — the "lag" angle on the drag line increases). Too slow → excessive kerf width, excessive dross, potential for double-arc (nozzle damage).
- **Torch standoff distance:** typically **3–6 mm** between the torch shield and the plate surface. Too close → nozzle contact, arc instability, nozzle damage. Too far → diffused plasma jet, rough cut.
- **Plasma gas pressure/flow:** must be within the machine's recommended range. Low gas pressure → turbulent, poor-quality plasma jet. High pressure → reduced arc temperature (too much cooling).

**Diagnosing cut quality:**[^2]

| Observation | Diagnosis | Fix |
|---|---|---|
| Top edge rounded/melted | Amperage too high | Reduce current |
| Cut stops mid-plate | Speed too fast OR amperage too low | Reduce speed, increase amps |
| Excessive dross on bottom | Speed too slow OR amperage too low | Increase speed OR increase amps |
| Bevel on cut face (not square) | Torch not perpendicular | Check torch angle |
| Rough, pitted cut face | Nozzle worn/damaged | Replace nozzle |
| Double arc damage on nozzle | Standoff too close; moisture in air | Increase standoff; dry air supply |

### Starting a PAC cut

1. **Set amperage** per the machine manufacturer's chart for material type and thickness.
2. **Verify compressed air supply** — adequate pressure (typically 5–7 bar / 70–100 PSI), clean and dry. Moisture in the air plasma degrades cut quality and damages the nozzle.[^2]
3. **Position torch at the edge** (edge start) or **over the pierce point** (pierce start).
4. **Pilot arc/transferred arc:** on most machines, pulling the trigger establishes the pilot arc, then moving the torch to the work surface transfers the arc to the work. Some machines auto-transfer. Follow manufacturer procedure.
5. **Pierce start (for holes and internal cuts):** tilt the torch 30–45° away from yourself, initiate the arc, then rotate to vertical as the pierce completes — this directs the initial blow-out material away from the torch nozzle (otherwise molten blow-back destroys the nozzle).
6. **Begin travel** once the arc is fully transferred and cut is through.
7. **Release trigger** at end of cut — allow the post-flow gas (air) to continue for the machine's post-flow time before removing the torch from the work area (this cools the nozzle and extends consumable life).[^2]

### PAC safety

**Specific hazards for PAC:**[^1] [^6]

- **Noise:** plasma cutting is **extremely loud** — 95–120 dBA depending on material, thickness, and gas. Hearing protection is mandatory, not optional.
- **UV/IR radiation:** the plasma arc is more intense UV-emitting than a welding arc of the same amperage. Bystanders must be protected from stray arc radiation.
- **Electromagnetic interference:** high-frequency (HF) pilot arc ignition can interfere with electronic equipment, pacemakers, and sensitive instrumentation. Follow machine-specific guidance for HF-emitting systems.
- **Fumes:** cutting coated, galvanized, or stainless material with plasma produces the same toxic fume hazards as welding — manganese, hexavalent chromium (stainless), zinc oxide (galvanized). LEV or respiratory protection required.
- **Fire:** plasma sparks travel farther than oxyfuel sparks (higher velocity) — observe NFPA 51B clearance requirements (10 m / 35 ft of combustibles).

**Filter shade for PAC:** CSA Z94.3 recommends **Shade 8–9** for plasma arc cutting at 300–400 A typical production amperages. For portable units under 100 A, Shade 7 is often adequate — confirm against the CSA Z94.3 table.[^6]

---

## Air carbon arc cutting and gouging (CAC-A)

### How CAC-A works

CAC-A uses a DC arc between a **carbon graphite electrode** and the base metal to melt the metal, with a high-velocity jet of **compressed air** blowing the molten metal away. The result is a clean, smooth groove or cut in virtually any metal.[^3]

This is fundamentally different from plasma cutting: the carbon electrode does not melt into the groove — it merely provides the arc. The metal melted by the arc is mechanically ejected by the air jet. The groove produced is bright, clean, and free of slag — ready for welding with minimal preparation.

**Primary uses in the welding trade:**
- **Back-gouging:** removing the root pass of a full-penetration groove weld from the backside to ensure full fusion before depositing the backing weld pass
- **Defect removal:** opening a gouge to remove a crack, porosity pocket, or inclusion identified by NDT
- **Weld removal:** removing a weld that needs to be replaced
- **Chamfer preparation:** preparing joint edges where an oxyfuel bevel is not practical (e.g., stainless or aluminum)

CAC-A works on mild steel, stainless steel, cast iron, aluminum, copper, and nickel alloys. It is the fastest mechanical metal removal process available to a welder.[^3]

### CAC-A equipment

| Component | Description |
|---|---|
| **Welding machine** | DC constant-current (CC); most CAC-A is done on **DCEP (electrode positive / reverse polarity)**. AC is possible with special electrodes but DCEP is standard. Must be capable of the high amperages required (typically 200–1000 A). |
| **Carbon arc gouging torch (air arc torch)** | Holds the carbon electrode; has an integrated compressed air valve; air flows from jets positioned parallel to the electrode |
| **Carbon electrodes** | Graphite-coated with copper for conductivity. Comes in sizes from 4 mm to 25 mm diameter — size matched to amperage and desired groove width |
| **Compressed air supply** | Minimum 550–620 kPa (80–90 PSI) at the torch; flow rate 170–400 L/min depending on electrode size. Must be dry |

## Diagram
*(SVG to be added: `assets/diagrams/p1-s1-j-cac-a-torch.svg` — cross-section of a CAC-A torch showing: electrode grip/clamp, air valve, air jets positioned parallel and behind the electrode, direction of air flow ejecting molten metal, groove profile in base metal, and labels for correct electrode stick-out distance)*

### Polarity and settings

**DCEP (DC Electrode Positive / Reverse Polarity)** is standard for CAC-A. The electrode positive configuration concentrates more heat at the workpiece surface, enabling efficient metal removal. DCEN (electrode negative) is used rarely and only with specific electrodes for aluminum.[^3]

**Amperage selection by electrode diameter:**[^3]

| Electrode diameter | Typical amperage range |
|---|---|
| 4 mm (5/32 in.) | 90–150 A |
| 6 mm (1/4 in.) | 200–350 A |
| 8 mm (5/16 in.) | 300–450 A |
| 10 mm (3/8 in.) | 350–550 A |
| 13 mm (1/2 in.) | 450–700 A |

### Technique — gouging and back-gouging

**Electrode stick-out:** the electrode projects from the torch clamp **approximately 150–200 mm (6–8 in.)**. Longer stick-out increases electrical resistance, but is practical for reaching into tight areas.[^3]

**Hold angle:** the electrode is held at **35–45° from horizontal** for most gouging. The air jets should be positioned behind the electrode (away from the direction of travel) so the blast of air pushes the molten metal forward, away from the electrode.

**Travel direction:** travel into the groove (moving away from the torch handle direction). Consistent travel speed produces a uniform groove width and depth.

**Depth control:**
- To **increase groove depth:** slow travel speed or increase amperage
- To **reduce groove depth:** increase travel speed or decrease amperage
- To **increase groove width:** use a larger diameter electrode

**Back-gouging technique:**

After completing the initial side of a full-penetration groove weld (where no backing bar is used):
1. Turn the weldment over (or work from the opposite side).
2. Gouge along the root of the original weld — remove metal until bright, uncontaminated metal is visible and the root of the original weld is fully exposed.
3. The resulting back-gouge groove must be clean (no carbon deposits, no slag) before welding.
4. **Carbon contamination:** if carbon is deposited in the groove (from the electrode or from improper technique), it must be ground out — carbon in the weld produces hard brittle zones and porosity. **Bright shiny groove = clean; dull sooty groove = carbon contamination present.**[^3]

**Grinding after CAC-A:** a light grind with a flap disc removes any surface carbon contamination or copper from the electrode. This is standard practice before welding any back-gouged surface.

### CAC-A safety — additional hazards

CAC-A produces hazards beyond standard arc welding:[^1] [^3]

- **Intense noise:** the high-velocity compressed air blast produces 100–120 dBA of noise — higher than most arc welding processes. Double hearing protection (foam earplugs + earmuffs) is recommended for sustained CAC-A work.
- **Molten metal spray:** the air blast ejects molten metal at high velocity over distances up to 3 m (10 ft). A clear zone of at least 3 m around the operation is required — people and combustibles must be outside this zone.
- **Fume generation:** CAC-A produces greater fume volumes than most welding processes at comparable amperages. LEV is required in enclosed spaces; respiratory protection may be required even with LEV.
- **High amperages:** CAC-A runs at amperages that can cause significant cable heating — inspect cables for adequacy (ampacity) for the process amperage being used.
- **Galvanized and coated materials:** gouging through zinc coatings or paint produces toxic zinc oxide or isocyanate fumes — avoid without engineering controls (LEV, respiratory protection).

**Filter shade for CAC-A:** CSA Z94.3 recommends **Shade 12–14** for CAC-A at 150–500 A typical amperages.[^6]

---

## Comparison: PAC vs CAC-A vs OFC

| | Plasma Arc Cutting (PAC) | Air Carbon Arc Cutting (CAC-A) | Oxyfuel Cutting (OFC) |
|---|---|---|---|
| **Metals** | Any conductive metal | Any conductive metal | Mild steel only |
| **Cut quality** | Excellent (narrow kerf, low HAZ) | Good groove, some carbon pickup | Good on mild steel, rough on heavy section |
| **Primary use** | Cutting plate and shapes | Gouging, defect removal, back-gouging | Cutting mild steel plate, structural shapes |
| **Equipment cost** | Moderate–high | Low–moderate | Low |
| **Portability** | Requires air/power | Requires compressor + power | Cylinder-portable, no power needed |
| **Noise** | Moderate–high (95–120 dBA) | Very high (100–120 dBA) | Low (< 85 dBA) |
| **Fumes** | Moderate | High | Moderate |
| **Shade required** | Shade 7–9 | Shade 12–14 | Shade 3–5 (goggles) |

---

## Numbers you need to memorize

- **PAC plasma jet temperature:** **8 000–25 000°C**[^2]
- **PAC torch standoff distance:** **3–6 mm** (shield to plate)[^2]
- **PAC air supply pressure:** typically **5–7 bar (70–100 PSI)**[^2]
- **PAC noise level:** **95–120 dBA** — hearing protection mandatory[^1]
- **PAC filter shade (production, 300–400 A):** Shade **8–9**[^6]
- **CAC-A polarity:** **DCEP (electrode positive, reverse polarity)** — standard[^3]
- **CAC-A electrode stick-out:** **150–200 mm (6–8 in.)**[^3]
- **CAC-A air supply:** minimum **550–620 kPa (80–90 PSI)** at torch[^3]
- **CAC-A noise level:** **100–120 dBA** — double hearing protection recommended[^1]
- **CAC-A filter shade (150–500 A):** Shade **12–14**[^6]
- **CAC-A molten metal ejection radius:** up to **3 m (10 ft)** — clear zone required[^3]
- **CAC-A electrode hold angle:** **35–45° from horizontal**[^3]

---

## What the textbook doesn't tell you

**PAC consumables die fast if you don't use post-flow.** The torch nozzle and electrode are relatively inexpensive but they are definitely consumables. Pulling the torch away from the work the instant you release the trigger, without allowing the post-flow gas to cool the nozzle, shortens consumable life dramatically. The post-flow is 3–8 seconds depending on amperage — wait for it. Experienced operators tell the difference immediately between a torch with good consumable life and one that's been treated carelessly by looking at the nozzle orifice.[^2]

**The pierce tilt on plasma is non-negotiable.** Every apprentice who ignores the 30–45° pierce tilt on the first day destroys a nozzle. The molten blow-back from a vertical pierce entry travels straight up into the nozzle orifice, deposits inside, and the next few cuts have a distorted, off-centre plasma jet. Tilt on the pierce, straighten up once the material is through. Takes two seconds to learn, costs a nozzle if you skip it.[^2]

**CAC-A carbon contamination is invisible and causes weld failures.** A back-gouge groove that looks clean may have a thin layer of carbon on the surface from the electrode. Carbon content at the fusion zone of the next weld pass causes localized martensite (hard, brittle) and can contribute to cracking in higher-strength steels. The standard practice is to grind after every CAC-A groove before welding — not because the groove looks dirty, but because of what you can't see.[^3]

**CAC-A on aluminum produces a different result.** On aluminum, CAC-A is done with DCEN (electrode negative) and requires immediate cleanup — aluminum absorbs carbon very efficiently, and even a brief soak produces a surface layer that must be ground out before welding. Some jurisdictions restrict CAC-A on aluminum for this reason. If your WPS specifies PAC for aluminum groove preparation, don't substitute CAC-A.[^3]

**Plasma tables don't eliminate all of the manual-cutting hazards.** CNC plasma tables are increasingly common in fabrication shops, and apprentices may operate them. The arc radiation, fume generation, and noise hazards are the same as hand PAC — the automation removes operator fatigue and positioning error, not the hazards. Water-table plasma systems (where the workpiece sits in water) significantly reduce fume and noise at the operator position but create a water management (wet slag) issue and require grounded water system precautions.[^2]

---

## Key terms

- **Plasma:** the fourth state of matter — a partially or fully ionized gas that conducts electricity and produces intense heat
- **PAC (Plasma Arc Cutting):** uses a constricted ionized gas jet to melt and eject metal from any conductive material
- **Transferred arc:** the condition in PAC where the arc jumps from the electrode to the workpiece (the productive cutting condition)
- **Pilot arc:** initial non-transferred arc between electrode and nozzle — ionizes the gas to allow transfer
- **Standoff distance:** the gap between the torch nozzle/shield and the plate surface — critical for cut quality
- **Kerf:** the slot produced by the cutting process
- **CAC-A (Air Carbon Arc Cutting and Gouging):** uses a DC arc from a carbon electrode and a compressed air blast to melt and remove metal — primarily used for gouging
- **DCEP (DC Electrode Positive, Reverse Polarity):** polarity standard for CAC-A — electrode connected to positive terminal
- **Back-gouging:** removing the root of a weld from the back side to ensure full penetration before depositing a backing weld
- **Carbon contamination:** deposit of carbon from the CAC-A electrode on the groove surface — must be ground out before welding
- **Post-flow:** the period of gas flow after the PAC arc stops — cools the nozzle and extends consumable life
- **Double-arc:** damage condition in PAC where the arc jumps from electrode to nozzle instead of or in addition to the workpiece — caused by excessive standoff or nozzle contamination

---

## Common exam trap

- **PAC polarity:** PAC power supplies are **DC**. The electrode inside the torch is typically DCEN (electrode negative) — the workpiece is positive. This is often confused with the machine output labeling. The key fact is that PAC power supplies are DC, not AC.
- **CAC-A polarity: DCEP, not DCEN.** Standard for carbon steel and most metals. The distractor offering DCEN for CAC-A is wrong for steel/stainless/cast iron. (DCEN is used for aluminum — a specialty application.)
- **PAC works on stainless, aluminum, copper:** the oxyfuel "mild steel only" limitation does NOT apply to PAC. A question that lists "stainless steel" as a material PAC cannot cut is wrong.
- **Filter shades:** PAC requires lower shade (7–9) than CAC-A (12–14) at typical amperages. Distractors may suggest the same shade for both.
- **CAC-A noise hazard:** CAC-A is explicitly louder than CAC-A welding and louder than plasma cutting in many applications — "single earplugs are sufficient" is wrong. Double hearing protection.
- **Post-flow omission:** a question about extending consumable life on a plasma torch — the correct answer always includes allowing post-flow to complete. Removing the torch before post-flow expires damages consumables.
- **Carbon contamination in back-gouge:** "the back-gouge is ready to weld as soon as it looks clean and shiny" is close but not complete. The complete answer includes grinding to remove surface carbon before welding.

---

## Practice question preview

**Q:** A welder needs to remove a 150 mm crack in a 20 mm stainless steel plate by back-gouging to allow rewelding. Which cutting process is most appropriate, and what is the required post-gouge preparation?

A) Oxyfuel cutting — used for all heavy plate removal; grind the groove smooth before rewelding  
B) Plasma arc cutting — PAC can cut stainless steel; no post-cut preparation needed for welding  
C) Air carbon arc cutting (CAC-A) with DCEP; follow with grinding to remove carbon contamination before welding  
D) Plasma arc cutting — PAC can cut stainless; plasma produces no HAZ requiring preparation  

**Correct: C**

**Explanation:** CAC-A is the preferred process for defect excavation and back-gouging because it produces a clean groove that can be controlled in depth and width, and it works on stainless steel. DCEP is the correct polarity. However, CAC-A on stainless steel deposits carbon on the gouge surface — this **must be ground out** before welding to prevent carbon contamination of the weld root (which would cause intergranular carbide precipitation and corrosion failure in stainless steel). Option A is wrong because OFC does not work on stainless steel (stainless forms a refractory chromium oxide that quenches the oxidation cutting reaction). Option B is partially correct (PAC does cut stainless) but PAC is not the standard process for defect excavation — it is a cutting, not a gouging, process; and "no preparation" is incorrect regardless of process. Option D incorrectly states PAC produces no HAZ — PAC does produce a narrow HAZ in stainless.

**Red Seal mapping:** C-12.01 (Sets up air carbon arc cutting equipment), C-12.02 (Performs air carbon arc cutting — process selection and post-gouge preparation)

---

[^1]: [CSA W117.2 — Safety in Welding, Cutting, and Allied Processes (2019)](https://www.csagroup.org/store/product/CSA%20W117.2%3A19/), Clause 6 (electrical safety for PAC and CAC-A — DC polarity, insulation, shock prevention); Clause 7 (noise hazard — PAC 95–120 dBA, CAC-A 100–120 dBA — hearing protection); Clause 10 (confined space operations — fume control requirements)
[^2]: [Hypertherm — Plasma Arc Cutting Handbook (public)](https://www.hypertherm.com/en-US/learn/education/resources/), Process overview (plasma temperatures 8 000–25 000°C); equipment components (electrode, nozzle, shield); gas selection by metal type; cut quality diagnostics; standoff distance (3–6 mm); air supply pressure (70–100 PSI); post-flow cooling; pierce technique (tilt 30–45°); consumable life best practices
[^3]: [Lincoln Electric — Air Carbon Arc Cutting and Gouging Guide](https://www.lincolnelectric.com/en/education-center/welding-education/air-carbon-arc-cutting), DCEP polarity for CAC-A; amperage selection by electrode diameter; air supply requirements (80–90 PSI, 80–90 PSI, 170–400 L/min); electrode stick-out (150–200 mm); back-gouging technique; carbon contamination identification and grinding requirement; aluminum DCEN exception; molten metal ejection radius (10 ft / 3 m)
[^4]: [Modern Welding (Bowditch, Goodheart-Willcox)](https://www.goodheartwillcox.com/products/modern-welding), Chapter 16 "Plasma Arc Cutting": process physics, equipment overview, gas selection, cut quality parameters, travel speed diagnostics; Chapter 17 "Air Carbon Arc Cutting": process mechanics, groove profile control, depth/width adjustment by amperage and speed, back-gouging application
[^5]: [Red Seal Occupational Standard — Welder (2024)](https://red-seal.ca/_conf/assets/custom/docms/welder/rsos-eng.pdf), Block C Task C-11 (PAC sub-tasks C-11.01–C-11.02 performance criteria) and Task C-12 (CAC-A sub-tasks C-12.01–C-12.02 performance criteria)
[^6]: [Alberta OHS Code 2023](https://open.alberta.ca/publications/occupational-health-and-safety-code), Part 18 (PPE), s.230 (filter shade selection references CSA Z94.3); [CSA Z94.3 — Eye and Face Protectors (2020)](https://www.csagroup.org/store/product/CSA%20Z94.3%3A20/), Table 1 — filter shade by process: PAC 300–400 A = Shade 8–9; CAC-A 150–500 A = Shade 12–14
