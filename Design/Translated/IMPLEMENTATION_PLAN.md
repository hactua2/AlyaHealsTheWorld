# Destination LLM Implementation Playbook

## 0. Mission

Implement a complete, coherent, playable fantasy RPG using **only the translated design layer as the implementation specification**. The game must function with placeholder or generic presentation and must remain compatible with future replacement of images, UI, audio, animations, names, and other presentation bindings.

The implementation goal is a real playable vertical slice that can grow into the complete game, not a collection of disconnected prototypes.

## 1. Read order and source authority

Before modifying code, read these files in order:

1. `Design/Translated/README.md`
2. `Design/Translated/SOURCE_AUDIT.md`
3. `Design/Translated/GAME_CORE.md`
4. `Design/Translated/GAMEPLAY_SYSTEMS.md`
5. `Design/Translated/CONTENT_SCHEMA.md`
6. `Design/Translated/NARRATIVE_STRUCTURE.md`
7. `Design/Translated/IMPLEMENTATION_RULES.md`
8. `Design/Translated/content/README.md`
9. Every file under `Design/Translated/content/`
10. This file

### Authority rules

- `CANON` decisions in `SOURCE_AUDIT.md` are mandatory.
- `DESIGN SUGGESTION — NOT CANON` is optional guidance, not a required game rule.
- `UNSPECIFIED` means do not silently invent canonical design.
- `EffectHook` content may be implemented as infrastructure with safe no-op behavior when its concrete effect is not yet defined.
- Do not require CSV, HTML, or original asset files to understand or implement gameplay.
- Preserve existing working project architecture where it does not violate translated contracts.

## 2. Global non-negotiable invariants

1. Gameplay data uses stable IDs; display names are never gameplay keys.
2. Definitions are separate from runtime state.
3. Gameplay logic is separate from presentation bindings.
4. Replacing all presentation assets must not alter combat, progression, saves, item compatibility, or content IDs.
5. Equipment slots use stable internal IDs and configurable display names.
6. The four secondary attributes remain permanent attributes using stable temporary IDs `TraitA` through `TraitD` until renamed.
7. Every enemy supports the Moral route.
8. `Moral` defeat always enters `Surrender`.
9. Surrender is not automatically recruitment.
10. `Health` defeat uses encounter-defined `DefeatResolution` data.
11. Recruitment is an explicit narrative/post-combat outcome.
12. Unresolved special effects use generic `EffectHook` infrastructure rather than bespoke hardcoded systems.
13. Do not hardcode future village balance values as canonical rules.
14. A content addition should normally be possible through data plus existing extension points.

## 3. Required execution discipline

For every phase:

1. Inspect the existing implementation relevant to the phase.
2. State the files/components that will change.
3. Make the smallest coherent architectural change.
4. Implement the phase.
5. Compile/run available automated validation.
6. Manually exercise the primary happy path when possible.
7. Record any unsupported design assumption as either `UNSPECIFIED` or an implementation note; do not upgrade it to canon.
8. Do not start broad polish before the phase acceptance criteria pass.

When an existing implementation conflicts with translated canon, translated canon wins. Refactor rather than preserving an incompatible shortcut.

## Phase 00 — Repository orientation and baseline

### Goal
Understand the current project without redesigning it blindly.

### Tasks

- Inventory engine/framework, project structure, existing scenes/screens, data models, runtime systems, tests, and build tooling.
- Identify existing combat, character, inventory, save, quest, UI, and presentation systems.
- Map each existing system to the translated architecture.
- Record obsolete, incomplete, compatible, and conflicting components.
- Establish a clean build/run baseline before major changes.

### Deliverable
A short implementation audit note under `Design/Translated/` or implementation documentation describing reuse/refactor/replace decisions.

### Acceptance criteria

- Project build status is known.
- Existing architecture is mapped.
- No translated content has yet been reinterpreted.

## Phase 01 — Domain architecture and data contracts

### Goal
Create the stable backbone before implementing content-heavy behavior.

### Implement

- Stable ID strategy.
- Definition vs runtime-state separation.
- Character, enemy, skill, item, encounter, quest, region, effect, and resolution definitions.
- Runtime combatant and progression state.
- Primary attributes: `Body`, `Agility`, `Soul`, `Charm`.
- Secondary attributes: `TraitA`, `TraitB`, `TraitC`, `TraitD`.
- `Health` and `Moral` resources.
- Equipment slot IDs.
- Presentation binding interfaces/data.
- Generic `EffectHook` contract with hook ID and parameter payload.

### Do not

- Bind gameplay to filenames, sprites, or display strings.
- Encode source-theme terminology in core architecture.

### Acceptance criteria

- Definitions can be loaded independently of presentation.
- Runtime state can reference definitions only by stable IDs.
- A placeholder character/enemy/item can be instantiated from data.
- Renaming a display label cannot break a lookup.

## Phase 02 — Combat foundation

### Goal
Produce a complete minimal turn-based combat loop with two resolution routes.

### Implement

- Turn/initiative flow.
- Target selection.
- Skill execution pipeline.
- Health damage and restoration.
- Moral damage, restoration, resistance, accuracy, overflow, and threshold/finisher support where defined by skill data.
- Buff/debuff lifecycle.
- Passive/equipment effect participation.
- Victory/defeat detection.

### Resolution contract

```text
Health reaches defeat condition
    -> Encounter.DefeatResolution
    -> configured ordinary/narrative/incapacitation/etc. outcome

Moral reaches surrender condition
    -> Surrender
    -> PostCombatResolution
    -> dialogue/event outcome
    -> optional recruitment or other authored result
```

Every enemy must be able to reach the Moral route.

### Acceptance criteria

- A combat encounter can be completed through Health.
- The same or another encounter can be completed through Moral.
- Moral completion reaches Surrender, not automatic recruitment.
- Health completion invokes data-driven resolution.
- Combat UI works with placeholder presentation.

## Phase 03 — Effects, equipment, and progression

### Goal
Make character customization and progression functional without bespoke one-off item architecture.

### Implement

- Stat modifiers.
- Trait modifiers.
- Active effects.
- Skill passives.
- Equipment passives.
- Persistent afflictions.
- Equipment compatibility by slot ID/tag.
- Item evolution/progression state infrastructure.
- Usage/experience counters.
- Context multipliers.
- History statistics.
- Generic `EffectHook` registration, validation, activation, parameter access, and safe unresolved behavior.

### Important rule

An unresolved hook must fail safely and visibly in development diagnostics; it must not corrupt state or silently create invented mechanics.

### Acceptance criteria

- Equipping/removing an item updates derived gameplay state correctly.
- Permanent effects persist according to their lifecycle.
- A new hook can be declared in data without changing item architecture.
- Unknown/disabled hooks do not crash the game or corrupt saves.

## Phase 04 — Narrative resolution and recruitment

### Goal
Connect combat outcomes to authored progression.

### Implement

- Dialogue/event abstraction.
- Conditions and consequences.
- Quest state.
- Quest-gated ally availability.
- Post-surrender resolution.
- Explicit recruitment outcomes.
- Encounter-specific Health `DefeatResolution`.
- Persistent narrative flags.

### Canonical behavior

`Surrender` means the combatant has stopped opposing the player through the Moral route. It opens a resolution event. That event decides what happens next.

Possible outcomes are data-driven; recruitment is only one outcome.

### Acceptance criteria

- A quest can gate an ally.
- A surrender event can recruit an enemy.
- A surrender event can also produce a non-recruitment outcome.
- Health defeat can produce a different configured resolution.
- Outcomes persist after save/load.

## Phase 05 — Exploration, regions, and encounters

### Goal
Create a playable world loop.

### Implement

- Region definitions and progression requirements.
- Exploration state.
- Encounter selection/spawning.
- Mob, Elite, and QuestTarget encounter roles.
- Quest targets.
- Rewards and progression conditions.
- Return path to the base/community loop.

### Content rule

Do not invent canonical regions, quests, or enemy statistics where translated content leaves them unspecified. Build reusable data infrastructure and populate only supported content or clearly marked placeholder/test content.

### Acceptance criteria

- Player can enter a region.
- Player can trigger combat.
- Player can resolve combat by both routes.
- Quest and encounter state update correctly.
- Player can return to the base loop.

## Phase 06 — Base, assignments, and extensible facilities

### Goal
Implement the infrastructure for community growth without prematurely fixing balance rules.

### Implement

- Base/community state.
- Character assignment framework.
- Facility definitions.
- Integration/Rehabilitation extension point.
- Resource production extension point.
- Equipment transmutation extension point.
- Expedition dispatch extension point.
- Persistent affliction/progression integration.

### Do not hardcode as canon

- costs;
- durations;
- capacities;
- success/failure probabilities;
- production formulas;
- expedition formulas.

These may exist as configurable placeholder/test values only if clearly isolated from canonical design data.

### Acceptance criteria

- Facilities can be represented by data.
- Characters can be assigned and unassigned.
- Facility actions have explicit inputs/outputs/state.
- Future rules can be added without rewriting the base architecture.

## Phase 07 — Populate translated content

### Goal
Load the translated content into the game through the data architecture.

### Populate

- Enemy roster from `content/enemies.md`.
- Character roster from `content/characters.md`.
- Skills from `content/skills.md`.
- Items from `content/items.md`.
- Protagonist state model from `content/protagonist.md`.
- World premise/mechanics from `content/world.md` and `content/mechanics.md`.

### Rules

- Preserve stable IDs from translated content.
- Keep provisional affinity and trait IDs configurable.
- Do not convert unspecified values into fake canonical data.
- Use development fixtures/test content where needed to exercise systems.

### Acceptance criteria

- All translated records validate against schemas.
- Broken references are reported.
- Placeholder content is clearly identified.
- No runtime dependency on original CSV/HTML files exists.

## Phase 08 — Functional UI and presentation bindings

### Goal
Make the entire loop usable while preserving presentation independence.

### Implement screens/views for

- exploration;
- combat;
- Health and Moral state;
- skill selection;
- surrender/defeat resolution;
- dialogue and recruitment;
- party/character sheet;
- inventory/equipment;
- base/assignments;
- save/load;
- debugging/validation where useful.

### Presentation contract

UI, images, portraits, animations, sounds, colors, and display names are replaceable bindings. Missing assets must degrade gracefully to placeholders.

### Acceptance criteria

A full gameplay loop is playable using generic assets only.

## Phase 09 — Persistence, migration, and validation

### Goal
Make the data-driven architecture safe to evolve.

### Implement

- Save/load for progression and runtime state.
- Versioned save format or migration strategy appropriate to the project.
- Stable ID validation.
- Missing-definition handling.
- Missing-presentation fallback.
- Content schema validation.
- EffectHook validation.

### Mandatory regression scenario

1. Start a game.
2. Enter combat.
3. Use Health route.
4. Save/load.
5. Enter another combat.
6. Use Moral route.
7. Resolve Surrender through narrative.
8. Recruit when configured.
9. Equip an item and verify modifiers.
10. Return to base and change an assignment.
11. Save/load again.
12. Replace presentation bindings or labels.
13. Verify gameplay and save compatibility remain intact.

## Phase 10 — Completion pass

### Goal
Turn the functional implementation into a coherent game experience without violating architecture.

### Work

- Improve feedback and clarity.
- Balance only where supported by available design or explicitly isolated tuning data.
- Improve accessibility.
- Improve pacing and transitions.
- Add diagnostics and developer tooling.
- Remove dead experimental paths.
- Verify no presentation dependency leaked into gameplay.

## 4. Required validation matrix

Before declaring the implementation complete, verify at minimum:

| Area | Required proof |
|---|---|
| IDs | Display-name changes do not break references |
| Presentation | Missing/replaced assets preserve gameplay |
| Combat | Health route completes |
| Combat | Moral route completes for every enemy definition |
| Surrender | Opens post-combat resolution |
| Recruitment | Explicitly granted by event outcome only |
| Health defeat | Uses encounter data |
| Items | Slot IDs, modifiers, restrictions, and persistence work |
| EffectHook | Known hooks execute; unknown hooks fail safely |
| Progression | Attributes/effects/history persist |
| Narrative | Quest gating and outcomes persist |
| Base | Assignment infrastructure works without fixed canonical balance |
| Save | Core state survives save/load |
| Content | No translated record has an unresolved broken reference |

## 5. Decision and ambiguity protocol

If implementation encounters a genuinely blocking ambiguity:

1. Search `Design/Translated/` first.
2. If marked `CANON`, implement it.
3. If marked `DESIGN SUGGESTION — NOT CANON`, do not treat it as mandatory.
4. If marked `UNSPECIFIED`, prefer generic infrastructure, data fields, or a documented extension point.
5. Only request a new `NEEDS DECISION` when implementation cannot proceed coherently without choosing between materially different game behaviors.

Never solve ambiguity by reading presentation-only source material into gameplay contracts unless the translated layer explicitly requires that dependency.

## 6. Completion definition

The implementation is complete when the project provides a coherent playable RPG loop covering:

```text
Explore
  -> Encounter
  -> Turn-based combat
      -> Health resolution OR Moral resolution
  -> DefeatResolution or Surrender resolution
  -> Narrative consequence
  -> Optional recruitment/reward/progression
  -> Return to exploration or base
  -> Character/equipment/assignment progression
  -> Persistent save state
```

The game must remain fully functional if presentation assets are replaced with generic placeholders or an alternative presentation pack.
