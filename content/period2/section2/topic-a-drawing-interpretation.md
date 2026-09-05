---
id: p2-s2-a
period: 2
section: 2
section_title: Drafting, Drawings and Specifications
topic_letter: A
topic_title: Drawing Interpretation
hours: 2
weight_pct: 1
outcome: >
  Upon successful completion, learners will be able to interpret drawings.
objectives:
  - Identify the alphabet of lines.
  - Describe the purpose of drawings.
  - Identify elements and information found on drawings.
  - Interpret symbols, views and sections used on drawings.
  - Identify metric and imperial dimensioning.
red_seal_mapping:
  - A-4.01 (Uses documentation and reference material)
  - A-4.02 (Interprets drawings and welding symbols)
  - B-7.02 (Transfers dimensions from drawings to materials)
citations:
  - source: Modern Welding (Bowditch, Goodheart-Willcox, 12th ed.)
    ref: Chapter 6 — Reading Drawings and Specifications; alphabet of lines, drawing views, title blocks, dimensioning
    url: https://www.g-w.com/modern-welding
  - source: AWS A2.4 — Standard Symbols for Welding, Brazing, and Nondestructive Examination (2012)
    ref: Drawing interpretation context for welding drawings; drawing elements and symbol placement rules
    url: https://pubs.aws.org/p/1130/a24a2-4-2012-standard-symbols-for-welding-brazing-and-nondestructive-examination
  - source: CWB Group — Welder Certification Study Guide
    ref: Drawing reading for welders, views, sections, title block elements, dimensioning conventions
    url: https://www.cwbgroup.org/education/learning-resources
  - source: AIT Welder Curriculum Guide 012 (2026), Period 2 Section 2 Topic A
    ref: pp. 36–37
    url: https://tradesecrets.alberta.ca/SOURCES/PDFS/CURRICULUM_GUIDES/012_OUTLINE.PDF
---

# Drawing Interpretation

A drawing is the universal language of fabrication. Somewhere between the engineer's design intent and your welding gun is a drawing that tells you *exactly* what to build, where to cut, how to join, and what tolerances to hold. Misread a drawing and you build the wrong thing — or worse, build a right thing with a wrong joint that fails in service. Reading drawings accurately is as fundamental as striking a clean arc.

---

## Why drawings exist: the purpose hierarchy

Every drawing serves a specific purpose in the fabrication chain.[^1]

| Drawing type | Purpose |
|---|---|
| **Design drawings** | Show what the final product must be; dimensions, materials, tolerances; prepared by engineers |
| **Shop drawings / fabrication drawings** | Show how to cut, form, and assemble; prepared by drafters based on design drawings; what you actually work from |
| **Assembly drawings** | Show how parts fit together; exploded views, part numbers, bill of materials (BOM) |
| **Detail drawings** | Show individual parts or weld joints in detail; large-scale views of complex features |
| **Erection drawings** | Show how to assemble and position the structure in the field |
| **As-built drawings** | Record what was actually built, including any field changes |

---

## Title block: reading the stamp before the part

Every drawing has a **title block** — typically in the lower-right corner. Never start work without reading it.[^1][^3]

**Title block contains:**
- **Project/drawing title** — what assembly or part this describes
- **Drawing number** — unique identifier; matches the spec sheet and material list
- **Revision level (Rev)** — latest revision letter/number. ALWAYS verify you have the current revision. Building from Rev A when Rev C exists is a common shop error.
- **Scale** — the ratio of drawing size to actual size (e.g., 1:10, 1:50, or "NOT TO SCALE" — NTS)
- **Materials** — base metal specification (A36, A572-50, stainless grade, etc.)
- **Finish requirements** — surface treatment, paint, galvanizing
- **Drawing standards** — indicates whether the drawing uses first-angle or third-angle projection (see below)
- **Drafter and approver names + dates**
- **Units** — metric (mm) or imperial (inches + fractions, or decimal inches)

**When in doubt, ask.** If the title block is unclear or the revision is uncertain, get clarification before cutting steel.

---

## The alphabet of lines

Lines are the vocabulary of a drawing. Different line types have specific meanings that are standardized.[^1]

| Line type | Appearance | Meaning |
|---|---|---|
| **Visible/object line** | Thick solid | Edges and surfaces you can see from this view |
| **Hidden line** | Thin dashed (- - - - ) | Edges hidden behind other surfaces in this view |
| **Centre line** | Thin, alternating long/short dashes (–·–·–) | Axis of symmetry; centre of holes, arcs, or rotation |
| **Dimension line** | Thin with arrowheads at ends | Shows the extent of a dimension |
| **Extension line** | Thin solid, from object to dimension line | Projects the dimension outward from the object |
| **Leader line** | Thin line with arrowhead at one end | Points from a note or symbol to the part it describes |
| **Section cutting plane line** | Thick, alternating long dash/short dashes | Shows where a section view is "cut" — arrows show viewing direction |
| **Section line / hatch** | Thin parallel diagonal lines in cut area | Indicates solid material in a section view |
| **Break line** | Jagged or wavy line | Indicates a portion of the drawing is omitted (long parts shortened) |
| **Phantom line** | Thin, alternating long/two-short dashes | Shows alternative positions, adjacent parts, or moved positions |

---

## Projection systems: first-angle vs third-angle

This is where fabricators from different countries get confused.[^1]

### Third-angle projection (used in North America)
- The projection plane sits **between the viewer and the object**
- The view you see on the right side of the front view = the object as seen from the **right**
- The view below the front view = the object as seen from **below** (bottom)
- **Symbol:** circle with a cone drawn to the LEFT of the circle tip (the cone tapers toward you)

### First-angle projection (used in Europe/ISO)
- The object sits **between the viewer and the projection plane**
- The view on the RIGHT of the front view = what you see when looking from the **LEFT** (opposite to 3rd angle!)
- **Symbol:** circle with a cone drawn to the RIGHT of the circle tip

**Why this matters:** If you use a first-angle drawing thinking it's third-angle, every auxiliary view will be on the wrong side. You'll mirror-image the part. Identify the projection symbol in the title block before interpreting views.

---

## The six standard views (orthographic projection)

An object can be described by up to six views: front, rear, top, bottom, left side, and right side.[^1]

**For most shop work, 3 views are sufficient:** front, top (plan), right side.

**Selecting the front view:** By convention, the front view is chosen to show the most descriptive face of the object — the face with the most features.

**Fold-out method (think of unfolding a box):** Imagine the object inside a glass box. Each face of the box receives one view. Unfold the box flat → the views are in their correct relative positions.

---

## Section views

A section view shows the interior of a part by imagining it "cut" along a section cutting plane.[^1]

**Full section:** Entire part cut through; interior fully revealed
**Half section:** Part cut through only half; one half shows exterior, one half shows interior (used on symmetrical parts)
**Detail section (broken-out section):** Small local cut to show a specific feature
**Revolved section:** Cross-section of a bar or structural shape rotated 90° into the view

**Reading a section view:**
1. Find the cutting plane line on the view that was "cut"
2. The arrows on the cutting plane line show the viewing direction
3. Find the corresponding section view (labeled A-A, B-B, etc.)
4. Hatching (diagonal lines) shows solid cut material

---

## Dimensioning: metric vs imperial

All dimensions on a drawing must be respected exactly — do not substitute approximate equivalents.[^1][^3]

### Metric (SI)
- Linear dimensions in **millimetres (mm)** — no suffix needed (implied)
- "3 500" = 3500 mm = 3.5 m (the space replaces commas in metric notation)
- Tolerances: ±0.5, ±1, ±3 mm depending on class of fit

### Imperial
- Linear dimensions in **inches** (fractions or decimals) or **feet-and-inches** (ft-in)
- 3/8" = three-eighths of an inch; 1'-6" = one foot six inches
- Tolerances: ±1/16", ±1/32", or ±0.010" (decimal) depending on precision required

### Dual dimensioning
Some drawings show both metric and imperial — confirm which is the primary system. Typically metric is in brackets: 1.500 [38.1].

**Never convert in your head and fabricate from the converted number.** Convert once, write it down, double-check, then fabricate.

---

## Geometric Dimensioning and Tolerancing (GD&T) — awareness level

Advanced drawings may use GD&T symbols to specify tolerances beyond ±X linear. For Period 2 awareness:[^1]

| Symbol | Meaning |
|---|---|
| ⌀ | Diameter |
| □ | Square |
| ○ | Circularity (roundness) |
| ▱ | Flatness |
| ⊙ | True position |
| // | Parallelism |
| ⊥ | Perpendicularity |

If you see a GD&T callout you don't recognize, consult with your engineer or supervisor before fabricating.

---

## Numbers you need to memorize

- **Third-angle projection:** standard in North America[^1]
- **First-angle projection:** standard in Europe/ISO[^1]
- **Identify projection type** from the title block before interpreting views — every time[^1]
- **"NTS" (Not To Scale):** never measure off the drawing — use only the stated dimensions[^1]
- **Revision letter must match** the revision specified in the work order or contract — always check[^1]
- **Metric linear dimensions on drawings:** in mm, no suffix[^1]
- **Hidden lines = dashed; centre lines = alternating long-short dash**[^1]

---

## What the textbook doesn't tell you

**Working from the wrong revision is the most common drawing error in fabrication shops.** A shop has 20 people. Two of them check that their drawing is the current revision before cutting. The rest assume their drawing is current because they grabbed it from the shelf. When Rev C gets issued and replaces Rev B, if the shop doesn't have a system for pulling and replacing drawings, Rev B copies float around for weeks. Build a discipline: **every morning, check your drawing revision against the controlled document list.**

**Section views are often the only way to understand a complex weld joint.** If a drawing shows a nozzle-to-shell connection on a pressure vessel, the plan and elevation views are useless for understanding the joint geometry. Find the section view. The section will show you exactly what the bevel looks like, the included angle, whether there's a backing ring, and what weld symbol applies.

**Leader lines with arrows vs leader lines with dots:** an arrowhead touches the *line* of the object it refers to; a filled dot touches the *surface* (face) it refers to. This distinction matters when reading surface finish callouts on machined parts that interface with your welds.

---

## Diagram

*(SVG to be added: `assets/diagrams/p2-s2-a-alphabet-of-lines.svg` — visual legend showing 8 line types with their correct visual appearance and names labeled)*

*(SVG to be added: `assets/diagrams/p2-s2-a-projection.svg` — side-by-side comparison of first-angle vs third-angle projection symbols and view layouts for the same simple block)*

---

## Key terms

- **Orthographic projection:** method of representing 3D objects on a 2D surface using parallel projection lines perpendicular to the drawing plane
- **Third-angle projection:** North American standard; view placed on same side as viewing direction
- **First-angle projection:** European/ISO standard; view placed on opposite side from viewing direction
- **Title block:** standardized information box on every drawing — contains drawing number, revision, scale, materials, drafter
- **Revision (Rev):** version letter or number; always confirm you have the current revision before fabricating
- **Section view:** view showing interior features by imagining the part cut along a defined plane
- **Section cutting plane line:** heavy line with arrows showing where and from which direction a section is taken
- **Hatching:** diagonal parallel lines in a section view indicating solid cut material
- **Alphabet of lines:** standardized set of line types (object, hidden, centre, dimension, extension, leader, cutting plane, break, phantom) used in engineering drawings
- **Bill of Materials (BOM):** list of all parts and materials, with quantities, that appear on an assembly drawing
- **GD&T:** Geometric Dimensioning and Tolerancing — advanced system for specifying shape and position tolerances

---

## Common exam trap

- **First-angle projection views are on the OPPOSITE side from what you'd expect using third-angle** — this is the most commonly missed question on drawing interpretation. If a drawing is first-angle and you use third-angle logic, every side view is mirrored.
- **Scale "NTS" means DO NOT measure the drawing** — exam distractors often suggest that a 1:50 scale allows measurement with a ruler and calculator. NTS drawings have no reliable geometric relationship between drawn size and real size.
- **Revision must be checked EVERY TIME** — not just when you receive a new drawing. Drawings get revised while a job is in progress.
- **Hidden lines show edges you CANNOT see in that view** — not edges that are unimportant. All hidden edges of a real object appear as hidden lines. If you see a dashed line, ask yourself: what feature is back there?
- **Centre lines are NOT object edges** — they mark centres and axes. Running a saw cut along a centre line cuts through the middle of a hole, not at an edge.

---

## Practice question preview

**Q:** A welder receives a drawing with the notation "NTS" below the scale box. The drawing shows a bracket that appears to measure 75 mm when held against a scale ruler at 1:1. What dimension should the welder use?

A) 75 mm — read directly from the scale
B) The dimension stated in the numbered dimension callout on the drawing only
C) The dimension from the previous revision, corrected for the known scale
D) Ask the engineer to redraw the part to scale

**Correct: B**

**Explanation:** "NTS" (Not To Scale) means the drawing's geometry does not reliably represent true proportions. The ONLY reliable dimensions are those explicitly labeled on the drawing with dimension lines and numbers. Measuring the drawing with a ruler is invalid — the drawing may have been distorted, cropped, or reproduced in a different format. Always fabricate from stated dimensions, never from scaled measurements.

**Red Seal mapping:** A-4.02 (Interprets drawings and welding symbols)

---

[^1]: [Modern Welding, 12th ed. (Bowditch, Goodheart-Willcox)](https://www.g-w.com/modern-welding), Chapter 6 — Reading Drawings and Specifications; alphabet of lines, orthographic projection (first- and third-angle), views, sections, title block, dimensioning conventions
[^2]: [AWS A2.4:2012 — Standard Symbols for Welding, Brazing, and Nondestructive Examination](https://pubs.aws.org/p/1130/a24a2-4-2012-standard-symbols-for-welding-brazing-and-nondestructive-examination); context for welding symbols within the drawing framework
[^3]: [CWB Group — Welder Certification Study Guide](https://www.cwbgroup.org/education/learning-resources); drawing reading for welders, title block elements, revision control, metric and imperial dimensioning
[^4]: [AIT Welder Curriculum Guide 012 (2026), Period 2 Section 2 Topic A](https://tradesecrets.alberta.ca/SOURCES/PDFS/CURRICULUM_GUIDES/012_OUTLINE.PDF), pp. 36–37
