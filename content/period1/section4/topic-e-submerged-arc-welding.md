---
id: p1-s4-e
period: 1
section: 4
section_title: Gas Metal Arc Welding (GMAW), Flux-Cored Arc Welding (FCAW), Metal-Cored Arc Welding (MCAW) and Submerged Arc Welding (SAW)
topic_letter: E
topic_title: Submerged Arc Welding (SAW)
hours: 3
weight_pct: 1
outcome: >
  Upon successful completion, learners will be able to identify and describe the
  components, consumables, and operation of the SAW process.
objectives:
  - Describe the operating principles of SAW.
  - Identify the components of SAW.
  - Describe SAW power sources and equipment.
  - Describe SAW operating variables.
  - Identify SAW filler metals and fluxes.
  - Identify advantages and disadvantages of SAW.
red_seal_mapping:
  - D-16.01 (Selects SAW equipment and consumables)
  - D-16.02 (Sets up SAW equipment)
  - D-16.03 (Sets operating parameters for SAW)
  - D-16.04 (Performs weld using SAW equipment)
citations:
  - source: Lincoln Electric — The Submerged Arc Welding Process (public education)
    ref: SAW operating principles, flux types (fused, bonded, agglomerated), wire classifications, current ranges, deposition rates
    url: https://www.lincolnelectric.com/en/education-center/welding-processes/saw
  - source: ESAB — Handbook of Arc Welding (public)
    ref: SAW equipment components, flux hopper and recovery, CC vs CV SAW power sources, operating variables
    url: https://www.esab.com/en/us/education/blog/the-esab-handbook
  - source: AWS A5.17 — Specification for Carbon Steel Electrodes and Fluxes for Submerged Arc Welding (2019)
    ref: Wire classification system, flux classification, flux-wire combination testing
    url: https://www.aws.org/standards/page/aws-a517
  - source: Modern Welding (Bowditch, Goodheart-Willcox, latest edition)
    ref: Chapter 17 (Submerged Arc Welding — operating principles, components, fluxes, applications)
    url: https://www.goodheartwillcox.com/products/modern-welding
  - source: AIT Welder Curriculum Guide 012 (2026), Period 1 Section 4 Topic E
    ref: pp. 206–215 (Submerged Arc Welding)
    url: https://tradesecrets.alberta.ca/SOURCES/PDFS/CURRICULUM_GUIDES/012_OUTLINE.PDF
---

# Submerged Arc Welding (SAW)

You can't see the arc in SAW — the arc is buried under a blanket of granular flux. You can't hear it the way you hear SMAW or GMAW — the submerged arc is almost completely silent to the operator. What you can see is a dramatic amount of weld metal being deposited at speeds and rates that no manual process approaches. SAW is the process of choice for heavy structural fabrication, pressure vessel manufacture, shipbuilding, and pipe manufacturing.

---

## Operating principles — how SAW works

In SAW, the welding arc is struck between a continuously fed electrode wire and the base metal, but the arc is completely submerged under a layer of granular flux.[^1] [^4]

**Step-by-step operation:**

1. A granular flux blanket is deposited ahead of the arc by a hopper mounted on the welding head (the flux falls by gravity ahead of the wire tip)
2. The electrode wire feeds from a spool through the contact tube (similar to GMAW) into the flux blanket
3. The arc is struck beneath the flux — the arc is invisible and the intense UV radiation is completely blocked by the flux
4. The flux melts in the arc zone: the inner portion becomes molten slag that floats over the weld pool; the outer portion remains granular and is recovered for reuse
5. The arc generates intense heat (SAW currents run 200–1,500 A or higher) that melts the wire and base metal at very high rates[^1]
6. After the weld is completed, the molten slag solidifies into a glassy layer (like SMAW slag) and is removed by chipping; the unmelted granular flux is vacuumed up by the flux recovery system and reused

**The key result:** Because the arc is submerged, virtually no UV radiation escapes — no welding helmet is required during the weld (though PPE is still required for setup, slag removal, and flux handling). Smoke and fume generation is also very low compared to other arc processes.

---

## Components of a SAW system

| Component | Function |
|---|---|
| **Power source (CC or CV)** | Provides the welding current — typically 600–1,500 A capacity for industrial SAW |
| **Wire feeder** | Feeds the solid electrode wire from a large coil (25–50 kg coils common) |
| **Contact tube** | Transfers current to the wire (similar to GMAW contact tip but designed for higher current) |
| **Flux hopper** | Stores and meters granular flux — deposits flux ahead of the arc |
| **Flux recovery system** | Vacuum or suction system that recovers unmelted flux from behind the weld bead for reuse |
| **Travel carriage (tractor)** | Motorized carriage that moves the welding head along the joint at a controlled, precise travel speed |
| **Work positioner/turning rolls** | Equipment that rotates or positions the workpiece for flat welding position (SAW is flat only) |
| **Control panel** | Sets and monitors current, voltage, travel speed, wire feed speed |
| **Electrode wire coil/drum** | 25 kg coils or 250+ kg bulk drums — SAW consumes large quantities of wire |

---

## Power sources for SAW

SAW uses higher currents than any manual process:[^1] [^2]

### Constant Current (CC) for SAW

- Similar to SMAW in that arc voltage varies naturally with arc length
- For SAW, voltage-sensing automatic arc length control (AVC) adjusts WFS to maintain voltage
- Better suited for single-wire SAW with precise voltage control requirements
- Typical: 600–1,200 A range for CC SAW

### Constant Voltage (CV) for SAW

- Self-regulating arc (same principle as GMAW) — simpler control
- More common for multi-wire SAW systems
- Typical: 400–1,000 A range for CV SAW

**Typical SAW current ranges:**[^1]
- Light structural applications: 200–500 A
- Medium structural (pressure vessels, beams): 400–800 A
- Heavy applications (thick plate, multi-wire): 800–1,500 A

The extreme heat generated at these amperages is why SAW achieves its extraordinary deposition rates — and also why it is confined to the flat (1G) and horizontal (2G) positions. The fluid, high-temperature weld pool cannot be controlled against gravity in any other position.

---

## Flux types — the most important material in SAW

In SAW, the flux does everything the shielding gas does in GMAW, plus it forms the slag blanket. The flux type has a major effect on arc characteristics, weld chemistry, and weld metal properties.[^1] [^2] [^3]

### Fused flux

**Manufacturing:** raw mineral ingredients are mixed and melted together in a furnace, then the melt is solidified and crushed to produce granules. All components are chemically combined.

| Property | Detail |
|---|---|
| **Homogeneity** | Very consistent — all granules have the same chemistry |
| **Hygroscopicity** | Low — resists moisture absorption better than bonded flux |
| **Arc stability** | Excellent — consistent chemistry = consistent arc |
| **Flux composition variability** | Low — cannot easily change the chemistry |
| **Primary use** | High-deposition, high-quality applications where consistency and low moisture are critical; pipeline; pressure vessels |

### Bonded flux (agglomerated flux)

**Manufacturing:** raw ingredients are mixed with a binder (typically potassium silicate), formed into granules (agglomerated), and then baked at lower temperatures than fused flux.

| Property | Detail |
|---|---|
| **Homogeneity** | Less than fused — some variability granule-to-granule |
| **Hygroscopicity** | Higher than fused — bonded flux absorbs moisture more readily; requires controlled storage in sealed containers or heated storage |
| **Flexibility** | Easier to modify the chemistry — alloy additions can be incorporated |
| **Arc stability** | Good — may require slightly higher voltage for stable arc vs. fused |
| **Primary use** | Structural steel, general fabrication, applications where alloy additions to the weld are needed |
| **Important:** Must be re-dried if moisture is absorbed (similar to low-hydrogen SMAW electrodes) |

### Agglomerated vs bonded

In industry, "bonded" and "agglomerated" are sometimes used interchangeably. Technically, bonded flux uses a chemical binder and low-temperature baking; agglomerated often refers to a ceramic-based or extruded form. For the Red Seal exam, know fused vs. bonded/agglomerated as two distinct types.[^1]

---

## SAW wire (electrode) classification — AWS A5.17

SAW wire for carbon and low-alloy steel is classified per AWS A5.17:[^3]

**Wire format: EX-X**

| Segment | Meaning |
|---|---|
| **E** | Electrode |
| **X** (1st) | Chemical composition class (L = low manganese, M = medium manganese, H = high manganese) |
| **X** (2nd) | Carbon content class (K, T, P — increasing carbon) |

**Common SAW wire examples:**

| AWS classification | Characteristic | Typical use |
|---|---|---|
| EL8 | Low manganese, low carbon | Mild steel structural with active flux |
| EM12K | Medium manganese, medium carbon | General mild steel SAW |
| EH14 | High manganese, medium-high carbon | Combined with specific fluxes for alloying |

**Flux-wire combinations:** In SAW, the wire and flux are selected as a COMBINATION to achieve the desired weld metal chemistry and mechanical properties. The flux transfers alloying elements to the weld (or picks them up from the base metal). You cannot arbitrarily mix any wire with any flux — check the flux-wire combination classification for the required deposit chemistry.[^1] [^3]

---

## SAW operating variables

The main process variables in SAW (similar to GMAW):[^1] [^2]

| Variable | Effect |
|---|---|
| **Amperage (WFS)** | Controls penetration depth and deposition rate — primary variable |
| **Voltage** | Controls bead width and flux consumption; higher V = wider, flatter bead; lower V = narrower, more convex bead |
| **Travel speed** | Controls bead width and heat input per unit length |
| **Wire diameter** | Larger diameter = higher current capacity = higher deposition at same current density |
| **Electrode extension** | Longer extension = more resistance preheat of wire = higher effective deposition at lower arc heat (important for controlling heat input) |
| **Polarity** | DCEP provides deeper penetration; DCEN provides higher deposition rate (similar to SMAW); AC is used for multi-wire setups to prevent arc blow |
| **Flux coverage depth** | 25–40 mm of flux above the arc is typical — too thin exposes the arc; too thick produces poor bead shape |

---

## Deposition rates — why SAW dominates heavy fabrication

SAW deposition rates are dramatically higher than any manual process:[^1]

| Process | Typical deposition rate |
|---|---|
| SMAW (E7018, 1/8") | 1–3 kg/hr |
| GMAW (ER70S-6, 0.045", spray) | 3–7 kg/hr |
| FCAW (E71T-1, 0.045") | 4–10 kg/hr |
| SAW (single wire, 5/32") | 10–20 kg/hr |
| SAW (twin-wire or multi-wire) | 20–50+ kg/hr |

**Why so high?**
- Continuous wire feed from large coils — no electrode change stops
- High current (400–1,500 A) melts wire and base metal extremely fast
- Flux blanket allows the full arc heat to go into the weld — no radiation losses
- Nearly 100% deposition efficiency — no significant spatter, minimal slag sticking losses

---

## Advantages and disadvantages of SAW

### Advantages

| Advantage | Detail |
|---|---|
| **Highest deposition rate** | Dramatically outperforms all other arc welding processes on thick plate in flat/horizontal |
| **Deep penetration** | High heat input achieves CJP in a single pass on thick plate that other processes would need multiple passes for |
| **No UV radiation** | Arc is completely buried — no welding helmet required while welding (though PPE still required) |
| **Very low fume/smoke** | The flux blanket suppresses smoke and fumes |
| **No arc flash risk to bystanders** | SAW can operate safely near other workers without screens |
| **Excellent weld quality** | Consistent, high-quality welds — the submerged arc produces very stable conditions |
| **High flux utilization** | Unmelted flux is recovered and reused |

### Disadvantages

| Disadvantage | Detail |
|---|---|
| **Flat and horizontal position only** | The fluid, high-temperature pool is controlled by gravity — SAW cannot be done out of position |
| **Not portable** | The carriage, flux system, recovery system, and large power source are heavy and fixed or semi-mobile |
| **High setup cost** | Significant capital cost for the tractor, flux handling system, and power source |
| **Joint preparation is critical** | The operator cannot see the arc — any fit-up problem (gap variation, offset) is not visible until the weld is done and inspected |
| **High heat input** | The very high amperages produce high heat input — can cause distortion, HAZ softening in HSLA steels, and wide HAZs that affect toughness |
| **Flux management** | Flux storage, drying (for bonded flux), and recovery add complexity to the process |

---

## Diagram

*(SVG to be added: `assets/diagrams/p1-s4-e-saw-process.svg` — cross-section and side-view diagram of the SAW process showing: electrode wire feeding from spool through contact tube into flux blanket; flux hopper depositing granular flux ahead of the arc; the buried arc zone (shown in cut-away) with molten weld pool, molten slag layer, and solidified slag behind; granular unmelted flux ahead; flux recovery vacuum system behind; work carriage travel direction arrow; labels for each component)*

---

## Numbers you need to memorize

- **SAW positions: flat and horizontal ONLY** — no vertical, no overhead[^1]
- **Typical SAW current range: 200–1,500 A**[^1]
- **SAW deposition rate (single wire): 10–20 kg/hr** — far exceeds any manual process[^1]
- **Flux layer depth above arc: approximately 25–40 mm**[^1]
- **Fused flux: lower hygroscopicity** (better moisture resistance) than bonded flux[^1] [^2]
- **Bonded/agglomerated flux: higher moisture absorption** — requires controlled storage and drying[^1]
- **SAW deposition efficiency: approaching 100%** — very low spatter, flux is recovered[^1]
- **SMAW deposition rate (comparison): 1–3 kg/hr** (SAW is 5–15× faster)[^1]

---

## What the textbook doesn't tell you

**SAW operators don't wear a helmet while welding — and this can create a false sense of safety.** Because the arc is buried, there's no UV exposure risk during welding. But the moment you stop the arc and start chipping the hot slag layer, there is a serious eye hazard (hot slag chips, possible heat radiation). PPE for slag removal is mandatory. Also, the flux layer itself can be at 300–500°C after the arc passes — picking up the hot, unmelted flux granules too quickly can cause burns. Let it cool or use the flux recovery system.

**Fit-up is everything in SAW.** In manual welding, a skilled welder can compensate for imperfect fit-up by adjusting technique in real time. SAW is automated — the carriage runs at a set speed, the wire feeds at a set rate, and the arc goes where it goes. If the root opening varies by 2 mm over the weld length, the penetration will vary and you might get incomplete fusion. SAW demands excellent fit-up preparation before the arc is struck.

**Flux recovery doesn't mean the same flux runs forever.** Recovered flux should be mixed with fresh flux in proportions specified by the manufacturer (a typical starting point is 50% recovered / 50% fresh, then verify with testing). Recycled flux accumulates fine particles (fines) from crushing during reuse, and these fines can affect arc stability and bead shape. Screen recovered flux to remove fines before reuse.[^2]

---

## Key terms

- **SAW (Submerged Arc Welding):** arc welding process where the arc is completely buried under a granular flux blanket
- **Flux (SAW):** granular mineral material that melts around the arc to form slag (protects and shapes the weld) and the outer unmelted layer is recovered for reuse
- **Fused flux:** manufactured by melting raw flux ingredients together — homogeneous, low hygroscopicity, excellent arc stability
- **Bonded/agglomerated flux:** manufactured by binding powdered ingredients with a binder — more flexible chemistry, higher moisture sensitivity, requires drying
- **Contact tube:** in SAW, the current-carrying conductor through which the electrode wire passes (equivalent to GMAW contact tip but at much higher current capacity)
- **Flux hopper:** the container that deposits granular flux ahead of the arc
- **Flux recovery:** the vacuum system that recovers unmelted granular flux for reuse after the arc passes
- **Travel carriage (tractor):** the motorized platform that moves the welding head at a controlled speed
- **Deposition rate:** the mass of weld metal deposited per hour — SAW achieves the highest deposition rates of any arc welding process
- **Electrode extension:** the length of wire protruding beyond the contact tube — longer extension increases resistance preheating of the wire

---

## Common exam trap

- **"SAW can be used in vertical position if the current is reduced"** — false. SAW is physically confined to flat and horizontal positions by the nature of the fluid, high-temperature weld pool and the granular flux system. Reducing current doesn't change this — the flux cannot stay in place on a vertical joint.
- **"Fused flux must be dried before use because it absorbs moisture"** — this applies to bonded/agglomerated flux, not fused flux. Fused flux has lower hygroscopicity. Bonded flux requires controlled storage and re-drying.
- **"The SAW operator wears a standard auto-darkening helmet during welding"** — false. The arc is completely submerged — no helmet is needed during the weld itself. PPE is still required for setup and slag removal.
- **"SAW wire can be matched with any available SAW flux"** — false. Wire and flux must be selected as a matched combination (flux-wire pair) to achieve the specified weld metal chemistry and mechanical properties per AWS A5.17. Using mismatched flux and wire may not produce the required mechanical properties.

---

## Practice question preview

**Q:** A fabricator producing heavy wall pressure vessel sections needs the highest possible deposition rate on flat-position groove welds in 50 mm thick mild steel plate. Which welding process is MOST appropriate?

A) SMAW with E7018 electrodes  
B) GMAW with ER70S-6 wire in spray transfer  
C) Submerged arc welding (SAW) with matched wire and flux  
D) FCAW with E71T-1 gas-shielded wire  

**Correct: C**

**Explanation:** SAW achieves the highest deposition rates of any common arc welding process (10–20+ kg/hr single wire vs. 1–3 kg/hr for SMAW and 3–10 kg/hr for GMAW/FCAW). For flat-position heavy plate groove welding, SAW is the industrial standard for deposition rate and efficiency. Option A (SMAW) has the lowest deposition rate. Option B (GMAW spray) is suitable but has much lower deposition than SAW. Option D (FCAW) is good but still far below SAW deposition rates. SAW also provides nearly 100% deposition efficiency (minimal waste) and very low fume generation.

**Red Seal mapping:** D-16.01 (Selects SAW equipment and consumables — identifies SAW as the appropriate process for high-deposition flat-position welding on thick plate)

---

[^1]: [Lincoln Electric — The Submerged Arc Welding Process](https://www.lincolnelectric.com/en/education-center/welding-processes/saw), operating principles (arc buried under flux), SAW current ranges (200–1,500 A), deposition rates (10–20 kg/hr single wire, multi-wire higher), position restriction (flat/horizontal only), flux layer depth (~25–40 mm), deposition efficiency (~100%), fused vs bonded flux comparison, advantages (no UV, high deposition, low fume) and disadvantages (position limited, fit-up critical)
[^2]: [ESAB — Handbook of Arc Welding](https://www.esab.com/en/us/education/blog/the-esab-handbook), SAW component descriptions (contact tube, flux hopper, flux recovery, travel carriage), CC vs CV power source for SAW, operating variables (amperage controls penetration; voltage controls bead width), flux recovery mixing ratio (50/50 typical), bonded flux moisture sensitivity and drying requirements
[^3]: [AWS A5.17 — Specification for Carbon Steel Electrodes and Fluxes for Submerged Arc Welding (2019)](https://www.aws.org/standards/page/aws-a517), wire classification system (EL8, EM12K, EH14), flux classification, flux-wire combination testing requirements, weld metal mechanical property requirements
[^4]: [Modern Welding (Bowditch, Goodheart-Willcox)](https://www.goodheartwillcox.com/products/modern-welding), Chapter 17 "Submerged Arc Welding": operating principles description, component identification, advantages and disadvantages, comparison of deposition rates to other processes
