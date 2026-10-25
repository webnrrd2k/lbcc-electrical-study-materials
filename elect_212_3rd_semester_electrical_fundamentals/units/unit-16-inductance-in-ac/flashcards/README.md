# Flashcards — Unit 16: Inductance in AC Circuits

62 cards. Read the question, answer it in your head, then click it to check.

Study guide for this unit: [study-guide.md](../study-guide.md). The raw card data is in [`unit16_flashcards.json`](unit16_flashcards.json) if you want to import the cards into a flashcard app.

---

<details><summary><b>1.</b> What is inductance (L), and what is its unit?</summary><br>A coil's ability to induce voltage in itself, opposing any change in current. Measured in henrys (H).<br><br><sub>1 mH = 0.001 H</sub><br><br></details>

<details><summary><b>2.</b> Which loads are treated as inductive?</summary><br>Anything with a coil: motors, transformers, ballasts, chokes, solenoids, contactor/relay coils.<br><br><sub>A single conductor's inductance is tiny and usually ignored</sub><br><br></details>

<details><summary><b>3.</b> When does a magnetic field induce a voltage in a coil?</summary><br>Whenever flux cuts the coil, i.e. whenever the current (and its field) changes.<br><br><sub>Unit 13 fact 1</sub><br><br></details>

<details><summary><b>4.</b> What is CEMF?</summary><br>Counter-electromotive force: the induced voltage, which always opposes the applied voltage.<br><img src="cemf_180.png"><br><br><sub>Lenz's law</sub><br><br></details>

<details><summary><b>5.</b> What is the induced voltage proportional to?</summary><br>The RATE OF CHANGE of current, not the amount of current.<br><img src="rate_of_change.png"><br><br></details>

<details><summary><b>6.</b> What does an inductor oppose?</summary><br>A CHANGE in current.<br><br><sub>Like a flywheel for current</sub><br><br></details>

<details><summary><b>7.</b> <img src="cemf_180.png"><br>What is the phase relationship between applied voltage and induced voltage?</summary><br>180° (exactly opposite).<br><br></details>

<details><summary><b>8.</b> A coil (6 Ω wire) on 120 VAC draws 0.8 A. How much voltage pushes current through the wire resistance?</summary><br>E = 0.8 × 6 = <b>4.8 V</b>. The rest is used overcoming the CEMF.<br><br></details>

<details><summary><b>9.</b> Same coil: what is the induced voltage? Why not 120 − 4.8?</summary><br>√(120² − 4.8²) = <b>119.904 V</b>. The resistive drop and the CEMF are 90° apart, so subtract as vectors.<br><img src="coil_voltages.png"><br><br><sub>The book's earlier 120 − 116 = 4 example is only a rough illustration</sub><br><br></details>

<details><summary><b>10.</b> <img src="ohmmeter_coil.png"><br>A contactor coil reads 6 Ω on an ohmmeter. Does it draw 120/6 = 20 A on 120 VAC?</summary><br>No. The ohmmeter shows only wire resistance. Reactance limits the AC current to far less.<br><br></details>

<details><summary><b>11.</b> What is inductive reactance (Xₗ)?</summary><br>The current-limiting effect of inductance, in ohms. It isn't resistance: it comes from the CEMF and produces no heat.<br><br></details>

<details><summary><b>12.</b> Formula for Xₗ?</summary><br>Xₗ = 2πfL  (f in Hz, L in H, Xₗ in Ω)<br><br></details>

<details><summary><b>13.</b> Rearranged reactance formulas?</summary><br>L = Xₗ / (2πf) and f = Xₗ / (2πL)<br><br></details>

<details><summary><b>14.</b> What number should you memorize for 60 Hz, and why?</summary><br><b>377</b> (2π × 60 = 376.99). At 60 Hz, Xₗ = 377 × L and L = Xₗ / 377.<br><br><sub>Doesn't apply at other frequencies</sub><br><br></details>

<details><summary><b>15.</b> How does Ohm's law work with reactance?</summary><br>Put Xₗ in place of R: I = E / Xₗ, E = I × Xₗ, Xₗ = E / I.<br><br></details>

<details><summary><b>16.</b> Three factors that set induced voltage (and therefore Xₗ)?</summary><br>1. Number of turns<br>2. Strength of the magnetic field<br>3. Speed of the cutting action (frequency)<br><br></details>

<details><summary><b>17.</b> What physical features set a coil's inductance?</summary><br>Number of turns, how close together they are, wire/coil size, and core material (iron ≫ air).<br><br></details>

<details><summary><b>18.</b> 0.8 H on 120 V, 60 Hz. Xₗ and current?</summary><br>Xₗ = 377 × 0.8 = <b>301.6 Ω</b>; I = 120 / 301.6 = <b>0.398 A</b>.<br><br><sub>Example 16–1</sub><br><br></details>

<details><summary><b>19.</b> 36 V, 400 Hz, 0.2 A. Find L.</summary><br>Xₗ = 36/0.2 = 180 Ω; L = 180 / (2π × 400) = <b>0.0716 H</b>.<br><br><sub>Example 16–2: 377 does NOT apply at 400 Hz</sub><br><br></details>

<details><summary><b>20.</b> A coil draws 24 A on 480 V, 60 Hz. Current at 400 Hz?</summary><br>L doesn't change. Current scales with 1/f: 24 × 60/400 = <b>3.6 A</b>.<br><img src="xl_vs_frequency.png"><br><br><sub>Example 16–3</sub><br><br></details>

<details><summary><b>21.</b> Does inductance change when the frequency changes?</summary><br>No. L is set by construction. Xₗ changes, because Xₗ is proportional to f.<br><br><sub>Exception: iron cores saturate at high current</sub><br><br></details>

<details><summary><b>22.</b> What is a pure inductor's Xₗ at DC (0 Hz)?</summary><br>Zero. Only the wire resistance limits current.<br><br><sub>An AC coil on DC will burn up</sub><br><br></details>

<details><summary><b>23.</b> Raise the frequency: what happens to Xₗ and current?</summary><br>Xₗ goes up and current goes down (in proportion).<br><img src="xl_vs_frequency.png"><br><br></details>

<details><summary><b>24.</b> 60 Hz coil or transformer on 50 Hz: what happens?</summary><br>Xₗ drops about 17%, so current rises about 20%. It runs hotter, and an iron core may saturate.<br><br></details>

<details><summary><b>25.</b> 50 Hz magnetic ballast on 60 Hz: overcurrent risk?</summary><br>No. Xₗ is higher at 60 Hz, so current is lower. The likely trouble is underpowered or poor lamp starting.<br><br><sub>Practical Application 1</sub><br><br></details>

<details><summary><b>26.</b> What happens to an iron-core inductor at high current?</summary><br>The core saturates, inductance drops, and current climbs quickly. Air cores don't saturate.<br><br></details>

<details><summary><b>27.</b> Unit pitfall: 33 mH in the reactance formula?</summary><br>Convert to henrys first: 0.033 H. Likewise kHz → Hz.<br><br><sub>Practice Problem 2</sub><br><br></details>

<details><summary><b>28.</b> <img src="inductor_symbols.png"><br>What do these two schematic symbols mean?</summary><br>Plain coil = air-core inductor. Coil with parallel lines = iron-core inductor.<br><br><sub>16–3</sub><br><br></details>

<details><summary><b>29.</b> Total inductance of inductors in series?</summary><br>Lₜ = L₁ + L₂ + L₃ (likewise Xₗₜ = Xₗ₁ + Xₗ₂ + Xₗ₃)<br><img src="inductors_series.png"><br><br><sub>16–4</sub><br><br></details>

<details><summary><b>30.</b> Three 0.6, 0.4 and 0.5 H inductors in series: Lₜ?</summary><br><b>1.5 H</b><br><br><sub>Example 16–4</sub><br><br></details>

<details><summary><b>31.</b> Total inductance of inductors in parallel?</summary><br>1/Lₜ = 1/L₁ + 1/L₂ + 1/L₃ (product-over-sum for two; L/N for N equal ones)<br><img src="inductors_parallel.png"><br><br><sub>Same forms for Xₗ</sub><br><br></details>

<details><summary><b>32.</b> 2.5, 1.8 and 1.2 H in parallel: Lₜ?</summary><br>1 / (0.4 + 0.556 + 0.833) = <b>0.559 H</b><br><br><sub>Example 16–6</sub><br><br></details>

<details><summary><b>33.</b> Sanity check for parallel inductance?</summary><br>The total must be smaller than the smallest inductor.<br><br><sub>Forgetting the final reciprocal is the classic error</sub><br><br></details>

<details><summary><b>34.</b> When do the simple series/parallel inductor formulas NOT apply?</summary><br>When the coils are magnetically coupled (mutual inductance), e.g. close together or sharing a core.<br><br><sub>Transformers work this way</sub><br><br></details>

<details><summary><b>35.</b> In a pure inductor, how are current and voltage related in phase?</summary><br>Current LAGS the applied voltage by 90°.<br><img src="lag_90.png"><br><br><sub>16–6</sub><br><br></details>

<details><summary><b>36.</b> Explain the 90° lag in three steps.</summary><br>1. Induced V is max when current changes fastest (at its zero crossing), so current leads the induced V by 90°.<br>2. Induced V is 180° from the applied V.<br>3. So current lags the applied V by 90°.<br><img src="rate_of_change.png"><br><br></details>

<details><summary><b>37.</b> What does "ELI the ICE man" mean?</summary><br>ELI: in an inductor (L), E comes before I (current lags).<br>ICE: in a capacitor (C), I comes before E (current leads).<br><br></details>

<details><summary><b>38.</b> Is the lag exactly 90° in a real coil?</summary><br>No. Wire resistance makes it a bit less. Loaded motors are often 30–40°.<br><br></details>

<details><summary><b>39.</b> <img src="power_inductive.png"><br>How much true power does a pure inductor use?</summary><br>Zero watts. Energy is stored in the field and returned each cycle.<br><br><sub>16–7</sub><br><br></details>

<details><summary><b>40.</b> In a pure inductor, what fraction of the time do V and I have the same sign?</summary><br>50%. Same sign: energy goes into the field. Opposite sign: it returns. Net zero.<br><br><sub>Figure 16–15 A–D</sub><br><br></details>

<details><summary><b>41.</b> General power formula for any circuit?</summary><br>P = E × I × cos θ<br><br><sub>θ = phase angle between voltage and current</sub><br><br></details>

<details><summary><b>42.</b> cos θ for a resistive vs a pure inductive circuit?</summary><br>Resistive: cos 0° = 1 (P = E × I). Pure inductive: cos 90° = 0 (P = 0).<br><br></details>

<details><summary><b>43.</b> Where does the power an inductor DOES use come from?</summary><br>Losses: I²R in the wire, plus eddy-current and hysteresis losses in the iron core.<br><br></details>

<details><summary><b>44.</b> What are VARs?</summary><br>Volt-amperes-reactive: reactive power, the power that charges and returns the magnetic field.<br><br><sub>16–8</sub><br><br></details>

<details><summary><b>45.</b> Formulas for VARs?</summary><br>VARs = Eₗ × Iₗ = Eₗ² / Xₗ = Iₗ² × Xₗ<br><br><sub>Use the inductor's own voltage and current</sub><br><br></details>

<details><summary><b>46.</b> Are VARs harmless because they're not true power?</summary><br>No. They're real current in real conductors, which heats wires and transformers. That's why reactors carry kVAR ratings.<br><br></details>

<details><summary><b>47.</b> Inductor on 480 V drawing 125 A: minimum kVAR rating?</summary><br>480 × 125 / 1000 = <b>60 kVAR</b>. Less than that and it would likely be destroyed.<br><br><sub>Example 16–7</sub><br><br></details>

<details><summary><b>48.</b> What is the Q of an inductor?</summary><br>Quality: the ratio of reactance to resistance. Q = Xₗ / R (no units).<br><img src="coil_model.png"><br><br><sub>16–9</sub><br><br></details>

<details><summary><b>49.</b> Q formulas, rearranged?</summary><br>Q = Xₗ / R, Xₗ = Q × R, R = Xₗ / Q<br><br><sub>Review Q11–13</sub><br><br></details>

<details><summary><b>50.</b> High Q vs low Q coil construction?</summary><br>Large wire → low R → high Q. Many turns of fine wire → high R → low Q.<br><br></details>

<details><summary><b>51.</b> Above what Q is a coil treated as pure?</summary><br>Q ≥ 10. The resistance is then negligible.<br><img src="coil_q10.png"><br><br><sub>Xₗ 100, R 10 → Z = 100.5 Ω</sub><br><br></details>

<details><summary><b>52.</b> What is impedance (Z)?</summary><br>The total current-limiting effect (R and X combined), in ohms.<br><br></details>

<details><summary><b>53.</b> Why does Z = √(R² + Xₗ²), not R + Xₗ?</summary><br>R and Xₗ are 90° apart, so they form the legs of a right triangle, and Z is the hypotenuse.<br><img src="coil_q10.png"><br><br></details>

<details><summary><b>54.</b> 480 V, 60 Hz, 0.6 A, 150 Ω wire resistance. Find L.</summary><br>Z = 480/0.6 = 800 Ω. Xₗ = √(800² − 150²) = 785.8 Ω. L = 785.8/377 = <b>2.084 H</b>.<br><img src="coil_true_l.png"><br><br><sub>Procedure: Z = E/I → remove R → L = Xₗ/2πf</sub><br><br></details>

<details><summary><b>55.</b> E/I measured on a coil gives you Xₗ or Z?</summary><br>Z. It's only about equal to Xₗ when Q ≥ 10.<br><br></details>

<details><summary><b>56.</b> <img src="inductive_kick.png"><br>What is inductive kick?</summary><br>When a coil's circuit opens, its collapsing field produces a voltage spike many times the supply voltage.<br><br><sub>Arcing contacts; it's why coils get diodes, snubbers or MOVs</sub><br><br></details>

<details><summary><b>57.</b> Why discharge large windings after a DC winding-resistance or DLRO test?</summary><br>The DC test current stores energy in the field, and breaking the leads can produce a dangerous kick. Let the test set discharge it.<br><br></details>

<details><summary><b>58.</b> Why must you never open a loaded CT secondary?</summary><br>With nothing to limit it, the secondary voltage can rise to lethal levels. Short the secondary before disconnecting a meter or relay.<br><br></details>

<details><summary><b>59.</b> Why does a stuck-open contactor armature burn out the coil?</summary><br>The air gap lowers L, so Xₗ is low and the coil keeps drawing inrush current (several × sealed current).<br><br></details>

<details><summary><b>60.</b> Why do inductive loads lower power factor?</summary><br>They make current lag voltage, adding reactive current. Utilities surcharge low PF; capacitors correct it.<br><br><sub>Preview of later units</sub><br><br></details>

<details><summary><b>61.</b> What are VFD line reactors?</summary><br>Series inductors (rated in % impedance / kVAR) that limit inrush and fault current and smooth harmonics.<br><br></details>

<details><summary><b>62.</b> Replacement inductor: 324 V across it, 18 A, 1.2 Ω wire resistance, 480 V supply. Which voltage do you use?</summary><br>The 324 V measured across the inductor, not the 480 V supply. Z = 324/18, remove R, then L = Xₗ/377. VARs from the inductor's own V and I.<br><br><sub>Practical Application 2: compute Q to judge whether R matters</sub><br><br></details>
