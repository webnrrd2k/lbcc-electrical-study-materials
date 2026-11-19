# Lab 3 Motor Control: Forward / Reverse Wiring Diagrams (PRELIMINARY, text only)

Text version of `wiring-diagrams.html`, without the drawings. **Preliminary:** drawn from the lab sheet (LAB3-F20b) and the layout drawings, before the panel was built. Check the terminal positions on your own parts.

## Build order, with quick checks along the way

Wire one section at a time and check it before you move on. A wrong contact block or a loose pin takes seconds to find on the bench and an afternoon to find in a finished panel. **Rules for every ohm/continuity check:** cord unplugged, 3PHIN feed unplugged, and **CB2 OFF**. The transformer secondary connects the 24 V bus to common through a few ohms, so with CB2 on, almost every control check reads "continuous" and tells you nothing. Clip leads help when you need one hand on a button. "Open" means the meter reads OL.

### 1. Bench-check the door devices (before wiring them)

Ohm across each contact by itself. This proves the contact blocks are the right type and on the right terminals.

| Meter on | Condition | Should read |
|---|---|---|
| STOP1 1–2, STOP2 1–2 | at rest | continuous (NC) |
| STOP1 1–2, STOP2 1–2 | button pressed | open |
| FWD 3–4, REV 3–4 | at rest | open (NO) |
| FWD 3–4, REV 3–4 | button pressed | continuous |
| FLS 21–22, RLS 21–22 | at rest | continuous (NC) |
| FLS 21–22, RLS 21–22 | lever actuated | open. In the circuit, FLS opens wire 4 → 5 and drops FW only; RLS opens wire 9 → 10 and drops RV only |
| FLS 13–14, RLS 13–14 | at rest / actuated | open / continuous (NO, not used in this lab) |

### 2. Bench-check each contactor and its aux block

With the aux block snapped on the front, push the contactor armature in by hand (unpowered) to operate every contact. Do this for FW and RV.

| Meter on | Condition | Should read |
|---|---|---|
| A1–A2 | at rest | a definite resistance (the coil): not 0, not open |
| 1L1–2T1, 3L2–4T2, 5L3–6T3, 7L4–8T4 | at rest | open |
| 1L1–2T1, 3L2–4T2, 5L3–6T3, 7L4–8T4 | armature pushed in | continuous |
| aux 23–24 | at rest / pushed in | open / continuous (NO, pilot light) |
| aux 31–32 | at rest / pushed in | continuous / open (NC, interlock) |

### 3. Bench-check each overload and set it up

Set the FLA dial and the AUTO/HAND reset selector where your instructor wants them (HAND: you press R after a trip; AUTO: it resets itself).

| Meter on | Condition | Should read |
|---|---|---|
| 95–96 | normal | continuous (NC) |
| 97–98 | normal | open (NO, not used) |
| 95–96 and 97–98 | trip it with the test button, if your model has one | 95–96 open, 97–98 continuous. Press R to reset, then recheck 95–96 |

### 4. Join each overload to its contactor, then check the pass-throughs right away

Plug the overload onto the contactor and **tighten the contactor's A2 and 2T1/4T2/6T3 screws** onto the overload's pins. Then install the short wire from overload A2 to overload 95 (wire 7 on FW, 12 on RV; see note 10).

| Meter on | Condition | Should read |
|---|---|---|
| overload A2 to contactor A1 | at rest | coil resistance. Open = the A2 pin isn't clamped |
| overload 14/22 to contactor 7L4 | at rest / armature pushed in | open / continuous. Proves the 14/22 pass-through |
| contactor 1L1 to overload 2T1 (same for L2, L3) | armature pushed in | continuous (through the heater) |
| contactor A1 to overload 96 | after wire 7 or 12 is on | coil resistance. This one check proves the coil, the A2 pin, wire 7/12 and the OL contact all at once |

### 5. Wire the 120 V supply and the transformer (cord, CB1, TB1, TBG1, T1, CB2, TB buses)

Install the primary links H1–H3 and H2–H4, the secondary link X2–X3, and the TB4–TB6 and TB7–TB9 comb jumpers.

| Meter on | Condition | Should read |
|---|---|---|
| cord plug H to N | CB1 on / off | low resistance (transformer primary) / open |
| cord plug H and N to G | CB1 on | open |
| TBG1 to transformer X4 | — | continuous (X4 is bonded to ground) |
| TB7 to TB9, TB4 to TB6 | — | continuous (comb jumpers seated) |
| **Powered** (cord in, 3PHIN still unplugged): TB7 to TB4 | CB2 on / off | ≈24 V AC / 0 V. Then unplug before you go on |

### 6. Wire the door (jumpers 2, 3, 4, 9, 15)

Check at the door ends of the wires before they go into the duct.

| Meter on | Condition | Should read |
|---|---|---|
| wire 1 (STOP1 1) to wire 3 (STOP2 2) | at rest / either STOP pressed | continuous / open |
| wire 3 to wire 4 (FWD 4) | at rest / FWD pressed | open / continuous |
| wire 3 to wire 9 (REV 4) | at rest / REV pressed | open / continuous |
| wire 4 to wire 5 (FLS 22) | at rest / FLS actuated | continuous / open |
| wire 9 to wire 10 (RLS 22) | at rest / RLS actuated | continuous / open |
| FWDON X2 to REVON X2 | — | continuous (wire 15 jumper) |

### 7. Wire the forward and reverse rungs (wires 1–12)

CB2 OFF for all of these. TB7 is the 24 V bus, TB4 is common.

| Meter on | Condition | Should read |
|---|---|---|
| TB7 to FW A1 | nothing pressed | open |
| TB7 to FW A1 | hold FWD | continuous |
| TB7 to FW A1 | hold FWD and actuate FLS | open (limit switch) |
| TB7 to FW A1 | hold FWD and press STOP1 or STOP2 | open |
| TB7 to FW A1 | no buttons, push FW's armature in | continuous (seal-in through 7L4 → 14/22) |
| RV 31 (wire 5) to RV 32 (wire 6) | at rest / RV armature pushed in | continuous / open. The interlock in the forward rung. (Check it here, not from TB7: with an armature pushed in, a back path through both coils can fool the meter) |
| FW A2 to TB4 | — | continuous (wire 7, OLF 95–96, wire 8) |
| TB7 to TB4 | nothing pressed / hold FWD | open / FW coil resistance. The whole forward rung in one check |
| Repeat for reverse: TB7 to RV A1 | hold REV, then add RLS or a STOP | continuous, then open |
| FW 31 (wire 10) to FW 32 (wire 11) | at rest / FW armature pushed in | continuous / open (interlock in the reverse rung) |
| TB7 to RV A1 | no buttons, push RV's armature in | continuous (seal-in) |
| RV A2 to TB4 | — | continuous (wire 12, OLR 95–96, wire 8) |
| TB7 to TB4 | hold REV | RV coil resistance |

### 8. Wire the pilot lights (wires 13–17)

CB2 OFF.

| Meter on | Condition | Should read |
|---|---|---|
| TB8 to FWDON X1 | at rest / FW armature pushed in | open / continuous |
| TB9 to REVON X1 | at rest / RV armature pushed in | open / continuous |
| FWDON X2 and REVON X2 to TB4 | — | continuous (wire 15) |

### 9. Wire the power circuit (L1–L3, T1–T3)

3PHIN feed unplugged. Watch for a phase swap: the one place the reversal can go wrong.

| Meter on | Condition | Should read |
|---|---|---|
| FW 1L1 to RV 5L3, FW 5L3 to RV 1L1, FW 3L2 to RV 3L2 | — | ≈0 Ω |
| FW 1L1 to RV 1L1 | — | open (if it's continuous, L1/L3 aren't swapped) |
| socket 24 (L1) to TB-T1, TB-T2, TB-T3 | nothing pushed | all open |
| socket 24 (L1) to TB-T1 | FW armature pushed in | continuous |
| socket 24 (L1) to TB-T3 | RV armature pushed in | continuous (RV swaps L1 and L3) |
| any L to any other L, any L to ground | — | open |

### 10. First power-up: control circuit only

Cord in, 3PHIN still unplugged, CB2 on. If something doesn't work, put the black lead on TB4 and walk the red lead down the rung (TB7, wire 2, wire 3, then hold FWD: wire 4, wire 5, A1). The fault is between the last point with 24 V and the first with 0 V. If A1 has 24 V and the coil won't pull in, check A2: 24 V there means the return (wire 7 / OL 95–96 / wire 8) is open.

| Meter on | Condition | Should read |
|---|---|---|
| Press FWD | — | FW pulls in, stays in after release, FWDON lights |
| Press REV while FW is running | — | nothing happens (interlock) |
| Press STOP1, then STOP2 (restart in between) | — | FW drops out each time |
| Actuate FLS while FW is running | — | FW drops out; RV still starts with REV |
| Repeat all of the above for REV, REVON and RLS | — | same, mirrored |
| Then, with the instructor: plug in 3PHIN | — | run the operation tests on the lab sheet |

## Wire list (one row per physical conductor)

| # | Wire | Color | From | To | Route | Note |
|---|---|---|---|---|---|---|
| | **120 V supply** | | | | | |
| 1 | **H** | black | *cord* | CB1-1 (top) | cord → left tray → top duct | Cord hot (smooth conductor if a flat cord) |
| 2 | **N** | white | *cord* | TB1 (top) | cord → left tray → top duct | Cord neutral (may be ribbed black on a flat cord) |
| 3 | **G** | green | *cord* | TBG1 (top) | cord → left tray → top duct | Cord ground |
| 4 | **H1** | black | CB1-2 (bottom) | Transformer H1 | bottom duct → side channel → top duct |  |
| 5 | **N2** | white | TB1 (bottom) | Transformer H4 | bottom duct → side channel → top duct | Ladder calls this N2 at TB1 and N1 at the transformer. See note 4 |
| | **24 V secondary** | | | | | |
| 6 | **G** | green | TBG1 (bottom) | Transformer X4 | bottom duct | Bonds X4 to ground, landed ON the transformer X4 screw |
| 7 | **X4** | white | Transformer X4 | TB4 (bottom) | bottom duct | Starts the X4N bus (TB4–TB6 comb jumper) |
| 8 | **X1** | red | Transformer X1 | CB2-1 (top) | bottom duct → side channel → top duct |  |
| 9 | **24** | red | CB2-2 (bottom) | TB7 (bottom) | bottom duct | Starts the 24 V bus (TB7–TB9 comb jumper) |
| | **Rungs 5–6: FORWARD** | | | | | |
| 10 | **1** | red | STOP1 1 (door) | TB7 (top) | **DOOR CHANNEL (right tray)** |  |
| 11 | **2** | red | STOP1 2 (door) | STOP2 1 (door) | door (jumper) | Door jumper |
| 12 | **3** | red | STOP2 2 (door) | FWD 3 (door) | door (jumper) | Door jumper |
| 13 | **3** | red | FWD 3 (door) | REV 3 (door) | door (jumper) | Door jumper |
| 14 | **3** | red | REV 3 (door) | FW 7L4 | **DOOR CHANNEL (right tray)** | FW holding contact, line side (13 on some contactors) |
| 15 | **3** | red | FW 7L4 | RV 7L4 | top duct | Panel jumper to RV holding contact |
| 16 | **4** | red | FWD 4 (door) | FLS 21 (door) | door (jumper) | Door jumper |
| 17 | **4** | red | FLS 21 (door) | OLF 14/22 (= FW 8T4) | **DOOR CHANNEL (right tray)** | FW holding contact, load side (14 on some contactors) |
| 18 | **5** | red | FLS 22 (door) | RV aux 31 | **DOOR CHANNEL (right tray)** | Into the RV interlock (NC) |
| 19 | **6** | red | RV aux 32 | FW A1 | top duct |  |
| 20 | **7** | red | OLF A2 (= FW coil A2) | OLF 95 | on the overload face | Short loop on OLF face. Field wire, NOT internal: see note 10. Color: see note 3 |
| 21 | **8** | white | OLF 96 | TB5 (bottom) | bottom duct |  |
| | **Rungs 7–8: REVERSE** | | | | | |
| 22 | **9** | red | REV 4 (door) | RLS 21 (door) | door (jumper) | Door jumper |
| 23 | **9** | red | RLS 21 (door) | OLR 14/22 (= RV 8T4) | **DOOR CHANNEL (right tray)** | RV holding contact, load side |
| 24 | **10** | red | RLS 22 (door) | FW aux 31 | **DOOR CHANNEL (right tray)** | Into the FW interlock (NC) |
| 25 | **11** | red | FW aux 32 | RV A1 | top duct |  |
| 26 | **12** | red | OLR A2 (= RV coil A2) | OLR 95 | on the overload face | Short loop on OLR face. Field wire, NOT internal: see note 10. Color: see note 3 |
| 27 | **8** | white | OLR 96 | OLF 96 | bottom duct | OLR 96 joins OLF 96 |
| | **Rungs 9–10: pilot lights** | | | | | |
| 28 | **13** | red | TB8 (top) | FW aux 23 | top duct |  |
| 29 | **14** | red | FW aux 24 | FWDON X1 (door) | **DOOR CHANNEL (right tray)** |  |
| 30 | **16** | red | TB9 (top) | RV aux 23 | top duct |  |
| 31 | **17** | red | RV aux 24 | REVON X1 (door) | **DOOR CHANNEL (right tray)** |  |
| 32 | **15** | white | REVON X2 (door) | FWDON X2 (door) | door (jumper) | Door jumper |
| 33 | **15** | white | FWDON X2 (door) | TB6 (bottom) | **DOOR CHANNEL (right tray)** |  |
| | **Power circuit (simulated 3-phase)** | | | | | |
| 34 | **L1** | black | 3PHIN socket 24 (L1) | FW 1L1 | top duct |  |
| 35 | **L1** | black | FW 1L1 | RV 5L3 | top duct | RV swaps L1 and L3 |
| 36 | **L2** | black | 3PHIN socket 21 (L2) | FW 3L2 | top duct |  |
| 37 | **L2** | black | FW 3L2 | RV 3L2 | top duct |  |
| 38 | **L3** | black | 3PHIN socket 14 (L3) | FW 5L3 | top duct |  |
| 39 | **L3** | black | FW 5L3 | RV 1L1 | top duct | RV swaps L1 and L3 |
| 40 | **T1** | black | OLF 2T1 | OLR 2T1 | bottom duct | Jumper OLF to OLR |
| 41 | **T1** | black | OLR 2T1 | TB-T1 (bottom) | bottom duct | One wire per TB-T terminal |
| 42 | **T2** | black | OLF 4T2 | OLR 4T2 | bottom duct | Jumper OLF to OLR |
| 43 | **T2** | black | OLR 4T2 | TB-T2 (bottom) | bottom duct | One wire per TB-T terminal |
| 44 | **T3** | black | OLF 6T3 | OLR 6T3 | bottom duct | Jumper OLF to OLR |
| 45 | **T3** | black | OLR 6T3 | TB-T3 (bottom) | bottom duct | One wire per TB-T terminal |

Door-channel wires (exactly 9): 1, 3, 4, 5, 9, 10, 14, 15, 17.

## Things to check

1. **PRELIMINARY: check your own parts before you wire.** This page was drawn from the lab sheet (LAB3-F20b), the component-layout and front-panel drawings, and the Additional Specifications. It was **not** drawn from photos of a built panel. The wire numbers and from/to terminals come from the ladder and should be right. Where each terminal physically sits on your contactors, aux blocks and the CR socket is a **guess**. Read the numbers stamped on your parts and go by those. Once the panel is wired, send photos and this page can be redrawn to match, the same as Lab 2.

2. **Exactly 9 wires through the door channel, and the door jumpers are why.** Wire numbers 1, 3, 4, 5, 9, 10, 14, 15 and 17 each cross the door **once** (the yellow tags). To keep it at one crossing per number, make these jumpers on the door itself: 2 (STOP1→STOP2), 3 (STOP2→FWD→REV), 4 (FWD→FLS), 9 (REV→RLS) and 15 (REVON X2→FWDON X2). Run all 9 in the **right** tray. The left tray is for the cord only. A control wire in the left tray, or a neutral (15) running by itself, loses selloff points.

3. **Wires 7 and 12 are not neutrals, so what color?** They run from the coil A2 to the overload 95, which is *upstream* of the OL contact. When an overload trips, 7 or 12 is at 24 V. The spec only says "24VAC Neutral: White", so they are drawn red here. In Lab 2 the same wire (wire 4) was white. Ask which color the instructor wants before you cut them. Wires 8 and 15 land straight on the X4N bus, so white is right for those.

4. **The lab sheet names the neutral jumper two ways.** The wire from TB1 (bottom) to the transformer is marked **N2** at TB1 and **N1** at the transformer. It is one conductor, so it gets one number. These labels use N2, as printed at the terminal block. Change it in the script if your instructor uses N1.

5. **Two kinds of contactor, same terminals.** The note on the lab sheet says some contactors use 13/14 for the holding contact and others use 7L4/14-22. 13 = 7L4 and 14 = 14/22. On the 7L4 type with the overload attached, the load side of that contact (8T4) is reached through the overload's **14/22** pass-through. The coil's A2 is reached through the overload's **A2** pass-through. Both work the same as in Lab 2. The interlocks (31-32, NC) and the pilot contacts (23-24, NO) are on the front aux block. Check that your aux block really has 23-24 NO and 31-32 NC.

6. **Transformer grounding: green goes to the X4 screw.** Per *Proper Grounding of the Motor Control Transformer*, the green bond lands directly on the transformer's X4 terminal, next to the white X4. Landing it at TB4 instead would be a code violation, even though Constructor draws it that way. Procedure photo 4 has to show it clearly.

7. **The power circuit: RV swaps L1 and L3.** FW gets L1/L2/L3 on 1L1/3L2/5L3. RV gets L3/L2/L1. The diagram makes the line-side jumpers contactor to contactor (FW 1L1→RV 5L3, FW 3L2→RV 3L2, FW 5L3→RV 1L1), so each socket terminal has only one wire. On the load side, the TB-T terminals are too small for two wires, so each OLF output (2T1/4T2/6T3) jumpers to the same OLR terminal, and one wire runs from OLR to the bottom of TB-T1..T3. That puts two wires under each OLR load-side screw, which the overload's box clamp is made for. Nothing goes on the top of TB-T (the motor is simulated) or upstream of the socket. Before power-on, an ohmmeter check catches a swap. FW 1L1 to RV 5L3 should be ~0 Ω, and FW 1L1 to RV 1L1 should be OL.

8. **Interlocking is electrical only.** FWD and REV are plain NO buttons with no button interlock. The only thing keeping FW and RV from both pulling in is each one's NC 31-32 in the other's rung. If your reversing pair has a mechanical interlock between them, install it too. Operation tests 7 and 8 film exactly this.

9. **Not used in this lab (leave empty).** TB2, TB3, TBG2, TBG3, the selector switch, the limit switches' NO 13-14, OLF/OLR 97-98, the other CR socket terminals, and the tops of TB-T1..T3. The spec says "No wiring to extra terminals".

10. **A2 to 95 is a wire YOU install. It is not internal.** Wires 7 (FW A2 → OLF 95) and 12 (RV A2 → OLR 95) are easy to skip, because the overload plugs right onto the contactor and looks like one unit. But the overload's 95-96 is a **separate, isolated contact**. Nothing inside connects it to the coil, because the maker can't know where you want it in your circuit (common side, hot side, several starters, a PLC input). Leave 7 or 12 off and that coil has no return path, so nothing happens when you press FWD or REV, even though every switch tests fine. 

   **Connections the parts make for you (don't wire these):** the two terminals of one contact (1L1-2T1, 7L4-8T4, 31-32, 23-24, a pushbutton's pair), connected only when that contact is closed; the overload's **A2** and **14/22** pass-throughs, which are the contactor's A2 and 8T4 (note 5; the pin only connects if the contactor's screw is tightened on it); the overload's line side, which plugs into the contactor's T terminals; and the top and bottom screws of one feed-through TB. 

   **Connections you must make:** everything else, including A2 → 95 (7, 12), 96 → common (8), the transformer links (H1-H3, H2-H4, X2-X3) and the comb jumpers (TB4-TB6, TB7-TB9). 

   **Rule of thumb:** separate contacts on one device are never connected inside it. 

   **Check before power-on:** with the cord unplugged, ohm from each coil's A2 to OLF 96. It should read ~0 Ω through wire 7 or 12 and the closed OL contact. If it reads OL (open), that return is missing. Powered, the symptom is 24 V (hot to OL 95) but 0 V (hot to coil A2).
