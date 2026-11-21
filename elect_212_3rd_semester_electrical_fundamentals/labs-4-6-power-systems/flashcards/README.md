# Flashcards — ELECT 212: Labs 4–6: Power Systems

43 cards. Read the question, answer it in your head, then click it to check.

Study guide for these cards: [study-guide.md](../study-guide.md).

- **Study online:** [flashcard page](https://webnrrd2k.github.io/lbcc-electrical-study-materials/flashcards/?deck=e212-power-systems): shuffle, flip, and mark the cards you know.
- **Download:** [Anki](power_systems.apkg) · [Quizlet import file](power_systems_quizlet.txt) (paste into Quizlet's Import box; images are not included) · [Emacs org-drill](power_systems.org) · [raw card data](power_systems.json)

## Contents

- [1. Split-phase 120/240 V](#1-split-phase-120240-v) (10)
- [2. Three-phase basics](#2-three-phase-basics) (6)
- [3. Wye systems](#3-wye-systems) (9)
- [4. Delta systems](#4-delta-systems) (9)
- [5. Three-phase power](#5-three-phase-power) (5)
- [6. Safety](#6-safety) (4)

---

## 1. Split-phase 120/240 V

<details><summary><b>1.</b> How is a 120/240 V single-phase three-wire system made?</summary><br>A transformer secondary with a grounded center tap. The center tap is the neutral; each end is a hot line.<br><br></details>

<details><summary><b>2.</b> Why is it 240 V between the two lines of a split-phase system?</summary><br>Each line is 120 V to neutral and the two are 180° apart, so they add to 240 V.<br><br></details>

<details><summary><b>3.</b> Which loads connect line to neutral, and which line to line?</summary><br>120 V loads (receptacles, lighting) line to neutral. 240 V loads (ranges, dryers, water heaters, A/C) line to line.<br><br></details>

<details><summary><b>4.</b> What current does the neutral of a split-phase system carry?</summary><br>The difference of the line currents: I_N = |I_L1 − I_L2|. Balanced loads give 0 A.<br><br></details>

<details><summary><b>5.</b> Worked: 15 A on L1 and 9 A on L2. Neutral current?</summary><br>15 − 9 = 6 A.<br><br></details>

<details><summary><b>6.</b> What is a multiwire branch circuit?</summary><br>Two or more hots with a voltage between them sharing one neutral (NEC Article 100).<br><br></details>

<details><summary><b>7.</b> What disconnect rule applies to a multiwire branch circuit?</summary><br>All the hots must open together: a 2-pole breaker or handle tie (NEC 210.4(B)).<br><br></details>

<details><summary><b>8.</b> What happens when the neutral of a split-phase circuit opens?</summary><br>The 120 V loads on opposite lines end up in series across 240 V. The smaller load (higher resistance) gets most of the voltage.<br><br></details>

<details><summary><b>9.</b> Worked: open neutral, 1000 W and 100 W 120 V lamps on opposite lines. Voltage on each?</summary><br>R = 14.4 Ω and 144 Ω; I = 240 ÷ 158.4 = 1.52 A. 1000 W lamp: about 22 V. 100 W lamp: about 218 V (burns out).<br><br></details>

<details><summary><b>10.</b> Why must a shared neutral not depend on a receptacle for continuity?</summary><br>Removing the device would open the neutral for the other circuit and cause open-neutral voltages (NEC 300.13(B)).<br><br></details>

## 2. Three-phase basics

<details><summary><b>11.</b> How far apart are the three voltages of a three-phase system?</summary><br>120°.<br><br></details>

<details><summary><b>12.</b> What is phase sequence (rotation)?</summary><br>The order in which the phases peak, for example A-B-C.<br><br></details>

<details><summary><b>13.</b> How do you reverse a three-phase motor?</summary><br>Swap any two of the three lines.<br><br></details>

<details><summary><b>14.</b> Give three reasons three-phase power is used.</summary><br>Smooth, constant power delivery; more power per pound of copper; three-phase motors are simpler and self-starting.<br><br></details>

<details><summary><b>15.</b> What is the difference between line values and phase values?</summary><br>Line values are measured between lines or in the line wires. Phase values are across (or through) one winding or one load.<br><br></details>

<details><summary><b>16.</b> What is the square root of 3, and when does it appear?</summary><br>About 1.732. It appears when converting between line and phase values, and in the three-phase power formula using line values.<br><br></details>

## 3. Wye systems

<details><summary><b>17.</b> In a wye, how do line and phase voltage compare?</summary><br>V_line = 1.732 × V_phase.<br><br></details>

<details><summary><b>18.</b> In a wye, how do line and phase current compare?</summary><br>They are equal.<br><br></details>

<details><summary><b>19.</b> Line-to-line voltage of a 120 V-per-phase wye?</summary><br>120 × 1.732 = 208 V.<br><br></details>

<details><summary><b>20.</b> Line-to-neutral voltage of a 480 V wye?</summary><br>480 ÷ 1.732 = 277 V.<br><br></details>

<details><summary><b>21.</b> Why is a 120 V wye 208 V line to line instead of 240 V?</summary><br>The two phase voltages are 120° apart, not 180°, so their phasor difference is 1.732 × 120.<br><br></details>

<details><summary><b>22.</b> What does the neutral carry on a balanced wye?</summary><br>0 A. The three phase currents cancel.<br><br></details>

<details><summary><b>23.</b> How do you find neutral current on an unbalanced resistive wye?</summary><br>I_N = √(Ia² + Ib² + Ic² − IaIb − IbIc − IcIa).<br><br></details>

<details><summary><b>24.</b> Worked: unbalanced wye, 10 A, 8 A and 6 A. Neutral current?</summary><br>√(100 + 64 + 36 − 80 − 48 − 60) = √12 ≈ 3.5 A.<br><br></details>

<details><summary><b>25.</b> Why can a wye neutral carry more current than the phases?</summary><br>Non-linear loads make triplen harmonics (3rd, 9th...) that add in the neutral instead of cancelling.<br><br></details>

## 4. Delta systems

<details><summary><b>26.</b> In a delta, how do line and phase voltage compare?</summary><br>They are equal.<br><br></details>

<details><summary><b>27.</b> In a delta, how do line and phase current compare?</summary><br>I_line = 1.732 × I_phase.<br><br></details>

<details><summary><b>28.</b> Worked: 240 V delta, each load draws 10 A. Line current?</summary><br>10 × 1.732 = 17.3 A.<br><br></details>

<details><summary><b>29.</b> Does a plain 3-wire delta have a neutral?</summary><br>No.<br><br></details>

<details><summary><b>30.</b> In a delta lab, where do you clamp to read phase amps versus line amps?</summary><br>Phase amps: around a load leg inside the delta. Line amps: around a feeder wire. Line amps are larger.<br><br></details>

<details><summary><b>31.</b> What is a high-leg (wild-leg) delta?</summary><br>A 240 V delta with one winding center-tapped for a neutral, giving 120/240 V four-wire service.<br><br></details>

<details><summary><b>32.</b> What voltage does the high leg read to neutral?</summary><br>About 208 V.<br><br></details>

<details><summary><b>33.</b> How must the high leg be identified, and where does it go in a panel?</summary><br>Marked orange (NEC 110.15), and on the B phase in panelboards (NEC 408.3(E)).<br><br></details>

<details><summary><b>34.</b> How much of three-transformer capacity can an open-delta bank carry?</summary><br>57.7%.<br><br></details>

## 5. Three-phase power

<details><summary><b>35.</b> Three-phase power formula using line values?</summary><br>P = 1.732 × V_line × I_line × PF.<br><br></details>

<details><summary><b>36.</b> Three-phase power formula using phase values?</summary><br>P = 3 × V_phase × I_phase × PF.<br><br></details>

<details><summary><b>37.</b> Worked: balanced 240 V delta heaters, 17.3 A per line, PF 1. Power?</summary><br>1.732 × 240 × 17.3 ≈ 7,200 W.<br><br></details>

<details><summary><b>38.</b> A 240 V heater runs on 208 V. About how much heat does it give?</summary><br>About 75%: power varies with voltage squared, (208/240)² ≈ 0.75.<br><br></details>

<details><summary><b>39.</b> What is apparent power in a three-phase circuit?</summary><br>S = 1.732 × V_line × I_line, in VA.<br><br></details>

## 6. Safety

<details><summary><b>40.</b> Why can&#x27;t you de-energize a multiwire circuit by turning off one breaker?</summary><br>The shared neutral still carries the other circuit&#x27;s current.<br><br></details>

<details><summary><b>41.</b> What is the danger of connecting a 120 V load on a high-leg delta?</summary><br>If it lands on the high leg it gets about 208 V.<br><br></details>

<details><summary><b>42.</b> Why measure every voltage combination on an unfamiliar system?</summary><br>Delta systems (ungrounded, corner-grounded or high-leg) can give unexpected line-to-ground readings.<br><br></details>

<details><summary><b>43.</b> What does an open neutral on a wye or split-phase service do to 120 V equipment?</summary><br>Applies unequal voltages, some near line-to-line, which destroys electronics and can start fires.<br><br></details>

---

*Generated by `tools/flashcards/build_decks.py` from the JSON file. Edit the JSON, not this page.*
