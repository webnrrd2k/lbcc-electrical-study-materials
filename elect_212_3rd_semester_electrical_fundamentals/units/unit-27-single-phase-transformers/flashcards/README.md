# Flashcards — Unit 27: Single-Phase Transformers

211 cards. Read the question, answer it in your head, then click it to check.

Study guide for this unit: [study-guide.md](../study-guide.md). The raw card data is in [`unit27_flashcards.json`](unit27_flashcards.json) if you want to import the cards into a flashcard app.

---

<details><summary><b>1.</b> Why is AC (not DC) used for power distribution?</summary><br>AC can be transformed. Stepping voltage up cuts current, so power travels long distances on smaller wire with less I²R loss.<br><img src="grid_steps.png"><br><br><sub>Doubling voltage halves current and cuts line loss to 1/4.</sub><br><br></details>

<details><summary><b>2.</b> Why won't a transformer work on steady DC?</summary><br>Only a CHANGING flux induces voltage. Steady DC makes constant flux, so nothing is induced, and the winding only sees its low resistance (it can overheat).<br><br><sub>Faraday's law: induced voltage depends on rate of change of flux.</sub><br><br></details>

<details><summary><b>3.</b> How is energy transferred from primary to secondary in a conventional transformer?</summary><br>Magnetically, through a shared changing flux in the iron core. There is no electrical connection between windings.<br><img src="xfmr_basic.png"><br><br><sub>Exception: the autotransformer, which shares one winding.</sub><br><br></details>

<details><summary><b>4.</b> In the slide demo, what happens to the lamp as the coils move closer, and when an iron core is added?</summary><br>It gets brighter both times. More of the primary's flux links the secondary (better coupling). Iron carries flux far more easily than air.<br><br><sub>Iron has high permeability.</sub><br><br></details>

<details><summary><b>5.</b> What mechanical device is a transformer most like?</summary><br>A gearbox. Gears trade speed for torque; a transformer trades voltage for current. Turns ratio = gear ratio, and power stays (almost) the same.<br><br><sub>Friction in gears ≈ core and copper losses.</sub><br><br></details>

<details><summary><b>6.</b> State the power rule that solves most transformer problems.</summary><br>Power in ≈ power out:  E<sub>P</sub> × I<sub>P</sub> = E<sub>S</sub> × I<sub>S</sub> (VA in = VA out).<br><img src="step_up_down.png"><br><br><sub>If more VA comes out than goes in, your math is wrong.</sub><br><br></details>

<details><summary><b>7.</b> Which side of a transformer carries the higher current?</summary><br>The low-voltage side. High voltage side = low current.<br><br><sub>Check every current answer with a VA check.</sub><br><br></details>

<details><summary><b>8.</b> Higher voltage lets you use smaller conductors. What is the trade-off?</summary><br>Insulation and clearances. Higher voltage needs thicker insulation and more spacing.<br><br><sub>Conductor area needed for a given loss goes as 1/V².</sub><br><br></details>

<details><summary><b>9.</b> Power transformer vs distribution transformer?</summary><br>Power transformer: between generator and primary distribution (substations, large). Distribution transformer: from primary distribution (4–35 kV) to the customer's service (e.g., 120/240 V).<br><br></details>

<details><summary><b>10.</b> Are 'primary' and 'secondary' fixed labels?</summary><br>No. Primary = the side the power enters. Feed a step-down unit from its low side and it becomes a step-up unit.<br><br><sub>H/X marks voltage level; primary/secondary marks power direction.</sub><br><br></details>

<details><summary><b>11.</b> Write the transformer EMF equation and define each term.</summary><br>E<sub>rms</sub> = 4.44 × f × N × Φ<sub>max</sub>. f = frequency (Hz), N = turns, Φmax = peak core flux (Wb).<br><br><sub>Every turn sees the same flux, so voltage per turn is the same on both windings.</sub><br><br></details>

<details><summary><b>12.</b> What happens if a 60 Hz transformer is run on 50 Hz at the same voltage?</summary><br>Flux rises about 20% (E = 4.44 f N Φ). The core can saturate, magnetizing current jumps, and it overheats.<br><br><sub>Overvoltage has the same effect.</sub><br><br></details>

<details><summary><b>13.</b> What is excitation (magnetizing) current?</summary><br>The small current the primary draws with no load, to magnetize the core. Typically a few percent of FLC or less, lagging voltage by nearly 90°.<br><br><sub>An unloaded transformer looks like an inductor.</sub><br><br></details>

<details><summary><b>14.</b> How does the primary 'know' that load was added to the secondary?</summary><br>Secondary current makes an opposing flux. The primary automatically draws more current to cancel it and keep core flux constant.<br><br><sub>The load sets the current; the transformer just passes it through.</sub><br><br></details>

<details><summary><b>15.</b> Why are transformer cores laminated?</summary><br>Thin, insulated silicon-steel sheets break up eddy-current paths, so the circulating currents (and their heat) stay small.<br><img src="laminations.png"><br><br><sub>Solid iron would act like a shorted turn.</sub><br><br></details>

<details><summary><b>16.</b> What are eddy currents?</summary><br>Circulating currents induced in the core iron itself by the changing flux. They waste power as heat.<br><br><sub>Reduced by thin insulated laminations.</sub><br><br></details>

<details><summary><b>17.</b> What is hysteresis loss, and how is it reduced?</summary><br>Energy lost each cycle re-magnetizing the iron. Reduced by using silicon steel with a narrow hysteresis loop.<br><br><sub>Hysteresis + eddy = core (iron) loss.</sub><br><br></details>

<details><summary><b>18.</b> Core loss vs copper loss: which changes with load?</summary><br>Core (iron) loss is roughly constant whenever energized. Copper (I²R) loss rises with the square of load current.<br><img src="efficiency_curve.png"><br><br><sub>Max efficiency occurs where they're equal.</sub><br><br></details>

<details><summary><b>19.</b> Core form vs shell form construction?</summary><br>Core form: windings surround the core legs. Shell form: the core surrounds the windings.<br><img src="core_shell.png"><br><br><sub>Core form is common on HV/large units; shell form on small units.</sub><br><br></details>

<details><summary><b>20.</b> The slides say core air gaps increase efficiency. Is that right?</summary><br>No. Air gaps raise magnetizing current and lower efficiency. They're used deliberately in reactors, ballasts, neon and flyback transformers to store energy or limit current.<br><br><sub>Slide 48 error.</sub><br><br></details>

<details><summary><b>21.</b> Transformer efficiency formula and typical range?</summary><br>%Eff = P<sub>out</sub> ÷ P<sub>in</sub> × 100. Typically 96–99%.<br><br><sub>Among the most efficient machines made.</sub><br><br></details>

<details><summary><b>22.</b> Why does oversizing a transformer 'for safety' waste energy?</summary><br>Core loss is paid 24/7 whether loaded or not. A lightly loaded big unit runs at low efficiency.<br><br></details>

<details><summary><b>23.</b> Write the turns, voltage and current ratio equation.</summary><br>N<sub>P</sub>/N<sub>S</sub> = E<sub>P</sub>/E<sub>S</sub> = I<sub>S</sub>/I<sub>P</sub><br><br><sub>Voltage goes WITH turns; current goes AGAINST turns.</sub><br><br></details>

<details><summary><b>24.</b> What is TTR?</summary><br>Transformer turns ratio: primary turns to secondary turns, usually written high side to low side (e.g., 10:1).<br><br><sub>Also the name of the field test that measures it.</sub><br><br></details>

<details><summary><b>25.</b> What is 'ampere-turns balance'?</summary><br>I<sub>P</sub> × N<sub>P</sub> = I<sub>S</sub> × N<sub>S</sub>. Primary ampere-turns equal secondary ampere-turns.<br><br><sub>Same as saying current ratio is the inverse of turns ratio.</sub><br><br></details>

<details><summary><b>26.</b> 1Ø 2,400–480 V transformer, I<sub>P</sub> = 15 A. Find TTR and I<sub>S</sub>.</summary><br>TTR = 2,400 ÷ 480 = 5:1. I<sub>S</sub> = 5 × 15 = 75 A. Check: 2,400×15 = 480×75 = 36,000 VA.<br><br><sub>Slides 59–60.</sub><br><br></details>

<details><summary><b>27.</b> 480–120 V (4:1) transformer. 240 V is applied to the primary. Secondary voltage?</summary><br>240 ÷ 4 = 60 V.<br><br><sub>The output is always proportional to the input.</sub><br><br></details>

<details><summary><b>28.</b> 480–120 V (4:1) transformer. 240 V is applied to the SECONDARY. What appears on the primary?</summary><br>240 × 4 = 960 V.<br><br><sub>The ratio is fixed and works both directions. That's how backfeed happens.</sub><br><br></details>

<details><summary><b>29.</b> What is reflected impedance?</summary><br>The primary sees the load impedance times the turns ratio squared: Z<sub>P</sub> = (N<sub>P</sub>/N<sub>S</sub>)² × Z<sub>S</sub>.<br><br><sub>A 2 Ω load on a 10:1 transformer looks like 200 Ω from the primary.</sub><br><br></details>

<details><summary><b>30.</b> A winding is tapped. Which turns do you use to compute TTR?</summary><br>The whole winding, unless the problem says which tap is used. E.g., 2,400 V to a center-tapped 240 V winding = 10:1.<br><br></details>

<details><summary><b>31.</b> Primary taps: 1,200 turns (240 V), 1,040 turns (208 V), 600 turns (120 V); secondary 120 turns, 24 V. Using the 1,040 tap, what is the ratio and primary voltage?</summary><br>1,040 ÷ 120 = 8.67:1; 8.67 × 24 V = 208 V.<br><br><sub>Slide 239.</sub><br><br></details>

<details><summary><b>32.</b> A 2:1 transformer is fed 438 V instead of 480 V. Output?</summary><br>219 V (not 240 V). A transformer can't correct low supply voltage; pick a tap that matches the actual supply.<br><br><sub>Slide 240.</sub><br><br></details>

<details><summary><b>33.</b> The slides say more primary turns makes a stronger field and more secondary current. What's actually true?</summary><br>At a fixed supply voltage, more primary turns means LESS flux and LOWER secondary voltage. Secondary current is set by the load.<br><br><sub>Slide 53 error.</sub><br><br></details>

<details><summary><b>34.</b> What is backfeeding a transformer?</summary><br>Energizing it from the 'wrong' side, usually the secondary. It steps the voltage up to full primary voltage on lines thought to be dead.<br><img src="backfeed.png"><br><br><sub>Classic case: a generator plugged into a house without a transfer switch.</sub><br><br></details>

<details><summary><b>35.</b> Before working on a transformer, which sides must be disconnected?</summary><br>BOTH primary and secondary. LOTO, test, and ground as necessary (work between grounds).<br><br><sub>Any transformer can be backfed.</sub><br><br></details>

<details><summary><b>36.</b> When removing an installed transformer, which leads come off first?</summary><br>The secondary (low-voltage) leads, to remove the backfeed path.<br><br></details>

<details><summary><b>37.</b> Why are transformers rated in VA, not watts?</summary><br>Heating depends on current, and current depends on VA regardless of power factor. A watt rating would let low-PF loads overheat the unit.<br><img src="va_vs_watts.png"><br><br><sub>Slide 78: 50 kW at PF 0.7 = 71.4 kVA vs 55.6 kVA at PF 0.9.</sub><br><br></details>

<details><summary><b>38.</b> FLC vs FLA?</summary><br>Same thing: full-load current/amps, the current the transformer can carry continuously at rated conditions.<br><br></details>

<details><summary><b>39.</b> Single-phase full-load current formula?</summary><br>I<sub>FL</sub> = VA ÷ E = kVA × 1,000 ÷ E.<br><br><sub>Three-phase: divide by E × 1.732.</sub><br><br></details>

<details><summary><b>40.</b> 1Ø 25 kVA, 240–120 V. Primary and secondary FLC?</summary><br>Primary: 25,000 ÷ 240 = 104.2 A. Secondary: 25,000 ÷ 120 = 208.3 A.<br><br><sub>kVA primary = kVA secondary.</sub><br><br></details>

<details><summary><b>41.</b> 1Ø 2,000 kVA, 12 kV–2.4 kV. Primary and secondary FLC?</summary><br>Primary: 2,000,000 ÷ 12,000 = 166.7 A. Secondary: 2,000,000 ÷ 2,400 = 833.3 A.<br><br><sub>833.3 ÷ 166.7 = 5 = TTR.</sub><br><br></details>

<details><summary><b>42.</b> How can you get the TTR from the full-load currents?</summary><br>Divide the secondary FLC by the primary FLC (high current ÷ low current).<br><br></details>

<details><summary><b>43.</b> Single-phase amps-per-kVA rule of thumb?</summary><br>Amps per kVA = 1,000 ÷ V. 120 V → 8.33, 240 V → 4.17, 480 V → 2.08, 2,400 V → 0.42.<br><img src="amps_per_kva.png"><br><br><sub>The slide's rounded chart (4, 2, 0.4) reads a few percent low.</sub><br><br></details>

<details><summary><b>44.</b> Name the common single-phase distribution transformer sizes.</summary><br>10, 15, 25, 37.5, 50, 75, 100, 150, 167 kVA.<br><br></details>

<details><summary><b>45.</b> A 50 kW load at PF 0.85 needs what size transformer?</summary><br>VA = W ÷ PF = 50,000 ÷ 0.85 = 58.8 kVA → next standard size up: 75 kVA.<br><br><sub>Never round down.</sub><br><br></details>

<details><summary><b>46.</b> Clamp-on: 200 A on each leg of a 240 V single-phase 60 kVA transformer. Load and % loaded?</summary><br>200 × 240 = 48 kVA. 48 ÷ 60 = 80% loaded.<br><br><sub>Slides 86–87.</sub><br><br></details>

<details><summary><b>47.</b> Unbalanced 120/240 V: L1 = 20 A, L2 = 30 A, N = 10 A. kVA load?</summary><br>(20 + 30) × 120 V = 6 kVA. Ignore the neutral current.<br><br><sub>Each 120 V half delivers its line current at 120 V.</sub><br><br></details>

<details><summary><b>48.</b> What is the limitation of a load check with a clamp meter?</summary><br>It's a snapshot. Peak demand (hot afternoon, evening) matters more than a single reading.<br><br></details>

<details><summary><b>49.</b> What is BIL?</summary><br>Basic Impulse Insulation Level: the peak lightning-type surge voltage (kV crest) the insulation can withstand without damage.<br><br><sub>Much higher than operating voltage, e.g., ~95 kV BIL for 15 kV-class gear.</sub><br><br></details>

<details><summary><b>50.</b> Name 8 items found on a transformer nameplate.</summary><br>Any 8: manufacturer, serial no., kVA, phases, frequency, HV and LV voltages, FLCs, temperature rise, %Z, polarity, connection diagram, tap table, cooling/insulation type, BIL, weight, oil volume.<br><br><sub>NEC 450.11 requires marking. The nameplate is a formal document.</sub><br><br></details>

<details><summary><b>51.</b> In '12,470 – 240', what does the dash mean?</summary><br>It separates the windings. First voltage = the side receiving power (primary), second = secondary.<br><br></details>

<details><summary><b>52.</b> 120/240 vs 240/120: what's the difference?</summary><br>120/240 = two separate 120 V coils (can be series for 3-wire or parallel). 240/120 = one 240 V coil with a center tap (3-wire only; can't parallel).<br><img src="voltage_notation.png"><br><br><sub>Order matters!</sub><br><br></details>

<details><summary><b>53.</b> What is a dry-type transformer?</summary><br>A self air-cooled transformer: air circulates through vents in a sheet-metal case. Most indoor building transformers.<br><br></details>

<details><summary><b>54.</b> Two jobs of oil in an oil-immersed transformer?</summary><br>Cooling (carries heat to tank and fins by convection) and insulation. It also keeps paper insulation from drying out and oxidizing.<br><br><sub>Mineral oil is flammable, so NEC Art. 450 Part II has stricter rules for it.</sub><br><br></details>

<details><summary><b>55.</b> How does natural convection cool an oil-filled transformer?</summary><br>Hot oil near the core rises (less dense), carries heat to the tank and radiators, cools, sinks, and returns.<br><br></details>

<details><summary><b>56.</b> What is Askarel, and what precautions apply?</summary><br>A nonflammable synthetic insulating liquid made of PCBs. Banned from new manufacture since the late 1970s. Toxic: avoid contact and fumes; it's hazardous waste.<br><br><sub>Less fire hazard than oil, but a health hazard.</sub><br><br></details>

<details><summary><b>57.</b> What ambient temperature are transformer ratings based on?</summary><br>40 °C maximum (30 °C average over 24 h).<br><br></details>

<details><summary><b>58.</b> A 65 °C rise transformer in a 40 °C ambient: average max winding temperature?</summary><br>40 + 65 = 105 °C. The hot spot runs higher still (insulation class covers it).<br><img src="temp_rise.png"><br><br><sub>Slide 106.</sub><br><br></details>

<details><summary><b>59.</b> Same kVA: 55 °C rise vs 65 °C rise unit. Which has more overload headroom?</summary><br>The 55 °C (lower-rise) unit. More copper/iron and better cooling: the 'young, healthy runner'.<br><br></details>

<details><summary><b>60.</b> Besides load current, name 4 factors that limit transformer loading.</summary><br>Cooling medium, ambient temperature, duration of overloads, rated temperature rise, altitude (also harmonics, blocked vents, low oil).<br><br></details>

<details><summary><b>61.</b> Overload vs fault?</summary><br>Overload: more than rated current through the normal path; damage is slow, from heat. Fault: current through an abnormal path, often many times rated; protection must clear it fast.<br><br><sub>An overload is NOT a fault.</sub><br><br></details>

<details><summary><b>62.</b> Why can a transformer tolerate short overloads?</summary><br>Thermal mass: temperature lags load by minutes to hours. Long overloads still age insulation fast (rule of thumb: life halves per ~8–10 °C over rating).<br><br></details>

<details><summary><b>63.</b> NEC 450.3(B) (≤1,000 V): what are the two overcurrent protection options?</summary><br>1) Primary only at ≤125% of primary FLC. 2) Primary up to 250% WITH secondary protection at ≤125% of secondary FLC.<br><br><sub>Next standard size up allowed when ≥9 A. Check your enforced NEC edition.</sub><br><br></details>

<details><summary><b>64.</b> Why is transformer primary protection sized well above 100% of FLC?</summary><br>Inrush: energizing can draw roughly 8–12× FLC for a few cycles while the core magnetizes.<br><br><sub>Time-delay fuses are common on primaries.</sub><br><br></details>

<details><summary><b>65.</b> Does protecting the transformer protect the secondary conductors?</summary><br>No. Secondary conductors need their own protection under NEC 240.21(C) (10 ft / 25 ft rules, etc.).<br><br></details>

<details><summary><b>66.</b> What do H and X terminal markings mean?</summary><br>H = high-voltage terminals (H1, H2, H0...). X = low-voltage terminals (X1, X2, X0...).<br><br><sub>H/X is about voltage level, not which side is the primary.</sub><br><br></details>

<details><summary><b>67.</b> The basic polarity rule?</summary><br>H1 and X1 are positive at the same instant (H2 and X2 negative).<br><br></details>

<details><summary><b>68.</b> Facing the low-voltage side, where is H1 normally?</summary><br>On your left (back-left bushing).<br><br></details>

<details><summary><b>69.</b> Additive vs subtractive: where is X1?</summary><br>Subtractive: X1 on the SAME side as H1 ('same side subtractive'). Additive: X1 diagonally opposite H1.<br><img src="polarity_add_sub.png"><br><br></details>

<details><summary><b>70.</b> Can polarity be changed from outside the transformer?</summary><br>No. It's set by winding direction and how the leads are brought out. You connect to suit it.<br><br></details>

<details><summary><b>71.</b> Which single-phase transformers are normally additive?</summary><br>Units of 200 kVA or less with HV of 8,660 V or less (ANSI C57.12.00). Larger or higher-voltage units are subtractive.<br><br><sub>Most pole-top distribution transformers are additive.</sub><br><br></details>

<details><summary><b>72.</b> Why is subtractive polarity preferred on large/HV units?</summary><br>Lower voltage stress between adjacent HV and LV leads: half the DIFFERENCE of the voltages vs half the SUM for additive.<br><br><sub>Slide 472.</sub><br><br></details>

<details><summary><b>73.</b> Can an additive and a subtractive transformer be paralleled?</summary><br>Yes, if you connect by H1/X1 markings (polarity), not by physical bushing position.<br><br></details>

<details><summary><b>74.</b> Describe the AC polarity test.</summary><br>Jumper H1 to the adjacent LV terminal. Apply low AC across H1–H2. Measure H2 to the other adjacent LV terminal. Higher than applied = additive; lower = subtractive.<br><img src="polarity_test.png"><br><br></details>

<details><summary><b>75.</b> Polarity test on a 4:1 unit with 120 V applied. What do additive and subtractive read?</summary><br>Secondary = 30 V. Additive: 120 + 30 = 150 V. Subtractive: 120 − 30 = 90 V.<br><br></details>

<details><summary><b>76.</b> Describe the DC 'kick' polarity test.</summary><br>Analog DC voltmeter on the LV winding. Briefly connect a battery to the HV winding (+ on the lead you call H1). Up-scale kick on MAKE → the LV lead on meter + is X1.<br><img src="kick_test.png"><br><br><sub>The break kick goes the other way; ignore it. Keep hands off: breaking DC on a winding makes a voltage spike.</sub><br><br></details>

<details><summary><b>77.</b> Why does the kick test only deflect momentarily?</summary><br>Voltage is induced only while flux is changing (when current starts or stops). Steady DC = no induced voltage.<br><br><sub>Lenz/Faraday.</sub><br><br></details>

<details><summary><b>78.</b> Series vs parallel connection of a 120/240 V secondary (25 kVA)?</summary><br>Series (X2–X3 jumpered): 120/240 V 3-wire, 104 A. Parallel (X1–X3, X2–X4): 120 V 2-wire, 208 A.<br><img src="series_parallel_sec.png"><br><br><sub>kVA is the same either way.</sub><br><br></details>

<details><summary><b>79.</b> Two secondary coils in series with one reversed: what happens?</summary><br>The voltages cancel: about 0 V instead of the sum.<br><img src="series_wrong.png"><br><br></details>

<details><summary><b>80.</b> Two secondary coils in parallel with one reversed: what happens?</summary><br>A dead short across both coils: huge current, blown fuse, damaged windings.<br><br></details>

<details><summary><b>81.</b> Does paralleling secondaries increase available kVA?</summary><br>No. It only changes how the available current is delivered (more amps at lower voltage).<br><br><sub>25 kVA ÷ 240 = 104 A; 25 kVA ÷ 120 = 208 A.</sub><br><br></details>

<details><summary><b>82.</b> Requirements for paralleling two transformers?</summary><br>Same voltage ratio (and tap), same/similar %Z, correct polarity; for 3Ø also same phase sequence and angular displacement.<br><br><sub>Mismatched ratio → circulating current even at no load. Mismatched %Z → unequal sharing.</sub><br><br></details>

<details><summary><b>83.</b> 50 kVA and 100 kVA transformers in parallel share a 75 kVA load. How much does each carry?</summary><br>50 kVA unit: 75 × 50/150 = 25 kVA. 100 kVA unit: 75 × 100/150 = 50 kVA.<br><br><sub>Assumes matched %Z.</sub><br><br></details>

<details><summary><b>84.</b> Test before making the final parallel connection?</summary><br>Read voltage across the open connection. ~0 V → connect. Voltage present (~double) → polarity wrong, DO NOT connect.<br><img src="parallel_test.png"><br><br><sub>Connecting wrong = huge circulating current.</sub><br><br></details>

<details><summary><b>85.</b> In a paralleled bank, one transformer's primary fuse blows. Is its primary dead?</summary><br>No. The other unit backfeeds it through the paralleled secondaries. Its primary stays at full voltage. The good unit may also be overloaded.<br><br><sub>Treat all primaries in a parallel bank as hot.</sub><br><br></details>

<details><summary><b>86.</b> Why is the center point of a 120/240 V 3-wire secondary grounded?</summary><br>To limit voltage to ground (120 V), provide a fault-current path, and limit voltages from lightning, surges or primary contact.<br><br></details>

<details><summary><b>87.</b> If the 120/240 V neutral were NOT grounded and L1 faulted to ground, what would L2's voltage to ground be?</summary><br>240 V.<br><br></details>

<details><summary><b>88.</b> What current does the neutral of a 120/240 V 3-wire system carry?</summary><br>The DIFFERENCE between L1 and L2 currents (the unbalance). Balanced = 0 A.<br><br><sub>The slide's 'sum of the unbalanced load' wording is wrong.</sub><br><br></details>

<details><summary><b>89.</b> 25 kVA 120/240 V: side 1 = 167 A, side 2 = 42 A. How loaded is each half?</summary><br>Each half is rated 12.5 kVA = 104 A. Side 1: 167/104 = 160% (60% overloaded). Side 2: 42/104 = 40% loaded.<br><img src="unbalanced_25.png"><br><br><sub>Total is exactly 25 kVA, yet one winding is overloaded. (Slide says '40% underloaded' — it's 40% loaded.)</sub><br><br></details>

<details><summary><b>90.</b> 75 kVA 12,500–120/240 V. Loads: 6 kVA @240 V, 3 kVA @120 V on L1 side, 3.6 kVA @120 V on L2 side. Find L1, L2, N and primary currents.</summary><br>240 V load 25 A; 3 kVA = 25 A; 3.6 kVA = 30 A. L1 = 50 A, L2 = 55 A, N = 5 A. Primary ≈ 12,600 ÷ 12,500 ≈ 1.0 A. Loaded 16.8%.<br><img src="three_wire_75.png"><br><br><sub>Slides 227–231.</sub><br><br></details>

<details><summary><b>91.</b> Open neutral on 120/240 V: what happens to the 120 V loads?</summary><br>Loads on opposite sides go in SERIES across 240 V. Voltage divides by resistance: the lighter load (higher R) gets the HIGHER voltage.<br><br><sub>Lights going bright/dim when a load cycles = open neutral. Emergency.</sub><br><br></details>

<details><summary><b>92.</b> Open neutral: 3 kVA and 3.6 kVA 120 V loads on opposite sides. Voltage on each?</summary><br>R = 4.8 Ω and 4.0 Ω; I = 240 ÷ 8.8 = 27.3 A. 3 kVA load: 131 V. 3.6 kVA load: 109 V.<br><img src="open_neutral.png"><br><br><sub>The slide figure has these reversed.</sub><br><br></details>

<details><summary><b>93.</b> What does %Z mean on a transformer nameplate?</summary><br>The percent of rated primary voltage needed to push full-load current through a shorted secondary.<br><br><sub>Tells you fault current and voltage regulation.</sub><br><br></details>

<details><summary><b>94.</b> Why is transformer impedance given in percent instead of ohms?</summary><br>One number works for both sides. In ohms, HV and LV values differ (by the turns ratio squared).<br><br></details>

<details><summary><b>95.</b> A 480 V transformer has 5 %Z. At what voltage does FLA flow with the secondary shorted, and what is the fault current at 480 V?</summary><br>0.05 × 480 = 24 V. At 480 V the fault current is 480/24 = 20 × FLA.<br><img src="pctz_test.png"><br><br><sub>5% = 1/20.</sub><br><br></details>

<details><summary><b>96.</b> Maximum short-circuit current formula from %Z?</summary><br>I<sub>SC</sub> = I<sub>FL</sub> × 100 ÷ %Z (infinite source).<br><img src="fault_multiplier.png"><br><br><sub>Real fault current is somewhat lower; this is the worst case.</sub><br><br></details>

<details><summary><b>97.</b> 25 kVA, 240 V, 2 %Z. Maximum fault current?</summary><br>FLC = 104.2 A. I<sub>SC</sub> = 104.2 × 100/2 = 5,208 A.<br><br></details>

<details><summary><b>98.</b> How is %Z measured (short-circuit test)?</summary><br>Short the secondary (ammeter in series), voltmeter on the primary, raise primary voltage from a Variac until rated FLC flows. %Z = that primary voltage ÷ rated × 100.<br><br><sub>Slides call this 'determining FLC' and say record the secondary voltage — it's %Z and the PRIMARY voltage.</sub><br><br></details>

<details><summary><b>99.</b> Low %Z vs high %Z: trade-offs?</summary><br>Low %Z: better voltage regulation, but higher fault current (higher AIC and arc-flash). High %Z: limits fault current, but more voltage drop/dip under load.<br><br><sub>%Z is a design choice, not a quality grade (slide 196 overstates this).</sub><br><br></details>

<details><summary><b>100.</b> A transformer is replaced with one of lower %Z. What must you check downstream?</summary><br>Interrupting ratings / SCCR of breakers and fuses (NEC 110.9), the available fault current marking (110.24), and arc-flash labels.<br><br></details>

<details><summary><b>101.</b> What is an isolation transformer?</summary><br>A 1:1 transformer used only for isolation: blocks spikes/noise, breaks ground loops, feeds sensitive equipment.<br><br><sub>Often has a grounded electrostatic shield.</sub><br><br></details>

<details><summary><b>102.</b> What grounding does an isolation transformer secondary need?</summary><br>It's a separately derived system (NEC 250.30): system bonding jumper, grounding electrode conductor, supply-side bonding jumper.<br><br><sub>Without it, a ground fault on the secondary won't trip anything.</sub><br><br></details>

<details><summary><b>103.</b> What is a buck-boost transformer?</summary><br>A small isolating transformer wired as an autotransformer with its LV winding in series with the line, to raise or lower voltage ~5–27%.<br><br></details>

<details><summary><b>104.</b> Boost vs buck connection: 120 V supply, 24 V winding?</summary><br>Boost (additive): 120 + 24 = 144 V. Buck (subtractive): 120 − 24 = 96 V.<br><img src="buck_boost.png"><br><br></details>

<details><summary><b>105.</b> Why is correct voltage important for motors?</summary><br>Low voltage raises motor current, lowers torque and raises temperature, shortening insulation life.<br><br></details>

<details><summary><b>106.</b> A 1 kVA buck-boost unit (24 V secondary) boosts 120 V to 144 V. About how much load can it feed?</summary><br>Secondary current limit = 1,000 ÷ 24 = 41.7 A. Load ≈ 41.7 × 144 ≈ 6 kVA.<br><br><sub>It only carries the 'difference' power. Size by load current.</sub><br><br></details>

<details><summary><b>107.</b> What is an autotransformer?</summary><br>A one-winding transformer: the same winding is both primary and secondary.<br><img src="autotransformer.png"><br><br><sub>Most efficient type; the shared section carries only the difference current.</sub><br><br></details>

<details><summary><b>108.</b> Two disadvantages of autotransformers?</summary><br>1) No isolation between HV and LV sides. 2) If the common winding opens while stepping down, full line voltage appears at the load.<br><br></details>

<details><summary><b>109.</b> What is a Variac?</summary><br>A variable autotransformer: a brush rides on the winding to give adjustable output from 0 to slightly above line voltage.<br><br><sub>Used in the lab bench supplies.</sub><br><br></details>

<details><summary><b>110.</b> NEC-permitted uses of autotransformers (from the slides)?</summary><br>Systems with a grounded conductor common to both sides; motor starting; theater dimming; lighting ballasts; buck/boost under certain conditions.<br><br><sub>NEC 210.9, 215.11, 450.4.</sub><br><br></details>

<details><summary><b>111.</b> What is a control transformer?</summary><br>Steps 240/480 V down to 120 V (or 24 V) for control circuits (coils, pilot lights, PLC I/O).<br><br></details>

<details><summary><b>112.</b> Dual-primary control transformer (240 × 480): how are primaries connected for each voltage?</summary><br>480 V: primaries in SERIES (jumper H2–H3). 240 V: primaries in PARALLEL (H1–H3, H2–H4).<br><img src="control_xfmr.png"><br><br><sub>Slide 247 mislabels the parallel case.</sub><br><br></details>

<details><summary><b>113.</b> Why is one side (X2) of a control transformer secondary often grounded?</summary><br>So a ground fault in the control circuit blows the fuse instead of energizing a coil and starting a motor.<br><br></details>

<details><summary><b>114.</b> Neon sign transformer voltages and currents?</summary><br>Primary 120/240 V; secondary 2,000–15,000 V; 30–120 mA. Self air-cooled, mounted in the sign.<br><br><sub>Current-limiting by design. NEC Art. 600. Lethal despite mA rating.</sub><br><br></details>

<details><summary><b>115.</b> What does a constant-current transformer do, and where is it used?</summary><br>Holds secondary current constant (usually 6.6 A) as load changes. Used on series streetlights and airport runway lighting.<br><img src="cct.png"><br><br><sub>Primary typically 2,400 V.</sub><br><br></details>

<details><summary><b>116.</b> Why are series streetlights/runway lights fed from a CCT?</summary><br>Series wiring saves copper, and lamp brightness tracks current closely, so regulating current keeps brightness steady.<br><br></details>

<details><summary><b>117.</b> How does a CCT regulate current mechanically?</summary><br>A movable coil floats; the windings' fields repel. More current pushes them apart, increasing leakage and reducing current. A counterweight and oil dashpot prevent 'hunting'.<br><br></details>

<details><summary><b>118.</b> Why must you never open a live series lighting (CCT) circuit?</summary><br>The regulator drives voltage to maximum trying to keep current flowing: several kV across the opening.<br><br></details>

<details><summary><b>119.</b> In a series lighting circuit, what keeps the circuit closed when a lamp fails?</summary><br>A film cutout or a reactor (reactance coil) at each lamp.<br><br></details>

<details><summary><b>120.</b> What is a K-rated transformer?</summary><br>One built to withstand extra heating from harmonic currents drawn by non-linear loads.<br><img src="harmonics.png"><br><br><sub>K-1 = linear loads only; common ratings K-4, K-13, K-20.</sub><br><br></details>

<details><summary><b>121.</b> Name 5 loads that produce harmonics.</summary><br>Any 5: switch-mode power supplies (PCs, TVs), VFDs, LED/fluorescent ballasts, UPSs, PV inverters, arc furnaces, welders, solid-state dimmers/heater controls, HVDC converters.<br><br></details>

<details><summary><b>122.</b> Why can the neutral of a 4-wire wye carry more current than the phases?</summary><br>Triplen harmonics (3rd, 9th...) from non-linear loads add in the neutral instead of cancelling.<br><br><sub>K-rated units often have a double-size neutral.</sub><br><br></details>

<details><summary><b>123.</b> How do you determine what K-rating is needed?</summary><br>Measure K-factor with a power-quality meter with the system fully loaded.<br><br></details>

<details><summary><b>124.</b> What is a no-load tap changer (NLTC), and the key rule for using it?</summary><br>A switch that changes the turns ratio (taps usually in 2½% steps). It must only be moved with the transformer DE-ENERGIZED.<br><br><sub>Substation load tap changers (LTCs) are different: they work under load.</sub><br><br></details>

<details><summary><b>125.</b> Secondary voltage is too low. Do you move to a higher or lower % primary tap?</summary><br>LOWER % tap (fewer primary turns) raises the output. Higher % tap lowers it.<br><img src="tap_direction.png"><br><br><sub>E.g., 95% tap raises output ~5%.</sub><br><br></details>

<details><summary><b>126.</b> What does a transformer pressure relief device do?</summary><br>A spring-loaded valve vents internal pressure from a fault or overheating so the tank doesn't rupture, then reseals. A flag stays up; often has alarm/trip contacts.<br><br><sub>A tripped PRD means a serious internal event: test before re-energizing.</sub><br><br></details>

<details><summary><b>127.</b> Wye: relationship of line and phase voltage and current?</summary><br>E<sub>L</sub> = 1.732 × E<sub>P</sub>; I<sub>L</sub> = I<sub>P</sub>.<br><img src="wye_delta.png"><br><br><sub>E.g., 208 V line → 120 V phase.</sub><br><br></details>

<details><summary><b>128.</b> Delta: relationship of line and phase voltage and current?</summary><br>E<sub>L</sub> = E<sub>P</sub>; I<sub>L</sub> = 1.732 × I<sub>P</sub>.<br><br><sub>Phase current inside a delta can't be clamped from outside.</sub><br><br></details>

<details><summary><b>129.</b> Three-phase kVA formula?</summary><br>kVA = E<sub>L</sub> × I<sub>L</sub> × 1.732 ÷ 1,000.<br><br></details>

<details><summary><b>130.</b> Forming a wye from three 1Ø cans: what gets connected together?</summary><br>The non-polarity terminals (H2s or X2s). That common point is the neutral; the polarity terminals become the lines.<br><br></details>

<details><summary><b>131.</b> Forming a delta from three 1Ø cans?</summary><br>Polarity to non-polarity around the loop (X1 of A to X2 of B, etc.). No neutral.<br><br></details>

<details><summary><b>132.</b> Advantages of three single-phase cans over one 3Ø tank?</summary><br>Replace one failed unit, keep one spare, run open-delta on two units (57.7% capacity).<br><br><sub>A single 3Ø tank is smaller, cheaper and more efficient.</sub><br><br></details>

<details><summary><b>133.</b> Test before closing a delta?</summary><br>Read voltage across the open corner. ~0 V (small reading OK) → close. ~2× winding voltage → a winding is reversed; DO NOT close.<br><img src="delta_close.png"><br><br><sub>Use a meter rated for at least 2× winding voltage.</sub><br><br></details>

<details><summary><b>134.</b> The four basic 3Ø transformer connections?</summary><br>Delta–delta, delta–wye, wye–delta, wye–wye.<br><br><sub>Delta–wye (e.g., 480 V → 208Y/120) is most common in buildings.</sub><br><br></details>

<details><summary><b>135.</b> What are instrument transformers for?</summary><br>Step high voltage/current down to safe standard values (120 V, 5 A) for meters, relays and SCADA, and isolate those devices from the primary.<br><br><sub>Small VA, high accuracy.</sub><br><br></details>

<details><summary><b>136.</b> PT vs CT connection and secondary rating?</summary><br>PT: in PARALLEL, 120 V secondary (115 V older). CT: in SERIES, 5 A secondary.<br><img src="pt_ct_connect.png"><br><br></details>

<details><summary><b>137.</b> The opposite safety rules for PTs and CTs?</summary><br>Never SHORT a PT secondary. Never OPEN a CT secondary.<br><br></details>

<details><summary><b>138.</b> Why must you never short a PT secondary?</summary><br>A PT is a voltage source; a short draws destructive current (slides: primary current could rise ~200×).<br><br><sub>PT primaries are fused; never remove a ground from an energized PT.</sub><br><br></details>

<details><summary><b>139.</b> Why must PT fuses/switches be opened when working on connected equipment?</summary><br>A PT can backfeed: voltage on its secondary steps up to full primary voltage.<br><br></details>

<details><summary><b>140.</b> Why must you never open the secondary of an energized CT?</summary><br>The CT is driven by primary current. With nothing to oppose the flux, it acts as a step-up transformer: thousands of volts, shock, arcing, insulation and core damage.<br><img src="ct_open_hazard.png"><br><br><sub>Short it at the shorting block or test switch first.</sub><br><br></details>

<details><summary><b>141.</b> Standard CT secondary current?</summary><br>5 A at rated primary current, regardless of primary rating.<br><br><sub>1 A secondaries also exist (common outside N. America, long runs).</sub><br><br></details>

<details><summary><b>142.</b> Name 4 CT types.</summary><br>Window/donut/ring, split-core, bar type, wound type, bushing type.<br><br><sub>Window CTs are less accurate at low ratios than wound CTs.</sub><br><br></details>

<details><summary><b>143.</b> A 600:5 CT has 300 A in the primary. Secondary current?</summary><br>600:5 = 120:1, so 300 ÷ 120 = 2.5 A.<br><br></details>

<details><summary><b>144.</b> Shortcut for finding the ratio of an X:5 CT?</summary><br>Double the primary number and drop the last zero. 600:5 → 120:1; 2000:5 → 400:1.<br><br><sub>Works because ÷5 = ×2 ÷10.</sub><br><br></details>

<details><summary><b>145.</b> CT current ratio vs turns ratio?</summary><br>I<sub>S</sub>/I<sub>P</sub> = N<sub>P</sub>/N<sub>S</sub>. A 600:5 window CT has 120 secondary turns.<br><br></details>

<details><summary><b>146.</b> 600:5 multi-ratio CT (X1–X2 20, X2–X3 10, X3–X4 50, X4–X5 40 turns). Which taps give 150:5?</summary><br>150:5 = 30:1 → 20 + 10 → X1–X3. Leave other taps open.<br><img src="ct_taps.png"><br><br><sub>Slides 381–382.</sub><br><br></details>

<details><summary><b>147.</b> Tapped CT: X1–X2 = 40, X1–X3 = 60, X1–X4 = 160, X1–X5 = 240 turns. Which taps give 500:5?</summary><br>500:5 = 100:1 → 160 − 60 = 100 → X3–X4.<br><br><sub>Slide 383.</sub><br><br></details>

<details><summary><b>148.</b> On a multi-ratio CT, what do you do with the unused taps?</summary><br>Leave them OPEN. Don't short them.<br><br></details>

<details><summary><b>149.</b> How does passing the primary through a window CT twice change its ratio?</summary><br>It halves it: 200:5 becomes 100:5. New ratio = nameplate ratio ÷ number of passes.<br><img src="ct_window.png"><br><br></details>

<details><summary><b>150.</b> How do you count 'turns' on a window CT?</summary><br>Count passes THROUGH the window, not loops around the outside. One loop around the housing = 2 passes.<br><br></details>

<details><summary><b>151.</b> 200:5 CT with 3 and with 4 passes?</summary><br>3 passes: 66.7:5 (13.3:1). 4 passes: 50:5 (10:1).<br><br></details>

<details><summary><b>152.</b> 2500/5 donut CT. How many passes for a 125:1 ratio?</summary><br>2500/5 = 500:1; 500 ÷ 125 = 4 passes.<br><br><sub>Slide 394.</sub><br><br></details>

<details><summary><b>153.</b> What is CT burden?</summary><br>Everything connected to the secondary: meters, relays, transducers, and lead wire resistance (VA or ohms).<br><br><sub>Excess burden reduces accuracy.</sub><br><br></details>

<details><summary><b>154.</b> What is CT saturation, and what is the knee point?</summary><br>Past a point, more primary current gives no more secondary current. The bend in the excitation curve is the knee point.<br><img src="ct_saturation.png"><br><br><sub>A saturated protection CT under-reports fault current; relay may not trip.</sub><br><br></details>

<details><summary><b>155.</b> Name 4 factors affecting CT accuracy.</summary><br>Burden, accuracy class, rating factor, load, external magnetic fields, temperature, physical configuration, tap selected.<br><br></details>

<details><summary><b>156.</b> How many points should a CT secondary circuit be grounded at?</summary><br>One point only (IEEE C57.13.3). NEC Art. 250 Part X covers instrument transformer grounding.<br><br></details>

<details><summary><b>157.</b> Should spare CTs be stored open or shorted?</summary><br>Shorted, including in storage and shipping.<br><br></details>

<details><summary><b>158.</b> Can you megger a CT secondary with the primary energized?</summary><br>No — not even with no load.<br><br></details>

<details><summary><b>159.</b> What is special about CT test switches?</summary><br>They're make-before-break: a shorting contact closes across the CT leads before the blade opens the meter circuit, so the CT is never open.<br><br></details>

<details><summary><b>160.</b> How does a CT shorting terminal block work?</summary><br>A metal bar runs down the block. Screws through the bar tie terminals to it; one screw always ties it to ground. Screws on a CT's terminals short and ground that CT.<br><img src="shorting_block.png"><br><br></details>

<details><summary><b>161.</b> CT polarity rule?</summary><br>Current IN on polarity (H1) means current OUT on polarity (X1) at the same instant.<br><img src="ct_polarity.png"><br><br><sub>CT polarity is always subtractive. Marks: H1/X1 or a dot.</sub><br><br></details>

<details><summary><b>162.</b> What goes wrong if instrument transformer polarity is reversed?</summary><br>Meters read backward, revenue meters record power in the wrong direction, protective relays cover the wrong zone or misoperate.<br><br></details>

<details><summary><b>163.</b> Two 800:5 CTs, 400 A primary, secondaries share a middle meter. When does the middle meter read 0 A?</summary><br>When the two CTs' 2.5 A secondary currents meet head-on in the shared meter: they cancel there and circulate through the outer meters (2.5 A each).<br><br><sub>Trace current out of X1 and back to its own X2 by the lowest-impedance path.</sub><br><br></details>

<details><summary><b>164.</b> What is a transducer (in metering/SCADA)?</summary><br>A device that converts CT/PT signals (or other physical quantities) into a standard signal, often 4–20 mA or a voltage, for a PLC/RTU/SCADA.<br><br></details>

<details><summary><b>165.</b> SCADA vs HMI?</summary><br>SCADA: the overall supervisory control and data acquisition system talking to RTUs/PLCs. HMI: the operator's graphical screen within it.<br><br></details>

<details><summary><b>166.</b> What should you inspect before accepting a transformer shipment?</summary><br>On the truck: damaged bushings, oil leaks, bulged/dented tank, broken gauges, overheating/arc signs, lead condition. Note damage before signing.<br><br></details>

<details><summary><b>167.</b> List the pre-energization field tests from the slides.</summary><br>Insulation resistance, turns ratio (TTR), polarity, winding resistance, power factor, CT saturation.<br><br><sub>Plus oil tests (dielectric, moisture, DGA) on liquid-filled units.</sub><br><br></details>

<details><summary><b>168.</b> Insulation resistance test: what does it measure and how is it done?</summary><br>Leakage through insulation, with a DC megohmmeter: each winding to ground and winding to winding. Higher megohms = less leakage.<br><br><sub>Record as a baseline; trend it, temperature-corrected. PI and DAR ratios show moisture.</sub><br><br></details>

<details><summary><b>169.</b> TTR test: what does it check?</summary><br>Low-voltage AC test confirming the HV-to-other-windings ratio at no load, on every tap of every winding.<br><br><sub>Catches shorted turns and wrong tap position. NETA ATS tolerance ≈ 0.5%.</sub><br><br></details>

<details><summary><b>170.</b> Winding resistance test finds what?</summary><br>Loose connections, broken strands, poor tap-changer contacts. Low-resistance DC test; compare phases and factory data, temperature-corrected.<br><br><sub>Discharge the winding afterward.</sub><br><br></details>

<details><summary><b>171.</b> What does an insulation power factor test measure?</summary><br>Ratio of resistive (loss) current to capacitive current under AC. Rising PF means insulation is degrading (moisture, contamination).<br><br><sub>Good insulation is well under 1%. Compare to the same unit's history.</sub><br><br></details>

<details><summary><b>172.</b> Why are power factor readings compared to previous readings rather than other equipment?</summary><br>Trend on the same unit is what reveals deterioration; values vary between designs.<br><br></details>

<details><summary><b>173.</b> Purpose of CT saturation testing?</summary><br>Confirms the CT won't saturate at its required burden; also verifies ratio and polarity vs manufacturer data.<br><br></details>

<details><summary><b>174.</b> Name 5 periodic transformer maintenance items.</summary><br>Keep records; maintain oil level; keep moisture out; keep parts clean/rust-free; test winding insulation and oil; lubricate moving parts; keep enclosures tight; check fans, arresters, gauges, grounds.<br><br></details>

<details><summary><b>175.</b> After disconnecting a transformer, why ground the windings?</summary><br>To discharge stored capacitive energy, especially after DC testing. Leave personal grounds on until all work is done.<br><br></details>

<details><summary><b>176.</b> Steps to make a transformer safe to work on?</summary><br>Open both sides, LOTO all sources, test for absence of voltage on both sides, apply grounds, work between grounds.<br><br><sub>NFPA 70E Art. 120.</sub><br><br></details>

<details><summary><b>177.</b> Safe energization practices?</summary><br>Verify grounds/tools removed, operate remotely if possible, know emergency shutoffs and first aid, wear required PPE, stand clear.<br><br></details>

<details><summary><b>178.</b> Why must transformer cases and metal enclosures (and fences) be grounded?</summary><br>To limit touch voltage from insulation failure and provide a low-impedance fault path so the OCPD trips fast.<br><br><sub>NEC 450.10, Art. 250.</sub><br><br></details>

<details><summary><b>179.</b> Three requirements of an effective ground-fault current path?</summary><br>Electrically continuous; able to safely carry any likely fault current for its duration; low impedance to trip the OCPD quickly.<br><br><sub>NEC 250.4.</sub><br><br></details>

<details><summary><b>180.</b> How does fault current divide among paths?</summary><br>It uses all available paths, dividing inversely to their impedance, and returns to its source (the transformer secondary).<br><br></details>

<details><summary><b>181.</b> Classic grounding mistake on a new building transformer?</summary><br>Missing system bonding jumper (no fault path), or bonding neutral to ground at both the transformer and downstream panel (neutral current on grounding conductors).<br><br><sub>Bond at one location only (NEC 250.30).</sub><br><br></details>

<details><summary><b>182.</b> Liquid-filled transformers: name 4 liquids used today, and the liquid's two jobs.</summary><br>Mineral oil (combustible), silicone fluid, seed-oil (natural ester) coolants, other non-toxic high-dielectric liquids. Jobs: insulate HV from LV windings, and carry heat from core and coils to the tank/radiators/fans.<br><br><sub>Textbook Ch. 13.</sub><br><br></details>

<details><summary><b>183.</b> Why did askarel disappear, even though it was nonflammable?</summary><br>It's a PCB mixture, found highly toxic. The Toxic Substances Control Act (1976) and EPA rules ended its use; old units were replaced or refilled.<br><br><sub>Textbook Ch. 13.</sub><br><br></details>

<details><summary><b>184.</b> Advantages of dry-type over liquid-filled transformers?</summary><br>Lighter, simpler to install, no leak precautions or containment, no coolant replacement. Fans can be added to carry more load.<br><br><sub>Textbook Ch. 13.</sub><br><br></details>

<details><summary><b>185.</b> What three sections make up a unit substation?</summary><br>High-voltage switch, dry-type transformer, secondary distribution section, all in one lineup.<br><br><sub>Often owner-furnished; common in industrial plants. Textbook Ch. 13.</sub><br><br></details>

<details><summary><b>186.</b> NEC 450.3 overcurrent devices protect what?</summary><br>The transformer only. Conductors supplying or leaving it may need their own protection (Articles 240 and 310).<br><br><sub>Textbook Ch. 13.</sub><br><br></details>

<details><summary><b>187.</b> NEC Table 450.3(A) vs 450.3(B)?</summary><br>(A): over 1,000 V, varies with %Z (≤6% or 6–10%), fuse vs breaker, and supervised vs any location. (B): 1,000 V or less (125/167/300% primary-only, or 250% primary with secondary protection).<br><br><sub>Supervised locations get higher limits.</sub><br><br></details>

<details><summary><b>188.</b> Can a transformer with manufacturer's coordinated thermal overload protection skip primary protection?</summary><br>Yes, if the feeder overcurrent device is set at no more than 6× primary FLC (%Z ≤6%) or 4× (%Z 6–10%).<br><br><sub>Textbook Fig. 13-2.</sub><br><br></details>

<details><summary><b>189.</b> 50 kVA, 480 V → 208Y/120 V 3Ø. Primary FLC, 125% primary fuse, and max primary fuse (with secondary protection)?</summary><br>FLC = 50,000 ÷ (480 × 1.732) = 60 A. 125% = 75 A → next standard 80 A dual-element fuses (100 A switch). Max = 60 × 250% = 150 A.<br><br><sub>Textbook Fig. 13-3.</sub><br><br></details>

<details><summary><b>190.</b> Same 50 kVA, 480–208Y/120 V transformer: secondary FLC and overcurrent device?</summary><br>FLC = 50,000 ÷ (208 × 1.732) = 139 A. ×125% = 174 A → 175 A fuses or breaker. It also protects the panel (408.36) and secondary conductors (240.21(C)).<br><br><sub>Textbook Fig. 13-3.</sub><br><br></details>

<details><summary><b>191.</b> Name the four grounding/bonding parts of a separately derived system (NEC 250.30(A)).</summary><br>System bonding jumper, supply-side bonding jumper, grounding electrode conductor, grounding electrode.<br><br><sub>Primary EGC sized per 250.122. Textbook Fig. 13-3.</sub><br><br></details>

<details><summary><b>192.</b> What is an open-delta bank, and when is it used?</summary><br>Two transformers giving 3Ø (and 1Ø via a center tap on one). Used where the utility has only two primary phases nearby, for small 3Ø loads, or where a third unit will be added later.<br><br><sub>Textbook Ch. 13.</sub><br><br></details>

<details><summary><b>193.</b> Two 100 kVA transformers in open delta: capacity?</summary><br>(100 + 100) × 0.866 = 173 kVA, or 300 × 0.577 = 173 kVA.<br><img src="open_delta.png"><br><br><sub>86.6% of the two nameplates, 57.7% of a full 3-unit delta.</sub><br><br></details>

<details><summary><b>194.</b> What is a corner-grounded delta?</summary><br>A 3-wire delta secondary with one phase grounded. Phase voltages are unchanged; overcurrent devices generally aren't allowed in the grounded phase.<br><br><sub>Textbook Ch. 13.</sub><br><br></details>

<details><summary><b>195.</b> 120/240 V 4-wire (high-leg) delta: voltages A–N, C–N, B–N, and phase-to-phase?</summary><br>A–N and C–N = 120 V; B–N = 208 V (high leg); every phase-to-phase = 240 V.<br><img src="high_leg_delta.png"><br><br><sub>B can't serve line-to-neutral loads.</sub><br><br></details>

<details><summary><b>196.</b> High-leg identification and position rules?</summary><br>Mark it orange (or other effective means) wherever the neutral is present (110.15, 230.56). It's the B phase, in the center position (408.3(E)(1)). Panel warning: 'Caution ___ Phase Has ___ Volts to Ground' (408.3(F)).<br><br><sub>Also called red leg or wild leg.</sub><br><br></details>

<details><summary><b>197.</b> High-leg meter-socket trap?</summary><br>Many utilities want the high leg on the RIGHT-hand (C) position in self-contained meter sockets ≤200 A, then back in the CENTER (B) at the service disconnect.<br><br><sub>CT-metered services over 200 A avoid it. Textbook Ch. 13.</sub><br><br></details>

<details><summary><b>198.</b> Most common system in modern commercial buildings, and its usual voltages?</summary><br>3Ø 4-wire wye: 208Y/120, 480Y/277, 600Y/347 V. Line-to-neutral loads can go on any phase.<br><br><sub>Primaries are usually delta (only 3 conductors). Textbook Ch. 13.</sub><br><br></details>

<details><summary><b>199.</b> NEC vs NESC: which applies to the utility's transformer?</summary><br>The NESC applies up to the service point (utility equipment); the NEC applies to premises wiring after it (90.2(D)(5)). The utility sets the service point.<br><br><sub>Check who furnishes the service conductors before you bid.</sub><br><br></details>

<details><summary><b>200.</b> What is primary (high-voltage) metering?</summary><br>The utility meters on the transformer's HV side with PTs and CTs, often with 15-minute demand registers for kW and kVAR. High demand or low PF raises the rate.<br><br><sub>Used for single-tenant buildings. Textbook Ch. 13.</sub><br><br></details>

<details><summary><b>201.</b> Up to what size is a service typically direct-metered (self-contained socket)?</summary><br>200 A. Larger: 320 A sockets (some utilities) or CT metering; the utility wires CTs to the meter.<br><br><sub>Textbook Ch. 13.</sub><br><br></details>

<details><summary><b>202.</b> Panelboards fed through a transformer: where must overcurrent protection be?</summary><br>On the secondary side (408.36(B)). Exception: 2-wire to 2-wire, or 3-wire delta–delta, can be protected by the primary device through the ratio (240.21(C)(1)).<br><br><sub>Textbook Ch. 12.</sub><br><br></details>

<details><summary><b>203.</b> What protects service conductors before the service disconnect?</summary><br>Only the utility's transformer primary fuses, which protect the utility transformer, not the conductors. Keep service conductors inside buildings short.<br><br><sub>Textbook Ch. 13.</sub><br><br></details>

<details><summary><b>204.</b> Can harmonics overheat a transformer without tripping its overcurrent device?</summary><br>Yes (NEC 450.3 Informational Note 2). Fixes: oversize the transformer, use K-rated, run separate neutrals for non-linear loads.<br><br><sub>IEEE C57.110. Textbook Ch. 8.</sub><br><br></details>

<details><summary><b>205.</b> Why does the textbook multiply the marked %Z by 0.9 in fault calculations?</summary><br>Listed transformers ≥25 kVA have ±10% impedance tolerance. Actual %Z may be 10% lower, which means more fault current: the worst case.<br><br><sub>I_SC = I_FL × 100 ÷ (%Z × 0.9).</sub><br><br></details>

<details><summary><b>206.</b> 225 kVA, 208Y/120 V, 2 %Z (infinite primary, book method). Fault current at the terminals?</summary><br>FLC = 225,000 ÷ (208 × 1.732) = 625 A. Multiplier = 100 ÷ (2 × 0.9) = 55.56. I_SC = 625 × 55.56 = 34,725 A.<br><br><sub>1% → 69,444 A; 4% → 17,363 A. Textbook Problem 1, Ch. 18.</sub><br><br></details>

<details><summary><b>207.</b> How do service conductors change the available fault current, and what method does the book use?</summary><br>Their impedance lowers it. Point-to-point method: f from length, conductor constant C and voltage; M = 1 ÷ (1 + f); I_end = I_start × M. Example: 34,725 A → about 30,558 A over 25 ft of 3 × 250 kcmil Cu in PVC.<br><br><sub>Textbook Problem 2, Ch. 18.</sub><br><br></details>

<details><summary><b>208.</b> Besides the transformer, what else adds to or raises available fault current?</summary><br>Motor contribution (running motors act as generators briefly) and higher system voltage (+10% V → +10% fault current).<br><br><sub>Book recommends interrupting ratings ≥25% above calculated. Textbook Ch. 18.</sub><br><br></details>

<details><summary><b>209.</b> What do NEC 110.24(A) and (B) require?</summary><br>(A) Non-dwelling service equipment field-marked with available fault current and the calculation date. (B) Recalculate and re-mark when changes (e.g., bigger or lower-%Z utility transformer) affect it.<br><br><sub>110.16(B), new in 2023: arc-flash label on non-dwelling service/feeder equipment ≥1,000 A.</sub><br><br></details>

<details><summary><b>210.</b> How can a PV inverter or generator create a hazard on the utility primary?</summary><br>By backfeeding through the service transformer: 240 V can appear as 12,000 V or more on the primary. Hence listed transfer switches and utility-interactive (anti-islanding) inverters.<br><br><sub>Textbook Ch. 16 and 22.</sub><br><br></details>

<details><summary><b>211.</b> Name 4 transformer-related causes of unbalanced voltage.</summary><br>Large single-phase loads, open connections at a transformer secondary, open-delta banks, unequal %Z of 1Ø transformers in a 3Ø bank (also unequal/open capacitor banks).<br><br><sub>Small voltage unbalance = big extra heat in a motor. Textbook Ch. 7.</sub><br><br></details>
