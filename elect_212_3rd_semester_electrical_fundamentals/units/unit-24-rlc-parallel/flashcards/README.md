# Flashcards — Unit 24: R-L-C Parallel Circuits

49 cards. Read the question, answer it in your head, then click it to check.

Study guide for this unit: [study-guide.md](../study-guide.md). The raw card data is in [`unit24_flashcards.json`](unit24_flashcards.json) if you want to import the cards into a flashcard app.

---

<details><summary><b>1.</b> What is shared by all branches of an RLC parallel circuit?</summary><br>The voltage.<br><img src="rlc_parallel_circuit.png"><br><br><sub>Summary</sub><br><br></details>

<details><summary><b>2.</b> Phase of each branch current vs voltage?</summary><br>Resistor: in phase. Inductor: lags 90°. Capacitor: leads 90°.<br><img src="branch_phases.png"><br><br><sub>Summary</sub><br><br></details>

<details><summary><b>3.</b> <img src="branch_phases.png"><br>How are Iₗ and Ic related in parallel?</summary><br>180° apart — they subtract (cancel).<br><br></details>

<details><summary><b>4.</b> When is a parallel RLC circuit lagging vs leading?</summary><br>More inductive VARs/current → lagging. More capacitive → leading.<br><br></details>

<details><summary><b>5.</b> In parallel, does the bigger or smaller reactance win?</summary><br>The SMALLER reactance draws more current and dominates (reverse of series).<br><br><sub>Xl 8 Ω vs Xc 16 Ω → inductive</sub><br><br></details>

<details><summary><b>6.</b> <img src="rlc_parallel_circuit.png"><br>Branch currents for 12 Ω ∥ Xl 8 Ω ∥ Xc 16 Ω on 240 V?</summary><br>Iᵣ 20 A, Iₗ 30 A, Ic 15 A.<br><br><sub>Example 24–1</sub><br><br></details>

<details><summary><b>7.</b> Total current formula for RLC parallel?</summary><br>Iₜ = √(Iᵣ² + (Iₗ − Ic)²)<br><img src="current_triangle_rlc.png"><br><br></details>

<details><summary><b>8.</b> <img src="current_cancel.png"><br>Iᵣ 20, Iₗ 30, Ic 15 A. Iₜ?</summary><br>√(20² + 15²) = <b>25 A</b><br><br></details>

<details><summary><b>9.</b> <img src="branch_exceeds_line.png"><br>Can a branch carry more current than the line?</summary><br>Yes — the 30 A coil branch exceeds the 25 A line current, because Ic cancels part of Iₗ.<br><br></details>

<details><summary><b>10.</b> Iᵣ 38, Iₗ 22, Ic 7 A. Iₜ?</summary><br>√(38² + 15²) ≈ <b>40.9 A</b><br><br><sub>Review Q3</sub><br><br></details>

<details><summary><b>11.</b> Simplest way to find Z in RLC parallel?</summary><br>Z = E / Iₜ = 240 / 25 = <b>9.6 Ω</b><br><br></details>

<details><summary><b>12.</b> Reciprocal formula for RLC parallel impedance?</summary><br>Z = 1 / √((1/R)² + (1/Xl − 1/Xc)²)<br><br><sub>Subtract the RECIPROCALS of Xl and Xc</sub><br><br></details>

<details><summary><b>13.</b> Second impedance method (combine reactances first)?</summary><br>X = Xl·Xc / (Xl + Xc) with Xc NEGATIVE; then Z = R·X/√(R² + X²). 8×(−16)/(8−16) = 16 Ω → Z = 9.6 Ω.<br><br><sub>Positive X = inductive</sub><br><br></details>

<details><summary><b>14.</b> Example 24–2: R 18 Ω, 9.76 mH, 5.5 µF at 1200 Hz. First step and Z?</summary><br>Xl = 73.59 Ω, Xc = 24.11 Ω (377 doesn't apply); Z ≈ <b>16.1 Ω</b>.<br><br><sub>Book's substitution shows a 74.589 typo</sub><br><br></details>

<details><summary><b>15.</b> Power values in Example 24–1?</summary><br>P 4800 W; VARsL 7200; VARsC 3600; VA 6000.<br><br></details>

<details><summary><b>16.</b> Apparent power formula for RLC parallel?</summary><br>VA = √(P² + (VARsL − VARsC)²)<br><br></details>

<details><summary><b>17.</b> Example 24–1 PF and θ?</summary><br>PF = 4800/6000 = 80% LAGGING; θ = 36.87°.<br><br></details>

<details><summary><b>18.</b> PF formulas in parallel RLC?</summary><br>P/VA, Iᵣ/Iₜ, Z/R<br><br><sub>Not R/Z, not voltage ratios</sub><br><br></details>

<details><summary><b>19.</b> L and C in Example 24–1?</summary><br>L = 8/377 = 0.0212 H; C = 1/(377 × 16) = 165.8 µF.<br><br></details>

<details><summary><b>20.</b> What is a tank circuit?</summary><br>An L-C parallel (resonant) circuit, in which energy swings back and forth between the coil and capacitor.<br><img src="tank_circuit.png"><br><br></details>

<details><summary><b>21.</b> At parallel resonance, what happens to impedance and line current?</summary><br>Impedance is MAXIMUM; line current is MINIMUM.<br><img src="tank_resonance_curves.png"><br><br><sub>Opposite of series resonance</sub><br><br></details>

<details><summary><b>22.</b> <img src="series_vs_parallel_resonance.png"><br>Compare series and parallel resonance.</summary><br>Series: Z min, current max, voltage magnified. Parallel: Z max, line current min, circulating current magnified.<br><br></details>

<details><summary><b>23.</b> What limits the line current of a real tank circuit?</summary><br>The resistance (Q) of the coil — capacitors have very high Q.<br><br><sub>Ideal: zero line current, infinite Z</sub><br><br></details>

<details><summary><b>24.</b> Q of a tank circuit — two formulas?</summary><br>Q = Xl/R = I(tank)/I(line)<br><br></details>

<details><summary><b>25.</b> <img src="tank_circuit.png"><br>0.0398 H (10 Ω), 0.442 µF on 480 V at 1200 Hz: tank current, Q and line current?</summary><br>Xl = Xc = 300 Ω → 1.6 A each; Q = 30; line = 1.6/30 = <b>0.0533 A</b>.<br><br></details>

<details><summary><b>26.</b> Check the tank line current using power.</summary><br>P = 1.6² × 10 = 25.6 W; I = 25.6/480 = 0.0533 A.<br><br></details>

<details><summary><b>27.</b> Impedance of that tank at resonance?</summary><br>480/0.0533 ≈ <b>9000 Ω</b> (book's 9006 comes from rounding).<br><br></details>

<details><summary><b>28.</b> Tank Xl = Xc = 30 Ω, coil Q = 15, 277 V. Line current?</summary><br>Tank = 277/30 ≈ 9.23 A; line = 9.23/15 ≈ <b>0.62 A</b>.<br><br><sub>Review Q4</sub><br><br></details>

<details><summary><b>29.</b> Bandwidth of a parallel resonant circuit?</summary><br>Frequency range where impedance is ≥ 0.707 × maximum; high Q = narrow, low Q = wide.<br><br></details>

<details><summary><b>30.</b> Pitfall: "tiny line current, so L and C are lightly loaded"?</summary><br>Wrong — each carries the full circulating tank current (Q × line current).<br><br></details>

<details><summary><b>31.</b> <img src="induction_heater.png"><br>How does an induction heater use a tank circuit?</summary><br>The work coil (with the pipe as core) and a capacitor resonate; I(tank) = Q × I(line) — Q 10: 100 A line → 1000 A heating current.<br><br></details>

<details><summary><b>32.</b> <img src="induction_heating_depth.png"><br>Induction heating: low vs high frequency?</summary><br>≤ 400 Hz heats evenly through; ≥ 1000 Hz skin effect heats the surface (case hardening).<br><br></details>

<details><summary><b>33.</b> Why is an induction heater only resonant with the part in the coil?</summary><br>The part acts as the coil's core, so it changes L.<br><br></details>

<details><summary><b>34.</b> How does an inductive proximity sensor use a tank circuit?</summary><br>Metal near the face adds eddy-current losses, Q collapses, the oscillation stops, and the sensor switches.<br><br></details>

<details><summary><b>35.</b> C to resonate with 0.796 mH (Xl 50 Ω) at 10 kHz?</summary><br>Xc must = 50 Ω: C = 1/(2π × 10,000 × 50) ≈ <b>0.318 µF</b>.<br><br><sub>Review Q5</sub><br><br></details>

<details><summary><b>36.</b> <img src="pf_correction_circuit.png"><br>Why can a capacitor correct a motor's power factor?</summary><br>In parallel, its leading current cancels much of the motor's lagging magnetizing current, so the line carries less.<br><br></details>

<details><summary><b>37.</b> <img src="motor_load_model.png"><br>How does a motor look electrically at no load vs full load?</summary><br>R in series with L; L (magnetizing) stays ~constant, R grows with load → low PF at no load, higher at full load.<br><br></details>

<details><summary><b>38.</b> PF correction step 1–2 (240 V, 10 A, 1630 W)?</summary><br>VA = 2400; PF = 67.9%; VARsL = √(2400² − 1630²) = 1761.6.<br><br></details>

<details><summary><b>39.</b> PF correction step 3–4 (target 95%)?</summary><br>New VA = 1630/0.95 = 1715.8; allowed VARs = √(1715.8² − 1630²) = 535.8.<br><br><sub>Watts don't change</sub><br><br></details>

<details><summary><b>40.</b> PF correction step 5–7?</summary><br>VARsC = 1761.6 − 535.8 = 1225.8; Xc = 240²/1225.8 = 46.99 Ω; C = 1/(377 × 46.99) = <b>56.45 µF</b> in parallel.<br><img src="pf_correction_triangles.png"><br><br></details>

<details><summary><b>41.</b> <img src="pf_correction_triangles.png"><br>After correcting that motor to 95%, what's the line current?</summary><br>≈ 1715.8/240 = <b>7.15 A</b> (down from 10 A). The motor's own current is unchanged.<br><br></details>

<details><summary><b>42.</b> Formula for Xc from required capacitive VARs?</summary><br>Xc = E² / VARsC<br><br></details>

<details><summary><b>43.</b> To correct to unity (100%), how many VARsC?</summary><br>Equal to all the existing inductive VARs.<br><br><sub>Review Q6</sub><br><br></details>

<details><summary><b>44.</b> Why correct to ~95% rather than 100%?</summary><br>Diminishing returns — each extra point needs more kVAR; overshooting makes PF leading and raises voltage.<br><br></details>

<details><summary><b>45.</b> Does corrected PF stay constant at all motor loads?</summary><br>No (despite the book). Watts drop at light load, so PF falls; an oversized capacitor can overcorrect.<br><br></details>

<details><summary><b>46.</b> Book error in PF correction step 5?</summary><br>It says reduce VARs "from 1715.789" — that's VA. The existing VARs are 1761.562. Also "PF = 0679" should be 0.679.<br><br></details>

<details><summary><b>47.</b> NEC limits for a capacitor on the load side of a motor overload?</summary><br>kVAR ≤ the amount to raise no-load PF to unity (460.7, avoids self-excitation); set overloads on the reduced current (460.9).<br><br></details>

<details><summary><b>48.</b> Why can PF banks cause harmonic problems in plants with drives?</summary><br>Bank + system inductance form a tank circuit; near a harmonic its high impedance magnifies harmonic voltage/current. Use detuned banks.<br><br></details>

<details><summary><b>49.</b> Practical: 240 V, 15 A, 2.2 kW motor to 95%. Method?</summary><br>VA = 3600 → PF ≈ 61%; VARs now = √(3600² − 2200²); target VA = 2200/0.95; VARs target; difference = VARsC; Xc = 240²/VARsC; C = 1/(377·Xc).<br><br></details>
