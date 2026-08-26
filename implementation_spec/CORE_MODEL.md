# Core System Model

## Canonical progression loop
Narrative milestone -> unlocks regions, resources, facilities, capabilities, or content -> exploration, encounters, quests, expeditions -> rewards and discoveries -> resources, items, currency -> buildings, equipment, modifications, assignments -> new capabilities -> next milestone.

No major subsystem should progress independently without feeding another subsystem.

## System boundaries
- Combat resolves encounters and can produce multiple outcome types.
- Exploration creates access to regions, encounters, gathering, discoveries, and quests.
- Economy tracks materials, components, currency, items, and consumption destinations.
- Buildings provide access, stability, conversion, or specialization.
- Community members can be assigned, gain expertise, and create opportunities.
- Progression controls access to future possibility layers.
- Content is data-driven where possible; concrete names and presentation are separate from mechanics.

## Design constraints
Prefer short loops. Avoid mandatory refinement chains, permanent depletion simulation, upkeep chores, universal level scaling, redundant currencies, and duplicate effect lifecycles.

## Primary outcome types
Encounter resolution supports at least: Defeat, Disable, Capture, Yield, Retreat, and ObjectiveComplete. Content can map these neutral identifiers to presentation-specific labels.

## Feedback model
Global trajectory uses a qualitative DirectionState. Local regions expose visible consequence states. Do not expose a deterministic universal completion percentage.