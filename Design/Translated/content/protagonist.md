# Translated Protagonist Content

## Core identity

The protagonist record is data-driven and separates gameplay state from presentation state.

## Primary attributes

The source defines four permanent primary attributes:

| ID | Source mechanical responsibilities |
|---|---|
| Body | Health damage inflicted; damage resistance; Health pool |
| Agility | Dodging; accuracy; initiative |
| Soul | Magic attack; Moral resistance |
| Charm | Moral damage; Moral accuracy; enemy likelihood of using Moral-oriented attacks |

These names are retained because they are already usable as neutral fantasy terminology.

## Permanent secondary attributes

The source defines four permanent secondary axes. Their internal IDs remain temporary:

| ID | Mechanical responsibilities |
|---|---|
| TraitA | Health damage inflicted; accuracy |
| TraitB | Moral resistance; damage resistance; debuff resistance |
| TraitC | Enemy likelihood of using Moral-oriented attacks; Moral damage; buff empowerment |
| TraitD | Moral damage; Moral accuracy; resistance to Moral-oriented attacks |

The IDs may later receive display names without changing save keys or mechanical references.

## Appearance states

The source contains multiple protagonist appearances. They are translated as presentation-only `AppearanceState` records.

Canonical implementation requirements:

- each appearance has a stable ID;
- appearance bindings may include portrait, model/sprite, animation, UI skin, and other presentation assets;
- obtaining/unlocking an appearance may be data-driven;
- changing appearance must not implicitly alter gameplay unless an explicit gameplay modifier record is attached.

The source does not provide supported unlock conditions or mechanics for the individual appearances.

## Secondary character sheet

The following data layers are preserved:

### Effect layers

- Active effects
- Equipment passives
- Skill passives
- Persistent afflictions/curses

Each effect should have a stable source ID, lifecycle, stacking rule, and modifier payload when implemented.

### Preference profile

The source contains preference categories for:

- Moral/combat interaction preference
- enemy preference
- position preference
- skill preference

Neutral implementation model:

`PreferenceProfile { preferredInteractionTags, preferredEnemyTags, preferredPositions, preferredSkillTags }`

The source does not define numerical values or exact AI behavior for these preferences.

### Experience and usage counters

The source tracks several theme-specific experience counters plus a generic count. Translation preserves the architectural requirement for extensible counters:

`ExperienceCounter { id, value, metadata }`

No new counter names or progression effects are invented here.

### Contextual multipliers

The source defines multiple context-specific multipliers. Translation preserves a generic system:

`ContextMultiplier { contextId, multiplier, modifierSource }`

The original context labels are presentation/theme-specific and are not required for the neutral implementation layer.

### History statistics

Preserve:

- enemies defeated;
- strongest enemy defeated;
- times defeated.

These are gameplay/history records and can feed achievements, progression, narrative conditions, or statistics UI.

## Canonical combat integration

The protagonist participates in the global two-channel resolution model:

- Health reduction -> conventional defeat;
- Moral reduction -> Surrender when applicable under combat rules.

Stat names and display labels must remain decoupled from underlying stable IDs.
