# Flashcards — Unit 20: Capacitance in AC Circuits

56 cards. Read the question, answer it in your head, then click it to check.

Study guide for this unit: [study-guide.md](../study-guide.md). The raw card data is in [`unit20_flashcards.json`](unit20_flashcards.json) if you want to import the cards into a flashcard app.

---

<details><summary><b>1.</b> Why are capacitors called the opposite of inductors?</summary><br>Almost every behaviour is reversed: Xc falls with frequency (Xl rises), current leads (Xl lags), Xc → ∞ at DC (Xl → 0).<br><br><sub>Intro</sub><br><br></details>

<details><summary><b>2.</b> Can current flow THROUGH a capacitor?</summary><br>No electrons cross the dielectric. But on AC, current flows continuously in the circuit as the capacitor charges, discharges and recharges — it "appears" to flow through.<br><img src="cap_ac_circuit.png"><br><br><sub>Review Q1</sub><br><br></details>

<details><summary><b>3.</b> <img src="tanks_analogy.png"><br>Explain the two-tank analogy.</summary><br>A reversing pump moves water back and forth between two tanks: flow never stops, but no water passes directly from tank to tank. Same as electrons charging each plate in turn.<br><br><sub>Figure 20–2</sub><br><br></details>

<details><summary><b>4.</b> Why does current "appear to flow" through a capacitor?</summary><br>Because the AC voltage continuously rises, falls and reverses, keeping the capacitor charging and discharging.<br><br><sub>Summary</sub><br><br></details>

<details><summary><b>5.</b> Does a capacitor block AC or DC?</summary><br>It blocks steady DC (after charging) and passes AC — more easily at higher frequency.<br><br></details>

<details><summary><b>6.</b> What is the impressed voltage?</summary><br>The voltage built up across the plates by the stored charge. It opposes the applied voltage and limits current.<br><img src="impressed_180.png"><br><br><sub>20–2</sub><br><br></details>

<details><summary><b>7.</b> <img src="impressed_180.png"><br>Phase relationship of impressed and applied voltage?</summary><br>180° apart.<br><br></details>

<details><summary><b>8.</b> What is capacitive reactance?</summary><br>The current-limiting effect of a capacitor (its countervoltage), symbol Xc, measured in ohms.<br><br></details>

<details><summary><b>9.</b> Formula for Xc?</summary><br>Xc = 1 / (2πfC)  (f in Hz, C in farads)<br><br><sub>At 60 Hz: Xc = 1/(377C)</sub><br><br></details>

<details><summary><b>10.</b> Rearranged Xc formulas?</summary><br>C = 1 / (2πf·Xc) and f = 1 / (2πC·Xc)<br><br></details>

<details><summary><b>11.</b> Two factors that determine capacitive reactance?</summary><br>Capacitance and frequency — Xc is INVERSELY proportional to both.<br><img src="xc_vs_frequency.png"><br><br><sub>Review Q2</sub><br><br></details>

<details><summary><b>12.</b> 35 µF on 120 V, 60 Hz: Xc and current?</summary><br>Xc = 1/(377 × 0.000035) = <b>75.79 Ω</b>; I = 120/75.79 = <b>1.58 A</b>.<br><br><sub>Example 20–1</sub><br><br></details>

<details><summary><b>13.</b> 480 V, 60 Hz, 2.6 A: capacitance?</summary><br>Xc = 480/2.6 = 184.6 Ω; C = 1/(377 × 184.6) = <b>14.37 µF</b>.<br><br><sub>Example 20–2</sub><br><br></details>

<details><summary><b>14.</b> Most common Xc calculation error?</summary><br>Leaving C in µF instead of converting to farads (35 µF = 0.000035 F). Also forgetting the reciprocal (1/x).<br><br></details>

<details><summary><b>15.</b> Xc of a capacitor at DC?</summary><br>Infinite — it blocks steady DC (opposite of an inductor, whose Xl = 0 at DC).<br><br></details>

<details><summary><b>16.</b> Frequency doubles. What happens to Xc and current?</summary><br>Xc halves; current doubles.<br><img src="xc_vs_frequency.png"><br><br><sub>20–8</sub><br><br></details>

<details><summary><b>17.</b> <img src="charge_rate_freq.png"><br>Why does Xc drop as frequency rises?</summary><br>Current is charge per second (I = Q/t). At higher frequency the same charge moves in less time, so more current flows for the same voltage.<br><br><sub>30 Hz → 1 C/s; 60 Hz → 2 C/s</sub><br><br></details>

<details><summary><b>18.</b> 300 Ω at 60 Hz. Xc at 100 Hz?</summary><br>300 × 60/100 = <b>180 Ω</b><br><br><sub>Practice 6</sub><br><br></details>

<details><summary><b>19.</b> Book table error check: 470 nF at 400 Hz?</summary><br><b>846.6 Ω</b> (the book's Table 20–1 says kΩ). Also 470 nF @ 1 kHz = 338.6 Ω and 750 nF @ 400 Hz = 530.5 Ω.<br><br></details>

<details><summary><b>20.</b> Phase of current vs voltage in a pure capacitive circuit?</summary><br>Current LEADS the applied voltage by 90°.<br><img src="lead_90.png"><br><br><sub>Review Q3/Q4</sub><br><br></details>

<details><summary><b>21.</b> What does "ELI the ICE man" say about capacitors?</summary><br>ICE: in a capacitor (C), current (I) comes before voltage (E).<br><img src="r_l_c_phase.png"><br><br></details>

<details><summary><b>22.</b> <img src="lead_90.png"><br>Why is capacitor current maximum when voltage is zero?</summary><br>Current depends on how fast the charge changes. At 0° the voltage (and charge) is changing fastest; at 90° it's at peak and momentarily not changing, so current = 0.<br><br><sub>Q = C × V</sub><br><br></details>

<details><summary><b>23.</b> <img src="r_l_c_phase.png"><br>Compare phase in R, L and C circuits.</summary><br>R: in phase. L: current lags 90°. C: current leads 90°.<br><br></details>

<details><summary><b>24.</b> Charge on a capacitor vs applied voltage?</summary><br>In phase: Q = C × V, so charge is zero when voltage is zero and peaks when voltage peaks.<br><br></details>

<details><summary><b>25.</b> True power in a pure capacitive circuit?</summary><br>Zero watts — energy stored while charging is returned while discharging.<br><img src="power_capacitive.png"><br><br><sub>20–5</sub><br><br></details>

<details><summary><b>26.</b> <img src="power_capacitive.png"><br>What do the gold and red areas represent?</summary><br>Gold: V and I same sign — charging, storing energy in the electrostatic field. Red: opposite signs — discharging, returning energy.<br><br></details>

<details><summary><b>27.</b> Why does P = E × I × cos θ give zero for a pure capacitor?</summary><br>θ = 90° and cos 90° = 0.<br><br></details>

<details><summary><b>28.</b> What unit is capacitor power measured in?</summary><br>VARs (volt-amperes-reactive), written VARsC.<br><br></details>

<details><summary><b>29.</b> Formulas for VARsC?</summary><br>VARsC = Ec × Ic = Ic² × Xc = Ec² / Xc<br><br></details>

<details><summary><b>30.</b> How are capacitive and inductive VARs related?</summary><br>180° out of phase — they cancel each other.<br><img src="vars_opposite.png"><br><br><sub>Basis of power-factor correction</sub><br><br></details>

<details><summary><b>31.</b> <img src="vars_opposite.png"><br>Why do plants install capacitor banks rated in kVAR?</summary><br>Their leading (capacitive) VARs cancel the motors' lagging (inductive) VARs, so the utility supplies less current and PF improves.<br><br></details>

<details><summary><b>32.</b> Q of a capacitor: formula?</summary><br>Q = R / Xc, where R is the dielectric's (leakage) resistance.<br><img src="cap_q_model.png"><br><br><sub>Flipped from an inductor's Q = Xl/R</sub><br><br></details>

<details><summary><b>33.</b> Other Q formulas for a capacitor?</summary><br>Q = VARsC / P, and approximately Q ≈ 1/PF (accurate when Q is high).<br><br></details>

<details><summary><b>34.</b> Is a capacitor's Q usually high or low? What lowers it?</summary><br>Very high. A leaky dielectric (lower R) lowers Q.<br><br></details>

<details><summary><b>35.</b> What is a capacitor's voltage rating really the rating of?</summary><br>The dielectric.<br><br><sub>20–7</sub><br><br></details>

<details><summary><b>36.</b> A nonpolarized capacitor is marked in VAC. What value is that?</summary><br>RMS — compare directly with the circuit's RMS voltage.<br><br></details>

<details><summary><b>37.</b> Marked VDC, WVDC or PEAK. How do you use it on AC?</summary><br>It's a PEAK value: compare it with the circuit's RMS × 1.414.<br><img src="voltage_rating.png"><br><br></details>

<details><summary><b>38.</b> How are electrolytic (polarized) capacitors rated?</summary><br>Always in DC volts.<br><br></details>

<details><summary><b>39.</b> <img src="voltage_rating.png"><br>300 WVDC capacitor on a 240 V line. OK?</summary><br>No: 240 × 1.414 = 339 V peak, which exceeds 300 V.<br><br><sub>Example 20–3</sub><br><br></details>

<details><summary><b>40.</b> 600 VDC capacitor on 480 VAC. OK?</summary><br>No: 480 × 1.414 ≈ 679 V peak > 600 V.<br><br><sub>Review Q7 / Practical App 1</sub><br><br></details>

<details><summary><b>41.</b> A 350 VAC capacitor is equivalent to what DC rating?</summary><br>About 350 × 1.414 ≈ 495 V peak (DC).<br><br><sub>Review Q10</sub><br><br></details>

<details><summary><b>42.</b> Life gain at half the rated voltage?</summary><br>About 8×.<br><br><sub>Review Q8</sub><br><br></details>

<details><summary><b>43.</b> Is there a standard for how capacitor voltage ratings are marked?</summary><br>No — you'll see VOLTS AC, VOLTS DC, PEAK VOLTS and WVDC. Read the label carefully.<br><br></details>

<details><summary><b>44.</b> In series, how do capacitive REACTANCES combine?</summary><br>They add: Xct = Xc1 + Xc2 + Xc3 (same angle).<br><img src="series_caps_example.png"><br><br><sub>Capacitance uses reciprocals</sub><br><br></details>

<details><summary><b>45.</b> In parallel, how do capacitive REACTANCES combine?</summary><br>Reciprocal formula: 1/Xct = 1/Xc1 + 1/Xc2 + 1/Xc3.<br><img src="parallel_caps_example.png"><br><br><sub>Capacitance adds</sub><br><br></details>

<details><summary><b>46.</b> <img src="series_caps_example.png"><br>10, 30, 15 µF in series on 480 V, 60 Hz. Xct, Ct and I?</summary><br>Xct = 265 + 88 + 177 = <b>530.5 Ω</b>; Ct = <b>5 µF</b>; I = <b>0.905 A</b>.<br><br><sub>Example 20–4</sub><br><br></details>

<details><summary><b>47.</b> In that series circuit, which capacitor has the largest voltage drop?</summary><br>The smallest one (10 µF): 240 V. Drops are 240, 80, 160 V.<br><br><sub>Check each cap's rating</sub><br><br></details>

<details><summary><b>48.</b> Do the series capacitor voltage drops add straight?</summary><br>Yes — all capacitor drops are in phase with each other (240 + 80 + 160 = 480 V).<br><br><sub>Unlike R + L drops</sub><br><br></details>

<details><summary><b>49.</b> <img src="parallel_caps_example.png"><br>50, 75, 20 µF in parallel, 787 VARs at 60 Hz. Find E.</summary><br>Xct = 18.29 Ω; E = √(VARs × Xct) = √(787 × 18.29) ≈ <b>120 V</b>.<br><br><sub>Example 20–5</sub><br><br></details>

<details><summary><b>50.</b> Formula for E from VARs and reactance?</summary><br>E = √(VARs × X)<br><br></details>

<details><summary><b>51.</b> Do VARs from several capacitors add?</summary><br>Yes — same-type VARs add straight in series or parallel.<br><br></details>

<details><summary><b>52.</b> Capacitor drawn onto a higher voltage than rated: two effects?</summary><br>VARs rise with V² (480 → 600 V ≈ +56% kVAR) and the dielectric is overstressed.<br><br></details>

<details><summary><b>53.</b> Why can PF capacitors overheat on VFD/electronic systems?</summary><br>Their Xc drops at harmonic frequencies, so they draw extra harmonic current and can resonate with system inductance.<br><br><sub>Detuned PF banks</sub><br><br></details>

<details><summary><b>54.</b> Field formula to check a run capacitor at 60 Hz?</summary><br>C (µF) ≈ 2652 × I ÷ E (current through it, voltage across it).<br><br></details>

<details><summary><b>55.</b> Add a series capacitor to reduce current from 24 A to 16 A on 480 V. Method?</summary><br>Existing Xc = 480/24; needed total = 480/16; series Xc's add, so the new cap supplies the difference in Xc. Convert that Xc to µF.<br><br><sub>Practice 7</sub><br><br></details>

<details><summary><b>56.</b> Four equal capacitors in series must total 20 µF. Value of each?</summary><br>C/N = 20 µF → each = 80 µF; each sees ¼ of the line voltage.<br><br><sub>Review Q11–12</sub><br><br></details>
