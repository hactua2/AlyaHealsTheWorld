# AHTW — Unity Vertical Slice Implementation Handoff

**Working title:** The Water We Share  
**Target:** Maintainable indie-scale Unity implementation, testable and extensible without building a generic framework.  
**Status:** Implementation contract proposal. This document does not claim that runtime systems already exist.  
**Audience:** An implementation LLM/developer working incrementally in the existing repository.

## 1. Mission and success boundary

Implement one integrated, playable vertical slice demonstrating:

**Meet a person in need → investigate a local Ferida manifestation → prepare and fight → make a costly collective decision → change the community → delegate the first autonomous Expedition.**

Canonical story:
- Hub: Brackenford.
- Region: Ashfen Verge.
- Local Ferida manifestation: The Red Thread.
- Water scarcity and unequal rationing predate the supernatural manifestation. The Ferida amplifies exhaustion, fear, and distrust; it does not create every social problem or remove characters' agency.
- The Organization provides genuine expertise and proposes a defensible containment plan, but its plan abandons lower residents and their seed reserve.
- Alya's third solution depends on local knowledge, repair materials, care, and collective effort.
- **Mandatory loss:** the lower-terrace seed reserve and a substantial part of the next planting cycle are lost. Brackenford survives and the downstream channel is secured.
- Alya is recognized as leader, makes an initial facility choice, and launches/resolves one autonomous Expedition.

The slice is not complete merely because scenes can be entered. It is complete when quest progression, combat/objective resolution, persistent state, community management, and the Expedition work together in an integrated build and the acceptance criteria in this document pass.

### Source-of-truth documents

Inspect and follow these documents before implementation:
- docs/VERTICAL_SLICE_SCOPE.md
- docs/vertical_slice/ACT_I_QUEST_GRAPH.md
- docs/vertical_slice/ACT_I_QUEST_GRAPH_CONTINUATION.md
- docs/vertical_slice/ACT_I_DIALOGUE_PACK.md
- docs/vertical_slice/ACT_I_CONTENT_CATALOG.md
- data/vertical_slice/act_i_quests.json
- data/vertical_slice/act_i_content.json
- data/vertical_slice/act_i_effects.json
- docs/NARRATIVE_CANON.md
- docs/architecture/GAME_ARCHITECTURE.md
- docs/IMPLEMENTATION_SPEC.md
- implementation_spec/COMBAT.md
- implementation_spec/TURN_RESOLUTION.md
- implementation_spec/STATUS_EFFECTS.md

If this handoff conflicts with a canonical contract, do not silently create a second rule. Report the exact conflict and update the relevant source of truth before implementing a workaround.

## 2. Non-negotiable engineering principles

1. Domain rules must be deterministic and testable outside Unity scenes wherever practical.
2. Unity is the composition and presentation environment, not the source of gameplay truth. MonoBehaviours collect input, render state, and call application services; they do not independently decide costs, quest outcomes, or rewards.
3. Maintain one source of truth for each piece of state. UI is a projection, never a parallel owner.
4. Use stable IDs for content links, events, save data, and tests. Display strings, scene object names, array indexes, and localized text are not identifiers.
5. Validate content at load/build time. Duplicate IDs, missing references, unsupported effect types, and invalid quest links must produce actionable diagnostics.
6. Commit canonical mutations before publishing domain events. Event handlers must never observe a half-committed transaction.
7. Prefer composition and small interfaces over deep inheritance. Use data-driven definitions and registered handlers for variable behavior.
8. Build only the systems needed by this slice, while leaving clean seams for future content. Avoid speculative frameworks and unrelated refactors.
9. Prefer explicit state transitions, clear error results, small methods, meaningful names, and readable code.
10. Automated validation is part of implementation. Use unit tests for rules, integration tests for cross-system contracts, and a small number of PlayMode tests for Unity wiring.

## 3. Inspect the repository before designing the final code layout

The implementation agent must first establish:
- whether a Unity project already exists and its root path;
- the Unity/editor version and current packages;
- current UI/input approach and coding conventions;
- existing runtime systems, tests, assembly definitions, and CI workflows;
- whether the slice JSON files are already included in the Unity content pipeline.

Do not create a second Unity project root or duplicate existing systems. Adapt the suggested logical layout below to the actual repository.

Suggested logical structure:

    Assets/_Project/
      Scenes/ (Bootstrap, Brackenford, AshfenVerge, Combat as needed)
      Prefabs/
      Art/
      Audio/
      UI/
      Scripts/
        Domain/ (Combat, Effects, Quests, Inventory, Community, Expeditions, World, Persistence)
        Application/ (Commands, Queries, Services, Validation)
        Infrastructure/ (Content, Persistence, Events, Logging)
        Presentation/ (Bootstrap, Exploration, Dialogue, Combat, Community, Expeditions, UI)
      Tests/
        EditMode/
        PlayMode/

If useful, create assembly definitions with conceptual boundaries:
- AHTW.Domain: plain C# models and rules; no UnityEngine dependency.
- AHTW.Application: use cases and orchestration; references Domain.
- AHTW.Infrastructure: JSON loading, save storage, event bus, logging; implements application/domain contracts.
- AHTW.Unity: MonoBehaviours, scenes, UI, audio/visual adapters.
- AHTW.Tests.EditMode and AHTW.Tests.PlayMode.

Fewer assemblies are acceptable if they fit the existing project better. Preserve the conceptual dependency direction and avoid cyclic dependencies.

## 4. SOLID architecture, service locator, and event bus

### 4.1 Dependency direction

Use this direction:

Presentation → Application → Domain  
Infrastructure → Domain/Application contracts

- **Domain:** entities/value objects, invariants, deterministic rules, and state transitions.
- **Application:** orchestrates use cases such as selecting a dialogue choice, resolving an encounter, building a facility, launching an Expedition, and saving.
- **Infrastructure:** JSON files, save storage, clocks/RNG adapters, event dispatch, and logging.
- **Presentation:** Unity scene/UI input and rendering; it does not mutate canonical state directly.

Domain code must not depend on Unity scenes, UI, static singletons, or concrete file storage.

### 4.2 SOLID expectations

- **Single Responsibility:** Quest progression, resource transactions, encounter resolution, content loading, and presentation have separate responsibilities. Do not create a single GameManager that owns all rules.
- **Open/Closed:** Add a supported effect handler without changing unrelated systems. Avoid designing a generic plugin framework without a real need.
- **Liskov Substitution:** In-memory and production implementations of repositories, clocks, RNG, and save stores must honor the same contracts and error semantics.
- **Interface Segregation:** Prefer narrow interfaces such as IQuestRepository, IResourceLedger, IGameClock, IRandomSource, and ISaveStore over a giant IGameService.
- **Dependency Inversion:** Application services depend on abstractions; concrete implementations are wired during startup.

Use interfaces when they create a meaningful seam for substitution/testing. Plain data objects and simple methods do not need an interface merely for style.

### 4.3 Service locator: allowed with guardrails

A small service locator is acceptable for this indie project:
- Register services once from a bootstrap/composition root.
- Prefer constructor injection inside Domain/Application code.
- Restrict locator lookups to Unity composition boundaries and adapters; do not let domain entities call ServiceLocator.Get<T>().
- Register required services explicitly and fail fast with actionable diagnostics if a required service is missing.
- Avoid hidden runtime registration and scattered lookups throughout gameplay code.
- Provide a test composition root using fakes and in-memory implementations.
- The locator resolves services; it must not own mutable gameplay state.

Suggested startup order: load content → validate content → create domain state → register services → restore save or create a new game → initialize presentation → enable player input. If validation fails, prevent entry into an invalid game state and expose diagnostics.

### 4.4 Event bus: facts, not commands

Use a typed event bus for decoupled notifications, not as a replacement for direct calls or all application orchestration.

Rules:
- Events are immutable facts describing something that has already happened, e.g. QuestStageCompleted, ResourceChanged, EncounterResolved, FacilityBuilt, ExpeditionLaunched, ExpeditionResolved.
- Commands express intent and call application services, e.g. ChooseDialogueOption, CommitRepairMaterials, LaunchExpedition. Do not publish a command as if it were a completed fact.
- Publish only after canonical state mutations have committed.
- Preserve deterministic ordering wherever event order affects gameplay.
- Subscribers must be disposed/unsubscribed when a service or view is destroyed. Scene reloads must not accumulate duplicate subscriptions.
- Event handlers may request a subsequent use case but must not mutate an uncommitted transaction.
- Bound effect-trigger recursion using the canonical execution budget.
- Do not use the bus for frame updates, every UI property, or data queries; query current state instead.
- In development builds, log event type, stable IDs, and correlation/transaction ID where useful.

## 5. Content pipeline and IDs

### 5.1 Loading pipeline

The three existing JSON files are the authored content baseline. Use this pipeline:

JSON bytes → DTO deserialization → schema/version checks → ID/reference validation → mapping to runtime definitions → immutable content registry.

Do not use mutable runtime objects as deserialization DTOs. Avoid duplicate sources of truth in ScriptableObjects; use ScriptableObjects only for Unity-facing configuration or authoring features that do not conflict with the canonical JSON.

The registry should support efficient stable-ID lookup and return explicit errors for unknown IDs. Never silently return a default definition when a referenced ID is missing.

### 5.2 ID policy

Preserve canonical IDs, including VS1_*, RESOURCE_*, ITEM_*, FAC_*, LOC_*, POI_*, ENEMY_*, ENC_*, EXP_*, ALYA, ALLY-001, and ALLY-005. Names and prose may change independently; IDs must not.

Validate:
- uniqueness in each namespace;
- all quest, effect, resource, item, facility, location, POI, enemy, encounter, and Expedition references;
- supported enum/handler values;
- required fields and valid numeric ranges;
- quest graph reachability and absence of accidental softlocks.

If an ID must change after it has appeared in saves, provide a migration/alias instead of silently orphaning state.

### 5.3 Effect handlers

Effect IDs in act_i_effects.json are content-level IDs, not permission to invent arbitrary global mechanics. Map supported effect types to small registered handlers. Each handler validates its payload, checks preconditions, applies a canonical mutation through the appropriate service, returns a structured result, and emits events only after commit.

If an effect type is unsupported by the existing implementation contracts, implement a contract-compliant handler or update the canonical schema/specification first. Never invoke arbitrary method names from content via reflection.

Prefer typed DTOs and validated effect payloads over unstructured dictionaries. Unknown effect types must fail validation.

## 6. Domain boundaries and state ownership

| Domain | Owns | Does not own |
|---|---|---|
| World/Quest | quest stages/objectives, flags, choice history, narrative/world states | inventory quantities or combat turn state |
| Characters/Party | party membership, availability, slice-relevant progression and relationship state | dialogue UI or transforms |
| Combat | participants, initiative, intent, meters, effects, objective progress, combat outcome | persistent quest completion policy |
| Inventory/Resources | quantities, item stacks, reservations, atomic cost/reward transactions | dialogue choice policy |
| Community | facility state, assignments, member availability, initial management choice | Expedition resolution internals |
| Expedition | activity ID, assigned member, status, game-time timestamps, deterministic result state | character membership or inventory storage |
| Content registry | immutable definitions loaded from content files | mutable playthrough state |
| Persistence | save DTOs, schema version, migrations | gameplay decisions |

A use case may coordinate multiple domains. For example, Q07 preparation may coordinate resource reservations, quest flags, and encounter modifiers through an application service. It must not let a quest object reach into a scene or UI.

### 6.1 Canonical mutation sequence

Follow the implementation contract:

**Canonical Mutation → Derived State → Domain Event → Event Handlers → Subsequent Canonical Mutation**

- Validate preconditions and all costs before committing.
- Multi-step operations are atomic by default.
- Do not publish events for a failed or rolled-back mutation.
- Derived values are recalculated/invalidated according to the canonical contract.
- Event subscribers may initiate subsequent application use cases but cannot observe uncommitted state.

### 6.2 Time and randomness

- Advance game time only through explicit player-controlled progression. Idle menus do not advance the world.
- Use an injectable IGameClock or explicit game-time value for simulation; never use Time.time or wall-clock time as canonical game time.
- Use an injectable deterministic random source for encounter and Expedition rolls. Persist the RNG state needed by the save contract.
- Tests should use a fixed clock and seeded RNG.
- Unity frame time drives animation/presentation only, not canonical simulation timestamps.

## 7. Required systems and slice behavior

### 7.1 Bootstrap and session
- Validate content before enabling player input.
- Create or restore a session through one explicit application entry point.
- Register services/subscribers once.
- Support a clean new-game/restart path for automated tests.
- Show developer diagnostics when content validation fails.

### 7.2 Quest and narrative state
Implement the eleven authored stages, VS1_Q01 through VS1_Q11.

Required behavior:
- The quest domain evaluates prerequisites and completion flags.
- Dialogue choices use stable IDs and are applied once; repeated interaction cannot reapply costs/rewards.
- Persist choice history or equivalent canonical flags.
- Optional discovery may change context, reward, dialogue, cost, or encounter pressure but never blocks the main path.
- Retreat follows the authored failure policy and cannot grant victory rewards or softlock progression.
- Stage transitions have explicit completion criteria and are idempotent where practical.
- Consequences are communicated through dialogue, UI, or world state.

Major choices:
- Q02: enforce rationing / share water / investigate.
- Q04: close gate / temporary diversion / withdraw.
- Q06: accept Organization plan / challenge it / request an alternative.
- Q07: workers first / channel first / staged diversion (the last requires the channel clue).
- Q09: care / repair / coordination as recovery priority.
- Q10: choose Recovery Room / Common Workshop / Coordination Board.

All branches converge on the authored main path. Do not create alternate campaigns.

### 7.3 Dialogue and interaction
- Keep dialogue data and choices separate from dialogue UI.
- Choices declare stable IDs, preconditions, and effect IDs.
- UI asks an application service to choose an option, then refreshes from canonical state.
- Do not encode gameplay rules solely in UnityEvents or button callbacks.
- Provide readable text, speaker identity, clear options, and reasons for known unavailable choices.
- Any optional adult content in the build must be skippable and must not gate the main path or essential rewards.

### 7.4 Exploration
Implement Brackenford, Ashfen Verge, and three POIs: Silt Path, Old Weir, Root-Vault Sluice. A compact location/POI UI or a small set of scenes is sufficient; open-world traversal and grid/range combat are out of scope.

Use stable location IDs from act_i_content.json. Interaction triggers query canonical state and issue application commands; they do not directly mutate quests. Returning to a location preserves discoveries and completed encounters according to quest state.

### 7.5 Combat

Encounters:
- ENC_VS1_01_HUSKS
- ENC_VS1_02_THREADLINGS
- ENC_VS1_03_HOLLOW_WARDEN
- ENC_VS1_04_ROOT_VAULT

Enemy archetypes:
- ENEMY_VS1_FRAYED_HUSK
- ENEMY_VS1_THREADLING
- ENEMY_VS1_HOLLOW_WARDEN
- ENEMY_VS1_ROOT_KNOT

Baseline party: ALYA + ALLY-001. ALLY-005 Cuidadora may join according to the authored care/recovery conditions.

Requirements:
- Implement only the skill/effect subset required by these encounters, but follow canonical combat, turn-resolution, and status-effect contracts.
- Initiative is determined at encounter start and remains stable for that encounter.
- Turn-start effects, duration updates/expiration, derived-state recalculation, action validation, costs, effects, reactions/chains, and terminal checks follow canonical order.
- Insufficient resources make an action unavailable. UI cannot commit invalid actions.
- Each action resolves atomically before terminal combat state is committed.
- Enemy intent visibility follows content definitions and canonical intent rules.
- Retreat is a contextual outcome where specified; retreat is not victory.
- Combat reports an outcome; the quest/application layer decides how that outcome advances the quest.
- Do not introduce grid movement, spatial range, universal level scaling, or new meters for this slice.

**Climax objective encounter:** victory requires explicit progress for all required objectives:
1. VS1_OBJ_STABILIZE_DIVERSION
2. VS1_OBJ_SEVER_FILAMENT
3. VS1_OBJ_SECURE_GATE

Defeating enemies alone is not victory. Q07 community contribution/preparation may reduce an objective requirement or remove/reduce one pressure source according to authored content. The seed-reserve loss and downstream-channel protection are mandatory outcomes regardless of preparation. Commit each outcome exactly once through the quest/outcome service; combat UI must never set those flags directly.

### 7.6 Effects and meters
Follow implementation_spec/COMBAT.md, implementation_spec/TURN_RESOLUTION.md, and implementation_spec/STATUS_EFFECTS.md. Do not invent an independent status timer or stacking model.

Effects must retain the definition ID, source, target, duration, stack state/strength, and runtime provenance required by the canonical contract. Bound trigger recursion using the execution budget. Keep content effect IDs separate from the global set of supported effect handler types.

Where item content modifies Vitality, verify the canonical meter definition before implementation; do not reinterpret it based only on the field name.

### 7.7 Inventory, resources, and rewards

Resources:
- RESOURCE_TIMBER
- RESOURCE_FIBER
- RESOURCE_BOTANICAL_EXTRACT
- RESOURCE_GOLD

Key items:
- ITEM_VS1_FILTER_FIBER
- ITEM_VS1_SOOTHING_TONIC
- ITEM_VS1_REPAIR_BUNDLE
- ITEM_VS1_SEED_RESERVE

Requirements:
- Apply rewards/costs exactly once.
- Validate all costs before committing; no partial deductions on failure unless the canonical contract explicitly allows them.
- Reserve/protect required repair materials from optional crafting while the mandatory repair objective is active.
- Evaluate conditional Q07 costs before committing preparation:
  - Gate closure may add 1 Timber.
  - Accepting the Organization plan may add 2 Gold to resident-support costs.
- Initial authoring baseline: 2 Timber, 2 Fiber, 0 Botanical Extract, 6 Gold. Guaranteed rewards are intended to prevent a mandatory softlock.
- Encounter 1 grants 1 Timber; encounter 2 guarantees at least 1 Fiber; the Hollow Warden encounter guarantees at least 1 Fiber; climax rewards include 2 Timber and 1 Fiber.
- Optional crafting cannot consume mandatory repair stock.
- Numeric values are provisional until runtime balance QA.

### 7.8 Community and facilities

After Q09/Q10, let the player choose one initial facility:
- FAC_VS1_RECOVERY_ROOM — Stability; improves recovery access and supports Cuidadora.
- FAC_VS1_COMMON_WORKSHOP — Conversion; enables a basic Timber/Fiber repair-bundle loop.
- FAC_VS1_COORDINATION_BOARD — Access; improves assignment/Expedition visibility.

The chosen facility is unlocked/selected and persisted. The other two remain visible future options, not free unlocks. Reuse the canonical building/facility model; do not create a parallel slice-only facility system.

Care-first can support Cuidadora's recruitment, and investing in the Recovery Room can also satisfy the authored recruitment condition. Otherwise she remains a trusted NPC and a later recruitment path is outside this slice.

### 7.9 Autonomous Expedition

Implement EXP_VS1_UPPER_ROUTE_SURVEY using the existing Expedition contract:
- choose an eligible community member;
- show purpose, estimated duration, cost/commitment, and result categories;
- validate eligibility and availability;
- launch without Alya;
- mark the assigned member unavailable to the active party while away;
- resolve at canonical game time with deterministic RNG/state;
- grant a small reward, discovery, or modest time-cost complication;
- restore availability according to canonical return rules;
- persist launched/resolved state;
- show the result and its community impact.

This is not a Sidequest. A Sidequest requires Alya; an Expedition is an NPC-only delegated activity. The basic Expedition must be available after Act I regardless of the chosen first facility. The Coordination Board improves visibility but is not a prerequisite.

### 7.10 Persistence

Implement versioned save/load. Persist at least:
- quest stage/objectives/flags/choice history;
- discoveries and optional objectives;
- party membership and relevant character/relationship state;
- inventory, resources, and unique narrative items;
- facility choice/unlocks, assignments, and member availability;
- Expedition status, timestamps, result state, and RNG information needed for reproducibility;
- game time and persistent event state required to reconstruct play.

Do not save mid-combat-resolution. Save at canonical safe boundaries. Use stable IDs in save DTOs; do not serialize GameObject references, delegates, Unity instance IDs, or reconstructible UI state. Add a save schema version and migration seam. A migration must validate the migrated result before replacing the original save.

## 8. Minimum UI/presentation

Build functional UI before final art polish:
1. Main menu or deterministic developer entry point (new game/load/restart).
2. Brackenford hub with interactions and visible community state.
3. Dialogue panel with speaker, text, options, and unavailable-state explanations where appropriate.
4. Ashfen Verge location/POI selection and discovery feedback.
5. Combat UI: party/enemy status, intent where available, action selection, effect feedback, objective progress, retreat, outcome.
6. Reward/quest update summary.
7. Inventory/resource view.
8. Facility selection and basic community status.
9. Expedition assignment/launch and result view.
10. Save/load controls or a test harness using the same persistence service.

Views query/render canonical state. UI callbacks issue commands; they do not own flags, costs, rewards, or progression. Missing art/audio must use explicit placeholders and diagnostics, not broken references or silent failures. Use the UI toolkit already present in the project.

## 9. Automated testing and validation

Use Unity Test Framework or the repository's current test runner. Prefer EditMode/plain C# tests for domain rules; use PlayMode tests for Unity lifecycle and scene wiring.

### 9.1 Unit tests
At minimum:
- registry rejects duplicate IDs, missing references, and unsupported effect types;
- quest prerequisites prevent premature progression;
- each major choice applies consequences once;
- optional clue unlocks staged diversion but is not mandatory;
- resource transactions are atomic on insufficient stock;
- conditional Q07 costs apply only when their flag is true;
- optional crafting cannot consume reserved repair materials;
- retreat does not award victory/completion rewards;
- terminal combat state waits for current atomic action to resolve;
- status duration/stacking/turn-start behavior matches canonical contracts;
- climax enemy defeat without objective completion is not victory;
- completing required objectives resolves the climax;
- mandatory seed loss and downstream protection commit exactly once;
- facility selection unlocks the right state and only one initial option is chosen;
- the basic Expedition remains available regardless of facility choice;
- assigned member cannot enter incompatible availability/activity states;
- Expedition result is deterministic for a fixed seed/state;
- save/load round-trip preserves slice state;
- invalid save schema/content IDs fail safely with diagnostics.

### 9.2 Integration tests
At minimum:
1. New game → Q01–Q03, including optional clue/reward.
2. Every Q02/Q04/Q06 choice path reaches Q07 without softlock.
3. Every Q07 preparation priority applies the correct climax modifiers/objective requirements.
4. Climax resolution applies mandatory loss, secures downstream channel, and advances to Q09.
5. Q09 priority and Q10 facility choice persist and display correctly.
6. Q11 launches/resolves an autonomous Expedition; member availability, reward, time, and quest flags agree.
7. Save at hub → reload → continue without duplicate costs/rewards/events.
8. Main path completes without optional discovery, adult content, or perfect combat outcomes.

### 9.3 PlayMode smoke tests
- Bootstrap validates content before gameplay.
- Required services/views initialize without missing dependencies.
- A dialogue choice triggers one application command and one consequence.
- Combat starts, accepts a valid action, resolves, and returns to quest flow.
- Facility selection and Expedition launch/resolution work.
- Save/load and scene transitions do not duplicate event subscriptions or UI listeners.

### 9.4 Testability rules
- Provide in-memory repositories/ledgers and deterministic clock/RNG implementations.
- Do not depend on wall-clock delays, animation timing, real filesystem paths, or unseeded randomness.
- Do not use Thread.Sleep for game-time progression.
- Prefer explicit AdvanceGameTime, ResolveEncounter, and CompleteExpedition operations.
- Assert canonical state and domain events, not only UI text or GameObject names.
- Include relevant stable IDs and expected/actual values in failures.

## 10. Recommended implementation sequence

Every increment should compile and be reviewable.

### Phase 0 — Repository reconnaissance
Inspect the actual project root, Unity version, packages, UI/input setup, existing code/tests, and current conventions. Identify existing systems before adding alternatives. Confirm the three JSON files are available. Produce a short plan and list any contract conflicts. Do not refactor unrelated code.

**Exit gate:** verified project map and a minimal implementation plan.

### Phase 1 — Bootstrap, content loading, and validation
Define content DTOs, ID/reference validation, content registry, structured result/error types, clock/RNG interfaces, save-store interface, and event interface. Implement the composition root/service locator with fail-fast checks. Add static content validation and unit tests for duplicate IDs, missing references, unsupported effects, and invalid quest links.

**Exit gate:** content loads and validation either passes or produces actionable diagnostics; invalid content cannot start gameplay.

### Phase 2 — Quest, dialogue, inventory/resources
Implement quest/world state, application use cases, typed effect handlers, atomic resource transactions, and a simple dialogue/choice UI. Test all choice consequences and the mandatory-material guarantee.

**Exit gate:** Q01–Q07 progress through a development harness without requiring combat scenes.

### Phase 3 — Exploration and encounter integration
Implement locations/POIs, discoveries, encounter start/return, reward reporting, and retreat policy. Connect encounters by stable IDs. Add tests for optional discovery and returning to the hub/region.

**Exit gate:** location flow works without scene scripts mutating canonical state.

### Phase 4 — Combat subset and climax objective
Implement the required deterministic turn pipeline and only the skills/effects used by the slice. Implement four encounters, intent UI, objective checks, and climax win conditions. Add tests for turn/effect contracts and objective edge cases.

**Exit gate:** all four encounters resolve consistently; defeating the Root-Knot alone cannot win the climax.

### Phase 5 — Community and Expedition
Implement the three facility choices, visible resource/community state, assignments/member availability, and the introductory autonomous Expedition. Use game-time advancement and deterministic resolution; do not create a separate Sidequest loop.

**Exit gate:** Q09–Q11 work and the player sees the community change and Expedition result.

### Phase 6 — Persistence and full-flow integration
Implement versioned save/load and migration validation. Add deterministic full-path tests and PlayMode smoke tests. Save only at canonical safe boundaries. Verify no duplicate rewards/events after load or scene transitions.

**Exit gate:** the main path survives save/load and required automated tests pass.

### Phase 7 — Manual playtest, usability, and balance
Play from a clean save without developer instructions. Confirm consequences are understandable and no branch softlocks. Tune provisional numeric values from actual play. Log issues rather than silently changing canonical design. Add only the polish needed to communicate state and feedback.

**Exit gate:** integrated acceptance criteria pass or remaining exceptions are explicitly documented and approved.

## 11. Integrated acceptance checklist

- [ ] New game, load, and restart work reliably.
- [ ] Content validation runs before gameplay and reports actionable errors.
- [ ] All eleven quest stages have explicit entry/exit criteria and stable IDs.
- [ ] Major choices persist and cannot apply twice.
- [ ] Optional content is optional; the main path remains completable without it.
- [ ] All four encounters use canonical combat contracts and produce correct outcomes/rewards.
- [ ] Climax requires objective checks; enemy defeat alone is insufficient.
- [ ] Mandatory seed-reserve loss and downstream-channel protection occur exactly once.
- [ ] Required Q07 materials cannot be consumed accidentally by optional crafting.
- [ ] One facility is selected and persisted; the other two remain future options.
- [ ] Cuidadora recruitment follows authored care/recovery conditions.
- [ ] First Expedition resolves autonomously and distinctly from a Sidequest.
- [ ] Assigned member availability/return state is correct.
- [ ] Save/load preserves state without duplicating effects, rewards, events, or subscriptions.
- [ ] Unit, integration, and PlayMode smoke tests pass.
- [ ] A fresh manual playthrough reaches the end of Q11 without external instructions.
- [ ] Provisional numeric balance and known limitations are documented.

## 12. Instructions to the implementation LLM

1. **Inspect before editing.** Do not assume this repository already contains a Unity runtime.
2. **Report a concise plan first**, including the first small milestone and expected files to change.
3. **Implement incrementally.** Avoid one enormous patch; compile/test after each milestone.
4. **Preserve source of truth.** If JSON and canonical specs disagree, stop and report the exact IDs/fields plus a proposed resolution.
5. **Never fabricate test results.** State exactly which tests ran, which passed/failed, and what could not run.
6. **Do not claim completion without evidence** from an integrated build and the acceptance checklist.
7. **Keep changes scoped.** No unrelated refactors, new frameworks, extra content, or gameplay systems without a demonstrated need.
8. **Summarize each milestone** with changed files, tests/commands actually run, remaining blockers, and the next smallest step.

### Suggested first task

Begin with Phase 0 and Phase 1 only: inspect the repository and identify the actual Unity project root/test setup, then implement the content-loading/validation seam and bootstrap composition root. Do not attempt the entire game in one pass. The first milestone should be reviewable, testable, and leave the project in a known state.
