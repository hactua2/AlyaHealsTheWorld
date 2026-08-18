# Source Audit

## Scope

This audit inventories source material that contributes concrete game-design intent and classifies how that information should enter the translated implementation layer.

## Classification

- **GI — Gameplay Invariant:** implementation-relevant behavior preserved directly or with minimal renaming.
- **NI — Narrative Invariant:** story role or relationship preserved independently of presentation.
- **PT — Presentation Only:** visual/audio/cosmetic information; excluded from implementation-facing design.
- **TR — Translation Required:** theme-specific terminology that contains gameplay information and must be re-expressed functionally.
- **HY — Hybrid:** mixed source; split into independent gameplay and presentation concepts.

## Audited sources

### Character roster CSV
**Path:** `Ayla heals the World - Characters.csv`

Sixteen character IDs with roles including ally, neutral, quest giver, quest target, and allies gated by quest completion.

**Classification:** NI + GI + PT/HY.

**Translated intent:** preserve identity and quest relationships, modeled through `CharacterRole`, `AvailabilityCondition`, `QuestRole`, and `RecruitmentState`.

**Confidence:** High for roster/role data; low for combat statistics because those columns are empty.

### Enemy roster CSV
**Path:** `Ayla heals the World - Enemies.csv`

Enemy IDs, faction/archetype, progression tiers, encounter roles, and weakness categories.

**Classification:** GI + TR.

**Translated intent:** preserve faction/archetype, tier, and encounter role. Weaknesses belong to the combat affinity/channel model and must be translated together with skill metadata.

**Confidence:** High for taxonomy and progression; medium for exact weakness semantics.

### Village mechanics CSV
**Path:** `Ayla heals the World - Mechanics.csv`

Enemy capture/integration through facilities, farming, transmutation using farmed resources, ally expeditions, and persistent character progression.

**Classification:** GI + TR.

**Translated intent:** `Integration/Rehabilitation`, `Resource Production`, `Equipment Transmutation`, `Expedition Dispatch`, and `Persistent Character Progression`.

**Confidence:** High that these are intended systems; medium for detailed rules because the source is sparse.

### Main character CSV
**Path:** `Ayla heals the World - MainCharacter - Ayla.csv`

Multiple appearance states; four primary attributes; four secondary traits; active/passive/persistent effect layers; preferences; experience counters; contextual multipliers; defeat history.

**Classification:** HY + TR + PT.

**Translated intent:** preserve data layers and mechanical consequences while moving appearance states to `AppearanceState` presentation bindings. Secondary traits should not be translated by literal renaming; their mechanical roles must be derived from skills and items.

**Confidence:** High for data-layer existence; medium for final neutral taxonomy.

### Skills CSV
**Path:** `Ayla heals the World - Skills.csv`

The file defines a substantial combat system with columns for activation/type, physical or magical channel, action family, body/context metadata, target, tier, special effects, and descriptions. Across the listed skills, the recurring mechanical behaviors are:

- direct Health damage;
- direct secondary-meter damage;
- damage-over-time on the secondary meter;
- buffs and debuffs;
- healing;
- stun/paralysis and other control effects;
- accuracy, dodge, attack, defense, and resistance modifiers;
- threat/targeting manipulation;
- area-of-effect actions;
- conditional finishers based on a secondary-meter threshold;
- resource-overfill triggers;
- consecutive-use scaling;
- low-enemy-count scaling;
- low-health scaling;
- prerequisite states that unlock follow-up skills;
- passive effects triggered by defeat, equipment, meter state, or combat events.

**Classification:** GI + TR + HY.

**Translated intent:** the implementation requires a general `SkillDefinition` with independent fields for damage channel, delivery/action family, targeting, tier, prerequisites, effects, and triggers. Original presentation/context metadata must not be used as implementation requirements.

**Important finding:** the source supports a genuine dual-resolution combat model rather than a cosmetic secondary meter. Health damage and secondary-meter damage have separate accuracy/resistance modifiers, threshold finishers, event triggers, and enemy weakness mappings.

**Confidence:** High for the existence of these mechanics; medium for final names and exact formulas, which are not specified.

### Items CSV
**Path:** `Ayla heals the World - Items.csv`

The file defines equipment by slot, primary-stat modifiers, secondary-trait modifiers, persistent special effects, evolution behavior, removal restrictions, and prerequisite/ability gating.

Mechanically reusable patterns include:

- flat stat modification;
- secondary build-trait modification;
- blessed/cursed item evolution over continued use;
- equipment that cannot be removed normally;
- reactive triggers when receiving a damage channel;
- meter-overfill triggers;
- temporary stat scaling based on meter state;
- stat growth after negative effects;
- periodic area effects;
- skill gating or prerequisite requirements.

**Classification:** GI + TR + HY.

**Translated intent:** implement a generic `EquipmentDefinition` and `PersistentEffectDefinition`, including `EvolutionRule`, `RemovalRule`, `TriggerRule`, and optional `AbilityRequirement`. Slot names and item appearance remain presentation/content data rather than core mechanics.

**Confidence:** High for reusable equipment behaviors; medium for the final slot taxonomy because current slot labels mix mechanical location and presentation.

## NEEDS DECISION

### ND-01 — Secondary combat meter: final neutral name
The sources clearly establish a second resolution meter, but do not provide a theme-neutral canonical name. The translated layer can preserve the model as a placeholder such as `Resolve` or `Morale`, but the final implementation term should be chosen before writing canonical content definitions.

**Source-supported facts:** it receives damage, has accuracy/resistance modifiers, can overfill, can trigger passives, can enable threshold finishers, and can define a non-standard combat victory path.

### ND-02 — Primary and secondary stat taxonomy
The source names four primary attributes and four secondary traits, but several secondary traits are theme-dependent labels. Their effects overlap with offensive, defensive, reactive, targeting, and support behavior.

**Decision required:** preserve eight explicit stats with neutral names, or refactor the second group into tags/build traits/modifiers instead of permanent attributes.

### ND-03 — Exact dual-resolution victory semantics
The skill data supports threshold finishers and an alternate resolution path, but does not fully specify what happens when the secondary meter reaches its terminal state: recruitment eligibility, surrender, temporary disablement, or another result.

**Decision required:** canonical outcome model for secondary-meter defeat/resolution.

### ND-04 — Equipment slot taxonomy
Current slots include accessory and location/presentation-derived categories. The source does not establish whether all of these are mechanically distinct inventory slots or primarily presentation groupings.

**Decision required:** final number and identity of gameplay equipment slots.

### ND-05 — Sparse village mechanics
The village CSV establishes system existence but not loops, durations, costs, capacity, failure states, or progression rules.

**Decision required later:** detailed rules for integration, farming, transmutation, expeditions, and persistent progression. These can remain as system shells during the translated specification phase.

## Audit findings

1. The source material already contains a useful separation between entity identity and behavior, even though the data is not normalized.
2. The strongest hidden implementation dependency is the dual-resolution combat model.
3. Skills and items show that the secondary channel is integrated into progression, equipment, passives, enemy weaknesses, and finishers.
4. Appearance states are suitable for a decoupled presentation-binding system.
5. Several fields mix implementation behavior with thematic context; these should be decomposed rather than merely renamed.

## Next audit targets

1. HTML representations and their relationship to CSV data.
2. Visual asset directories as role/presentation references only.
3. Existing `Design/` documentation and current game implementation.
4. Cross-check conflicts between GDD, CSV data, and implemented systems.

## Translation rule

The translated layer records what a source element **does for the game**. It must not require an implementation model to know the original presentation-specific framing in order to reproduce that behavior.
