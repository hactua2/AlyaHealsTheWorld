# Explicit Implementation Contracts

This document defines cross-system contracts that the destination LLM must preserve when implementing or extending the Unity project. These contracts supplement the implementation playbook and are canonical unless explicitly marked otherwise.

## 1. Skill Resolution Pipeline

Each skill execution follows this logical order:

```text
Select Skill
-> Validate user
-> Validate target(s)
-> Pay costs
-> Apply gameplay effects
-> Request/play the skill cut-in presentation
-> Resolve reactions and passives
-> Evaluate Health defeat / Moral surrender
-> Continue or end combat according to the resolved state
```

The cut-in is intentionally placed immediately after gameplay effects.

### Rule

The cut-in contains no gameplay logic and cannot alter skill results, targets, costs, damage, Moral changes, reactions, passives, defeat, or surrender.

If presentation fails, is missing, or is replaced, gameplay continues normally.

## 2. Skill Cut-In Contract

Every skill has an associated cut-in presentation reference.

Minimum conceptual contract:

```text
SkillDefinition
- id
- gameplay data
- cutInId

CutInDefinition
- id
- presentationBindingId
- displayDuration
```

A cut-in is a brief image shown when its skill is used. It is presentation-only feedback, not a cinematic subsystem.

### Required behavior

- Each skill resolves its `cutInId` through presentation data.
- Missing cut-in data uses a graceful fallback or skips presentation.
- A cut-in must not block gameplay indefinitely.
- Replacing a cut-in image must not alter gameplay state.
- The same skill execution must produce equivalent gameplay results with normal, replaced, or missing cut-in assets.

## 3. Source of Truth for Stats and Modifiers

Base definitions and runtime state must never be conflated.

The derived-stat pipeline is:

```text
Character Definition / Base Stats
+ Permanent Attributes
+ Equipment Modifiers
+ Persistent Effects
+ Skill Passives
+ Active Buffs/Debuffs
+ Contextual Modifiers
= Derived Runtime Stats
```

### Rules

- Base definitions are not mutated by temporary combat effects.
- Runtime modifiers are represented by explicit modifier/effect records with source IDs.
- Removing a modifier source removes only the contribution attributable to that source.
- Combat calculations consume derived values or a documented combat snapshot, not arbitrary cached display values.
- UI reads gameplay state but is not the source of truth.

## 4. Effect Lifecycle and Stacking

### Turn timing

For effects affecting a combatant:

1. At the beginning of the affected character's turn, process that character's applicable effects.
2. Decrement each effect's duration immediately.
3. Expire/remove effects whose duration is exhausted according to their lifecycle.

### Stacking rules

- Effects with different identities/stacks are computed in the order in which they were inflicted.
- For equivalent stacks/effects, only the strongest effect remains active.
- The implementation must define strength comparison as explicit effect data or a deterministic comparison rule; it must not depend on display names.

### Equipment lifecycle

Removing equipment immediately removes effects contributed by that equipment.

### Scope

This contract governs runtime lifecycle. Save-persistence policy is not expanded here beyond existing project implementation and should not be redesigned solely for this document.

## 5. Targeting Contract

Skills use an explicit `TargetRule`; skill names or presentation must never determine targeting behavior.

Minimum supported target rules:

```text
Self
SingleEnemy
AllEnemies
SingleAlly
AllAllies
RandomValidTarget
```

The implementation may support additional rules when represented explicitly as data.

### Validation

Before costs or effects are applied, the combat system validates that the selected targets satisfy the declared target rule.

## 6. RNG and Deterministic Testing Contract

Randomness must be accessed through a centralized, replaceable random provider or equivalent abstraction.

This covers, where applicable:

- accuracy;
- dodge;
- chance-based effects;
- random targeting;
- encounter selection;
- other random gameplay outcomes.

### Requirements

- Production gameplay may use the normal random implementation.
- Tests and verification fixtures can supply deterministic values or seeds.
- A verification fixture must be able to reproduce the same result without relying on uncontrolled randomness.

## 7. Reward Contract

Encounter outcomes resolve through a common result structure rather than each combat/narrative path granting rewards through bespoke code.

Conceptual structure:

```text
EncounterResolutionResult
- outcomeId
- rewards
- narrativeConsequences
- recruitmentResult
- stateChanges
```

Health defeat, Moral surrender, quest completion, and other encounter outcomes may populate different combinations of these fields.

Rewards and consequences are resolved from explicit encounter/resolution data.

## 8. Common Narrative Consequence Language

Dialogue, quests, surrender resolutions, encounter resolutions, and other authored events use a common consequence abstraction.

Minimum consequence operations:

```text
SetFlag
AdvanceQuest
CompleteQuest
GrantItem
RemoveItem
RecruitCharacter
ChangeRelationship
UnlockRegion
StartEncounter
TriggerEffectHook
```

Additional consequence types may be added as stable data-driven operations.

### Rule

Narrative content should request consequences through this common language rather than embedding one-off gameplay mutations inside dialogue presentation code.

## 9. Character Lifecycle Contract

A character can participate in multiple systems over time. Character availability/state must therefore be represented explicitly rather than inferred from UI or scene presence.

The lifecycle model must support, where applicable:

```text
Encountered
Resolved
Recruited
Available
Assigned
Unavailable
```

Not every character must traverse every state.

### Rules

- A character's role in one system does not require a different content ID in another system.
- Recruitment is an explicit state transition caused by a consequence.
- Assignment changes operational/base availability but does not silently alter identity.
- Additional states may be introduced through explicit data/state contracts.

## 10. Encounter Contract

An encounter is the explicit bridge between exploration, combat, narrative resolution, and rewards.

Conceptual structure:

```text
EncounterDefinition
- id
- participants
- encounterRole
- entryConditions
- HealthDefeatResolution
- SurrenderResolution
- rewards
- narrativeHooks
```

### Canonical resolution behavior

```text
Health defeat
-> configured HealthDefeatResolution

Moral defeat
-> Surrender
-> configured SurrenderResolution / PostCombatResolution
```

All enemies support the Moral route.

Surrender does not imply recruitment; the configured resolution decides consequences.

## 11. Existing Implementation Preservation Rule

Some systems, including the combat turn structure and the conventional post-Health-defeat disappearance behavior, may already exist in the Unity implementation.

The destination LLM must inspect existing code before replacing such systems. Where existing behavior satisfies translated canon, preserve and integrate it rather than rebuilding it unnecessarily.

The primary implementation uncertainty identified for review is whether the Moral mechanic and associated skills are fully integrated into the existing combat implementation.

## 12. Verification Requirements for These Contracts

The destination LLM must verify at minimum:

### Skill + cut-in

- Execute a skill with a valid target.
- Confirm gameplay effects resolve before the cut-in request.
- Confirm the cut-in image appears briefly.
- Repeat with a replaced binding and with a missing binding.
- Confirm identical gameplay outcomes and no deadlock.

### Derived stats

- Record base/derived values.
- Add equipment/effects.
- Verify derived values change without mutating base definitions.
- Remove the source and verify the corresponding contribution disappears.

### Effects

- Apply effects of different identities in known order.
- Verify processing order follows infliction order.
- Apply equivalent effects of different strengths.
- Verify only the strongest remains.
- Advance to the affected character's turn and verify immediate duration decrement and expiration behavior.
- Remove equipment and verify its effects disappear immediately.

### Targeting

Verify each minimum target rule accepts valid targets and rejects invalid ones before effects are applied.

### RNG

Run the same deterministic fixture repeatedly and verify identical outcomes.

### Rewards and consequences

Resolve Health and Moral encounters with distinct configured results and verify rewards/consequences are generated through the common result/consequence contracts.

### Character lifecycle

Verify explicit transitions for at least encountered -> resolved and resolved -> recruited -> available -> assigned using a deterministic fixture.

### Encounter

Verify one encounter through Health and one through Moral, confirming their configured resolution contracts are distinct and data-driven.
