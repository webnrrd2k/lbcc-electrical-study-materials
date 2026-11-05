# Lab 2 Motor Control: Start / Stop / Jog, Matched to My Panel

This redraws the LAB2-F20 circuit so it lines up with the photos of Jeff Polaski's panel. Figure 1 puts each part where it sits on the door and backplate. Figure 2 is the same ladder diagram as the lab sheet, labeled with the same tags, places, wire colors and wire numbers. An orange 1 marks a problem described at the bottom of the page.

red: 24 V control (hot side) white: 24 V common (X4N side) / 120 V neutral black: 120 V hot ribbed black: cord neutral green: ground wire number (same as the lab sheet)

## Figure 1: Physical wiring diagram (laid out like your photos)

Parts are in the same left-to-right order as your photos. The door is shown from the inside, the way photo 2 sees it, so it is the mirror image of the front: from the front the order is STOP, START, (unlabeled red), JOG, selector, LS1, LS2, MOTOR-ON, spare pilot. The routes through the ducts are simplified. The terminal each wire lands on is what matters.

## Figure 2: The lab ladder, relabeled with the physical parts

The rungs, contact numbers and wire numbers are all the same as on the lab sheet. What's added: each device is labeled with where it is on your panel, the wires are in their real colors, and CR1's coil is labeled with its socket pins 2 and 7. Those are what A1/A2 mean on an 8-pin octal relay.

## Wire list (from → to)

| Wire | Color | From | To | Note |
| --- | --- | --- | --- | --- |
| **H** | black | Cord hot | CB1-1 | Smooth conductor of the flat cord |
| **N** | ribbed black | Cord neutral | TB1 (top) | See problem 2 |
| **G** | green | Cord ground | TBG1 (top) |  |
| **H1** | black | CB1-2 | T1 H1 | Loops below CB1, up the top duct |
| **N2/N1** | white | TB1 (bottom) | T1 H4 | Via bottom duct, up beside T1 |
| **X4** | green | T1 X4 | TBG1 (bottom) | Grounds the 24 V common ✓ |
| **X4** | white | T1 X4 | TB4 (bottom) | Starts the X4N common bus |
| **X1** | red | T1 X1 | CB2-1 | Exact route not visible |
| **24** | red | CB2-2 | TB7 (bottom) | Red loop under CB2 |
| **1** | red | TB7 (top) | PB1 STOP 1 | To the door |
| **2** | red | PB1 STOP 2 | PB2 START 3 | Jumper on the door |
| **2** | red | PB2 START 3 | CR1 pin 1 |  |
| **3** | red | PB2 START 4 | CR1 pin 3 and pin 2 (A1) | See 'couldn't confirm' |
| **4** | white | CR1 pin 7 (A2) | OL1 95 | See problem 4 |
| **4** | white | OL1 A2 (= M coil A2) | OL1 95 | White loop on the right of OL1 |
| **5** | white | OL1 96 | TB5 (bottom) |  |
| **7** | red | TB8 (top) | CR1 pin 8 |  |
| **7** | red | CR1 pin 8 | PB4 JOG 3 |  |
| **8** | red | PB4 JOG 4 | CR1 pin 6 |  |
| **8** | red | CR1 pin 6 | M A1 |  |
| **9** | red | TB9 (top) | M 7L4 |  |
| **10** | red | OL1 14/22 (= M 8T4) | PL1 X1 | Red wire that runs up across the contactor face |
| **11** | white | PL1 X2 | TB6 (bottom) |  |

Each TB terminal is a feed-through, so its top and bottom screws are the same point. The orange comb jumpers tie TB4–TB6 into one X4N bus and TB7–TB9 into one 24 V bus. TB2, TB3, TBG2, TBG3, TBL1–3, OL1 97/98, PB3, SS1, PL2 and LS1/LS2 have nothing on them in this lab.

## Problems and things to check

1**Schematic: JOG skips the STOP button.** Rung 7 is fed straight from TB8 on the 24 V bus, not from the far side of STOP. If someone is holding JOG, pressing STOP does nothing. M stays on until JOG is let go (or OL1 trips). In the usual "jog with a control relay" circuit, STOP comes first and feeds both the CR1 rung and the M rung, so STOP always wins. To fix it, feed wire 7 from wire 2 (the load side of STOP) instead of from TB8. Your panel is wired the way the lab sheet shows, so ask your instructor whether this is on purpose.

2**The cord neutral is a black wire.** Your cord is a flat 3-wire cord where both current-carrying wires are black, and the neutral is marked only by ribs on its jacket. The black on TB1 has to be the ribbed one. If hot and neutral are swapped, CB1 ends up switching the neutral, and the transformer primary stays live even with CB1 off. Check it with the cord plugged in: CB1-1 should read about 120 V to ground, and TB1 about 0 V. Then put white tape on the neutral at both ends. The cord also comes in through a Halex clamp made for NM (Romex) cable. A grip listed for flexible cord is the right part, so check whether your instructor cares.

3**Things the lab sheet doesn't make obvious (no change needed).** (a) On the 8-pin socket, CR1's "A1/A2" are pins 2 and 7. Its contacts are 1–3 and 8–6, which match the 750-series pinout. (b) The "M 7L4 – 14/22" contact on rung 9 is the contactor's 4th pole (7L4–8T4) used as a holding contact. You reach its bottom end through the overload's 14/22 pass-through terminal, because OL1 covers 8T4. (c) In the same way, the white loop at OL1 "A2" is really the contactor coil's A2. (d) The fuse sizes work: 50 VA ÷ 120 V ≈ 0.42 A primary, so CB1 at 1.5 A is under the 500% allowed for control transformers drawing less than 2 A. 50 VA ÷ 24 V ≈ 2.1 A secondary, which CB2 at 2 A fits.

4**Wire 4 is white, but it isn't grounded.** Wire 4 runs from the coils to OL1-95, and it sits *upstream* of the OL contact. When OL1 trips with a coil energized, this "white" wire reads 24 V to ground. NFPA 79 keeps white for grounded conductors only, so strictly wire 4 should be red, or whatever your class uses for control wires. Wires 5 and 11 land straight on the X4N bus, so white is correct for them. This is a fine point, and plenty of lab panels do it the same way.

5**The power circuit isn't built yet.** Nothing is on TBL1–3 or on M's 1L1/3L2/5L3, so the M contacts and OL1 heaters in the right half of the sheet aren't in your photos yet. When you wire the motor, set OL1's dial to the motor's nameplate full-load current. A ½ HP 3-phase motor is roughly 1–2.5 A depending on voltage, and the dial should read in that range.

6**Small housekeeping items.** I couldn't see wire-number markers on the conductors. Adding them (1, 2, 3, ... 11) would tie the panel to the sheet in a way anyone can follow. The "TBL1-3" label sits under the CR1 socket rather than under the 3PH terminals. Also check that the door is bonded to the enclosure with a ground jumper, since it holds metal-bodied devices. That jumper isn't in the photos.

### Things I couldn't confirm from the photos

I checked the transformer links, both breakers, the TB groups, the overload terminals (95/96/A2/14/22), the contactor (7L4/A1) and the door devices against your photos, and they match the sheet. The one place I couldn't trace every conductor is CR1's socket. There are five red ferrules on top, a red and a white on the bottom, and the relay hides part of it. Since the bottom white can only be wire 4, the bottom row is the coil, so I've shown wire 3 reaching pin 2 from START. Worth checking with a continuity test: pin 1 to START 3; pins 2 and 3 to START 4; pin 8 to TB8 and JOG 3; pin 6 to JOG 4 and M A1.