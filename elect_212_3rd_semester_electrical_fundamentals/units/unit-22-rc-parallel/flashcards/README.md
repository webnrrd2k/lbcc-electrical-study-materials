# Flashcards — Unit 22: Resistive-Capacitive Parallel Circuits

44 cards. Read the question, answer it in your head, then click it to check.

Study guide for this unit: [study-guide.md](../study-guide.md). The raw card data is in [`unit22_flashcards.json`](unit22_flashcards.json) if you want to import the cards into a flashcard app.

---

<details><summary><b>1.</b> What is the same across every branch of a parallel R-C circuit?</summary><br>The voltage (magnitude and phase).<br><img src="rc_parallel_circuit.png"><br><br><sub>Summary</sub><br><br></details>

<details><summary><b>2.</b> Phase of the resistive branch current?</summary><br>In phase with the voltage.<br><img src="branch_currents_rc.png"><br><br></details>

<details><summary><b>3.</b> Phase of the capacitive branch current?</summary><br>Leads the voltage by 90°.<br><img src="branch_currents_rc.png"><br><br></details>

<details><summary><b>4.</b> <img src="branch_currents_rc.png"><br>How many degrees apart are Iᵣ and Ic in parallel?</summary><br>90°<br><br><sub>Review Q1</sub><br><br></details>

<details><summary><b>5.</b> Does total current lead or lag in parallel R-C?</summary><br>Leads, by an angle between 0° and 90°.<br><img src="total_current_lead.png"><br><br></details>

<details><summary><b>6.</b> What sets the phase angle in parallel R-C?</summary><br>How current splits between branches: tan θ = Ic/Iᵣ = R/Xc.<br><br><sub>Book says "resistance to capacitance"</sub><br><br></details>

<details><summary><b>7.</b> In parallel R-C, does a bigger capacitor make the circuit more or less capacitive?</summary><br>MORE capacitive — lower Xc draws more Ic (opposite of series R-C).<br><br><sub>Bigger R also makes it more capacitive</sub><br><br></details>

<details><summary><b>8.</b> In a parallel phasor diagram, what is the reference and which way does Ic point?</summary><br>Voltage is the reference (0°). Ic points UP (leading). Iᵣ lies along E.<br><img src="parallel_rc_phasor.png"><br><br><sub>Il pointed down in Unit 18</sub><br><br></details>

<details><summary><b>9.</b> <img src="rc_parallel_circuit.png"><br>30 Ω ∥ Xc 20 Ω on 240 V: branch currents?</summary><br>Iᵣ = 240/30 = <b>8 A</b>; Ic = 240/20 = <b>12 A</b>.<br><br><sub>Example 22–1</sub><br><br></details>

<details><summary><b>10.</b> Branch current formulas?</summary><br>Iᵣ = E/R; Ic = E/Xc<br><br></details>

<details><summary><b>11.</b> Capacitance for Xc = 20 Ω at 60 Hz?</summary><br>C = 1/(377 × 20) = <b>132.6 µF</b><br><br></details>

<details><summary><b>12.</b> Total current formula in parallel R-C?</summary><br>Iₜ = √(Iᵣ² + Ic²)<br><img src="current_triangle_rc.png"><br><br><sub>Iᵣ = √(Iₜ² − Ic²), Ic = √(Iₜ² − Iᵣ²)</sub><br><br></details>

<details><summary><b>13.</b> Iᵣ = 8 A, Ic = 12 A. Iₜ?</summary><br>√(64 + 144) = <b>14.42 A</b> (not 20 A)<br><img src="current_triangle_rc.png"><br><br></details>

<details><summary><b>14.</b> <img src="clamp_readings_rc.png"><br>Feeder clamp reads 14.4 A while branches read 8 A and 12 A. Fault?</summary><br>No — the branch currents are 90° apart and add as vectors.<br><br></details>

<details><summary><b>15.</b> Several capacitor branches plus a resistor: how do you get Iₜ?</summary><br>Add the capacitor currents straight (same phase), then Iₜ = √(Iᵣ² + Ic total²).<br><br></details>

<details><summary><b>16.</b> Simplest way to find Z when E and Iₜ are known?</summary><br>Z = E/Iₜ = 240/14.422 = <b>16.64 Ω</b><br><br></details>

<details><summary><b>17.</b> Product-over-vector-sum formula for parallel R-C?</summary><br>Z = R·Xc / √(R² + Xc²)<br><br><sub>600/36.06 = 16.64 Ω</sub><br><br></details>

<details><summary><b>18.</b> Reciprocal formula for parallel R-C impedance?</summary><br>Z = 1 / √((1/R)² + (1/Xc)²)<br><br></details>

<details><summary><b>19.</b> Is parallel Z larger or smaller than R and Xc?</summary><br>Smaller than both.<br><br><sub>16.64 &lt; 20 &lt; 30</sub><br><br></details>

<details><summary><b>20.</b> <img src="z_parallel_rc.png"><br>Which formula gives Z for 30 Ω ∥ Xc 20 Ω?</summary><br>Only R·Xc/√(R² + Xc²) = <b>16.64 Ω</b>. √(R² + Xc²) = 36.06 is the series answer; R·Xc/(R + Xc) = 12 ignores the 90°.<br><br></details>

<details><summary><b>21.</b> Can you draw an impedance triangle with R and Xc as legs for a parallel circuit?</summary><br>No — draw the current triangle instead.<br><br></details>

<details><summary><b>22.</b> Power values for the 30 Ω ∥ 20 Ω, 240 V example?</summary><br>P = 240 × 8 = <b>1920 W</b>; VARsc = 240 × 12 = <b>2880</b>; VA = 240 × 14.42 = <b>3461</b>.<br><img src="power_triangle_22.png"><br><br></details>

<details><summary><b>23.</b> Formula linking P, VARs and VA (any circuit)?</summary><br>VA = √(P² + VARs²)<br><br></details>

<details><summary><b>24.</b> How is the parallel power triangle related to the current triangle?</summary><br>It's the current triangle × E.<br><br></details>

<details><summary><b>25.</b> You know VARs and Xc but not E. Find E.</summary><br>E = √(VARs × Xc)  (also √(P × R), √(VA × Z))<br><br><sub>From VARs = E²/Xc</sub><br><br></details>

<details><summary><b>26.</b> PF formulas for parallel R-C?</summary><br>PF = P/VA = Iᵣ/Iₜ = Z/R<br><br><sub>55.47% in the main example</sub><br><br></details>

<details><summary><b>27.</b> Why is parallel PF Z/R, not R/Z?</summary><br>Parallel Z &lt; R, so R/Z would exceed 1 — impossible for PF.<br><br></details>

<details><summary><b>28.</b> Why can't voltage ratios give PF in a parallel circuit?</summary><br>Voltage is the same on every branch, so Eᵣ/Eₜ is always 1.<br><br></details>

<details><summary><b>29.</b> Main example θ?</summary><br>cos⁻¹(0.5547) = <b>56.31°</b>, current leading.<br><img src="total_current_lead.png"><br><br></details>

<details><summary><b>30.</b> Other trig ratios for θ in parallel R-C?</summary><br>tan θ = Ic/Iᵣ = VARs/P; sin θ = Ic/Iₜ = VARs/VA<br><img src="parallel_rc_phasor.png"><br><br></details>

<details><summary><b>31.</b> Given PF and VA, how do you get P and VARs?</summary><br>P = VA × PF; VARs = √(VA² − P²) (or VA × sin θ).<br><br><sub>Example 22–2</sub><br><br></details>

<details><summary><b>32.</b> Example 22–2: PF 47.1%, VA 4086.13, 33.15 µF at 400 Hz. First three steps?</summary><br>θ = cos⁻¹(0.471) ≈ 61.9°; P = 4086.13 × 0.471 = 1924.5 W; VARs = √(VA² − P²) = 3604.6.<br><img src="example_22_2_power.png"><br><br></details>

<details><summary><b>33.</b> Example 22–2: Xc and voltage?</summary><br>Xc = 1/(2π × 400 × 0.00003315) = <b>12 Ω</b> (377 doesn't apply at 400 Hz); E = √(3604.6 × 12) = <b>208 V</b>.<br><br></details>

<details><summary><b>34.</b> <img src="example_22_2_circuit.png"><br>Example 22–2: currents, R and Z?</summary><br>Ic = 17.33 A, Iᵣ = 9.25 A, Iₜ = 19.64 A; R = 22.49 Ω; Z = 10.59 Ω.<br><br></details>

<details><summary><b>35.</b> Key first move in a parallel circuit when E isn't given?</summary><br>Find E (it's the bridge into every branch) — e.g., √(VARs × Xc), √(P × R) or √(VA × Z).<br><br><sub>Mirror of finding I first in series</sub><br><br></details>

<details><summary><b>36.</b> Book typos in Example 22–2?</summary><br>"1 Hz" on top of the Xc fraction (should be 1); θ shown as 61.9° then 61.93° (rounding).<br><br></details>

<details><summary><b>37.</b> Wrong-file check: what is this chapter's real title?</summary><br>Unit 22: Resistive-Capacitive Parallel Circuits.<br><br><sub>The PDF filename said R-L-C series</sub><br><br></details>

<details><summary><b>38.</b> <img src="pf_correction_circuit.png"><br>How are power-factor correction capacitors connected?</summary><br>In PARALLEL with the load (across the line) — never in series.<br><br></details>

<details><summary><b>39.</b> <img src="pf_correction_vectors.png"><br>How does a parallel capacitor reduce feeder current on a motor circuit?</summary><br>Its leading current cancels part of the motor's lagging current; the feeder carries the smaller vector sum.<br><br></details>

<details><summary><b>40.</b> A capacitor uses no watts. Does it draw real line current?</summary><br>Yes — e.g., 132.6 µF on 240 V draws 12 A. Feeders/disconnects are sized at 135% of capacitor rated current (NEC 460.8).<br><br></details>

<details><summary><b>41.</b> Motors shut off but PF capacitors stay on. Result?</summary><br>The plant goes leading; voltage can rise. Banks are often switched with the load or automatically.<br><br></details>

<details><summary><b>42.</b> Series vs parallel R-C: what changes?</summary><br>Series: current shared, Z = √(R² + Xc²), PF = R/Z, bigger C → more resistive. Parallel: voltage shared, Z = R·Xc/√(R² + Xc²), PF = Z/R, bigger C → more capacitive.<br><img src="series_vs_parallel_rc.png"><br><br></details>

<details><summary><b>43.</b> 40 Ω ∥ 132.6 µF on 120 V, 60 Hz: first step?</summary><br>Convert C to Xc: 1/(377 × 0.0001326) = 20 Ω. Then Iᵣ = 3 A, Ic = 6 A, Iₜ = √45 ≈ 6.71 A.<br><br><sub>Review Q2</sub><br><br></details>

<details><summary><b>44.</b> 208 V, 46 A, 4975 W (parallel R-C). Route to R and C?</summary><br>Iᵣ = 4975/208; R = 208/Iᵣ; Ic = √(46² − Iᵣ²); Xc = 208/Ic; C = 1/(377 Xc).<br><br><sub>Review Q6–7</sub><br><br></details>
