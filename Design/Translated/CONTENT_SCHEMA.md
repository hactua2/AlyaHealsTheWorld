# Content Schema

## General rule

Every gameplay definition requires a stable internal ID. Display names, descriptions, and presentation bindings are replaceable data.

## CharacterDefinition

- id
- displayNameKey
- roles
- availabilityCondition
- recruitmentState
- primaryAttributes
- secondaryAttributes (four permanent axes)
- skillIds
- equipmentState
- activeEffects
- passiveEffects
- persistentTraits
- preferenceProfile
- historyCounters
- assignmentCapabilities
- aptitudeData
- appearanceStateIds

## EnemyDefinition

- id
- faction/archetype
- tier
- encounterRole
- primaryAttributes
- secondaryAttributes where applicable
- health rules
- moral rules
- affinities/resistances
- skillIds
- surrenderEligibility
- postCombatResolutionId

## SkillDefinition

- id
- displayNameKey
- role/type
- affinity/channel
- targetRule
- tier
- resourceCost
- requirements
- effectList
- conditionalRules
- progressionRules

## EffectDefinition

- id
- trigger
- duration
- stackRule
- target scope
- modifiers
- conditions

## EquipmentDefinition

- id
- displayNameKey
- slotId
- compatibilityTags
- primaryModifiers
- secondaryModifiers
- passiveEffectIds
- persistentRestrictions
- evolutionRule
- presentationBindingId

## QuestDefinition

- id
- regionId
- role in main/optional progression
- prerequisites
- objectives
- involvedEntityIds
- completion conditions
- rewards
- state transitions
- follow-up IDs

## RegionDefinition

- id
- progression order
- entry conditions
- exploration areas
- encounter pools
- main quest chain
- optional quest IDs
- recruitable IDs
- major confrontation IDs
- unlock rewards

## StructureDefinition

- id
- displayNameKey
- unlockCondition
- supportedFunctions
- upgradeStates
- effects
- presentationBindingId

## ExpeditionDefinition

- id
- requirements
- assignedEntities
- destination/risk metadata
- resolution rule reference
- reward pool

## PresentationBinding

- bindingId
- portraitId
- worldSpriteId
- battleSpriteId
- animationSetId
- soundSetId
- uiVariantId

No gameplay rule may require a specific value inside a PresentationBinding.
