---
id: p1-s2-a
period: 1
section: 2
section_title: Drafting, Drawings and Specifications
topic_letter: A
topic_title: Weld Symbols
hours: 6
weight_pct: 2
outcome: >
  Upon successful completion, learners will be able to explain the purpose of welding
  symbols, define and interpret weld, welding, and supplementary symbols; interpret
  NDT symbols.
objectives:
  - Explain the purpose of welding symbols.
  - Define weld, welding, and supplementary symbols.
  - Interpret weld, welding, and supplementary symbols.
  - Identify the dimensioning of welding symbols.
  - Interpret NDT symbols.
red_seal_mapping:
  - B-7.02 (Transfers dimensions from drawings to materials)
  - B-8.01 (Prepares materials)
  - B-8.02 (Fits components for welding)
citations:
  - source: AWS A2.4 — Standard Symbols for Welding, Brazing, and Nondestructive Examination (2020)
    ref: Full standard — all welding symbol elements, reference line, arrow, tail, supplementary symbols
    url: https://www.aws.org/standards/page/aws-a24
  - source: AWS A3.0 — Standard Welding Terms and Definitions (2020)
    ref: Definitions for weld types, joint types, weld symbol terminology
    url: https://www.aws.org/standards/page/aws-a30
  - source: Modern Welding (Bowditch, Goodheart-Willcox, latest edition)
    ref: Chapter 7 (Reading Welding Symbols and Drawings)
    url: https://www.goodheartwillcox.com/products/modern-welding
  - source: Lincoln Electric — Welding Symbol Reference Card (public)
    ref: Quick-reference welding symbol chart
    url: https://www.lincolnelectric.com/en/education-center/welding-education
  - source: AIT Welder Curriculum Guide 012 (2026), Period 1 Section 2 Topic A
    ref: pp. 37–42
    url: https://tradesecrets.alberta.ca/SOURCES/PDFS/CURRICULUM_GUIDES/012_OUTLINE.PDF
---

# Weld Symbols

A welder who cannot read welding symbols cannot work from a drawing — and in any industrial, structural, or pressure vessel shop, you work from drawings. Welding symbols are the language that tells you exactly what weld to put where, how big, how many passes, and what quality is required. Get this wrong and you're either under-building or wasting filler metal.

---

## Why welding symbols exist

Welding symbols eliminate ambiguity. Without a standard symbol system, every engineer would write notes like "put a weld here, about 6 mm, on both sides, continuous" — and every shop would interpret that differently. AWS A2.4 is the North American standard that defines every symbol element so that a drawing produced in Edmonton is read identically in Calgary, Ontario, or Houston.[^1]

The key distinction that trips up beginners:

- **Weld symbol:** the symbol for a specific type of weld (fillet, groove, plug, etc.) — the small geometric shape below or above the reference line
- **Welding symbol:** the complete assembly on the drawing — reference line + arrow + weld symbol(s) + dimensions + tail + supplementary symbols[^1]

You will hear these used interchangeably on the job, but on an exam they mean different things.

---

## The complete welding symbol — all 8 elements

Every welding symbol is built on a **reference line** — a horizontal line that anchors all information.[^1] [^3]

```
(Tail) ───────── Reference Line ──────────── Arrow
                  ^               ^
             Above = Other side   Below = Arrow side
```

### Element-by-element breakdown

| Element | Location | What it means |
|---|---|---|
| **Reference line** | Horizontal line | The backbone — everything else hangs off this |
| **Arrow** | Points to the joint | Indicates which joint or member the symbol applies to |
| **Arrow side / other side** | Below / above the reference line | Below = arrow side (near side); above = other side (far side) |
| **Weld symbol** | On reference line (below or above) | Identifies the type of weld (fillet, groove, plug, etc.) |
| **Dimensions** | Left of the weld symbol | Size, length, pitch of the weld |
| **Supplementary symbols** | On or around reference line | All-around, field weld, flush/convex/concave contour, melt-through |
| **Tail** | Opposite end from arrow | Welding process, specification, procedure reference (WPS number) |
| **Specification/process** | Inside the tail | Optional — names the process (SMAW, GMAW) or WPS reference |

**Critical rule:** Information placed **below** the reference line applies to the **arrow side** of the joint (the side the arrow points to). Information placed **above** the reference line applies to the **other side** (the far side).[^1] This trips up almost every apprentice at least once.

---

## Standard weld symbols reference table

These are the basic weld symbols you must recognize. All per AWS A2.4.[^1]

### Groove weld symbols

| Weld type | Symbol shape | Notes |
|---|---|---|
| **Square groove** | Two parallel vertical lines | Used for thin materials without beveling |
| **V-groove** | Two diagonal lines forming a V | Most common groove for plate welding |
| **Bevel groove** | One diagonal line (only one side beveled) | Arrow always points to the beveled member |
| **U-groove** | Two curved lines forming a U | Deeper root radius, more expensive to prep |
| **J-groove** | One curved line (one side only) | Arrow always points to the J-prepared member |
| **Flare-V groove** | Two convex curves forming a V | For round bar or tube-to-plate |
| **Flare-bevel groove** | One convex curve | For one curved member to flat plate |

### Fillet weld symbol

The fillet weld symbol is a **right triangle** placed on the reference line with the vertical leg always on the left side (perpendicular to the reference line). The leg size is written to the **left** of the symbol. The weld length is written to the **right**.[^1]

Example: `6 ▷ 50-100` means: 6 mm leg fillet weld, 50 mm long, 100 mm pitch (intermittent)

### Plug and slot weld symbols

| Symbol | Appearance | Use |
|---|---|---|
| **Plug weld** | Circle | Filling a hole drilled through the top member to fuse to the bottom |
| **Slot weld** | Rectangle/elongated oval | Filling an elongated slot |

### Spot and seam weld symbols

| Symbol | Appearance | Use |
|---|---|---|
| **Spot weld** | Circle on reference line | Resistance spot welding or GMAW spot |
| **Seam weld** | Two parallel horizontal lines through a circle | Continuous resistance or GMAW seam |

### Surfacing (buildup) weld symbol

A single wavy line below the reference line — indicates depositing weld metal on a surface (hardfacing, dimensional restoration).

---

## Supplementary symbols

These modify the basic weld symbol:[^1]

| Supplementary symbol | Appearance | Meaning |
|---|---|---|
| **All-around** | Circle at the junction of arrow and reference line | Weld continues all the way around the joint |
| **Field weld** | Flag at the junction of arrow and reference line | Weld to be made in the field (on site), not in the shop |
| **Melt-through** | Solid circle on the opposite side | Full penetration is required; root will be visible on the back side |
| **Flush contour** | Straight line (like an underline on the weld symbol) | Weld face to be finished flush with the base metal surface |
| **Convex contour** | Convex curve above/below the weld symbol | Weld face to have a convex profile |
| **Concave contour** | Concave curve | Weld face to have a concave profile |
| **Backing** | Rectangle below a groove symbol | A backing bar or strip is used at the root |
| **Spacer** | Rectangle with an X through it | A spacer (not a backing) is used |

**Contour symbols combined with finish symbols:**

When a contour symbol appears WITH a letter finish symbol, the weld must be mechanically finished to that contour:
- **C** = chipping
- **G** = grinding
- **M** = machining
- **R** = rolling

Example: a flush contour symbol with a "G" below it means: grind the weld face flush with the base metal surface.[^1]

---

## Dimensioning welding symbols — what goes where

### Fillet weld dimensions

For a fillet weld, the dimension to the **left** of the symbol is the **leg size**. The dimension to the **right** is the **length**.[^1]

Intermittent fillet welds use the format: `length – pitch`

Example: `6 ▷ 50-150` = 6 mm leg fillet, 50 mm weld, 150 mm on centre (50 mm weld + 100 mm gap, repeating)

### Groove weld dimensions

- **Left of symbol:** depth of preparation (S) — how deep the groove is machined
- **In parentheses:** effective throat (E) — the actual depth of weld penetration required
- **Right of symbol:** length (if partial)
- **Angle:** the included angle of the groove, placed inside the symbol

For a complete joint penetration (CJP) groove weld, no size dimension is required — the weld must be full penetration by definition.[^1]

For a partial joint penetration (PJP) groove weld, the depth of groove preparation (S) and effective throat (E) must both be specified.

### Root opening

The root opening dimension is placed **inside** the groove symbol (between the two lines of a V or between the single line and reference line of a bevel).[^1]

---

## NDT symbols

Non-destructive testing symbols follow the same reference line / arrow side / other side convention as welding symbols, but use a separate set of letter codes and geometric symbols per AWS A2.4.[^1]

Common NDT method letters:

| Letter | Method |
|---|---|
| **RT** | Radiographic testing (X-ray or gamma ray) |
| **UT** | Ultrasonic testing |
| **MT** | Magnetic particle testing |
| **PT** | Liquid penetrant testing |
| **VT** | Visual testing |
| **ET** | Eddy current testing |

NDT symbols appear on drawings to specify testing location, method, extent (% of weld length), and acceptance standard. The tail of an NDT symbol typically references the applicable procedure or standard.[^1]

**Example:** A symbol with "UT" above the reference line with "100%" at the tail means: ultrasonic test 100% of the weld on the other side.

---

## Diagram

*(SVG to be added: `assets/diagrams/p1-s2-a-weld-symbols.svg` — a fully annotated welding symbol showing reference line, arrow, arrow-side fillet weld symbol with leg size and length, other-side V-groove symbol with depth of prep and included angle, all-around supplementary symbol circle, field weld flag, tail with process designation, and a separate legend panel showing 10 basic weld symbols side by side)*

---

## Numbers you need to memorize

- **Arrow-side rule:** symbol below the reference line = arrow side (the side the arrow touches)[^1]
- **Other-side rule:** symbol above the reference line = other side (far side)[^1]
- **Fillet dimension: left = leg size; right = length** — not swapped[^1]
- **Intermittent format:** length-pitch (e.g., 50-150 = 50 mm weld / 150 mm centre-to-centre)[^1]
- **CJP groove:** no size dimension required — full penetration by definition[^1]
- **PJP groove:** must specify S (depth of prep) and E (effective throat) in parentheses[^1]
- **All-around symbol:** circle at the arrow-line junction — weld goes all the way around[^1]
- **Field weld symbol:** flag at the arrow-line junction — weld is made on site[^1]
- **Bevel and J-groove arrow rule:** the arrow always points to the member that is beveled or J-prepared — this is the "broken arrow" convention[^1]

---

## What the textbook doesn't tell you

**The broken arrow is mandatory for bevel and J-grooves, and shops actually check this.** When one member of a joint is to be beveled (bevel groove or J-groove), the arrow is drawn with a deliberate bend or kink pointing toward the beveled member. This tells the fabricator which piece to machine. If you draw a straight arrow on a bevel-groove symbol, you're saying "I don't know which piece to bevel" — a good shop will send the drawing back.[^1]

**The tail is often the most important part of the symbol on a structural job.** In structural and pressure vessel fabrication, the tail references a WPS (Welding Procedure Specification) number. That WPS controls every parameter — process, filler metal, preheat, interpass temperature, PWHT. The weld symbol is the "what"; the WPS in the tail is the "how." If there's a WPS number in the tail, you're required to follow it — it's not a suggestion.[^3]

**"All-around" doesn't mean "everywhere on the structure" — it means all around the specific joint shown.** A beginner sees the all-around circle and thinks they need to weld every joint on the assembly. It means: at this specific joint, the weld goes continuously around the full perimeter — typically a structural attachment or post base plate situation.[^1]

**On the job, drawings often miss information or have conflicts.** When a welding symbol dimension conflicts with a note in the drawing (e.g., the symbol says 6 mm fillet but the note says "8 mm fillet"), the correct action is to stop and ask — not to pick the one you prefer. Raise it with the engineer or QC. In most jurisdictions, the detail drawing governs over a general note, but not always.[^3]

---

## Key terms

- **Reference line:** horizontal line that is the backbone of every welding symbol
- **Arrow:** line connecting the reference line to the joint; arrow side = near side
- **Arrow side:** the side of the joint the arrow touches — symbols below the reference line apply here
- **Other side:** the far side of the joint — symbols above the reference line apply here
- **Weld symbol:** the geometric figure representing a specific weld type (the right triangle, V shape, etc.)
- **Welding symbol:** the complete assembly (reference line + arrow + weld symbols + dimensions + tail)
- **Tail:** the forked end of the reference line — carries process, WPS, or specification reference
- **CJP (Complete Joint Penetration):** groove weld that penetrates fully through the joint — no size dimension required on the symbol
- **PJP (Partial Joint Penetration):** groove weld with specified limited penetration depth — S and E both required
- **Intermittent weld:** a weld made in segments (length-pitch format) rather than continuously
- **Supplementary symbol:** all-around, field weld, melt-through, contour — modifiers to the basic weld symbol
- **NDT symbol:** non-destructive testing symbol using the same reference line convention; specifies test method, location, and extent

---

## Common exam trap

- **"Below the reference line = other side"** — this is exactly backwards. Below = arrow side. Above = other side. This is the #1 wrong answer on welding symbol questions.
- **Weld symbol vs. welding symbol** — "The triangle represents the welding symbol" is wrong. The triangle is the weld symbol (specifically, a fillet weld symbol). The welding symbol is the whole assembly.
- **Fillet weld dimension placement** — "The number to the right of the fillet weld symbol is the leg size" — wrong. The number to the LEFT is the leg size. Right is the length.
- **Broken arrow on bevel grooves** — "The arrow can point to either member in a bevel groove joint" is false. It must point to the beveled member (the broken arrow convention is mandatory).
- **All-around vs. field weld** — confusing these two supplementary symbols. All-around = circle; field weld = flag. Both appear at the junction of arrow and reference line.
- **NDT and welding symbols on the same drawing** — these can appear together. An NDT symbol doesn't replace the welding symbol; it adds a testing requirement to a weld that is already specified by its own symbol.

---

## Practice question preview

**Q:** On a welding symbol, a fillet weld symbol (right triangle) appears **above** the reference line with the number 8 to its left and 75 to its right. What does this specify?

A) An 8 mm fillet weld, 75 mm long, on the arrow side of the joint  
B) A 75 mm fillet weld, 8 mm long, on the other side of the joint  
C) An 8 mm fillet weld, 75 mm long, on the other side of the joint  
D) An 8 mm fillet weld, 75 mm long, on both sides of the joint  

**Correct: C**

**Explanation:** The fillet weld symbol above the reference line specifies the **other side** of the joint (the side the arrow does NOT touch). The number to the left of the weld symbol = leg size (8 mm). The number to the right = weld length (75 mm). Option A is wrong because above the line = other side, not arrow side. Option B swaps the dimensions. Option D requires the weld symbol to appear both above and below the reference line.

**Red Seal mapping:** B-7.02 (Transfers dimensions from drawings to materials — reads and interprets welding symbols on fabrication drawings)

---

[^1]: [AWS A2.4 — Standard Symbols for Welding, Brazing, and Nondestructive Examination (2020)](https://www.aws.org/standards/page/aws-a24), complete standard: reference line, arrow, arrow-side/other-side convention, all weld symbols (groove, fillet, plug, slot, spot, seam, surfacing), supplementary symbols (all-around, field weld, melt-through, contour, backing, spacer), finish symbols (C/G/M/R), dimensioning conventions (size, length, pitch, root opening, groove angle, depth of prep, effective throat), broken arrow rule for bevel/J-groove, NDT symbols
[^2]: [AWS A3.0 — Standard Welding Terms and Definitions (2020)](https://www.aws.org/standards/page/aws-a30), definitions: weld symbol vs. welding symbol, CJP, PJP, intermittent weld, reference line, arrow side, other side
[^3]: [Modern Welding (Bowditch, Goodheart-Willcox)](https://www.goodheartwillcox.com/products/modern-welding), Chapter 7 "Reading Welding Symbols and Drawings": welding symbol element functions, tail/WPS reference practice, drawing conflicts, groove dimensioning, NDT symbols
[^4]: [Lincoln Electric — Welding Symbol Reference Card](https://www.lincolnelectric.com/en/education-center/welding-education), quick-reference chart for all standard weld symbols, supplementary symbols, and finish designations per AWS A2.4
