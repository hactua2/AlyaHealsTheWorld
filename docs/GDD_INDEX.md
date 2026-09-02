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
8. `docs/archive/` — historical material only; never overrides current sources.

## GDD structure

| Section | Intended source | Status |
|---|---|---|
| 00 Game Overview | `docs/architecture/GAME_ARCHITECTURE.md` | CLOSED |
| 01 Design Pillars | Architecture / narrative | CLOSED |
| 02 Game Loop | Architecture | CLOSED |
| 03 World | `docs/systems/world/` + data | CONTENT/SPEC DETAIL NEEDED |
| 04 Narrative | `docs/NARRATIVE_CANON.md` + narrative implementation docs | CANON CLOSED / CONTENT NEEDED |
| 05 Characters | `docs/systems/characters/` + `docs/characters/ALLIES_ROSTER.md` + `docs/characters/NPCS_DESIGN.md` | **ALLY ROSTER LOCKED / NPC MODEL LOCKED / NPC ROSTER CONTENT NEEDED** |
| 06 Combat | `docs/systems/combat/` + implementation contracts | RULES CLOSED / CONTENT NEEDED |
| 07 Skills | `docs/systems/combat/SKILLS_AUDIT.md` + skill data | STRUCTURE CLOSED / CONTENT LOCK PENDING |
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
Complete game content catalog and dependency graph closed. **PENDING — CURRENT PHASE.** C3 recruitable ally roster is conceptually locked; C4 NPC model is conceptually locked; the concrete NPC roster is the next active content-lock pass.

### Checkpoint D — Production Complete
Implementation, UI, art, audio, localization, persistence, and QA requirements closed for every planned content item. **PENDING.**

## Content/data principle

The GDD should explain what the game means and how it behaves. Large concrete catalogs should remain in structured data where practical. Stable IDs must connect narrative, systems, data, UI, assets, and QA.

## Current planning-to-production boundary

Core gameplay rules and implementation contracts are closed. Remaining work is primarily content lock and production specification: roster completeness, concrete content definitions, asset requirements/dependencies, narrative content, UI presentation, audio, localization, accessibility and QA requirements.

The recruitable ally roster is conceptually closed in `docs/characters/ALLIES_ROSTER.md`. NPC structure and the relevance/H-tier model are conceptually closed in `docs/characters/NPCS_DESIGN.md`. Numerical stats, exact skills, AI parameters, operational recruitment scripting, detailed H-content implementation and final asset IDs remain downstream specifications and should not be confused with open roster decisions.

## Maintenance rule

Whenever a planning decision is finalized, update the relevant domain source first and then update this index/audit status. Historical batch logs are secondary context only and must not become competing sources of truth.
