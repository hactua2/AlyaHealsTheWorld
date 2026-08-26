# Implementation Rules

## Separation of concerns

Implementation must maintain separate layers for:

1. design definitions;
2. runtime state;
3. gameplay logic;
4. narrative/event resolution;
5. presentation bindings.

## Hard constraints

- Do not hardcode behavior from a visual asset name.
- Do not use display names as persistent identifiers.
- Do not derive equipment behavior from slot display text.
- Do not make recruitment depend on a portrait, animation, or presentation asset.
- Do not make combat effects depend on theme-specific vocabulary.
- Do not embed presentation-specific rules inside combat, progression, save, or quest systems.

## Stable IDs

Characters, enemies, skills, items, quests, regions, structures, slots, effects, and presentation bindings must use stable IDs suitable for save data.

## Data-driven content

Adding a normal character, enemy, skill, item, quest, region, or presentation replacement should primarily require new or edited data rather than modification of core logic.

## Save/load

Save data must reference stable IDs and runtime values. Presentation changes must not invalidate saves.

## Placeholder-first implementation

The implementation model may use neutral placeholder art, icons, sounds, and labels where final presentation is unavailable. Functional validation precedes presentation polish.

## Acceptance rule

A feature is incomplete if replacing all presentation bindings can change its gameplay behavior, save compatibility, or progression logic.
