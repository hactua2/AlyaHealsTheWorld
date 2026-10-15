# Alya Heals the World — GDD Index

## Purpose
This file is the reference map for the eventual complete Game Design Document. It deliberately keeps the GDD modular: high-level decisions live in architecture, system behavior lives in `docs/systems/`, implementation contracts live in `docs/implementation/`, canonical narrative lives in `docs/NARRATIVE_CANON.md`, and concrete content lives in `data/` or dedicated content documents.

The GDD is considered complete when every required domain points to a current source-of-truth document and that document is closed at the relevant planning checkpoint.

## Authority hierarchy
1. `docs/architecture/GAME_ARCHITECTURE.md` — high-level architecture.
2. `docs/NARRATIVE_CANON.md` — canonical narrative.
3. `docs/systems/` — current system behavior and cross-system rules.
4. `docs/implementation/` — implementation-facing contracts.
5. `data/` — structured concrete content.
6. `docs/characters/` and other dedicated content documents — canonical content definitions where a structured table alone is insufficient.
7. `assets/` — visual/reference assets.
8. `docs/archive/` — historical material only; never overrides current sources of truth.

## GDD structure

| Section | Intended source | Status |
|---|---|---|
| 00 Game Overview | `docs/architecture/GAME_ARCHITECTURE.md` | CLOSED |
| 01 Design Pillars | Architecture / narrative | CLOSED |
| 02 Game Loop | Architecture | CLOSED |
| 03 World | `docs/systems/world/` + data | CONTENT/SPEC DETAIL NEEDED |
| 04 Narrative | `docs/NARRATIVE_CANON.md` + narrative implementation docs | CANON CLOSED / CONTENT NEEDED |
| 05 Characters | `docs/characters/CHARACTER_BIBLE.md` + `docs/characters/ALLIES_ROSTER.md` + `docs/characters/NPCS_DESIGN.md` | CHARACTER BIBLE LOCKED / DOWNSTREAM DATA & PRODUCTION NEEDED |
| 06 Combat | `docs/systems/combat/` + implementation contracts | RULES CLOSED / CONTENT NEEDED |
| 07 Skills | `docs/systems/combat/SKILLS_AUDIT.md` + skill data | NORMALIZED CATALOG BASELINE CREATED / RUNTIME & BALANCE QA PENDING |
| 08 Status Effects | `docs/systems/combat/` + implementation contracts | RULES CLOSED / CONTENT NEEDED |
| 09 Enemies | `docs/systems/combat/` + `data/enemies/` | ARCHITECTURE CLOSED / CONTENT LOCK PENDING |
| 10 Items | `docs/systems/items/` + `data/items/` | RULES CLOSED / CONTENT LOCK PENDING |
| 11 Economy | `docs/systems/economy/` | RULES CLOSED / CONTENT/SPEC DETAIL NEEDED |
| 12 Resources | `docs/systems/resources/` | RULES CLOSED / CONTENT NEEDED |
| 13 Buildings | `docs/systems/community/` | RULES CLOSED / CONTENT NEEDED |
| 14 Community | `docs/systems/community/` | RULES CLOSED / CONTENT NEEDED |
| 15 Exploration | `docs/systems/exploration/` | RULES CLOSED / CONTENT NEEDED |
| 16 Quests | `docs/systems/quests/` | RULES CLOSED / CONTENT NEEDED |
| 17 Progression | `docs/systems/progression/` | RULES CLOSED / CONTENT NEEDED |
| 18 Time | `docs/systems/time/` | RULES CLOSED / CONTENT NEEDED |
| 19 Recruitment | `docs/systems/recruitment/` | RULES CLOSED / CONTENT NEEDED |
| 20 Rehabilitation | `docs/systems/recruitment/` or community docs | RULES CLOSED / CONTENT NEEDED |
| 21 Transmutation | `docs/systems/items/` / resources docs | RULES CLOSED / CONTENT NEEDED |
| 22 Information Architecture | `docs/systems/ux/` | CONTENT/SPEC DETAIL NEEDED |
| 23 UI/UX | `docs/systems/ux/` | CONTENT NEEDED |
| 24 Save/Persistence | `docs/systems/persistence/` + implementation contracts | RULES CLOSED / IMPLEMENTATION NEEDED |
| 25 Audio | `docs/audio/` | PRODUCTION SPEC NEEDED |
| 26 Art Direction | `docs/art/` | PRODUCTION SPEC NEEDED |
| 27 Localization | `docs/localization/` | OPEN DECISION |
| 28 Accessibility | `docs/systems/ux/` | OPEN DECISION |
| 29 Implementation Contracts | `docs/implementation/` | CLOSED FOR CURRENT CORE SCOPE |
| 30 QA / Definition of Done | `docs/qa/` | PRODUCTION SPEC NEEDED |

## Completion gates

### Checkpoint A — Architecture Complete
Macro architecture closed. **COMPLETE.**

### Checkpoint B — Rules Complete
Deterministic rules, formulas, state transitions, edge cases, and system interfaces closed. **COMPLETE.**

### Implementation Specification I1–I11
Implementation-facing contracts established. **COMPLETE.**

### I12 — Cross-System Integration Audit
Cross-system ordering, state composition, transactions, time advancement, determinism, AI fallback and source-of-truth boundaries audited. **COMPLETE.**

### Checkpoint C — Content Complete
Full-game base content catalog and dependency graph authored in `docs/FULL_GAME_CONTENT_LOCK.md` and three stable-ID catalogs under `data/content/`. **CONTENT LOCK BASELINE AUTHORED; FORMAL GATE VALIDATION PENDING.** The catalog defines 5 acts, 47 main quest stages, 25 authored sidequests, 7 regions, 10 allies, 21 named NPCs, 12 reusable NPC templates, 35 enemy archetypes, 9 major bosses, 8 special encounters, 12 facilities, 8 resources, 36 canonical items, 8 outfits, 8 Expedition templates, and 5 ending families. Existing skills catalog remains 67 canonical records. Static JSON parsing and duplicate-ID checks passed; cross-system implementation, legacy data reconciliation, dialogue/asset mapping and content QA remain.

### Checkpoint D — Production Complete
Implementation, UI, art, audio, localization, persistence, and QA requirements closed for every planned content item. **PENDING.**

## Content/data principle
The GDD should explain what the game means and how it behaves. Large concrete catalogs should remain in structured data where practical. Stable IDs must connect narrative, systems, data, UI, assets, and QA.

## Current planning-to-production boundary
Core gameplay rules and implementation contracts are closed. Remaining work is primarily content lock and production specification: concrete content definitions, asset requirements/dependencies, narrative content, UI presentation, audio, localization, accessibility and QA requirements.

The recruitable ally roster is conceptually closed in `docs/characters/ALLIES_ROSTER.md`. NPC structure and the relevance/H-tier model are conceptually closed in `docs/characters/NPCS_DESIGN.md`. `docs/characters/CHARACTER_BIBLE.md` consolidates the locked character identity rules and concrete Named NPC roster. Numerical stats, exact skills, AI parameters, operational recruitment scripting, detailed H-content implementation and final asset IDs remain downstream specifications.

## Current project orientation and production references
- `docs/PROJECT_STATE_AND_ROADMAP.md` — current project summary, canon, locked decisions, remaining work and recommended next sequence.
- `docs/VERTICAL_SLICE_SCOPE.md` — approved scope baseline, content budget, narrative requirements, exclusions, dependencies and acceptance criteria for the first Act I vertical slice.
- `docs/vertical_slice/ACT_I_QUEST_GRAPH.md` and `docs/vertical_slice/ACT_I_QUEST_GRAPH_CONTINUATION.md` — authored Act I quest graph, choice/state consequences, climax objective, leadership transition and first Expedition.
- `docs/vertical_slice/ACT_I_DIALOGUE_PACK.md` — first-pass dialogue anchors and choice labels for the vertical slice.
- `docs/vertical_slice/ACT_I_CONTENT_CATALOG.md` — human-readable content decisions, enemy/encounter roles, resource/facility economy and implementation gate.
- `docs/vertical_slice/UNITY_IMPLEMENTATION_HANDOFF.md` — Unity implementation handoff for an implementation LLM: SOLID boundaries, service locator/event bus guardrails, content validation, system responsibilities, persistence, tests, implementation phases, and acceptance criteria.\n- `docs/FULL_GAME_CONTENT_LOCK.md` — canonical full-game content lock: five-act arc, 47 main quest stages, regions, factions, character arcs, enemy/boss roster, facilities, resources, items, sidequests, Expeditions, outfits, and endings.\n- `data/content/full_game_world_catalog.json` — stable-ID acts, regions, factions, main quests, sidequests, Expedition templates, and ending families.\n- `data/content/full_game_gameplay_catalog.json` — stable-ID enemies, bosses, special encounters, facilities, resources, items, and Alya outfits.\n- `data/content/full_game_character_arcs.json` — locked ally/NPC arcs, 12 generic NPC templates, and relationship clusters.
- `data/vertical_slice/act_i_quests.json` and `data/vertical_slice/act_i_content.json` — structured stable-ID quest and content data; numeric values are provisional pending runtime integration and balance QA.
- `data/vertical_slice/act_i_effects.json` — slice-specific choice effects, conditional costs, and encounter modifiers mapped to deterministic handlers.
- `docs/art/CHARACTER_IMAGE_PROMPTS.md` — full-body character reference prompts and generation guidance.
- `docs/art/CHARACTER_EROTIC_CG_MATRIX.md` — first-pass situations and CG beats for 31 adult characters; non-graphic direction, not a final asset/unlock specification.

## Maintenance rule
Whenever a planning decision is finalized, update the relevant domain source first and then update this index/audit status. Historical batch logs are secondary context only and must not become competing sources of truth.

## Skills audit update — Pass 2

The skill architecture remains closed; the concrete catalog remains unlocked. The current skill sources are:
- `docs/systems/combat/SKILLS_AUDIT.md` — approved meter migration, P-growth capability, and cluster consolidation decisions.
- `docs/systems/combat/SKILL_CATALOG_RECONCILIATION_PASS_1.md` — initial row-by-row audit.
- `docs/systems/combat/SKILL_CATALOG_RECONCILIATION_PASS_2.md` — applied decisions and proposed mechanical disposition for 54 legacy rows plus fourteen additions.
- `docs/systems/combat/SKILL_CATALOG_RECONCILIATION_PASS_3.md` — thematic/function review of the highest-impact clusters: control, reactive defense, Strain/DoT/finishers, capabilities, passives, and economy.
- `docs/systems/combat/SKILL_CATALOG_SCALING_AUDIT.md` — per-skill proposed attributes, body-part scaling inputs, canonical effects, synergies, and distinct-identity rationale for 54 legacy skills plus 14 proposed additions.
- `docs/systems/combat/SKILL_CATALOG_RECONCILIATION_PASS_4.md` — focused single-target actions; updated with the owner's decisions on basic-attack identity, Spank/Bite channels, Flirt's hybrid role, explicit self-risk, AS Chain behavior, and H-job's Mind Aspect.
- `docs/systems/combat/SKILL_CATALOG_RECONCILIATION_PASS_5.md` — updated with the owner's decisions on distinct area actions, Summon c-s target-count scaling, Summon Tentacles friendly fire, Bkakke's all-target victory condition, merging Enslave/Absolute Control, and the three Overflow roles.
- `docs/systems/combat/SKILL_CATALOG_RECONCILIATION_PASS_6.md` — updated with seven owner decisions covering Bkakke failure risk, area-skill identities, Summon Tentacles affected sides, Overflow event frequency, Alya-only P-growth, attribute/Aspect composition, and H-job DoT identity.
- `docs/systems/combat/SKILL_CATALOG_RECONCILIATION_PASS_7.md` — eight semantic recommendations accepted by default, closing remaining skill-level decisions.
- `docs/systems/combat/SKILL_CATALOG_CONTENT_LOCK.md` — final semantic dispositions for all 54 named legacy entries and fourteen proposed additions; defines the production handoff and exit criteria.
- `implementation_spec/SKILL_CATALOG.md` — schema, meter migration, capability contract, and validation rules.
- `data/skills/skills.csv` — normalized primary catalog (67 canonical records); companion mechanics are in `data/skills/skill_definitions.json`.
- `docs/systems/combat/SKILL_CATALOG_PRODUCTION_HANDOFF.md` — migration summary, validation commands, and remaining release gate.
- `docs/systems/combat/SKILL_CATALOG_BALANCE_BASELINE.md` — provisional coefficients, costs, caps, progression, and required encounter scenarios.

Pass 3 recommends preserving action fantasy while separating it from mechanical identity; skills may share mechanical templates without being merged when their per-skill attribute scaling, body-part association, requirements, costs, synergies, or tactical hooks differ. The project owner confirmed that body-part affinity modifies skill effectiveness after the weighted primary-attribute contribution; multi-Aspect rules must be declared per skill. Control/outcome, reactive defense, AoE, and Overflow clusters continue through skill-level reconciliation.

The Scaling Audit proposes attributes, effects, synergies, and distinct-identity rationale for every named legacy skill and all fourteen proposed additions. Passes 4–6 reflect the owner's explicit decisions; Pass 7 recommendations are accepted by default. `SKILL_CATALOG_CONTENT_LOCK.md` closes semantic design for the legacy inventory and fourteen additions. The normalized CSV and companion definitions are now authored on the production branch; numeric values remain provisional and runtime integration plus encounter-level balance QA are still required.

Approved decisions: neutral implementation vocabulary is canonical; tiers represent both progression/unlock expectation and expected power; unlocks combine Skill Points, prerequisites, and progression gates; CSV is the primary catalog with companion definitions for complex mechanics; preserve themes but merge only genuine mechanical redundancy; H-gauge maps to Strain and Health Damage to Vitality damage subject to per-effect semantic validation; P-growth is a Capability/Transformation that enables dependent skills.
\n\n## Full-game content lock update — 2026-10-15\n\nThe first full-game content lock baseline is authored. It is a content/design closure, not a claim that the project is runtime- or release-complete. The canonical scope and stable-ID inventories are in `docs/FULL_GAME_CONTENT_LOCK.md` and `data/content/`. The catalog's 47 main quest stages supersede the earlier planning estimate of 45. Static JSON parsing and duplicate-ID checks passed on the three new JSON catalogs. Remaining work is a formal schema/reference validator, reconciliation of legacy CSV IDs, per-quest objective/reward/dialogue completion, exact numeric balance, and asset/localization/QA mapping.\n