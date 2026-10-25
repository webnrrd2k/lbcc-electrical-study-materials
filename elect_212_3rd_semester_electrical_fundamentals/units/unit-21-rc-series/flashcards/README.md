# Flashcards — Unit 21: Resistive-Capacitive Series Circuits

42 cards. Read the question, answer it in your head, then click it to check.

Study guide for this unit: [study-guide.md](../study-guide.md). The raw card data is in [`unit21_flashcards.json`](unit21_flashcards.json) if you want to import the cards into a flashcard app.

---

<details><summary><b>1.</b> How is solving an R-C series circuit different from R-L series?</summary><br>Same procedure. Swap Xl→Xc, VARsL→VARsC, and the current LEADS instead of lags.<br><br><sub>Intro</sub><br><br></details>

<details><summary><b>2.</b> In a pure capacitive circuit, does current lead or lag?</summary><br>Leads the voltage by 90°.<br><br><sub>Review Q1</sub><br><br></details>

<details><summary><b>3.</b> In an R-C series circuit, by how much are V and I out of phase?</summary><br>Between 0° and 90°, with current LEADING.<br><img src="wave_rc_lead.png"><br><br></details>

<details><summary><b>4.</b> What sets the phase angle in R-C series?</summary><br>The ratio of R to Xc (tan θ = Xc/R) — the book says "capacitance", but it's capacitive reactance.<br><br></details>

<details><summary><b>5.</b> In series R-C, does a bigger capacitor make the circuit more or less resistive?</summary><br>MORE resistive — a bigger C has less Xc, so the angle shrinks.<br><br><sub>Counter-intuitive</sub><br><br></details>

<details><summary><b>6.</b> What is the same everywhere in a series R-C circuit?</summary><br>The current: Iₜ = Iᵣ = Ic.<br><img src="rc_series_circuit.png"><br><br></details>

<details><summary><b>7.</b> Phase of Eᵣ and Ec relative to the current?</summary><br>Eᵣ in phase with I; Ec lags I by 90° (i.e., I leads Ec).<br><img src="phasor_rc.png"><br><br><sub>So Eᵣ and Ec are 90° apart</sub><br><br></details>

<details><summary><b>8.</b> Which three groups organize R-C circuit quantities?</summary><br>Resistive (R, Eᵣ, Iᵣ, P), capacitive (Xc, Ec, Ic, VARsc, C), total (Z, Eₜ, Iₜ, VA, PF, θ).<br><img src="three_groups_rc.png"><br><br></details>

<details><summary><b>9.</b> <img src="three_groups_rc.png"><br>Golden rule for Ohm's law in R-C circuits?</summary><br>Only inside one group; cross groups with the right triangle.<br><br></details>

<details><summary><b>10.</b> Impedance formula for series R-C?</summary><br>Z = √(R² + Xc²)<br><img src="impedance_triangle_rc.png"><br><br><sub>R = √(Z² − Xc²), Xc = √(Z² − R²)</sub><br><br></details>

<details><summary><b>11.</b> <img src="rc_series_circuit.png"><br>R = 12 Ω, Xc = 16 Ω. Z and I on 240 V?</summary><br>Z = √(144 + 256) = <b>20 Ω</b>; I = 240/20 = <b>12 A</b>.<br><br><sub>Main example</sub><br><br></details>

<details><summary><b>12.</b> Why isn't Z = 12 + 16 = 28 Ω?</summary><br>R and Xc are 90° apart, so they add as vectors.<br><br></details>

<details><summary><b>13.</b> Z = 84 Ω, R = 32 Ω. Xc?</summary><br>√(84² − 32²) ≈ <b>77.7 Ω</b><br><br><sub>Review Q4</sub><br><br></details>

<details><summary><b>14.</b> 20 Ω resistor + 110.5 µF at 60 Hz. First step?</summary><br>Convert C to Xc: 1/(377 × 0.0001105) ≈ 24 Ω. Then Z = √(20² + 24²) ≈ 31.2 Ω.<br><br><sub>Review Q2</sub><br><br></details>

<details><summary><b>15.</b> Xc = 50 Ω at 60 Hz. At 1000 Hz?</summary><br>50 × 60/1000 = <b>3 Ω</b><br><br><sub>Review Q5</sub><br><br></details>

<details><summary><b>16.</b> Voltage drop formulas in series R-C?</summary><br>Eᵣ = I × R; Ec = I × Xc<br><br><sub>Example: 144 V and 192 V</sub><br><br></details>

<details><summary><b>17.</b> Capacitance from Xc in the main example?</summary><br>C = 1/(377 × 16) = <b>165.8 µF</b><br><br><sub>21–6</sub><br><br></details>

<details><summary><b>18.</b> Total voltage from the drops?</summary><br>Eₜ = √(Eᵣ² + Ec²)<br><img src="voltage_triangle_rc.png"><br><br><sub>Ec = √(Eₜ² − Eᵣ²)</sub><br><br></details>

<details><summary><b>19.</b> <img src="meter_drops_rc.png"><br>Meters read 144 V on R and 192 V on C on a 240 V supply. Problem?</summary><br>No — the drops are 90° apart: √(144² + 192²) = 240 V.<br><br></details>

<details><summary><b>20.</b> When checking a series capacitor's voltage rating, which voltage do you use?</summary><br>The capacitor's own drop Ec (× 1.414 if rated in VDC) — not the supply.<br><br><sub>Review Q6</sub><br><br></details>

<details><summary><b>21.</b> True power formula in R-C series?</summary><br>P = Eᵣ × I (resistive values only) = 144 × 12 = <b>1728 W</b><br><br></details>

<details><summary><b>22.</b> Reactive power formula?</summary><br>VARsc = Ec × I = 192 × 12 = <b>2304 VARs</b><br><br></details>

<details><summary><b>23.</b> Apparent power?</summary><br>VA = Eₜ × I = 240 × 12 = <b>2880 VA</b>, or √(P² + VARsc²)<br><img src="power_triangle_rc.png"><br><br></details>

<details><summary><b>24.</b> Which part of an R-C circuit produces watts?</summary><br>Only the resistor.<br><br><sub>Summary</sub><br><br></details>

<details><summary><b>25.</b> How are the impedance, voltage and power triangles related?</summary><br>Similar triangles: voltage = impedance × I; power = impedance × I². Same angle θ.<br><br></details>

<details><summary><b>26.</b> Power factor formulas for series R-C?</summary><br>PF = P/VA = R/Z = Eᵣ/Eₜ<br><br><sub>60% in the main example</sub><br><br></details>

<details><summary><b>27.</b> Main example θ?</summary><br>cos⁻¹(0.6) = <b>53.13°</b>, current leading.<br><img src="wave_rc_lead.png"><br><br></details>

<details><summary><b>28.</b> Other trig ratios for θ in R-C series?</summary><br>tan θ = Xc/R = VARsc/P; sin θ = Xc/Z = Ec/Eₜ<br><br></details>

<details><summary><b>29.</b> <img src="lead_vs_lag.png"><br>Same numbers, R-L vs R-C: what's different about PF?</summary><br>The number is the same; the direction differs — R-L is LAGGING, R-C is LEADING.<br><br></details>

<details><summary><b>30.</b> PF = 76%. Phase angle?</summary><br>cos⁻¹(0.76) ≈ <b>40.5°</b><br><br><sub>Review Q3</sub><br><br></details>

<details><summary><b>31.</b> Eₜ = 460 V and θ = 44°. Ec?</summary><br>Ec = Eₜ × sin θ ≈ 460 × 0.695 ≈ <b>320 V</b><br><br><sub>Practice 8</sub><br><br></details>

<details><summary><b>32.</b> Example 21–1: R 5 W, C₁ 3.75 VARs, C₂ 5.625 VARs on 42.5 V. VA and I?</summary><br>VARs add: 9.375. VA = √(5² + 9.375²) = <b>10.625</b>; I = 10.625/42.5 = <b>0.25 A</b>.<br><img src="example_21_1_power.png"><br><br></details>

<details><summary><b>33.</b> <img src="example_21_1_circuit.png"><br>Example 21–1: Xc and C of each capacitor?</summary><br>Ec₁ = 15 V → Xc₁ = 60 Ω → 44.2 µF. Ec₂ = 22.5 V → Xc₂ = 90 Ω → 29.5 µF.<br><br></details>

<details><summary><b>34.</b> Book error: Example 21–1 computes C₁ = 1/(377 × 30 Ω). Fix?</summary><br>Should be 60 Ω (the answer 44.2 µF is correct for 60 Ω). Also Figs 21–9/21–10 show 3.73 VARs; it's 3.75.<br><br></details>

<details><summary><b>35.</b> A 2 W, 120 V lamp must run on 480 V with a series capacitor. Voltage across the cap?</summary><br>√(480² − 120²) = <b>464.8 V</b> (not 360 V).<br><img src="lamp_dropper_triangle.png"><br><br><sub>Example 21–2</sub><br><br></details>

<details><summary><b>36.</b> <img src="lamp_dropper.png"><br>Capacitor value for that lamp dropper?</summary><br>I = 2/120 = 0.01667 A → Xc ≈ 27.9 kΩ → C ≈ <b>95 nF</b>.<br><br></details>

<details><summary><b>37.</b> Why use a capacitor instead of a resistor to drop voltage?</summary><br>The capacitor drops voltage with essentially no watts (reactive power); a resistor would waste ~6 W as heat.<br><br></details>

<details><summary><b>38.</b> Exception to the lamp-dropper calculation?</summary><br>It assumes the lamp is a constant resistance; a cold filament or an LED doesn't behave that way.<br><br></details>

<details><summary><b>39.</b> Why can too much leading PF be a problem?</summary><br>Over-correction raises voltage and can upset generators/regulators. Aim for ~0.95–1.0, not as capacitive as possible.<br><br></details>

<details><summary><b>40.</b> Where do you meet series R-C circuits on the job?</summary><br>RC snubbers across contacts/triacs, phase-shift networks, capacitive droppers in pilot lights and small supplies.<br><br></details>

<details><summary><b>41.</b> RC circuit: 120 V, resistor 25 Ω dropping 65 V. Steps to find C?</summary><br>I = 65/25; Ec = √(120² − 65²); Xc = Ec/I; C = 1/(377·Xc).<br><br><sub>Review Q7</sub><br><br></details>

<details><summary><b>42.</b> 240 V, 20 A, 3 kW in a series RC circuit. PF and the route to C?</summary><br>PF = 3000/4800 = <b>62.5%</b>. R = P/I², Z = E/I, Xc = √(Z² − R²), C = 1/(377·Xc).<br><br><sub>Review Q8</sub><br><br></details>
