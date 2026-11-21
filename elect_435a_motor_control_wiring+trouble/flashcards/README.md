# Flashcards — ELECT 435A: Motor Control Basics

53 cards. Read the question, answer it in your head, then click it to check.

- **Study online:** [flashcard page](https://webnrrd2k.github.io/lbcc-electrical-study-materials/flashcards/?deck=e435a-motor-control): shuffle, flip, and mark the cards you know.
- **Download:** [Anki](motor_control.apkg) · [Quizlet import file](motor_control_quizlet.txt) (paste into Quizlet's Import box; images are not included) · [Emacs org-drill](motor_control.org) · [raw card data](motor_control.json)

## Contents

- [1. Components](#1-components) (10)
- [2. Terminal numbers](#2-terminal-numbers) (10)
- [3. Ladder diagrams and circuits](#3-ladder-diagrams-and-circuits) (15)
- [4. Wiring practice](#4-wiring-practice) (9)
- [5. Testing and troubleshooting](#5-testing-and-troubleshooting) (9)

---

## 1. Components

<details><summary><b>1.</b> What is a contactor?</summary><br>A heavy-duty electrically operated switch. Its coil pulls in main power contacts that carry motor current.<br><br></details>

<details><summary><b>2.</b> What is the difference between a contactor and a motor starter?</summary><br>A motor starter is a contactor plus an overload relay.<br><br></details>

<details><summary><b>3.</b> What does an overload relay protect against?</summary><br>Motor overheating from sustained overcurrent. It opens the control circuit; it does not protect against short circuits.<br><br></details>

<details><summary><b>4.</b> What protects the motor circuit against short circuits?</summary><br>The branch-circuit short-circuit and ground-fault device: fuses or a circuit breaker ahead of the starter.<br><br></details>

<details><summary><b>5.</b> What is a control relay used for?</summary><br>Switching low-current control signals and adding contacts. It does not carry motor current.<br><br></details>

<details><summary><b>6.</b> What does a control transformer do?</summary><br>Steps line voltage down to a safer control voltage (24 V in the lab panels) for the push buttons, coils and lights.<br><br></details>

<details><summary><b>7.</b> What is a limit switch used for in a forward/reverse circuit?</summary><br>It opens when the machine reaches the end of travel and drops out that direction only.<br><br></details>

<details><summary><b>8.</b> What is a pilot light for?</summary><br>Showing the operator a state, such as motor running forward.<br><br></details>

<details><summary><b>9.</b> What does the FLA dial on an overload relay set?</summary><br>The trip current. Set it to the motor nameplate full-load amps.<br><br></details>

<details><summary><b>10.</b> What is the difference between HAND and AUTO reset on an overload?</summary><br>HAND: someone must press reset after a trip. AUTO: it resets itself when it cools. Use HAND where an automatic restart could hurt someone.<br><br></details>

## 2. Terminal numbers

<details><summary><b>11.</b> What are terminals A1 and A2?</summary><br>The two ends of a contactor or relay coil.<br><br></details>

<details><summary><b>12.</b> What do 1L1, 3L2, 5L3 and 2T1, 4T2, 6T3 mean on a contactor?</summary><br>Line-side and load-side terminals of the three main power poles: 1L1 to 2T1, 3L2 to 4T2, 5L3 to 6T3.<br><br></details>

<details><summary><b>13.</b> What do the units digits 1-2 and 3-4 tell you about an auxiliary contact?</summary><br>1-2 is normally closed (NC); 3-4 is normally open (NO). The tens digit is the position number.<br><br></details>

<details><summary><b>14.</b> Is aux contact 23-24 NO or NC?</summary><br>Normally open (ends in 3-4).<br><br></details>

<details><summary><b>15.</b> Is aux contact 31-32 NO or NC?</summary><br>Normally closed (ends in 1-2).<br><br></details>

<details><summary><b>16.</b> What are overload terminals 95-96 and 97-98?</summary><br>95-96 is the normally closed trip contact wired in series with the coils. 97-98 is a normally open alarm contact.<br><br></details>

<details><summary><b>17.</b> A push button&#x27;s NC contact is usually numbered...?</summary><br>1-2 (for example a STOP button).<br><br></details>

<details><summary><b>18.</b> A push button&#x27;s NO contact is usually numbered...?</summary><br>3-4 (for example a START button).<br><br></details>

<details><summary><b>19.</b> On an 8-pin octal relay, which pins are usually the coil?</summary><br>Pins 2 and 7.<br><br></details>

<details><summary><b>20.</b> What do H1-H4 and X1-X4 mean on a control transformer?</summary><br>H terminals are the primary (high-voltage) side; X terminals are the secondary (low-voltage) side.<br><br></details>

## 3. Ladder diagrams and circuits

<details><summary><b>21.</b> How is a ladder diagram read?</summary><br>Left to right across each rung, top to bottom. Power rails on the sides; one load (coil or light) per rung, at the right end.<br><br></details>

<details><summary><b>22.</b> Where do the overload contacts go in a control rung?</summary><br>In series with the coil, between the coil and the common side.<br><br></details>

<details><summary><b>23.</b> What is a seal-in (holding) contact?</summary><br>A normally open contact of the contactor wired across the START button, so the coil stays energized after START is released.<br><br></details>

<details><summary><b>24.</b> What is 3-wire control?</summary><br>Momentary START/STOP buttons with a seal-in contact. It gives low-voltage protection: after a power loss the motor does not restart by itself.<br><br></details>

<details><summary><b>25.</b> What is 2-wire control?</summary><br>A maintained contact (switch, float, thermostat) runs the coil directly. It gives low-voltage release: the motor restarts when power returns.<br><br></details>

<details><summary><b>26.</b> How are multiple STOP buttons wired?</summary><br>In series (any one opens the circuit).<br><br></details>

<details><summary><b>27.</b> How are multiple START buttons wired?</summary><br>In parallel (any one can start).<br><br></details>

<details><summary><b>28.</b> What does jog (inch) mean?</summary><br>The motor runs only while the button is held; the seal-in is bypassed.<br><br></details>

<details><summary><b>29.</b> Why should a JOG circuit still be fed through STOP?</summary><br>So pressing STOP always stops the motor, even while someone is holding JOG.<br><br></details>

<details><summary><b>30.</b> What is electrical interlocking in a forward/reverse starter?</summary><br>Each contactor&#x27;s NC aux contact (for example 31-32) is wired in series with the other contactor&#x27;s coil, so both can&#x27;t pull in at once.<br><br></details>

<details><summary><b>31.</b> What is mechanical interlocking?</summary><br>A mechanical bar between the two contactors that physically prevents both from closing.<br><br></details>

<details><summary><b>32.</b> What is push-button interlocking?</summary><br>Each direction button&#x27;s NC contact is in the other direction&#x27;s rung, so pressing one drops out the other.<br><br></details>

<details><summary><b>33.</b> How does a 3-phase motor reverse?</summary><br>Swap any two of the three line leads (the reversing contactor swaps L1 and L3).<br><br></details>

<details><summary><b>34.</b> Why must forward and reverse never pull in together?</summary><br>Two lines would be shorted together phase to phase.<br><br></details>

<details><summary><b>35.</b> What is a common forgotten wire on a starter?</summary><br>The coil return: coil A2 to the overload 95 terminal. Without it the coil has no path and nothing pulls in.<br><br></details>

## 4. Wiring practice

<details><summary><b>36.</b> NFPA 79 wire color for AC control circuits?</summary><br>Red.<br><br></details>

<details><summary><b>37.</b> NFPA 79 wire color for DC control circuits?</summary><br>Blue.<br><br></details>

<details><summary><b>38.</b> NFPA 79 wire color for the grounded (common) control conductor?</summary><br>White (or white with a stripe for DC).<br><br></details>

<details><summary><b>39.</b> NFPA 79 wire color for equipment grounding?</summary><br>Green, or green with yellow stripe.<br><br></details>

<details><summary><b>40.</b> What color does NFPA 79 use for interlock circuits fed from an outside source?</summary><br>Orange (or yellow), because they stay live when the panel disconnect is off.<br><br></details>

<details><summary><b>41.</b> Why should a white wire be used only for the grounded conductor?</summary><br>Workers assume white is near ground potential. A white wire upstream of the overload contact can read full control voltage when the overload trips.<br><br></details>

<details><summary><b>42.</b> Why is one side of the control transformer secondary grounded?</summary><br>So a ground fault in the control circuit blows the fuse or trips the breaker instead of starting the motor by itself.<br><br></details>

<details><summary><b>43.</b> Which side of the control circuit goes to the push buttons and contacts?</summary><br>The fused, ungrounded (hot) side. The grounded side goes to the coils&#x27; A2 ends through the overload contacts.<br><br></details>

<details><summary><b>44.</b> Why give every wire a number at both ends?</summary><br>So the panel matches the ladder diagram and anyone can trace a fault.<br><br></details>

## 5. Testing and troubleshooting

<details><summary><b>45.</b> What must be off before doing ohm or continuity checks on a control panel?</summary><br>All power: cord unplugged, motor supply unplugged, control breaker off.<br><br></details>

<details><summary><b>46.</b> Why are continuity checks useless with the control transformer still connected and switched on?</summary><br>The transformer secondary joins the hot and common buses through a few ohms, so almost everything reads continuous.<br><br></details>

<details><summary><b>47.</b> What should a contactor coil read on an ohmmeter?</summary><br>A definite resistance: not zero (shorted) and not open.<br><br></details>

<details><summary><b>48.</b> How do you bench-test a contactor&#x27;s main contacts without power?</summary><br>Push the armature in by hand and check each pole (1L1-2T1 and so on) goes from open to continuous.<br><br></details>

<details><summary><b>49.</b> A motor starts but stops as soon as START is released. Most likely cause?</summary><br>The seal-in (holding) contact is missing, miswired or not closing.<br><br></details>

<details><summary><b>50.</b> Pressing START does nothing at all. What do you check first?</summary><br>Control power, the STOP button and overload contact (both NC), and the coil return wire.<br><br></details>

<details><summary><b>51.</b> An overload keeps tripping. What are common causes?</summary><br>FLA set too low, a mechanically overloaded or binding motor, a lost phase (single-phasing), or a bad connection heating the overload.<br><br></details>

<details><summary><b>52.</b> What is single-phasing?</summary><br>Losing one line of a 3-phase supply. The motor draws high current on the other two lines and overheats.<br><br></details>

<details><summary><b>53.</b> What is the safe way to check for voltage?</summary><br>Test your meter on a known live source, test the circuit, then test the meter again (live-dead-live).<br><br></details>

---

*Generated by `tools/flashcards/build_decks.py` from the JSON file. Edit the JSON, not this page.*
