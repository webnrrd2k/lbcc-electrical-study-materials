# ELECT 280 Traffic Signal Systems 1 — Syllabus Study Guide

This guide follows the ELECT 280 syllabus and modules in order. Each section uses the same seven parts: **1 Main ideas, 2 Examples, 3 Background, 4 Dangerous conditions, 5 Exceptions, 6 Common misunderstandings, 7 Easily overlooked.**

Sources are the course intersection prints, the 2018 Caltrans Electrical Standard Plans, the 332L Cabinet Manual v3.0, the CA MUTCD, the FHWA Signal Timing Manual and Detector Handbook. NEC article numbers refer to NFPA 70. Code values and Caltrans specification limits change between editions, so check the edition your agency uses before relying on a number.

| Section | Covers assignments |
| --- | --- |
| A. Phases and phase numbering | 1, 3, 5 |
| B. Ring diagram and concurrency | 2, 7 |
| C. Plans and Caltrans Standard Plans | 2 |
| D. Pedestrian heads and push buttons | 3, 9, 14 |
| E. Loop detectors and detector designations | 3, 6, 9, 14 |
| F. The Model 332 cabinet | 4 |
| G. PDA, output file, load switches and flash | 8, 11 |
| H. The 210 monitor and diode card | 10 |
| I. Conduit and conductor schedule: signal cable and DLCs | 12, 13 |
| J. Power, street lighting and grounding | 15 |
| K. The controller and signal timing | Module 16 |

## A. Phases and phase numbering (Assignments 1, 3, 5)

**1. Main ideas**

- A phase is the timing for a movement, or a set of movements that can safely move together. Caltrans uses the NEMA 8-phase "dual ring" layout.
- Even phases (2, 4, 6, 8) are through movements. Odd phases (1, 3, 5, 7) are protected left turns.
- Ø2 and Ø6 run in opposite directions on the main street. Ø4 and Ø8 run in opposite directions on the side street.
- Each left turn uses the same approach as one through phase: Ø1 with Ø6, Ø5 with Ø2, Ø3 with Ø8, Ø7 with Ø4. Each left turn crosses the through phase whose number is one higher or lower: Ø1 crosses Ø2, Ø5 crosses Ø6, Ø3 crosses Ø4, Ø7 crosses Ø8.

**2. Examples**

- Main street runs east and west and Ø2 is eastbound through. Then Ø6 is westbound through, Ø1 is the westbound left (it shares the approach with Ø6 and crosses eastbound Ø2), and Ø5 is the eastbound left.
- On a quiz print: mark the main-street throughs with 2 and 6 and their lefts with 1 and 5, then the side street with 4 and 8 and its lefts with 3 and 7.

**3. Background**

- Number from the main street. Caltrans usually assigns Ø2 to the main-street direction going north or east, but each agency and plan can differ. The plan's phase diagram, drawn as small arrows in the title block area, is the final word.
- Signal heads sit on the **far side** of the intersection and face approaching drivers. CA MUTCD Part 4D requires at least two heads for each through movement, and far-side placement is the norm.
- A "MAT" is a head on the mast arm, "MAS" a side-mounted head on the mast arm, and "pole" a head on the pole shaft. These come from the Standard and Equipment Schedule.

**4. Dangerous conditions**

A wrong phase label at a head means the wrong wires get landed in the cabinet. That can show a green to conflicting traffic. Always check a new or rewired intersection in flash or with the heads covered, then watch one full cycle in operation.

**5. Exceptions**

- Split phasing: when the two directions of a street run one after the other, for example Ø3 and Ø4 timing in sequence instead of together.
- Permissive or protected-permissive lefts (flashing yellow arrow, FYA) have their own head arrangement and may use an overlap channel.
- Some agencies, or a "T" intersection, leave phases unused. The plan's phase diagram marks those blocks "NOT USED".
- Overlaps (A, B, C, D) are outputs tied to two or more phases, such as a right-turn arrow that runs with a compatible left turn.

**6. Common misunderstandings**

- Labeling a head by its corner instead of by the traffic it faces.
- Assuming Ø2 is always northbound. Check the plan's phase diagram.
- Pairing a left turn with the wrong through phase. Use the rule: the same approach equals a compatible pair (1-6, 5-2, 3-8, 7-4).

**7. Easily overlooked**

- Read the north arrow first. Prints are often turned so north is not up.
- Existing (E) equipment is drawn with lighter or dashed symbols, and new equipment with solid symbols. Both still need phases.
- Right-turn heads usually run with the parallel through phase unless the plan shows an overlap.

## B. Ring diagram and concurrency (Assignments 2, 7)

**1. Main ideas**

- The ring diagram shows the order phases time in. Ring 1 runs Ø1 → Ø2 ‖ Ø3 → Ø4. Ring 2 runs Ø5 → Ø6 ‖ Ø7 → Ø8.
- Phases in the same ring conflict and never time together. Concurrency means one phase from Ring 1 and one from Ring 2 timing together.
- The **barrier** (double line) splits main-street phases from side-street phases. Both rings must reach the barrier and cross it together.
- In the course diagram, ped phases sit above their through phases: 13 (Ø2P) and 14 (Ø4P) in Ring 1, and 15 (Ø6P) and 16 (Ø8P) in Ring 2.

**2. Examples**

| Left of barrier (main street) | Right of barrier (side street) |
| --- | --- |
| 1+5 (both lefts) | 3+7 (both lefts) |
| 1+6 (westbound left with westbound through) | 3+8 |
| 2+5 | 4+7 |
| 2+6 (both throughs), with peds 13 and 15 | 4+8 (both throughs), with peds 14 and 16 |

A common sequence is: 1+5 → 1+6 or 2+5 (whichever left finishes first) → 2+6 → barrier → 3+7 → 3+8 or 4+7 → 4+8 → barrier.

**3. Background**

- **The yellow line is the yellow change interval.** It warns drivers that the green is ending. The CA MUTCD minimum yellow depends on posted speed, about 3.0 s at 25 mph up to about 5.0 s at 55 mph. Kinematic formula: Y = t + v/(2a + 2gG). With t = 1 s, a = 10 ft/s² and a 45 mph (66 ft/s) flat approach, Y = 1 + 66/20 = 4.3 s.
- **The red line is the red clearance, or all-red.** Every approach shows red so a car that entered on yellow can clear. A common estimate is R = (W + L)/v. For a 70 ft wide intersection, a 20 ft car and 66 ft/s, R = 90/66 ≈ 1.4 s.
- The barrier exists because every main-street movement conflicts with every side-street movement.
- NEMA TS-2 and the FHWA Signal Timing Manual (Chapter 4) describe the dual-ring structure.

**4. Dangerous conditions**

Programming two conflicting phases to run together, such as Ø2 with Ø3, causes a green-green conflict. The 210 monitor should catch it only if the diode card is right (see Section H). Short yellow or zero all-red causes red-light running and right-angle crashes.

**5. Exceptions**

- Lead/lag left turns: Ø5 can time after Ø2, which is a lagging left. This needs care with the "yellow trap" when a permissive left faces a lagging opposing through.
- Split phasing puts phases one after another in the same ring and leaves the other ring empty on that side.
- A "soft" barrier, a single line in the course drawing, can be crossed in some sequences. The hard double barrier cannot.

**6. Common misunderstandings**

- Treating the red line as "the light is red". It means **all** approaches are red at once.
- Drawing concurrency arrows across the barrier.
- Thinking both rings must change at the same time inside a barrier group. They don't. Only at the barrier.
- Forgetting the peds. Ø2P can run only while Ø2 times.

**7. Easily overlooked**

- The ring diagram is a picture of the **logic**. The diode card in the 210 monitor has to match it.
- Ped timing (walk + flashing don't walk) often sets how long the through phase must last, especially on wide streets.
- In "dual entry" mode, a call on one through phase can make the controller time its partner through too.

## C. Plans and Caltrans Standard Plans (Assignment 2)

**1. Main ideas**

- A signal plan (an "E" sheet) shows what to build. The Caltrans Standard Plans show how standard items are built and what each symbol means.
- Each plan has a legend, notes, a Standard and Equipment Schedule (poles, heads, push buttons, luminaires), and a Conduit and Conductor Schedule.
- The 2018 Electrical Standard Plans start with ES-1A to ES-1C, which cover symbols, abbreviations and how conduit runs are numbered.

**2. Examples**

- ES-1C shows how conduit run numbers work.
- Abbreviations from the legend: AB = abandon (remove conductors from the conduit). BC = install a pull box in an existing conduit run. CB = install conduit into an existing pull box. CF = conduit stays for future use, conductors removed, pull tape installed. RR = remove and reuse. RS = remove and salvage. RC = removed and becomes the contractor's property. SC = splice new to existing conductors. SD = service disconnect. PEC = photoelectric control. DH = detector handhole.
- A typical plan legend: "existing 2070 controller in a 332 cabinet with BBS to remain", "existing 120/240 V metered Type III-BF service", "repull existing SIC through new conduit".
- Pole types in the schedule: 15TS, 19-4-100 and 29-5-100. Look up each type in the ES standard and lighting plans for its mast arm, luminaire and foundation.

**3. Background**

- **Order of precedence:** project special provisions, then the plans, then the Standard Plans, then the Standard Specifications (Caltrans Std Specs Section 5-1.02). When the plan and the Standard Plan differ, follow the project documents.
- Existing equipment is drawn with outlined or lighter symbols and new equipment with solid symbols. Many Standard Plan symbols come in both versions.
- Plan notes set clearances. A typical plan requires 36 in. from the curb face to any fixed object inside curb returns, 18 in. along sidewalks, a 48 in. flat area at each APS, and a 48 in. pedestrian walkway. These come from ADA and Caltrans design rules.
- Wiring and materials must also meet the NEC. Caltrans electrical work is covered by Std Specs Sections 86 (general electrical) and 87 (systems), along with NEC Articles 300 (wiring methods), 310 (conductors) and 352/344 (PVC and rigid conduit).

**4. Dangerous conditions**

- Not checking for underground utilities before you dig foundations or trench conduit. Call 811 (USA North / DigAlert in California) at least two working days before.
- Placing a pole or cabinet without the required clearance creates a crash hazard and an ADA barrier.

**5. Exceptions**

- City and county agencies may use their own standard plans and symbols. Many large cities have their own details.
- Some plan notes override the Standard Plans. Example: "SIC repull only" in a run means that run gets no new signal cable.
- Bonus question idea: a substitute pole, such as a 29A-5-100 for a 29-5-100, works only if the anchor bolt pattern, foundation and mast arm all match the Standard Plan tables. Check before you say yes.

**6. Common misunderstandings**

- Using the Standard Plans in place of the project plan.
- Missing the difference between existing and new symbols.
- Reading AB as "remove conduit". It means abandon the conduit and pull its conductors.

**7. Easily overlooked**

- Check the revision date in the title block. Course prints can be many years old.
- Scale (1 in. = 20 ft on that plan) lets you check conduit lengths and the 345 ft distance to the limit line.
- Read the notes on every sheet. Many say "this sheet only".

## D. Pedestrian heads and push buttons (Assignments 3, 9, 14)

**1. Main ideas**

- A ped phase runs with the parallel vehicle through phase: Ø2P with Ø2, Ø4P with Ø4, Ø6P with Ø6, Ø8P with Ø8.
- The ped head is on the far end of the crosswalk, facing people about to cross. The push button (PPB, or APS when accessible) is at the near end, where people wait.
- Ped intervals: **Walk**, then **Flashing Don't Walk** (ped clearance), then steady Don't Walk.
- In the cabinet, push buttons enter the controller through 242 DC isolators in the input file. The 332L manual shows which input file slots hold the ped isolators. Ped outputs leave through the 2P, 4P, 6P and 8P switch packs.

**2. Examples**

- A crosswalk across the east leg of an east-west main street runs north-south, parallel to the side street. Its ped head runs with the side-street through phase (Ø4 or Ø8), not with Ø2 or Ø6.
- A corner pole can hold a Ø6 ped head and a Ø4 push button. The button on a pole often serves a different crosswalk from the head on that same pole.

**3. Background**

- **Ped clearance (CA MUTCD 4E.06):** FDW time = crossing distance ÷ 3.5 ft/s. The walk + FDW together must also cover the full distance from the push button at 3.0 ft/s. The minimum walk is normally 7 s.
- Example: a 60 ft crosswalk gives 60 ÷ 3.5 = 17.1 s FDW. With a 6 ft walk from the button, (60 + 6) ÷ 3.0 = 22 s. Walk 7 + FDW 17.1 = 24.1 s, which is more than 22 s, so it meets the rule.
- Countdown displays are required on new ped heads where the ped clearance is more than 7 s (CA MUTCD 4E.07).
- **APS placement (CA MUTCD 4E.08 and 4E.09):** within 5 ft of the crosswalk line extended, 1.5 to 6 ft from the curb edge, and at least 10 ft between two APS units on one corner. The button about 3.5 ft high, next to a level 48 in. landing (plans often call this out in a note).
- The 3CSC carries the push-button circuit, one cable for each push-button location.

**4. Dangerous conditions**

- A ped head landed on the wrong phase can show Walk while conflicting cars have green. Check every ped display during turn-on.
- APS units and ped heads carry 120 VAC in the pole. The push button is low voltage, but a damaged pole can put 120 V on the housing. Check for voltage before you touch a knocked-down push-button post.

**5. Exceptions**

- Ped recall: a ped phase can be set to time every cycle without a button press, which is common downtown.
- Exclusive ped phase ("scramble"): all vehicles stop and peds cross in every direction.
- Leading Pedestrian Interval (LPI): Walk starts 3 to 7 s before the parallel green.
- A ped switch pack's yellow output is normally unused. It shows as "Ø2P Y" on the output file list.

**6. Common misunderstandings**

- Giving a ped head the phase of the street it crosses instead of the parallel street.
- Assuming the button and the head on one pole serve the same crosswalk.
- Thinking pressing the button gives an immediate walk. It only places a call that the controller serves in sequence.

**7. Easily overlooked**

- A post with only a push button needs a 3CSC but no 12CSC.
- A pole without an APS needs a 12CSC but no 3CSC.
- Ped timing often sets the minimum green of the parallel through phase.

## E. Loop detectors and vehicle detector designations (Assignments 3, 6, 9, 14)

**1. Main ideas**

- An inductive loop is a few turns of wire in a saw cut in the pavement. A loop detector card (Model 222, two channels) drives it as part of a tuned circuit.
- A vehicle's metal carries eddy currents that **lower** the loop's inductance. The card sees the frequency rise and sends a "call" to the controller.
- **VDD format = Phase, File, Slot, Channel.** Example: 2I2U = Ø2, Input File I, slot 2, Upper channel. I file serves Ø1–Ø4 and J file serves Ø5–Ø8.
- Path: loop → splice in the pull box → DLC (detector lead-in cable) → cabinet input panel TB → input file slot pins → 222 card → controller.

**2. Examples**

- Each detector channel lands on its own pair of input panel TB positions and its own pair of input file pins. The upper and lower channels of one slot use different pins. Find them in the input panel and input file drawings of the 332L manual.
- A print with four loops on the Ø3 approach, wired to two cards in J8 and J6, could show 3J8U, 3J8L, 3J6U and 3J6L. Each designation gets its own DLC.
- The I file holds Ø1–Ø4 detectors and the J file Ø5–Ø8. Slot I14 holds the 242 for Flash Sense and Stop Time. Other slots hold ped isolators and preemption inputs; the 332L manual shows the standard layout.

**3. Background**

- **Inductance:** L grows with the square of the number of turns (L ∝ N²) and with the loop's area. The card's oscillator frequency is f = 1 ÷ (2π√LC), so lower L gives higher f.
- **Reactance:** X\_L = 2πfL. At 60 Hz, X\_L ≈ 377 × L. A 10 mH coil gives 3.77 Ω, not 3,770 Ω, so convert milli and micro first.
- **Impedance:** Z = √(R² + X\_L²), not R + X\_L. A coil with 6 Ω resistance drawing 0.8 A at 120 V has Z = 150 Ω and X\_L = √(150² − 6²) ≈ 149.9 Ω, so L = 149.9 ÷ 377 ≈ 0.40 H.
- The lead-in adds inductance and resistance, so long DLC runs lower the loop's sensitivity. Keep the total inside the card's tuning range (loops are usually about 50 to 700 µH).
- **Field tests (Caltrans Std Specs 87 and the FHWA Traffic Detector Handbook):** measure insulation resistance to ground with a megger (typically 100 MΩ or more), loop circuit resistance (a few ohms), and inductance. Check the limits in the edition you work under.
- Twist the loop wires between the saw cut and the pull box, and use shielded, twisted-pair DLC. Ground the shield at the cabinet end only, to reject noise and crosstalk.

**4. Dangerous conditions**

- A megger test (500 V or 1,000 V) will damage the 222 card. Unplug the card and lift the lead-in first.
- Saw cutting and sealing happens in live traffic. Use traffic control per CA MUTCD Part 6.
- **Inductive kick:** opening a current-carrying coil makes a voltage spike, v = L × Δi/Δt. Interrupting 2 A in a 0.4 H coil in 1 ms gives 800 V. This is why relay coils need snubbers or diodes.
- A failed loop that is "stuck on" or "stuck off" can strand a phase or give max green every cycle. Most cards and controllers have a fail-safe that places a constant call.

**5. Exceptions**

- Video, radar, thermal and magnetometer detectors replace loops at many sites, but they still report calls through input file channels.
- Bicycle detection needs higher sensitivity or a special loop shape (Type D diamond or quadrupole) to pick up a bike in the center of the lane.
- Some loops are wired in series or parallel onto one channel. Series raises total inductance and parallel lowers it.

**6. Common misunderstandings**

- Thinking a vehicle **raises** inductance. It lowers it.
- Measuring a coil with an ohmmeter and calling that its impedance. An ohmmeter reads only DC resistance.
- Marking loops that are drawn without a designation. The instructor marks extra items wrong.
- Thinking "U" and "L" mean upstream and limit line. They mean the **upper and lower channel** of the card.

**7. Easily overlooked**

- One DLC for each designation, even when two loops share a pull box.
- Plan callouts such as "INSTALL 4 DLC" count only what that leg adds, not the total in the conduit.
- Writing "U&L" in one slot (for example 2I4U&L) means both channels of that card are used.

## F. The Model 332 controller cabinet (Assignment 4)

**1. Main ideas**

- The 332L cabinet (Caltrans TEES 2009) holds everything that runs the intersection. Its cage, from top to bottom: 2070 controller, drawer shelf, Input File I, Input File J, PDA #2L with the 206L power supply, and Output File #1L.
- The rear panels hold the Service Panel Assembly (SPA) with the TBS terminal block and surge filter, the input panel with the loop terminal blocks, and the police panel switches.
- Power path: utility or BBS → TBS → main breaker and surge filter → "clean AC" to the controller, 206L supply and input files → PDA breakers → switch packs → field wiring → heads.

| Part | What it does |
| --- | --- |
| 2070 controller | Runs the timing program and reads the detector inputs. Sends 24 VDC low-true signals to the load switches through connector C4. |
| Input Files I and J | 14 slots each, for 2-channel or 4-channel cards. Hold 222/224 loop detectors, 242 DC isolators and 252 AC isolators. |
| PDA #2L | Signal circuit breakers, two 204 flashers, the SSR, HI and K24 relays, and the 206L 24 VDC supply. |
| Output File #1L | 12 × 200 switch packs, 4 flash transfer relays (FTRs), the 210 monitor, and the flash program blocks. |
| Police panel | Signals ON/OFF and AUTO/FLASH switches, with limited access for police and fire. |

**2. Examples**

- Labeling the cabinet: the I file holds loops on Ø1–Ø4; the J file holds Ø5–Ø8; the PDA has breakers, clean 120 V GFCI and the auto-flash switch; the power supply turns 120 VAC into 24 VDC; the load switch uses a triac to send 120 VAC to the heads; the FTRs switch between normal operation and fail-safe flash.
- The 242 in slot I14 gives the controller Flash Sense and Stop Time. Turning the police panel to FLASH also triggers Stop Time.

**3. Background**

- **Two grounds:** the DC logic ground (white wire with a red stripe, TB1-2) is kept apart from the AC wiring. AC neutral (AC−) and equipment ground are bonded only at the service, as NEC 250.24 and 250.142 require.
- TB1-1 carries +24 VDC to the field side of the input panel.
- The SPA's TBS is a 5-position block for the utility and the BBS. When a BBS is installed, the #8 AWG jumper on TBS is removed.
- A Model 2070 replaced the older 170 controller. Both fit the 332 cabinet, but the software differs (the course uses Swarco Omni eX).
- 332 is a Caltrans/TEES cabinet. NEMA TS-1 and TS-2 cabinets do the same job with different hardware. The concepts carry over.

**4. Dangerous conditions**

- 120 VAC is on the PDA, service panel and outlets **even with the signals OFF**. Test before you touch.
- A BBS inverter can keep the cabinet live after you open the utility breaker. Turn off the BBS and verify zero voltage (NFPA 70E 120.5, verifying an electrically safe work condition).
- If the 210 is removed and the door is closed, the cabinet goes to flash by design. Never jumper this to run without a monitor.
- Lightning and surges come in on loops and service. Keep the surge filter and grounding in good condition.

**5. Exceptions**

- Output File #2L adds 4 more overlap phases when needed.
- Some agencies use 336 cabinets (smaller) or ATC cabinets with a different layout.
- Some cabinets use a Model 2010 monitor in place of the 210. The 2010 adds red-fail and other checks.

**6. Common misunderstandings**

- Thinking the controller powers the lamps. The load switches do, from the PDA breakers.
- Calling the J file "vehicle detectors" as if the I file weren't. Both hold detector cards.
- Thinking Signals OFF makes the cabinet safe to work in.

**7. Easily overlooked**

- The cabinet door switch tells the controller when the door is open, which shows up in logs.
- Fans and the thermostat matter. Southern California cabinets get hot enough to cause electronics to fail.
- The cabinet print in the door is the record of how the cabinet is wired. Update it when you change anything.

## G. PDA, output file, load switches and flash (Assignments 8, 11)

**1. Main ideas**

- Each PDA signal circuit breaker feeds a group of three switch packs: a left turn, a through and its ped.
- A Model 200 switch pack (load switch) has three outputs. Each output is a triac that switches 120 VAC to a field wire when the controller pulls its 24 VDC input low.
- In normal operation the FTRs connect the switch pack outputs to the field. In flash they drop out and connect the field to the 204 flashers through the flash program blocks.

**2. Examples**

- Tracing Ø2 green: the breaker for the Ø1/Ø2/Ø2P group → the PDA output terminal → the output file → the Ø2 switch pack → its green output on a field terminal (FT) block → a 12CSC conductor → the Ø2 heads.
- The field terminal blocks list each output by phase and color, such as Ø4R, Ø4Y, Ø4G, Ø4P DW, Ø4P Y and Ø4P Walk. The cabinet manual's output file drawing gives the terminal numbers.
- Read flasher voltage at the PDA's flasher test terminals. The meter should swing on and off about once a second.

**3. Background**

- **Flash program blocks** choose red or yellow flash for each phase. Typically the main street flashes yellow and the side street red, or everything flashes red. The agency decides.
- A 204 flasher has two alternating outputs. Flash rate is 50 to 60 flashes per minute (CA MUTCD 4L), with the light on for about half of each cycle.
- The flash pairs (such as 1 with 6, and 2 with 5) are compatible movements on the same approach. Splitting them across two flasher circuits balances the load.
- When FLASH is selected or the 210 trips, the FTR coils and SSR are de-energized. The HI and K24 relays remove 24 VDC from the switch pack inputs as a backup in case the SSR fails to open.
- A triac is a bidirectional thyristor. Once triggered, it conducts until the AC current crosses zero, which makes it suitable for switching AC lamps without contacts.

**4. Dangerous conditions**

- A shorted (failed-on) triac lights a head even when the controller says off. That is the main reason the 210 monitor exists.
- Pulling or inserting a switch pack while it is energized can arc and damage the connector. Put the intersection in flash first.
- In flash, the field wires carry 120 VAC from the flashers. Flash does not make the heads safe to work on.
- A dark intersection is legally an all-way stop (CVC 21800(d)), but drivers often miss it. Restore flash or put up temporary stop control quickly.

**5. Exceptions**

- The ped switch pack's yellow output is normally unused, but it still appears on the terminal list.
- Overlaps use extra switch packs or the Output File #2L.
- LED heads draw much less current than incandescent ones. A very light load can confuse the monitor's fault sensing, so some agencies add load resistors.

**6. Common misunderstandings**

- Reading the PDA or output file drawing as if it were the front view when it is the rear view.
- Thinking flash comes from the controller. It comes from the 204 flashers through the FTRs, so the cabinet can still flash with the controller removed.
- Mixing up ped output order. It is Don't Walk, Yellow (unused), Walk.

**7. Easily overlooked**

- Flash set by the monitor (MU) stays on until someone resets the monitor. Flash from the police panel switch clears when the switch is returned to AUTO.
- After a flash, the controller usually restarts in a set "start-up" phase and interval. Check that it starts correctly.

## H. The 210 conflict monitor and diode card (Assignment 10)

**1. Main ideas**

- The Model 210 monitor (MU) watches the field outputs on 16 channels. If two conflicting channels are on at the same time, it puts the intersection into flash.
- The program card is a diode matrix. **A diode in place means "these two channels conflict".** You cut out a diode only for a pair that is allowed to run together.
- The card comes with every diode in place, so every channel conflicts with every other one. That is the safe default.

| Channel | Assignment |
| --- | --- |
| 1–8 | Ø1 to Ø8 vehicle phases |
| 9, 10 | Overlap A, Overlap B |
| 11, 12 | Special |
| 13, 14, 15, 16 | Ø2 Ped, Ø4 Ped, Ø6 Ped, Ø8 Ped |

**2. Examples**

How to decide on any pair:

1. **Vehicle with vehicle:** use the ring diagram. Pairs on the same side of the barrier, one from each ring, can be compatible. Example: 1-6 (westbound left with westbound through) is compatible, so its diode comes out.
2. **Ped with vehicle:** a ped phase is compatible with a vehicle phase only if no vehicle on that phase turns or drives through the crosswalk. Example: 1-13 stays in, because Ø1 is the westbound left and it turns through the crosswalk that Ø2P peds are using.
3. **Ped with ped:** two ped phases are compatible when their through phases are compatible.
4. **Overlaps:** compatible only with the phases the overlap runs with.

Check your list against the intersection's phase diagram before you cut anything.

**3. Background**

- Number of diodes = number of channel pairs = n(n − 1) ÷ 2 = 16 × 15 ÷ 2 = **120**.
- The 210 also trips on low +24 VDC (24V-I and 24V-II) and on the controller's watchdog signal (CVM). That way a dead or crashed controller sends the intersection to flash.
- A trip latches. The intersection stays in flash until a technician finds the cause and presses reset.
- The monitor measures the AC voltage on the field side of the switch packs. That means it also catches a shorted load switch, a cross-wired cable and wrong field wiring.

**4. Dangerous conditions**

- **Removing a diode for a conflicting pair** means the monitor will no longer catch that conflict. Two conflicting greens can then show without the intersection going to flash. This can cause a right-angle crash.
- Moving a program card from one cabinet to another. Each card matches only its own intersection's phasing.
- Jumpering out or removing the monitor to stop a "nuisance" trip. Find the cause instead: often a bad load switch, a failing LED head or a field short.

**5. Exceptions**

- The Model 2010 adds red-fail monitoring (no red showing on a channel), minimum yellow checks and a fault log.
- Flashing yellow arrow (FYA) left turns and overlaps need extra card setup. Check the agency's FYA wiring detail.
- Some channels can be jumpered for ped yellow on the card ("Ø2 Ped Yellow + Ø4 Ped Yellow" on the instruction sheet). Follow the agency's standard.

**6. Common misunderstandings**

- Thinking a diode means "allowed". It means **conflict**.
- Forgetting the ped and overlap channels and removing only the 8 vehicle pairs.
- Removing diodes for both sides of the barrier as if they were all compatible. 2-3 or 4-6 are never compatible.

**7. Easily overlooked**

- Label the card with the intersection name, date and your initials (step 4 on the instruction sheet).
- Check the card against the ring diagram and the plan's phase diagram. All three must match.
- After installing the card, test it. Put the controller in a test mode and force a conflict, or use a monitor tester, to prove the monitor trips.

## I. Conduit and conductor schedule: signal cable and DLCs (Assignments 12, 13)

**1. Main ideas**

- The schedule lists, for each numbered conduit run, how many of each cable or conductor it carries and the conduit size.
- **12CSC** (12-conductor signal cable): one for each standard with signal heads. **3CSC**: one for each push-button location. **DLC**: one for each detector designation. **SIC**: interconnect to other signals.
- Signal cable runs continuously, without splices, from the cabinet to the pole's terminal compartment. So **a run carries one cable for every pole beyond it**, and the run leaving the cabinet carries all of them.

**2. Examples (a made-up four-corner intersection)**

The cabinet is on the SW corner. Run 1 goes from the cabinet to the SW pull box. Run 2 goes from the SW pull box to the SE corner, run 3 from the SE corner to the NE corner, and run 4 from the SW pull box to the NW corner. Every corner has one pole with heads and a push button.

| Run | Poles beyond it | 12CSC | 3CSC |
| --- | --- | --- | --- |
| 1 | SW, SE, NE, NW | 4 | 4 |
| 2 | SE, NE | 2 | 2 |
| 3 | NE | 1 | 1 |
| 4 | NW | 1 | 1 |

The SW pole is fed by a short stub from the SW pull box. Run 1 leaves the cabinet, so it carries every cable.

Conductor check for one 12CSC: 3 per vehicle phase (R, Y, G) + 2 per ped phase (Walk, DW) + 1 common. A pole with Ø1, Ø6 and Ø6P heads needs 3 + 3 + 2 + 1 = 9, which fits in 12.

**3. Background**

- **Conduit fill (NEC Chapter 9, Table 1):** 53% for one conductor, 31% for two, and 40% for three or more. Cable area = πd² ÷ 4. Many agencies use a lower limit, so check the special provisions.
- **Fill example** (cable sizes assumed; check the data sheet): a 12CSC with 0.60 in. OD has an area of about 0.28 in², and a 3CSC with 0.35 in. OD about 0.10 in². Eight of each is 8 × 0.28 + 8 × 0.10 = 3.04 in². A 3 in. Schedule 40 PVC has 7.07 in² total, so 40% is 2.83 in². One conduit is not enough, so a run like this needs two 3 in. conduits (shown as 2-3" on a schedule).
- Pulling tension and the number of bends also limit a run. NEC 352.26 allows no more than 360° of bends between pull points.
- The common in a 12CSC is the white (grounded) conductor. NEC 200.6 and 200.7 reserve white for the grounded conductor.
- DLC is spliced to the loop wire in the pull box nearest the loop. That is the only splice in the detector circuit. Solder and seal or use the agency's approved splice kit.

**4. Dangerous conditions**

- Pulling cable into a conduit that already has live conductors can damage their insulation and create a shock or short. De-energize them or pull with care.
- Overfilled conduit overheats and damages insulation when the cable is pulled in.
- A crushed or cracked conduit under traffic lets water in, causing ground faults and loop failures.

**5. Exceptions**

- Plan notes override the counting rule. "Repull existing SIC only" means no new signal cable in that run.
- A shorter route through a median may exist, but the plan's design route is what counts.
- A pole with more than 12 needed conductors gets a second 12CSC or a larger cable such as a 28CSC.

**6. Common misunderstandings**

- Counting a pole only in the last run before it, instead of in every run between it and the cabinet.
- Reading plan callouts such as "INSTALL 4 DLC" as the total in the run instead of what that leg adds.
- Giving a push-button-only post a 12CSC, or giving a pole with no APS a 3CSC.

**7. Easily overlooked**

- Check your totals. The cabinet run must equal the number of poles (12CSC), push-button locations (3CSC) and designations (DLC).
- Larger conduit on a run usually means more cable. Use it to confirm your routing.
- Write down any assumption on the sheet, such as a conduit that isn't labeled. The instructor can then follow your reasoning.

## J. Power, street lighting and grounding (Assignment 15)

**1. Main ideas**

- The service (Type III-BF, 120/240 V, metered) feeds the signal cabinet and the street lighting. A typical one has a 100 A 2P main, a 15 A 1P PEC breaker, and an unmetered 30 A 2P lighting breaker.
- **Signal power (#6 on many plans):** service → CB → cabinet only.
- **Lighting (#10 on many plans, 2 conductors):** follows the poles that have luminaires. The 240 V circuit uses two hot conductors.
- **Ground (#8 on many plans):** an equipment grounding / bonding conductor in **every** conduit run, including DLC-only and SIC-only runs.

**2. Examples**

- A run from the service to the cabinet carries the 2 signal power conductors and 1 ground.
- A run between two corners that both have electroliers carries the 2 lighting conductors and 1 ground.
- A run that carries only DLCs or SIC still gets 1 ground.
- A run made of two conduits (2-3" on a schedule) gets a ground in each conduit, so 2.

**3. Background**

- **Ground size, NEC 250.122:** sized by the breaker ahead of the circuit. 15 A → #14, 20 A → #12, 30–60 A → #10, 100 A → #8, 200 A → #6 copper. A #8 suits a 100 A main.
- **Ampacity, NEC 310.16:** copper at 75°C: #10 = 35 A, #8 = 50 A, #6 = 65 A. Check that each conductor's ampacity is at least the breaker rating, with the NEC 240.4(D) small-conductor limits.
- **Voltage drop:** VD = 2KIL ÷ CM, with K = 12.9 for copper. A 240 V lighting circuit on #10 (10,380 CM) carrying 6 A for 400 ft gives VD = 2 × 12.9 × 6 × 400 ÷ 10,380 ≈ 6.0 V, or 2.5%. The NEC suggests no more than 3% on a branch circuit and 5% total (210.19 informational note).
- **Ground electrodes, NEC 250.52 and 250.53:** an 8 ft rod. One rod must measure 25 Ω or less, or a second rod is added at least 6 ft away.
- **Testing ground resistance (NETA ATS / MTS):** use the fall-of-potential (3-point) method with the potential probe at about 62% of the distance to the current probe. A clamp-on tester works only when there is a parallel ground path.
- **The earth is never the fault-return path** (NEC 250.4(A)(5)). The #8 bonding conductor brings fault current back to the service so the breaker trips.
- **Lighting control:** a photoelectric control (PEC) turns the lights on at dusk, either at each luminaire or through a contactor at the service. Caltrans fuses each luminaire in the pole base or the adjacent pull box.

**4. Dangerous conditions**

- **An ungrounded pole or cabinet can become energized** by a fault and stay energized, because no breaker trips. A person touching it completes the circuit. Bond every standard, cabinet and metal pull box lid.
- An open neutral on a 120/240 V service can put up to 240 V across 120 V loads and destroy equipment.
- The service is an arc-flash hazard. Use NFPA 70E PPE and an energized-work permit if work cannot be done de-energized.
- Before a fall-of-potential test, make sure no fault current can flow on the electrode. Lifting a ground on a live system can leave equipment ungrounded.
- A knocked-down electrolier can leave 240 V lighting conductors exposed. Open the lighting breaker before handling.

**5. Exceptions**

- Street lighting on the unmetered breaker is billed at a flat utility rate, so it is kept separate from the metered signal load.
- Some agencies use a 120 V lighting circuit with one hot and a neutral instead of 240 V.
- Where a BBS is installed, the service panel wiring changes. The TBS jumper is removed (Section F).

**6. Common misunderstandings**

- Leaving out the ground in runs that carry only DLC or SIC. Every run gets one.
- Running lighting conductors into the signal cabinet feed.
- Thinking a ground rod by itself protects people. It does not clear a fault. The bonding conductor back to the service does.
- Sizing the ground to the load instead of to the breaker.

**7. Easily overlooked**

- Use bonding jumpers across slip bases and from the anchor bolts to the standard.
- Pull box lids that are metal must be bonded.
- Electrolier types on the Standard Plans (15, 15D, 21, 21D, 30, 31, 32) have different arm and foundation details. Read the schedule.

## K. The controller and signal timing (Module 16, Omni eX on the 2070)

**1. Main ideas**

- The 2070 runs Swarco Omni eX software. It reads detector and push-button calls, times each phase, and drives the load switches.
- **Actuated timing:** a phase starts with a minimum green. Each vehicle call adds a passage (extension) time. The phase ends by **gap-out** (no car within the passage time) or **max-out** (it reaches max green).
- Each phase also has yellow, red clearance, walk and ped clearance (FDW) times, plus recall and detector settings.

| Setting | What it does |
| --- | --- |
| Min green | Shortest green, so drivers waiting at the stop bar can start up |
| Passage / extension | Time added for each actuation (gap timer) |
| Max green | Upper limit when there are calls on conflicting phases |
| Yellow / red clearance | Change intervals (Section B) |
| Walk / ped clearance | Ped intervals (Section D) |
| Recall (min, max, ped, soft) | Serves the phase without a call |
| Detector memory (locking / non-locking) | Whether a call is held after the vehicle leaves the loop |

**2. Examples**

- Passage 3.0 s and max green 40 s: if cars keep arriving less than 3 s apart, Ø2 runs to 40 s and maxes out. If a 3 s gap appears at 22 s, it gaps out at 22 s.
- **Coordinated cycle check:** each ring's splits must add up to the same total at each barrier. Ring 1: Ø1 12 + Ø2 38 = 50 s, and Ring 2: Ø5 15 + Ø6 35 = 50 s. Side street: Ø3 10 + Ø4 30 = 40 s, and Ø7 12 + Ø8 28 = 40 s. Cycle length = 50 + 40 = 90 s.

**3. Background**

- The FHWA Signal Timing Manual (2nd ed., Chapter 4) is the main timing reference. The CA MUTCD Part 4 sets minimum yellow, ped walking speed and flash rates.
- **Coordination** uses a common cycle length, splits (the time given to each phase) and an offset (how one signal's cycle lines up with the next signal along the street) to create a "green wave". SIC or fiber links the controllers.
- **Preemption:** railroad preemption has top priority and clears cars off the tracks. Emergency vehicle preemption (EVA to EVD inputs on the J file) gives a green to the approaching fire truck.
- A typical Webster estimate of cycle length is C = (1.5L + 5) ÷ (1 − Y), where L = total lost time per cycle and Y = sum of critical flow ratios. This is an extra topic beyond the course.

**4. Dangerous conditions**

- Setting yellow or red clearance below the CA MUTCD minimum, or entering 0 by mistake.
- Loading the wrong database into a controller, or one meant for another intersection. Always back up the old one first.
- Changing timing or preemption while the intersection runs without watching the result. Railroad preemption errors can trap a vehicle on the tracks.
- Leaving a phase on recall with no detection, which wastes green and causes red-light running out of frustration.

**5. Exceptions**

- Pretimed (fixed-time) operation ignores detectors.
- Time-of-day plans change timing, coordination or flash operation by the clock.
- Some phases rest in green (main-street recall) while others rest in red until called.

**6. Common misunderstandings**

- Thinking max green is how long the phase always runs. It only applies when there is a call on a conflicting phase.
- Mixing up passage time with min green.
- Assuming the detector card's "delay" and "extend" settings are the same as controller timings. Both exist and they add together.

**7. Easily overlooked**

- Check timing units. Many values are entered in tenths of a second.
- Write every change in the intersection's timing sheet and log.
- After a power failure or flash, the controller restarts in its start-up phase. Check that it is set correctly.
