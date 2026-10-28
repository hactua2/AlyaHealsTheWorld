# AHTW — Master Implementation Handoff for a Local LLM

Audience: coding LLM operating on a local AHTW checkout.
Mission: turn the locked design and content into a maintainable, tested, integrated Unity game without inventing requirements.
Current truth: core design/specification is substantially closed and the full-game content-lock baseline is authored. This is an implementation plan, not evidence that runtime systems already exist.

## 1. Mandatory first action: repository reconnaissance
Before creating, moving or rewriting code, inspect the actual checkout and report:
1. Repository root, Git status and branch.
2. Whether a Unity project exists; locate Assets/, Packages/manifest.json, ProjectSettings/ProjectVersion.txt and .asmdef files.
3. Unity/editor version, packages, input/UI/render pipeline and platform assumptions.
4. Existing C# source, scenes, prefabs, ScriptableObjects, tests, CI and build configuration.
5. Asset folders and content import/loading conventions.
6. CSV/JSON catalogs, validators and legacy ID overlap.
7. Which acceptance criteria are already satisfied, partial or absent, with file evidence.

Do not assume a conventional Unity root exists. If absent, report it and propose the smallest explicit bootstrap plan before creating one. Do not create a second Unity project beside an existing one.

Deliver a concise RECONNAISSANCE_REPORT.md (or update project status) with evidence, risks and a proposed first milestone. Do not begin broad implementation before this report.

## 2. Source-of-truth hierarchy
Read docs/LOCAL_LLM_KNOWLEDGE_PACK.md, then:
- docs/architecture/GAME_ARCHITECTURE.md
- docs/NARRATIVE_CANON.md
- docs/IMPLEMENTATION_SPEC.md
- docs/architecture/R1_R15_STRUCTURAL_GAMEPLAY_CHECKPOINT.md
- implementation_spec/README.md
- implementation_spec/IMPLEMENTATION_RULES.md
- implementation_spec/INTEGRATION_CONTRACTS.md
- implementation_spec/CORE_MODEL.md
- implementation_spec/DATA_MODEL.md
- implementation_spec/CONTENT_CONTRACTS.md
- implementation_spec/COMBAT.md
- implementation_spec/TURN_RESOLUTION.md
- implementation_spec/STATUS_EFFECTS.md
- implementation_spec/SKILL_CATALOG.md
- docs/systems/combat/SKILLS_AUDIT.md
- docs/FULL_GAME_CONTENT_LOCK.md
- all three data/content/*.json catalogs
- docs/vertical_slice/UNITY_IMPLEMENTATION_HANDOFF.md
- all Act I vertical-slice docs and JSON datasets
- docs/characters/CHARACTER_BIBLE.md, ALLIES_ROSTER.md and NPCS_DESIGN.md
- docs/art/CHARACTER_IMAGE_PROMPTS.md and CHARACTER_EROTIC_CG_MATRIX.md before art-facing work.

Use docs/GDD_INDEX.md to locate other domain specs. Read detailed files relevant to the current milestone; do not dump every large JSON into every prompt if the coding environment can inspect files on demand.

### Conflict policy
Architecture governs high-level boundaries; narrative canon governs story truth; system specifications/contracts govern mechanics; Full Game Content Lock governs concrete scope, identities and narrative beats; structured data governs stable IDs and exact records; specialized character/art/slice docs govern their details. Archive docs are historical only. If active sources conflict, stop, cite exact paths/sections/IDs, propose the smallest correction and update the canonical source before coding around it. Never invent a third version.

## 3. Engineering architecture
Dependency direction:
Unity Presentation → Application Use Cases → Domain Rules.
Infrastructure implements repository, clock, RNG, save, content and event interfaces.

- Domain: plain C# entities/value objects, invariants and deterministic state transitions; no UnityEngine, scene/UI, file storage or service-locator calls.
- Application: use cases/orchestration such as dialogue choice, encounter resolution, reward application, facility construction, assignment, Expedition and save/load.
- Infrastructure: JSON parsing, validation, repositories, persistence, clock/RNG adapters, logging and typed event bus.
- Presentation: MonoBehaviours/UI collect input, invoke application use cases and render state; never own duplicate gameplay truth.

SOLID expectations: one responsibility per type/service; avoid a God-object GameManager; prefer composition and narrow interfaces; use interfaces where they provide a meaningful test/substitution seam, not for every class.

Service locator is permitted only at the composition/bootstrap boundary with explicit registration and fail-fast diagnostics. Prefer constructor injection inside Domain/Application. Locator resolves services but does not own gameplay state. Provide a test composition root with fakes/in-memory implementations.

Event bus rules: use typed immutable events for committed facts (QuestStageCompleted, ResourceChanged, EncounterResolved, FacilityBuilt, ExpeditionResolved). Commit canonical mutations and derived state before publishing. Events are not commands or queries. Define subscription disposal/lifetime and deterministic handler order.

## 4. Content/data pipeline
1. Load content from explicit configured locations.
2. Validate JSON/schema, required fields, stable-ID uniqueness, enums, supported effect types and every cross-reference.
3. Diagnostics must identify file, record ID and field.
4. Do not start a new game if mandatory content is invalid.
5. Separate immutable definitions, mutable save state and transient runtime state.
6. Store stable IDs, not labels/localized strings/scene names/array indices, in saves and links.
7. Keep localization/presentation text separate from mechanical definitions.
8. Do not overwrite legacy CSV catalogs until migration is mapped and reviewed.
9. Keep validation runnable outside Unity where practical and run it in CI.

Existing validation entry points:
- tools/validate_skill_catalog.py
- tools/validate_full_game_content.py
- tests/test_skill_catalog.py
- tests/test_full_game_content.py
- .github/workflows/skill-catalog-validation.yml

These tools/tests are authored; their existence does not imply they have passed. Run and report actual results.

## 5. Implementation phases

### Phase 0 — Reconnaissance and plan
Deliver the report in section 1. Avoid broad code changes.

### Phase 1 — Data/bootstrap foundation
- Confirm project root and Unity/editor compatibility.
- Run validators and tests; fix defects in small commits.
- Add schema/reference checks if gaps remain.
- Establish content-loading boundary and actionable diagnostics.
- Establish bootstrap/composition root, logging and test composition root.
- Establish domain/application/infrastructure/presentation boundaries using existing project conventions.
Acceptance: content loads and validates; invalid content fails clearly; domain logic is testable without scene setup; tests run in CI.

### Phase 2 — Persistent state, time, resources and quest state
- Implement canonical state containers, stable-ID repositories and versioned save/load.
- Process intermediate timestamps chronologically; equal timestamps use explicit priority.
- Implement atomic resource transactions and unlimited-capacity inventory.
- Implement quest graph, objective progress, flags, dialogue outcomes and idempotent rewards.
- Preserve aliases VS1_Q01–VS1_Q11 alongside Q01–Q11 until migration is explicitly approved.
Acceptance: deterministic quest/resource rules; reload restores canonical state; reward replay cannot grant twice.

### Phase 3 — Dialogue and exploration
- Implement content-driven dialogue nodes, choices, conditions and effects.
- Implement Brackenford/Ashfen Verge navigation, local POIs, travel time and encounter triggers.
- Never use display text as dialogue ID or choice-state key.
Acceptance: Act I progresses through quest/dialogue state, not scene-specific hardcoded progression.

### Phase 4 — Combat and effects
- Implement deterministic turn lifecycle/action-resolution pipeline.
- Implement targeting, resource checks, ordered effects, status duration/stacking, reactions, thresholds, encounter objectives and outcome policies.
- Implement enemy intent and explicit AI fallback.
- Combat objectives cannot always resolve by reducing Vitality alone; support retreat/partial outcomes where specified.
Acceptance: EditMode/unit tests cover lifecycle, effect timing, stacking, resource rejection, target invalidation, deterministic RNG and terminal state; PlayMode tests cover Unity wiring.

### Phase 5 — Community, facilities, assignments and Expeditions
- Implement facility construction, costs and upgrades from data.
- Implement member availability, one primary assignment per member, aptitude/progression and interruption rules.
- Implement autonomous NPC-only Expedition checkpoints/outcomes. Assigned allies cannot join the active party until return.
- Basic assignments and Expeditions unlock after Act I regardless of initial facility. Coordination Board adds CAPABILITY_EXPEDITION_OVERVIEW/visibility, not the basic unlock.
Acceptance: resource transactions are atomic; assignments respect availability; Expedition outcomes are deterministic/testable.

### Phase 6 — Integrated Act I vertical slice
Working title: The Water We Share. Hub Brackenford; region Ashfen Verge; manifestation The Red Thread; Mara Venn is irrigation keeper and seed-reserve steward.

End-to-end flow:
1. Meet a person in need.
2. Investigate water allocation and Ferida signs.
3. Prepare and resolve encounters.
4. Make a costly collective decision.
5. Persist community/resource/quest consequences.
6. Recognize Alya as leader and choose one initial facility.
7. Launch and resolve the first autonomous Expedition.

Mandatory outcome: lower-terrace seed reserve and a substantial part of next planting cycle are lost; Brackenford survives and downstream channel is secured. No optional path removes both costs. The Organization remains nuanced; the Ferida amplifies existing problems rather than causing every injustice.

Starting resources, material gates and effects are specified in vertical-slice JSON/docs. Preserve mandatory repair feasibility; optional crafting cannot consume reserved materials. Do not remove the mandatory loss to simplify code.

Acceptance: all 11 Act I stages traversable; choices cause intended state changes; objective combat/partial resolution works; facility choice persists; Expedition completes; save/load works; integration tests pass.

### Phase 7 — Production hardening
- Complete file-level asset registry and map existing assets before large-scale generation.
- Finalize remaining dialogue, exact rewards, encounter tuning, facility costs/upgrades and economy rates.
- Resolve localization/base language, accessibility/settings, audio event mapping and production QA.
- Run CI, integration tests, PlayMode tests, build verification and structured playtest; record actual results.
- Expand Acts II–V using the validated data/workflow patterns; do not create new architecture per act.

## 6. Non-negotiable game invariants
- Alya is fixed protagonist; standard direct party is Alya plus one ally unless narrative exception.
- Sidequests require Alya; Expeditions are delegated NPC/community activities.
- NPCs do not act in combat as NPCs; use separate Enemy/Boss records if needed.
- Inventory has no fixed capacity limit; no tactical grid or independent range system.
- Initiative order is stable after encounter-start randomization.
- Surrendered and Incapacitated are separate; neither acts; both count toward combat termination.
- Effects/time processing are deterministic, ordered and data-driven.
- Equipment removal immediately removes effects sourced only by that equipment.
- First facility choice does not gate basic assignments/Expeditions.
- Act I seed-reserve loss is mandatory.
- No main-path softlocks from optional costs or content.
- Do not redesign skills during integration plumbing; preserve semantics and report genuine conflicts.
- Adult scenes are optional, adult-only, consent-aware, and never gate main plot/endings.

## 7. Test and reporting contract
For each milestone, add/update tests alongside behavior. Use unit/EditMode tests for deterministic domain rules, integration tests for system contracts, and a small number of PlayMode tests for Unity wiring. Use fake clock/RNG, in-memory repositories and a test composition root where useful.

Report exact commands, exit codes and results. Never claim CI, Unity compilation, runtime behavior or tests passed unless actually executed. Avoid unrelated mass refactors. Preserve a clean working tree where possible and use small, understandable commits.

Every milestone report must contain:
1. What changed and why.
2. Files changed.
3. Decisions made/deferred.
4. Tests/validators actually run and results.
5. Known gaps/risks.
6. Next smallest task.

## 8. First task prompt (copy into the coding LLM)
Read docs/LOCAL_LLM_KNOWLEDGE_PACK.md and this handoff. Inspect the entire local repository without making broad changes. Determine whether a Unity project exists and where; identify editor/package versions, code conventions, systems, content loaders, tests and CI. Run the existing validators/tests if possible, recording exact output. Compare the current state against Phase 0/1 and the vertical-slice handoff. Return a reconnaissance report with evidence, risks, files to touch and a small implementation plan. Do not create a second Unity root, invent design rules or claim tests passed without running them. Stop after the report and proposed first milestone.
