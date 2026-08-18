# Translated Content Index

These files are the implementation-facing content layer derived from repository source material.

- `characters.md` — character roster and role contracts.
- `enemies.md` — enemy roster, archetypes, tiers, encounter roles, and neutral affinity IDs.
- `items.md` — equipment and item mechanics separated from display terminology.
- `skills.md` — skill roster and functional effects.
- `protagonist.md` — protagonist attributes, state layers, counters, and presentation boundaries.
- `mechanics.md` — village and persistent-progression mechanics supported by source.
- `world.md` — neutral world premise and narrative invariants.

## Consumption rule

An implementation model should use these files together with the root translated design documents. It should not need to inspect the original CSV, HTML, image, or theme-specific source files to implement the gameplay contracts defined here.

## Incomplete data rule

If a source leaves a statistic, quest, action list, formula, unlock condition, or other content undefined, this translated layer must preserve that absence. Implementation defaults may be introduced only when explicitly marked as a design suggestion or later promoted to canon.
