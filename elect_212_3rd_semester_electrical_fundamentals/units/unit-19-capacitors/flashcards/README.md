# Flashcards — Unit 19: Capacitors

87 cards. Read the question, answer it in your head, then click it to check.

Study guide for this unit: [study-guide.md](../study-guide.md). The raw card data is in [`unit19_flashcards.json`](unit19_flashcards.json) if you want to import the cards into a flashcard app.

---

<details><summary><b>1.</b> What does a capacitor oppose?</summary><br>A change of <b>voltage</b>. (An inductor opposes a change of current.)<br><br><sub>Summary</sub><br><br></details>

<details><summary><b>2.</b> How is the simplest capacitor built?</summary><br>Two metal plates separated by an insulator called the dielectric.<br><img src="cap_construction.png"><br><br><sub>19–1</sub><br><br></details>

<details><summary><b>3.</b> <img src="cap_construction.png"><br>What is the dielectric?</summary><br>The insulating material between a capacitor's plates.<br><br><sub>Review Q1</sub><br><br></details>

<details><summary><b>4.</b> <img src="cap_symbols.png"><br>Identify these schematic symbols.</summary><br>Nonpolarized, polarized (electrolytic), variable, trimmer.<br><br><sub>Figures 19–2, 19–29</sub><br><br></details>

<details><summary><b>5.</b> Three factors that determine capacitance?</summary><br>1. Surface area of the plates<br>2. Distance between the plates<br>3. Type of dielectric<br><img src="capacitance_factors.png"><br><br><sub>Review Q2</sub><br><br></details>

<details><summary><b>6.</b> <img src="capacitance_factors.png"><br>How does each factor change capacitance?</summary><br>More area → more C. Plates closer → more C. Higher dielectric constant → more C.<br><br></details>

<details><summary><b>7.</b> What happens when a capacitor is connected to a DC source?</summary><br>Electrons leave the plate on the + terminal and pile onto the plate on the − terminal. Current flows until the capacitor voltage equals the source, then stops.<br><img src="rc_circuit.png"><br><br></details>

<details><summary><b>8.</b> When does current flow in a capacitor circuit?</summary><br>Only while the capacitor is charging or discharging.<br><br><sub>On AC, it's always charging/discharging, so current flows continuously</sub><br><br></details>

<details><summary><b>9.</b> What happens when the battery is removed from a charged capacitor?</summary><br>It stays charged as long as there's no path for the electrons between the plates.<br><br></details>

<details><summary><b>10.</b> What is leakage current?</summary><br>Current that creeps through the imperfect dielectric and slowly discharges the capacitor. Excessive leakage = a "leaky" capacitor.<br><br></details>

<details><summary><b>11.</b> Book error: "leakage current is proportional to the resistance of the dielectric." Fix it.</summary><br>It's inversely related: higher dielectric resistance means LESS leakage (I = V/R).<br><br></details>

<details><summary><b>12.</b> In what form does a capacitor store energy?</summary><br>In an electrostatic field, in the dielectric.<br><br><sub>Review Q4. Inductors use a magnetic field</sub><br><br></details>

<details><summary><b>13.</b> What does "electrostatic" mean?</summary><br>Electric charges that are stationary (not moving).<br><br></details>

<details><summary><b>14.</b> What is dielectric stress?</summary><br>The dielectric's electron orbits stretch toward the positive plate when charged. This is where the energy is stored, like a drawn bowstring.<br><img src="dielectric_stress.png"><br><br></details>

<details><summary><b>15.</b> <img src="dielectric_stress.png"><br>What is the dielectric stress proportional to?</summary><br>The voltage between the plates.<br><br><sub>Too much voltage breaks the dielectric down (short)</sub><br><br></details>

<details><summary><b>16.</b> What does a capacitor's voltage rating mean?</summary><br>The maximum voltage the dielectric is designed to withstand without breaking down.<br><br></details>

<details><summary><b>17.</b> Life-span rule: run a capacitor at half its rated voltage. Result?</summary><br>About 8 times longer life than at full rated voltage.<br><br><sub>U.S. military study</sub><br><br></details>

<details><summary><b>18.</b> Why can a capacitor deliver thousands of amps briefly?</summary><br>Energy stored slowly is released almost instantly when the leads are shorted.<br><br><sub>Camera flash: ~500 V capacitor dumps into a xenon tube</sub><br><br></details>

<details><summary><b>19.</b> Why is handing someone a charged capacitor dangerous?</summary><br>It can deliver enough energy to put a heart into fibrillation.<br><br><sub>Book caution</sub><br><br></details>

<details><summary><b>20.</b> Energy stored in a capacitor (formula)?</summary><br>W = ½ × C × V² (joules)<br><br><sub>Not in the book. Double V = 4× energy</sub><br><br></details>

<details><summary><b>21.</b> What is the dielectric constant?</summary><br>How many times more capacitance a material gives compared with vacuum (K = 1). Unitless.<br><img src="dielectric_constants.png"><br><br><sub>Book labels it F/in. — a typo</sub><br><br></details>

<details><summary><b>22.</b> Dielectric constants of air, paper, mica, water, ceramic?</summary><br>Air ≈ 1.006, paper ≈ 3.5, mica ≈ 6.4–7, pure water 81, ceramic up to ~1200.<br><img src="dielectric_constants.png"><br><br></details>

<details><summary><b>23.</b> Air capacitor = 3 µF. Insert a material (same spacing) and it's 15 µF. K?</summary><br>15 / 3 = <b>5</b><br><br><sub>Review Q3</sub><br><br></details>

<details><summary><b>24.</b> What is the basic unit of capacitance, and who is it named for?</summary><br>The farad (F), after Michael Faraday.<br><br></details>

<details><summary><b>25.</b> Define one farad.</summary><br>A change of 1 volt across the plates moves 1 coulomb of charge.<br><br></details>

<details><summary><b>26.</b> Formula linking charge, capacitance and voltage?</summary><br>Q = C × V (coulombs = farads × volts)<br><br></details>

<details><summary><b>27.</b> Why is the farad rarely used?</summary><br>It's enormous. A 1 F air capacitor with plates 1 in. apart would need about 1,108 square miles of plate.<br><br><sub>Example 19–1</sub><br><br></details>

<details><summary><b>28.</b> Values of µF, nF and pF?</summary><br>µF = 10⁻⁶ F, nF = 10⁻⁹ F, pF = 10⁻¹² F<br><br><sub>pF also written µµF or mmF</sub><br><br></details>

<details><summary><b>29.</b> An old motor capacitor is marked "35 MFD." What does MFD mean?</summary><br>Microfarads (35 µF), not megafarads.<br><br></details>

<details><summary><b>30.</b> Formula for capacitors in parallel?</summary><br>Cₜ = C₁ + C₂ + C₃<br><img src="caps_parallel.png"><br><br><sub>Same effect as bigger plates</sub><br><br></details>

<details><summary><b>31.</b> <img src="caps_parallel.png"><br>20, 30 and 60 µF in parallel?</summary><br><b>110 µF</b><br><br><sub>Figure 19–12</sub><br><br></details>

<details><summary><b>32.</b> Formulas for capacitors in series?</summary><br>1/Cₜ = 1/C₁ + 1/C₂ + …; two: C₁C₂/(C₁ + C₂); N equal: C/N<br><img src="caps_series.png"><br><br><sub>Same effect as wider plate spacing</sub><br><br></details>

<details><summary><b>33.</b> <img src="caps_series.png"><br>20, 30 and 60 µF in series?</summary><br><b>10 µF</b><br><br><sub>Example 19–2</sub><br><br></details>

<details><summary><b>34.</b> How do capacitor combinations compare with resistors?</summary><br>Opposite: capacitors ADD in parallel and use reciprocals in series.<br><br></details>

<details><summary><b>35.</b> When can you use Cₜ = C/N?</summary><br>Only when all the series capacitors are the same value.<br><br></details>

<details><summary><b>36.</b> Voltage across each capacitor in parallel?</summary><br>The full applied voltage. Each must be rated for it.<br><br></details>

<details><summary><b>37.</b> <img src="series_voltage_split.png"><br>Two equal capacitors in series on 480 V. Voltage on each?</summary><br>240 V each (equal capacitors split evenly).<br><br><sub>Practical App 3: two 50 µF 370 V caps = 25 µF for a 480 V job</sub><br><br></details>

<details><summary><b>38.</b> Unequal capacitors in series: which gets the most voltage?</summary><br>The SMALLEST capacitance (voltage is inversely proportional to C).<br><br><sub>Check each one's rating</sub><br><br></details>

<details><summary><b>39.</b> 2.2 µF + 280 nF + 470 pF in parallel. First step?</summary><br>Convert to one unit: 2.2 µF + 0.28 µF + 0.00047 µF ≈ 2.48 µF.<br><br><sub>Practice 4</sub><br><br></details>

<details><summary><b>40.</b> How do capacitors charge and discharge?</summary><br>At an exponential rate: fast at first, slowing as they approach full (or empty).<br><img src="charge_curve.png"><br><br></details>

<details><summary><b>41.</b> How much does the voltage change in each time constant?</summary><br>63.2% of the change still remaining.<br><img src="charge_curve.png"><br><br></details>

<details><summary><b>42.</b> <img src="charge_curve.png"><br>Charging to 100 V: voltage after 1, 2, 3, 4, 5 τ?</summary><br>63.2, 86.5, 95, 98.2, ~99.3 V (book rounds 86.4)<br><br></details>

<details><summary><b>43.</b> <img src="discharge_curve.png"><br>Discharging from 100 V: voltage after 1, 2, 3, 4, 5 τ?</summary><br>36.8, 13.5, 5, 1.8, ~0.7 V<br><br></details>

<details><summary><b>44.</b> How many time constants to fully charge or discharge?</summary><br>Five.<br><br><sub>Summary</sub><br><br></details>

<details><summary><b>45.</b> RC time constant formula and units?</summary><br>τ = R × C (ohms × farads = seconds)<br><br><sub>τ = tau</sub><br><br></details>

<details><summary><b>46.</b> Rearranged time-constant formulas?</summary><br>R = τ / C and C = τ / R. Total time = 5τ.<br><br></details>

<details><summary><b>47.</b> 50 µF and 100 kΩ: τ and total charge time?</summary><br>τ = 0.00005 × 100,000 = <b>5 s</b>; total = <b>25 s</b>.<br><br><sub>Example 19–3</sub><br><br></details>

<details><summary><b>48.</b> 100 pF must fully charge in 0.2 s. What resistance?</summary><br>τ = 0.2 / 5 = 0.04 s; R = 0.04 / (100 × 10⁻¹²) = <b>400 MΩ</b>.<br><br><sub>Example 19–4: divide total by 5 first</sub><br><br></details>

<details><summary><b>49.</b> 500 kΩ, total charge time 15 s. Capacitance?</summary><br>τ = 3 s; C = 3 / 500,000 = <b>6 µF</b>.<br><br><sub>Example 19–5</sub><br><br></details>

<details><summary><b>50.</b> What are charge and discharge times proportional to?</summary><br>Both the capacitance and the resistance in the circuit.<br><br><sub>Summary</sub><br><br></details>

<details><summary><b>51.</b> Name common applications for capacitors.</summary><br>PF correction, motor start/run, SCR/Triac phase shift, filtering pulsating DC, RC timing, frequency/pulse circuits.<br><br><sub>19–9</sub><br><br></details>

<details><summary><b>52.</b> Nonpolarized capacitors: other name, and where can they be used?</summary><br>"AC capacitors." They work on AC or DC, either way around.<br><br><sub>Review Q9: yes on DC</sub><br><br></details>

<details><summary><b>53.</b> How is an oil-filled paper capacitor built, and where is it used?</summary><br>Metal-foil plates separated by oil-soaked paper. Used for motor run/start capacitors and PF correction.<br><br></details>

<details><summary><b>54.</b> What does the dot, arrow or dash on an oil-filled capacitor mark?</summary><br>The terminal connected to the plate nearest the metal case (the one most likely to short to ground on failure).<br><br></details>

<details><summary><b>55.</b> Which side should the identified terminal connect to, and why?</summary><br>The LINE side, not the start winding. A short then goes straight to ground and trips the breaker fast. Via the start winding, reactance limits the fault and the winding can overheat.<br><img src="identified_terminal.png"><br><br><sub>Figures 19–21 / 19–22</sub><br><br></details>

<details><summary><b>56.</b> <img src="identified_terminal.png"><br>The identified mark is on the compressor's run-winding terminal. Wrong?</summary><br>Not necessarily. Trace it: if that terminal is the same node as the line, it's correct. The rule is keep it off the START winding.<br><br><sub>Practical App 1</sub><br><br></details>

<details><summary><b>57.</b> Polarized capacitors: other name, and where can they be used?</summary><br>Electrolytic capacitors. DC only, observing the marked polarity.<br><br></details>

<details><summary><b>58.</b> What happens if a polarized capacitor is reversed?</summary><br>It can be damaged and sometimes explodes.<br><br></details>

<details><summary><b>59.</b> Main advantage of electrolytic capacitors?</summary><br>Very high capacitance in a small case (the oxide insulating film is only a few molecules thick).<br><br></details>

<details><summary><b>60.</b> Wet-type electrolytic: construction and response to reversed polarity?</summary><br>Aluminum foil + borax electrolyte forming an oxide film. Reversed, the film dissolves and it shorts — but it REFORMS when polarity is corrected.<br><br></details>

<details><summary><b>61.</b> Dry-type electrolytic: what's different?</summary><br>The electrolyte is held in gauze (leak-proof), but reversed polarity PERMANENTLY damages it.<br><br><sub>Review Q11</sub><br><br></details>

<details><summary><b>62.</b> How is an AC electrolytic capacitor made?</summary><br>Two wet-type electrolytics back-to-back (negative to negative) in one case. Each half-cycle one forms while the other shorts.<br><img src="ac_electrolytic.png"><br><br><sub>Review Q10. Used as small-motor start caps and ceiling-fan run caps</sub><br><br></details>

<details><summary><b>63.</b> How does a variable capacitor work?</summary><br>Movable plates on a shaft interleave with fixed plates, changing the effective area. Air dielectric, rated in pF.<br><br></details>

<details><summary><b>64.</b> What is a trimmer capacitor?</summary><br>A small variable capacitor: a screw moves one plate closer to or farther from a fixed plate.<br><br></details>

<details><summary><b>65.</b> How are capacitor color codes read, in which unit?</summary><br>Digits, multiplier, tolerance (and voltage/class), with the value in picofarads. There's no single universal standard.<br><br><sub>Check manufacturer data</sub><br><br></details>

<details><summary><b>66.</b> Postage-stamp mica: what does a 6-dot code add over a 5-dot?</summary><br>The third dot becomes a third digit.<br><br></details>

<details><summary><b>67.</b> Mica code: first dot white vs black?</summary><br>White = EIA standard (silver = paper dielectric). Black = JAN (Joint Army-Navy, military).<br><br><sub>Review Q15 starts with black</sub><br><br></details>

<details><summary><b>68.</b> On a ceramic capacitor, what does the wide band mean?</summary><br>The temperature coefficient.<br><br><sub>19–15</sub><br><br></details>

<details><summary><b>69.</b> What is a temperature coefficient?</summary><br>How much capacitance changes with temperature, in ppm/°C. P = increases with heat; N = decreases.<br><br><sub>NP0 ≈ zero</sub><br><br></details>

<details><summary><b>70.</b> What is a dipped tantalum capacitor?</summary><br>A match-head-shaped capacitor coded with color bands/dots for value, tolerance and voltage.<br><br><sub>19–16</sub><br><br></details>

<details><summary><b>71.</b> <img src="film_code.png"><br>Read the film capacitor code "105 K".</summary><br>10 + five zeros = 1,000,000 pF = <b>1 µF</b>; K = ±10%.<br><br><sub>19–17</sub><br><br></details>

<details><summary><b>72.</b> Tolerance letters J, K, M, H?</summary><br>J ±5%, K ±10%, M ±20%, H ±3%<br><br></details>

<details><summary><b>73.</b> Read "253 H".</summary><br>25 + 3 zeros = 25,000 pF = <b>0.025 µF</b>, ±3%.<br><br><sub>Review Q13</sub><br><br></details>

<details><summary><b>74.</b> First step before testing any capacitor?</summary><br>Discharge it through a resistor/discharge tool and verify zero volts with a meter.<br><br></details>

<details><summary><b>75.</b> <img src="ohmmeter_test.png"><br>What does a good capacitor do on an analog ohmmeter?</summary><br>The needle swings up-scale, then returns to infinity. Reversing the leads swings about twice as far, then returns.<br><br><sub>Stays low = shorted</sub><br><br></details>

<details><summary><b>76.</b> Why does the needle swing twice as far when you reverse the leads?</summary><br>The capacitor is already charged to the meter's voltage, so reversing adds that charge to the new one.<br><br></details>

<details><summary><b>77.</b> <img src="leakage_test.png"><br>How do you test a capacitor for leakage?</summary><br>Apply rated DC through a microammeter in series. Once charged, current should be zero (or near it).<br><br><sub>Summary bullet</sub><br><br></details>

<details><summary><b>78.</b> What is a HIPOT?</summary><br>A dielectric test set ("high potential"): variable high voltage, a voltmeter and a microammeter, used to test dielectric strength at rated voltage.<br><br></details>

<details><summary><b>79.</b> <img src="capacitance_test.png"><br>How do you measure actual capacitance with AC?</summary><br>Apply AC (≤ rated voltage), measure current. Xc = E / I, then C = 1 / (2πf × Xc).<br><br><sub>Finds open plates. At 60 Hz, C(µF) ≈ 2652 × I / E</sub><br><br></details>

<details><summary><b>80.</b> Two tests needed for a large AC capacitor?</summary><br>1. Dielectric strength (short/leakage).<br>2. Capacitance value (open plates).<br><br></details>

<details><summary><b>81.</b> Is a capacitor safe once the power is off?</summary><br>No. It can stay charged for a long time. Verify zero volts (VFD buses, PF banks, power supplies).<br><br></details>

<details><summary><b>82.</b> How should you discharge a capacitor?</summary><br>Through a properly sized resistor or discharge tool — not a screwdriver.<br><br><sub>A dead short can weld tools and throw molten metal</sub><br><br></details>

<details><summary><b>83.</b> What does the NEC require for PF-correction capacitors?</summary><br>A means of discharging stored voltage (bleed resistors) — for low-voltage caps, to 50 V or less within 1 minute (Article 460).<br><br><sub>Don't trust it; measure</sub><br><br></details>

<details><summary><b>84.</b> Replacing a run capacitor: which ratings must match?</summary><br>Same µF (within tolerance), same OR HIGHER voltage rating. 440 V can replace 370 V; never the reverse.<br><br></details>

<details><summary><b>85.</b> Start vs run capacitors: interchangeable?</summary><br>No. Start caps (AC electrolytic, high µF) are intermittent duty only. Run caps (oil/film) are continuous duty.<br><br></details>

<details><summary><b>86.</b> Signs of a failed run capacitor?</summary><br>Bulged top, leaking oil, motor hums but won't start, motor runs hot. A dual cap (HERM/FAN/C) can fail on one section.<br><br></details>

<details><summary><b>87.</b> A 240 VAC circuit needs a 10 µF cap; the spare is 350 WVDC. What must you compare?</summary><br>The AC PEAK (240 × 1.414 ≈ 339 V) against the DC rating. It barely fits — and an AC-duty rating is preferred.<br><br><sub>Practical App 2</sub><br><br></details>
