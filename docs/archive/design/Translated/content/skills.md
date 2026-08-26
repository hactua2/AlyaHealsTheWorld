# Translated Skill Content

## Purpose

This document translates the concrete skill roster into implementation-facing behavior. It preserves tier, activation type, targeting, prerequisites, and gameplay effects while replacing presentation-dependent action names and body/context metadata with neutral skill identities.

Source-specific labels are not required by the implementation model.

## Canonical combat vocabulary

- `HealthDamage`: conventional damage.
- `MoralDamage`: damage to the second combat resource.
- `MoralOverfill`: exceeding the normal Moral pressure threshold.
- `SurrenderFinisher`: immediately resolves an eligible target into surrender.
- `Buff` / `Debuff`: persistent or timed stat/state modification.
- `AoE`: affects all valid targets.

## Secondary attribute gates

The source groups many skills under four permanent secondary attributes. Their final neutral display names remain intentionally unresolved until the cross-reference pass is complete. For implementation, preserve four stable internal gates:

- `TraitA`
- `TraitB`
- `TraitC`
- `TraitD`

These IDs may later receive neutral display names without changing save data or skill behavior.

## Translated roster

### Tier 1

| ID | Neutral name | Target | Effect summary |
|---|---|---|---|
| SK_SENSORY_ENHANCEMENT | Sensory Disruption | Enemy | Increases incoming MoralDamage and HealthDamage. |
| SK_RECOVERY_GAMBIT | Recovery Gambit | Enemy, Self | Heals self and increases enemy preference for Moral-channel actions. |
| SK_EVASIVE_ROUTINE | Evasive Routine | Self | Increases dodge chance. |
| SK_ENTICING_WORDS | Distracting Words | Enemy | Deals MoralDamage. |
| SK_HYPNOTIZE | Hypnotic Lock | Enemy | Stuns target and deals MoralDamage over time. |
| SK_REACTIVE_PROVOCATION | Reactive Provocation | Enemy, Self | Deals MoralDamage through a reactive interaction. |
| SK_SENSORY_DEPRIVATION | Sensory Suppression | Enemy | Lowers accuracy, defense, and dodge. |
| SK_DIRECT_STRIKE | Direct Strike | Enemy | Deals MoralDamage and HealthDamage. |
| SK_PROTECTIVE_INSTINCT | Protective Instinct | Ally | Increases probability that allies attract enemy attacks. |
| SK_SUBMISSIVE_STRIKE_01 | Opening | Enemy | Deals MoralDamage. |
| SK_SUBMISSIVE_STRIKE_02 | Yield | Enemy | Deals MoralDamage. |
| SK_SUBMISSIVE_STRIKE_03 | Close Contact | Enemy | Deals MoralDamage. |
| SK_SERVICE | Field Service | Ally | Heals ally. |
| SK_PRECISE_TOUCH | Precise Touch | Enemy | Deals MoralDamage. |
| SK_REPEATED_PRESSURE | Repeated Pressure | Enemy | Applies MoralDamage over time. |
| SK_ESCALATION | Escalation | Enemy | Deals MoralDamage and increases MoralDamage taken when used consecutively. |
| PS_OVERFLOW_RECOVERY | Overflow Recovery | Ally, Self | Heals when MoralOverfill occurs. |
| PS_OTHERWORLDLY_CHARM | Unsettling Presence | Enemy | Increases likelihood of Moral-channel attacks and lowers likelihood of Health-channel attacks. |
| PS_EQUIPMENT_PRESSURE | Equipment Pressure | Enemy | Deals MoralDamage over time while required equipment condition is met. |
| PS_OFFENSIVE_TRAIT | Offensive Trait | Enemy | Increases HealthDamage dealt. |
| PS_DEFENSIVE_TRAIT | Defensive Trait | Self | Reduces HealthDamage received. |
| PS_MORAL_REFLECTION | Moral Reflection | Ally, Enemy | Reflects a portion of received MoralDamage. |

### Tier 2

| ID | Neutral name | Target | Effect summary |
|---|---|---|---|
| SK_ENCOURAGE | Encourage | Ally | Increases allies' attack. |
| SK_GRAND_GESTURE | Grand Gesture | All Enemies | AoE MoralDamage. |
| SK_PURIFICATION | Self Purification | Self | Requires TransformationState; heals self and removes negative statuses. |
| SK_INFLUENCE | Lingering Influence | Enemy | MoralDamage over time and increases enemy preference for Moral-channel attacks. |
| SK_TRANSFORMATION | Arcane Transformation | Ally | Enables TransformationState required by other skills. |
| SK_DOMINATING_MANEUVER | Dominating Maneuver | Enemy, Self | Deals MoralDamage and HealthDamage. |
| SK_MAGICAL_RESTRAINT | Magical Restraint | Enemy, Self | AoE MoralDamage. |
| SK_DEMORALIZE | Demoralize | Enemy | Lowers attack and defense. |
| SK_BITE | Bite | Enemy | Deals MoralDamage and HealthDamage. |
| SK_BIND | Arcane Bind | Enemy | Deals MoralDamage and applies paralysis. |
| SK_PREVENT_OVERFLOW | Pressure Seal | Enemy | Prevents MoralOverfill and causes HealthDamage when the target receives MoralDamage while the meter is filled. |
| SK_TRANSFORMED_ASSAULT | Transformed Assault | Enemy | Requires TransformationState; deals MoralDamage and HealthDamage, with increased MoralDamage as target Health decreases. |
| SK_PRESSURE_01 | Focused Pressure | Enemy | Deals MoralDamage. |
| SK_SUMMONED_PRESSURE | Summoned Pressure | All Enemies | MoralDamage to all enemies; damage increases as enemy count decreases. |
| SK_SURRENDER_FINISHER | Threshold Break | Enemy | If target is within the configured Moral threshold, resolves the target into Surrender. |
| PS_REWARD_INSIGHT | Reward Insight | Self | Increases rewards found after victory. |
| PS_ALLY_INSPIRATION | Ally Inspiration | Ally | Increases allies' attack. |
| PS_MORAL_MASTERY | Moral Mastery | Self | Increases Moral-channel accuracy and damage. |
| PS_MORAL_VICTORY_RECOVERY | Victory Recovery | Ally | Heals whenever an enemy is defeated through Moral-channel resolution. |

### Tier 3

| ID | Neutral name | Target | Effect summary |
|---|---|---|---|
| SK_DISRUPTING_REVEAL | Disrupting Reveal | All Enemies, Self | AoE MoralDamage and increased dodge chance. |
| SK_PINK_MIST | Enervating Mist | All Enemies | MoralDamage over time and reduced defenses. |
| SK_TRANSFORMED_STRIKE | Transformed Strike | Enemy | Requires TransformationState; deals MoralDamage. |
| SK_TRANSFORMED_STUN | Transformed Lock | Enemy | Requires TransformationState; deals MoralDamage and stuns. |
| SK_STOMP | Crushing Blow | Enemy | Deals MoralDamage and HealthDamage; HealthDamage scales with target Moral pressure. |
| SK_OTHERWORLDLY_SUMMON | Otherworldly Summon | Ally, Enemy, Self | AoE MoralDamage and HealthDamage; creates broad threat/aggro. Damage increases as enemy count decreases. |
| SK_ENSLAVE_TRANSLATED | Command Break | Enemy | Finisher-style action that applies MoralDamage, HealthDamage, and a control debuff. In translated design, successful terminal resolution must map to Surrender rather than automatic ownership or recruitment. |
| SK_AREA_PRESSURE | Area Pressure | All Enemies | AoE MoralDamage. |
| SK_HIGH_RISK_FINISHER | All-or-Nothing Break | Enemy Group, Self | If every enemy is below the Moral threshold, resolves combat; otherwise the user receives heavy MoralDamage. |
| SK_DEEP_PRESSURE | Deep Pressure | Enemy | Deals MoralDamage. |
| SK_WORSHIP_TRANSLATED | Reverent Pressure | All Enemies | AoE MoralDamage and increases likelihood of Moral-channel attacks. |
| PS_AFTERSHOCK | Moral Aftershock | All Enemies | Deals AoE MoralDamage when the user's MoralOverfill occurs. |
| PS_DIVINE_HEALTH | Divine Resilience | Ally | Grants debuff immunity; healing allies also removes debuffs. |

## Required data fields

Each translated skill should support:

```text
skillId
DisplayNameKey
ActivationType
Tier
DamageChannels[]
TargetRule
Effects[]
Prerequisites[]
RequiredTraits[]
EquipmentConditions[]
ScalingRules[]
```

## Translation notes

1. Source `Element` values `Physical` and `Magical` are directly preserved as implementation tags.
2. Source action/context categories are not required as literal player-facing categories. Where mechanically useful, they should become neutral action tags or prerequisites.
3. Source body/context metadata is presentation data unless it demonstrably gates an effect; when it gates an effect, represent the gate through an abstract state, equipment condition, or action tag.
4. `TransformationState` is preserved because multiple skills explicitly depend on an enabling state.
5. Surrender finishers are compatible with the canonical rule: Moral defeat leads to Surrender, followed by post-combat dialogue that may offer recruitment.

## NEEDS DECISION

**ND-06 — Final neutral names for the four permanent secondary attributes.**

The source establishes four persistent attribute-gated families, but their literal names are presentation/theme-specific. The implementation can safely use stable internal IDs now; a canonical neutral display taxonomy still requires a project-owner decision or stronger evidence from other sources.
