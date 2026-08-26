# Implementation Rules and Invariants

## State ownership
Each value has one canonical owner. Derived values are recalculated from canonical state.

## Deterministic ordering
When multiple effects, stacks, or triggers apply, process them in defined application order unless a system explicitly specifies priority.

## Event-driven integration
Major systems should emit events rather than directly coupling UI, rewards, narrative, and analytics to internal logic.

Recommended event families: CombatEvent, EffectEvent, ResourceEvent, ItemEvent, BuildingEvent, AssignmentEvent, RegionEvent, EncounterEvent, QuestEvent, ProgressionEvent.

## Content abstraction
Mechanics use stable IDs, tags, enums, and data definitions. Presentation text, icons, localization, animation, and narrative framing should be replaceable without changing core logic.

## No speculative systems
Do not implement encumbrance, farming simulation, permanent depletion, extra crafting trees, additional currencies, automatic universal scaling, or parallel status lifecycles unless a concrete content requirement proves the existing architecture insufficient.

## Testing priorities
Test lifecycle boundaries, equipment removal, equivalent-effect replacement, gate visibility, deterministic procedural generation, save/load recalculation, reward sinks, and reassignment without expertise loss.