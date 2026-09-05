---
id: p1-s4-c
period: 1
section: 4
section_title: Gas Metal Arc Welding (GMAW), Flux-Cored Arc Welding (FCAW), Metal-Cored Arc Welding (MCAW) and Submerged Arc Welding (SAW)
topic_letter: C
topic_title: Wire Feed Welding Shielding Gases
hours: 6
weight_pct: 3
outcome: >
  Upon successful completion, learners will be able to identify shielding gases and
  supply systems for wire feed processes.
objectives:
  - Identify shielding gases for wire feed processes.
  - Identify shielding gas supply systems.
red_seal_mapping:
  - D-14.01 (Selects FCAW, MCAW and GMAW gas, equipment and consumables)
  - D-14.02 (Sets up FCAW, MCAW and GMAW equipment)
  - D-14.03 (Sets operating parameters for FCAW, MCAW and GMAW)
citations:
  - source: AWS A5.32 — Specification for Welding Shielding Gases (2011)
    ref: Full standard — purity requirements, classification of shielding gas mixtures for arc welding
    url: https://www.aws.org/standards/page/aws-a532
  - source: Lincoln Electric — Shielding Gas Selection Guide (public)
    ref: Gas selection by process, transfer mode effects, CO₂/Argon mix comparison, flow rates
    url: https://www.lincolnelectric.com/en/education-center/welding-education/shielding-gas-selection
  - source: Miller Electric — Shielding Gas Guide (public)
    ref: Gas effects on arc (penetration, spatter, bead shape), flow rate recommendations, cylinder types
    url: https://www.millerwelds.com/resources/article-library/mig-gmaw-welding-guide
  - source: ESAB — Handbook of Arc Welding (public)
    ref: Shielding gas chemistry, Argon/CO₂ mix ratios, tri-mix gases for stainless, gas supply systems
    url: https://www.esab.com/en/us/education/blog/the-esab-handbook
  - source: AIT Welder Curriculum Guide 012 (2026), Period 1 Section 4 Topic C
    ref: pp. 182–192 (shielding gases for wire feed processes)
    url: https://tradesecrets.alberta.ca/SOURCES/PDFS/CURRICULUM_GUIDES/012_OUTLINE.PDF
---

# Wire Feed Welding Shielding Gases

Shielding gas is not an afterthought — it is an active participant in the arc chemistry. The gas you choose determines what transfer mode is achievable, how much spatter you clean up, whether you can weld out of position, and the profile and mechanical properties of the completed weld. Getting the gas wrong is one of the most common setup errors on wire feed processes.

---

## Why shielding gas is needed

When arc temperatures melt steel (above ~1,500°C), the molten metal is extremely reactive to atmospheric gases:[^1] [^2]

- **Oxygen (O₂):** oxidizes the weld metal, consuming alloying elements and reducing strength and ductility; causes porosity and slag inclusions
- **Nitrogen (N₂):** dissolves in molten weld metal; when the weld cools, nitrogen becomes insoluble and forms porosity (elongated pores); also creates iron nitrides that reduce toughness
- **Water vapour (H₂O):** introduces hydrogen, which causes delayed cold cracking (HAC)

The shielding gas forms an inert or semi-reactive envelope around the arc and the weld pool, displacing the atmosphere.

**For self-shielded FCAW:** the flux core generates its own shielding gas (primarily CO₂ and CO) from organic compounds in the flux — no external gas is required.

---

## The primary shielding gases and their properties

### Carbon dioxide (CO₂ — 100%)

**Classification:** active gas (reactive with the arc)[^1] [^3]

**Arc chemistry:** CO₂ partially dissociates in the arc into CO and free oxygen at arc temperatures. The free oxygen provides some oxidation, which contributes to good penetration but also increases oxidation of alloying elements.

| Property | Effect |
|---|---|
| **Penetration** | Deep — higher penetration than Argon-rich mixes for the same settings |
| **Spatter** | HIGH — CO₂ promotes globular and erratic transfer; spray transfer is NOT achievable with pure CO₂ |
| **Transfer modes** | Short-circuit and globular only — spray transfer requires Argon content |
| **Bead shape** | Narrower, deeper profile |
| **Arc** | Stiffer, more turbulent arc |
| **Cost** | Lowest — CO₂ is the cheapest shielding gas |
| **Applications** | FCAW gas-shielded (C suffix electrodes); GMAW where cost is primary concern and out-of-position work is not needed; thick structural plate |

**Typical flow rate for CO₂ shielding on GMAW/FCAW:** 25–35 CFH (11.8–16.5 L/min)[^2] [^3]

---

### Argon (Ar — 100%)

**Classification:** inert gas — does not react with the arc or weld metal[^1] [^3]

**Arc chemistry:** pure Argon provides no active chemistry. The arc is very stable. The inert nature means alloying elements are preserved.

| Property | Effect |
|---|---|
| **Penetration** | Shallower than CO₂ for steel — profile is "finger-shaped" in cross-section |
| **Spatter** | Very low |
| **Transfer modes** | Spray transfer achievable; short-circuit achievable |
| **Bead shape** | Wider, flatter profile |
| **Arc** | Very smooth and stable |
| **Applications for steel welding** | Generally NOT used alone for steel (profile is poor — finger penetration); **primary use: aluminum and other non-ferrous metals** |

**For aluminum:** 100% Argon is the standard shielding gas for GMAW and GTAW of aluminum. The argon also provides arc cleaning action on aluminum's surface oxide layer.[^3]

**Typical flow rate for 100% Argon:** 20–30 CFH (9.5–14.2 L/min)[^2] [^3]

---

### 75/25 Argon/CO₂ (also written C25, or Ar-25% CO₂)

**The most common GMAW shielding gas in North American mild steel fabrication.**[^1] [^2]

| Property | Effect |
|---|---|
| **Transfer modes** | Short-circuit and globular — **75% Ar is below the minimum for spray transfer** (need ~80%+ Ar for spray) |
| **Penetration** | Moderate — deeper than 100% Ar, shallower than 100% CO₂ |
| **Spatter** | Low-moderate — significantly less than CO₂ alone |
| **Bead shape** | Good profile — slightly convex |
| **Arc** | Stable, smooth — better than CO₂ |
| **Positions** | All positions — especially with short-circuit transfer |
| **Applications** | General GMAW mild steel in all positions; the default choice when you don't have a specific reason to choose otherwise |

**Typical flow rate:** 25–45 CFH (11.8–21.2 L/min)[^2] [^3]

**Note on the 80% Ar threshold:** The transition to spray transfer requires approximately 80% or more Argon content in the mix. 75/25 Ar/CO₂ falls just below this threshold. To run spray transfer, you need 90/10 or higher Argon content.[^1]

---

### 90/10 Argon/CO₂ (also written C10, or Ar-10% CO₂)

| Property | Effect |
|---|---|
| **Transfer modes** | Short-circuit, globular, AND **spray transfer** achievable (90% Ar is above the ~80% minimum for spray) |
| **Penetration** | Deep for spray transfer; moderate for short-circuit |
| **Spatter** | Very low (especially in spray) |
| **Bead shape** | Wider, good fill |
| **Applications** | GMAW spray transfer on mild steel (flat and horizontal); MCAW with E70C-6M |

**Typical flow rate:** 30–45 CFH (14.2–21.2 L/min)[^2] [^3]

---

### Tri-mix gases (for stainless steel)

For GMAW and FCAW of stainless steel, a three-component gas is often used to balance penetration, stability, and prevention of sensitization (carbide precipitation):[^3] [^4]

**Common tri-mix for stainless GMAW:**

**90% Helium / 7.5% Argon / 2.5% CO₂** (or similar formulations)

| Component | Role |
|---|---|
| **Helium (He)** | Increases arc energy (helium arc is hotter than Ar arc for the same current); improves penetration and travel speed |
| **Argon (Ar)** | Provides arc stability |
| **CO₂ (small %)** | Stabilizes the arc; controls the weld profile |

**Why CO₂ content must be low for stainless:** excess CO₂ (carbon) causes carbon pickup in the weld metal and can precipitate chromium carbides at grain boundaries — sensitization — which destroys the corrosion resistance of stainless steel. The CO₂ content in stainless shielding gas is kept very low (typically ≤ 2.5%).[^3]

---

## Shielding gas reference table

| Gas | % composition | Transfer modes | Penetration | Spatter | Positions | Primary application |
|---|---|---|---|---|---|---|
| **100% CO₂** | — | Short-circuit, globular | Deep | High | All | FCAW-G (C suffix); budget GMAW |
| **100% Argon** | — | Short-circuit, spray | Shallow (finger) | Very low | All | Aluminum welding |
| **75/25 Ar/CO₂** | 75% Ar + 25% CO₂ | Short-circuit, globular | Moderate | Low-moderate | All | General mild steel GMAW |
| **90/10 Ar/CO₂** | 90% Ar + 10% CO₂ | Short-circuit, globular, spray | Deep (spray) | Very low | All / F+H for spray | Spray GMAW; MCAW |
| **98/2 Ar/O₂** | 98% Ar + 2% O₂ | Spray | Deep | Low | F+H | Stainless spray GMAW |
| **Tri-mix (He/Ar/CO₂)** | ~90%He/7.5%Ar/2.5%CO₂ | Spray | Deep | Low | F+H | Stainless GMAW |
| **None** | N/A | Short-circuit | Moderate | Moderate | All | Self-shielded FCAW (E71T-11) |

---

## Gas flow rates — typical ranges

**Typical flow rates per AWS A5.32 guidance and manufacturer recommendations:**[^1] [^2]

| Application | Typical flow rate (CFH) | Typical flow rate (L/min) |
|---|---|---|
| GMAW short-circuit (75/25 Ar/CO₂) | 25–35 CFH | 11.8–16.5 L/min |
| GMAW spray (90/10 Ar/CO₂) | 35–45 CFH | 16.5–21.2 L/min |
| FCAW gas-shielded (CO₂ or 75/25) | 35–50 CFH | 16.5–23.6 L/min |
| GTAW (100% Ar, stainless/steel) | 15–25 CFH | 7.1–11.8 L/min |
| Aluminum GMAW (100% Ar) | 25–35 CFH | 11.8–16.5 L/min |

**Note:** Higher flow rates are not always better. Excessive flow creates turbulence that actually draws in atmospheric air, contaminating the shield. Match flow rate to nozzle size and application. Check your WPS for the specified flow rate — these are typical industry ranges, not universal values.[^2]

**Why flow rate too low causes porosity:**
- Insufficient gas coverage allows O₂ and N₂ to reach the arc and weld pool
- Result: porosity (especially elongated/piping porosity from nitrogen)

**Why flow rate too high causes porosity:**
- Turbulent gas flow creates Venturi-effect entrainment of atmospheric air
- Result: same symptom (porosity) from the opposite cause — a common diagnostic trap

---

## Shielding gas supply systems

### Cylinder types and markings

**High-pressure cylinders (typical for Ar, Ar/CO₂ pre-mix, CO₂, and He):**[^5]
- Steel cylinders, typically painted according to gas type
- Pressurized to approximately 6,000–6,500 kPa (870–945 psi) for Ar and Ar mixtures when full
- CO₂ cylinders are stored as liquid — pressure varies significantly with temperature (approximately 5,800 kPa / 840 psi at 21°C for liquid CO₂)

**Cylinder valve types:**
- CGA 580 fitting (North American standard for inert gases — Argon, Helium, mixed inert/CO₂)
- CGA 320 fitting (CO₂ cylinders — liquid service, different thread)
- Never interchange fittings — the different threads are a safety feature preventing connection of the wrong gas

**Safety:**
- Store cylinders upright, chained or secured at all times — a falling cylinder that shears the valve stem becomes a rocket
- Never use a cylinder that is damaged, dented, or has a defective valve
- Never use oil or grease on cylinder valves or regulators — oxygen cylinders especially, but also inert gas regulators can be damaged by oil contamination

### Regulator and flowmeter

**Regulator:** reduces the high cylinder pressure (6,000+ kPa) to a usable working pressure (~200–700 kPa / 30–100 psi) for the flowmeter and hose.[^2]

**Flowmeter (flow gauge):**
- Ball-float type: a ball floats in a tapered tube; the gas flow rate is read at the centre of the ball at the indicated scale in CFH or L/min
- Rotameter type: similar but more precise
- The flowmeter shows **volumetric flow rate** (CFH or L/min) — not pressure

**Reading the flowmeter:**
- Set with the regulator open and the gun trigger held (simulating welding conditions — flow changes when the gun is triggered vs. at rest)
- The ball should float at the centre of the target flow rate mark
- Check for leaks at all fittings (use soapy water — never an open flame)

---

## Diagram

*(SVG to be added: `assets/diagrams/p1-s4-c-shielding-gases.svg` — two panels: (1) gas supply system diagram showing cylinder → regulator → flowmeter → hose → wire feeder → gun → nozzle → arc zone, with labels for each component; (2) four bead cross-section sketches comparing penetration profiles for 100% CO₂, 75/25 Ar/CO₂, 90/10 Ar/CO₂ (spray), and no gas (self-shielded) side by side)*

---

## Numbers you need to memorize

- **Minimum Argon for spray transfer: ~80% Ar** — 75/25 does NOT achieve spray; 90/10 does[^1]
- **75/25 Ar/CO₂: most common mild steel GMAW gas — all positions, short-circuit/globular**[^2]
- **100% CO₂: FCAW gas-shielded (C suffix electrodes); high spatter; deep penetration; no spray**[^1]
- **100% Argon: aluminum welding** — NOT used alone for steel (finger penetration)[^3]
- **Typical GMAW flow rate: 25–45 CFH (11.8–21.2 L/min)**[^2]
- **FCAW gas-shielded flow rate: 35–50 CFH (16.5–23.6 L/min)** — higher than GMAW due to larger nozzle standoff[^2]
- **CO₂ max in stainless shielding gas: ~2.5%** — excess causes sensitization[^3]
- **Self-shielded FCAW (E71T-11): NO external gas**[^4]
- **Cylinder CGA 580: Argon and inert mixes; CGA 320: CO₂**[^5]

---

## What the textbook doesn't tell you

**Shielding gas contamination is usually invisible until you have porosity.** A tiny leak in the gas hose connection allows atmospheric air to dilute the shielding gas. The weld looks identical visually until you see porosity. Check all gas fittings before welding by pressurizing with the gun trigger held and looking/listening for leaks. On cold mornings, O-ring seals in quick-connect fittings can shrink and leak — always check.

**CO₂ cylinders are liquid, not gas.** This means a few things: (1) when nearly empty, the liquid level drops and you may get gas quality variation; (2) the pressure gauge on a CO₂ cylinder tells you much less about remaining contents than on an Argon cylinder — weight is a better indicator of remaining CO₂; (3) withdrawing CO₂ too fast cools the liquid and can cause icing of the regulator/valve — this is why you may see frost on CO₂ cylinder connections at high flow rates.

**The gas nozzle distance matters for shielding effectiveness.** For gas-shielded FCAW, the WFS typically requires a longer CTWD (1–1.5 in) and the nozzle may protrude less past the contact tip than in GMAW. The result: the gas nozzle is farther from the weld pool. This is by design — the wire stickout itself provides some protection — but it does mean that even a small draft can disrupt FCAW shielding more easily than GMAW.

---

## Key terms

- **Shielding gas:** gas that surrounds the arc and weld pool to displace atmospheric O₂, N₂, and H₂O
- **Active gas:** a shielding gas (like CO₂) that participates in arc chemistry — partially dissociates and can oxidize weld metal
- **Inert gas:** a shielding gas (like Argon or Helium) that does not react chemically with the arc or weld pool
- **Spray transition:** the minimum Argon content (approximately 80%) and minimum amperage required for spray metal transfer to occur
- **75/25 Ar/CO₂:** 75% Argon, 25% CO₂ — the most common GMAW gas for mild steel; enables short-circuit transfer only
- **90/10 Ar/CO₂:** 90% Argon, 10% CO₂ — enables spray transfer; used for GMAW spray mode and MCAW
- **CFH:** cubic feet per hour — the standard unit for gas flow rate in North American industry
- **L/min:** litres per minute — the metric unit for gas flow rate
- **CGA fitting:** Compressed Gas Association standard cylinder valve fitting — CGA 580 for Argon/inert; CGA 320 for CO₂
- **Flowmeter:** device that measures volumetric flow rate of shielding gas (ball-float or rotameter type)
- **Sensitization:** in stainless steel, the precipitation of chromium carbides at grain boundaries due to excessive carbon (from CO₂) — destroys corrosion resistance in the heat-affected zone

---

## Common exam trap

- **"75/25 Ar/CO₂ can run spray transfer if you increase the voltage"** — false. 75% Argon is below the minimum Argon content for spray transfer (~80% Ar). You cannot achieve spray transfer with 75/25 regardless of voltage setting. Switch to 90/10 or higher Argon content.
- **"Use 100% Argon for mild steel GMAW"** — not recommended. 100% Argon on mild steel produces a "finger" penetration profile — narrow, deep, and prone to lack of sidewall fusion. The correct gas for mild steel GMAW is a CO₂-containing mix.
- **"Higher shielding gas flow rate always means better shielding"** — false. Excessive flow creates turbulence that entrains atmospheric air into the shielding envelope, causing porosity. Use the flow rate specified in the WPS.
- **"Self-shielded FCAW wire can be used with shielding gas if working outdoors"** — false. Adding external gas to self-shielded FCAW wire interferes with its self-shielding mechanism and degrades weld quality.

---

## Practice question preview

**Q:** A welder is setting up GMAW with ER70S-6 wire and wants to achieve spray transfer for a flat-position fillet weld on 3/8 inch mild steel plate. Which shielding gas should be selected?

A) 100% CO₂  
B) 75/25 Argon/CO₂  
C) 90/10 Argon/CO₂  
D) 100% Argon  

**Correct: C**

**Explanation:** Spray transfer requires a minimum of approximately 80% Argon in the shielding gas mix. Option A (100% CO₂) cannot achieve spray transfer — only short-circuit and globular. Option B (75/25 Ar/CO₂) has only 75% Argon — below the minimum for spray transfer. Option C (90/10 Ar/CO₂) has 90% Argon — above the threshold — and is the standard gas for GMAW spray transfer on mild steel. Option D (100% Argon) would technically support spray transfer (100% Ar > 80% Ar), but 100% Argon on mild steel produces the undesirable "finger" penetration profile and is not the standard choice for mild steel.

**Red Seal mapping:** D-14.01 (Selects FCAW, MCAW and GMAW gas, equipment and consumables — selects shielding gas appropriate to the transfer mode required)

---

[^1]: [AWS A5.32 — Specification for Welding Shielding Gases (2011)](https://www.aws.org/standards/page/aws-a532), purity classification, minimum Argon content for spray transfer (~80% Ar), CO₂ active gas characteristics, gas mixture classifications
[^2]: [Lincoln Electric — Shielding Gas Selection Guide](https://www.lincolnelectric.com/en/education-center/welding-education/shielding-gas-selection), flow rate recommendations by application (25–35 CFH for short-circuit GMAW; 35–50 CFH for FCAW), CO₂ vs Ar/CO₂ effects on penetration and spatter, 75/25 vs 90/10 selection criteria
[^3]: [ESAB — Handbook of Arc Welding](https://www.esab.com/en/us/education/blog/the-esab-handbook), Argon for aluminum (100% Ar), tri-mix for stainless (He/Ar/CO₂), CO₂ content limit for stainless (≤ 2.5% to prevent sensitization), gas chemistry effects on arc characteristics and weld bead shape
[^4]: [Miller Electric — Shielding Gas Guide](https://www.millerwelds.com/resources/article-library/mig-gmaw-welding-guide), self-shielded FCAW (no external gas), gas flow rate effects (excessive flow = turbulence = porosity), shielding gas system components (cylinder, regulator, flowmeter)
[^5]: [AIT Welder Curriculum Guide 012 (2026)](https://tradesecrets.alberta.ca/SOURCES/PDFS/CURRICULUM_GUIDES/012_OUTLINE.PDF), Period 1 Section 4 Topic C: CGA fitting types (580 for Ar/inert, 320 for CO₂), cylinder storage requirements, gas supply system identification
