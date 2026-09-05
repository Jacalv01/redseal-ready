# Visual Explainers — Asset Plan

**Purpose:** Some welding concepts are impossible to learn from text alone. This folder holds inline diagrams and animations that make the invisible visible.

**Format:** SVG for diagrams (vector, scales on any screen, small file size, accessible with ARIA labels). Static SVG or SMIL animation. No video for v1.

**Naming:** kebab-case, no spaces, no capitals. Suffix `-anim.svg` for animated versions.

## Priority list — 20 assets

Ordered by teaching value. First 10 are must-have for v1; second 10 are v1.1.

### v1 must-have

| # | ID | Concept | Lesson link |
|---|---|---|---|
| 1 | smaw-arc-anatomy | Cross-section of SMAW arc: electrode core, coating, gas shield, molten pool, slag | period1/section3/topic-a-smaw-equipment |
| 2 | polarity-dcep-dcen | DCEP vs DCEN electron flow, heat distribution 70/30 vs 30/70 | period1/section3/topic-a-smaw-equipment |
| 3 | weld-positions-plate | 1F/2F/3F/4F and 1G/2G/3G/4G positions with plate orientations | period1/section2/topic-f-joint-and-weld-types |
| 4 | weld-positions-pipe | 1G rotated, 2G fixed, 5G fixed, 6G 45° inclined pipe positions | period3/section4/topic-b-smaw-mild-steel-pipe |
| 5 | joint-types | Butt, lap, tee, corner, edge joint diagrams with typical weld symbol | period1/section2/topic-f-joint-and-weld-types |
| 6 | groove-prep-single-v | Single-V groove: root opening, root face, bevel angle, included angle labeled | period1/section2/topic-a-weld-symbols |
| 7 | weld-defects-visual | Grid of 8 defect types (undercut, porosity, incomplete fusion, cold lap, overlap, crater crack, arc strike, sugaring) with visual signature | period1/section1/topic-g-weld-faults |
| 8 | gmaw-transfer-modes | Short-arc / globular / spray / pulsed spray droplet transfer illustrated | period1/section4/topic-a-wire-feed-equipment-power-sources |
| 9 | gtaw-tungsten-tip | DCEN pointed geometry vs AC balled — 2× diameter rule and grind-direction | period2/section4/topic-b-gtaw-electrodes-fillers-gases |
| 10 | welding-symbol-anatomy | AWS A2.4 symbol with arrow side / other side, tail, all-around, field weld | period1/section2/topic-a-weld-symbols |

### v1.1 nice-to-have

| # | ID | Concept | Lesson link |
|---|---|---|---|
| 11 | heat-input-effect | Same weld with low / medium / high HI → HAZ width and grain size | period1/section3/topic-a-smaw-equipment |
| 12 | back-step-vs-skip | Back-step and skip-weld sequence arrows | period2/section2/topic-b-pattern-development |
| 13 | mitre-elbow-pipe | 2-piece and 4-piece mitre elbow layout with cut angles | period3/section3/topic-c-piping-drawings |
| 14 | sling-angle-load | Same 500 kg load at 0°, 60°, 120° showing leg tension | period1/section1/topic-c-climbing-material-handling-rigging-hoisting |
| 15 | flame-types-oxy | Neutral, carburizing, oxidizing flame cross-sections | period1/section1/topic-f-oxyfuel-equipment-cutting |
| 16 | stainless-heat-tint | Straw / gold / red / blue / purple / black tint colours with acceptability bands | period3/section2/topic-b-stainless-steel-metallurgy |
| 17 | ndt-methods | VT / PT / MT / RT / UT quick-reference chart with what each detects | period3/section2/topic-e-non-destructive-testing |
| 18 | fillet-geometry | Leg, throat, actual throat vs theoretical, convex vs concave | period1/section2/topic-a-weld-symbols |
| 19 | pipe-bevel-terminology | Land, root face, bevel angle, included angle on a pipe end | period3/section4/topic-b-smaw-mild-steel-pipe |
| 20 | walking-the-cup | GTAW walk-the-cup technique showing cup contact + rocking motion | period3/section5/topic-a-gtaw-mild-steel-plate-pipe |

## Design conventions

- **Colours:** Muted palette — steel grey `#4A5568`, arc yellow `#F6E05E`, molten orange `#DD6B20`, slag purple `#805AD5`. Never pure red/green (colourblind unfriendly).
- **Labels:** Sans-serif (SVG default `system-ui`), 14px min, contrast ratio > 4.5:1.
- **Callouts:** Numbered circles `①②③…` with a legend below the diagram.
- **Size:** Design at 800 × 600 viewBox; SVG scales to fit any screen.
- **Accessibility:** Every SVG has a `<title>` and `<desc>` element. Meaningful `role="img"` on the root.
- **File size:** Aim for < 20 KB per asset. Optimize with SVGO before commit.

## Adding a visual to a lesson

Add to the lesson's frontmatter:

```yaml
visuals:
  - id: smaw-arc-anatomy
    caption: "SMAW arc cross-section showing electrode core, flux coating, gas shield, molten pool, and slag layer."
    embed_after_heading: "What SMAW is — process overview"
```

Rork/app reads the frontmatter, loads `assets/visuals/{id}.svg`, and embeds it after the specified H2.
