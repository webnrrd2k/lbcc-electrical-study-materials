# Flashcards — Unit 23: R-L-C Series Circuits

46 cards. Read the question, answer it in your head, then click it to check.

Study guide for this unit: [study-guide.md](../study-guide.md). The raw card data is in [`unit23_flashcards.json`](unit23_flashcards.json) if you want to import the cards into a flashcard app.

---

<details><summary><b>1.</b> Phase of the resistor's voltage vs the series current?</summary><br>In phase.<br><img src="drop_phases.png"><br><br><sub>Review Q1</sub><br><br></details>

<details><summary><b>2.</b> Phase of the inductor's voltage vs the series current?</summary><br>Eₗ LEADS the current by 90°.<br><img src="drop_phases.png"><br><br><sub>Review Q2</sub><br><br></details>

<details><summary><b>3.</b> Phase of the capacitor's voltage vs the series current?</summary><br>Ec LAGS the current by 90°.<br><img src="drop_phases.png"><br><br><sub>Review Q3</sub><br><br></details>

<details><summary><b>4.</b> <img src="drop_phases.png"><br>What is the phase relationship between Eₗ and Ec in series?</summary><br>180° apart — exactly opposite, so they subtract.<br><br></details>

<details><summary><b>5.</b> What is the same through every part of an RLC series circuit?</summary><br>The current.<br><img src="rlc_series_circuit.png"><br><br></details>

<details><summary><b>6.</b> How do Xl and Xc combine in series?</summary><br>They subtract: net X = Xl − Xc. The smaller is eliminated, the larger reduced.<br><img src="reactance_cancel.png"><br><br></details>

<details><summary><b>7.</b> Impedance formula for RLC series?</summary><br>Z = √(R² + (Xl − Xc)²)<br><img src="impedance_triangle_rlc.png"><br><br><sub>R = √(Z² − (Xl − Xc)²)</sub><br><br></details>

<details><summary><b>8.</b> <img src="reactance_cancel.png"><br>R 12 Ω, Xl 24 Ω, Xc 8 Ω. Z?</summary><br>√(12² + 16²) = <b>20 Ω</b><br><br><sub>Example 23–1</sub><br><br></details>

<details><summary><b>9.</b> Xc is larger than Xl. Does the negative difference matter in Z?</summary><br>No — it's squared. R 10, Xl 30, Xc 54 → √(100 + 576) = 26 Ω.<br><br></details>

<details><summary><b>10.</b> Two common Z mistakes in RLC series?</summary><br>Adding Xl + Xc, or putting Xl and Xc separately into √(R² + …). Always subtract first.<br><br></details>

<details><summary><b>11.</b> Why can RLC series current be surprisingly large?</summary><br>Xl and Xc cancel, so Z can be smaller than either reactance.<br><br></details>

<details><summary><b>12.</b> <img src="rlc_series_circuit.png"><br>RLC example on 240 V: current and drops?</summary><br>I = 240/20 = 12 A; Eᵣ = 144 V, Eₗ = 288 V, Ec = 96 V.<br><br></details>

<details><summary><b>13.</b> <img src="drops_exceed_supply.png"><br>Can a component's voltage exceed the supply in RLC series?</summary><br>Yes — Eₗ = 288 V on a 240 V supply. Eₗ and Ec partly cancel, so the supply only provides the difference.<br><br><sub>Check capacitor ratings!</sub><br><br></details>

<details><summary><b>14.</b> Total voltage formula in RLC series?</summary><br>Eₜ = √(Eᵣ² + (Eₗ − Ec)²)<br><br><sub>√(144² + 192²) = 240 V</sub><br><br></details>

<details><summary><b>15.</b> L and C values in Example 23–1?</summary><br>L = 24/377 = 0.0637 H; C = 1/(377 × 8) = 331.6 µF.<br><br></details>

<details><summary><b>16.</b> 66.3 µF, 0.0663 H, 8 Ω on 120 V, 60 Hz. Current?</summary><br>Xc = 40 Ω, Xl = 25 Ω → Z = √(64 + 225) = 17 Ω → I = <b>7.05 A</b>.<br><br><sub>Example 23–2</sub><br><br></details>

<details><summary><b>17.</b> Xl 62 Ω, Xc 38 Ω on 208 V. What R limits current to 8 A?</summary><br>Z = 208/8 = 26 Ω; R = √(26² − 24²) = <b>10 Ω</b>.<br><br><sub>Example 23–3</sub><br><br></details>

<details><summary><b>18.</b> Power quantities in Example 23–1?</summary><br>P 1728 W; VARsL 3456; VARsC 1152; net 2304 VARs inductive; VA 2880.<br><img src="power_vectors_rlc.png"><br><br></details>

<details><summary><b>19.</b> Apparent power formula in RLC circuits?</summary><br>VA = √(P² + (VARsL − VARsC)²)<br><br></details>

<details><summary><b>20.</b> <img src="power_vectors_rlc.png"><br>Why do inductive and capacitive VARs cancel?</summary><br>While the coil stores energy the capacitor releases it (and vice versa) — they trade energy locally, so the source supplies only the net.<br><br></details>

<details><summary><b>21.</b> Book typo in Figure 23–6?</summary><br>VARsC shown as 1142; correct value is 1152 (96 V × 12 A). Also "PF = 0.06 × 100" should be 0.6.<br><br></details>

<details><summary><b>22.</b> When is the RLC series PF lagging?</summary><br>When inductive VARs (Xl) exceed capacitive VARs (Xc) — current lags.<br><br></details>

<details><summary><b>23.</b> When is the RLC series PF leading?</summary><br>When capacitive VARs (Xc) exceed inductive — current leads.<br><br></details>

<details><summary><b>24.</b> Example 23–1 PF and θ?</summary><br>PF = 1728/2880 = 60% LAGGING; θ = 53.13°.<br><br></details>

<details><summary><b>25.</b> 18 W, 24 VARsL, 34 VARsC in series. PF, leading or lagging?</summary><br>Net 10 VARs capacitive → PF = 18/√(18² + 10²) ≈ 87.4% LEADING.<br><br><sub>Practice 6–7</sub><br><br></details>

<details><summary><b>26.</b> tan θ in an RLC series circuit?</summary><br>tan θ = (Xl − Xc)/R = (VARsL − VARsC)/P<br><br></details>

<details><summary><b>27.</b> What is resonance?</summary><br>The frequency at which Xl = Xc, so they cancel completely.<br><img src="resonance_crossing.png"><br><br><sub>23–2</sub><br><br></details>

<details><summary><b>28.</b> <img src="resonance_crossing.png"><br>Why must Xl and Xc be equal at some frequency?</summary><br>Xl rises with frequency and Xc falls — the curves must cross.<br><br></details>

<details><summary><b>29.</b> Resonant frequency formula?</summary><br>fR = 1 / (2π√(LC))  (L in H, C in F)<br><br></details>

<details><summary><b>30.</b> Formulas for the L or C needed to resonate at fR?</summary><br>L = 1/(4π²f²C); C = 1/(4π²f²L) — both π and f squared.<br><br><sub>Works for series or parallel</sub><br><br></details>

<details><summary><b>31.</b> C needed to resonate with 0.2 H at 1200 Hz?</summary><br>≈ <b>88 nF</b><br><br></details>

<details><summary><b>32.</b> L needed to resonate with 50 µF at 400 Hz?</summary><br>≈ <b>3.17 mH</b><br><br></details>

<details><summary><b>33.</b> At series resonance, what are Z, current and PF?</summary><br>Z = R (minimum), current maximum, PF = 100% (θ = 0°).<br><img src="resonance_current.png"><br><br></details>

<details><summary><b>34.</b> <img src="resonance_current.png"><br>0.0159 H (5 Ω wire) + 1.59 µF on 50 V: current at resonance (1000 Hz)?</summary><br>Only R limits it: 50/5 = <b>10 A</b> (vs ~0.47 A at 600 Hz, ~0.73 A at 1400 Hz).<br><br></details>

<details><summary><b>35.</b> <img src="resonance_voltages.png"><br>In that circuit, the voltage across L and across C at resonance?</summary><br>10 A × 100 Ω = <b>1000 V</b> each — on a 50 V supply.<br><br><sub>Magnified by Q = Xl/R = 20</sub><br><br></details>

<details><summary><b>36.</b> At resonance, do L and C disappear?</summary><br>No — they cancel each other's effect on the source, but each carries full current and develops a full (high) voltage.<br><br></details>

<details><summary><b>37.</b> What is bandwidth?</summary><br>The frequency range between the two points where current is 0.707 × maximum: B = f₂ − f₁.<br><img src="bandwidth.png"><br><br></details>

<details><summary><b>38.</b> Bandwidth formula using Q?</summary><br>B = fR / Q<br><br></details>

<details><summary><b>39.</b> <img src="resonance_current.png"><br>High-Q vs low-Q resonant circuit?</summary><br>High Q (low R): sharp peak, narrow bandwidth. Low Q: flat peak, wide bandwidth.<br><br><sub>Bandwidth is inversely proportional to Q</sub><br><br></details>

<details><summary><b>40.</b> <img src="bandwidth.png"><br>Resonance at 1000 Hz, 0.707 points at 995 and 1005 Hz. Bandwidth?</summary><br><b>10 Hz</b> (narrow — high Q)<br><br></details>

<details><summary><b>41.</b> Resonance at 1200 Hz, 0.707 points at 1150 and 1250 Hz. Bandwidth?</summary><br><b>100 Hz</b> (wide — low Q)<br><br></details>

<details><summary><b>42.</b> Why can PF capacitor banks cause trouble on systems with VFDs?</summary><br>Capacitors + system inductance form a resonant L-C circuit; if it lands near a harmonic (300, 420 Hz…) currents/voltages are magnified — blown fuses, failed caps. Hence detuned banks.<br><br></details>

<details><summary><b>43.</b> <img src="resonant_test_set.png"><br>How do resonant AC test sets produce very high test voltages?</summary><br>A tuned reactor resonates with the cable's capacitance; at resonance the voltage across the cable is magnified (≈ Q × supply).<br><br></details>

<details><summary><b>44.</b> What is ferroresonance?</summary><br>Resonance between an iron-core transformer's (nonlinear) inductance and cable capacitance — often after single-phase switching — producing erratic overvoltages.<br><br></details>

<details><summary><b>45.</b> 400 Hz resonant HV source: 15 mH, 2 Ω, 240 V. Capacitor voltage rating?</summary><br>At resonance I = 240/2 = 120 A; Ec = I × Xc (= I × Xl ≈ 120 × 37.7 Ω). The rating must exceed THAT (×1.414 if DC-rated), not 240 V.<br><br><sub>Practical Application</sub><br><br></details>

<details><summary><b>46.</b> Review Q4 (400 Hz): what must you NOT use?</summary><br>377 — compute 2π × 400 for Xl and Xc.<br><br></details>
