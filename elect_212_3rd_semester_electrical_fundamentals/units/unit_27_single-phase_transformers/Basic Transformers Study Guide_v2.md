# **Basic Transformers Study Guide**

Nov 9, 2026 · @Jeff

## **1. Why transformers matter**

A transformer trades voltage for current at almost no cost in power: step the voltage up 10× and the current drops to 1/10. That one trick is why AC beat DC for power distribution, and why nearly every electrical job you will do sits downstream of a transformer.

This guide follows the instructor's "Basic Transformers" slide deck (472 slides). It adds the textbook-style theory the slides skip, and it flags slide errors in section 13. Section 15 adds the transformer material from the course textbook, Electrical Wiring—Commercial (18th ed., 2023 NEC), mainly Chapters 13 and 18. That book covers installation and the NEC, not transformer theory, so the theory in sections 2–3 is standard material rather than from the book.

**Intuition: a magnetic gearbox.** Gears trade speed for torque. A small gear driving a big gear gives less speed but more torque, and the power (speed × torque) is the same minus friction. A transformer trades voltage for current the same way. The gear-tooth ratio becomes the turns ratio, and friction becomes core and copper losses.

**The one rule that solves most problems:**



- E = voltage, I = current, P = primary (the side the power comes in on), S = secondary (the side feeding the load).

- The high-voltage side always carries the low current, and the low-voltage side always carries the high current.

- A transformer never creates power. If your answer has more VA coming out than going in, you made a mistake.

**Why this matters for wire size.** For the same power, doubling the voltage halves the current. Line loss is I²R, so halving the current cuts loss to 1/4. For a given loss, the conductor area needed goes as 1/V². That is why the grid steps up to hundreds of kV for transmission and back down to 120/240 V at your house. The trade-off is insulation: high voltage needs thicker insulation and bigger clearances.

**Power vs. distribution transformer** (slide terms):

| Term | Where it sits |
| - | - |
| Power transformer | Between the generator and the primary distribution circuit (substations, large kVA) |
| Distribution transformer | Between the primary distribution circuit (typically 4–35 kV) and the customer's service (120/240 V, 208Y/120, 480Y/277) |

**Trade points that get overlooked**

- Transformers only work on AC (or changing DC). Steady DC makes no changing flux, so nothing is induced. Steady DC on a winding just sees the low winding resistance and can burn it up.

- Most transformers have no electrical connection between windings. They are coupled magnetically, not electrically. The big exception is the autotransformer (section 9).

- "Primary" and "secondary" are roles, not fixed labels. The side the power enters is the primary. Feed a step-down transformer from its low side and it becomes a step-up transformer. That's backfeed (section 3), and it kills linemen.

## **2. How a transformer works**

AC in the primary makes a changing magnetic flux in the iron core. That same flux passes through the secondary and induces a voltage in it. Every turn on either winding sees the same flux, so every turn gets the same volts. That is why voltage follows the turns ratio.

### **2.1 Mutual induction (the slide's lamp demo)**

- The slides show two coils: one fed with AC, one wired to a lamp. Moving the coils closer makes the lamp brighter. Adding an iron core makes it much brighter.

- Closer coils and an iron core both mean more of the primary's flux links the secondary. Iron carries flux hundreds to thousands of times more easily than air (it has high permeability).

- This is Faraday's law: a changing flux through a coil induces a voltage. Lenz's law gives the direction: the induced voltage pushes current that opposes the change.

The textbook-level equation behind it (for sine waves):



- f = frequency (Hz), N = number of turns, Φmax = peak core flux (webers).

- For a given winding on a given supply, the flux is fixed by the applied voltage and frequency. Load current does not change it much.

- Consequences: feeding a 60 Hz transformer at 50 Hz raises the flux about 20%, which can saturate the core and overheat it. Overvoltage does the same thing.

### **2.2 Excitation (magnetizing) current**

- With the secondary open, the primary still draws a small current. It magnetizes the core. It is called excitation current or no-load current.

- It is typically a few percent of full-load current or less on power and distribution transformers.

- It lags the voltage by nearly 90°, because an unloaded transformer looks like an inductor.

- When you add load, the secondary current makes its own flux. The primary automatically draws extra current to cancel it. That is how the primary "knows" the load: the load sets the current, the transformer just passes it through.

### **2.3 Core and laminations**

- The core is built from thin silicon-steel sheets, each insulated (varnish or oxide coating) from its neighbor. It is not solid iron.

- **Eddy currents:** the changing flux induces little circulating currents in the core iron itself. They waste power as heat. Thin insulated laminations break up the paths so eddy currents stay small.

- **Hysteresis loss:** energy lost each cycle re-magnetizing the iron. Silicon steel is chosen because it has a narrow hysteresis loop.

- Eddy + hysteresis = **core loss (iron loss)**. It is present whenever the transformer is energized, loaded or not. It is roughly constant.

- **Copper loss (I²R)** is heat in the windings. It rises with the square of load current.

### **2.4 Core vs shell construction**

| Form | What surrounds what | Notes |
| - | - | - |
| Core form | Windings surround the core legs | Common on high-voltage, large units. Easier to insulate and cool |
| Shell form | The core surrounds the windings | Better magnetic shielding and short-circuit strength. Common on small and low-voltage units |

Three-phase units use a three-leg (or five-leg) core, one leg per phase.

### **2.5 Efficiency**



- Modern transformers run about 96–99% efficient. Big units are at the top of that range. They are among the most efficient machines made.

- Efficiency is highest when copper loss equals core loss. That usually happens somewhere around half to three-quarters load.

- A lightly loaded transformer still pays its full core loss. That's why oversizing a transformer "for safety" wastes energy around the clock.

**Common mistakes**

- Thinking the secondary voltage comes from current flowing across. It comes from flux. There is no copper path (except in an autotransformer).

- Thinking load current is set by the transformer. The load sets it. The transformer only sets the voltage.

- Saying "no load means no loss." Core loss is there 24/7 while energized.

## **3. Turns, voltage and current ratios**

Voltage goes with turns, and current goes against turns. More turns means more volts and fewer amps on that side.

### **3.1 The ratio equations**



- N = turns, E = voltage, I = current, P = primary, S = secondary.

- **TTR (transformer turns ratio)** = NP : NS, usually written high side to low side (for example 10:1).

- Cross-multiplied forms (slide 61): EP × NS = ES × NP, and IP × NP = IS × NS. The second one is "ampere-turns balance": primary ampere-turns equal secondary ampere-turns.

- Step-down: NP \> NS. Step-up: NP \< NS. Isolation: 1:1.

**Worked check (slides 59–60).** 1Ø, 2,400–480 V, IP = 15 A.

1. TTR = 2,400 ÷ 480 = 5:1.

2. Current goes the other way: IS = 5 × 15 = 75 A.

3. Check: 2,400 × 15 = 36,000 VA, and 480 × 75 = 36,000 VA. Power in = power out.

**The ratio is fixed and works both ways (slides 62–63).** For a 480–120 V (4:1) transformer:

- 240 V on the primary gives 240 ÷ 4 = 60 V out.

- 240 V on the *secondary* gives 240 × 4 = 960 V on the primary. The transformer doesn't care which side you feed.

### **3.2 Reflected impedance (textbook background)**

The primary "sees" the load impedance multiplied by the turns ratio squared:



Example: a 2 Ω load on a 10:1 step-down looks like 200 Ω from the primary. This is why a small load current on the high side can represent a big load on the low side.

### **3.3 Tapped windings**

- When a winding has taps, compute the TTR from the **whole** winding unless the question tells you which tap is used. Example: 2,400 V to a 240 V winding (center-tapped) is 10:1, not 20:1.

- Slide 239 example: a primary with taps at 1,200 turns (240 V), 1,040 turns (208 V) and 600 turns (120 V), and a 120-turn, 24 V secondary. Using the 1,040-turn tap: 1,040 ÷ 120 = 8.67:1, and 8.67 × 24 = 208 V.

- The output is always proportional to the input. A 2:1 transformer gives 240 V from 480 V, but only 219 V from 438 V. Pick the tap that matches your *actual* supply voltage, not the nominal one.

### **3.4 Backfeeding**

- **Backfeed** = energizing a transformer from the side you didn't expect. Because the ratio works both ways, 120 V accidentally applied to the low side of a 480–120 V unit puts 480 V on the high side.

- Classic case: a portable generator plugged into a house with no transfer switch or interlock. Through the pole transformer, a 240 V generator puts thousands of volts on a line the lineman thinks is dead.

- Field rules from the slides:

  a. Never work on a transformer unless **both** sides are disconnected. Use LOTO, and ground as required (work between grounds).

  b. Prove the secondary is de-energized, not just the primary.

  c. When removing an installed transformer, disconnect the **secondary (low-voltage) leads first**. That removes the backfeed path before you touch the high side.

**Common mistakes**

- Inverting the current ratio. Current is highest on the low-voltage side. Do a VA check every time.

- Using a tap's turns when the question asks for the full-winding TTR (or the reverse).

- Assuming an open primary fuse or switch means the transformer is dead. It may be fed from the secondary.

## **4. Ratings, nameplate and full-load current**

A transformer's real limit is heat, and heat comes from current. So transformers are rated in VA (volts × amps), which fixes the current at rated voltage no matter what the load's power factor is.

### **4.1 Why VA, not watts**

- Copper loss depends on current, and current depends on VA, not watts.

- Slide 78 example: two identical transformers each feed 50 kW. At PF 0.9 the load is 55.6 kVA. At PF 0.7 it's 71.4 kVA. Same watts, but the second one carries about 29% more current and runs much hotter.

- Common single-phase distribution sizes: 10, 15, 25, 37.5, 50, 75, 100, 150, 167 kVA.

### **4.2 Full-load current (FLC = FLA)**

FLC and FLA mean the same thing: the current the transformer can carry continuously at rated conditions.



(For three-phase, divide by E × 1.732 instead.)

| Example | Primary FLC | Secondary FLC |
| - | - | - |
| 25 kVA, 240–120 V | 25,000 ÷ 240 = 104.2 A | 25,000 ÷ 120 = 208.3 A |
| 2,000 kVA, 12 kV–2.4 kV | 2,000,000 ÷ 12,000 = 166.7 A | 2,000,000 ÷ 2,400 = 833.3 A |

- kVA in = kVA out, so both sides check: 104.2 × 240 = 208.3 × 120 = 25 kVA.

- The ratio of the FLCs is the TTR: 833.3 ÷ 166.7 = 5.

**Amps-per-kVA rule of thumb (slide 83).** For single-phase, amps per kVA = 1,000 ÷ volts. So 120 V → 8.33, 240 V → 4.17, 480 V → 2.08, 2,400 V → 0.42, 12,000 V → 0.083. The slide's rounded values (4, 2, 0.4, 0.08) are fine for a field estimate but come out a few percent low.

### **4.3 Load checks with a clamp meter**

- **Balanced 120/240 V:** both legs read the same. kVA = leg amps × 240 V. Example: 200 A × 240 V = 48 kVA on a 60 kVA unit = 80% loaded.

- **Unbalanced 120/240 V:** add the two line currents, multiply by 120 V, and ignore the neutral. Example: L1 = 20 A, L2 = 30 A, N = 10 A → (20 + 30) × 120 = 6 kVA.

- Why it works: each 120 V half-winding delivers its line current at 120 V.

- A load check is a snapshot. Peak load (hot afternoon, evening) is what matters. A one-time reading at 9 a.m. can badly understate it.

### **4.4 Sizing a transformer**



Slide 90: 50 kW at PF 0.85 → 58.8 kVA. No standard size is exactly 58.8, so go to the next standard size up: **75 kVA**. Never round down.

In practice you also allow for growth and continuous loads, and the NEC sets the overcurrent protection (section 5).

### **4.5 Nameplate**

The nameplate is a legal document. It gives the limits for continuous operation without damage. NEC 450.11 requires the key items to be marked.

Typical items: manufacturer, serial number, kVA, phases, frequency, high and low voltages, full-load currents, temperature rise (°C), %Z, polarity (single-phase), connection diagram, tap table, insulation/cooling type (dry, oil), BIL, weight and oil volume.

The slide 32 nameplate example reads: 50 kVA, single-phase, 60 Hz, 55 °C rise, class OA (oil, self-cooled), 2.2 %Z, subtractive polarity, 12,000–120/240 V, with taps at 100%, 97.5%, 95%, 92.5% and 90% of the HV rating.

**BIL (Basic Impulse Insulation Level)** is the peak lightning-type surge voltage the insulation can survive. It is in kV crest, and it's much higher than the operating voltage (for example, about 95 kV BIL for 15 kV-class distribution equipment).

### **4.6 Reading voltage ratings: dash vs slash**

| Written as | Meaning |
| - | - |
| 12,470 – 240 | Dash separates windings. First voltage = the side receiving power (primary), second = secondary |
| 120/240 | Slash = one winding offers two voltages. Smaller first: two separate 120 V coils. Series them for 120/240 V 3-wire, or parallel them for 120 V 2-wire at double current |
| 240/120 | Larger first: one 240 V coil with a center tap brought out. 3-wire only. You can't parallel it |
| 208Y/120 | Three-phase wye: 208 V line-to-line, 120 V line-to-neutral |

**Common mistakes**

- Dividing kVA by kV and forgetting the units. kVA ÷ kV = A, and kVA ÷ V = kA.

- Using 240 V for an unbalanced load check. Add the legs and use 120 V.

- Sizing to watts instead of VA when the PF is below 1.

- Reading "120/240" and "240/120" as the same thing. They are wired differently.

## **5. Cooling, temperature rise, overloads and protection**

Every loading rule comes back to one thing: the insulation's temperature. Heat ages insulation, and insulation life is the transformer's life.

### **5.1 Cooling methods**

| Type | How it works | Where you see it |
| - | - | - |
| Dry-type (self air-cooled) | Air circulates through vents in a sheet-metal case | Most indoor building transformers (480–208Y/120 etc.) |
| Oil-immersed, self-cooled | Core and coils sit in mineral oil. Oil rises when hot (natural convection), carries heat to the tank and fins, and sinks as it cools | Pole and pad-mount distribution, substations |
| Forced air / forced oil | Fans on the radiators and/or oil pumps add capacity | Substation units with two or three kVA ratings on one nameplate |
| Askarel (PCB) | Nonflammable synthetic liquid | Old units only. Banned from new manufacture in the late 1970s. Toxic |

- Oil is both coolant and insulation. It is a far better insulator than air and keeps the paper insulation from drying out and oxidizing.

- Mineral oil burns. The NEC (Article 450, Part II) puts tighter rules on oil-filled units indoors and near buildings: vaults, separation, or fire barriers.

- Many newer units use less-flammable liquids (natural esters such as FR3, or silicone). The rules for those are looser than for mineral oil.

- If you find an old unit marked Askarel or "contains PCBs", don't open it or touch leaking fluid. It's hazardous waste with its own handling rules.

- Older cooling-class codes on nameplates: OA (oil, self-cooled), FA (forced air), FOA (forced oil and air). Newer codes: ONAN, ONAF, OFAF.

### **5.2 Temperature rise**



- Ratings assume 40 °C maximum ambient (30 °C average over 24 hours).

- Slide example: 65 °C rise + 40 °C ambient = 105 °C. That's the *average* winding temperature. The hottest spot inside runs higher (about 15–30 °C more, depending on the type), and the insulation class is chosen to cover the hot spot.

- Common ratings: liquid-filled 55 °C or 65 °C rise. Dry-type 80 °C, 115 °C or 150 °C rise (usually on 220 °C insulation).

- A lower-rise unit at the same kVA has more copper and iron, so it runs cooler and has overload headroom. That's the slide's "young, healthy runner."

- Other things that cut capacity: high ambient (rooftops, desert), high altitude (thin air cools poorly, above about 1,000 m / 3,300 ft), blocked vents, harmonics (section 9), and low oil level.

### **5.3 Overload vs fault**

- **Overload:** more than rated current, but through the normal path, for example 130% of FLA for two hours. Not a fault. Damage comes slowly, from heat.

- **Fault (short circuit or ground fault):** current through an abnormal path, often many times rated. Protective devices must clear it fast.

- Transformers have a lot of thermal mass. The temperature lags the load by minutes to hours, so short peaks are tolerated. Long overloads age insulation fast. A common rule of thumb is that insulation life halves for every 8–10 °C above rated hot-spot temperature.

- Many units have a winding-temperature or oil-temperature gauge with a drag (max) pointer and alarm contacts. Read and reset the max pointer during inspections.

### **5.4 Overcurrent protection (NEC 450.3)**

- The slides simplify this to "protection goes on the primary." The NEC actually gives two choices for transformers of 1,000 V or less (450.3(B)):

  a. **Primary only:** at no more than 125% of primary FLC (when the primary FLC is 9 A or more).

  b. **Primary and secondary:** primary up to 250%, *with* secondary protection at no more than 125% of secondary FLC.

- If 125% doesn't land on a standard fuse or breaker size, you may go up to the next standard size (for currents of 9 A or more). Smaller transformers get higher percentages (167% below 9 A, 300% below 2 A on the primary).

- Over 1,000 V uses a different table (450.3(A)), based on fuse vs breaker and supervised vs unsupervised locations.

- Transformer protection is not the whole story. The secondary conductors need their own protection under 240.21(C) (the "transformer secondary conductor" rules, such as the 10 ft and 25 ft rules).

- Code numbers and percentages are from the 2023 NEC. Check the edition your jurisdiction enforces.

**Inrush.** Energizing a transformer can draw roughly 8–12× FLC for a few cycles while the core magnetizes. That's why the NEC allows primary protection well above 100%, and why time-delay fuses are common on transformer primaries.

**Common mistakes**

- Treating the nameplate kVA as the limit in every condition. Hot ambient, altitude, and harmonics all reduce real capacity.

- Sizing primary protection at 100% of FLC. Inrush will nuisance-trip it.

- Forgetting secondary conductor protection. Protecting the transformer doesn't automatically protect the wire leaving it.

## **6. Polarity**

Polarity tells you which secondary terminal goes positive at the same instant as a given primary terminal. You don't care on a single transformer feeding a load. You care a lot the moment you connect windings or transformers together.

### **6.1 Terminal markings**

- High-voltage terminals: **H1, H2** (H3, H4 for more, H0 for a neutral).

- Low-voltage terminals: **X1, X2** (X3, X4 for taps or a second winding, X0 for a neutral). Further windings use Y and Z.

- The rule: **H1 and X1 are positive at the same instant.** H2 and X2 are negative at that instant.

- H/X is about voltage level, not direction of power. On a step-up unit, the X side is the primary.

- Small transformers and instrument transformers often mark polarity with a dot instead (the dotted ends are "in phase").

### **6.2 Additive vs subtractive**

Stand facing the low-voltage side. H1 is normally on your left (the back-left bushing). Then:

| Polarity | Where X1 is | Memory aid |
| - | - | - |
| Subtractive | X1 on the **same** side as H1 (left) | "Same side subtractive" |
| Additive | X1 **diagonally opposite** H1 (right) | Opposite = additive |

- Polarity is set by how the windings are wound and how the leads are brought out. You can't change it from outside. You can only connect to suit it.

- Standard practice (ANSI/IEEE C57.12.00): single-phase units of 200 kVA or less, with HV of 8,660 V or less, are additive. Everything larger or higher voltage is subtractive. Most pole-top distribution transformers are additive.

- Why subtractive for big units: if the HV and LV leads were accidentally connected, the stress between adjacent leads is half the *difference* of the voltages, not half the sum. That's a lower insulation stress.

- Additive and subtractive transformers **can** be paralleled or banked together. You just connect by H1/X1 markings, not by physical bushing position.

### **6.3 Polarity test with AC (no nameplate)**

1. Jumper H1 to the adjacent low-voltage terminal (the one directly across from it).

2. Apply a low, known AC voltage across H1–H2 (for example 120 V on the HV winding).

3. Measure from H2 to the other adjacent low-voltage terminal.

4. Reading **higher** than the applied voltage = **additive** (the windings add). Reading **lower** = **subtractive** (they oppose).

Example: a 480–120 V (4:1) unit with 120 V applied gives 30 V on the LV winding. Additive reads 120 + 30 = 150 V. Subtractive reads 120 − 30 = 90 V.

### **6.4 Kick test (DC)**

1. Connect an analog DC voltmeter across the low-voltage winding. Note which lead is on its + terminal.

2. Note which HV lead will go to the battery +.

3. Briefly connect a small battery (a few volts) to the HV winding. The meter needle kicks while the current is building.

4. If the needle kicks up-scale, the LV lead on meter + has the same polarity as the HV lead on battery + (that pair is H1/X1). A down-scale kick means the opposite.

5. When you break the battery circuit, the needle kicks the other way. Read the **make** kick, not the break kick.

The kick happens only while the flux is changing (Lenz's law), which is why steady DC shows nothing. Opening the DC circuit on a winding can produce a large inductive voltage spike, so keep hands off the leads.

**Common mistakes**

- Assuming polarity from bushing position on an unfamiliar unit. Verify by markings or test.

- Assuming current direction and voltage polarity are the same thing (slide 469). In a transformer, current flows *into* H1 on the primary and *out of* X1 on the secondary at the same instant.

- Testing polarity at full voltage. Use a low test voltage.

## **7. Connecting windings, paralleling, and 3-wire service**

Windings connect like batteries. Series adds voltage, parallel adds current capacity, and getting the polarity wrong either cancels the voltage or makes a dead short.

### **7.1 Series and parallel secondaries (one transformer)**

A 120/240 V secondary is two 120 V coils (X1–X2 and X3–X4).

| Connection | How | Result (25 kVA example) |
| - | - | - |
| Series | Jumper X2 to X3. Take X1 and X4 as lines, the jumper as neutral | 120/240 V 3-wire, 104 A per line |
| Parallel | Jumper X1 to X3 and X2 to X4 | 120 V 2-wire, 208 A |

- Series with one coil reversed: the voltages cancel, and you read about 0 V instead of 240 V.

- Parallel with one coil reversed: a dead short across both coils. Huge current, blown fuse, damaged windings.

- Series or parallel changes the voltage and current. It never changes the kVA. Both connections are still 25 kVA.

Primaries can be series/parallel connected the same way. Control transformers (240 × 480 primaries) use this: series for 480 V, parallel for 240 V.

### **7.2 Paralleling two transformers**

Requirements, so the units share load instead of fighting each other:

1. Same voltage ratio (and same tap setting). Otherwise current circulates between them even with no load.

2. Same (or very close) %Z. Otherwise the lower-%Z unit hogs the load.

3. Correct polarity. Connect by H1/X1 markings. Additive and subtractive units can be paralleled.

4. For three-phase: same phase sequence and same angular displacement.

**Load sharing.** With matched %Z, each unit carries load in proportion to its kVA rating. Slide 169: 50 kVA + 100 kVA feeding a 75 kVA load. The 50 kVA unit carries 75 × 50/150 = 25 kVA, and the 100 kVA unit carries 50 kVA.

**Test before you connect.** Energize both, but leave the last secondary connection open. Read voltage across the open gap:

- About 0 V → phasing is correct, make the connection.

- About double voltage → polarity is wrong. **Do not connect.** You'd be shorting two sources together.

**Backfeed hazard in a parallel bank.** If one unit's primary fuse blows, the other unit feeds it backward through the paralleled secondaries. Its primary stays energized at full voltage. Treat every primary in a paralleled bank as hot until both sides are open. The remaining unit is also now carrying the whole load, so it may be overloaded.

### **7.3 Three-wire 120/240 V service**

- The center point (neutral) of the series secondary is grounded. Grounding limits the voltage to ground (120 V) and provides a path for fault current. It also keeps a lightning or primary-contact event from raising the whole secondary far above ground.

- If the neutral weren't grounded and one line faulted to ground, the other line would sit at 240 V to ground.

- The neutral carries the **difference** between the two line currents (the unbalance), not the sum. With balanced line-to-line and 120 V loads, the neutral carries 0 A.

### **7.4 Unbalanced loading**

Each half of a 120/240 V winding is only rated for half the kVA. A transformer can be under its total kVA and still overload one half.

**Slide 224 example.** 25 kVA 120/240 V. Each half is good for 12.5 kVA, or 12,500 ÷ 120 = 104 A.

- Side 1: 120 V × 167 A = 20 kVA → 167 ÷ 104 = **160%**. That side is 60% overloaded.

- Side 2: 120 V × 42 A = 5 kVA → 42 ÷ 104 = **40%** loaded. (The slide says "40% underloaded." It's actually 40% loaded, or 60% under capacity.)

- Total is 25 kVA, exactly nameplate, yet one winding is cooking.

**Slide 227 example (75 kVA, 12,500–120/240 V).** Loads: 6 kVA at 240 V, 3 kVA on one 120 V side, 3.6 kVA on the other.

| Meter | Location | Reading |
| - | - | - |
| A5 | 240 V load | 6,000 ÷ 240 = 25 A |
| A3 | Line 1 | 25 A (240 V load) + 25 A (3 kVA at 120 V) = 50 A |
| A4 | Line 2 | 25 A + 30 A (3.6 kVA at 120 V) = 55 A |
| A6 | Neutral | 30 − 25 = 5 A |
| A1, A2 | Primary | 12,600 VA ÷ 12,500 V ≈ 1.0 A |

Total load 12.6 kVA ÷ 75 kVA = 16.8% loaded.

Check: (50 × 120) + (55 × 120) = 12,600 VA. That matches the "add the legs × 120" rule from section 4.

### **7.5 Open neutral**

If the neutral opens, the 120 V loads on opposite sides end up in **series across 240 V**. The voltage divides by resistance, so the side with less load (higher resistance) gets the higher voltage.

Slide 234 example: 3 kVA load (R = 120² ÷ 3,000 = 4.8 Ω) and 3.6 kVA load (R = 4.0 Ω).

- I = 240 ÷ (4.8 + 4.0) = 27.3 A.

- 3 kVA load: 27.3 × 4.8 = **131 V**. 3.6 kVA load: 27.3 × 4.0 = **109 V**.

- The slide's figure labels these the other way round. The lighter load gets the higher voltage.

In real life, an open service neutral shows up as lights that go bright on one side and dim on the other when a big 120 V load cycles. Electronics on the high side get destroyed. Treat it as an emergency.

**Common mistakes**

- Checking only total kVA on a 120/240 V unit. Check each leg against half the rating.

- Saying the neutral carries the sum of the line currents.

- Paralleling transformers without the zero-volt test.

## **8. Percent impedance (%Z) and fault current**

%Z is the percentage of rated primary voltage it takes to push full-load current through a shorted secondary. It tells you how much fault current the transformer can deliver: the lower the %Z, the bigger the fault current.

### **8.1 What %Z means**

- Short the secondary. Slowly raise the primary voltage from zero. When full-load current flows, stop. That voltage as a percentage of rated voltage is %Z.

- Slide 194 example: a 480 V winding with 5 %Z reaches full-load current at 0.05 × 480 = 24 V.

- In a real fault, the full 480 V is applied, not 24 V. That's 480 ÷ 24 = 20× more voltage, so **20× full-load current**.

- It's given in percent so one number works for both sides. In ohms, the HV and LV sides would have different values (they differ by the turns ratio squared).

### **8.2 Short-circuit current formula**



This assumes the utility source can supply unlimited current (an "infinite bus"). Real fault current is a bit lower, but this worst case is what you use to check equipment ratings.

| Transformer | FLC (secondary) | %Z | Max fault current |
| - | - | - | - |
| 480 V, 5 %Z (slide 194) | I\_FL | 5 | 20 × I\_FL |
| 25 kVA, 240 V, 2 %Z | 104.2 A | 2 | 104.2 × 50 = 5,208 A |
| 50 kVA, 240 V, 2.2 %Z (slide 32 nameplate) | 208.3 A | 2.2 | 208.3 × 45.5 ≈ 9,470 A |

To convert %Z to ohms on one side: Z(Ω) = (%Z ÷ 100) × E² ÷ VA.

### **8.3 How %Z is measured (short-circuit test)**

The slides describe this test on slides 73–75:

1. Ammeter in series with the secondary, and short the secondary.

2. Voltmeter across the primary.

3. Feed the primary from a variable supply (a Variac). Raise it until nameplate full-load current flows in the secondary.

4. Record the **primary** voltage. %Z = (that voltage ÷ rated primary voltage) × 100.

The slides title this "How is FLC physically determined" and say to record the *secondary* voltage. Both are off: FLC comes from the nameplate (VA ÷ V), the shorted secondary has nearly 0 V across it, and what the test measures is impedance voltage on the primary.

### **8.4 Typical values and why they vary**

- Small single-phase distribution transformers: roughly 1.5–3 %Z. Big power transformers: 5–15% or more, higher for higher voltage and MVA (see the slide 190 table).

- **Low %Z:** better voltage regulation (less voltage sag under load), but much higher fault current. That means higher AIC ratings downstream and more arc-flash energy.

- **High %Z:** limits fault current, but more voltage drop under load and more voltage dip when a big motor starts.

- %Z is a design choice for the application, not a quality grade. (Slide 196 claims low %Z means a better, more expensive transformer. That's not a reliable rule.)

### **8.5 Why electricians care**

- **Interrupting rating (NEC 110.9) and SCCR:** every breaker and fuse downstream must be able to interrupt the available fault current. A replacement transformer with lower %Z can make existing panels under-rated.

- **Available fault current marking (NEC 110.24):** service equipment in non-dwelling occupancies must be field-marked with the available fault current. It must be updated when the transformer changes.

- **Arc flash (NFPA 70E):** more fault current means more incident energy and bigger PPE requirements.

- **Paralleling:** units need matched %Z to share load (section 7).

**Common mistakes**

- Thinking %Z is a loss or efficiency figure. It's about fault current and regulation.

- Forgetting that %Z = 2 means 50× FLC. Small %Z, big fault.

- Assuming the worst-case formula is the real fault current. It's the ceiling. Utility and conductor impedance bring it down.

## **9. Special-purpose transformers**

They all run on the same turns-ratio physics. Each type just wires or builds the windings differently for one job.

### **9.1 Isolation transformers**

- 1:1 ratio. The point is the isolation, not a voltage change.

- They block noise and spikes from passing straight through, break ground loops, and feed sensitive electronics and lab gear. Many have a grounded electrostatic shield between the windings for extra noise rejection.

- **Overlooked:** an isolation transformer's secondary is a **separately derived system** (NEC 250.30). It needs its own system bonding jumper and grounding electrode connection. Otherwise its secondary is floating, and a ground fault won't trip anything.

### **9.2 Buck-boost transformers**

A small, ordinary isolating transformer wired as an autotransformer, with its low-voltage winding in series with the line. It trims voltage by about 5–27%.

- **Boost** (additive connection): the secondary voltage adds to the line. Slide 208: 120 V + 24 V = 144 V.

- **Buck** (subtractive connection): the secondary voltage subtracts. Slide 209: 120 V − 24 V = 96 V.

- Typical uses: running 230 V equipment from a 208 V system, or correcting voltage drop at the end of a long run.

- Why bother: low voltage on a motor raises its current, cuts its torque, and overheats it. Low voltage also cuts the output of heaters and lamps.

- **The big trade point:** the buck-boost unit only carries the *difference* power. Its secondary carries the full load current, but only at 24 V. So a 1 kVA unit (24 V → 41.7 A) boosting 120 to 144 V can feed about 41.7 × 144 = 6 kVA of load. Size it by the load current, not the load kVA.

- Buck-boost connections are autotransformers, so they don't isolate.

### **9.3 Autotransformers (and Variacs)**

- One winding acts as both primary and secondary. Part of the winding is shared by both circuits.

- The shared section carries only the difference between the primary and secondary currents. So autotransformers are smaller, cheaper, and more efficient than two-winding units, especially for small ratio changes.

- A **Variac** is a variable autotransformer: a carbon brush rides on the bare winding to give 0 V to slightly above line voltage. The lab bench supplies use them.

- **Disadvantages:** there is no isolation between the high and low sides. And if the common part of the winding opens while stepping down, the full line voltage appears at the load.

- **NEC limits** (450.4, 210.9, 215.11): an autotransformer can't feed a branch circuit or feeder unless the system has a grounded conductor common to both sides. There are exceptions, such as boosting 208 to 240 V. Approved uses in the slides include reduced-voltage motor starting, theater dimming, lighting ballasts, and buck-boost.

- Slide 262 shows the unsafe case: an autotransformer fed from an ungrounded three-phase system. A ground fault anywhere on that system can put a dangerous voltage to ground on the lighting circuit.

### **9.4 Control transformers**

- They step 240 V or 480 V down to 120 V (or 24 V) for motor-control circuits: coils, pilot lights, PLC inputs.

- Dual primary (often marked 240 × 480): primaries in **series for 480 V**, in **parallel for 240 V**. Wire the jumpers per the diagram on the unit.

- The secondary is usually fused, and one side (X2) is often grounded so a ground fault blows the fuse instead of starting the motor. (NEC 430.72 covers control-circuit transformer protection.)

- Control transformers are built to handle the big inrush when contactor coils pull in, which is why they're rated in VA with an "inrush VA" spec.

### **9.5 Neon sign transformers**

- 120 or 240 V primary, 2,000–15,000 V secondary, 30–120 mA.

- They are designed to limit their own current (high leakage reactance), because a gas tube has negative resistance and would run away on a stiff source.

- Covered by NEC Article 600. Modern units must have secondary ground-fault protection.

- The secondary voltage is lethal even though the current rating is in milliamps.

### **9.6 Constant-current transformers (CCTs)**

- They supply a fixed secondary current, usually **6.6 A**, to **series** circuits: older street lighting and airport runway lighting.

- Series wiring saves copper: one small conductor runs lamp to lamp.

- How: a movable coil floats on the core. The two windings' fields repel. More load current pushes the coil apart, which raises leakage and drops current back. A counterweight and an oil dashpot keep it from "hunting." Newer regulators do it electronically.

- The voltage rises and falls automatically with the load. The primary is usually fed at a constant 2,400 V.

- Each lamp has a film cutout or reactor so the circuit doesn't open when one lamp fails.

- Lamp brightness tracks current closely. That's why runway lights are regulated on current, not voltage.

- **Safety:** an open series circuit drives the regulator to its maximum voltage, which can be several kV. Never open a live series lighting circuit.

### **9.7 K-rated transformers (harmonics)**

- Non-linear loads draw current in pulses, not smooth sine waves. Examples: switch-mode power supplies, VFDs, LED drivers, UPSs, PV inverters, and arc devices.

- Pulsed current contains harmonics (multiples of 60 Hz: 180, 300, 420 Hz...). Harmonics cause extra eddy-current heating in the windings and extra stray loss.

- Triplen harmonics (3rd, 9th, ...) add in the neutral of a wye system. A neutral can carry more current than the phases.

- A **K-factor** rating says how much harmonic heating the unit can take. K-1 = linear loads only. Common ratings are K-4, K-13 and K-20. The slides give a range of 1–50.

- K-rated units have heavier or specially built windings and often a double-size neutral.

- To pick a K rating, measure the actual K-factor with a power-quality meter at full load.

### **9.8 Multi-tap windings and the no-load tap changer (NLTC)**

- Taps let the transformer match the actual supply voltage. They're usually in 2½% steps, for example 2 above and 2 below nominal.

- An NLTC changes the turns ratio but **must only be moved with the transformer de-energized**. Moving it energized can arc and destroy the switch.

- Substation units may have an on-load tap changer (LTC) that adjusts automatically under load. That's a different device.

- **The tap direction trap:** taps are usually on the primary. If the supply is high, select a *higher* primary tap (more turns), which *lowers* the output. To raise a low secondary, select a lower % tap. Moving to the "95%" tap raises the output voltage by about 5%.

- Multiple isolated secondaries (slide 242) are different from a tapped secondary. Each winding is separate and can feed a different circuit.

### **9.9 Pressure relief device (PRD)**

- An internal arc or severe overheating makes gas and expands the oil. The PRD is a spring-loaded valve that vents the pressure so the tank doesn't rupture.

- It reseals automatically when the pressure drops. It has a flag that stays up to show it operated, and often alarm or trip contacts.

- A tripped PRD flag means something serious happened inside. Don't just reset it and re-energize. The unit needs testing first.

## **10. Three-phase banks (preview)**

A three-phase bank is three single-phase windings connected in wye or delta. The √3 (1.732) factor shows up in voltage for wye and in current for delta. You worked these relationships in Labs 5–7. This section covers the transformer-specific parts.

### **10.1 Wye vs delta relationships**

| Connection | Voltage | Current | Neutral? |
| - | - | - | - |
| Wye (star) | E\_line = E\_phase × 1.732 | I\_line = I\_phase | Yes, the common point |
| Delta | E\_line = E\_phase | I\_line = I\_phase × 1.732 | No (except a center-tapped high-leg delta) |



- "Phase" means the winding. "Line" means the conductor between the bank and the load. (The slides call line current "line-to-line current." Line current is the current in one line conductor.)

- 1 ÷ 1.732 = 0.577, so phase voltage in a wye is 57.7% of line voltage (the slides round to 58%). Example: 208 V line → 120 V phase.

- You can't clamp phase current inside a delta winding. Only line current is measurable from outside.

### **10.2 Forming banks from three single-phase cans**

- **Wye:** connect the three non-polarity terminals (H2s on the primary, X2s on the secondary) together. That point is the neutral (H0/X0). The polarity terminals (H1/X1) become the lines.

- **Delta:** connect polarity to non-polarity around the loop: X1 of unit A to X2 of unit B, X1 of B to X2 of C, and close with X1 of C to X2 of A. No neutral.

- Advantages of three separate cans over one three-phase tank: you can replace one failed unit, keep a single spare, and run a delta bank "open-delta" on two units at 57.7% of the three-unit capacity. A single three-phase tank is smaller, cheaper and more efficient.

- The four basic combinations are delta–delta, delta–wye, wye–delta and wye–wye. Delta–wye (for example 480 V delta to 208Y/120 V) is the most common in buildings.

### **10.3 Closing a delta safely**

1. Connect all but the last corner of the delta.

2. Energize and read voltage across the open corner, with a meter rated for at least twice the winding voltage.

3. Near zero (a few volts from small imbalances is normal) → correct. Close it.

4. About **twice** the winding voltage → one winding is reversed. **Do not close.** Closing would short the bank with a huge circulating current.

### **10.4 Wye with neutral**

A four-wire wye secondary feeds both three-phase loads and single-phase line-to-neutral loads. The neutral carries the vector (phasor) sum of the unbalanced phase currents. With perfectly balanced linear loads, that's zero. With non-linear loads, triplen harmonics add, and the neutral can carry more current than any phase (section 9.7).

## **11. Instrument transformers (PTs and CTs)**

Instrument transformers shrink high voltages and currents to safe, standard values (120 V and 5 A) for meters and relays, and isolate those devices from the primary. The two safety rules are opposites: **never short a PT secondary, never open a CT secondary.**

### **11.1 What they feed**

- Meters (amps, volts, watts, vars, revenue kWh), protective relays, transducers and SCADA/telemetry.

- They have small VA ratings because they only power instruments. Accuracy matters more than capacity, especially for revenue metering.

- Slide 342 example: a 1200/5 CT and a 100/1 PT feeding relays and meters.

- **Transducers** convert the CT/PT signals into a standard analog signal (often 4–20 mA or 0–10 V) for a PLC, RTU or SCADA system. The HMI is the operator's graphic screen in that system.

### **11.2 Potential (voltage) transformers — PTs / VTs**

- Connected in **parallel** (across) the circuit being measured.

- Secondary is 120 V at rated primary voltage (115 V on older units).

- PT primaries are fused (NEC requires it). Open the PT fuses or switches when working on the equipment, because a PT can backfeed from its secondary.

- **Never short a PT secondary.** It's a voltage source. A short draws destructive current. The slides say primary current could rise about 200×.

- Never remove the ground from an energized PT secondary.

### **11.3 Current transformers — CTs**

- Connected in **series** with the circuit: the primary conductor passes through or is part of the CT.

- Secondary is **5 A** at rated primary current, regardless of the primary rating. (1 A secondaries also exist, common outside North America and on long secondary runs.)

- Types: window/donut/ring (cable passes through), split-core (opens to clamp around a conductor, same idea as a clamp-on ammeter), bar type, wound type, and bushing CTs (mounted around a transformer or breaker bushing).

- Window CTs are less accurate at low ratios than wound CTs.

**Ratio math**



- 600:5 = 120:1. 300 A through it gives 300 ÷ 120 = 2.5 A.

- **Shortcut** for X:5 ratios: double the primary number and drop the last zero. 600:5 → 120:1. 2000:5 → 400:1. (It works because dividing by 5 is the same as ×2 ÷ 10.)

- A window CT has 1 primary turn, so the turns ratio and current ratio are the same number. The secondary has 120 turns on a 600:5 CT.

**Multi-ratio (tapped) CTs.** The secondary has taps X1–X5. Pick the pair whose turns add up (or subtract) to the ratio you need. Leave unused taps open (don't short them).

- Slide 381: a 600:5 CT with sections X1–X2 = 20, X2–X3 = 10, X3–X4 = 50, X4–X5 = 40 turns. For 150:5 = 30:1, use 20 + 10 → **X1–X3**.

- Slide 383: turns from X1 are X2 = 40, X3 = 60, X4 = 160, X5 = 240. For 500:5 = 100:1, use 160 − 60 → **X3–X4**.

**Wrapping the primary through a window CT.** Each extra pass through the window acts like more primary current, so the effective ratio divides by the number of passes.



- 200:5 with 2 passes → 100:5. 3 passes → 66.7:5. 4 passes → 50:5.

- Count passes **through the window**, not loops around the outside. One loop around the housing = 2 passes.

- Slide 394: a 2500/5 (500:1) CT needs 500 ÷ 125 = **4 passes** to act as 125:1.

- Use this when a CT is too big for the load. A 2500:5 CT on a 100 A load reads almost nothing and is inaccurate down there.

### **11.4 Burden, saturation and accuracy**

- **Burden** = everything connected to the secondary: meters, relays, and the resistance of the wiring. Expressed in VA or ohms.

- More burden means the CT has to produce more voltage to push 5 A. Too much burden pushes it toward saturation and its accuracy falls off (the secondary reads low).

- **Saturation:** past a point, more primary current gives no more secondary current. The bend in the excitation curve is the **knee point**. A protection CT must stay below its knee during a fault, or the relay sees less current than is really flowing and may not trip.

- Accuracy also depends on accuracy class, rating factor, temperature, nearby magnetic fields, physical setup, and which tap you use.

### **11.5 Never open an energized CT secondary**

- A CT is driven by the primary current. It will push its share of current through whatever is on the secondary.

- Open the secondary and there's nothing to oppose the flux. The CT acts like a huge step-up transformer, and the secondary voltage can reach **thousands of volts**. That's a shock hazard, and it can arc, burn insulation, and permanently magnetize or damage the core.

- Short CT secondaries (at a shorting block or test switch) **before** removing any meter or relay.

- Keep spare CTs shorted in storage and shipping.

- Don't megger a CT secondary while the primary is energized.

- Ground the CT secondary circuit at **one point only** (industry practice per IEEE C57.13.3). NEC Article 250 Part X covers instrument transformer grounding.

### **11.6 Test switches and shorting terminal blocks**

- **Test switches:** knife switches in the panel between the CTs/PTs and the meters and relays. The CT switches are **make-before-break**. A shorting contact closes across the CT leads before the blade opens the meter circuit, so the CT is never open.

- **Shorting terminal blocks:** a metal shorting bar runs down the block. Screws through the bar tie terminals together. One screw always ties the bar to ground. Adding screws on a CT's terminals shorts and grounds that CT.

- Sequence for pulling a meter on a live CT circuit: install the shorting screws (or open the test switch, which shorts first), verify current is now bypassing the meter, then disconnect.

### **11.7 CT polarity**

- Marks: H1/H2 on the primary, X1/X2 on the secondary, or a dot (black or white) at H1 and X1. Instrument transformer polarity is always subtractive.

- The rule: **current in on polarity (H1) means current out on polarity (X1)** at the same instant.

- Wrong polarity makes meters read backward, makes revenue meters register power flow in the wrong direction, and makes protective relays (differential, directional) cover the wrong zone or misoperate.

- Slides 429–436 work two circuits with two 800:5 CTs and 400 A primary (2.5 A secondaries). Trace each CT's secondary current out of X1 and back to its own X2 by the lowest-impedance path. Where the two CTs' currents push the same way through a meter, it reads 2.5 A. Where the currents meet head-on in a shared meter, they cancel and that meter reads 0 A, while the two currents circulate through the outer meters.

**Common mistakes**

- Counting wraps around the outside of a donut CT instead of passes through the window.

- Using a CT ratio backward. The secondary current is always the small number.

- Shorting unused taps on a multi-ratio CT. Leave them open.

- Thinking a CT "turned off" when the meter is removed. As long as primary current flows, the CT is live.

## **12. Inspection, testing, safety and grounding**

Test before you energize, trend the results over the transformer's life, and never trust that a transformer is dead until both sides are open, tested and grounded.

### **12.1 Receiving inspection (before you sign for it)**

- Inspect on the truck, before unloading: damaged or cracked bushings, oil leaks, a bulged or dented tank, broken gauges, and shipping impact recorders if fitted.

- Look for discoloration, overheating, arc marks (lightning, birds) on used or relocated units.

- Check primary, secondary and ground leads for damage, tight connections, and proper clearances.

- Note damage on the bill of lading before signing. A claim is much harder afterward.

### **12.2 Pre-energization tests**

| Test | What it checks | Notes |
| - | - | - |
| Insulation resistance (megger) | Insulation leakage: each winding to ground and winding to winding (HV–LV, HV–G, LV–G) | DC test. Higher megohms = less leakage. Record it as a baseline for future trending. PI (10 min ÷ 1 min) and DAR (60 s ÷ 30 s) ratios show moisture and contamination |
| Turns ratio (TTR) | The ratio matches the nameplate on every tap of every winding | Low-voltage AC test. Catches shorted turns and wrong tap position. NETA ATS gives the acceptance tolerance (about 0.5% of calculated) |
| Polarity | Markings are correct, or finds unmarked polarity | Most TTR sets also report polarity |
| Winding resistance | Loose connections, broken strands, bad tap-changer contacts | Low-resistance DC test (DLRO / winding-resistance meter). Compare phases and factory data. Correct for temperature |
| Power factor (dissipation factor) | Insulation quality by the ratio of resistive (loss) current to capacitive current | Good insulation has a very low PF, typically well under 1%. Trend against the same unit's past results, not against other equipment |
| CT saturation / excitation | The CT won't saturate at its required burden. Also confirms ratio and polarity | Compare to the manufacturer's excitation curve |

Liquid-filled units also get oil tests: dielectric breakdown, moisture, and dissolved gas analysis (DGA). Gases in the oil point to specific internal problems (arcing, overheating, partial discharge) long before failure.

### **12.3 Periodic maintenance**

- Keep a record for each unit: specs, test history, repairs, spare parts.

- Keep oil at the proper level, and keep insulating liquid or air free of moisture.

- Keep parts clean and free of rust, dirt and corrosion. Keep enclosures and gaskets tight.

- Test winding insulation and the oil periodically.

- Lubricate moving parts. Check fans, coolers, lightning arresters, gauges, alarms, and grounds.

- For dry-type units: vacuum out dust (it blocks cooling) and check that vents aren't obstructed.

### **12.4 Working on or near transformers**

1. **De-energize both sides.** Any transformer can be backfed from its secondary, from a paralleled unit, from a generator, or from a PT.

2. Lock out and tag out every source (NFPA 70E Article 120).

3. Test for absence of voltage on both sides with a properly rated meter or detector.

4. **Ground the windings** to drain stored capacitive charge. Large windings and cables can hold a dangerous charge, especially after DC insulation or winding-resistance testing.

5. Leave personal protective grounds on until all work is done. Work between grounds.

6. When energizing: confirm all grounds and tools are removed, close remotely if possible, know where the emergency shutoffs are, wear the PPE your arc-flash label calls for, and stand clear of the unit.

### **12.5 Bonding and grounding**

- The NEC requires transformer cases, tanks, and other non-current-carrying metal (including fences around outdoor units) to be grounded (NEC 450.10, Article 250).

- Purpose: limit touch voltage from an insulation failure, and give fault current a low-impedance path so the overcurrent device opens fast.

- The effective ground-fault current path must be: electrically continuous, able to carry the fault current safely for as long as it lasts, and low enough impedance to trip the protective device quickly (NEC 250.4).

- Fault current uses **every** available path, dividing in inverse proportion to each path's impedance. It always returns to its source, which for a transformer secondary is the secondary winding.

- Most building transformers create a **separately derived system** (NEC 250.30). The secondary needs a system bonding jumper (neutral to case/ground, at one location only), a grounding electrode conductor, and a supply-side bonding jumper.

- A missing system bonding jumper is a classic install error. A ground fault on that secondary has no path home and won't trip the breaker.

**Common mistakes**

- Comparing a megger reading to a generic "good" number instead of trending it on that unit, corrected for temperature.

- Removing grounds right after a DC test before the winding is discharged.

- Bonding neutral to ground at both the transformer and the downstream panel. That puts neutral current on the grounding conductors.

## **13. Corrections to the slides**

Most of the deck's math checks out. These are the spots where the slides are wrong or misleading. Know the slide's version for the quiz, but know the correct version for the field.

| Slide | Slide says | Correct version |
| - | - | - |
| 48 | Air gaps in a core increase efficiency | Air gaps raise magnetizing current and lower efficiency. They're used on purpose in reactors, neon/ballast and flyback transformers to store energy or limit current, not in ordinary power transformers |
| 53 | More primary turns makes a stronger field and more secondary current | For a fixed supply voltage, more primary turns means *less* flux (E = 4.44 f N Φ) and *lower* secondary voltage. Secondary current is set by the load |
| 73–75 | Short-circuit test "determines FLC" and you record the *secondary* voltage | FLC comes from the nameplate (VA ÷ V). The test measures %Z, and you record the *primary* voltage (the secondary is shorted, so it's near 0 V) |
| 83 | Amps per kVA: 240 V → 4, 480 V → 2, 2,400 V → 0.4 | Exact factor is 1,000 ÷ V: 4.17, 2.08, 0.417. The rounded chart reads about 4% low |
| 196 | Low %Z = better-quality, more expensive transformer | %Z is a design choice. Low %Z gives better regulation but more fault current. High %Z limits fault current |
| 219 | Neutral carries the *sum* of the unbalanced load | The neutral carries the *difference* between the two line currents |
| 226 | 41.7 A ÷ 104.2 A = ".399A", "40% underloaded" | The ratio has no unit (0.40). That side is 40% *loaded*, which is 60% under capacity |
| 229 | "Load 3 is 5kVA, so 3,600 ÷ 120 = 30A" | Load 3 is 3.6 kVA. The 30 A answer is right |
| 234 | Open neutral: 3 kVA load gets 109 V, 3.6 kVA load gets 131 V | Reversed. The smaller load has higher resistance and gets the higher voltage: 3 kVA → 131 V, 3.6 kVA → 109 V |
| 247 | Control transformer parallel: "primary windings connected in series for higher input current" | Copy error. Primaries in **parallel** are for the **lower** input voltage (240 V) |
| 301 | Line current is "line-to-line current" | Line current is the current in one line conductor. Only voltage is measured line-to-line |
| 302, 305 | Values differ "by √3 (or 58%)" | They differ by a factor of 1.732. 58% (0.577) is 1 ÷ √3, so the phase value is 58% of the line value |
| 312 | Advantage of three 1Ø cans: "easier to cool" (garbled) | The usual advantages: you can replace one failed unit, keep one spare, and run open-delta on two units |
| 113, 115 | Protection goes on the primary. Units with integral thermal protection don't need primary fuses | NEC 450.3 allows primary-only or primary-plus-secondary protection. The feeder still needs overcurrent protection, and secondary conductors need their own (240.21(C)) |
| 450 | Bad insulation's PF approaches 100% | Insulation PF rises as it degrades, but you're looking at changes of a fraction of a percent to a few percent, not values near 100%. Trend it on the same unit |

Slide 139's reason for additive polarity (HV winding next to the core) is not the usual explanation either. The standard reason is lead-to-lead voltage stress, as slide 472 says, plus historical practice for small distribution units (ANSI C57.12.00).

## **14. Cheat sheet**

| Topic | Formula or fact |
| - | - |
| Power balance | EP × IP = ES × IS (VA in = VA out) |
| Ratios | NP/NS = EP/ES = IS/IP |
| Induced voltage | E = 4.44 × f × N × Φmax |
| Reflected impedance | ZP = (NP/NS)² × ZS |
| Efficiency | %Eff = Pout ÷ Pin × 100 (typically 96–99%) |
| 1Ø full-load current | I = VA ÷ E = kVA × 1,000 ÷ E |
| 3Ø full-load current | I = VA ÷ (E × 1.732) |
| Amps per kVA (1Ø) | 1,000 ÷ V (120 V → 8.33, 240 V → 4.17) |
| Sizing | kVA = kW ÷ PF, then the next standard size up |
| 120/240 load check | kVA = (I\_L1 + I\_L2) × 120 ÷ 1,000. Each half-winding max = kVA/2 |
| Neutral current (1Ø 3-wire) | I\_N = I\_L1 − I\_L2 |
| Paralleled load share | Each unit carries load × (its kVA ÷ total kVA), if %Z matches |
| Fault current | I\_SC = I\_FL × 100 ÷ %Z |
| Temperature | Max temp = 40 °C ambient + rated rise (plus hot-spot allowance) |
| Buck-boost | Boost: E\_line + E\_sec. Buck: E\_line − E\_sec. Unit carries load current at E\_sec only |
| Wye | E\_L = E\_P × 1.732, I\_L = I\_P |
| Delta | E\_L = E\_P, I\_L = I\_P × 1.732 |
| CT secondary | I\_S = I\_P × 5 ÷ rating. Shortcut: double the primary, drop a zero |
| CT wraps | New ratio = nameplate ratio ÷ passes through the window |
| Polarity | H1 and X1 positive together. Facing LV side: X1 same side as H1 = subtractive |
| AC polarity test | Reading \> applied = additive. Reading \< applied = subtractive |
| PT / CT rules | PT: in parallel, 120 V, never short. CT: in series, 5 A, never open |

**Five things to remember in the field**

1. Any transformer can be backfed. Open, test and ground both sides.

2. Never open a live CT secondary. Short it first.

3. Check each half of a 120/240 V winding, not just the total kVA.

4. Zero-volt test before closing a delta or paralleling transformers.

5. Lower %Z means more fault current downstream. Check AIC ratings when a transformer is replaced.

## **15. What the textbook adds**

*Electrical Wiring—Commercial* (Simmons, Mullin, Ode & Smith, 18th ed., 2023 NEC) treats transformers from the installer's side: which NEC rules apply, how banks are connected, and how much fault current they deliver. The page numbers below are the book's printed page numbers.

### **15.1 Where to find it in the book**

| Topic | Book location |
| - | - |
| Liquid-filled vs dry-type, overcurrent protection, connections | Ch. 13, pp. 313–319 |
| Separately derived 480 → 208Y/120 V worked example | Ch. 13, Fig. 13-3 (p. 317) |
| Utility supply: pad-mount, unit substation, vault; metering | Ch. 13, pp. 319–323 |
| Transformer secondary conductors (240.21(C)) | Ch. 8, p. 237 |
| Harmonics and K-rated transformers | Ch. 5 (p. 111) and Ch. 8 (pp. 242–244) |
| High-leg panelboards, 408.36(B) | Ch. 12, p. 296 |
| Fault current at transformer terminals, Table 18-1 | Ch. 18, pp. 481–486 |
| Backfeed through a transformer from a generator or PV inverter | Ch. 16 (p. 432) and Ch. 22 (p. 550) |

### **15.2 Liquid-filled vs dry-type (Ch. 13)**

- **Liquid-filled:** windings in mineral oil (combustible), silicone, seed-oil (natural ester) or other non-toxic liquids. The liquid insulates HV from LV and carries heat to the tank, radiators or fans.

- **Askarel** (PCBs) was nonflammable and good indoors, but it's toxic. Federal law (Toxic Substances Control Act, 1976) and EPA rules ended its use. Old units have been replaced or had the liquid swapped out.

- **Dry-type:** lighter, simpler to install, no leak containment or coolant changes. Core and coils are open to air. Fans can be added to carry more load.

- A **unit substation** puts the HV switch, the dry-type transformer and the secondary distribution section in one lineup.

### **15.3 NEC 450.3 in practice (Fig. 13-2 and 13-3)**

- 450.3 overcurrent devices protect **the transformer only**. The conductors on each side may need their own protection (Articles 240 and 310).

- Table 450.3(A) is for over 1,000 V. It depends on the transformer's %Z (up to 6%, or 6–10%), fuse vs breaker, and whether the location is **supervised** (qualified people maintain and monitor it). Supervised locations get higher limits.

- Table 450.3(B) is for 1,000 V or less. These are the 125% / 167% / 300% primary-only and 250% primary-plus-secondary rules from section 5.4.

- A transformer with manufacturer's coordinated thermal overload protection can skip individual primary protection, if the feeder protection is no more than 6× primary FLC (%Z up to 6%) or 4× (%Z 6–10%).

**The book's worked example (Fig. 13-3):** 50 kVA, 480 V delta primary, 208Y/120 V secondary, installed as a separately derived system.

| Step | Primary | Secondary |
| - | - | - |
| FLC = kVA × 1,000 ÷ (E × 1.732) | 50,000 ÷ (480 × 1.732) = 60 A | 50,000 ÷ (208 × 1.732) = 139 A |
| × 125% | 75 A → next standard size: 80 A dual-element time-delay fuses in a 100 A switch | 174 A → 175 A fuses or breaker |
| Maximum allowed | 60 × 250% = 150 A (only with secondary protection) | — |

The 175 A secondary device also protects the panelboard (408.36) and the secondary conductors (240.21(C)).

The same figure labels the grounding parts of a separately derived system, all in 250.30(A): the **system bonding jumper**, the **supply-side bonding jumper**, the **grounding electrode conductor** and the **grounding electrode**. The equipment grounding conductor on the primary is sized by 250.122.

### **15.4 Transformer connections (Ch. 13)**

| Connection | What it gives you | Key point |
| - | - | - |
| Single-phase 120/240 V | 120 V or 120/240 V, 2- or 3-wire | The center tap must be grounded (Art. 250 Part II) |
| Open delta (two transformers) | 3Ø, or 3Ø plus 1Ø from a center tap on one unit | Useful where the utility has only two primary phases, or 3Ø load may grow (add the third unit later). Also lets a delta bank limp along if one unit fails |
| Three-wire delta | 3Ø only | One phase may be grounded: a **corner-grounded delta**. Overcurrent devices generally aren't allowed in the grounded phase |
| Four-wire (high-leg) delta | 240 V 3Ø plus 120/240 V 1Ø | A–N and C–N = 120 V. **B–N = 208 V** (the high leg) |
| Four-wire wye | 208Y/120, 480Y/277, 600Y/347 | The most common commercial system. Line-to-neutral loads on any phase |

**Open-delta capacity:** two units deliver 86.6% of their combined rating, or 57.7% of what three would give in full delta. Both ways land on the same number:



For open delta feeding 3Ø loads only, the center tap isn't connected.

**High-leg delta rules** (also Ch. 12, p. 296):

- The high leg (also called red leg or wild leg) can't be used for line-to-neutral loads. At 208 V to ground it would overvolt any 120 V load.

- Mark it **orange** (or other effective means) wherever the neutral is present: NEC 110.15, 230.56.

- It must be the **B phase**, in the center position in panelboards and switchboards: 408.3(E)(1).

- Panels with a high leg must carry a field-applied warning, filled in as "Caution \_\_\_ Phase Has \_\_\_ Volts to Ground" (408.3(F)).

- **Meter-socket trap:** many utilities require the high leg on the *right-hand* position (C) in self-contained meter sockets of 200 A or less, then back to the center (B) in the service disconnect. CT-metered services over 200 A avoid this.

The book shows every 3Ø connection with a **delta primary**. That's the most common choice because the primary needs only three conductors. For anything unusual, get engineering or manufacturer help.

### **15.5 Utility side, metering and backfeed (Ch. 13, 16, 22)**

- **NEC vs NESC:** utility equipment up to the **service point** follows the National Electrical Safety Code, and premises wiring after it follows the NEC (90.2(D)(5)). The utility decides where the service point is.

- Supply arrangements: pad-mount transformers feeding a bus duct, unit substations (owner-furnished, common in industrial plants), pad-mount enclosures with the CTs inside ("transclosures"), and transformers in underground vaults (Art. 450 Part III).

- **Metering:** a single tenant may be metered on the **primary** side with PTs and CTs, often with 15-minute demand registers for kW and kVAR. High demand or low PF raises the bill. Up to 200 A is usually direct-metered. Larger services use 320 A sockets or CT metering, with the utility wiring from the CTs to the meter.

- **Backfeed:** a generator without a listed transfer switch, or a PV inverter, can push power back through the service transformer. The book's PV example: 240 V from an inverter can show up as 12,000 V or more on the utility primary. That's why inverters must be utility-interactive (anti-islanding) and why transfer switches must be listed.

### **15.6 Secondary conductors and panelboards**

- Conductors leaving a transformer secondary follow 240.21(C). The rules work like the feeder tap rules in 240.21(B). You have to account for the voltage ratio when checking whether primary protection covers the secondary.

- Panelboards fed through a transformer need overcurrent protection on the **secondary** side (408.36(B)). The exception: a 2-wire primary to 2-wire secondary, or a 3-wire delta–delta, can be protected by the primary device through the ratio (240.21(C)(1)).

- Service conductors only have the utility's transformer primary fuses ahead of them. Those fuses protect the utility transformer, not your conductors, so keep service conductors inside a building as short as possible.

### **15.7 Harmonics and K-rated transformers (Ch. 5, 8)**

- Non-linear loads can overheat a transformer **without** tripping its overcurrent device (NEC 450.3 Informational Note 2).

- Symptoms to recognize: overheated neutrals, hot or failed transformers, hot lugs and busbars, unexplained breaker trips, flickering lights.

- Fixes the book lists: oversize (derate) the transformer, use a K-rated transformer, and run separate neutrals for non-linear loads. IEEE C57.110 covers transformer capability with non-sinusoidal current.

### **15.8 Fault current from a transformer (Ch. 18)**

The book adds two refinements to the section 8 formula:

1. **±10% impedance tolerance.** Listed transformers of 25 kVA and up can have actual %Z up to 10% below the nameplate value. For the worst case, the book multiplies the marked %Z by 0.9.

2. **Voltage swings.** A 10% higher system voltage means 10% more fault current.



**Book example (Problem 1):** 225 kVA, 208Y/120 V, 2 %Z, infinite primary.

| Marked %Z | Multiplier = 100 ÷ (%Z × 0.9) | Fault current (FLC 625 A) |
| - | - | - |
| 1% | 111.11 | 69,444 A |
| 2% | 55.56 | 34,725 A |
| 4% | 27.78 | 17,363 A |

FLC = 225,000 ÷ (208 × 1.732) = 625 A.

**Conductors cut the fault current (Problem 2, point-to-point method):** 25 ft of three parallel 250 kcmil copper in PVC from that transformer reduces 34,725 A to about 30,558 A at the service. The method computes a factor f from the conductor length, the conductor constant C and the voltage, then multiplies by M = 1 ÷ (1 + f) (here f = 0.130, M = 0.88).

- Motors running at the moment of a fault act as generators briefly and add current ("motor contribution").

- Good practice in the book: pick interrupting ratings at least 25% above the calculated available fault current.

- **Marking:** 110.24(A) requires the available fault current, and the date it was calculated, on non-dwelling service equipment. 110.24(B) requires it to be rechecked when changes (such as a bigger or lower-%Z utility transformer) affect it. 110.16(B) (new in 2023) requires an arc-flash label on non-dwelling service and feeder equipment rated 1,000 A or more.

### **15.9 Other textbook points worth knowing**

- **Unbalanced voltage** (Ch. 7): causes include large single-phase loads, open connections at a transformer secondary, open-delta banks, and single-phase transformers with unequal %Z in the same 3Ø bank. A little voltage unbalance makes a lot of extra heat in the motor phase with the highest current. Some lights dimming while others brighten points to a bad utility transformer winding.

- **Class 2 transformers** (Ch. 20) for low-voltage remote control are built to limit their own output: on overload, the voltage drops. Others use an auto-reset thermal device or fuse links.

- **Plan symbols** (Ch. 2 and Appendix): a dry-type transformer is tagged with a number keyed to the transformer schedule (for example "T45"). The one-line symbol shows the delta primary and grounded-wye secondary.
