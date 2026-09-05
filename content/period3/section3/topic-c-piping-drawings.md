---
id: p3-s3-c
period: 3
section: 3
section_title: Drafting, Drawings and Specifications
topic_letter: C
topic_title: Piping Drawings
hours: 16
weight_pct: 7
outcome: >
  Upon successful completion, learners will be able to analyze, identify, and interpret
  piping drawings including spool sheets, isometric drawings, and orthographic projections
  of piping systems.
objectives:
  - Describe the purpose of a spool sheet.
  - Interpret symbols that represent individual components on a spool sheet.
  - Interpret position and orientation of piping systems from an isometric drawing.
  - Interpret component sizes in a piping system from a spool sheet.
  - Develop isometric drawings from orthographic projections.
  - Develop a material list for a piping system.
  - Interpret pipe drawings.
red_seal_mapping:
  - A-4.01 (Uses documentation and reference material)
  - A-4.02 (Interprets drawings and welding symbols)
  - B-7.01 (Develops templates)
  - B-7.02 (Transfers dimensions from drawings to materials)
  - B-8.02 (Fits components for welding)
citations:
  - source: ASME B31.3 — Process Piping
    ref: Symbol conventions, joint requirements, pipe schedule and material spec references
    url: https://www.asme.org/codes-standards/find-codes-standards/b31-3-process-piping
  - source: ASME/ANSI B36.10M — Welded and Seamless Wrought Steel Pipe
    ref: Pipe schedule tables (OD, wall thickness, weight per metre for schedules 40, 80, 160, XXH)
    url: https://www.asme.org/codes-standards/find-codes-standards/b36-10m-welded-and-seamless-wrought-steel-pipe
  - source: Modern Welding (Bowditch et al., Goodheart-Willcox)
    ref: Chapter on piping drawings — isometric drawing, spool sheets, fitting symbols, orthographic interpretation
    url: https://www.g-w.com/modern-welding
  - source: ASME B16.9 — Factory-Made Wrought Buttwelding Fittings
    ref: Elbow, tee, reducer, cap dimensions and end prep requirements
    url: https://www.asme.org/codes-standards/find-codes-standards/b16-9-factory-made-wrought-buttwelding-fittings
  - source: Lincoln Electric — Pipe Welding and Piping System Fundamentals
    ref: Reading spool sheets, identifying spools, pipe schedule interpretation
    url: https://www.lincolnelectric.com/en/education-center/welding-education
---

# Piping Drawings

Process piping is the circulatory system of industrial plants — refineries, chemical plants, power stations, pulp mills. Every joint in that system was made by a welder, and every weld was traced to a drawing. The drawing tells you what pipe grade, what fitting, what weld prep, and what NDE is required. If you can read a spool sheet, you can work in any process plant on the continent.

---

## Types of Piping Drawings

Piping information is communicated through several drawing types, each serving a different audience:[^3][^5]

| Drawing type | Description | Purpose |
|---|---|---|
| **P&ID (Piping and Instrumentation Diagram)** | Schematic showing ALL pipes, valves, instruments, and equipment — not to scale, no dimensions | Engineering reference, control system design, operations |
| **Plot plan** | Top-down plan view of the facility — equipment locations, pipe rack routes | Physical location reference |
| **Orthographic piping drawing** | Three-view (plan + two elevations) layout of piping runs at correct scale | Engineering deliverable |
| **Isometric drawing (ISO or spool sheet)** | 3D pictorial view on a 2D plane — the welder's primary working document | Fabrication and fit-up in shop or field |
| **Bill of materials / material list** | Table listing all pipe, fittings, and hardware for each spool | Procurement, receiving, QC |

---

## Pipe Schedule — Wall Thickness

Pipe is specified by **Nominal Pipe Size (NPS)** and **Schedule**. NPS is a nominal (not actual) outside diameter identifier. Schedule determines wall thickness.[^2]

### ASME B36.10M pipe schedule examples

| NPS | Outside Diameter (OD) mm | Schedule 40 wall (mm) | Schedule 80 wall (mm) | Schedule 160 wall (mm) |
|---|---|---|---|---|
| 1" (25mm NPS) | 33.40 | 3.38 | 4.55 | 6.35 |
| 2" (50mm NPS) | 60.33 | 3.91 | 5.54 | 8.74 |
| 4" (100mm NPS) | 114.30 | 6.02 | 8.56 | 13.49 |
| 6" (150mm NPS) | 168.28 | 7.11 | 10.97 | 14.27 |
| 8" (200mm NPS) | 219.08 | 8.18 | 12.70 | 23.01 |
| 12" (300mm NPS) | 323.85 | 9.53 | 17.48 | 25.40 |

*Note: values above are approximate — always verify against ASME B36.10M tables.[^2]*

### Special schedule designations

- **Sch STD:** Standard wall — approximately equal to Sch 40 for NPS ≤ 10"; varies for larger sizes
- **Sch XH (or XS):** Extra Heavy — approximately equal to Sch 80 for NPS ≤ 8"
- **Sch XXH (or XXS):** Double Extra Heavy — the heaviest standard schedule
- **Sch 160:** Used in high-pressure piping — heavier than XH in most sizes

**On the spool sheet:** pipe is specified as, for example: **6" Sch 80 A106 Gr. B** = 6-inch NPS, Schedule 80 wall, to ASTM A106 Grade B (seamless carbon steel).

---

## Pipe Material Specifications

| Specification | Material | Notes |
|---|---|---|
| **ASTM A106 Gr. B** | Carbon steel, seamless | Most common process pipe for temperatures to 425 °C — weld without preheat for most schedules |
| **ASTM A53 Gr. B** | Carbon steel, ERW or seamless | Lower grade than A106 — utility and structural pipe |
| **ASTM A333 Gr. 6** | Carbon steel, low-temperature | Charpy tested at −50 °C — for cryogenic or Arctic service |
| **ASTM A312 TP316L** | 316L austenitic stainless, seamless | Chemical and sanitary process |
| **ASTM A335 P22** | 2.25Cr-1Mo alloy steel | High-temperature service (boiler tubes, steam lines to 600 °C) |
| **ASME SA-106 Gr. B** | Same as A106 but with ASME certification | Required when ASME B31.3 code applies |

---

## Piping Fittings — Symbols and Components

Pipe spool sheets use standardized symbols for each fitting type.[^1][^4]

### Buttweld fittings (BW) — ASME B16.9

Buttweld fittings have beveled ends that are welded to the pipe. The most common in process piping.

| Fitting | Symbol on isometric | Description |
|---|---|---|
| **90° long radius elbow (90LR)** | Quarter-circle arc with arrow | Radius = 1.5 × NPS — smooth, low-pressure-drop turn |
| **45° elbow** | Half of 90LR, 45° angle | Gradual change of direction |
| **Tee (equal)** | T-shape intersection | Three-way connection, all legs same size |
| **Reducer (concentric)** | Trapezoid, centerlines aligned | Transitions between two pipe sizes — centerlines match |
| **Reducer (eccentric)** | Trapezoid, one side flat | Transitions between sizes with flat on one side — allows drainage or venting |
| **Cap** | Semicircle end | Closes off the end of a pipe |
| **Weld neck flange (WNF)** | Flange symbol (parallel lines) with hub | Buttweld flange — connects pipe to equipment |

### Socket weld and threaded fittings

Used for smaller pipe sizes (NPS ≤ 2" typically):
- **Socket weld (SW):** fitting socket receives the pipe end; fillet weld at the socket face
- **Threaded (THD or THRD):** screwed connection — not typically welded; used for utility services

---

## The Isometric Drawing (Spool Sheet) — The Welder's Document

An isometric drawing shows a pipe run in a 3D pictorial view projected onto a 2D surface. The axes are drawn at 30° from horizontal:[^3]

- **Horizontal pipe:** drawn at 30° from horizontal (either right-or-left-running)
- **Vertical pipe:** drawn exactly vertical on the sheet
- **The third axis:** the depth axis, also drawn at 30° from horizontal but in the opposite direction

This gives a clear 3D representation without a full perspective projection.

### Key elements on a spool sheet

| Element | Description |
|---|---|
| **Spool number** | Unique identifier (e.g., "SP-101-A3") — links to the overall piping arrangement |
| **Pipe specification (spec break)** | The pipe material class (e.g., "Class 1A: 6" Sch 80 A106 Gr. B") |
| **Dimensions** | Face-to-face or end-to-end dimensions of each segment — given in mm |
| **Fitting symbols** | Each elbow, tee, reducer, flange shown in isometric symbol |
| **Weld numbers / weld marks** | Each field weld labeled (e.g., "W-1," "W-2") — used for weld tracking |
| **Joint type** | BW (buttweld), SW (socket weld), FL (flanged) — labeled at each connection |
| **NDE requirements** | RT, UT, VT requirements noted for each joint or overall |
| **Weld detail references** | Detail drawing number for unusual joint configurations |
| **North arrow and elevation** | Orientation and height reference |
| **Bill of materials** | Table listing all pipe sections, fittings, flanges with quantities |

---

## Reading Dimensions on Spool Sheets

Pipe dimensions are given as:[^1][^3]

- **Face-to-face (F-F or FTF):** the distance between the two end faces of the spool — the overall assembled length
- **Center-to-face (CTF or CL to face):** from the centerline of a fitting to the end face of the spool — used for elbows and tees
- **Center-to-center (CTC or CL to CL):** from centerline of one fitting to centerline of another

**Dimension callout example:** "CL–CL = 4200 mm" means the distance between the centerlines of the two elbow fittings on that leg is 4200 mm.

**Takeout:** when cutting pipe to fit between two fittings, you subtract the "takeout" of each fitting (the distance from the end of the fitting to its centerline — tabulated in ASME B16.9 tables) from the face-to-face dimension.[^4]

**Cut length = Face-to-face distance − (takeout fitting 1) − (takeout fitting 2)**

---

## Developing an Isometric from Orthographic Projections

Orthographic drawings show the piping from directly above (plan view) and directly from the side (elevation views). Isometrics are derived from these views.[^3]

### Step-by-step method

1. **Start with the plan (top view):** identify which way each pipe run goes (north-south or east-west). Mark the horizontal direction changes (elbows).

2. **Add the elevation view:** identify which pipe runs rise or drop. Vertical runs show as vertical lines in the elevation; what appears as a dot in the plan view (coming straight toward you) is a horizontal run in the elevation.

3. **Choose an isometric starting point:** start at one end of the spool (a flange, a connection to equipment, or an open end).

4. **Draw horizontal runs:** north-south runs on the spool go to the upper right on the iso; east-west runs go to the upper left. (Convention varies — match your drawing system.)

5. **Draw vertical runs:** straight up or down on the isometric sheet.

6. **Add fittings:** at each direction change, add the appropriate fitting symbol. Annotate with fitting type, size, and class.

7. **Add dimensions:** face-to-face between each pair of fittings.

8. **Complete the BOM:** list each component from the iso — count elbows, tees, reducers, flanges, and calculate pipe cut lengths.

---

## Material List Development from Spool Sheet

From the completed isometric, develop the material list:[^3]

| Item | How to determine |
|---|---|
| **Pipe quantity (metres)** | Sum of all cut lengths — add 50–100 mm per cut for beveling and cleanup |
| **Elbows** | Count from the iso — identify size (NPS) and type (90LR, 45°) |
| **Tees** | Count and identify equal vs. reducing, plus branch size for reducing tees |
| **Reducers** | Count and identify concentric vs. eccentric, plus both end sizes |
| **Flanges** | Count, identify class (150, 300, 600), type (WNF, slip-on), and NPS |
| **Gaskets** | One per flanged connection — match flange class and facing type |
| **Bolts and nuts** | Per ASME B16.5 table for each flange size and class |

**Tip:** check the BOM on the spool sheet against your manual count from the iso — discrepancies indicate a reading error or a drawing error. Both happen.

---

## NDE Requirements on Piping Spool Sheets

ASME B31.3 specifies examination categories for process piping:[^1]

| Category | Examination required |
|---|---|
| **Category D (Normal fluid service)** | VT 5% RT — one RT per welder, minimum 5% of joints |
| **Category M (Moderate hazard)** | More RT/UT — 10–20% RT per welder |
| **Category H (High-pressure)** | 100% RT or UT on all joints |
| **Critical (highly hazardous)** | 100% RT + UT + hardness testing |

The NDE category for each joint is specified on the spool sheet or in the project piping specification document.

---

## Numbers you need to memorize

- **6" (150mm NPS) OD:** 168.28 mm[^2]
- **6" Sch 80 wall:** 10.97 mm (verify against B36.10M)[^2]
- **4" (100mm NPS) OD:** 114.30 mm[^2]
- **90° LR elbow radius:** 1.5 × NPS (long radius)[^4]
- **Isometric drawing axis angles:** 30° from horizontal for two axes; vertical for the third[^3]
- **ASME B31.3 Normal service minimum RT:** 5% of joints per welder[^1]

---

## What the textbook doesn't tell you

**The spool number and weld numbers are quality control documents, not just drawing labels.** When an inspector does RT on W-3 of spool SP-101-A3, the radiograph is filed against that exact weld ID. If the weld fails and is repaired, the repair weld gets a different suffix (W-3R1). This traceability chain is the legal record of the piping installation. Never make a weld without confirming you know its weld ID.[^1]

**"Eccentric" vs "concentric" reducer selection is engineering — not random.** Eccentric reducers are used where drainage is required (flat side on top allows liquid to drain through; flat side on bottom traps gas). Concentric reducers are used for vertical runs and for instrument-connected pipe. The spec sheet shows which to use. Don't substitute without engineering approval.[^4]

**Pipe and fitting tolerances stack up.** The sum of cut-length tolerances, elbow radius tolerances, and flange face tolerances can produce a spool that's 5–10 mm different from the drawing dimension. Field welders know to anticipate this. "The spool doesn't fit" is one of the most common field piping problems. Leave the final field weld (the "make-up weld") with enough float in the bevel preparation to absorb the tolerance stack — or verify against the physical configuration before cutting the last length.[^3]

**Read the piping spec before reading the spool.** Each project has a piping specification (piping class document) that defines which materials, valves, and fitting standards apply to each service. The spool sheet references the spec by a "spec break" code. The spec tells you exactly which ASTM number, which flange class, and which fitting standard applies. The spool sheet refers to the spec — the spec is the authority.[^1]

---

## Diagram

*(SVG to be added: `assets/diagrams/p3-s3-c-isometric-axes.svg` — 3D coordinate system showing isometric convention: north-south pipe at upper right (30°), east-west pipe at upper left (30°), vertical pipe straight up — with example 2-elbow run from an orthographic plan view mapped to the isometric)*

*(SVG to be added: `assets/diagrams/p3-s3-c-fitting-symbols.svg` — isometric symbols for: 90LR elbow, 45° elbow, equal tee, concentric reducer, eccentric reducer, weld neck flange, cap — each with name and BW/SW/FL designation)*

*(SVG to be added: `assets/diagrams/p3-s3-c-spool-sheet-sample.svg` — a simple isometric spool sheet showing: 3 pipe sections, 2 elbows, 1 flange at each end, weld numbers W-1 through W-4, dimensions, north arrow, basic BOM table)*

---

## Key terms

- **NPS (Nominal Pipe Size):** the nominal (approximate) pipe designation — OD is standardized regardless of schedule
- **Schedule:** the wall thickness designation — Sch 40, Sch 80, Sch 160, XH, XXH
- **Spool:** a pre-fabricated section of pipe with fittings — assembled in shop, then installed in the field
- **Isometric drawing:** a 2D drawing representing a 3D pipe run using 30° axes for horizontal directions and vertical for up-down
- **P&ID (Piping and Instrumentation Diagram):** schematic of the entire piping system showing all equipment, instruments, and controls — not to scale
- **BW (Buttweld):** a butt joint end preparation — the standard connection type for ASME B31.3 process piping
- **Weld neck flange (WNF):** a pipe flange with a long tapered neck for buttwelding — the strongest flange type
- **Eccentric reducer:** a reducer with the flat side on one wall — used for horizontal pipe where drainage must be maintained
- **Takeout:** the distance from the fitting end to its centerline — subtracted when calculating pipe cut lengths
- **Spec break:** the notation on a spool sheet indicating which piping specification (material class) applies
- **Face-to-face (FTF):** the overall dimension of a spool from one end face to the other
- **Center-to-face (CTF):** dimension from a fitting centerline to the end face of the spool

---

## Common exam trap

- **NPS is nominal, NOT actual OD.** A 6" NPS pipe has an OD of 168.28 mm, not 6" (152.4 mm). OD is fixed for each NPS; schedule changes the wall and therefore the ID.
- **Long radius elbow radius = 1.5 × NPS (long radius); short radius = 1.0 × NPS.** The standard fitting specified in most codes is the long radius (LR).
- **Isometric axes:** horizontal pipes are drawn at 30° — NOT horizontal on the paper. Vertical pipes are drawn vertical. The 30° convention is what creates the 3D illusion.
- **Eccentric vs concentric reducer:** ECCENTRIC has one side flat — used for horizontal runs where drainage is needed. CONCENTRIC has centerlines aligned — used for vertical runs. They serve different purposes and cannot be freely substituted.
- **ASME B31.3 "Normal" category requires 5% RT minimum** — not 100%. 100% RT is required only for high-pressure or critical service.
- **Weld numbers are traceability records** — they connect each weld to the welder, WPS, NDE record, and repair history. Never skip weld identification.

---

## Practice question preview

**Q:** A spool sheet shows a horizontal pipe run with an eccentric reducer transitioning from 4" to 3" NPS. The notation shows "Flat on Bottom." What is the purpose of placing the flat side on the bottom of an eccentric reducer?

A) It creates a larger throat area for higher flow velocity through the transition  
B) It ensures the pipe centerlines remain aligned to prevent flow turbulence  
C) It allows gases to vent upward through the top of the reducer  
D) It prevents liquid from pooling at the transition — the flat bottom maintains drainability

**Correct: D**

**Explanation:** An eccentric reducer with flat on bottom (FOB) maintains a flat bottom face through the size transition. In a horizontal liquid pipe run, this ensures that liquid drains through the transition without pooling — the flat bottom carries liquid continuously downward without creating a pocket. Flat on top (FOT) is used when the top of the pipe must remain at the same elevation (useful for connecting to pump suctions where the top of pipe is the reference). Option B describes a concentric reducer, not eccentric. Options A and C do not describe the engineering purpose of eccentricity.

**Red Seal mapping:** A-4.02 (Interprets drawings and welding symbols), B-8.02 (Fits components for welding)

---

[^1]: [ASME B31.3 — Process Piping](https://www.asme.org/codes-standards/find-codes-standards/b31-3-process-piping); symbol conventions, examination categories (Normal/High-pressure), NDE percentages, joint requirements, piping spec document requirements
[^2]: [ASME/ANSI B36.10M — Welded and Seamless Wrought Steel Pipe](https://www.asme.org/codes-standards/find-codes-standards/b36-10m-welded-and-seamless-wrought-steel-pipe); pipe schedule tables — OD values, wall thicknesses for Sch 40/80/160/XH/XXH
[^3]: [Modern Welding (Bowditch et al., Goodheart-Willcox)](https://www.g-w.com/modern-welding); isometric drawing conventions (30° axes), spool sheet components, orthographic-to-isometric conversion, material list development
[^4]: [ASME B16.9 — Factory-Made Wrought Buttwelding Fittings](https://www.asme.org/codes-standards/find-codes-standards/b16-9-factory-made-wrought-buttwelding-fittings); fitting symbols, takeout dimensions, elbow radius (1.5× NPS for LR), eccentric vs concentric reducer descriptions
[^5]: [Lincoln Electric — Pipe Welding and Piping System Fundamentals](https://www.lincolnelectric.com/en/education-center/welding-education); reading spool sheets, identifying spools, pipe schedule interpretation, field vs shop welds
