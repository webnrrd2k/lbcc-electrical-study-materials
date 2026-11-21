# ELECT 280 — Traffic Signal Systems 1

Study guides and flashcards for ELECT 280. The class covers reading Caltrans traffic signal plans, the Caltrans Standard Plans legend, signal phasing and the ring diagram, the Model 332 controller cabinet, loop detectors, the 210 conflict monitor, conduit and conductor schedules, and basic 2070 controller programming.

[← Back to all classes](../README.md)

---

## Quick reference

- **[Cheat Sheet (PDF)](elect_280_cheat_sheet.pdf)** ([read on GitHub](elect_280_cheat_sheet.md)): the most important ideas from the course on 7 pages:
    + **Course at a glance:** the 10 core skills, in the order the class builds them
    + **Key numbers and formulas:** ring diagram pairs, detector designations (2I2U), 332 cabinet layout, PDA breakers, diode card math, cable rules, loop inductance and yellow-interval formulas
    + **Every assignment:** what it asks, the skills it tests, and the common mistakes
    + **Safety and the biggest misunderstandings**

- **[Syllabus Study Guide (PDF)](elect_280_study_guide.pdf)** ([read on GitHub](elect_280_study_guide.md)): 17 pages that follow the syllabus topic by topic (A–K). Each topic has the same seven parts:
    1. Main ideas
    2. Examples
    3. Background: math up to trigonometry, with NEC, NFPA 70E, NETA, CA MUTCD and Caltrans references
    4. Dangerous conditions
    5. Exceptions to the rule
    6. Common misunderstandings
    7. Points that are easy to overlook

| Topic | Assignments |
|-------|-------------|
| A. Phases and phase numbering | 1, 3, 5 |
| B. Ring diagram and concurrency | 2, 7 |
| C. Plans and Caltrans Standard Plans | 2 |
| D. Pedestrian heads and push buttons | 3, 9, 14 |
| E. Loop detectors and detector designations | 3, 6, 9, 14 |
| F. The Model 332 cabinet | 4 |
| G. PDA, output file, load switches and flash | 8, 11 |
| H. The 210 monitor and diode card | 10 |
| I. Conduit and conductor schedule: signal cable and DLCs | 12, 13 |
| J. Power, street lighting and grounding | 15 |
| K. The controller and signal timing | Module 16 |

---

## Flashcards: Caltrans plan symbols

Picture-front flashcards made from the legend in the 2018 Caltrans Electrical Standard Plans. Each card shows a symbol, and the back says what it is. Most symbols come in pairs, **new** and **existing**, because telling them apart on a plan matters.

| Deck | Cards | What's in it |
|------|-------|--------------|
| [Caltrans legend symbols](flashcards/caltrans_legend_symbols/) | 71 | Signal equipment (heads, ped heads, push buttons, standards, controller), conduit types, flashing beacons, service equipment |
| [Plan abbreviations](flashcards/plan_abbreviations/) | 20 | AB, BC, BP, CB, CC, CF, DH, FA, IS, NS, PEC, PEU, RC, RE, RL, RR, RS, SC, SD, TSP |
| [Standard electroliers](flashcards/standard_electroliers/) | 22 | Types 15, 15D, 21, 21D, 30, 31, 32, new and existing |
| [Miscellaneous electroliers](flashcards/misc_electroliers/) | 8 | Luminaire on wood pole, non-standard and city electroliers, future foundation |
| [Soffit and wall-mounted luminaires](flashcards/soffit_luminaires/) | 5 | Pendant, flush-mounted and wall-mounted luminaires, existing to remain or be modified |

Each deck folder has the symbol images plus the cards in two formats:

- **`.json`**: front, back, notes and tags for each card, for importing into a flashcard app such as Anki.
- **`.org`**: Emacs org-mode with `:drill:` tags, for use with org-drill.

---

## Tips

- **Phase a head by the traffic it faces, not the corner it stands on.** A far-side head on the NE corner serves northbound traffic.
- **A ped phase takes the number of the parallel through phase,** not the street being crossed.
- **On the diode card, a diode means "conflict".** Remove a diode only for a pair that may run together.
- **Only mark what is on the print.** Write down any assumption you make on the sheet.
- **Check code values against your edition.** NEC, CA MUTCD and Caltrans spec numbers change between editions.

---

## Folder layout

```
elect_280_traffic_signal_systems_1/
├── README.md                      (this page)
├── elect_280_cheat_sheet.pdf      (7-page overview)
├── elect_280_cheat_sheet.md       (same content, readable on GitHub)
├── elect_280_study_guide.pdf      (17-page guide, topic by topic)
├── elect_280_study_guide.md       (same content, readable on GitHub)
└── flashcards/
    ├── caltrans_legend_symbols/   (71 cards)
    ├── plan_abbreviations/        (20 cards)
    ├── standard_electroliers/     (22 cards)
    ├── misc_electroliers/         (8 cards)
    └── soffit_luminaires/         (5 cards)
```
