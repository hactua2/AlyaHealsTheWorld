# Source Audit

## Scope

This audit inventories source material that contributes concrete game-design intent and classifies how that information should enter the translated implementation layer.

## Classification

- **GI — Gameplay Invariant:** implementation-relevant behavior preserved directly or with minimal renaming.
- **NI — Narrative Invariant:** story role or relationship preserved independently of presentation.
- **PT — Presentation Only:** visual/audio/cosmetic information; excluded from implementation-facing design.
- **TR — Translation Required:** theme-specific terminology that contains gameplay information and must be re-expressed functionally.
- **HY — Hybrid:** mixed source; split into independent gameplay and presentation concepts.

## Initial audited sources

### Character roster CSV

**Path:** `Ayla heals the World - Characters.csv`

**Observed design information:** sixteen named character IDs with roles including ally, neutral, quest giver, quest target, and allies gated by quest completion.

**Classification:** NI + GI + PT/HY.

**Translated intent:** preserve character identity and quest relationships, but model access as explicit recruitment/availability conditions rather than relying on presentation. Required concepts include `CharacterRole`, `AvailabilityCondition`, `QuestRole`, and `RecruitmentState`.

**Confidence:** High for roster/role data; low for combat statistics because those columns are currently empty.

### Enemy roster CSV

**Path:** `Ayla heals the World - Enemies.csv`

**Observed design information:** enemy IDs, world/faction archetypes, progression tiers, encounter roles, and weakness categories.

**Classification:** GI + TR.

**Translated intent:** preserve faction/archetype, tier, and encounter role. Replace theme-specific weakness terminology with a neutral affinity/channel system after skill data is fully audited.

**Confidence:** High for taxonomy and progression; medium for exact weakness semantics pending cross-reference with skills.

### Village mechanics CSV

**Path:** `Ayla heals the World - Mechanics.csv`

**Observed design information:** enemy capture/integration through facilities, farming, transmutation using farmed resources, dispatching allies on expeditions, and character curse progression.

**Classification:** GI + TR.

**Translated intent:** implement as `Integration/Rehabilitation`, `Resource Production`, `Equipment Transmutation`, `Expedition Dispatch`, and `Persistent Character Progression`. The exact fictional framing of behavior change is not required by the implementation contract.

**Confidence:** High that these are intended systems; medium for detailed rules because the source is sparse.

### Main character CSV

**Path:** `Ayla heals the World - MainCharacter - Ayla.csv`

**Observed design information:** multiple appearance states; four primary attributes; four theme-specific secondary traits; active/passive/curse effect layers; preferences; experience counters; contextual multipliers; defeat history.

**Classification:** HY + TR + PT.

**Translated intent:**

- preserve primary-stat structure after confirming naming;
- preserve four permanent secondary attributes, with neutral names derived from their mechanical effects;
- preserve active effects, equipment passives, skill passives, persistent afflictions, preference profiles, usage/experience counters, multipliers where mechanically meaningful, and history statistics;
- move outfits entirely to the presentation layer as `AppearanceState`.

**Confidence:** High for existence of these data layers; medium for final neutral taxonomy.

### Skills CSV

**Path:** `Ayla heals the World - Skills.csv`

**Observed design information:** skills are grouped by role/type, element or affinity, target rule, tier, special effects, and interactions with both Health and the second combat meter.

**Classification:** GI + TR + HY.

**Translated intent:** preserve skill roles, targeting, tiers, costs, effects, prerequisites, combo conditions, finishers, and interactions with the two combat-resolution channels. Theme-specific descriptions must be translated into functional effects.

**Confidence:** High for the existence of a dual-channel combat model; medium for final affinity naming pending complete cross-reference.

### Items CSV

**Path:** `Ayla heals the World - Items.csv`

**Observed design information:** equipment slots, primary and secondary stat modifiers, blessed/cursed progression states, persistent restrictions, usage-based evolution, and special conditional effects.

**Classification:** GI + TR + HY.

**Translated intent:** preserve all mechanical modifiers and progression behavior. Slot IDs must be stable mechanical identifiers with configurable display names. The appearance or fictional nature of an item must not determine its gameplay behavior.

**Confidence:** High for equipment behavior; medium for exact final slot taxonomy.

## Canonical decisions from project owner

### ND-01 — Second combat meter

**Decision:** The neutral canonical name is **Moral**.

**Implementation rule:** Combatants have at least two independent resolution resources: `Health` and `Moral`. Health represents conventional combat endurance. Moral represents willingness or capacity to continue opposition. Systems may damage, restore, resist, or modify either resource independently.

**Status:** CANON.

### ND-02 — Secondary attributes

**Decision:** The four translated secondary axes remain **permanent character attributes**.

**Implementation rule:** The translation layer must preserve four persistent secondary attributes. Their neutral names will be derived from demonstrated mechanical effects rather than literal source terminology.

**Status:** CANON; neutral naming pending cross-reference.

### ND-03 — Moral resolution outcome

**Decision:** Reaching the Moral defeat condition causes **Surrender**.

**Implementation rule:** A surrendered combatant enters a post-combat resolution state. A dialogue or narrative event then determines whether recruitment is available and whether the player accepts it. Surrender itself is not automatically recruitment.

**Status:** CANON.

### ND-04 — Equipment slots

**Decision:** Slot naming is presentation/configuration data and may change without affecting mechanics.

**Implementation rule:** Equipment uses stable internal slot IDs. Each slot has a configurable display name. Item effects, restrictions, compatibility, saves, and code references must depend on IDs/tags rather than localized or presentation-facing names.

**Status:** CANON.

### ND-05 — Village mechanical detail

**Decision:** Detailed numerical and operational rules will be decided later.

**Implementation rule:** Translate only behavior directly supported by source material. Do not invent canonical costs, durations, capacities, failure probabilities, or progression formulas.

**Status:** CANON.

## Explicit suggestion policy

When the translated documentation needs to discuss an implementation option that is not established by source material or a project-owner decision, it must be marked exactly as:

> **DESIGN SUGGESTION — NOT CANON**

Suggestions must be separated from canonical requirements and must never be phrased as existing game rules.

## Current village-system suggestions

These are not canonical decisions and are provided only as possible future directions.

### Integration/Rehabilitation

> **DESIGN SUGGESTION — NOT CANON:** Use staged integration rather than an instant conversion. A surrendered or captured unit could require facility capacity, time, or assigned supervision before becoming fully available.

### Resource Production

> **DESIGN SUGGESTION — NOT CANON:** Give each production assignment an explicit input, output, interval, and capacity so balancing can later be data-driven.

### Equipment Transmutation

> **DESIGN SUGGESTION — NOT CANON:** Define transmutation recipes as data records containing required resources, output pools, and optional risk parameters rather than hardcoded logic.

### Expedition Dispatch

> **DESIGN SUGGESTION — NOT CANON:** Resolve expeditions from party capability, assigned roles, risk tier, and duration, returning deterministic or weighted outcomes. The exact formula remains undecided.

### Persistent Character Progression

> **DESIGN SUGGESTION — NOT CANON:** Model persistent afflictions and long-term traits as data-driven states with explicit acquisition, modification, and removal rules so the future design can change them without rewriting combat.

## Audit findings so far

1. The source material already contains a useful separation between entity identity and behavior, even though the data is not yet normalized.
2. The strongest hidden implementation dependency is the second combat-resolution channel. Enemy weaknesses and skill metadata must be audited together before final neutral terminology is chosen.
3. Character appearance states are suitable for a fully decoupled presentation-binding system.
4. The source contains systems not yet sufficiently detailed to implement safely. Those systems remain open rather than being silently invented.
5. Canonical decisions and design suggestions are now explicitly separated.

## Next audit targets

1. HTML representations and their relationship to CSV data
2. visual asset directories as role/presentation references only
3. existing `Design/` documentation and current game implementation
4. cross-reference of skill, enemy, item, and main-character terminology

## Translation rule

The translated layer records what a source element **does for the game**. It must not require an implementation model to know the original theme-specific framing in order to reproduce that behavior.
