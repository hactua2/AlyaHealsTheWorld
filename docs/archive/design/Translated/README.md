# Translated Game Design

This directory contains the neutral implementation-oriented design layer for the game.

## Purpose

The original CSV, HTML, visual assets, and other source materials remain the authoritative historical source for design intent. This directory does not replace or modify them.

Its purpose is to extract and preserve:

- gameplay rules;
- progression systems;
- narrative structure;
- content roles and relationships;
- data contracts;
- implementation requirements;
- acceptance criteria.

Theme-specific presentation, visual identity, and other replaceable presentation details are intentionally separated from implementation-facing specifications.

## Translation principle

Each source concept should be represented as:

`Source material -> design intent -> neutral implementation concept`

The implementation layer must depend on stable IDs, roles, tags, states, data, and behavior rather than on specific visual assets or theme-dependent terminology.

## Planned documents

- `SOURCE_AUDIT.md` — inventory and classification of source materials.
- `GAME_CORE.md` — invariant player fantasy, pillars, and core loop.
- `GAMEPLAY_SYSTEMS.md` — combat, exploration, recruitment, progression, base management, and related rules.
- `CONTENT_SCHEMA.md` — neutral data contracts for characters, enemies, skills, items, quests, structures, and regions.
- `NARRATIVE_STRUCTURE.md` — act and quest structure independent from presentation.
- `IMPLEMENTATION_RULES.md` — architecture, separation of logic and presentation, and implementation constraints.
- `content/` — translated content specifications.
- `translation/` — source-to-neutral terminology and design mappings that are safe to expose to an implementation model.

## Source preservation rule

No source file should be edited merely to make it neutral. Translation is additive: the original material remains intact and the translated layer records the implementation-facing interpretation.
