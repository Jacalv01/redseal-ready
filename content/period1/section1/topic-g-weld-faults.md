---
id: p1-s1-g
period: 1
section: 1
section_title: Foundational Skills, Safety and Procedures
topic_letter: G
topic_title: Weld Faults
hours: 4
weight_pct: 2
outcome: >
  Upon successful completion, learners will be able to define classifications of weld
  faults, identify weld faults, their causes, and methods of prevention.
objectives:
  - Define the classifications of weld faults.
  - Identify weld faults, their causes and methods of prevention.
red_seal_mapping:
  - A-5.01 (Inspects welds)
  - B-8.03 (Monitors and adjusts welding parameters)
citations:
  - source: CSA W59 — Welded Steel Construction (2018)
    ref: Clause 5 (workmanship, weld quality) — weld discontinuity acceptance criteria
    url: https://www.csagroup.org/store/product/CSA%20W59%3A18/
  - source: CWB Group — Weld Defects and Discontinuities (public knowledge base)
    ref: Visual weld defect identification and root cause guide
    url: https://www.cwbgroup.org/association/education
  - source: Modern Welding (Bowditch, Goodheart-Willcox, latest edition)
    ref: Chapter 22 (Weld Quality — discontinuities, defects, testing methods)
    url: https://www.goodheartwillcox.com/products/modern-welding
  - source: TWI Global — Weld Defects and How to Avoid Them (public knowledge base)
    ref: Articles on porosity, cracking, undercut, incomplete fusion, distortion
    url: https://www.twi-global.com/technical-knowledge/job-knowledge/weld-defects-prevention
  - source: Lincoln Electric — The Procedure Handbook of Arc Welding (public)
    ref: Section 5 (weld quality and inspection — discontinuity classifications)
    url: https://www.lincolnelectric.com/en/education-center/welding-education/procedure-handbook
  - source: AIT Welder Curriculum Guide 012 (2026), Period 1 Section 1 Topic G
    ref: pp. 33–36
    url: https://tradesecrets.alberta.ca/SOURCES/PDFS/CURRICULUM_GUIDES/012_OUTLINE.PDF
---

# Weld Faults

A weld that looks good isn't necessarily a good weld. A weld that passes visual inspection isn't necessarily code-compliant. Understanding weld faults is about understanding what failure looks like before the structure it's holding up shows you.

---

## Discontinuity vs. defect — the critical distinction

Before classifying faults, get the vocabulary right:[^3]

- **Discontinuity:** any interruption in the physical consistency of a weld or base metal — deviation from ideal geometry, composition, or continuity. A discontinuity is a **neutral term** — it does not by itself mean the weld is rejected.
- **Defect:** a discontinuity that **exceeds the acceptance limits** of the applicable standard (e.g., CSA W59, AWS D1.1). A defect requires repair or replacement. Not every discontinuity is a defect.

**This distinction matters on exams and on the job.** If a quality inspector calls something a "discontinuity," they haven't rejected the weld yet. If they call it a "defect," it's rejected. The acceptance criteria in the code determine which is which.

---

## Classification of weld faults

Weld faults fall into six major categories:[^3] [^4]

### 1. Dimensional faults

Faults related to weld geometry rather than internal soundness:

| Fault | Description | Cause | Prevention |
|---|---|---|---|
| **Undersized weld** | Weld is smaller than specified (leg, throat, or width) | Travel speed too fast, current too low | Match WPS parameters, measure weld size |
| **Oversized weld** | Weld is larger than required — wastes filler, can cause distortion | Travel speed too slow | Adjust speed; check periodically with fillet gauge |
| **Unequal leg length** (fillet) | One leg longer than the other | Torch/electrode angle not 45° for equal-leg fillet | Maintain consistent work angle throughout the pass |
| **Improper profile** | Convex bead (too "tall"), concave bead (too flat/hollow) | Current, speed, electrode angle errors | See below on convexity and concavity |
| **Overlap/cold lap** | Weld metal rolls over the toe of the weld without fusing to the base metal | Current too low, travel too slow | Maintain adequate current and travel speed |

**Convexity and concavity (fillet welds):**
- **Convexity** (weld is too "peaked"): reduces the effective throat; stress concentrates at the steep toe; can be code-rejected for excessive convexity. Generally: max convexity = 1 + (weld size/10) per CSA W59.[^1]
- **Concavity** (weld is "hollowed"): reduces throat below the specified minimum — a structural deficiency. A concave fillet weld has less load-carrying capacity than it appears to have.

### 2. Porosity

Gas trapped in solidifying weld metal, creating spherical or elongated voids.

**Types:**
- **Uniformly distributed porosity:** small pores spread throughout the weld (contamination throughout)
- **Clustered porosity:** pores grouped in one area (localized contamination at start/stop)
- **Piping porosity (wormhole):** elongated tubular void aligned with the solidification direction — often caused by nitrogen or water contamination
- **Surface porosity:** visible pore opening at the surface[^2]

**Causes:**
- Contamination: moisture, oil, grease, rust, mill scale, paint, zinc coating on the base metal or electrode
- Moisture in electrode coating (SMAW) — E7018 LH electrodes are highly hygroscopic; must be stored in an oven (usually 120–150°C) and used within 4 hours of removal from the oven
- Shielding gas problems (GMAW/FCAW): gas contamination, inadequate flow rate, drafts disturbing the shielding gas envelope
- Too long an arc length (excessive arc length allows atmospheric contamination)
- Sulfur in the base metal (causes elongated porosity)

**Prevention:**
- Clean the base metal before welding: degrease, wire brush rust and mill scale, grind off coatings
- Store low-hydrogen electrodes correctly and use within oven-release time limits
- Check shielding gas flow and coverage; eliminate drafts
- Maintain correct arc length (SMAW: roughly equal to electrode diameter)

**Code significance:** CSA W59 limits porosity by size, frequency, and cluster size. Piping porosity is generally a defect regardless of size.[^1]

### 3. Incomplete fusion (lack of fusion)

The weld metal fails to fuse with the base metal or with a previous weld pass. It's a planar defect — thin and crack-like — making it more dangerous than porosity of the same size, because it has a sharp root that concentrates stress.[^2] [^4]

**Types:**
- **Sidewall fusion (fusion with groove faces):** the weld doesn't bond to the groove wall
- **Interbead fusion (interpass):** the new pass doesn't fuse to the previous pass surface
- **Root fusion:** the root pass doesn't penetrate to the root of the joint

**Causes:**
- Current too low (not enough heat to melt the groove face)
- Travel speed too fast (weld pool moves before fusion occurs)
- Incorrect electrode or torch angle (not directed at the fusion zone)
- Excessive joint bevels that are too wide for the arc to bridge
- Interpass temperature too low (joint is chilled between passes)
- Slag not fully removed between passes (SMAW)

**Prevention:**
- Use the correct WPS amperage — don't undercut on current
- Clean each pass before depositing the next
- Direct the electrode at the fusion zone (joint walls), not just the weld pool centre
- Preheat when required by code or WPS (reduces chilling of the fusion zone)

### 4. Cracks

The most serious category of weld defect. Cracks are planar, sharp-rooted discontinuities that propagate under stress. A crack in a structural weld is almost always a reject — they do not "stay put" under load.[^4]

**Types by location:**

| Crack type | Location | Primary cause |
|---|---|---|
| **Centreline (longitudinal)** | Along the weld centreline | High sulfur or phosphorus in base metal; weld bead too convex; insufficient fill at the end of a pass |
| **Transverse** | Across the weld | Hydrogen-induced cracking (cold cracking) in high-restraint joints |
| **Toe crack** | At the toe of the weld (fusion line) | Stress concentration + hydrogen (HAZ cracking) |
| **Root crack** | At the weld root | Incomplete root penetration + hydrogen + restraint |
| **Crater crack** | At the end of a pass (in the crater) | Shrinkage during solidification — the molten crater shrinks inward |
| **Heat-affected zone (HAZ) crack** | In the base metal adjacent to the weld | Hydrogen-induced cracking; base metal hardenability |

**Cold cracking vs hot cracking:**

- **Hot cracking (solidification cracking):** occurs while the weld is still at high temperature, during solidification. Cause: low-melting-point impurities (sulfur, phosphorus) that segregate to grain boundaries during cooling, then crack as the weld contracts. Prevention: low-sulfur/phosphorus base metal and filler; avoid excessively convex beads; high-Cr-Ni stainless can be prone to hot cracking (control ferrite content).

- **Cold cracking (hydrogen-induced cracking / HAC):** occurs after the weld has cooled, sometimes hours to days later. Requires three conditions simultaneously: hydrogen in the weld, a susceptible microstructure (hard martensite), and stress. Prevention: use low-hydrogen electrodes (E7018); preheat to slow cooling rate; control interpass temperature; post-weld heat treatment (PWHT) when required by code.[^2]

**Crater cracks:** fill the crater before breaking the arc — strike back into the molten weld pool rather than simply pulling away. Most welders call this "filling the crater."

## Diagram
*(SVG to be added: `assets/diagrams/p1-s1-g-weld-faults.svg` — cross-section views of a fillet weld and groove weld, with labeled callouts showing: undercut, overlap, porosity (spherical voids), incomplete fusion at sidewall, toe crack, root crack, and crater crack location at weld end)*

### 5. Undercut

A groove melted into the base metal at the toe of the weld, not filled by weld metal. Undercut reduces the effective throat of the weld and creates a stress concentration at the notch.[^2]

**Causes:**
- Current too high (excessive melt-back at the toe)
- Electrode/torch angle directed too steeply toward the base metal
- Travel speed too fast (molten metal removed before it can refill)
- Electrode too large for the joint

**Prevention:**
- Reduce current
- Adjust work angle to direct arc toward the weld pool centre
- Reduce travel speed slightly
- Use the correct electrode diameter

**Code significance (CSA W59):**[^1]
- Undercut is acceptable up to **0.5 mm depth** for most static load applications
- For cyclically loaded (fatigue) structures: undercut must be zero — flush with the base metal

### 6. Incomplete joint penetration (insufficient penetration)

The weld does not extend to the required depth in the joint — typically a problem in groove welds where full-penetration welds are called for.[^2]

**Not to be confused with partial joint penetration (PJP)** — PJP joints are *designed* to have a specific unfused depth; insufficient penetration in a PJP joint means the actual penetration is less than specified.

**Causes:**
- Joint too narrow (insufficient root opening)
- Current too low
- Travel speed too fast
- Electrode too large to access the root
- Improper joint preparation (root face too thick)

**Prevention:**
- Verify joint preparation dimensions before welding (root opening, root face, bevel angle)
- Use correct process parameters per WPS
- Use a smaller diameter electrode for the root pass in narrow groove welds

---

## Additional faults — surface and profile

### Spatter

Expelled droplets of metal that solidify on the base metal surface. Not a structural defect, but:[^3]

- Excessive spatter can mask surface cracks (NDT interference)
- Spatter on painted surfaces causes coating adhesion failure
- Spatter in threaded holes or bearing bores is a manufacturing problem

**Causes:** arc length too long; current too high; wrong polarity; wet or contaminated electrodes (SMAW).

### Arc strike (arc burn)

An inadvertent arc struck on the base metal outside the weld zone. Creates a small heat-affected zone that can introduce hardening and hydrogen cracking, especially in high-strength steels.[^1]

**CSA W59 and most structural codes require arc strikes to be ground smooth** and the area inspected (visually or by MT/PT). On pressure vessels (CSA B51), arc strikes outside weld zones may require full removal and repair.

### Distortion

Weld shrinkage — as weld metal cools, it contracts, pulling the joint out of square. Not a defect by classification, but a quality problem that creates fit-up issues for subsequent work.[^3]

- **Angular distortion:** typical in single-sided fillet and groove welds
- **Longitudinal distortion:** bowing along the length of a welded assembly
- **Transverse distortion:** shrinkage across the joint width (pulling the plates together)

**Control:** balanced welding sequences; backstep technique; presetting (pre-bending parts against expected distortion); jigs and fixturing; thermal stress relief post-weld.

---

## Numbers you need to memorize

- **Undercut acceptance limit (static loads, CSA W59):** ≤ **0.5 mm** depth[^1]
- **Undercut acceptance limit (cyclic/fatigue loads):** **zero** (flush with base metal)[^1]
- **SMAW E7018 storage temperature:** **120–150°C** (holding oven to prevent moisture absorption)[^5]
- **Time out of oven before re-drying required:** typically **4 hours** for E7018 per manufacturer guidelines[^5]
- **Cold cracking (HAC) triangle:** hydrogen + susceptible microstructure + stress — all three must be present[^2]
- **Hot cracking cause:** low-melting impurities (sulfur, phosphorus) segregating at grain boundaries during solidification[^4]
- **Porosity — piping porosity:** elongated tubular void, generally a defect regardless of size[^1]
- **Discontinuity vs. defect:** a discontinuity is not automatically a defect — the applicable code acceptance criteria determine rejection

---

## What the textbook doesn't tell you

**Cold cracking can appear days after welding.** This is the most dangerous thing about hydrogen-induced cracking — the weld passes visual inspection at the end of shift, then a crack propagates 36 hours later when the temperature stabilizes. High-restraint joints (thick plate, fully restrained frames) welded without proper preheat using non-low-hydrogen consumables are the common failure scenario. This is exactly why E7018 electrodes exist and why WPS preheat requirements are not optional.[^2]

**Arc strikes on high-strength steel are code failures.** An apprentice who strikes an arc on the base metal of a high-strength steel structure (A514, T-1, HSLA) and tries to "grind it smooth" without notifying the QC inspector is creating a hidden time bomb — the arc strike creates a small brittle martensite zone that can propagate a crack under service loading. Report it, inspect it, and grind only after the inspector assesses it.[^1]

**The "porosity feels fine, let's keep going" instinct is wrong.** Surface porosity is visible; subsurface porosity is not. If you see surface porosity, assume there is more below the surface. The cause (moisture, contamination, shielding gas) is still present — fix the root cause before continuing.[^4]

**Overlap (cold lap) is a fusion problem, not just an appearance problem.** Overlap looks like extra weld metal — it can look like a good, heavy bead to an untrained eye. But the weld metal has rolled over the base without bonding to it — zero fusion at the toe. It's effectively an unfused notch. A welder who adds extra passes to "fill out" a cold joint without fixing the heat input and travel speed is making it worse, not better.[^3]

---

## Key terms

- **Discontinuity:** any interruption in the theoretical ideal structure of a weld — neutral term, not a rejection
- **Defect:** a discontinuity that exceeds code acceptance limits — a rejection
- **Porosity:** gas-trapped voids within weld metal
- **Piping porosity:** elongated tubular void — more serious classification than spherical porosity
- **Incomplete fusion (IF):** weld metal that does not bond to base metal or previous passes — planar, crack-like
- **Incomplete joint penetration (IJP):** weld that does not reach required depth in a groove weld
- **Undercut:** groove melted into the base metal at the weld toe, unfilled by weld metal
- **Overlap (cold lap):** weld metal that rolls over the base metal without fusing
- **Cold cracking (HAC — hydrogen-assisted cracking):** delayed cracking after cooling, requires hydrogen + susceptible microstructure + stress
- **Hot cracking:** solidification cracking at high temperature — sulfur/phosphorus segregation at grain boundaries
- **Crater crack:** solidification crack at the termination point of a weld pass
- **Arc strike:** inadvertent arc contact on base metal outside the weld zone
- **HAZ (Heat-Affected Zone):** base metal adjacent to the weld that has been altered by welding heat without being melted

---

## Common exam trap

- **Discontinuity vs defect:** "All undercut is a defect" is false — undercut up to 0.5 mm depth is acceptable under CSA W59 for static loads. Only undercut exceeding the code limit becomes a defect.
- **Cold cracking timing:** "Cold cracking appears immediately after welding" is false — it can appear hours to days later. A weld that passed visual inspection at day's end can crack overnight.
- **Porosity cause — wet electrodes:** distractors often blame "wrong polarity" or "arc length too long" for porosity when the actual cause is moisture in the electrode coating. For SMAW E7018, moisture is the primary porosity cause.
- **Overlap appearance:** overlap looks like extra weld metal and is sometimes mistaken as a quality weld. The key visual: the toe of the bead rolls over without forming a clean fusion line with the base metal — the transition is rounded, not crisp.
- **Undercut in cyclic structures:** the standard 0.5 mm allowance does NOT apply to structures under cyclic (fatigue) loading. For fatigue-critical joints, undercut must be zero.
- **Crater cracks:** caused by shrinkage during solidification at the weld termination. Prevention = filling the crater before breaking the arc. Distractors may say "current too high" — that causes hot cracking in the bead body, not specifically crater cracks.

---

## Practice question preview

**Q:** A visual inspection reveals a weld with undercut at the toe measuring 0.8 mm deep on a structural fillet weld in a statically loaded steel connection governed by CSA W59. The welder proposes to weld over the undercut to fill it. What is the correct course of action?

A) The undercut is acceptable — 0.8 mm is within the general CSA W59 tolerance  
B) The undercut exceeds the 0.5 mm limit for static loads and must be repaired by grinding the undercut smooth and rewelding if needed  
C) The undercut must be reported to the engineer of record, who has sole authority to accept or reject  
D) Welding over the undercut is an approved repair method for undercut less than 1 mm deep  

**Correct: B**

**Explanation:** CSA W59 sets the acceptance limit for undercut at **0.5 mm depth** for statically loaded connections. At 0.8 mm, this undercut exceeds the code limit and is classified as a defect — it must be repaired. The repair method for undercut is typically to grind the notch smooth and deposit a cover pass (a repair weld) that achieves full fusion at the toe — simply grinding may reduce the weld size below the specified minimum, so rewelding is often required. Option A is wrong because 0.8 mm exceeds 0.5 mm. Option C incorrectly suggests the engineer decides acceptance — CSA W59 sets the acceptance criteria; the engineer approves departure from them only for specific engineering judgments. Option D is incorrect — welding directly over unfused undercut without repair preparation traps the notch.

**Red Seal mapping:** A-5.01 (Inspects welds — identifies and classifies weld discontinuities and defects against applicable standard acceptance criteria)

---

[^1]: [CSA W59 — Welded Steel Construction (2018)](https://www.csagroup.org/store/product/CSA%20W59%3A18/), Clause 5 "Workmanship": undercut limits (5.6 — ≤ 0.5 mm static, zero for fatigue), porosity acceptance (5.7), arc strike repair requirements, discontinuity definition
[^2]: [TWI Global — Weld Defects and How to Avoid Them](https://www.twi-global.com/technical-knowledge/job-knowledge/weld-defects-prevention), articles on: porosity root causes, incomplete fusion mechanisms, cold cracking (HAC) — hydrogen triangle, hot cracking and solidification cracking, undercut causes and prevention, incomplete joint penetration
[^3]: [Modern Welding (Bowditch, Goodheart-Willcox)](https://www.goodheartwillcox.com/products/modern-welding), Chapter 22 "Weld Quality": discontinuity vs defect distinction, dimensional faults (undersized, oversized, unequal leg), convexity/concavity, overlap definition, distortion types and control
[^4]: [Lincoln Electric — The Procedure Handbook of Arc Welding](https://www.lincolnelectric.com/en/education-center/welding-education/procedure-handbook), Section 5 "Weld Quality": hot cracking mechanism (sulfur/phosphorus segregation), crack classification by location, porosity types including piping porosity
[^5]: [Lincoln Electric — Welding Consumables Guide — Low-Hydrogen Electrodes](https://www.lincolnelectric.com/en/products/consumables/smaw), E7018 storage requirements (120–150°C holding oven), 4-hour atmospheric exposure limit before re-drying; [Miller Electric — Stick Welding Guide](https://www.millerwelds.com/resources/article-library)
