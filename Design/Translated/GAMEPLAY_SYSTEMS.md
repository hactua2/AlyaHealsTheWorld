# Gameplay Systems

## Combat

Combat is turn-based and data-driven. A combatant exposes at minimum:

- Health and maximum Health;
- Moral and maximum Moral;
- primary attributes;
- four permanent secondary attributes;
- active effects;
- passive effects;
- skills;
- equipment modifiers;
- targetability and position state where relevant.

### Resolution

A conflict can end through:

- **Health defeat:** the target reaches its Health defeat condition.
- **Moral surrender:** the target reaches its Moral surrender condition and enters Surrender.

Surrender must transition into a post-combat dialogue or event. Recruitment, refusal, release, quest advancement, or another explicitly authored outcome may follow. Surrender must not automatically add the target to the roster.

### Skills

Skills are defined by data including ID, role/type, affinity or channel where applicable, target rule, tier, resource cost, requirements, and effects. Effects may modify Health, Moral, attributes, statuses, targeting, turn flow, or other declared combat state.

The original source contains conditional effects, finishers, persistent modifiers, and progression interactions; these must remain representable without requiring theme-specific terminology.

## Characters and progression

Characters have persistent identity, availability state, roles, attributes, skills, effects, equipment, history, and assignment state.

The translated design preserves:

- primary attributes;
- four permanent secondary attributes;
- active effects;
- equipment passives;
- skill passives;
- persistent afflictions/traits;
- preference or behavior profiles where mechanically meaningful;
- usage/history counters;
- appearance states as presentation data.

## Recruitment

Recruitment may originate from authored quest conditions, narrative events, or post-combat Surrender outcomes. Availability must be represented explicitly and must not depend on a portrait, sprite, or presentation asset.

## Community and base systems

The source establishes the existence of:

- character integration/rehabilitation;
- resource production/farming;
- equipment or resource transmutation;
- expedition dispatch;
- persistent character progression;
- assignment of characters to functions.

Detailed timing, cost, capacity, probability, and balancing rules remain undecided unless separately promoted to canonical design.

## Equipment

Equipment behavior is independent of its display name and visual representation. Slots use stable internal IDs; display names are configurable. Items may modify primary/secondary attributes, apply passive effects, have progression/evolution rules, or impose persistent restrictions.

## Exploration and regions

The translated design preserves a progression loop of exploration, encounter resolution, resource/recruit acquisition, return to base, and expansion into additional regions. Region content must be data-driven and able to expose main quests, optional content, encounters, bosses or major confrontations, recruitables, and base unlocks.

## Suggestions not promoted to canon

### DESIGN SUGGESTION — NOT CANON
Use explicit encounter result objects such as `Victory`, `Surrender`, `Escape`, and `QuestResolution` so downstream systems do not infer outcomes from presentation or enemy names.

### DESIGN SUGGESTION — NOT CANON
Represent party suitability and community-job aptitude as independent values, allowing a character to improve through time spent in a role without requiring natural aptitude to be the only source of competence.
