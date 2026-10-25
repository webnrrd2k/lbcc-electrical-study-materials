# Flashcards — Unit 18: Resistive-Inductive Parallel Circuits

54 cards. Read the question, answer it in your head, then click it to check.

Study guide for this unit: [study-guide.md](../study-guide.md). The raw card data is in [`unit18_flashcards.json`](unit18_flashcards.json) if you want to import the cards into a flashcard app.

---

<details><summary><b>1.</b> Why do so many real circuits contain R and L in parallel?</summary><br>Every load on a branch circuit is in parallel, and mixed loads are common: lights + fan motor, heat strips + compressor.<br><img src="branch_loads.png"><br><br><sub>Why You Need to Know</sub><br><br></details>

<details><summary><b>2.</b> What is the same across every branch of a parallel R-L circuit?</summary><br>The voltage, in both magnitude and phase: Eₜ = Eᵣ = Eₗ.<br><img src="rl_parallel_circuit.png"><br><br><sub>Summary bullet 1</sub><br><br></details>

<details><summary><b>3.</b> Phase of the resistive branch current?</summary><br>In phase with the voltage.<br><img src="branch_currents_wave.png"><br><br><sub>Summary</sub><br><br></details>

<details><summary><b>4.</b> Phase of the inductive branch current?</summary><br>Lags the voltage by 90°.<br><img src="branch_currents_wave.png"><br><br><sub>Summary</sub><br><br></details>

<details><summary><b>5.</b> <img src="branch_currents_wave.png"><br>In parallel, how many degrees apart are Iᵣ and Iₗ?</summary><br>90°<br><br><sub>Review Q1</sub><br><br></details>

<details><summary><b>6.</b> In a parallel phasor diagram, what is the 0° reference, and why?</summary><br>Voltage. It's the one quantity shared by every branch. (In series it was current.)<br><img src="parallel_phasor.png"><br><br><sub>Iᵣ lies along E; Iₗ points down (lagging)</sub><br><br></details>

<details><summary><b>7.</b> What sets the phase angle between total current and voltage in parallel R-L?</summary><br>How the current is split: the ratio of Iᵣ to Iₗ (set by R vs Xₗ).<br><br><sub>18–1</sub><br><br></details>

<details><summary><b>8.</b> In parallel, does a BIGGER resistance make the circuit more or less resistive?</summary><br>Less. A bigger R draws less current, so the inductive branch dominates and PF drops. (Opposite of series.)<br><br><sub>The branch with more current dominates</sub><br><br></details>

<details><summary><b>9.</b> <img src="rl_parallel_circuit.png"><br>What is this circuit, and what is each branch current?</summary><br>R-L parallel. Iᵣ = 240/15 = <b>16 A</b>; Iₗ = 240/20 = <b>12 A</b>.<br><br><sub>Figure 18–4</sub><br><br></details>

<details><summary><b>10.</b> Formula for the resistive branch current?</summary><br>Iᵣ = E / R<br><br><sub>Voltage is the same as the supply</sub><br><br></details>

<details><summary><b>11.</b> Formula for the inductive branch current?</summary><br>Iₗ = E / Xₗ<br><br></details>

<details><summary><b>12.</b> Watts in the 15 Ω / 20 Ω / 240 V example?</summary><br>P = E × Iᵣ = 240 × 16 = <b>3840 W</b><br><br></details>

<details><summary><b>13.</b> VARs in the 15 Ω / 20 Ω / 240 V example?</summary><br>VARs = E × Iₗ = 240 × 12 = <b>2880 VARs</b><br><br></details>

<details><summary><b>14.</b> Inductance for Xₗ = 20 Ω at 60 Hz?</summary><br>L = 20 / 377 = <b>0.0531 H</b><br><br></details>

<details><summary><b>15.</b> Formula for total current in parallel R-L?</summary><br>Iₜ = √(Iᵣ² + Iₗ²)<br><img src="current_triangle.png"><br><br><sub>Rearranged: Iᵣ = √(Iₜ² − Iₗ²), Iₗ = √(Iₜ² − Iᵣ²)</sub><br><br></details>

<details><summary><b>16.</b> Iᵣ = 16 A and Iₗ = 12 A. Total current?</summary><br>√(16² + 12²) = <b>20 A</b> (not 28 A)<br><img src="current_triangle.png"><br><br></details>

<details><summary><b>17.</b> Why can't you add Iᵣ + Iₗ directly?</summary><br>They're 90° apart, so they peak at different times. They add as vectors (Pythagorean theorem).<br><br><sub>Summary bullet 4</sub><br><br></details>

<details><summary><b>18.</b> Iᵣ = 6.5 A, Iₗ = 8 A. Iₜ?</summary><br>√(6.5² + 8²) ≈ <b>10.3 A</b><br><br><sub>Review Q6</sub><br><br></details>

<details><summary><b>19.</b> <img src="clamp_readings.png"><br>Branch clamps read 16 A and 12 A, feeder reads 20 A. Fault?</summary><br>No. Mixed R and L branch currents add as vectors, so the feeder reads less than the straight sum.<br><br></details>

<details><summary><b>20.</b> Two inductive branches draw 9 A and 6 A. Total inductive current?</summary><br><b>15 A</b>. Same-type currents are in phase, so they add straight. Then combine with Iᵣ by the Pythagorean theorem.<br><br><sub>Example 18–2</sub><br><br></details>

<details><summary><b>21.</b> Easiest way to find Z if you know E and Iₜ?</summary><br>Z = Eₜ / Iₜ = 240 / 20 = <b>12 Ω</b><br><br></details>

<details><summary><b>22.</b> Reciprocal formula for parallel R-L impedance?</summary><br>Z = 1 / √((1/R)² + (1/Xₗ)²)<br><br><sub>Square the reciprocals, add, root, then take the reciprocal again</sub><br><br></details>

<details><summary><b>23.</b> Product-over-vector-sum formula for parallel R-L impedance?</summary><br>Z = (R × Xₗ) / √(R² + Xₗ²)<br><br><sub>15 × 20 / 25 = 12 Ω</sub><br><br></details>

<details><summary><b>24.</b> Is parallel Z bigger or smaller than R and Xₗ?</summary><br>Smaller than both (12 Ω is less than 15 and 20).<br><br><sub>Adding a path lowers total opposition</sub><br><br></details>

<details><summary><b>25.</b> Can you draw an impedance triangle (R and Xₗ as legs) for a parallel circuit?</summary><br>No. That only works in series. In parallel, use the reciprocal formula, product-over-vector-sum, or E/Iₜ.<br><img src="z_parallel_formulas.png"><br><br><sub>Book's Helpful Hint</sub><br><br></details>

<details><summary><b>26.</b> <img src="z_parallel_formulas.png"><br>Which of these gives the parallel Z for 15 Ω ∥ 20 Ω?</summary><br>Only R·Xₗ / √(R² + Xₗ²) = <b>12 Ω</b>. √(R² + Xₗ²) = 25 Ω is the series answer; R·Xₗ / (R + Xₗ) = 8.57 Ω ignores the 90°.<br><br></details>

<details><summary><b>27.</b> R = 24 Ω ∥ Xₗ = 20 Ω. Z?</summary><br>(24 × 20) / √(24² + 20²) = <b>15.4 Ω</b><br><br><sub>Review Q7. 31.2 Ω would be the series mistake</sub><br><br></details>

<details><summary><b>28.</b> <img src="example_18_2_circuit.png"><br>Two inductors (40 Ω and 60 Ω) in parallel with a resistor. First step for Z?</summary><br>Combine the inductors first with the ordinary reciprocal formula: 1/(1/40 + 1/60) = <b>24 Ω</b>. Then use the vector formula with R.<br><br><sub>Example 18–2</sub><br><br></details>

<details><summary><b>29.</b> Is the power triangle different for parallel circuits?</summary><br>No. Watts, VARs and VA add the same way in any circuit: VA = √(P² + VARs²).<br><img src="power_triangle_18.png"><br><br><sub>Summary bullet 6</sub><br><br></details>

<details><summary><b>30.</b> Apparent power in the 240 V, 20 A example?</summary><br>VA = E × Iₜ = 240 × 20 = <b>4800 VA</b><br><br></details>

<details><summary><b>31.</b> How is the parallel power triangle related to the current triangle?</summary><br>It's the current triangle multiplied by E (16/12/20 A × 240 V).<br><br><sub>Same shape, same angle</sub><br><br></details>

<details><summary><b>32.</b> You know VA and Z but not E. How do you find E?</summary><br>VA = E²/Z, so E = √(VA × Z).<br><br><sub>Example 18–2: √(6120 × 21.176) = 360 V</sub><br><br></details>

<details><summary><b>33.</b> VA = 325, PF = 66%. True power?</summary><br>P = 325 × 0.66 ≈ <b>214.5 W</b><br><br><sub>Review Q8</sub><br><br></details>

<details><summary><b>34.</b> VA = 465, P = 320 W. VARs?</summary><br>√(465² − 320²) ≈ <b>337 VARs</b><br><br><sub>Review Q9</sub><br><br></details>

<details><summary><b>35.</b> PF formulas for a parallel R-L circuit?</summary><br>PF = P / VA = Iᵣ / Iₜ = Z / R<br><br><sub>80% in the main example</sub><br><br></details>

<details><summary><b>36.</b> Why is parallel PF Z/R instead of R/Z?</summary><br>Parallel Z is smaller than R, so R/Z would exceed 1, and PF can never exceed 1.<br><br><sub>Series uses R/Z</sub><br><br></details>

<details><summary><b>37.</b> R = 8 Ω, Z = 5 Ω (parallel). PF?</summary><br>Z/R = 5/8 = <b>62.5%</b><br><br><sub>Example 18–1</sub><br><br></details>

<details><summary><b>38.</b> Why can't voltage ratios give PF in a parallel circuit?</summary><br>The voltage is the same on every branch, so Eᵣ/Eₜ is always 1. Use currents instead.<br><br><sub>Mirror of the series rule</sub><br><br></details>

<details><summary><b>39.</b> Main example PF and θ?</summary><br>PF = 3840/4800 = 16/20 = 12/15 = <b>80%</b>; θ = cos⁻¹(0.8) = <b>36.87°</b>, current lagging.<br><img src="total_current_wave.png"><br><br></details>

<details><summary><b>40.</b> What is the relationship between θ and PF in any AC circuit?</summary><br>cos θ = PF<br><br></details>

<details><summary><b>41.</b> Other trig ratios for θ in parallel R-L?</summary><br>tan θ = Iₗ / Iᵣ = VARs / P<br>sin θ = Iₗ / Iₜ = VARs / VA<br><img src="parallel_phasor.png"><br><br></details>

<details><summary><b>42.</b> Book wording check: "PF is the relationship of apparent power to true power." Correct?</summary><br>Backwards. PF = true power ÷ apparent power. The book's formulas are right.<br><br></details>

<details><summary><b>43.</b> <img src="example_18_2_circuit.png"><br>Example 18–2: R 45 Ω, Xₗ 40 and 60 Ω, VA 6120. Find E and Iₜ.</summary><br>Xₗₜ = 24 Ω → Z = 21.176 Ω → E = √(6120 × 21.176) = <b>360 V</b> → Iₜ = 360 / 21.176 = <b>17 A</b>.<br><br></details>

<details><summary><b>44.</b> Example 18–2 branch currents? Check Iₜ.</summary><br>Iᵣ = 8 A, Iₗ₁ = 9 A, Iₗ₂ = 6 A. Iₗ = 15 A, √(8² + 15²) = 17 A ✓<br><br></details>

<details><summary><b>45.</b> Example 18–2 PF and θ?</summary><br>P = 2880 W, so PF = 2880/6120 = <b>47.06%</b>; θ = <b>61.93°</b>.<br><img src="example_18_2_power.png"><br><br></details>

<details><summary><b>46.</b> Book typo in Example 18–2: "P = 359.996 V × 8 V"?</summary><br>Should be 8 <b>A</b>.<br><br><sub>Also Fig 18–13's VARs labels differ slightly from the text (rounding)</sub><br><br></details>

<details><summary><b>47.</b> <img src="branch_loads.png"><br>Give real examples of parallel R-L loads.</summary><br>Ceiling fan with a light kit; a branch with incandescent lamps, fluorescent fixtures and motors; heat-pump compressor + heat strips.<br><br><sub>Figure 18–16</sub><br><br></details>

<details><summary><b>48.</b> Heat pump: 34 A compressor at 70% PF plus 10 kW strip heat on 240 V. How do you find total current?</summary><br>Compressor Iᵣ = 34 × 0.7 = 23.8 A, Iₗ = √(34² − 23.8²) ≈ 24.3 A. Strip = 41.7 A resistive. Iₜ = √((23.8 + 41.7)² + 24.3²) ≈ <b>69.8 A</b>.<br><img src="heat_pump_vectors.png"><br><br><sub>Practical App 2. Not 34 + 41.7 = 75.7 A</sub><br><br></details>

<details><summary><b>49.</b> 500 W of lamps + an inductive load on 120 V; total 7 A. Steps to find the load's inductance?</summary><br>Iᵣ = 500/120 = 4.17 A → Iₗ = √(7² − 4.17²) → Xₗ = 120/Iₗ → L = Xₗ/377.<br><br><sub>Practical App 1</sub><br><br></details>

<details><summary><b>50.</b> Adding resistive load in parallel with a motor does what to the PF?</summary><br>Raises it. More resistive current, same VARs, so the angle shrinks. (The VARs don't go away.)<br><br></details>

<details><summary><b>51.</b> Where are power-factor-correction capacitors connected relative to motors?</summary><br>In parallel (across the line), so their leading current cancels the motors' lagging current.<br><br><sub>Coming in the capacitance units</sub><br><br></details>

<details><summary><b>52.</b> Why do NEC load calculations often add amps straight even though the physics says vector sum?</summary><br>It's a deliberate, conservative simplification: the straight sum is never smaller than the vector sum.<br><br></details>

<details><summary><b>53.</b> Series vs parallel R-L: what's shared, and which PF ratios work?</summary><br>Series: current shared; PF = R/Z = Eᵣ/Eₜ. Parallel: voltage shared; PF = Z/R = Iᵣ/Iₜ. P/VA works for both.<br><img src="series_vs_parallel.png"><br><br></details>

<details><summary><b>54.</b> Practice 15 asks for "the reactance" when Xₗ = 48 Ω is given. What does it mean?</summary><br>Almost certainly inductance: L = 48 / 377 ≈ 0.127 H.<br><br><sub>Likely book typo</sub><br><br></details>
