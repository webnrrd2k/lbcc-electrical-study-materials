# ELECT 245 — Chapter 12 Study Guide: Panelboard Selection and Installation

## Orientation

Chapter 12 covers two jobs: choosing and installing a panelboard (NEC Article 408 plus parts of 110, 210, 215, 240, 312), and giving people safe room to work on it (NEC 110.26). The textbook is *Electrical Wiring: Commercial*, 18th ed., Chapter 12, pp. 290–311, written to the 2023 NEC (NFPA 70-2023). 

**Learning objectives:**

1. Identify the criteria for selecting a panelboard.
2. Correctly place and number circuits in a panelboard.
3. Determine the correct overcurrent protection for a panelboard.
4. Prepare a panelboard directory.
5. Determine the working space required around electrical equipment.

**Topics, book pages and NEC sections:**

| Topic | Book pages | Main NEC sections |
| --- | --- | --- |
| What a panelboard is; MLO vs. main breaker; dead front | 291–292 | Art. 100 (definition), 408.38, 408.36, 408.54 |
| Bus construction, phase arrangement, circuit numbering | 292–295 | 408.3(E), 408.3(F), 408.41 |
| Panelboard ratings and overcurrent protection | 295–296 | 408.30, 408.36, 240.21, 215.2(A) |
| Cabinet sizing and gutters | 296–297 | 312.6–312.9, 408.3(G), 110.14 |
| Circuit directory, voltage/color ID, source ID, unused openings | 297–300 | 110.22, 408.4, 210.5(C), 215.12(C), 408.7, 110.12(A) |
| Working space: conditions, depth, width, height | 300–304 | 110.26(A), Table 110.26(A)(1) |
| Limited-access spaces (above ceilings, crawl spaces) | 304–305 | 110.26(A)(4) |
| Access/egress, large equipment, personnel doors | 305–307 | 110.26(C)(1)–(C)(3) |
| Illumination; dedicated space indoor and outdoor | 307–308 | 110.26(D), 110.26(E)(1), 110.26(E)(2) |
| Summary | 309 | — |

**2023 NEC changes and easy-to-miss details.** Older study materials often get these wrong:

- **Voltage bands.** Older tables stop at "151–600 V" and send "over 600 V" to Part III. The 2023 NEC adds a **601–1000 V** row to Table 110.26(A)(1) and moves the Part III threshold to **over 1000 V**.
- **"Large equipment."** It is easy to mix up the two thresholds. **Large equipment = 1200 A or more AND over 6 ft (1.8 m) wide**, which needs an entrance at each end (110.26(C)(2)). **800 A or more, any width**, triggers panic or fire-exit hardware on personnel doors within 25 ft (110.26(C)(3)).
- **Height of working space** is **110.26(A)(3)**.
- **Dedicated space outdoors** is **110.26(E)(2)**. Indoor is (E)(1).
- **Dedicated space height:** it does not always run to the structural ceiling. The rule is **6 ft above the equipment or to the structural ceiling, whichever is lower**.
- **Panel overcurrent rules:** both rules come from 408.36, although the book's bullet on p. 295 points the first one to 408.30. In fact, 408.30 sets the panel rating against the calculated load, and 408.36 says the protection can't exceed the panel rating.
- **Book typo (p. 304):** "a concrete pad is permitted to protrude *more than* 6 in." It should read *not more than* 6 in., as Figure 12-18 and p. 303 say.

## Core concepts in depth

### 1. What a panelboard is, and what it is not

A panelboard is busing plus automatic overcurrent devices, built to sit in a cabinet or cutout box against a wall and be **accessible only from the front** (NEC Art. 100). A switchboard can be reached from the rear too and usually stands on the floor. Commercial jobs often buy three separate parts: the cabinet (Art. 312), the interior (Art. 408), and the trim, which comes flush or surface. A residential "load center" is an enclosed panelboard with all three parts in one box.

- **Main-breaker panel:** has its own main overcurrent device.
- **Main-lug-only (MLO):** branch breakers only. It's protected by the feeder device upstream.
- **Dead front is mandatory (408.38).** No live parts are exposed to the person operating the breakers.
- **No 42-circuit limit since the 2008 NEC.** The old "lighting and appliance" vs. "power" categories are gone. Today the panel's design, rating, and listing set the maximum number of devices (408.36, 408.54).
- **Snap-switch panels (408.36(A)).** If a panel has snap switches rated 30 A or less, its overcurrent protection can't exceed 200 A. These are old fusible panels where a switch sat beside each fuse. You'll only meet them in existing buildings. Their switch contact gaps can be too small to break motor loads cleanly.

### 2. Bus construction and phase arrangement

The main bus bars run vertically almost the full height of the panel. Branch stabs connect to alternating bus bars. On a typical panel, the two positions directly across from each other are on the **same phase**, and positions next to each other on one side are on **different phases**.

| Position (left / right) | 1ø, 3-wire (A-B) | 3ø, 4-wire (A-B-C) |
| --- | --- | --- |
| 1 / 2 | A | A |
| 3 / 4 | B | B |
| 5 / 6 | A | C |
| 7 / 8 | B | A |
| 9 / 10 | A | B |
| 11 / 12 | B | C |

- **Odd numbers on the left, even on the right**, whether the breakers are 1-, 2-, or 3-pole.
- A 3-phase panel adds poles in **steps of 6** (A, B, C on each side). That's why panels come in 18, 24, 30, 36, 42 positions and up to about 60.
- Any three adjacent positions on one side give you A-B-C, so a 3-pole breaker drops in anywhere. Any two adjacent positions give a 2-pole at 208 V.
- **408.3(E)(1) AC phase order:** A, B, C from front to back, top to bottom, or left to right, as viewed from the front of the equipment.
- **High-leg (4-wire delta) must be phase B.** Exception: a section that shares a structure with the meter may match the meter's arrangement, where utilities often put the high leg on C.
- **408.3(E)(2) DC buses** may be in any order. Field-mark them with polarity, grounding system, and nominal voltage. This matters more now with PV (Art. 690) and battery systems.
- **Always check the panel's wiring diagram.** Not every manufacturer follows the "typical" pattern.

### 3. The high-leg (wild-leg, red-leg) delta, with the trig

A 120/240-V, 3-phase, 4-wire delta has one winding center-tapped and grounded. Phases A and C sit 120 V from the center tap. Phase B sits at the far corner of the triangle. Model it as an equilateral triangle with 240-V sides and the grounded point at the midpoint of side A–C. The B-to-ground voltage is then the triangle's height:

$$
V_{B\text{-}N} = 240 \sin 60^\circ = 240 \times 0.866 = 207.8 \text{ V}
$$

The book writes the same thing as 120 × √3 = 208 V, because 240 sin 60° = 120 × 2 × (√3/2).

- **Marking:** the high leg must be orange or otherwise effectively identified (110.15, 230.56). The panel needs a permanent field label reading "CAUTION: \_\_ PHASE HAS \_\_ VOLTS TO GROUND" (408.3(F)(1)).
- **Why it matters:** a 120-V single-pole breaker on the B bus puts 208 V on a 120-V load. Only 3-phase or 240-V loads go on B.

The same √3 explains 208Y/120 V: in a wye, line-to-line voltage is phase voltage × √3, so 120 × 1.732 = 207.8 V.

$$
V_{L\text{-}L} = \sqrt{3}\, V_{L\text{-}N} = 2\, V_{L\text{-}N} \cos 30^\circ
$$

### 4. Rating the panelboard and its overcurrent protection

Three numbers have to line up: **calculated load ≤ OCPD rating ≤ panelboard bus rating**, and the OCPD also has to protect the feeder conductors.

- **408.30:** the panel's rating can't be less than the minimum feeder capacity calculated per Art. 220. Bus ratings come in 60, 100, 200, 225, 400, 600 A and up.
- **408.36:** each panelboard gets overcurrent protection rated **no more than the panel rating**. The device can be inside the panel (a main breaker) or anywhere on the supply side (the feeder breaker protecting an MLO).
- **Exception in 408.36:** if the feeder OCPD doesn't exceed the rating of the smallest panel it feeds, those panels don't each need a main.
- **408.36(B), transformer-fed panels:** the protection goes on the **secondary** side. Exception: for a 2-wire-to-2-wire or 3-wire delta-delta transformer, primary protection may also protect the secondary through the turns ratio, per 240.21(C)(1). A 480 to 208Y/120 dry-type is delta-wye, so it doesn't qualify. Its panel needs secondary protection.
- **240.4:** the OCPD protects the conductors at their ampacity. Book Figure 12-7 shows a 225-A MLO fed by 150-A conductors on a 150-A breaker. That's legal, because 150 A protects the wire and doesn't exceed 225 A.
- **Continuous loads (3 h or more), 215.2(A)(1) and 210.20(A):** the OCPD must be at least 125% of the continuous load plus 100% of the noncontinuous load. Put another way, continuous load can't exceed 80% of a standard-rated device. The exception is an assembly and OCPD both **listed for 100%** operation.
- **Feeding several panels from one feeder:** use a wireway or junction box with taps (240.21(B), the 10-ft and 25-ft tap rules), feed-through lugs, or double lugs. Double lugs are only legal if listed for two conductors (110.14(A)).

### 5. Cabinet sizing and wiring space

- Gutters must leave room to bend conductors, splice, and tap (312.6, 312.7, 312.8, 312.9, 408.3(G), 408.55).
- **312.8 (cabinet used for splices and taps):** conductors can fill no more than **40%** of the cross-section at any point. Conductors plus splices and taps can fill no more than **75%**. A warning label is needed if the cabinet holds feed-through conductors for other equipment.
- Bending space depends on conductor size and whether the conductor goes straight into the terminal or bends 90°. Check Tables 312.6(A) and 312.6(B) before you order a narrow cabinet for big feeders.

### 6. Identification: directory, voltage and color, source

- **Circuit directory (110.22(A), 408.4(A)):** every circuit and every change needs a legible, permanent description that is:
  1. located in a directory on the face, inside, or next to the panel door;
  2. specific to the purpose of each circuit, **including spares with a breaker installed**;
  3. detailed enough that circuits can't be confused;
  4. not dependent on transient occupancy ("Tom Jones's office" is wrong);
  5. clear about any abbreviations or symbols used.
- **Voltage and color coding (210.5(C) branch circuits, 215.12(C) feeders):** where premises have **more than one nominal voltage system** (or both AC and DC), the panel must be permanently marked with the system voltage and the color code for each ungrounded conductor. The method may be posted or documented. 210.5(C)(1) Exception: when adding a new system to an unmarked existing one, mark only the new system and add a label saying "other unidentified systems exist on the premises."
- **Source identification (408.4(B), 110.22(A)):** any panel fed by a feeder, outside one- and two-family dwellings, must be labeled with where its power comes from and that location. The label must be permanently affixed, durable for the environment, and **not handwritten**.
- **Close unused openings (408.7, 110.12(A)):** missing breaker knockouts and open raceway knockouts must be closed with protection equal to the enclosure wall. Use listed filler plates and knockout seals, not tape or cardboard.
- **One conductor per terminal (408.41):** each grounded (neutral) conductor gets its own terminal. Lugs and breakers may take two conductors only if listed for it (110.14(A), 110.3(B)).

| System | Phase A | Phase B | Phase C | Neutral | Code basis |
| --- | --- | --- | --- | --- | --- |
| 208Y/120 V | Black | Red | Blue | White | Industry convention; NEC requires white or gray for neutral only (200.6) |
| 480Y/277 V | Brown | Orange | Yellow | Gray | Industry convention; post per 210.5(C) |
| 120/240 V delta high-leg | Black | **Orange** (required) | Black or red | White | 110.15 requires orange or other ID for the high leg |

The NEC only mandates white or gray for the grounded conductor, green (or bare) for the equipment grounding conductor, and orange for the high leg. Everything else is convention that you **post** at the panel. A brown-orange-yellow 480-V system also puts orange on a conductor that is not a high leg. That's why the posted legend is so important.

### 7. Working space: NEC 110.26

Working space is about **getting in and getting out**, safely, around equipment that may be examined, adjusted, serviced, or maintained while energized. It applies to the **space at the equipment, not the room**. Open equipment doors can't reduce the access path below 24 in. wide by 6½ ft high (110.26 intro).

**Table 110.26(A)(1): minimum working space depth (nominal voltage to ground):**

| Voltage to ground | Condition 1 | Condition 2 | Condition 3 | Typical example |
| --- | --- | --- | --- | --- |
| 0–150 V | 3 ft (900 mm) | 3 ft (900 mm) | 3 ft (900 mm) | 208Y/120 V or 120/240 V panel |
| 151–600 V | 3 ft (900 mm) | 3½ ft (1.0 m) | 4 ft (1.2 m) | 480Y/277 V switchboard |
| 601–1000 V | 3 ft (900 mm) | 4 ft (1.2 m) | 5 ft (1.5 m) | 1000-V PV or DC systems (new row in 2023) |

- **Condition 1:** exposed live parts on one side and nothing live or grounded on the other, or live parts on both sides guarded by insulation.
- **Condition 2:** live parts on one side and **grounded** parts on the other. Concrete, brick, tile, and similar conductive building materials count as grounded, as do metal pipes, ducts, and raceways. That makes most real electrical rooms Condition 2.
- **Condition 3:** exposed live parts on both sides, for example two panels facing each other across an aisle.
- **Measure from** exposed live parts, or from the enclosure front (dead front) if the equipment is enclosed.

| Dimension | Requirement | NEC |
| --- | --- | --- |
| Depth | Per the table above, measured from the front | 110.26(A)(1) |
| Width | 30 in. (762 mm) or the width of the equipment, whichever is greater. Doesn't need to be centered. Working spaces may overlap. | 110.26(A)(2) |
| Doors | Hinged doors and panels must open at least 90° | 110.26(A)(2) |
| Height | 6½ ft (2.0 m) or the height of the equipment, whichever is greater | 110.26(A)(3) |
| Intrusions | Associated electrical equipment above or below, and housekeeping pads, may extend no more than 6 in. into the space. Exception: meters in meter sockets. | 110.26(A)(3) |
| Floor | Clear, and as level and flat as practical (new 2023) | 110.26(A)(6) |
| Clear space | No storage, ever | 110.26(B) |
| Lighting | Required for the working space. Must not be automatic-only: some manual control is required. | 110.26(D) |

**Limited-access spaces (110.26(A)(4)).** These cover equipment above lay-in ceilings or in crawl spaces, at 1000 V or less, likely to be serviced energized.

- Access opening: at least 22 × 22 in. (559 × 559 mm) above a ceiling, or 22 × 30 in. (559 × 762 mm) in a crawl space.
- Width: the enclosure width or 30 in., whichever is greater. Doors must open 90°.
- Depth: per Table 110.26(A)(1). Height: whatever the space allows. A horizontal structural member or access panel is permitted in the space.

**Access and egress (110.26(C)).**

- **All equipment, (C)(1):** at least one entrance of sufficient area. A door is permitted but not required. The NEC gives no dimensions; the building code may.
- **Large equipment, (C)(2):** **1200 A or more AND over 6 ft wide**, or grouped service disconnects per 230.71(B) whose combined rating is 1200 A or more and combined width over 6 ft. It needs an entrance at **each end** of the working space, each at least **24 in. wide by 6½ ft high**. Both conditions must apply.
  - (C)(2)(a): one entrance is OK if there is a **continuous, unobstructed way of egress travel**.
  - (C)(2)(b): one entrance is OK if the working space depth is **doubled**. The entrance edge must then be at least one working-space depth from the equipment.
- **Personnel doors, (C)(3):** equipment rated **800 A or more** containing overcurrent, switching, or control devices, with any width. Any door within **25 ft (7.6 m) of the nearest edge of the working space** must open **at least 90° in the direction of egress**, with **listed panic or fire-exit hardware**. The reason: a burned, blinded worker has to be able to push their way out.

**Dedicated equipment space (110.26(E)).** This applies to switchboards, switchgear, panelboards, and MCCs.

- **Indoor, (E)(1)(a):** the footprint of the equipment (its width and depth), from the floor to 6 ft above the equipment or to the structural ceiling, whichever is lower. Keep it clear of piping, ducts, leak protection, and other foreign equipment. Raceways and electrical equipment serving the installation are allowed.
- **(E)(1)(b):** foreign systems above that zone are allowed only with protection against leaks, condensation, and breaks.
- **Outdoor, (E)(2):** identified enclosures, protected from accidental contact, vehicles, and leaks from piping. The same working clearances apply as indoors. No architectural appurtenances in the working space. The footprint is dedicated from grade to 6 ft above the equipment.

### 8. Related rules the chapter assumes, from outside Chapter 12

These aren't central to the textbook chapter, but they decide real panel installations.

| Topic | Rule | NEC |
| --- | --- | --- |
| Breaker handle height | Center of the operating handle no higher than 6 ft 7 in. (2.0 m) in its highest position | 240.24(A), 404.8(A) |
| Panel location | Readily accessible to occupants. Not near easily ignitible material such as clothes closets, not in bathrooms of dwellings or guest rooms, not over steps. | 240.24(B), (D), (E), (F) |
| Interrupting rating / SCCR | Breakers and the panel must be rated for the available fault current at their line terminals. Series ratings only as tested and marked. | 110.9, 110.10, 240.86 |
| Fault current marking | Service equipment outside dwellings must be field marked with the available fault current and the date | 110.24 |
| Arc-flash label | Panels likely to be worked on energized need a warning label. Service and feeder equipment rated 1000 A or more needs a label with voltage, fault current, clearing time, and date. Verify the threshold in your code book. | 110.16 |
| Listed breakers only | Install breakers the panel is listed for (the manufacturer's or UL "classified" breakers) | 110.3(B) |
| Torque | Tighten terminals to the specified torque with an approved means, such as a calibrated torque tool | 110.14(D) |
| Neutral and ground separation | In a feeder-supplied panel, neutrals are isolated from the enclosure. EGCs go on a separate, bonded bar. Remove the bonding screw or strap that's in the box. | 250.24(A)(5), 250.142(B), 408.40 |
| Damp or wet locations | Cabinet rated for the location. Mount with ¼ in. (6 mm) air space behind it in wet locations. | 312.2, 408.37 |

## Worked examples

### Example 1: Sizing a panelboard, its feeder breaker, and its feeder

A tenant space on a 208Y/120-V, 3-phase, 4-wire system has a calculated load (Art. 220) of 52,000 VA. Of that, 30,000 VA is continuous lighting and 22,000 VA is noncontinuous.

1. Calculated load current:

$$
I = \frac{VA}{\sqrt{3}\, V_{L\text{-}L}} = \frac{52{,}000}{1.732 \times 208} = \frac{52{,}000}{360.3} = 144.3 \text{ A}
$$

2. Minimum OCPD, per 215.3: 125% of the continuous load plus 100% of the noncontinuous load.

$$
I_{OCPD} = \frac{1.25(30{,}000) + 22{,}000}{360.3} = \frac{59{,}500}{360.3} = 165.2 \text{ A} \;\Rightarrow\; 175 \text{ A (next standard size, 240.6(A))}
$$

3. Feeder conductors: ampacity of at least 165.2 A (215.2(A)(1)), protected by the 175-A breaker. 2/0 AWG Cu THWN-2 at the 75°C column is 175 A, so it fits with no rounding up needed. Apply any ambient or bundling adjustments first.
4. Panelboard: the bus must be at least 144.3 A (408.30) and at least the 175-A protection (408.36). Choose a **225-A bus, MLO**, protected by the 175-A feeder breaker. A 200-A bus would also comply. The 225-A bus leaves room for growth, and a 42-circuit 225-A interior is usually a stock item.
5. Check the interrupting rating: the available fault current at the panel must not exceed the breakers' interrupting rating or the panel's SCCR (110.9, 110.10).

### Example 2: Review Question 14, OCP for a 150-A panel with a 78-A load

The OCPD must be at least the load and no more than the panel rating (408.36).

| OCPD | OK? | Why |
| --- | --- | --- |
| 70 A | No | Smaller than the 78-A load; it would trip |
| 80, 90, 100, 125, 150 A | Yes | At least 78 A and no more than 150 A |
| 175, 200, 225 A | No | Exceeds the 150-A panel rating, violating 408.36 |

If the 78 A were all continuous, the minimum becomes 1.25 × 78 = 97.5 A, so only 100, 125, and 150 A would work. In every case the feeder conductors also have to be protected at their ampacity (240.4).

### Example 3: Counting poles and spare capacity

The book's owner's panel is 3-phase with 36 poles. It holds nine 1-pole, two 2-pole, and three 3-pole breakers.

- Poles used: 9 × 1 + 2 × 2 + 3 × 3 = 9 + 4 + 9 = **22 poles**.
- Poles left: 36 − 22 = **14**.
- What fits in the leftover spaces depends on **where** they are, not just how many. A 3-pole needs three adjacent spaces on the same side. Four open spaces split two-and-two across the panel hold only 2-pole and 1-pole breakers.
- In a directory, "Spare" means a breaker is installed but not used, and it must still be described (408.4(A)(3)). "Space" means no breaker is installed.

For the Drugstore questions (Review Q3–7), Table 12-1 jumps from circuit 22 to 25. Circuits 23 and 24 aren't listed, so check whether the indoor AC unit and the unit heater are 2-pole or 3-pole against the Appendix A load form before you count.

### Example 4: Field-checking a high-leg delta panel before landing 120-V loads

Expected readings on a 120/240-V, 4-wire delta panel:

| Measurement | Expected |
| --- | --- |
| A–N | 120 V |
| C–N | 120 V |
| **B–N** | **208 V** (240 sin 60°) |
| A–B, B–C, C–A | 240 V |

If B–N reads 208 V, the positions on bus B (positions 3/4, 9/10, 15/16, and so on in the typical pattern) take only 2- or 3-pole breakers. A 120-V receptacle there would see 208 V. Label the panel per 408.3(F)(1) and mark the high-leg conductor orange (110.15).

### Example 5: Working-space depth and width

| Situation | Voltage to ground | Condition | Minimum depth | Minimum width |
| --- | --- | --- | --- | --- |
| 208Y/120-V panel (20 in. wide) facing a block wall | 120 V | 2 | 3 ft | 30 in. |
| 480Y/277-V dead-front switchboard facing a concrete-block wall (Review Q8) | 277 V | 2 | **3½ ft** | Width of the switchboard |
| Two 480Y/277-V panels facing each other across an aisle | 277 V | 3 | 4 ft | 30 in. each |
| 480Y/277-V panel facing a drywall partition with wood studs, nothing grounded opposite | 277 V | 1 | 3 ft | 30 in. |
| 1000-V DC PV combiner facing a grounded metal rack | 1000 V | 2 | 4 ft | 30 in. or the enclosure width |

On the drywall row: many inspectors treat drywall walls as Condition 2 anyway, because of metal studs, boxes, and raceways inside the wall. Ask the AHJ.

### Example 6: Large equipment, access, and doors

| Equipment | Large (110.26(C)(2))? | Entrances needed | Panic hardware on doors within 25 ft (110.26(C)(3))? |
| --- | --- | --- | --- |
| 1600-A switchboard, 8 ft wide | Yes (1200 A or more and over 6 ft) | Each end, 24 in. × 6½ ft. One is OK with continuous egress or doubled depth. | Yes |
| 1000-A switchboard, 5 ft wide | No (under 1200 A) | One of "sufficient area" | **Yes** (800 A or more, any width) |
| 1200-A switchboard, exactly 6 ft wide | No (must be **over** 6 ft) | One | Yes |
| Three 400-A service disconnects grouped per 230.71(B), 2½ ft each | Yes (1200 A combined, 7½ ft combined) | Each end | Depends: (C)(3) is written per piece of equipment. Ask the AHJ. |
| 600-A panel | No | One | No |

Doubled depth for the 1600-A, 277-V board facing concrete (Condition 2): 2 × 3½ ft = 7 ft. The single entrance's nearest edge must then be at least 3½ ft from the equipment.

### Example 7: Dedicated space (Review Question 9)

A panel's top is at 6 ft 7 in. and the structural deck is at 14 ft. The dedicated zone runs from the floor to the lower of these two heights:

- 6 ft above the equipment: 6 ft 7 in. + 6 ft = 12 ft 7 in.
- The structural ceiling: 14 ft.

So the zone ends at 12 ft 7 in.

- A duct crossing the panel's footprint below 12 ft 7 in. violates 110.26(E)(1)(a).
- A duct above 12 ft 7 in. is allowed, but only with protection against leaks and condensation per 110.26(E)(1)(b).
- If the deck were at 10 ft, the zone would stop at 10 ft, and nothing could cross the footprint at all.

In Q9, "8 ft above the panel" read literally is above the 6-ft zone. The electrician's absolute claim ("only for electrical") is then stronger than the code. The answer depends on whether the book means 8 ft above the floor (a violation) or above the panel top (permitted with protection). Answer by citing 110.26(E) and stating which reading you used.

### Example 8: What a lost neutral does to a multiwire branch circuit

Take a 208Y/120-V multiwire branch circuit (A, B, shared N). One leg feeds a 1500-W heater, the other a 100-W lamp, both rated 120 V. Then the shared neutral opens.

$$
R_{heater} = \frac{V^2}{P} = \frac{120^2}{1500} = 9.6\ \Omega \qquad R_{lamp} = \frac{120^2}{100} = 144\ \Omega
$$

The two loads are now in series across A–B, which is 208 V:

$$
I = \frac{208}{9.6 + 144} = 1.354 \text{ A} \qquad V_{lamp} = 1.354 \times 144 = 195 \text{ V} \qquad V_{heater} = 1.354 \times 9.6 = 13 \text{ V}
$$

The small (high-resistance) load gets 195 V, 63% over its rating, and fails or overheats. The big load barely runs. On a 120/240-V system the series voltage is 240 V. That's why 408.41 allows **one neutral per terminal**, and why 210.4(B) requires a multiwire branch circuit to be disconnected simultaneously (a handle-tied or multipole breaker).

The symptom that tells you it's a lost neutral: loads on one leg dim while loads on the other get brighter. Or one load only works when an unrelated load on the other leg is switched on, like the textbook's refrigerator that only runs when the garbage disposal is on.

## Safety and dangerous conditions

The working-space rules exist because arc flash and arc blast kill. A panelboard is where most commercial electricians meet that hazard. The default is **de-energize, test, lock out**. Energized work is the exception, and it has to be justified and permitted.

### The governing documents

| Document | What it covers for this chapter |
| --- | --- |
| NFPA 70 (NEC) 110.26, 110.16, 110.24 | Installation side: the space, the labels, the fault-current marking |
| NFPA 70E, *Standard for Electrical Safety in the Workplace* | Work practices: electrically safe work condition (8 steps, cited in the textbook as 120.5), energized work permit (130.2), shock and arc-flash risk assessment (130.4, 130.5), PPE (130.7) |
| OSHA 29 CFR 1910.303(g) | Federal working-space rule. Mirrors NEC 110.26 and is enforceable on the employer. |
| OSHA 1910.333, 1910.147 / 1926.417 | Safe work practices, lockout/tagout (general industry and construction) |
| ANSI/NETA MTS and ATS | Maintenance and acceptance testing: infrared scans under load, torque checks, insulation-resistance tests of bus and breakers |

### Establishing an electrically safe work condition (NFPA 70E, summarized)

1. Identify every source of supply, using drawings, the directory, and the 408.4(B) source label.
2. Interrupt the load current, then open the disconnecting device for each source.
3. Where possible, visually verify that all blades are open or breakers are withdrawn.
4. Release stored energy (capacitors), and block or relieve other stored energy.
5. Apply lockout/tagout devices per the written procedure.
6. Test each phase conductor, phase-to-phase and phase-to-ground, with an adequately rated meter. **Check the meter on a known live source before and after the test.**
7. Where induced voltage or stored energy could re-energize the circuit, apply temporary protective grounds.
8. Only then is the circuit treated as de-energized.

**Live-dead-live.** If the meter isn't proven on a known source both before and after, a dead reading means nothing.

### Dangerous conditions this chapter can create or expose

| Condition | Why it's dangerous | Prevention |
| --- | --- | --- |
| **Main breaker OFF does not mean panel dead** | The line side of the main, the feeder lugs, and feed-through lugs stay energized. An MLO panel is dead only when the **upstream** feeder breaker is open. | Open and lock the source shown on the 408.4(B) label. Test the line lugs. |
| **Feed-through or double-lugged panels** | Downstream panels fed from this panel's lugs stay live from the line side. Opening one panel's main may kill nothing. | Trace the feeder. Label the source on every panel. |
| **Multiple sources** | Generators, transfer switches, UPS, and PV backfeed can energize the bus with the utility off | Lock out every source. Look for 705.12 backfeed breakers and placards. |
| **High leg (B phase, 208 V to ground)** | 120-V equipment on B gets 208 V. Fire and equipment damage follow. | Measure B–N before adding circuits. Orange marking. 408.3(F)(1) label. |
| **Lost or shared neutral (two neutrals under one screw)** | Loosening the screw to remove a dead circuit's neutral opens a live circuit's neutral. That causes shock and series overvoltage on loads. | One neutral per terminal (408.41). Turn off **all** circuits sharing a neutral. |
| **Multiwire branch circuit with independent 1-pole breakers** | Turning off one breaker leaves the shared neutral carrying the other leg's current. Opening it can shock you. | 210.4(B): simultaneous disconnect (handle ties or multipole breakers). Group the neutral with its hots (210.4(D)). |
| **Open knockouts or missing filler plates** | Fingers, tools, or rodents can reach the bus | Listed filler plates and knockout closures (408.7, 110.12(A)) |
| **Working space used as storage, or blocked egress** | No room to step back from an arc, no way out | 110.26(B). Doors with panic hardware for 800 A or more (110.26(C)(3)). |
| **Under-rated breakers (interrupting rating below available fault current)** | A breaker that can't clear the fault can explode | Verify 110.24 marking against breaker AIC and panel SCCR. Use only tested series combinations (240.86). |
| **Neutral bonded to the enclosure in a subpanel** | Neutral current flows on the EGC, conduit, and building steel. Shock hazard, and GFCI and ground-fault relays misoperate. | Remove the bonding screw or strap in feeder panels. Separate the EGC bar. |
| **Loose terminations** | Heat, then insulation failure, then an arcing fault | Torque to the label value (110.14(D)). Infrared scan under load per NETA MTS. |
| **Removing the dead front while energized** | The cover itself can slip into the bus. Cover screws can drop onto live parts. | Treat cover removal as energized work. Wear PPE per the panel's arc-flash label. |

### Arc-flash facts worth knowing

- Arc temperatures can reach about 35,000°F. The pressure wave can rupture eardrums and throw a worker across the room. Copper expands about 67,000 times in volume when it vaporizes.
- Incident energy rises with available fault current and with **clearing time**. A properly sized feeder breaker with an instantaneous trip, or 240.87 energy-reducing maintenance switching, reduces the hazard.
- The book stresses that injured workers are often burned, blinded, and deafened. That's why the code wants push-to-open panic hardware and two ways out of large-equipment rooms.

## Exceptions, misunderstandings, and field pitfalls

### Exceptions you should know exist

These are summarized. Read the exact wording in your 2023 NEC before relying on one.

| Rule | Exception (summary) |
| --- | --- |
| 110.26(A)(1) depth | **Ex. 1:** No working space is needed at the back or sides of dead-front equipment if nothing there is renewable or adjustable (fuses, switches) and everything is reachable from the front. **Ex. 2:** Smaller spaces are allowed by special permission for very low voltage (30 V rms, 42 V peak, or 60 V DC or less). **Ex. 3:** In existing buildings where equipment is replaced, Condition 2 spacing is allowed between facing dead-front panels if written procedures keep both from being open at once and only authorized, qualified people service them. |
| 110.26(A)(3) height | Meters in meter sockets may extend more than 6 in. (the utility controls them). Existing dwelling-unit service equipment or panels up to 200 A get height relief. |
| 110.26(C)(2) large equipment | One entrance is enough with continuous, unobstructed egress travel ((C)(2)(a)) or a doubled working space ((C)(2)(b)). |
| 408.36 panel protection | No main is needed if the supply-side OCPD doesn't exceed the panel rating. Transformer-fed panels may use primary protection only for 2-wire-to-2-wire or delta-delta (3-wire-to-3-wire) transformers. |
| 408.3(E)(1) high leg on B | A section sharing the meter's structure may match the meter's phase arrangement (often C). |
| 210.5(C)(1) voltage ID | When adding a new system in an existing building, mark only the new one and label "other unidentified systems exist on the premises." |
| 408.4(B) source marking | Doesn't apply to one- and two-family dwellings |

### Common misunderstandings

- **"Working space = the room."** No. It's the box in front of (and, where needed, beside or behind) the equipment. A big room can still be in violation if a cabinet, rack, or pallet sits in the box.
- **"3 ft clearance, always."** Only up to 150 V to ground, or Condition 1. A 277-V panel facing a block wall needs 3½ ft. Two 277-V panels facing each other need 4 ft.
- **"Use line-to-line voltage."** The table uses **voltage to ground**. 480Y/277 is a 277-V row entry (151–600). 208Y/120 is a 120-V entry (0–150). The high leg on a 240-V delta is 208 V to ground, which lands that panel in the 151–600 V row.
- **"Width = width of the panel."** It's 30 in. minimum even for a 14-in.-wide panel, and it doesn't have to be centered.
- **"Dedicated space goes to the ceiling."** It goes to 6 ft above the equipment or the structural ceiling, whichever is **lower**. A suspended ceiling is not the structural ceiling.
- **"Large equipment = 800 A."** 1200 A AND over 6 ft is large (two exits). 800 A or more, any width, means panic hardware on doors within 25 ft.
- **"A door is required."** Not by the NEC for ordinary equipment, only an entrance "of sufficient area." The building code or the owner may require one.
- **"MLO panels are unprotected."** They're protected by the feeder OCPD, and that device must not exceed the bus rating.
- **"A 42-circuit limit."** Gone since the 2008 NEC. The listing governs.
- **"The color code is NEC-mandated."** Black-red-blue and brown-orange-yellow are conventions. The NEC requires that you **post or document** whatever code you use (210.5(C), 215.12(C)), plus white or gray neutral, green EGC, and orange high leg.
- **"Spare" vs. "space."** A spare is a breaker installed with nothing on it, and it must be labeled. A space is an empty position. Both should appear in the directory so nobody guesses.

### Pitfalls real crews run into

1. **Directories written in pencil, or "Lights" / "Recepts" / "Bob's office."** These fail 408.4(A). A good entry gives the type of load, the area, and the location: "Receptacles, Computer Room 3, north wall," "RTU-2 (roof)," "Water heater WH-1, basement mech. room." Use room numbers from the drawings, not people's names.
2. **Directory not updated after a change.** 408.4(A) covers "every circuit **and circuit modification**." A remodel that moves loads and leaves the old directory is a violation and a lockout hazard.
3. **Handwritten source labels.** 408.4(B)(3) forbids them. Use engraved phenolic or a printed durable label: "Fed from MDP-1, circuit 7, main electrical room 101." Drilling a listed enclosure to attach it, especially outdoors or in wet locations, can void the listing (312.10). Use adhesive rated for the environment.
4. **Housekeeping pads poured too far forward.** A pad that sticks out more than 6 in. in front of the switchboard violates 110.26(A)(3). Coordinate with the concrete sub before the pour.
5. **Other trades invading the dedicated space.** Sprinkler mains, condensate lines, and ductwork over panels are the classic case (Review Q9). Catch it at coordination drawings or rough-in, not at final inspection.
6. **Storage creep.** Electrical rooms become mop closets after occupancy. 110.26(B) and OSHA 1910.303(g)(1)(ii) apply for the life of the building. Paint or tape the floor in front of the panels.
7. **Occupancy-sensor-only lighting in electrical rooms.** 110.26(D) requires some manual control. A sensor-only room can go dark mid-task.
8. **Two neutrals under one terminal** after a panel change-out. It's common when the replacement panel has fewer neutral terminals. Add a listed neutral bar extension; don't double up.
9. **Mixing breaker brands.** "It fits" doesn't mean it's listed. Use the panel manufacturer's breakers or UL-classified breakers named on the panel label (110.3(B)).
10. **Ignoring interrupting ratings when adding a panel near a big transformer.** A 10-kA breaker on a bus with 25 kA available is a bomb. Get the fault-current number (110.24) first.
11. **Motor rotation after re-terminating feeders.** If 3-phase motors run backward after a feeder change, swapping two feeder phases fixes every motor at once. **Re-identify** those conductors with colored tape at both ends afterward, per the textbook.
12. **Transformer-fed panels with no secondary protection.** A 480–208Y/120 delta-wye transformer can't use the primary-only exception. The panel needs a main, or a secondary OCPD within the 240.21(C) tap distances.
13. **Bonding screw left in a subpanel.** It's shipped in the box for service use. Remove it for feeder-supplied panels and keep the EGC bar separate.
14. **Above-ceiling equipment (VFDs, small panels, disconnects) with no access.** 110.26(A)(4) requires at least a 22 × 22 in. opening and full working-space depth in front.

## Quick reference and self-check

### Numbers to memorize

| Item | Value | NEC |
| --- | --- | --- |
| Working depth, 0–150 V to ground | 3 ft, all conditions | Table 110.26(A)(1) |
| Working depth, 151–600 V | 3 / 3½ / 4 ft (Conditions 1 / 2 / 3) | Table 110.26(A)(1) |
| Working depth, 601–1000 V | 3 / 4 / 5 ft | Table 110.26(A)(1) |
| Working width | 30 in. or the equipment width, whichever is greater | 110.26(A)(2) |
| Door and hinged-panel swing | 90° minimum | 110.26(A)(2) |
| Headroom | 6½ ft or the equipment height, whichever is greater | 110.26(A)(3) |
| Allowed intrusion (associated equipment, pads) | 6 in. maximum | 110.26(A)(3) |
| Open doors must leave | 24 in. wide × 6½ ft high | 110.26 intro |
| Limited access opening | 22 × 22 in. (ceiling), 22 × 30 in. (crawl space) | 110.26(A)(4) |
| Large equipment | 1200 A or more AND over 6 ft wide | 110.26(C)(2) |
| Large-equipment entrance | 24 in. wide × 6½ ft high, at each end | 110.26(C)(2) |
| Panic hardware | 800 A or more, door within 25 ft, opens 90° in direction of egress | 110.26(C)(3) |
| Dedicated space | Footprint, floor to 6 ft above the equipment or the structural ceiling, whichever is lower | 110.26(E)(1) |
| Snap-switch panel OCP | 200 A maximum if switches are 30 A or less | 408.36(A) |
| High-leg voltage to ground | 208 V (240 sin 60°), phase B, orange | 408.3(E)(1), 408.3(F)(1), 110.15 |
| Continuous load | 3 h or more; OCPD at least 125% (80% loading) unless 100%-rated | 215.2(A), 215.3 |
| Max breaker handle height | 6 ft 7 in. | 240.24(A), 404.8(A) |

### Key terms

- **Panelboard:** busing and automatic OCPDs in a cabinet, accessible only from the front (Art. 100).
- **Switchboard:** a large free-standing assembly, often accessible from the rear.
- **Cabinet:** the enclosure with a swinging door that houses the panelboard (Art. 312).
- **MLO (main lugs only):** a panel with no main OCPD; it's protected upstream.
- **Dead front:** no live parts exposed on the operating side (408.38).
- **Feeder:** the conductors between the service (or a separately derived system) and the final branch-circuit OCPD (Art. 100).
- **Multiwire branch circuit:** two or more ungrounded conductors sharing one neutral, with voltage between them (Art. 100).
- **High leg:** the conductor in a 4-wire delta with the higher voltage to ground (208 V).
- **Working space / dedicated equipment space:** the space for the worker (110.26(A)) vs. the zone reserved for the electrical installation (110.26(E)).
- **Conditions 1, 2, 3:** what is opposite the live parts: nothing, grounded surfaces, or more live parts.
- **Spare vs. space:** an installed but unused breaker vs. an empty position.
- **Qualified person:** someone with the skills and knowledge for the equipment and safety training to recognize and avoid the hazards (Art. 100, NFPA 70E).

### Self-check questions

1. What physically distinguishes a switchboard from a panelboard?
2. A 225-A panel has a 175-A feeder breaker and no main. Is that legal? Cite the rule.
3. Why can't a 120-V circuit be put on bus B of a 120/240-V delta panel?
4. What is the working depth for a 480Y/277-V switchboard facing a concrete-block wall?
5. Two 208Y/120-V panels face each other across an aisle. What is the working depth?
6. A 1000-A, 5-ft switchboard has a door 20 ft from its working space. What hardware is required?
7. List four conditions a 408.4(A) directory entry must meet.
8. What three things does 408.4(B) require of the source label?
9. A sprinkler main is to run 4 ft above the top of a panel, below a 16-ft deck. Allowed?
10. What is the minimum access opening for a panel above a lay-in ceiling?
11. When is 210.5(C) voltage and color identification required?
12. Matching (Review Q13): 110.26(A)(1), (A)(2), (A)(3), (B), (C)(1), (C)(2)(a), (C)(2)(b), (C)(3), (D), (E)(1), (E)(2).

### Answers

1. A panelboard is accessible only from the front and is usually wall-mounted in a cabinet. A switchboard is usually free-standing and may be accessible from the rear.
2. Yes. The OCPD is no larger than the panel rating (408.36), and the supply-side location is allowed. It must also protect the feeder conductors (240.4).
3. B is 208 V to ground. A 120-V load would see 208 V.
4. 3½ ft (277 V to ground, Condition 2).
5. 3 ft (120 V to ground; all conditions are 3 ft).
6. The door must open at least 90° in the direction of egress, with listed panic or fire-exit hardware (110.26(C)(3), 800 A or more). The board isn't "large equipment," so one entrance is enough.
7. Any four of: legible and permanent; at or next to the panel; specific to each circuit, including spares; not confusable; not based on transient occupancy; abbreviations explained.
8. Identify the source and its physical location; permanently affixed and durable for the environment; not handwritten.
9. No. It's inside the dedicated zone (6 ft above the panel is lower than the deck), which violates 110.26(E)(1)(a).
10. 22 × 22 in. (559 × 559 mm), per 110.26(A)(4).
11. Where the premises have more than one nominal voltage system, or both AC and DC. It's still good practice with only one.
12. (A)(1) depth · (A)(2) width · (A)(3) height · (B) clear spaces · (C)(1) minimum entrance and egress · (C)(2)(a) large equipment (unobstructed exit) · (C)(2)(b) working space (doubled) · (C)(3) personnel doors · (D) illumination · (E)(1) indoor dedicated space · (E)(2) outdoor dedicated space. The two (C)(2) letters are the least certain match; check them in your code book.

### Sources

- Simmons, Mullin, Ode, Smith, *Electrical Wiring: Commercial*, 18th ed. (Cengage, 2024), Chapter 12, pp. 290–311.
- NFPA 70-2023 sections as quoted in the textbook. Content from outside the chapter (NFPA 70E, OSHA, NETA, sections 110.9–110.24, 240.24, 250, 312.8) is from general code knowledge, not the course files. Verify it against your own code book.
