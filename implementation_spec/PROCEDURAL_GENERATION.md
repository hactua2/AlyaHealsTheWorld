# Procedural Generation

Procedural generation is a major tool for repeatable exploration, gathering maps, and selected quest spaces.

## Generation inputs
regionId, primaryProfile, secondaryInfluence, majorModifiers, ecologyState, progressionTier, encounterPools, resourcePools, authoredConstraints, randomSeed.

## Generation requirements
Generated maps must express the semantic identity of their region. Randomization may change layout, routes, encounters, resources, opportunities, and modifiers, but should not erase authored progression or required quest constraints.

## Authored constraints
Critical narrative beats, guaranteed objectives, accessibility requirements, and hard progression gates override random generation.

## Determinism
A seed should reproduce a map when the same generator version and input configuration are used. Persist seed and generator version for saved instances when reproducibility matters.

## Content profiles
Use profile data and weighted pools instead of hard-coded map-specific logic. Major modifiers should transform an existing profile rather than requiring a completely separate generation pipeline.