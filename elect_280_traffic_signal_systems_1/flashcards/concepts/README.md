# Flashcards — ELECT 280: Course Concepts

103 cards. Read the question, answer it in your head, then click it to check.

Study guide for these cards: [elect_280_study_guide.md](../../elect_280_study_guide.md).

- **Study online:** [flashcard page](https://webnrrd2k.github.io/lbcc-electrical-study-materials/flashcards/?deck=e280-concepts): shuffle, flip, and mark the cards you know.
- **Download:** [Anki](concepts.apkg) · [Quizlet import file](concepts_quizlet.txt) (paste into Quizlet's Import box; images are not included) · [Emacs org-drill](concepts.org) · [raw card data](concepts.json)

## Contents

- [1. Phases and phase numbering](#1-phases-and-phase-numbering) (11)
- [2. Ring diagram and timing intervals](#2-ring-diagram-and-timing-intervals) (12)
- [3. Plans and Standard Plans](#3-plans-and-standard-plans) (6)
- [4. Pedestrian heads and push buttons](#4-pedestrian-heads-and-push-buttons) (13)
- [5. Loop detectors and detector designations](#5-loop-detectors-and-detector-designations) (12)
- [6. The 332 cabinet](#6-the-332-cabinet) (11)
- [7. Load switches, PDA and flash](#7-load-switches-pda-and-flash) (10)
- [8. The 210 monitor and diode card](#8-the-210-monitor-and-diode-card) (9)
- [9. Conduit, cable, power and grounding](#9-conduit-cable-power-and-grounding) (12)
- [10. Safety](#10-safety) (7)

---

## 1. Phases and phase numbering

<details><summary><b>1.</b> In NEMA 8-phase numbering, what do odd and even phase numbers mean?</summary><br>Even phases (2, 4, 6, 8) are through movements. Odd phases (1, 3, 5, 7) are protected left turns.<br><br></details>

<details><summary><b>2.</b> Which phases are usually the main street, and which the side street?</summary><br>Ø2 and Ø6 are the main-street throughs (opposite directions). Ø4 and Ø8 are the side-street throughs.<br><br></details>

<details><summary><b>3.</b> Which through phase shares an approach with each left-turn phase?</summary><br>Ø1 with Ø6, Ø5 with Ø2, Ø3 with Ø8, Ø7 with Ø4. A left turn and the through on the same approach can run together.<br><br></details>

<details><summary><b>4.</b> Which through phase does each left turn cross?</summary><br>Ø1 crosses Ø2, Ø5 crosses Ø6, Ø3 crosses Ø4, Ø7 crosses Ø8 (the opposing through).<br><br></details>

<details><summary><b>5.</b> How do you decide which phase a signal head belongs to?</summary><br>By the traffic it faces, not the corner it stands on. Heads sit on the far side and face approaching drivers.<br><br><sub>A far-side head on the NE corner faces south and serves northbound traffic.</sub><br><br></details>

<details><summary><b>6.</b> Where do signal heads normally go, and how many does a through movement need?</summary><br>On the far side of the intersection. The CA MUTCD requires at least two primary signal faces for the through movement on an approach.<br><br></details>

<details><summary><b>7.</b> What is the first thing to check on a signal plan before marking phases?</summary><br>The north arrow. Prints are often rotated so north is not up.<br><br></details>

<details><summary><b>8.</b> Where is the final word on which direction is Ø2?</summary><br>The plan&#x27;s phase diagram. Ø2 is often the main-street direction going north or east, but agencies differ.<br><br></details>

<details><summary><b>9.</b> What is split phasing?</summary><br>The two directions of a street time one after the other (for example Ø3 then Ø4) instead of together, usually because of shared or heavy left turns.<br><br></details>

<details><summary><b>10.</b> What is an overlap?</summary><br>An output tied to two or more phases, such as a right-turn arrow that is green during its parallel through and a compatible left turn. Overlaps A and B use 210 channels 9 and 10.<br><br></details>

<details><summary><b>11.</b> What does a flashing yellow arrow (FYA) left-turn display mean?</summary><br>Permissive left turn: drivers may turn after yielding to oncoming traffic and pedestrians.<br><br></details>

## 2. Ring diagram and timing intervals

<details><summary><b>12.</b> Write out the standard dual-ring diagram.</summary><br>Ring 1: Ø1 Ø2 | Ø3 Ø4. Ring 2: Ø5 Ø6 | Ø7 Ø8. The barrier (|) separates the main-street group from the side-street group.<br><br></details>

<details><summary><b>13.</b> What is concurrency?</summary><br>Two phases timing at the same time: one from Ring 1 and one from Ring 2, on the same side of the barrier.<br><br></details>

<details><summary><b>14.</b> List the compatible phase pairs on each side of the barrier.</summary><br>Left side: 1+5, 1+6, 2+5, 2+6. Right side: 3+7, 3+8, 4+7, 4+8.<br><br></details>

<details><summary><b>15.</b> Can two phases in the same ring time together?</summary><br>No. Phases in one ring always conflict and time one after another.<br><br></details>

<details><summary><b>16.</b> What is the barrier, and what rule applies to it?</summary><br>The line between main-street and side-street phases. Both rings must reach it and cross it together, because every main-street movement conflicts with every side-street movement.<br><br></details>

<details><summary><b>17.</b> What three intervals make up a vehicle phase?</summary><br>Green, yellow change, and red clearance.<br><br></details>

<details><summary><b>18.</b> What is the red clearance (all-red) interval?</summary><br>A time when every approach shows red, so a vehicle that entered on yellow can clear the intersection.<br><br></details>

<details><summary><b>19.</b> Within what range should a yellow change interval fall?</summary><br>3 to 6 seconds (CA MUTCD 4F.17). Longer yellows go with higher approach speeds.<br><br></details>

<details><summary><b>20.</b> What is the kinematic formula for the yellow change interval?</summary><br>Y = t + v / (2a + 2gG), with t = 1 s, v in ft/s, a = 10 ft/s², g = 32.2 ft/s², G = grade as a decimal.<br><br><sub>35 mph = 51.5 ft/s on a flat road gives about 3.6 s.</sub><br><br></details>

<details><summary><b>21.</b> CA MUTCD Table 4D-101(CA): which speed sets the minimum yellow?</summary><br>The 85th-percentile speed rounded up to the next 5 mph. If only the posted speed is known, add 7 mph (posted 30 mph or more) or 10 mph (25 mph or less).<br><br><sub>Example: 35 mph posted gets 4.1 s.</sub><br><br></details>

<details><summary><b>22.</b> How long are red clearance intervals normally?</summary><br>0.1 to 2.0 seconds, and they should not exceed 6 seconds except for unusual cases (CA MUTCD 4F.17).<br><br></details>

<details><summary><b>23.</b> What is a lagging left turn?</summary><br>A left-turn phase that times after the opposing through, for example Ø5 after Ø2.<br><br></details>

## 3. Plans and Standard Plans

<details><summary><b>24.</b> What do the Caltrans Standard Plans sheets ES-1A to ES-1C cover?</summary><br>Electrical symbols, abbreviations, and how conduit runs are numbered.<br><br></details>

<details><summary><b>25.</b> What comes first when the project plan and the Standard Plans disagree?</summary><br>The project documents: special provisions, then the project plans, then the Standard Plans, then the Standard Specifications.<br><br></details>

<details><summary><b>26.</b> How do existing and new equipment look different on a plan?</summary><br>Existing equipment is drawn outlined or lighter; new equipment is drawn solid.<br><br></details>

<details><summary><b>27.</b> Which two schedules on a signal plan list the equipment and wiring?</summary><br>The Standard and Equipment Schedule (poles, heads, push buttons, luminaires) and the Conduit and Conductor Schedule.<br><br></details>

<details><summary><b>28.</b> What must you do before digging foundations or trenching conduit in California?</summary><br>Call 811 (USA North or DigAlert) at least two working days ahead so underground utilities are marked.<br><br></details>

<details><summary><b>29.</b> Why read every note on a signal plan sheet?</summary><br>Notes can override the general rules, for example &#x27;repull existing SIC only&#x27; in a run, and many say &#x27;this sheet only&#x27;.<br><br></details>

## 4. Pedestrian heads and push buttons

<details><summary><b>30.</b> Which vehicle phase does a ped phase run with?</summary><br>The parallel through phase: Ø2P with Ø2, Ø4P with Ø4, Ø6P with Ø6, Ø8P with Ø8.<br><br></details>

<details><summary><b>31.</b> What are the pedestrian intervals, in order?</summary><br>Walk, flashing Don&#x27;t Walk (pedestrian change interval), then steady Don&#x27;t Walk.<br><br></details>

<details><summary><b>32.</b> What walking speed sets the pedestrian clearance time?</summary><br>3.5 ft/s (CA MUTCD 4I.06). Consider 2.8 ft/s where older or disabled pedestrians routinely cross.<br><br></details>

<details><summary><b>33.</b> What second check must walk plus clearance pass?</summary><br>Walk + clearance must let someone leaving the push button (or 6 ft behind the curb) at the start of Walk cross at 3 ft/s.<br><br></details>

<details><summary><b>34.</b> How long should the Walk interval be?</summary><br>At least 7 seconds; as short as 4 seconds is allowed where pedestrian volumes and needs don&#x27;t require 7.<br><br></details>

<details><summary><b>35.</b> What is the buffer interval added in the 2023 MUTCD?</summary><br>At least 2 seconds of steady Don&#x27;t Walk after the flashing Don&#x27;t Walk, before conflicting traffic is released.<br><br></details>

<details><summary><b>36.</b> When is a countdown display required on a ped head?</summary><br>When the pedestrian change interval is more than 7 seconds (CA MUTCD 4I.04).<br><br></details>

<details><summary><b>37.</b> How high are ped signal heads mounted?</summary><br>Bottom of the housing 7 to 10 feet above the sidewalk (CA MUTCD 4I.03).<br><br></details>

<details><summary><b>38.</b> Where should a pedestrian push button be placed?</summary><br>No more than 5 ft from the outside edge of the crosswalk, 1.5 to 6 ft from the curb face, about 3.5 ft high (4 ft max), with its face parallel to the crosswalk.<br><br></details>

<details><summary><b>39.</b> How far apart should two push buttons on one corner be?</summary><br>At least 10 feet. Closer than that, accessible signals must use speech walk messages.<br><br></details>

<details><summary><b>40.</b> Does the push button on a pole always serve the ped head on that same pole?</summary><br>No. The button usually serves a different crosswalk from the head mounted on the same pole.<br><br></details>

<details><summary><b>41.</b> What is a Leading Pedestrian Interval (LPI)?</summary><br>Walk starts a few seconds before the parallel green, so pedestrians get into the crosswalk before turning cars move.<br><br></details>

<details><summary><b>42.</b> What is ped recall?</summary><br>The controller serves the ped phase every cycle without anyone pressing the button.<br><br></details>

## 5. Loop detectors and detector designations

<details><summary><b>43.</b> How does an inductive loop detect a vehicle?</summary><br>The vehicle&#x27;s metal carries eddy currents that lower the loop&#x27;s inductance. The detector card sees its oscillator frequency rise and places a call.<br><br></details>

<details><summary><b>44.</b> Does a vehicle over a loop raise or lower the loop&#x27;s inductance?</summary><br>Lower.<br><br></details>

<details><summary><b>45.</b> What does a vehicle detector designation like 2I2U mean?</summary><br>Phase 2, Input File I, slot 2, Upper channel.<br><br></details>

<details><summary><b>46.</b> In a designation, what do U and L stand for?</summary><br>The upper and lower channel of the two-channel detector card. They do not mean upstream or limit line.<br><br></details>

<details><summary><b>47.</b> Which input file holds which phases?</summary><br>Input File I holds Ø1–Ø4 detectors; Input File J holds Ø5–Ø8.<br><br></details>

<details><summary><b>48.</b> Trace a loop&#x27;s path from the street to the controller.</summary><br>Loop wire → splice in the pull box → DLC (detector lead-in cable) → input panel terminal block → input file slot → 222 detector card → controller.<br><br></details>

<details><summary><b>49.</b> How many DLCs does each detector designation need?</summary><br>One DLC per designation, even when loops share a pull box.<br><br></details>

<details><summary><b>50.</b> What inductance range do loop detector cards typically work with?</summary><br>About 50 to 700 µH (FHWA Traffic Detector Handbook).<br><br></details>

<details><summary><b>51.</b> Why can&#x27;t you measure a loop&#x27;s impedance with an ohmmeter?</summary><br>An ohmmeter uses DC and reads only resistance. Impedance needs an AC measurement or an LCR meter.<br><br></details>

<details><summary><b>52.</b> What must you do before meggering a loop?</summary><br>Unplug the 222 card and lift the lead-in. The megger&#x27;s 500 or 1000 V test voltage will damage the card.<br><br></details>

<details><summary><b>53.</b> How is the DLC shield grounded?</summary><br>At the cabinet end only, to reject noise without creating a ground loop.<br><br></details>

<details><summary><b>54.</b> What does a long lead-in do to loop sensitivity?</summary><br>It adds inductance and resistance, so the vehicle&#x27;s change is a smaller fraction of the total and sensitivity drops.<br><br></details>

## 6. The 332 cabinet

<details><summary><b>55.</b> List the 332L cage from top to bottom.</summary><br>2070 controller, drawer shelf, Input File I, Input File J, PDA #2L (with the 206L power supply), Output File #1L.<br><br></details>

<details><summary><b>56.</b> What does the 2070 controller do?</summary><br>Runs the timing program, reads detector and push-button calls, and drives the load switches with 24 VDC logic.<br><br></details>

<details><summary><b>57.</b> What plugs into the input files?</summary><br>222 two-channel loop detectors, 242 DC isolators (push buttons, flash sense), and other detector or isolator cards.<br><br></details>

<details><summary><b>58.</b> What does the 242 in slot I14 provide?</summary><br>Flash Sense and Stop Time inputs to the controller.<br><br></details>

<details><summary><b>59.</b> What is in the PDA #2L?</summary><br>Signal circuit breakers, two 204 flashers, the SSR, HI and K24 relays, and the 206L 24 VDC power supply.<br><br></details>

<details><summary><b>60.</b> What is in Output File #1L?</summary><br>12 Model 200 switch packs, 4 flash transfer relays (FTRs), the 210 monitor, and the flash program blocks on the back.<br><br></details>

<details><summary><b>61.</b> What switches are on the police panel?</summary><br>Signals ON/OFF and AUTO/FLASH.<br><br></details>

<details><summary><b>62.</b> Does Signals OFF make the cabinet safe to work in?</summary><br>No. It only removes power from the heads. The PDA, service panel and the controller&#x27;s clean AC stay live.<br><br></details>

<details><summary><b>63.</b> What happens if the 210 monitor is removed and the door is closed?</summary><br>The cabinet goes into flash. This is by design.<br><br></details>

<details><summary><b>64.</b> How are the DC logic ground and AC wiring kept apart in a 332?</summary><br>The DC ground (white with a red stripe) runs separately from the AC wiring; AC neutral and equipment ground bond only at the service.<br><br></details>

<details><summary><b>65.</b> What changes in the service panel when a battery backup system (BBS) is installed?</summary><br>The #8 jumper on the TBS terminal block is removed, and the BBS can keep the cabinet live during a utility outage.<br><br></details>

## 7. Load switches, PDA and flash

<details><summary><b>66.</b> What does a Model 200 switch pack do?</summary><br>Three triac outputs switch 120 VAC to the field wires (R/Y/G or Don&#x27;t Walk/Yellow/Walk) when the controller pulls the 24 VDC inputs low.<br><br></details>

<details><summary><b>67.</b> How many switch packs does each PDA signal breaker feed?</summary><br>Three: a left turn, a through, and its ped phase.<br><br></details>

<details><summary><b>68.</b> What is the output order of a ped switch pack?</summary><br>Don&#x27;t Walk, Yellow (normally unused), Walk.<br><br></details>

<details><summary><b>69.</b> What do the flash transfer relays (FTRs) do?</summary><br>In normal operation they connect the switch packs to the field. In flash they drop out and connect the field to the 204 flashers.<br><br></details>

<details><summary><b>70.</b> What do the flash program blocks set?</summary><br>Whether each phase flashes red or yellow when the cabinet is in flash.<br><br></details>

<details><summary><b>71.</b> What flash rate does the CA MUTCD require?</summary><br>50 to 60 flashes per minute, with the light on for 1/2 to 2/3 of each cycle (4G.01).<br><br></details>

<details><summary><b>72.</b> Does flash come from the controller?</summary><br>No. It comes from the 204 flashers through the FTRs, so the cabinet can flash with the controller removed.<br><br></details>

<details><summary><b>73.</b> How do monitor-caused flash and police-panel flash differ when clearing?</summary><br>Monitor flash latches until someone resets the 210. Police-panel flash clears when the switch goes back to AUTO.<br><br></details>

<details><summary><b>74.</b> What failure is the main reason the 210 monitor exists?</summary><br>A shorted (failed-on) triac that lights a head when the controller says off.<br><br></details>

<details><summary><b>75.</b> How must drivers treat a dark (unpowered) signal in California?</summary><br>As an all-way stop (CVC 21800(d)).<br><br></details>

## 8. The 210 monitor and diode card

<details><summary><b>76.</b> What does the 210 conflict monitor do?</summary><br>Watches the field outputs on 16 channels and puts the intersection into flash if two conflicting channels are on together.<br><br></details>

<details><summary><b>77.</b> On the 210 program card, what does a diode in place mean?</summary><br>That pair of channels conflicts. You remove a diode only for a pair allowed to run together.<br><br></details>

<details><summary><b>78.</b> How many diodes are on a 16-channel card, and why?</summary><br>120: one per pair of channels, 16 × 15 ÷ 2.<br><br></details>

<details><summary><b>79.</b> What are 210 channels 9 to 16 used for?</summary><br>9 and 10: Overlaps A and B. 11 and 12: special. 13 to 16: Ø2, Ø4, Ø6 and Ø8 peds.<br><br></details>

<details><summary><b>80.</b> When is a ped channel compatible with a vehicle channel?</summary><br>Only if no vehicle on that phase drives or turns through the crosswalk.<br><br><sub>Ø1 (westbound left) stays in conflict with Ø2P, because it turns through that crosswalk.</sub><br><br></details>

<details><summary><b>81.</b> Besides conflicts, what else trips a 210?</summary><br>Low +24 VDC and a missing controller watchdog signal (CVM).<br><br></details>

<details><summary><b>82.</b> What is the worst mistake you can make on a diode card?</summary><br>Removing a diode for a pair that conflicts. The monitor will then not catch two conflicting greens.<br><br></details>

<details><summary><b>83.</b> What does a Model 2010 monitor add over a 210?</summary><br>Red-fail monitoring, minimum yellow checks and a fault log.<br><br></details>

<details><summary><b>84.</b> Why must a program card never move to another cabinet?</summary><br>Each card matches one intersection&#x27;s phasing.<br><br></details>

## 9. Conduit, cable, power and grounding

<details><summary><b>85.</b> What does a 12CSC serve, and how many does a pole need?</summary><br>The signal heads on one standard. One 12CSC per pole with heads, as long as the pole needs 12 or fewer conductors.<br><br></details>

<details><summary><b>86.</b> How do you count conductors needed in a 12CSC?</summary><br>3 per vehicle phase (R, Y, G) + 2 per ped phase (Walk, Don&#x27;t Walk) + 1 common.<br><br></details>

<details><summary><b>87.</b> What does a 3CSC serve?</summary><br>One push-button location.<br><br></details>

<details><summary><b>88.</b> How many cables does a conduit run carry?</summary><br>One cable for every pole beyond it, because signal cable runs unspliced from the cabinet to each pole. The run leaving the cabinet carries all of them.<br><br></details>

<details><summary><b>89.</b> What is the NEC conduit fill limit for three or more conductors?</summary><br>40% of the conduit&#x27;s inside area (NEC Chapter 9, Table 1). 53% for one conductor, 31% for two.<br><br></details>

<details><summary><b>90.</b> How many degrees of bends are allowed between pull points?</summary><br>360° total (for example NEC 352.26 for PVC).<br><br></details>

<details><summary><b>91.</b> Which conduit runs get an equipment ground or bonding conductor?</summary><br>Every run, including ones that carry only DLC or SIC.<br><br></details>

<details><summary><b>92.</b> How is the equipment grounding conductor sized?</summary><br>By the breaker ahead of the circuit (NEC 250.122): for example 20 A → #12, 30–60 A → #10, 100 A → #8 copper.<br><br></details>

<details><summary><b>93.</b> Why isn&#x27;t a ground rod by itself enough to protect people?</summary><br>The earth is not an effective fault path (NEC 250.4(A)(5)). The bonding conductor back to the service carries fault current so the breaker trips.<br><br></details>

<details><summary><b>94.</b> What resistance must a single ground rod meet?</summary><br>25 Ω or less, or a second electrode is added at least 6 ft away (NEC 250.53).<br><br></details>

<details><summary><b>95.</b> What voltage-drop limits does the NEC recommend?</summary><br>3% on a branch circuit and 5% total (informational note, not a requirement).<br><br></details>

<details><summary><b>96.</b> What color must the grounded (common) conductor be?</summary><br>White or gray (NEC 200.6).<br><br></details>

## 10. Safety

<details><summary><b>97.</b> What must you do before pulling a switch pack, FTR or monitor?</summary><br>Put the intersection into flash, under traffic control.<br><br></details>

<details><summary><b>98.</b> Why can a cabinet still be live after you open the utility breaker?</summary><br>A battery backup system (BBS) inverter can keep feeding it. Turn the BBS off and verify zero voltage.<br><br></details>

<details><summary><b>99.</b> What should you do before handling wires at a knocked-down pole?</summary><br>Open the signal and lighting breakers at the service and test before touching.<br><br></details>

<details><summary><b>100.</b> Which standard covers arc-flash PPE and verifying a safe work condition?</summary><br>NFPA 70E.<br><br></details>

<details><summary><b>101.</b> Which part of the CA MUTCD covers traffic control for work in the street?</summary><br>Part 6, temporary traffic control.<br><br></details>

<details><summary><b>102.</b> What is the danger of an ungrounded pole or cabinet?</summary><br>A fault can energize it without tripping a breaker, and a person touching it completes the circuit.<br><br></details>

<details><summary><b>103.</b> Why can opening a current-carrying coil be dangerous?</summary><br>Inductive kick: v = L × Δi/Δt. Interrupting 2 A in a 0.4 H coil in 1 ms makes about 800 V.<br><br></details>

---

*Generated by `tools/flashcards/build_decks.py` from the JSON file. Edit the JSON, not this page.*
