---
id: p3-s3-a
period: 3
section: 3
section_title: Drafting, Drawings and Specifications
topic_letter: A
topic_title: Structural Drawings
hours: 16
weight_pct: 6
outcome: >
  Upon successful completion, learners will be able to analyze, identify, and interpret
  structural drawings including site plans, structural shapes, bill of materials, and
  structural drawing types.
objectives:
  - Interpret abbreviations used on drawings.
  - Identify site plans, benchmarks and orientation.
  - Identify structural shapes and how they are specified.
  - Identify types of structural drawings.
  - Extract dimensions and other information from drawings.
  - Interpret bill of materials for drawings.
  - Interpret drawings.
red_seal_mapping:
  - A-4.01 (Uses documentation and reference material)
  - A-4.02 (Interprets drawings and welding symbols)
  - B-7.02 (Transfers dimensions from drawings to materials)
  - B-8.01 (Prepares materials)
citations:
  - source: CSA G40.20 / G40.21 — General Requirements for Rolled or Welded Structural Quality Steel
    ref: Steel grade designations, yield strength, impact test requirements
    url: https://www.csagroup.org/store/product/CSA%20G40%3A20/
  - source: CISC — Handbook of Steel Construction (11th edition)
    ref: Structural shape designations (W, C, L, HSS, WWF), section properties, connection details
    url: https://www.cisc-icca.ca/resources/handbook-of-steel-construction/
  - source: CSA W59 — Welded Steel Construction (2018)
    ref: Clause 5 (design), Clause 4 (workmanship), weld joint designations for structural connections
    url: https://www.csagroup.org/store/product/CSA%20W59%3A18/
  - source: Modern Welding (Bowditch et al., Goodheart-Willcox)
    ref: Chapter on blueprint reading — structural drawings, abbreviations, section views, bill of materials
    url: https://www.g-w.com/modern-welding
  - source: CWB Group — Structural Welding Inspector Training Resources
    ref: Drawing interpretation for structural welds, weld symbol reading in structural context
    url: https://www.cwbgroup.org/education
---

# Structural Drawings

Every piece of structural steel on a building, bridge, or tower begins as a line on a drawing. Your job is to take those lines and make them into real steel — with the right cuts, the right holes, and the right welds. A welder who can read structural drawings is worth twice what one who can't earns. You become a fabricator, not just a burner.

---

## Types of Structural Drawings

A structural steel project produces several interconnected drawing types, each serving a different purpose:[^4][^5]

| Drawing type | Purpose | Who uses it |
|---|---|---|
| **Architectural drawings** | Show building form, room layouts, finishes | Architects, general contractor |
| **Structural general arrangement (GA)** | Show the overall structural layout — columns, beams, grids | Structural engineers, project managers |
| **Site plan** | Plan view of the entire site — location of structures, benchmarks, north arrow | All trades |
| **Elevation drawings** | Vertical views of the structure from each face | Structural engineers, fabricators |
| **Detail drawings** | Enlarged views of specific connections, joints, or assemblies | Fabricators, welders |
| **Shop drawings (fabrication drawings)** | Fabricator's working drawings — material lists, exact dimensions for each piece | Fabricators, welders |
| **Erection drawings** | Show how prefabricated pieces are assembled on-site | Iron workers, welders (site) |
| **Spool sheets (piping)** | Isometric and bill of materials for pipe assemblies — covered in Section 3C | Pipefitters, pipe welders |

---

## Site Plans and Orientation

### Benchmark

A **benchmark** is a permanent, fixed reference point for elevation (height) on the construction site.[^4]

- Typically a brass disc set in concrete, or a permanent mark on a fixed structure
- All elevation measurements on the site are referenced to the benchmark elevation
- Benchmark elevation may be expressed as absolute elevation (metres above sea level) or as a site datum (e.g., benchmark = 100.000 m, even if the actual elevation above sea level is 694 m)

**Why welders care:** steel members and connections must be set to specific elevations relative to the benchmark. When you're working on structural connections at elevation, the engineer's detail drawing references benchmark elevation. Fabrication heights ("top of steel" elevations) are on the structural drawings.

### North arrow

Every site plan shows a **north arrow** — indicating site north. Note that site north may not be geographic north — developers sometimes rotate the grid for project convenience.[^4]

- **Column lines:** structural grids are labeled with numbers (east-west) and letters (north-south), or vice versa. Columns are named by their grid intersection (e.g., "Column B4" is at the intersection of gridline B and gridline 4).
- **Drawing orientation:** the plan view is usually shown with north toward the top of the sheet. Always check the north arrow — some drawings rotate the view.

---

## Structural Shape Designations

The CISC (Canadian Institute of Steel Construction) and CSA G40.20/G40.21 define standard structural shapes.[^1][^2]

### W-Shape (Wide Flange)

- **Designation:** W followed by nominal depth in mm × mass in kg/m. Example: **W310 × 97**
  - Nominal depth: 310 mm (actual depth may vary)
  - Mass: 97 kg per metre of length
- **Profile:** two parallel flanges connected by a web — looks like an "H" or "I" in cross-section
- **Common use:** primary structural members — beams, columns, girders
- **Previous designation:** "S" or "I" beams were older standard — W is the modern Canadian/North American standard

### C-Shape (Channel)

- **Designation:** C followed by depth in mm × mass in kg/m. Example: **C250 × 30**
- **Profile:** web with one flange on each side (U-shaped cross-section)
- **Common use:** purlins, girts, secondary framing, crane rails

### L-Shape (Angle)

- **Designation:** L followed by leg dimensions × thickness, all in mm. Example: **L127 × 89 × 12** (two legs of different size) or **L102 × 102 × 9.5** (equal legs)
- **Profile:** two flat legs at 90°
- **Common use:** bracing, connections, gussets, secondary members, clip angles

### HSS (Hollow Structural Section)

- **Designation:** HSS followed by outer dimensions × wall thickness
  - Square: **HSS 152 × 152 × 9.5**
  - Rectangular: **HSS 203 × 152 × 9.5**
  - Round: **HSS 168.3 × 9.5** (diameter × wall)
- **Profile:** square, rectangular, or round hollow tube
- **Common use:** columns, bracing, trusses, architecturally exposed structures
- **Welding note:** HSS has lower ductility than W-shapes at the corners. When fitting connections to HSS, use prequalified details from CSA W59[^3]

### WWF (Welded Wide Flange)

- **Designation:** WWF followed by depth × mass. Example: **WWF900 × 253**
- **Profile:** similar to W, but fabricated by welding three plates together (not rolled)
- **Common use:** very large beams and columns that exceed standard rolled W-shape sizes
- **Weld quality:** the flange-to-web welds are fillet or partial penetration per the fabricator's procedure — qualify under CSA W47.1

### Plate

- **Designation:** PL followed by thickness × width × length. Example: **PL25 × 300 × 1000** (25 mm thick, 300 mm wide, 1000 mm long)
- **Common use:** gusset plates, connection plates, base plates, stiffeners

---

## Grade Designations — CSA G40.21

CSA G40.21 specifies grades of structural steel most commonly used in Canadian construction:[^1]

| Grade | Min yield strength (MPa) | UTS range (MPa) | Notes |
|---|---|---|---|
| **230W** | 230 | 380–515 | Old "mild steel" equivalent — rare in new construction |
| **260W** | 260 | 410–550 | Common general structural use |
| **300W** | 300 | 450–620 | Standard for buildings and bridges |
| **350W** | 350 | 480–650 | High-strength structural — bridges, heavy fabrication |
| **350WT** | 350 | 480–650 | As 350W + Charpy impact tested at −20°C (T = tested) |
| **480W** | 480 | 590–760 | Very high strength — special applications |

The "W" suffix indicates the grade meets the requirements of CSA G40.21. The "T" suffix indicates the material has been Charpy V-notch impact tested.[^1]

---

## Common Structural Drawing Abbreviations

| Abbreviation | Meaning |
|---|---|
| **BM** | Bill of Materials (also: Benchmark in survey context) |
| **BOP** | Bottom of Plate or Bottom of Pipe |
| **BOF** | Bottom of Footing |
| **CL (or ℄)** | Centerline |
| **TOS** | Top of Steel |
| **EL or ELEV** | Elevation |
| **GL** | Grade Level |
| **FS** | Field Splice (a joint made on-site, not in shop) |
| **TP** | Top Plate |
| **BP** | Base Plate |
| **GUSS** | Gusset Plate |
| **STIFF** | Stiffener |
| **PL** | Plate |
| **SIM** | Similar (a note indicating a detail is the same as another nearby) |
| **TYP** | Typical (applies everywhere unless otherwise shown) |
| **NTS** | Not to Scale |
| **GA** | Gauge (wire size) or General Arrangement |
| **OC or @ OC** | On Centre (spacing between repetitive elements) |

---

## Bill of Materials (BOM / Material List)

Every structural drawing includes a Bill of Materials — a table listing every piece of steel required for the assembly.[^4]

### Typical BOM columns

| Column | What it contains |
|---|---|
| **Item no.** | A unique number for each piece (matches mark on the drawing) |
| **Qty (quantity)** | How many of this piece are required |
| **Description** | Shape designation (e.g., W310×97) |
| **Length** | Cut length in mm |
| **Material spec** | Grade (e.g., CSA G40.21 350W) |
| **Unit mass (kg/m)** | Mass per unit length from CISC tables |
| **Total mass (kg)** | Qty × length × kg/m |
| **Remarks** | Special instructions (e.g., "galvanize," "drill 4-22mm holes") |

### Using the BOM

1. **Verify material is on hand:** before cutting, confirm the grade and section size match what the BOM specifies
2. **Check the MTR:** the material in the yard must have a Mill Test Report confirming it meets the specified grade (see Section 2D)
3. **Calculate cut list:** some shops issue separate "cut lists" from the BOM; others expect the fabricator to generate cut lengths from the drawing dimensions
4. **Track waste:** structural fabrication generates drops (offcuts). Long drops are marked with grade and heat number and returned to stock.

---

## Interpreting Structural Details

### Section views and cutting planes

Structural drawings use section cuts to show the internal geometry of connections that can't be seen in plan or elevation:

- A **cutting plane line** (a dashed or phantom line with arrows showing direction of view) indicates where a section is cut
- The **section view** is labeled with matching letters (e.g., "Section A-A" at the bottom of the sheet, referenced by "A-A" arrows on the plan)
- Section views show the weld joint geometry, bolt size and pattern, and plate thicknesses

### Column base plates

A typical steel column base plate detail shows:[^2]

- **Base plate size:** plan dimensions (e.g., 450 × 450 × 25 PL)
- **Weld to column:** fillet or CJP groove weld at the column-to-plate connection — size, length, and type shown with weld symbols
- **Anchor bolt pattern:** bolt size, grade (e.g., ASTM F1554 Gr. 36 or Gr. 55), projection above base plate, and hole tolerances in the plate
- **Grout space:** a gap between the base plate and concrete pedestal is filled with non-shrink grout after erection

### Beam-to-column connections

Common types shown on structural details:[^2]

| Connection type | Description |
|---|---|
| **Shear tab (single plate)** | A plate welded to the column web, bolted to the beam web — simple shear connection |
| **Clip angle** | Two L-shapes welded to the column, bolted to the beam — older standard shear connection |
| **Moment connection** | Beam flanges welded to column flanges (CJP groove welds) with web shear tab — transfers both shear and moment |
| **End plate** | A plate welded to the beam end, bolted to the column — moment or shear variant |

---

## Elevation Drawings — How to Read Height Dimensions

Elevation drawings show the structure from the side (north, south, east, or west face).[^4]

- **Grid lines are vertical:** each column line is shown as a vertical dashed line
- **Elevations are horizontal:** dimensions to the bottom of steel (BOS), top of concrete (TOC), and floor levels
- **Member sizes are labeled:** the W or HSS designation is shown at each beam and column
- **Connections are called out:** bolt circles, weld symbols, and detail reference bubbles

**Reading height dimensions:** elevations are given relative to a datum (0.000 elevation or benchmark). "EL = 104.200" means 104.200 metres above the benchmark. TOS (top of steel) elevation tells you where the top flange sits — the connection detail tells you how the beam is configured relative to that elevation.

---

## Numbers you need to memorize

- **W310 × 97:** depth 310 mm, mass 97 kg/m[^2]
- **HSS designation order:** outer dimensions × wall thickness[^2]
- **L-shape designation order:** longer leg × shorter leg × thickness (all mm)[^2]
- **CSA G40.21 Grade 350W yield strength:** 350 MPa minimum[^1]
- **CSA G40.21 Grade 300W yield strength:** 300 MPa minimum[^1]
- **"T" suffix (350WT):** Charpy impact tested at −20 °C[^1]

---

## What the textbook doesn't tell you

**The shop drawing is not the structural drawing.** The engineer's structural drawing shows WHAT must be built. The shop drawing (prepared by the fabricator's drafting department) shows HOW each piece will be fabricated. If the shop drawing has an error, the fabricator is responsible — but the structural drawing governs for design. When in doubt, check the original structural drawing, not just the shop drawing.[^5]

**"TYP" on structural drawings means 'all similar locations' — verify.** If a detail shows a W250 × 49 connection with a 6 mm fillet weld and says "TYP," that weld size applies at all similar connections unless specifically noted otherwise. Read carefully — sometimes one of the ten "typical" connections is different and the drawing says "EXC AT B4" (except at B4).[^4]

**Steel sizes are nominal — actual dimensions differ slightly.** A W310 × 97 has a nominal depth of 310 mm but the actual CISC-tabulated depth is 308 mm. When setting elevations and detailing connections, use the actual tabulated dimensions from the CISC Handbook, not the nominal designation.[^2]

**Field splice locations are engineering decisions, not fabricator choices.** FS (field splice) marks on the drawing were placed by the engineer based on transportation limitations (maximum piece length), crane capacity, and connection economics. Do not move field splice locations without engineering approval.[^4]

---

## Diagram

*(SVG to be added: `assets/diagrams/p3-s3-a-structural-shapes.svg` — cross-section comparison of: W-shape, C-shape, L-shape (equal leg), HSS square, HSS round, plate — each with designation format shown)*

*(SVG to be added: `assets/diagrams/p3-s3-a-beam-column-connection.svg` — isometric view of a W-shape beam connected to a W-shape column flange using a moment connection: CJP groove weld at top and bottom flanges, shear tab at web — weld symbols and member designations labeled)*

*(SVG to be added: `assets/diagrams/p3-s3-a-grid-elevation.svg` — elevation view showing: column grid lines (A, B, C), elevation marks (EL=104.200, TOS), floor levels, member designations — a simplified two-bay, two-storey frame)*

---

## Key terms

- **Structural shape:** a standard rolled or welded steel section designated by a letter code and dimensions (W, C, L, HSS, WWF)
- **W-shape (Wide Flange):** the most common structural beam/column — designation W[depth]×[kg/m]
- **HSS (Hollow Structural Section):** square, rectangular, or round hollow tube — high torsional stiffness
- **L-shape (Angle):** two legs at 90° — used for bracing and connections
- **CSA G40.21:** Canadian standard for structural steel grades — the "W" suffix grades (230W, 260W, 300W, 350W)
- **Grade 350W:** the dominant high-strength structural steel grade — 350 MPa minimum yield
- **TOS (Top of Steel):** the elevation of the top flange of a structural beam — design reference point
- **BOM (Bill of Materials):** a complete list of all steel pieces in an assembly — quantity, shape, size, grade
- **Benchmark:** a fixed reference point for elevation measurements on the construction site
- **Grid lines:** the coordinate system of columns on structural drawings — numbered one axis, lettered the other
- **Section view:** a detail drawn as if the structure were cut along a cutting plane — reveals internal geometry
- **Field splice (FS):** a structural connection made on-site (not in the fabrication shop)
- **Shop drawing:** the fabricator's working drawing showing exact piece dimensions and weld details

---

## Common exam trap

- **W310 × 97 means depth 310 mm, mass 97 kg/m** — not width, not strength, not area. The first number is depth.
- **Grade 350W yield strength is 350 MPa** — not 350 ksi, not 350 HV. MPa = megapascals.
- **"TYP" means typical at all similar locations** — do not assume it means the worst-case weld applies everywhere. Read for exceptions.
- **Site north ≠ geographic north** — always check the north arrow on the site plan, don't assume the drawing is oriented north-up.
- **BOM quantity × length × kg/m gives total mass** — not just length. This is how you estimate steel tonnage.
- **Benchmark is a reference for elevation — not a reference for horizontal location.** Horizontal location comes from coordinates referenced to property lines or a grid.

---

## Practice question preview

**Q:** A structural drawing calls for a member designated "HSS 152 × 152 × 9.5" made from CSA G40.21 Grade 350W steel. What does the designation "350W" indicate about this material?

A) The steel has a minimum yield strength of 350 ksi and is weldable  
B) The steel has a minimum yield strength of 350 MPa and meets the requirements of CSA G40.21  
C) The steel weighs 350 kg per metre of length  
D) The steel has a maximum carbon equivalent of 350 and requires preheat

**Correct: B**

**Explanation:** CSA G40.21 Grade 350W designates structural steel with a minimum yield strength of 350 MPa. The "W" indicates the grade satisfies all the requirements of CSA G40.21 for general welded construction. Option A is wrong — 350 ksi would be an extremely high value (≈ 2415 MPa); CSA grades use MPa. Option C confuses the grade designation with the mass-per-unit-length of a W-shape. Option D is incorrect — carbon equivalent is not expressed in the same units as a material grade designation.

**Red Seal mapping:** A-4.01 (Uses documentation and reference material), A-4.02 (Interprets drawings and welding symbols)

---

[^1]: [CSA G40.20 / G40.21 — General Requirements for Rolled or Welded Structural Quality Steel](https://www.csagroup.org/store/product/CSA%20G40%3A20/); grade designations (230W, 260W, 300W, 350W, 350WT), minimum yield strengths, UTS ranges, Charpy T suffix requirement
[^2]: [CISC — Handbook of Steel Construction (11th edition)](https://www.cisc-icca.ca/resources/handbook-of-steel-construction/); W-shape, C-shape, L-shape, HSS, WWF designation formats, actual vs nominal dimensions, section properties, connection details
[^3]: [CSA W59 — Welded Steel Construction (2018)](https://www.csagroup.org/store/product/CSA%20W59%3A18/); Clause 5 (design provisions), HSS connection prequalified details, weld joint design for structural applications
[^4]: [Modern Welding (Bowditch et al., Goodheart-Willcox)](https://www.g-w.com/modern-welding); blueprint reading chapter — plan views, elevation views, section views, BOM interpretation, abbreviations, benchmarks
[^5]: [CWB Group — Structural Welding Inspector Training Resources](https://www.cwbgroup.org/education); shop drawing vs. structural drawing hierarchy, weld symbol reading in structural context, drawing traceability
