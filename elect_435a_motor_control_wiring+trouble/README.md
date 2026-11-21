# ELECT 435A — Motor Control Wiring and Troubleshooting

Wiring diagrams and troubleshooting notes for the ELECT 435A motor control labs.

[← Back to all classes](../README.md)

---

## Labs

### Lab 2 — Start/Stop/Jog

- **[Wiring Diagrams](https://webnrrd2k.github.io/lbcc-electrical-study-materials/elect_435a_motor_control_wiring%2Btrouble/labs/lab_2_startstopjog/wiring-diagrams.html)**: the physical layout of the panel and the lab ladder diagram, with a wire list and problems to check. ([text-only version](labs/lab_2_startstopjog/wiring-diagrams-text-only.md))

### Lab 3 — Forward/Reverse Controls

- **[Wiring Diagrams](https://webnrrd2k.github.io/lbcc-electrical-study-materials/elect_435a_motor_control_wiring%2Btrouble/labs/lab_3_forwardreverse_controls/wiring_diagrams/wiring-diagrams.html)**: the physical layout of the panel, the lab ladder diagram, a wire list, a build order with quick meter checks after each stage, and things to check.
    + Wire labels: [HTML](https://webnrrd2k.github.io/lbcc-electrical-study-materials/elect_435a_motor_control_wiring%2Btrouble/labs/lab_3_forwardreverse_controls/wiring_diagrams/wire-labels.html) or [CSV](https://webnrrd2k.github.io/lbcc-electrical-study-materials/elect_435a_motor_control_wiring%2Btrouble/labs/lab_3_forwardreverse_controls/wiring_diagrams/wire-labels.csv)
    + Tasks to complete: [Emacs org-mode](https://webnrrd2k.github.io/lbcc-electrical-study-materials/elect_435a_motor_control_wiring%2Btrouble/labs/lab_3_forwardreverse_controls/lab3-tasks.org) or [plain text](https://webnrrd2k.github.io/lbcc-electrical-study-materials/elect_435a_motor_control_wiring%2Btrouble/labs/lab_3_forwardreverse_controls/lab3-tasks.txt). The task-by-task checklist: 11 milestones (M0–M10), sub-milestones and checkboxes, all in order. Same content in both; the .txt opens in any text editor.

---

## Flashcards

- **[Motor Control Basics](flashcards/)** (53 cards): components, terminal numbers (A1/A2, 13-14, 95-96...), ladder logic, seal-in and interlocking, NFPA 79 wire colors, and testing and troubleshooting. Study them on the page, on the [flashcard study page](https://webnrrd2k.github.io/lbcc-electrical-study-materials/flashcards/?deck=e435a-motor-control), or download them for Anki, Quizlet or Emacs.

---

## Folder layout

```
elect_435a_motor_control_wiring+trouble/
├── README.md                          (this page)
├── flashcards/                        (53 cards: README, .json, .apkg, Quizlet .txt, .org)
└── labs/
    ├── lab_2_startstopjog/
    │   ├── README.md
    │   ├── wiring-diagrams.html       (the diagrams; opens as a web page)
    │   └── wiring-diagrams-text-only.md
    └── lab_3_forwardreverse_controls/
        ├── lab3-tasks.org             (task checklist, Emacs org-mode)
        ├── lab3-tasks.txt             (same checklist, plain text)
        └── wiring_diagrams/
            ├── wiring-diagrams.html   (diagrams, wire list, build order)
            ├── wire-labels.html / .csv
            └── build_diagrams.py      (generates the pages above)
```
