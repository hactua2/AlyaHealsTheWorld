# Data Model

Use stable IDs and data-driven definitions. Avoid hard-coding content names into system logic.

## Core entities
Character: id, stats, vitality, strain, tags, skills, passives, equipment, effects.
Skill: id, tags, targeting rules, costs, effects, conditions, cooldown, chain rules.
Effect: id, sourceId, targetId, startRule, duration, stacks, strength, tags.
Item: id, category, stackLimit, value, tags, payload.
Equipment: id, slot, modifiers, grantedEffects, grantedSkills, modificationState.
Resource: id, family, acquisitionModes, renewalPolicy, sinks.
Building: id, role, tier, requirements, modules, unlockedCapabilities.
Member: character plus aptitude records, assignment, specialization state.
Region: id, primaryProfile, secondaryProfile, modifiers, unlockRule, encounterPools.
Encounter: id, categories, requirements, outcomeRules, rewardPool.
Quest: id, state machine, requirements, visibleRewardHints, hiddenRewards, outcomes.

## Required enums
ItemCategory = Resource | Component | Consumable | Equipment | Unique
BuildingRole = Access | Stability | Conversion | Specialization
RegionProfile = Settlement | WildGrowth | LivingTerritory | AncientTerritory
EcologyState = Normal | Disturbed | Altered
AptitudeRank is ordered and paired with a qualitative label.

## Persistence rule
Persistent state stores facts and identifiers, not recomputable derived values. Recalculate derived stats from canonical sources when loading or changing equipment/effects.