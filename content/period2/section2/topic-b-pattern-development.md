---
id: p2-s2-b
period: 2
section: 2
section_title: Drafting, Drawings and Specifications
topic_letter: B
topic_title: Pattern Development
hours: 22
weight_pct: 8
outcome: >
  Upon successful completion, learners will be able to identify and describe drawing tools and methods for pattern development; perform layouts.
objectives:
  - Describe the principles of scale drawings.
  - Describe the principles of perspective, oblique and isometric drawings.
  - Describe and sketch orthographic projection.
  - Develop an orthographic drawing to scale.
  - Describe drawing tools.
  - Describe the parts of geometric shapes and angles.
  - Perform layouts.
red_seal_mapping:
  - B-7.01 (Develops templates)
  - B-7.02 (Transfers dimensions from drawings to materials)
  - A-4.02 (Interprets drawings and welding symbols)
citations:
  - source: Modern Welding (Bowditch, Goodheart-Willcox, 12th ed.)
    ref: Chapter 7 — Pattern Development; parallel line development, radial line development, triangulation, geometric construction
    url: https://www.g-w.com/modern-welding
  - source: Lincoln Electric — Sheet Metal Drafting and Pattern Development
    ref: Cylinder and cone development, offset transitions, stretchout calculation
    url: https://www.lincolnelectric.com/en/education-center/welding-education/procedure-handbook
  - source: CWB Group — Welder Certification Study Guide
    ref: Pattern development methods, layout tools, scale drawing fundamentals
    url: https://www.cwbgroup.org/education/learning-resources
  - source: AIT Welder Curriculum Guide 012 (2026), Period 2 Section 2 Topic B
    ref: pp. 37–40
    url: https://tradesecrets.alberta.ca/SOURCES/PDFS/CURRICULUM_GUIDES/012_OUTLINE.PDF
---

# Pattern Development

Pattern development is how a flat piece of metal becomes a cylinder, cone, transition, or duct. Before CNC laser cutting and CAD became universal, every duct elbow and tank nozzle was laid out by hand using geometric construction. That skill still matters — in field work, remote sites, custom fabrication, and repair — and it appears on the Red Seal exam. If you can develop a pattern from a drawing, you can build almost anything without a machine telling you how.

---

## Scale drawings: working principles

A scale drawing represents a real object at a consistent reduced (or enlarged) ratio.[^1]

**Scale notation:** written as ratio:
- **1:1** — full size (actual dimensions)
- **1:10** — 1 unit on drawing = 10 units on real object (10× reduction)
- **1:2** — half size
- **2:1** — twice actual size (used for very small parts)

**Scale ruler (architect's or engineer's rule):**
- Each face has a different scale pre-marked
- For a 1:10 scale drawing, use the 1:10 face — each graduated unit represents 10 mm of real dimension
- Never measure with a regular ruler on a scaled drawing

**Golden rule of scale drawings:** **Always use the stated dimension callouts, not scaled measurement.** Scale rules are for constructing the drawing, not for recovering dimensions from finished drawings. On shop fabrication drawings, all critical dimensions are called out with dimension lines.[^1]

---

## Types of pictorial drawings

These drawing types show objects in 3D appearance for clarity. They are *not* used for direct fabrication — they illustrate design intent.[^1]

### Perspective drawing
Objects appear as they do to the human eye — distant features are smaller. Lines converge toward one or two vanishing points on the horizon. Used in architectural renderings and presentations.

### Oblique drawing
The front face is drawn true (flat, undistorted). The third dimension (depth) is drawn at an angle — typically 30° or 45° — with depth lines drawn at a reduced scale (usually ½ true length). Quick to draw; useful for sketches.

### Isometric drawing
Three axes at 120° apart; all three dimensions drawn at the same scale and at 30° from horizontal. An isometric gives a realistic-looking 3D view without the vanishing point complications of perspective. Common in shop sketches, piping isometrics, and weld procedure illustrations.

**Isometric construction:**
1. Draw a vertical axis (height)
2. Draw two axes at 30° from horizontal (left and right)
3. Mark true dimensions along all three axes
4. Complete the outline using lines parallel to the axes

---

## Geometric shapes: definitions for layout

Before developing patterns, you need to describe the shapes precisely.[^1]

| Term | Definition |
|---|---|
| **Prism** | 3D shape with identical polygonal cross-sections (square duct, rectangular tank) |
| **Cylinder** | Circular prism — cross-section is a circle |
| **Cone** | Tapers from a circular base to a point (apex) |
| **Pyramid** | Tapers from a polygonal base to an apex |
| **Frustum** | A cone or pyramid with the apex removed by a plane cut — a truncated cone; reducer in duct |
| **Transition piece** | Changes from one cross-sectional shape to another (round-to-square, square-to-rectangle) |
| **Stretchout** | The developed flat pattern — the length of the material when the shape is "unrolled" flat |
| **Seam** | The joint where the flat pattern edges meet when the shape is formed |

---

## The three methods of pattern development

### Method 1: Parallel line development

**Used for:** Prisms and cylinders — shapes with parallel elements (all "length" lines are parallel to each other)[^1]

**The principle:** A cylinder "unrolls" into a rectangle. The width of the rectangle = the circumference of the cylinder (π × diameter). The height = the length of the cylinder.

**Step-by-step: right cylinder development**

1. **Draw the front view** and **top view (plan)** of the cylinder to scale
2. **Divide the top view circle** into equal segments (typically 12) — these are the elements
3. **Number the elements** (0 through 12, back to 0)
4. **Draw the stretchout line** horizontally below or beside the front view
5. **Transfer each element's width** along the stretchout line: total stretchout width = π × D
6. **For a mitered or angled cut at the end,** project the height of each element at the cut angle to the stretchout — connecting the points gives the true mitered profile on the flat pattern

**Example:** 150 mm diameter cylinder, cut at 45°:
- Stretchout width = π × 150 = **471.2 mm** (this is the width of the flat sheet to cut)
- The 45° cut at the end produces a sinusoidal curve on the flat pattern[^1]

### Method 2: Radial line development

**Used for:** Cones and pyramids — shapes where all elements converge to an apex point[^1]

**The principle:** A cone "unrolls" into a sector (pie slice) of a circle. The radius of the sector = the **slant height** of the cone.

**Step-by-step: right cone development**

1. **Draw front view** showing height (H) and base diameter (D)
2. **Calculate slant height (L):** L = √(H² + (D/2)²)
3. **Draw a partial circle** with radius = L (the slant height)
4. **Calculate the arc length** of the sector = circumference of cone base = π × D
5. **Step off the arc:** divide the base circle (top view) into 12 equal parts; transfer each chord length along the arc until you reach full circumference
6. **Connect arc ends to apex** — this gives the flat pattern outline
7. The flat sector is your cut-and-form template

**Example:** Cone: height 200 mm, base diameter 150 mm
- Slant height = √(200² + 75²) = √(40000 + 5625) = √45625 = **213.6 mm**
- Arc length (stretchout) = π × 150 = **471.2 mm**
- Arc angle = (arc length / slant height circumference) × 360° = (471.2 / (2π × 213.6)) × 360° = **126.2°**[^1]

### Method 3: Triangulation

**Used for:** Transition pieces that change shape — round-to-square, square-to-rectangle at different centres[^1]

**The principle:** The surface of the transition piece is divided into small triangles. The true length of each triangle's sides is found using true-length diagrams, and the triangles are assembled flat edge-to-edge to build the pattern.

**Step-by-step: round-to-square transition**

1. **Draw front view and plan view** — plan shows the square outlet centred below the round inlet (or offset)
2. **Divide the round end** into equal segments (12 is typical)
3. **Connect each segment point on the round end to the corners of the square end** — these are the triangle elements
4. **Find true lengths** using a true-length diagram:
   - In plan view: measure the horizontal distance of each element
   - In front view: measure the vertical height
   - True length = √(horizontal² + vertical²)
5. **Assemble the flat pattern** by drawing each triangle in sequence, side-sharing with the adjacent triangle
6. **Result:** The flat pattern for one of the four triangulated panels of the transition

---

## Drawing tools and their uses

| Tool | Use |
|---|---|
| **T-square** | Draws horizontal lines on a drawing board; provides reference for the 90° triangle |
| **30-60-90 triangle** | Draws lines at 30°, 60°, and 90° |
| **45-45-90 triangle** | Draws lines at 45° and 90° |
| **Compass** | Draws arcs and circles of any radius; also used to transfer distances |
| **Dividers** | Transfer equal segments; step off distances along curves |
| **Scale ruler** | Multi-scale ruler for constructing and reading scaled drawings |
| **Protractor** | Measures and constructs angles not achievable with standard triangles |
| **French curve / irregular curve** | Draws smooth curves that aren't arcs of a circle |
| **Drawing pencil** | HB for lettering, H or 2H for fine lines, B for shading |
| **Soapstone / scriber** | Mark directly on metal in the shop |

---

## Numbers you need to memorize

- **Cylinder stretchout width** = π × D (circumference)[^1]
- **Cone slant height** = √(H² + r²) where r = base radius[^1]
- **Cone arc angle (degrees)** = (base circumference / slant height circumference) × 360°[^1]
- **Number of equal divisions used on plan view:** 12 is standard for most patterns (gives good accuracy)[^1]
- **Isometric axes:** three axes at **120°** to each other; each 30° from horizontal[^1]
- **Oblique drawing depth lines:** typically at **30° or 45°**, reduced to **½ actual length**[^1]

---

## What the textbook doesn't tell you

**Triangulation is the technique that unlocks everything else.** Parallel line works for straight cylinders, radial line for cones — but real-world duct and tank work is full of offset nozzles, compound transitions, and oblique cones. Triangulation handles all of them because it reduces any surface to triangles and solves each triangle with the Pythagorean theorem. Master triangulation and you can develop any shape.

**The divide-into-12 convention is not arbitrary.** Twelve is divisible by 2, 3, 4, and 6. You can mark quarter-points, third-points, and sixth-points without fraction arithmetic. Sixteen divisions are more accurate but harder to step off without error. Twelve is the practical optimum for hand layout.

**On the shop floor, development goes on the steel directly.** A paper template is made first (trial on cardboard), checked for fit, adjusted, then transferred to plate with a soapstone or scriber. Roll the developed shape on a plate roller, check the joints, tack, then fully weld. The math has to be right before the metal is marked.

---

## Diagram

*(SVG to be added: `assets/diagrams/p2-s2-b-cylinder-development.svg` — parallel line development of a right cylinder cut with a 45° miter: front view showing the mitered cut, plan view with 12 divisions numbered, stretchout rectangle below with element heights plotted and the miter curve traced.)*

*(SVG to be added: `assets/diagrams/p2-s2-b-cone-development.svg` — radial line development of a right cone: front view with slant height labeled L, plan view with 12 divisions, flat sector with radius L and stepped-off arc equal to cone base circumference.)*

*(SVG to be added: `assets/diagrams/p2-s2-b-triangulation.svg` — triangulation of a round-to-square transition: plan view showing round inlet and square outlet with triangles drawn; true-length diagram showing how slant height is found from plan horizontal + front view vertical.)*

---

## Key terms

- **Pattern development:** geometric process of finding the flat shape that folds or rolls into a 3D object
- **Stretchout:** the total flat length of a developed pattern — the circumference of a cylinder, or arc length of a cone sector
- **Parallel line development:** method for prisms and cylinders where all elements are parallel; object "unrolls" flat
- **Radial line development:** method for cones and pyramids where elements converge at an apex; object "unrolls" into a sector
- **Triangulation:** method for transition pieces; surface divided into triangles, each solved for true length, assembled flat
- **Slant height:** the distance from the apex of a cone to the edge of its base along the surface — key dimension for cone development
- **True length:** actual length of a line element in 3D space — found using the Pythagorean theorem from plan and elevation views
- **True-length diagram:** auxiliary construction used to find the actual length of a foreshortened element
- **Frustum:** a cone with its apex removed — a truncated cone (common reducer fitting)
- **Transition piece:** fitting that changes cross-sectional shape — round-to-square, rectangle-to-rectangle of different size

---

## Common exam trap

- **Parallel line development is for CYLINDERS and PRISMS** — not cones. Exam may present a cone and ask which method applies — the answer is radial line, not parallel line.
- **Radial line development uses SLANT HEIGHT as the radius** — not the vertical height or the base diameter. Slant height = √(H² + r²).
- **Triangulation is NOT used for simple cylinders** — it's for transition pieces where elements are neither parallel nor concurrent. Using it on a cylinder is unnecessary work but not wrong; the exam may ask "most efficient method" rather than "only correct method."
- **Stretchout of a cylinder = π × D, not 2π × D** — 2π × r = π × D, they're the same thing. But be careful not to use the radius where the diameter is needed.
- **Isometric scale = full scale on all three axes** — oblique drawings reduce the depth axis to ½. Don't confuse them.

---

## Practice question preview

**Q:** A fabricator needs to develop a flat pattern for a 250 mm diameter, 400 mm long right cylinder. What is the correct stretchout (unrolled flat) width of the pattern?

A) 250 mm
B) 400 mm
C) 785 mm
D) 1257 mm

**Correct: C**

**Explanation:** The stretchout width of a cylinder equals its circumference: π × D = π × 250 = **785.4 mm** (approximately 785 mm). (A) 250 mm is just the diameter. (B) 400 mm is the length of the cylinder — the HEIGHT of the flat pattern, not the width. (D) 1257 mm would be roughly π × 400 — confusing the length for the diameter in the formula.

**Red Seal mapping:** B-7.01 (Develops templates); B-7.02 (Transfers dimensions from drawings to materials)

---

[^1]: [Modern Welding, 12th ed. (Bowditch, Goodheart-Willcox)](https://www.g-w.com/modern-welding), Chapter 7 — Pattern Development; parallel line development (cylinders), radial line development (cones), triangulation (transitions), geometric construction, scale drawings, isometric/oblique drawing types
[^2]: [Lincoln Electric — Sheet Metal Drafting and Pattern Development, Procedure Handbook](https://www.lincolnelectric.com/en/education-center/welding-education/procedure-handbook); stretchout calculation, cylinder and cone development worked examples
[^3]: [CWB Group — Welder Certification Study Guide](https://www.cwbgroup.org/education/learning-resources); pattern development methods overview, layout tools, scale drawing fundamentals
[^4]: [AIT Welder Curriculum Guide 012 (2026), Period 2 Section 2 Topic B](https://tradesecrets.alberta.ca/SOURCES/PDFS/CURRICULUM_GUIDES/012_OUTLINE.PDF), pp. 37–40
