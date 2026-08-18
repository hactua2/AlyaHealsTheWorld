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
- replace theme-specific secondary traits with neutral combat/build traits based on actual mechanical effects;
- preserve active effects, equipment passives, skill passives, persistent afflictions, preference profiles, usage/experience counters, multipliers where mechanically meaningful, and history statistics;
- move outfits entirely to the presentation layer as `AppearanceState`.

**Confidence:** High for existence of these data layers; medium for final neutral taxonomy.

## Audit findings so far

1. The source material already contains a useful separation between entity identity and behavior, even though the data is not yet normalized.
2. The strongest hidden implementation dependency is the second combat-resolution channel. Enemy weaknesses and skill metadata must be audited together before final neutral terminology is chosen.
3. Character appearance states are suitable for a fully decoupled presentation-binding system.
4. The source contains systems not yet sufficiently detailed to implement safely. These should be marked `NEEDS DECISION` rather than invented during translation.

## Next audit targets

1. `Ayla heals the World - Skills.csv`
2. `Ayla heals the World - Items.csv`
3. HTML representations and their relationship to CSV data
4. visual asset directories as role/presentation references only
5. existing `Design/` documentation and current game implementation

## Translation rule

The translated layer records what a source element **does for the game**. It must not require an implementation model to know the original theme-specific framing in order to reproduce that behavior.
