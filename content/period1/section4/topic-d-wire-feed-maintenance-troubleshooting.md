---
id: p1-s4-d
period: 1
section: 4
section_title: Gas Metal Arc Welding (GMAW), Flux-Cored Arc Welding (FCAW), Metal-Cored Arc Welding (MCAW) and Submerged Arc Welding (SAW)
topic_letter: D
topic_title: Wire Feed Welding Maintenance and Troubleshooting
hours: 6
weight_pct: 2
outcome: >
  Upon successful completion, learners will be able to set up, maintain, and
  troubleshoot wire feed welding equipment.
objectives:
  - Demonstrate the set-up and maintenance required for wire feed drive systems and gun assemblies.
  - Perform corrective measures for malfunctioning wire process equipment.
  - Describe the effects of angle and inclination.
red_seal_mapping:
  - A-1.01 (Maintains hand, power, layout and measuring tools)
  - D-14.02 (Sets up FCAW, MCAW and GMAW equipment)
  - D-14.03 (Sets operating parameters for FCAW, MCAW and GMAW)
citations:
  - source: Miller Electric — Wire Feed Welding Troubleshooting Guide (public)
    ref: Bird-nesting causes and cures, contact tip wear, gas coverage problems, drive roll troubleshooting
    url: https://www.millerwelds.com/resources/article-library/mig-gmaw-welding-guide
  - source: Lincoln Electric — Troubleshooting Wire Feed Welding (public)
    ref: Feeding problems, arc instability, porosity causes, gun maintenance procedures
    url: https://www.lincolnelectric.com/en/education-center/welding-education
  - source: Modern Welding (Bowditch, Goodheart-Willcox, latest edition)
    ref: Chapter 14–15 (GMAW/FCAW setup and troubleshooting, gun angle effects, inclination effects)
    url: https://www.goodheartwillcox.com/products/modern-welding
  - source: ESAB — Handbook of Arc Welding (public)
    ref: Wire feed equipment maintenance procedures, gun angle effects on weld profile and penetration
    url: https://www.esab.com/en/us/education/blog/the-esab-handbook
  - source: AIT Welder Curriculum Guide 012 (2026), Period 1 Section 4 Topic D
    ref: pp. 193–205 (wire feed maintenance and troubleshooting)
    url: https://tradesecrets.alberta.ca/SOURCES/PDFS/CURRICULUM_GUIDES/012_OUTLINE.PDF
---

# Wire Feed Welding Maintenance and Troubleshooting

Wire feed equipment has more components and more potential failure points than a stick welder. The upside: when it works correctly, it's faster and more consistent. The downside: when it fails, production stops. An apprentice who can diagnose and fix common feeding problems and arc problems is worth far more than one who can only weld when everything is already set up perfectly.

---

## Equipment setup sequence — doing it right from the start

A correct setup prevents most troubleshooting situations. Follow this sequence every time you set up a wire feed machine:[^1] [^2]

### 1. Power source setup

- Set the machine to the correct process (GMAW, FCAW — check the manual for mode selection if it's a multi-process unit)
- Set polarity for the wire type:
  - GMAW solid wire (ER70S-6): **DCEP**
  - FCAW gas-shielded (E71T-1): **DCEP**
  - FCAW self-shielded (E71T-11): **DCEN** ← verify this is correct before welding
  - MCAW (E70C-6M): **DCEP**
- Start with voltage and WFS settings from a reference chart (electrode manufacturer's data or machine chart) for your wire diameter and material thickness. You will fine-tune after first test bead.

### 2. Wire feeder and spool setup

- Load the wire spool so it feeds off the top (counterclockwise looking at the spool face from the front of the feeder) — check manufacturer instruction for specific machine
- Thread the wire through the inlet guide, over the drive rolls, through the outlet guide, and into the gun liner
- Install the correct drive rolls for the wire type:
  - Solid wire (ER70S-6): smooth V-groove
  - Cored wire (E71T-1, E70C-6M): knurled/serrated V-groove
  - Aluminum: smooth U-groove
- Set drive roll tension (see tension test below)

**Drive roll tension test:**[^1]
1. Hold the wire coming out of the gun nozzle with your thumb and forefinger — gently restrain it.
2. Activate the wire feed by pressing the trigger (with the gun pointed safely away from the work).
3. The drive rolls should slip before the wire buckles or bends sharply.
4. If the rolls don't slip easily: tension is too high — loosen the adjustment.
5. If the rolls slip without restraining force: tension is too low — tighten slightly.

### 3. Gun and liner setup

- Inspect the liner — look for kinks, debris, or excessive wear
- Install the correct contact tip for the wire diameter (0.035" tip for 0.035" wire)
- Install the gas nozzle
- Check the O-ring or seal at the gun-liner connection
- Blow out the liner with compressed air (brief burst) to clear any shavings before use

### 4. Shielding gas setup

- Open the cylinder valve (stand to the side — never in front of the regulator during initial opening)
- Connect the regulator to the cylinder (correct CGA fitting for the gas type)
- Set the flowmeter to the specified flow rate (WPS or reference table) — trigger the gun to check flow while the gun is pointed at a safe target
- Inspect all connections for leaks (soapy water or gas leak detector spray — never flame)

---

## Common problems and corrective measures

### Problem 1: Bird-nesting (wire tangling at the drive rolls or in the gun)

**What it looks like:** the wire stops feeding, buckles, and tangles into a ball ("bird's nest") behind the drive rolls, at the inlet guide, or in the first few inches of the gun liner.

**Causes:**[^1] [^2]
- Drive roll tension too high (wire buckles under excessive pressure)
- Contact tip is plugged (worn oval, or a burnback has welded the wire to the tip) — wire can't exit the gun, so it backs up
- Liner is kinked or clogged — wire meets resistance and buckles back
- Wire spool is dragging (brake tension too tight) — WFS pulls but the wire isn't coming off the spool freely
- Wrong drive roll for the wire type (smooth rolls on cored wire — slippage)
- Inlet and outlet guides misaligned — wire rubs on guide edges

**Corrective action:**
1. CUT the bird-nested wire — don't try to unspool it
2. Inspect and clear the cause before re-threading
3. Re-thread the wire and do a proper drive roll tension test before resuming

---

### Problem 2: Burnback (wire fuses to the contact tip)

**What it looks like:** the arc stops unexpectedly and the wire appears stuck inside the gun tip. When you look at the contact tip, the wire is fused into it.

**Causes:**[^1]
- Contact tip-to-work distance (CTWD) too short — the arc burned back to the tip before the wire could feed
- Wire feed speed too low for the set voltage
- Contact tip worn (hole is oval — wire wanders and makes intermittent contact causing arc instability)
- Trigger stuck/malfunctioning — wire continues to feed after arc goes out and feeds into the solidifying weld pool

**Corrective action:**
1. Cut the wire above the burnback point
2. Remove the contact tip (it may need pliers — don't burn your hands)
3. Replace the contact tip
4. Check and adjust CTWD and WFS before continuing
5. Inspect the trigger for smooth operation

---

### Problem 3: Porosity (gas pores in the weld)

**Causes (wire feed specific):**[^1] [^3]

| Cause | Corrective action |
|---|---|
| Gas flow too low | Increase flow rate to recommended range |
| Gas flow too high (turbulence) | Reduce flow rate |
| Gas hose leak | Check all fittings with soapy water; replace damaged hose |
| Wind disrupting shielding | Use a windscreen; reposition work; switch to self-shielded FCAW |
| Contaminated base metal (rust, oil, paint, moisture) | Clean base metal before welding |
| Wrong gas for the wire (e.g., CO₂ on MCAW) | Verify gas type matches electrode specification |
| Gas nozzle clogged with spatter | Clean or replace nozzle |
| Damaged or contaminated wire (rusty wire from improper storage) | Replace wire spool; inspect wire spool storage conditions |

---

### Problem 4: Excessive spatter

**Causes:**[^1] [^2]

| Cause | Corrective action |
|---|---|
| Voltage too high for WFS (arc too long) | Reduce voltage slightly |
| Voltage too low for WFS (arc too short, frequent shorts) | Increase voltage slightly |
| Wrong gas (CO₂ causes more spatter than Ar/CO₂) | Evaluate whether switching to Ar/CO₂ mix is appropriate |
| Wrong polarity (especially DCEP on SS-FCAW E71T-11) | Verify polarity for the wire type |
| Contaminated base metal | Clean the base metal |
| Wire oxidized | Check wire storage condition; replace if rusty |

---

### Problem 5: Inconsistent wire feed speed / erratic arc

**Causes:**[^1] [^2]

| Cause | Corrective action |
|---|---|
| Worn/kinked liner | Replace the liner |
| Drive roll worn smooth (no grip) | Replace drive rolls |
| Drive roll tension incorrect | Re-set tension (see tension test) |
| Dirty or worn contact tip | Replace contact tip |
| Wire spool brake too tight | Loosen spool brake — spool should spin freely when you pull the wire by hand |
| Gun cable too tightly coiled (liner kinking) | Straighten the gun cable; avoid sharp bends in the cable |
| Wire shavings in the liner | Blow out the liner with compressed air |

---

## Gun angle effects — work angle and travel angle

Gun angle is just as important in wire feed welding as electrode angle in SMAW. It affects:[^1] [^4]

- Bead profile (width and reinforcement height)
- Penetration depth and direction
- Spatter direction
- Shielding gas coverage

### Work angle

**For a T-joint fillet weld:**
- Ideal work angle: **45°** to both members (bisects the joint angle)
- Effect of too high (toward vertical member): undercut at top toe; more penetration into vertical
- Effect of too low (toward horizontal member): undercut at bottom toe or overlap; less penetration into horizontal

### Travel angle

**Forehand (push) vs. backhand (drag/pull):**

| Technique | Gun angle | Effect |
|---|---|---|
| **Forehand (push)** | Gun points in the direction of travel (5–15° lean toward the weld) | Wider bead; shallower penetration; better visibility of the joint ahead; better gas coverage |
| **Backhand (drag/pull)** | Gun points away from the direction of travel (5–15° lean away) | Narrower bead; deeper penetration; better for thick materials and root passes |

**Standard GMAW short-circuit travel angle:** Forehand (push) technique, **5–15° from perpendicular** pointed in the direction of travel.[^1]

**Standard FCAW travel angle:** backhand (drag) is often preferred for FCAW, particularly for self-shielded, because dragging the gun away from the travel direction helps control the larger weld pool typical of FCAW.

---

## Effects of inclination (gun angle relative to horizontal)

When welding on an incline or on joints that are not perfectly horizontal or vertical, the gun inclination relative to gravity changes the penetration pattern and bead shape.[^3] [^4]

**Uphill (gun angled upward, welding upward):**
- Pool flows away from the direction of travel (downward)
- Gravity tends to hold the pool "in" the joint
- Good fusion; deep penetration at the root

**Downhill (gun angled downward, welding downward):**
- Pool flows toward the direction of travel
- Faster travel possible
- Shallower penetration — thin plate only; avoid on structural joints

**For horizontal fillet welds:** the gun must compensate for gravity pulling the pool downward. Lowering the work angle (aim more toward the bottom member) helps counteract pool sag.

---

## Drive system maintenance schedule

Regular maintenance prevents most wire feed problems.[^1] [^2]

| Item | Maintenance action | Frequency |
|---|---|---|
| **Contact tips** | Replace when worn oval, plugged, or burned back | As needed (multiple times per shift in high-deposition work) |
| **Gas nozzle** | Clean spatter from inside with pliers or nozzle reamer; apply nozzle gel/spray to resist spatter | Daily or as needed |
| **Drive rolls** | Inspect for wear; clean accumulated metal shavings | Weekly or when feeding problems begin |
| **Liner** | Blow out with compressed air; replace if kinked or worn | Monthly or when wire feeding becomes rough |
| **Gun cable** | Inspect for kinks and damage to the outer sheath; coil loosely for storage | Weekly |
| **Wire spool** | Cover with plastic bag when not in use to prevent rust and moisture absorption | After each shift |
| **Inlet/outlet guides** | Inspect for wear (guides develop grooves that grip the wire) | Monthly |

---

## Numbers you need to memorize

- **FCAW self-shielded (E71T-11) polarity: DCEN** — verify every time you change wire type[^1]
- **GMAW solid wire (ER70S-6) polarity: DCEP**[^1]
- **Drive roll for solid wire: smooth V-groove; for cored wire: knurled V-groove; for aluminum: smooth U-groove**[^1]
- **Standard GMAW travel angle: 5–15° forehand (push)**[^1]
- **Backhand/drag: narrower bead, deeper penetration; forehand/push: wider bead, shallower penetration**[^1]
- **Bird-nesting: check contact tip, liner condition, drive roll tension, and spool brake first**[^1]
- **Burnback: check CTWD, WFS relative to voltage, contact tip condition**[^1]

---

## What the textbook doesn't tell you

**The liner is the most neglected component on any MIG machine.** Most apprentices replace contact tips when the arc goes bad — but if replacing the tip doesn't fix the problem, the liner is almost always the culprit. A liner that's full of shavings and wire fragments causes intermittent resistance that shows up as erratic arc, bird-nesting, and inconsistent bead width. Replace liners proactively — they're cheap compared to the downtime.

**Anti-spatter spray inside the nozzle is a maintenance shortcut, not a replacement for cleaning.** Anti-spatter (dip or spray) reduces the adhesion of spatter to the nozzle interior and extends the time between cleanings. But it must be applied to a CLEAN nozzle — applying it over accumulated spatter just seals the old spatter in place. The spatter must still be physically removed. Also: never get anti-spatter on the contact tip or into the gas orifices.

**"Push" vs. "drag" is process-specific, not a preference.** GMAW short-circuit: push is standard because it provides better visibility and gas coverage, and shallower penetration is acceptable. FCAW: drag is often preferred because the larger pool needs better control and the self-shielded wire's longer stickout changes the geometry. SAW: always flat position, no angular variation needed. Know which technique is correct for which process before you develop a habit that's wrong for the job.

**Inconsistent WFS is often the extension cord, not the feeder.** A wire feeder running through an undersized extension cord experiences voltage drop. The motor slows down, wire feed speed drops, the arc goes erratic. If the machine works fine at the panel but erratically at the end of a long cord — check the cord sizing for the machine's input amperage. Minimum 10-gauge (14-gauge for short runs on smaller machines) — check the machine manual.[^1]

---

## Key terms

- **Bird-nesting:** wire tangling into a ball at the drive rolls or in the gun — caused by any condition that prevents the wire from feeding forward freely
- **Burnback:** wire fusing to the contact tip when the arc burns back to the tip — caused by too-short CTWD, low WFS, or worn contact tip
- **Drive roll tension:** the clamping force applied by the drive rolls to the wire — must be sufficient to feed without slipping, but not so high as to crush cored wire
- **Liner:** the spiral-wire or plastic tube inside the gun cable through which the electrode wire travels
- **Forehand (push) technique:** gun aimed in the direction of travel — wider bead, shallower penetration, better gas coverage
- **Backhand (drag) technique:** gun aimed away from the direction of travel — narrower bead, deeper penetration
- **Work angle:** electrode/gun angle perpendicular to the direction of travel — determines leg length distribution and fusion
- **Travel angle:** electrode/gun angle along the direction of travel — determines push or drag technique
- **Inclination:** the direction of travel relative to horizontal (uphill or downhill) — affects pool control and penetration
- **CTWD (Contact Tip to Work Distance):** total distance from tip end to work surface; adjusting this changes effective stickout and amperage

---

## Common exam trap

- **"Forehand (push) technique produces deeper penetration than backhand (drag)"** — false. Backhand (drag) produces deeper, narrower penetration. Push produces wider, shallower penetration.
- **"Porosity means the wire feed speed is too high"** — not necessarily. Porosity in wire feed welding is almost always a gas coverage problem — the root cause is usually a leak, insufficient flow, wind, or contamination. WFS affects deposition rate, not gas coverage.
- **"Replace the contact tip when bird-nesting occurs"** — possibly correct, but the bird-nesting may have been caused by the contact tip blockage OR by liner problems, drive roll tension, or spool brake. Replacing only the tip without investigating the true cause means the problem will return.
- **"Backhand/drag is the standard technique for GMAW short-circuit on thin sheet"** — this is arguable on exams. The industry standard for GMAW short-circuit on thin sheet is forehand (push) — better visibility, shallower penetration (burn-through risk reduced), better gas coverage. Drag is acceptable and used, but push is more commonly described as the standard.

---

## Practice question preview

**Q:** During GMAW operation, the wire repeatedly bird-nests at the drive rolls. The contact tip has been replaced and the problem continues. What is the MOST likely remaining cause?

A) Wire feed speed is set too high  
B) The liner is kinked or clogged with wire shavings  
C) The shielding gas flow rate is too low  
D) The voltage is set too high  

**Correct: B**

**Explanation:** After replacing the contact tip (which can cause bird-nesting if worn/plugged), the next most likely cause is a kink or clog in the liner. When the liner provides resistance to wire travel, the wire buckles backward and tangles at the drive rolls. A clogged liner (from accumulated wire shavings, debris, or a kink from coiling) presents high feeding resistance that the drive rolls cannot overcome, causing the wire to buckle. Option A (WFS too high) would cause burnback or poor weld bead, not bird-nesting. Option C (gas flow) does not affect wire feeding. Option D (voltage too high) causes arc instability, not wire feeding problems.

**Red Seal mapping:** D-14.02 (Sets up FCAW, MCAW and GMAW equipment — troubleshoots and corrects wire feeding problems)

---

[^1]: [Miller Electric — Wire Feed Welding Troubleshooting Guide](https://www.millerwelds.com/resources/article-library/mig-gmaw-welding-guide), bird-nesting causes (contact tip plugged, liner kinked, tension too high, spool brake), burnback causes (CTWD too short, low WFS), drive roll tension test procedure, contact tip replacement frequency, gun cable maintenance
[^2]: [Lincoln Electric — Troubleshooting Wire Feed Welding](https://www.lincolnelectric.com/en/education-center/welding-education), porosity root causes (gas coverage, contamination), spatter causes and corrections, inconsistent WFS causes (liner wear, drive roll wear, extension cord voltage drop), maintenance schedule
[^3]: [Modern Welding (Bowditch, Goodheart-Willcox)](https://www.goodheartwillcox.com/products/modern-welding), Chapter 14–15 "GMAW/FCAW Setup and Troubleshooting": gun angle effects on bead profile (push vs drag), inclination effects (uphill vs downhill), work angle for T-joint fillets, forehand 5–15° standard angle
[^4]: [ESAB — Handbook of Arc Welding](https://www.esab.com/en/us/education/blog/the-esab-handbook), gun angle effects on penetration and bead shape, forehand vs backhand penetration characteristics, inclination effects on pool control, FCAW drag preference
