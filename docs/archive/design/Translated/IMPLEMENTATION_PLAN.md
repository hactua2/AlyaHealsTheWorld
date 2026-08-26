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
9. Do not claim a phase is complete without producing observable evidence according to the Unity/MCP verification protocol below.

When an existing implementation conflicts with translated canon, translated canon wins. Refactor rather than preserving an incompatible shortcut.

## 4. Unity/MCP verification protocol

The destination LLM has access to Unity through MCP. Use that capability as a verification instrument, not merely as a code-editing transport.

For each implementation unit, define and execute:

### 4.1 Success contract

Every meaningful task must specify:

- **Implementation target:** what must exist after the change.
- **Observable proof:** what can be inspected through Unity, tests, logs, serialized state, scene hierarchy, or gameplay execution.
- **Verification action:** the exact class of Unity/MCP action required to produce that proof.
- **Expected result:** the state that constitutes success.
- **Failure signal:** compile error, exception, assertion failure, incorrect state, missing object, or incorrect transition.
- **Recovery rule:** inspect the failure, make the smallest correction, and rerun the same verification before proceeding.

### 4.2 Evidence hierarchy

Prefer stronger evidence over weaker evidence:

1. Automated test passes.
2. Unity compiles with no relevant errors.
3. Runtime execution reaches the expected state.
4. Inspector/serialized state matches the expected data.
5. Scene hierarchy contains expected runtime objects.
6. Logs confirm expected transitions.
7. Code inspection alone.

Code inspection is not sufficient proof when a behavior can be executed.

### 4.3 Completion rule

A task is only `COMPLETE` when all applicable checks pass:

```text
BUILD PASS
AND
TEST PASS where testable
AND
RUNTIME OBSERVATION PASS where executable
AND
STATE/CONTENT VALIDATION PASS where data is involved
```

If a check cannot yet be automated, record the manual Unity/MCP procedure that proves it.

### 4.4 Required phase report

At the end of each phase, produce a concise report containing:

```text
PHASE: <number/name>
STATUS: COMPLETE | PARTIAL | BLOCKED

IMPLEMENTED:
- <concrete capability>

VERIFIED BY:
- <test/build/runtime/inspector/log evidence>

EXPECTED RESULT:
- <observable result>

ACTUAL RESULT:
- <observed result>

FAILED CHECKS:
- none | <specific failures>

OPEN ASSUMPTIONS:
- none | UNSPECIFIED / implementation notes
```

A `PARTIAL` or `BLOCKED` phase must not be described as successful.

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

### How you know you succeeded

- Unity project opens successfully.
- Current compile status is explicitly recorded.
- Existing scenes can be enumerated through the available Unity/MCP inspection capability.
- At least one baseline build/compile check is executed.
- The architecture map names the existing systems that will be reused, refactored, or replaced.

**Success evidence:** a baseline report plus observed Unity compile/runtime state.

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

### How you know you succeeded

Create a minimal automated test or Unity validation fixture that:

1. creates a definition with a stable ID;
2. creates independent runtime state referencing that ID;
3. instantiates a placeholder character, enemy, and item;
4. changes only a display label/presentation binding;
5. verifies stable references and gameplay values remain unchanged.

**Expected result:** all references resolve through stable IDs and presentation changes do not alter runtime behavior.

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

### How you know you succeeded

Using deterministic test encounters or Unity test fixtures:

**Health proof**

1. Start combat with known Health values.
2. Execute enough valid actions to reach the Health defeat threshold.
3. Observe that the encounter enters its configured `DefeatResolution`.
4. Assert that `Surrender` was not required for this route.

**Moral proof**

1. Start an equivalent encounter with known Moral values.
2. Execute enough valid actions to reach the Moral surrender threshold.
3. Observe the explicit `Surrender` state.
4. Observe transition to `PostCombatResolution`.
5. Verify the result is not automatic recruitment unless the configured event explicitly grants it.

**Expected result:** both routes are executable, deterministic in the fixture, and produce distinct configured state transitions.

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

### How you know you succeeded

Execute a Unity test sequence:

1. Record baseline derived stats.
2. Equip a known item.
3. Inspect/assert changed derived stats.
4. Unequip it and assert restoration to baseline.
5. Trigger a known implemented `EffectHook` and verify its expected state change.
6. Trigger an unknown/disabled hook.
7. Verify a diagnostic is produced and gameplay state remains valid.
8. Save/load and verify equipment, persistent effects, counters, and history remain consistent.

**Expected result:** modifiers are reversible where appropriate, known hooks execute, unresolved hooks are safe, and persistence survives reload.

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

### How you know you succeeded

Prepare three deterministic event fixtures:

- surrender -> recruitment;
- surrender -> non-recruitment consequence;
- Health defeat -> distinct configured resolution.

For each fixture, execute the encounter in Unity and inspect the resulting party/quest/narrative state.

Then save/load and verify the consequence persists.

**Expected result:** identical combat state can lead to different consequences based on resolution data, not hardcoded enemy behavior.

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

### How you know you succeeded

From a clean Unity play session:

1. enter a test or supported region;
2. trigger each supported encounter role;
3. complete at least one encounter through Health;
4. complete at least one through Moral;
5. verify quest/encounter progression updates;
6. return to the base state.

**Expected result:** no manual editor intervention is required between exploration, combat, resolution, and return.

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

### How you know you succeeded

Using generic fixture data:

1. create a facility definition;
2. assign a character;
3. execute one facility action;
4. inspect explicit input/output/state records;
5. unassign/reassign the character;
6. replace fixture balance values;
7. verify the facility architecture still works without code changes.

**Expected result:** assignment and facility behavior are data-driven, while placeholder balance remains clearly non-canonical.

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

### How you know you succeeded

Run a content validation pass that:

- loads every translated record;
- verifies unique IDs;
- resolves all declared references;
- checks slot and affinity IDs;
- reports unresolved `EffectHook` IDs;
- distinguishes intentional placeholder/test data from canonical data;
- confirms the runtime does not read original CSV/HTML files.

**Expected result:** validation report contains no unresolved broken references. Intentional unresolved hooks are explicitly reported as safe hooks, not errors that corrupt loading.

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

### How you know you succeeded

Run two presentation configurations:

1. normal/generic placeholder bindings;
2. intentionally missing or replaced bindings.

Execute the same gameplay scenario in both and compare:

- combat resolution;
- progression;
- item compatibility;
- narrative outcome;
- save/load state.

**Expected result:** presentation may visibly differ, but gameplay state and results are equivalent.

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

### How you know you succeeded

The entire scenario above must be executed as one repeatable integration test where feasible, or as a documented Unity/MCP procedure otherwise.

Capture and compare key state before and after each save/load:

- stable IDs;
- party composition;
- attributes;
- effects;
- inventory/equipment;
- quest flags;
- base assignments.

**Expected result:** state survives reload and presentation replacement without changing gameplay semantics.

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

### How you know you succeeded

Perform a final smoke test from a clean launch covering the complete loop:

```text
Launch
-> Load/new game
-> Explore
-> Encounter
-> Combat
-> Health or Moral resolution
-> Narrative consequence
-> Optional recruitment/reward
-> Character/equipment progression
-> Base interaction
-> Save
-> Reload
-> Repeat encounter
```

Then run the content validation, compile/build validation, automated tests, and presentation replacement check.

**Expected result:** all mandatory checks pass and no phase remains `PARTIAL` or `BLOCKED`.

## 5. Required validation matrix

Before declaring the implementation complete, verify at minimum:

| Area | Required proof |
|---|---|
| Build | Unity compile/build completes without relevant errors |
| IDs | Display-name changes do not break references |
| Presentation | Missing/replaced assets preserve gameplay |
| Combat | Health route completes and invokes configured resolution |
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
| Runtime | Complete smoke test reaches expected end state |

## 6. Decision and ambiguity protocol

If implementation encounters a genuinely blocking ambiguity:

1. Search `Design/Translated/` first.
2. If marked `CANON`, implement it.
3. If marked `DESIGN SUGGESTION — NOT CANON`, do not treat it as mandatory.
4. If marked `UNSPECIFIED`, prefer generic infrastructure, data fields, or a documented extension point.
5. Only request a new `NEEDS DECISION` when implementation cannot proceed coherently without choosing between materially different game behaviors.

Never solve ambiguity by reading presentation-only source material into gameplay contracts unless the translated layer explicitly requires that dependency.

## 7. Completion definition

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

No implementation phase may be marked complete based solely on code existence. Completion requires the observable evidence defined by the Unity/MCP verification protocol.
