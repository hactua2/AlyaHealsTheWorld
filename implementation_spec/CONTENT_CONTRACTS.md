# Content Contracts

All content definitions are data-driven and use stable IDs. Presentation data must not be required by core simulation.

## Common fields
Every definition should support: id, version, tags, requirements, metadata, and optional presentationRef.

## Requirement contract
Requirements are declarative predicates evaluated against canonical game state.

Supported logical composition: AllOf, AnyOf, NoneOf, Not.

Atomic predicates may reference milestone flags, unlocked regions, inventory quantities, building state, member aptitude, quest state, encounter state, tags, or custom content predicates registered by the implementation.

## Effect primitive contract
Effects are ordered data entries. Recommended primitives include:
- ModifyMeter
- ModifyResource
- ApplyEffect
- RemoveEffect
- AddStack
- RemoveStack
- ModifyStat
- GrantItem
- ConsumeItem
- ChangeIntent
- ChangeState
- GrantCapability
- SpawnEncounter
- UnlockContent

Custom effects require a stable type ID and deterministic handler.

## Reward contract
A reward pool contains ordered or weighted entries with eligibility requirements, quantity rules, visibility, and duplicate policy.

Visibility = VisibleHint | VisibleExact | Hidden.

Reward generation must record the seed/random state used when reproducibility is required.

## Processing contract
Buildings and assignments may define processes:
processId, inputs, outputs, durationModel, capacity, requirements, completionEvents.

DurationModel is one of Immediate, TurnBased, ExpeditionBased, EncounterBased, RealTimeConfigurable. The chosen model is content-configurable; no system may assume real-time passage.

## Reference integrity
Content references must resolve at validation time. Missing IDs, cyclic upgrade graphs, impossible mandatory requirements, and reward pools with no eligible output are validation errors.