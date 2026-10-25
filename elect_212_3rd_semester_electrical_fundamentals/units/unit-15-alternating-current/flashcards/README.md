# Flashcards — Unit 15: Alternating Current

75 cards. Read the question, answer it in your head, then click it to check.

Study guide for this unit: [study-guide.md](../study-guide.md). The raw card data is in [`unit15_flashcards.json`](unit15_flashcards.json) if you want to import the cards into a flashcard app.

---

<details><summary><b>1.</b> What is the single biggest advantage of AC over DC?</summary><br>AC can be transformed (stepped up or down with a transformer); DC can't (without electronics).<br><br><sub>15–1</sub><br><br></details>

<details><summary><b>2.</b> Why transmit power at high voltage?</summary><br>For the same power, higher voltage means less current. Line loss is I²R, so 1/10 the current gives 1/100 the loss, and smaller wire.<br><br><sub>Common transmission voltages: 69, 138, 345 kV</sub><br><br></details>

<details><summary><b>3.</b> Is "DC can't be transformed" still strictly true?</summary><br>Not today. Power electronics convert DC to DC (chargers, solar optimizers, HVDC lines). Give the book's answer on the book's test.<br><br></details>

<details><summary><b>4.</b> History check: which event is usually credited with settling AC vs DC lighting?</summary><br>The 1893 World's Columbian Exposition in Chicago (Westinghouse won). The book says 1904 St. Louis.<br><br><sub>Use the book's answer on the book's test</sub><br><br></details>

<details><summary><b>5.</b> How does AC differ from DC?</summary><br>AC reverses its direction of flow at regular intervals; DC flows one way.<br><br><sub>Summary</sub><br><br></details>

<details><summary><b>6.</b> <img src="waveform_types.png"><br>Name the three AC waveforms shown.</summary><br>Square, triangle, and sine.<br><br></details>

<details><summary><b>7.</b> How are square waves usually produced?</summary><br>By electronic switching circuits called oscillators.<br><br><sub>Cheap inverters/UPS: "modified sine" = stepped square</sub><br><br></details>

<details><summary><b>8.</b> What is a linear wave?</summary><br>One whose voltage changes at a constant rate, so it plots as straight lines (e.g., the triangle wave).<br><br><sub>100 V at 2 ms → 50 V at 1 ms</sub><br><br></details>

<details><summary><b>9.</b> Why is the sine wave the most common AC waveform?</summary><br>Every rotating machine (generator or alternator) produces one.<br><br></details>

<details><summary><b>10.</b> How many electrical degrees are in one sine wave?</summary><br>360°<br><img src="sine_cycle.png"><br><br><sub>Review Q2</sub><br><br></details>

<details><summary><b>11.</b> Where does a sine wave hit +peak, zero, and −peak?</summary><br>+peak at 90°, zero at 180°, −peak at 270°, back to zero at 360°.<br><img src="sine_cycle.png"><br><br><sub>Review Q3: max negative at 270°</sub><br><br></details>

<details><summary><b>12.</b> What is a cycle?</summary><br>One complete waveform: 0 → +peak → 0 → −peak → 0 (360°).<br><br></details>

<details><summary><b>13.</b> What is frequency, and what is its unit?</summary><br>The number of complete cycles per second, measured in hertz (Hz).<br><br><sub>60 Hz in US/Canada; 50 Hz most of the world</sub><br><br></details>

<details><summary><b>14.</b> Formulas linking period and frequency?</summary><br>T = 1/f and f = 1/T (T in seconds, f in Hz).<br><br></details>

<details><summary><b>15.</b> Period of 60 Hz?</summary><br>1/60 = <b>16.67 ms</b>; a peak every 8.33 ms.<br><br></details>

<details><summary><b>16.</b> 1200 Hz: time for one cycle?</summary><br>T = 1/1200 = <b>0.833 ms</b><br><br><sub>Example 15–1</sub><br><br></details>

<details><summary><b>17.</b> A cycle takes 0.04 ms. Frequency?</summary><br>0.04 ms = 0.00004 s, so f = 1/0.00004 = <b>25 kHz</b>.<br><br><sub>Example 15–2: convert prefixes first</sub><br><br></details>

<details><summary><b>18.</b> Prefix values: ms, µs, kHz, MHz?</summary><br>ms = 10⁻³ s, µs = 10⁻⁶ s, kHz = 10³ Hz, MHz = 10⁶ Hz<br><br></details>

<details><summary><b>19.</b> Electrical vs mechanical degrees on a 4-pole machine?</summary><br>One mechanical revolution = 720 electrical degrees (2 cycles). They're only equal on a 2-pole machine.<br><br><sub>Needed later for motor speed</sub><br><br></details>

<details><summary><b>20.</b> What happens to a 60 Hz motor run on 50 Hz?</summary><br>It runs at about 5/6 speed and can overheat. Always check the nameplate frequency.<br><br><sub>Aircraft use 400 Hz</sub><br><br></details>

<details><summary><b>21.</b> Why does generator voltage follow a sine curve?</summary><br>The loop cuts flux slowly near 0° (moving almost parallel) and fastest at 90° (moving straight across). The cutting rate follows sin θ.<br><br><sub>1 V is induced when flux is cut at 1 Wb/s; 1 Wb = 10⁸ lines</sub><br><br></details>

<details><summary><b>22.</b> Instantaneous value formula?</summary><br>e(inst) = E(max) × sin θ<br><img src="instantaneous_values.png"><br><br><sub>Rearranged: E(max) = e/sin θ; sin θ = e/E(max)</sub><br><br></details>

<details><summary><b>23.</b> 100 V peak: voltage at 30°? at 45°?</summary><br>30°: 100 × 0.5 = <b>50 V</b>. 45°: 100 × 0.707 = <b>70.7 V</b>.<br><img src="instantaneous_values.png"><br><br></details>

<details><summary><b>24.</b> 138 V peak: voltage at 78°?</summary><br>138 × sin 78° ≈ <b>135 V</b><br><br><sub>Example 15–3</sub><br><br></details>

<details><summary><b>25.</b> 246 V at 53°. What's the peak?</summary><br>246 / sin 53° ≈ <b>308 V</b><br><br><sub>Example 15–4</sub><br><br></details>

<details><summary><b>26.</b> 350 V peak. At what angle is it 53 V?</summary><br>sin⁻¹(53/350) = <b>8.7°</b>, and also 180° − 8.7° = <b>171.3°</b>.<br><img src="two_angles.png"><br><br><sub>Example 15–5. The book gives 8.685° because it rounded early</sub><br><br></details>

<details><summary><b>27.</b> <img src="two_angles.png"><br>Why does every voltage value occur twice per half-cycle?</summary><br>The wave passes it once rising and once falling: at θ and at 180° − θ. sin⁻¹ only gives the first.<br><br></details>

<details><summary><b>28.</b> What sign is the voltage between 180° and 360°?</summary><br>Negative (sine is negative there). sin 225° = −0.707.<br><br></details>

<details><summary><b>29.</b> How do you handle an angle over 360°?</summary><br>Subtract 360°: 400° is the same as 40°.<br><br><sub>One practice-table row uses 400°</sub><br><br></details>

<details><summary><b>30.</b> Angle and time are linked how?</summary><br>θ = 360° × f × t<br><br></details>

<details><summary><b>31.</b> Name the four values used to describe a sine wave.</summary><br>Peak-to-peak, peak, RMS, and average.<br><img src="peak_pp_rms.png"><br><br><sub>15–3</sub><br><br></details>

<details><summary><b>32.</b> What is peak (amplitude)?</summary><br>From zero to the highest point in either direction.<br><img src="peak_pp_rms.png"><br><br><sub>Peak = ½ p-p</sub><br><br></details>

<details><summary><b>33.</b> What is peak-to-peak?</summary><br>From +peak to −peak (2 × peak). It's the easiest value to read off an oscilloscope.<br><br></details>

<details><summary><b>34.</b> 100 V peak AC and 100 V DC each across 100 Ω. Same heat?</summary><br>No. DC: 100 W. AC at 100 V peak: only 50 W, because it's below 100 V most of the time.<br><img src="rms_heating.png"><br><br><sub>Figure 15–10</sub><br><br></details>

<details><summary><b>35.</b> What does RMS (effective value) mean?</summary><br>The AC value that produces the same heat as that much DC.<br><img src="rms_heating.png"><br><br><sub>Root-Mean-Square: square every value, average them, take the root</sub><br><br></details>

<details><summary><b>36.</b> RMS ↔ peak conversions (sine wave)?</summary><br>RMS = peak × 0.707 (÷ √2)<br>Peak = RMS × 1.414 (× √2)<br><br></details>

<details><summary><b>37.</b> 354 V peak → RMS?</summary><br>354 × 0.707 = <b>250 V</b><br><br><sub>Example 15–6</sub><br><br></details>

<details><summary><b>38.</b> 120 V RMS → peak? peak-to-peak?</summary><br>Peak ≈ <b>170 V</b>; p-p ≈ <b>339 V</b>.<br><br><sub>Example 15–7</sub><br><br></details>

<details><summary><b>39.</b> Peak values of 208, 240, 277, 480 V systems?</summary><br>294, 339, 392, 679 V<br><img src="rms_peak_table.png"><br><br><sub>Know these for component ratings</sub><br><br></details>

<details><summary><b>40.</b> What value do AC voltmeters/ammeters, nameplates and the NEC use?</summary><br>RMS, unless stated otherwise.<br><br></details>

<details><summary><b>41.</b> What value are component voltage ratings (diodes, capacitors, MOVs, ballast maximums) often given in?</summary><br>Peak. Convert the system's RMS voltage to peak before comparing.<br><br><sub>Practical App 2: 277 V RMS ≈ 392 V peak</sub><br><br></details>

<details><summary><b>42.</b> Do 0.707 and 1.414 work for every waveform?</summary><br>No, only sine waves. Square wave: RMS = peak. Triangle: RMS = 0.577 × peak.<br><img src="rms_by_waveform.png"><br><br></details>

<details><summary><b>43.</b> <img src="distorted_current.png"><br>Why use a True RMS meter?</summary><br>Average-responding meters assume a sine wave. On distorted loads (VFDs, LED drivers, computers) they can read 20–40% off, usually low.<br><br></details>

<details><summary><b>44.</b> Book typo: "100 V RMS applied to a 100-V resistor" — fix it.</summary><br>It should say a 100-Ω resistor.<br><br></details>

<details><summary><b>45.</b> "It's only 120 V." What does the insulation actually see?</summary><br>About 170 V peak, twice every cycle.<br><br></details>

<details><summary><b>46.</b> What is the average of a full, unrectified sine wave over one cycle?</summary><br>Zero. The + and − halves cancel.<br><br><sub>Average values only mean something after rectification</sub><br><br></details>

<details><summary><b>47.</b> What does a rectifier do?</summary><br>Uses diodes to let current flow in one direction only, turning AC into DC.<br><img src="bridge_rectifier.png"><br><br></details>

<details><summary><b>48.</b> Full-wave vs half-wave rectifier?</summary><br>Full-wave (bridge, 4 diodes): both halves flipped positive. Half-wave (1 diode): the negative half is blocked.<br><img src="rectified.png"><br><br></details>

<details><summary><b>49.</b> What are pulsating DC and ripple?</summary><br>Pulsating DC rises and falls but never reverses. Ripple is the bumps in it.<br><br></details>

<details><summary><b>50.</b> Full-wave average formulas?</summary><br>avg = peak × 0.637 = RMS × 0.9<br><img src="rectified.png"><br><br><sub>0.637 × 1.414 = 0.9</sub><br><br></details>

<details><summary><b>51.</b> Half-wave average formulas?</summary><br>avg = peak × 0.318 = RMS × 0.45 (half of full-wave)<br><img src="rectified.png"><br><br></details>

<details><summary><b>52.</b> 120 V RMS into a full-wave rectifier: average DC?</summary><br>120 × 0.9 = <b>108 V</b><br><br><sub>Example 15–8</sub><br><br></details>

<details><summary><b>53.</b> 277 V into a half-wave rectifier: average DC?</summary><br>277 × 0.45 = <b>124.65 V</b><br><br><sub>Example 15–9</sub><br><br></details>

<details><summary><b>54.</b> 88 V peak-to-peak: average value?</summary><br>Halve first: 44 V peak. Then 44 × 0.637 ≈ <b>28 V</b>.<br><br><sub>Review Q9: using p-p directly is the classic mistake</sub><br><br></details>

<details><summary><b>55.</b> <img src="filter_capacitor.png"><br>A capacitor is added after the rectifier. What does the DC read now?</summary><br>Close to peak (≈ 1.414 × RMS), not 0.9 × RMS.<br><br><sub>480 V VFD DC bus ≈ 650–680 VDC. Treat it as live until verified discharged.</sub><br><br></details>

<details><summary><b>56.</b> What does a DC voltmeter read on pulsating DC?</summary><br>The average value.<br><br></details>

<details><summary><b>57.</b> What is wavelength (λ)?</summary><br>The distance a radiated wave travels during one cycle.<br><img src="wavelength.png"><br><br></details>

<details><summary><b>58.</b> Wavelength formula?</summary><br>λ = 300,000,000 m/s ÷ f (answer in meters)<br><br><sub>Using 186,000 mi/s gives miles</sub><br><br></details>

<details><summary><b>59.</b> Wavelength at 100 MHz? At 60 Hz?</summary><br>100 MHz: <b>3 m</b>. 60 Hz: about <b>5,000 km</b> (≈3,100 mi), which is why power wiring isn't an antenna.<br><br></details>

<details><summary><b>60.</b> Two characteristics of a resistive load?</summary><br>1. It produces heat.<br>2. Voltage and current are in phase.<br><br><sub>15–4</sub><br><br></details>

<details><summary><b>61.</b> Examples of resistive loads?</summary><br>Heaters, water-heater and range elements, incandescent lamps.<br><br></details>

<details><summary><b>62.</b> In a pure resistive AC circuit, do the DC Ohm's law and power formulas work?</summary><br>Yes, unchanged, as long as every value is RMS.<br><br><sub>Never mix peak and RMS</sub><br><br></details>

<details><summary><b>63.</b> Exception: is an incandescent lamp a constant resistance?</summary><br>No. The cold filament is about 1/10 of its hot resistance, so there's a large inrush at switch-on.<br><br></details>

<details><summary><b>64.</b> Name the three basic types of AC loads.</summary><br>Resistive, inductive, capacitive.<br><br><sub>Summary</sub><br><br></details>

<details><summary><b>65.</b> Why is power always positive in a resistive AC circuit?</summary><br>Voltage and current always have the same sign: + × + = +, and − × − = +.<br><img src="resistive_power.png"><br><br><sub>15–5</sub><br><br></details>

<details><summary><b>66.</b> <img src="resistive_power.png"><br>At what frequency does power pulse in a 60 Hz resistive circuit?</summary><br>120 Hz (twice line frequency), because it peaks on both half-cycles.<br><br><sub>Source of 120 Hz lamp flicker</sub><br><br></details>

<details><summary><b>67.</b> Average power vs peak power (resistive)?</summary><br>Average = ½ of peak. W = E(RMS) × I(RMS).<br><br><sub>100 V pk × 1 A pk = 100 W pk → 50 W avg</sub><br><br></details>

<details><summary><b>68.</b> Preview: what happens to power when V and I are out of phase?</summary><br>During part of each cycle they have opposite signs, so power is negative and flows back to the source. That's reactive power.<br><br><sub>Units 16–17</sub><br><br></details>

<details><summary><b>69.</b> What is skin effect?</summary><br>With AC, current crowds toward the conductor's surface, which raises its effective resistance.<br><img src="skin_effect.png"><br><br><sub>15–6</sub><br><br></details>

<details><summary><b>70.</b> How does skin effect change with frequency?</summary><br>It increases as frequency increases.<br><br></details>

<details><summary><b>71.</b> Does skin effect matter at 60 Hz?</summary><br>For ordinary building wire, no. For large conductors (≈500 kcmil+) and bus bar, yes. That's why NEC Ch. 9 Table 9 lists AC resistance separately.<br><br><sub>Skin depth in copper at 60 Hz ≈ 8.5 mm</sub><br><br></details>

<details><summary><b>72.</b> How do you reduce skin effect for high-frequency grounding?</summary><br>Use conductors with a lot of surface area: wide copper strap or flat braid.<br><br><sub>Green Tip</sub><br><br></details>

<details><summary><b>73.</b> Why do harmonics increase conductor heating?</summary><br>Harmonic currents (180, 300 Hz…) have stronger skin effect and add I²R losses.<br><br><sub>K-rated transformers, oversized neutrals</sub><br><br></details>

<details><summary><b>74.</b> Why must all conductors of an AC circuit run in the same raceway?</summary><br>A lone conductor heats surrounding steel by induction. Grouping them cancels the field. (NEC 300.3(B), 300.20)<br><br><sub>Related to, but not the same as, skin effect</sub><br><br></details>

<details><summary><b>75.</b> 240 V AC bridge feeding a crane magnet with 400 V diodes. What must you compare?</summary><br>The diodes' peak rating with the peak of 240 V RMS (≈339 V). Leave margin for high line voltage and spikes.<br><br><sub>Practical App 1: then DC out = 240 × 0.9</sub><br><br></details>
