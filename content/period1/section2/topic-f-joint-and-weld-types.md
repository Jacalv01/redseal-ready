---
id: p1-s2-f
period: 1
section: 2
section_title: Drafting, Drawings and Specifications
topic_letter: F
topic_title: Joint and Weld Types
hours: 4
weight_pct: 2
outcome: >
  Upon successful completion, learners will be able to identify joint and weld types;
  describe weld dimensions and variations.
objectives:
  - Identify the five basic joints.
  - Describe the types of welds and their dimensions.
  - Identify joint and weld type variations.
red_seal_mapping:
  - B-8.01 (Prepares materials)
  - B-8.02 (Fits components for welding)
  - D-13.04 (Performs weld using SMAW equipment)
  - D-14.04 (Performs weld using FCAW, MCAW and GMAW equipment)
citations:
  - source: AWS A3.0 — Standard Welding Terms and Definitions (2020)
    ref: Full standard — all joint type definitions, weld type definitions, fillet weld terminology (leg, throat, convexity, concavity)
    url: https://www.aws.org/standards/page/aws-a30
  - source: CSA W59 — Welded Steel Construction (2018)
    ref: Clause 4 (design of welded joints) — joint types, weld types, prequalified joint configurations
    url: https://www.csagroup.org/store/product/CSA%20W59%3A18/
  - source: Modern Welding (Bowditch, Goodheart-Willcox, latest edition)
    ref: Chapter 6 (Weld Joints and Weld Types — butt, corner, T, lap, edge; groove, fillet, plug, slot)
    url: https://www.goodheartwillcox.com/products/modern-welding
  - source: Lincoln Electric — Procedure Handbook of Arc Welding (public)
    ref: Section 2 — joint design, weld types, groove dimensions, fillet weld dimensions
    url: https://www.lincolnelectric.com/en/education-center/welding-education/procedure-handbook
  - source: AIT Welder Curriculum Guide 012 (2026), Period 1 Section 2 Topic F
    ref: pp. 81–90
    url: https://tradesecrets.alberta.ca/SOURCES/PDFS/CURRICULUM_GUIDES/012_OUTLINE.PDF
---

# Joint and Weld Types

Before you pick up an electrode, you need to know what kind of joint you're welding and what kind of weld goes in it. The wrong weld type in the wrong joint either fails structurally or costs far more filler metal than necessary. This is fundamental joint design — the starting point of every welding symbol you'll ever read.

---

## The five basic joint types

A **joint** is where two or more members come together. AWS A3.0 defines five fundamental joint types — everything in welding fabrication is a variation on these five.[^1]

### 1. Butt joint

Two members in the **same plane**, aligned end-to-end (or edge-to-edge). The joint line runs between the two members.[^1] [^3]

**Used for:** joining plate to plate, pipe to pipe end-to-end, structural beams spliced along their length.

**Variations:** square groove (thin material, no bevel), V-groove, double-V, bevel, U-groove, J-groove.

**Key characteristic:** requires groove weld. On thick plate, requires beveling to get penetration to the root. CJP butt welds carry the full design load — they must achieve full penetration.

**Where you'll see it on the job:**
- Pipe weld on a pressure line (100% butt joint — code governed by CSA B51)
- Structural beam splice plates welded to flanges and web
- Tank shell seams

---

### 2. Corner joint

Two members meet at approximately **90°**, with the joint at the corner of a box or frame. One member's end meets the face of the other member.[^1] [^3]

**Used for:** box sections, tank corners, structural frame corners, machine guards.

**Variations:** open corner (two beveled pieces form a V at the corner), closed corner (one piece laps over the other edge), half-open corner.

**Key characteristic:** can use groove or fillet welds, or a combination. The choice depends on the required strength and whether full penetration is needed.

**Where you'll see it on the job:**
- Square tubing frame corners
- Structural box columns
- Fabricated machinery guards

---

### 3. T-joint (Tee joint)

One member's **edge** meets the **face** of another member at approximately 90° — forming a T shape when viewed from the side.[^1] [^3]

**Used for:** web-to-flange connections in built-up beams (H-beams, I-beams), stiffener plates welded to plate, lug plates, pad eyes.

**Weld type:** almost always fillet welds on both sides. Where higher strength is needed, may use groove welds (requiring bevel prep on the web or stiffener edge).

**Key characteristic:** the standard T-joint fillet weld does NOT achieve full penetration into the root by default — there is always an unfused root area at the centre of a double-fillet T-joint. For full penetration in a T-joint, one or both members must be beveled (forming a groove) and the weld must be a CJP groove weld.

**Where you'll see it on the job:**
- Every web-to-flange weld in a structural beam
- Gusset plates welded to columns
- Base plates welded to columns

---

### 4. Lap joint

Two members **overlap** each other, with the weld on the overlapping surface edge.[^1] [^3]

**Used for:** thin sheet metal fabrication, repair welds, structural connections where plates must overlap for load transfer, structural angles bolted and welded (overlap portion).

**Weld type:** fillet welds on the exposed edge(s) of the overlap. Plug and slot welds through the top member to the bottom member.

**Key characteristic:** lap joints are efficient for load transfer but create a stress concentration at the lap gap (the root of the fillet weld). Not suitable for fatigue-critical joints under cyclic loading. CSA W59 specifies minimum lap lengths to ensure adequate load transfer.[^2]

**Minimum lap overlap:** per CSA W59, the overlap must be at least 5× the thickness of the thinner member (minimum 25 mm) for load-carrying lap joints.[^2]

**Where you'll see it on the job:**
- Structural base plate reinforcement plates
- Field splice connections in tanks
- Repair overlays on worn components

---

### 5. Edge joint

Two or more members with their **edges** parallel and in the same plane, joined along that edge.[^1] [^3]

**Used for:** joining thin plates side by side (sheet metal, thin flanges), seal welds on non-structural joints, flanges on light gauge enclosures.

**Weld type:** edge weld (a weld along the edges of two or more overlapping members). Not to be confused with a butt joint — in an edge joint both members' faces are in the same plane, not their ends.

**Key characteristic:** lowest strength of the five joint types. Generally used for thin gauge work or non-structural sealing applications. Not used for structural load-bearing applications.

**Where you'll see it on the job:**
- Sheet metal ductwork seams
- Non-structural flange attachment on light enclosures
- Seal welds on tank vents and non-pressure connections

---

## Summary — five basic joints

| Joint | Members relationship | Typical weld | Common application |
|---|---|---|---|
| **Butt** | Same plane, end-to-end | Groove weld (V, bevel, U, J) | Pipe welds, plate splices |
| **Corner** | 90°, end meets face | Groove or fillet | Box sections, frame corners |
| **T (Tee)** | 90°, edge meets face | Fillet (or groove for CJP) | Built-up beams, stiffeners |
| **Lap** | Overlapping, parallel | Fillet on edge; plug/slot | Overlap splices, repairs |
| **Edge** | Edge-to-edge, same plane | Edge weld | Sheet metal, seal welds |

---

## Weld types — what actually goes in the joint

A **weld type** describes the geometry of the deposited weld metal, not the joint configuration. The same joint type can have different weld types applied to it.[^1]

### Groove weld

A weld made in a groove (channel) between two members. The groove is created by beveling one or both members, or it occurs naturally at a root opening.[^1] [^4]

**Complete Joint Penetration (CJP) groove weld:** penetrates the full thickness of the joint — carries the full design load. Requires full penetration to the root, verified by visual inspection of the back side or by back gouging and rewelding.

**Partial Joint Penetration (PJP) groove weld:** penetrates to a specified depth less than the full thickness. Used where full penetration is not required by the design.

**Groove weld types (named for the groove shape):**

| Type | Profile | Notes |
|---|---|---|
| Square groove | No bevel — root opening only | Thin material, limited thickness |
| V-groove | Both sides beveled symmetrically | Most common for plate in all positions |
| Bevel groove | One side only beveled | Arrow side rule applies |
| U-groove | Both sides have a radius (concave curve) | Deeper, more expensive prep; less filler |
| J-groove | One side has a radius | Requires machining; arrow side rule applies |
| Flare-V | Both members are curved (round bar) | Curved surface to curved surface |
| Flare-bevel | One curved, one flat member | Round to flat plate |

### Fillet weld

A weld of approximately triangular cross-section made at the intersection of two surfaces, typically at roughly 90° to each other.[^1]

**Fillet weld dimensions:**

| Dimension | Definition | Symbol |
|---|---|---|
| **Leg length** | Distance from the toe to the root along one face of the base metal | s or w |
| **Theoretical throat** | Perpendicular distance from the root to the face of the weld (for an equal-leg 45° fillet, = leg × 0.707) | t or T |
| **Actual throat** | Perpendicular distance from root to weld face, accounting for actual convexity or concavity | — |
| **Toe** | The point where the weld face meets the base metal surface | — |
| **Root** | The deepest point of the weld penetration | — |
| **Face** | The exposed surface of the weld | — |

**For an equal-leg fillet weld:**
Theoretical throat = leg × sin(45°) = leg × 0.707

**Example:** A 10 mm equal-leg fillet weld has a theoretical throat of 10 × 0.707 = **7.07 mm**[^1]

**Convexity:** weld face bulges outward beyond the toe-to-toe line — reduces effective throat if excessive. CSA W59 limits maximum convexity.[^2]

**Concavity:** weld face curves inward below the toe-to-toe line — reduces actual throat below the theoretical throat. A concave fillet has less load capacity than an equal-leg fillet of the same specified size.

**Reinforcement:** for groove welds, the weld metal deposited above the base metal surface — must be within code limits (typically max 3 mm above flush for CJP groove welds per CSA W59).[^2]

## Diagram

*(SVG to be added: `assets/diagrams/p1-s2-f-joint-weld-types.svg` — two panels: (1) The 5 basic joint types shown as cross-section sketches labeled butt, corner, T, lap, and edge; (2) Fillet weld cross-section with labeled toe, root, face, leg length, and theoretical throat; (3) Groove weld cross-section showing CJP V-groove with root opening, root face, groove angle, and reinforcement)*

---

### Plug and slot welds

**Plug weld:** a weld made through a circular hole drilled in one member (the top member) to fuse it to the underlying member. The hole is filled, partially or completely, with weld metal.[^1]

**Slot weld:** similar to a plug weld but the hole is elongated (a slot). Provides more weld area than a plug.

**Applications:** attaching thin plate overlays where edge fillet welds alone aren't sufficient, connecting deck plates to beams.

### Spot weld (arc spot)

A weld made by fusing two overlapping members at a single point by fusing through the top member without a pre-drilled hole. Made by GMAW or GTAW. Distinguished from resistance spot welding by the process.[^1]

### Seam weld

A continuous weld along the length of a joint, as opposed to intermittent welds. Or specifically, a resistance seam weld made by passing electrodes along the joint while current flows (rollers).[^1]

### Surfacing (buildup/cladding)

Weld metal deposited on a surface to build up dimension (worn equipment restoration) or for hardfacing (wear resistance). Not a joint weld — the weld metal adds to one surface only.[^1]

---

## Joint variations — groove weld dimensions

### Root opening (R)

The distance between the root faces of the two members before welding. Provides access for the electrode to reach the root and achieve penetration.[^4]

- Too small → incomplete root penetration (burn-through risk reduced but fusion risk increased)
- Too large → burn-through risk; excess weld metal consumption; distortion

### Root face (f)

The un-beveled land at the root of a groove preparation. Provides a surface to arrest root burn-through.[^4]

- Too thick → incomplete penetration
- Too thin → melt-through / burn-through

### Groove angle (included angle)

The total angle of the groove opening — the sum of both bevel angles (or twice the bevel angle if symmetrical).[^4]

- Too small → access for electrode difficult; fusion at sidewalls inadequate
- Too large → excessive weld volume (more filler consumed); more distortion from heat input

**Typical groove angles by process:**

| Process | Typical included angle | Root opening |
|---|---|---|
| SMAW V-groove | 60° | 1/16 to 1/8 in (1.6–3.2 mm) |
| SMAW bevel groove | 45° | 1/16 to 1/8 in |
| GMAW V-groove | 60° | 0–1/8 in |
| GTAW (TIG) V-groove — pipe | 75° | 3/32 in (2.4 mm) typical |

These are typical starting points — the actual WPS governs.[^4]

---

## Numbers you need to memorize

- **Five basic joint types:** Butt, Corner, T, Lap, Edge[^1]
- **Fillet weld theoretical throat = leg × 0.707** (for equal-leg 45° fillet)[^1]
- **Minimum lap overlap (CSA W59):** at least 5× the thinner member thickness, min 25 mm[^2]
- **Maximum groove weld reinforcement (CJP, CSA W59):** typically ≤ 3 mm above flush[^2]
- **Typical SMAW V-groove included angle:** 60°[^4]
- **Fillet weld face components:** toe (where face meets base metal), root (deepest point), face (exposed surface)[^1]

---

## What the textbook doesn't tell you

**T-joint fillet welds always have an unfused root — that's by design.** The diagram showing two 45° fillet welds on a T-joint always has a triangular unfused area at the centre (where the two weld roots meet). This is not a defect — it's an inherent characteristic of the joint design. The structural design accounts for it. The ONLY way to achieve full penetration in a T-joint is to bevel the web member and make a CJP groove weld — which is expensive. For most structural T-joints, double fillet welds are entirely adequate.[^2]

**Lap joint minimum overlap is specified in code — and frequently violated on the job.** When repair welders weld a small lap patch over a corroded area, the overlap is often less than the minimum 5× thickness specified by CSA W59. If the patch is load-bearing, this is a code violation that could cause failure. Always check the minimum lap length for the material thickness.[^2]

**The difference between a bevel joint and a V-groove matters for the arrow on the symbol.** In a V-groove, both pieces are beveled — the arrow can point to either piece (they're symmetric). In a bevel groove, only ONE piece is beveled — the arrow MUST use the broken-arrow convention to identify which piece is machined. This is one of the most commonly misread welding symbols.[^1]

---

## Key terms

- **Butt joint:** two members in the same plane, end to end — groove weld joint
- **Corner joint:** two members at 90°, one member's end to the other's face
- **T-joint (tee):** one member's edge meets another's face at 90° — fillet weld joint by default
- **Lap joint:** two members overlapping — fillet weld on the exposed edge(s)
- **Edge joint:** members edge-to-edge in the same plane — edge weld, typically non-structural
- **Groove weld:** weld deposited in a groove between two members
- **Fillet weld:** triangular cross-section weld at the intersection of two surfaces (typically 90°)
- **CJP:** Complete Joint Penetration — groove weld penetrating the full thickness
- **PJP:** Partial Joint Penetration — groove weld to a specified depth only
- **Leg length:** dimension of the fillet weld along the face of each base metal member
- **Theoretical throat:** leg × 0.707 for an equal-leg fillet — the shortest distance from root to face
- **Toe:** the junction of the weld face and the base metal surface
- **Root opening:** the gap between members at the root of a groove joint
- **Root face:** the un-beveled land at the root of a groove preparation
- **Groove angle (included angle):** the total opening angle of a groove joint

---

## Common exam trap

- **"A T-joint with two fillet welds has complete joint penetration"** — false. A standard double-fillet T-joint has an inherently unfused root. CJP requires a beveled groove preparation.
- **"The theoretical throat of a 10 mm fillet weld is 10 mm"** — false. Theoretical throat = 10 × 0.707 = 7.07 mm. The leg is 10 mm; the throat is smaller.
- **"An edge joint and a butt joint are the same thing"** — false. In a butt joint, the member ends meet edge-to-edge in the same plane. In an edge joint, two members' faces are in the same plane and the edges are joined along the edge face. They look similar but are geometrically different.
- **"Lap joints are preferred for cyclic loading"** — false. Lap joints create stress concentrations at the root of the fillet weld and are generally not recommended for fatigue-critical (cyclically loaded) structures.

---

## Practice question preview

**Q:** A structural T-joint uses a 10 mm equal-leg fillet weld on both sides of the web. What is the theoretical throat of each fillet weld?

A) 10 mm  
B) 7.07 mm  
C) 14.14 mm  
D) 5.00 mm  

**Correct: B**

**Explanation:** The theoretical throat of an equal-leg fillet weld is the leg size multiplied by 0.707 (sin 45°). 10 mm × 0.707 = 7.07 mm. This is the perpendicular distance from the weld root to the hypotenuse (face) of the right isosceles triangle formed by the fillet weld cross-section. Option A (10 mm) is the leg size, not the throat. Option C (14.14 mm) doubles the leg incorrectly. Option D has no basis.

**Red Seal mapping:** B-8.02 (Fits components for welding — identifies joint types and weld dimensions to verify proper fit-up)

---

[^1]: [AWS A3.0 — Standard Welding Terms and Definitions (2020)](https://www.aws.org/standards/page/aws-a30), complete definitions: the five basic joint types (butt, corner, T, lap, edge), all weld types (groove, fillet, plug, slot, spot, seam, surfacing), fillet weld terminology (toe, root, face, leg length, theoretical throat, actual throat, convexity, concavity), groove weld dimensions (root opening, root face, groove angle)
[^2]: [CSA W59 — Welded Steel Construction (2018)](https://www.csagroup.org/store/product/CSA%20W59%3A18/), Clause 4 "Design of Welded Connections": prequalified joint dimensions, minimum lap overlap (5× thickness, min 25 mm), CJP groove weld reinforcement limits (≤ 3 mm), fillet weld convexity limits, T-joint unfused root design basis
[^3]: [Modern Welding (Bowditch, Goodheart-Willcox)](https://www.goodheartwillcox.com/products/modern-welding), Chapter 6 "Weld Joints and Weld Types": all five joint types with diagrams, weld types with cross-section illustrations, groove weld dimensions, fillet weld throat and leg terminology
[^4]: [Lincoln Electric — Procedure Handbook of Arc Welding](https://www.lincolnelectric.com/en/education-center/welding-education/procedure-handbook), Section 2 "Joint Design": groove geometry (root opening, root face, groove angle), typical groove dimensions by process (SMAW, GMAW, GTAW), CJP vs PJP groove design
