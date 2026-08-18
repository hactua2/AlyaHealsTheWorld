# Master Implementation Plan

## 00 Project orientation
Inventory the existing project and preserve working architecture.

## 01 Core architecture
Separate design definitions, runtime state, gameplay logic, narrative resolution, and presentation bindings. Use stable IDs.

## 02 Combat foundation
Implement turn-based combat with Health and Moral. Health defeat and Moral Surrender are separate outcomes. Surrender enters post-combat resolution.

## 03 Character progression
Implement primary attributes, four permanent secondary attributes, effects, skills, equipment, history, and assignments with persistent state.

## 04 Recruitment and narrative resolution
Implement quest-gated and surrender-gated availability. Recruitment must be an explicit event outcome.

## 05 Exploration and encounters
Implement data-driven regions, encounters, quests, major confrontations, rewards, and progression.

## 06 Base and assignments
Implement assignment infrastructure and extension points for integration, production, transmutation, and expeditions. Do not hardcode undecided balance rules as canon.

## 07 Content population
Translate audited characters, enemies, skills, items, quests, and regions into neutral implementation data.

## 08 UI and presentation
Implement functional UI with replaceable presentation bindings and placeholders.

## 09 Save/load and validation
Validate stable IDs, persistent runtime state, and save compatibility after presentation replacement.

## 10 Polish
Improve feedback, accessibility, pacing, balancing, and presentation without violating the translated contracts.

## Blocking rule
If a translated document marks a point `NEEDS DECISION`, do not invent a canonical rule. Implement surrounding infrastructure or leave a documented extension point.
