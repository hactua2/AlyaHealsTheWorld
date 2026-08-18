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

Preserves sixteen character IDs and roles including ally, neutral, quest giver, quest target, and quest-gated ally.

**Classification:** NI + GI + HY.

**Translation:** `content/characters.md`.

### Enemy roster CSV

**Path:** `Ayla heals the World - Enemies.csv`

Preserves enemy IDs, archetypes/factions, tiers, encounter roles, and weakness categories.

**Classification:** GI + TR.

**Translation:** `content/enemies.md`.

### Skills CSV

**Path:** `Ayla heals the World - Skills.csv`

Preserves skill type, affinity/channel, target rule, tier, special effects, requirements, and interactions with Health and Moral.

**Classification:** GI + TR + HY.

**Translation:** `content/skills.md`.

### Items CSV

**Path:** `Ayla heals the World - Items.csv`

Preserves stable item identity, stat modifiers, secondary-attribute modifiers, persistent restrictions, usage-based evolution, and conditional effects.

**Classification:** GI + TR + HY.

**Translation:** `content/items.md`.

### Main character CSV

**Path:** `Ayla heals the World - MainCharacter - Ayla.csv`

Preserves primary attributes, four permanent secondary attributes, effect layers, preferences, extensible counters, contextual multipliers, history statistics, and appearance-state architecture.

**Classification:** GI + TR + HY + PT.

**Translation:** `content/protagonist.md`.

### Mechanics CSV

**Path:** `Ayla heals the World - Mechanics.csv`

Preserves integration/rehabilitation, resource production, equipment transmutation, expedition dispatch, and persistent affliction progression.

**Classification:** GI + TR.

**Translation:** `content/mechanics.md`.

### HTML exports

**Paths:** `HTML/Characters.html`, `Enemies.html`, `Items.html`, `MainCharacter - Ayla.html`, `Mechanics.html`, `Skills.html`.

**Finding:** These are large spreadsheet-style exports corresponding to the planning tables. The mechanics HTML confirms the same concrete mechanics rows as the CSV, including integration, production, transmutation, expedition dispatch, and progression, rather than introducing a separate canonical ruleset.

**Classification:** HY, primarily source presentation/verification.

**Translation treatment:** HTML is not required by the implementation layer after extraction.

### Visual asset directories

**Paths:** `Characters/`, `Enemies/`, `Items/`, `MainCharacter/`.

**Finding:** Asset files are image-oriented and filenames are largely opaque identifiers. They provide presentation references but do not reliably encode gameplay contracts in filenames.

**Classification:** PT, with possible HY role-reference value.

**Translation treatment:** no source asset path is required by gameplay logic. Future presentation bindings should map stable content IDs to replaceable asset references.

### Character description / scenario source

**Path:** `CharDesc`

**Observed design information:** a fantasy-world premise, magical creatures, unexplored wilds, and an explicit source-specific philosophy that conflicts—including combat—can be resolved through an alternative relationship/intimacy route.

**Classification:** NI + TR + PT.

**Translation:** `content/world.md` preserves the fantasy setting, wild exploration, community growth, and alternative conflict-resolution structure while separating source-specific presentation and adult-theme details.

## Canonical decisions from project owner

### ND-01 — Second combat meter

**Decision:** The neutral canonical name is **Moral**.

**Implementation rule:** Combatants have at least two independent resolution resources: `Health` and `Moral`. Health represents conventional combat endurance. Moral represents willingness or capacity to continue opposition.

**Status:** CANON.

### ND-02 — Secondary attributes

**Decision:** The four translated secondary axes remain **permanent character attributes**.

**Implementation rule:** The translation layer preserves four persistent secondary attributes. Their neutral names remain configurable/temporary while stable IDs are used internally.

**Status:** CANON.

### ND-03 — Moral resolution outcome

**Decision:** Reaching the Moral defeat condition causes **Surrender**.

**Implementation rule:** Surrender enters a post-combat dialogue or narrative event that determines recruitment or another authored outcome. Surrender is not automatic recruitment.

**Status:** CANON.

### ND-04 — Equipment slots

**Decision:** Slot naming is presentation/configuration data and may change without affecting mechanics.

**Implementation rule:** Equipment uses stable internal IDs and configurable display names. Code, saves, restrictions, and compatibility depend on IDs/tags.

**Status:** CANON.

### ND-05 — Village mechanical detail

**Decision:** Detailed numerical and operational rules will be decided later.

**Implementation rule:** Translate only behavior directly supported by source material. Do not invent canonical costs, durations, capacities, probabilities, or formulas.

**Status:** CANON.

## Explicit suggestion policy

When translated documentation discusses an implementation option not established by source material or a project-owner decision, it must be marked exactly as:

> **DESIGN SUGGESTION — NOT CANON**

Suggestions must be separated from canonical requirements and never phrased as existing game rules.

## Current village-system suggestions

### Integration/Rehabilitation

> **DESIGN SUGGESTION — NOT CANON:** Use staged integration rather than instant conversion, with future capacity/time/supervision parameters represented as data.

### Resource Production

> **DESIGN SUGGESTION — NOT CANON:** Give each production assignment explicit input, output, interval, and capacity fields for future balancing.

### Equipment Transmutation

> **DESIGN SUGGESTION — NOT CANON:** Define recipes as data records with required resources, output pools, and optional risk parameters.

### Expedition Dispatch

> **DESIGN SUGGESTION — NOT CANON:** Resolve expeditions from party capability, assigned roles, risk tier, and duration; exact formulas remain undecided.

### Persistent Character Progression

> **DESIGN SUGGESTION — NOT CANON:** Model persistent states as data-driven records with explicit acquisition, modification, progression, and removal rules.

## Audit conclusions

1. CSV and corresponding HTML files describe the same planning layer; HTML primarily serves as verification/presentation and does not need to be exposed to the implementation model.
2. Visual assets can be fully decoupled because gameplay contracts do not depend on their filenames or paths.
3. The source supports a coherent fantasy RPG premise with exploration, wild regions, conventional and alternative conflict resolution, recruitment, and community growth.
4. Several concrete content fields remain intentionally empty or underspecified. The translated layer preserves those gaps rather than inventing canonical content.
5. No additional `NEEDS DECISION` was required during this audit pass.

## Translation rule

The translated layer records what a source element **does for the game**. It must not require an implementation model to know the original theme-specific framing in order to reproduce that behavior.
