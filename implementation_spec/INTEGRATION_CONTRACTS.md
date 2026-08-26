# Integration Contracts

This document defines ownership and handoff between major systems.

## Canonical ownership
- CharacterSystem owns base character state, loadout references, and derived-stat recomputation.
- EffectSystem owns active effects and lifecycle transitions.
- CombatSystem owns turn order, action resolution, intent, and encounter-local terminal checks.
- EncounterSystem owns encounter lifecycle and maps combat/non-combat outcomes into encounter outcomes.
- ExplorationSystem owns region access, map instances, discovery, and encounter entry.
- EconomySystem owns inventory quantities, currency, resource transactions, and atomic cost/reward operations.
- BuildingSystem owns building lifecycle, modules, processes, and exposed capabilities.
- CommunitySystem owns member lifecycle, aptitude records, assignments, and assignment outputs.
- ProgressionSystem owns milestone flags, gate evaluation, and unlock state.
- QuestSystem owns quest state machines and branch outcomes.
- FeedbackSystem derives global and local direction presentation from configured facts; it does not overwrite canonical narrative/progression state.

## Required handoffs
Exploration -> Encounter: create instance with region context, seed, modifiers, and entry requirements.
Encounter -> Combat: create combat only when the selected interaction mode requires it.
Encounter -> Economy: grant encounter rewards through atomic reward transactions.
Quest -> Progression: emit state changes and unlock requests; Progression validates gates.
Building -> Economy: all costs and outputs use Economy transactions.
Assignment -> Community: completion updates assignment state; experience updates are permanent canonical facts.
Equipment -> Character/Effect: equipment grants references; removal immediately invalidates solely granted effects.
Progression -> Exploration/Building/Content: unlock events update availability without duplicating milestone logic.

## Transaction rule
A cross-system operation must either:
1. complete all canonical mutations; or
2. fail without partial canonical mutation.

Event publication occurs after the corresponding canonical transaction commits, except explicitly declared interrupt events.

## Save/load boundary
Persist canonical facts, IDs, lifecycle states, active effects, assignment/process instances, region/quest/progression state, random state where needed, and content version references.

On load:
1. validate content references;
2. restore canonical state;
3. migrate versioned content/state if necessary;
4. recompute all derived state;
5. rebuild transient caches/subscriptions;
6. run integrity validation before exposing gameplay.