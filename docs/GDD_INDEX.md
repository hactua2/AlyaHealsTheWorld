# Alya Heals the World — GDD Index

## Purpose

This file is the reference map for the eventual complete Game Design Document. It deliberately keeps the GDD modular: high-level decisions live in architecture, system behavior lives in `docs/systems/`, implementation contracts live in `docs/implementation/`, canonical narrative lives in `docs/NARRATIVE_CANON.md`, and concrete content lives in `data/` or dedicated content documents.

The GDD is considered complete when every required domain below points to a current source-of-truth document and that document is closed at the relevant planning checkpoint.

## Authority hierarchy

1. `docs/architecture/GAME_ARCHITECTURE.md` — high-level architecture.
2. `docs/NARRATIVE_CANON.md` — canonical narrative.
3. `docs/systems/` — current system behavior and cross-system rules.
4. `docs/implementation/` — implementation-facing contracts.
5. `data/` — structured concrete content.
6. `assets/` — visual/reference assets.
7. `docs/archive/` — historical material only; never overrides current sources.

## GDD structure

| Section | Intended source | Status |
|---|---|---|
| 00 Game Overview | `docs/architecture/GAME_ARCHITECTURE.md` | CLOSED |
| 01 Design Pillars | Architecture / narrative | CLOSED |
| 02 Game Loop | Architecture | CLOSED |
| 03 World | `docs/systems/world/` + data | SPECIFICATION NEEDED |
| 04 Narrative | `docs/NARRATIVE_CANON.md` + narrative implementation docs | CANON CLOSED / CONTENT NEEDED |
| 05 Characters | `docs/systems/characters/` + `data/characters/` | SPECIFICATION NEEDED / CONTENT NEEDED |
| 06 Combat | `docs/systems/combat/` | IN PROGRESS — B5–B8 CLOSED |
| 07 Skills | `docs/systems/combat/SKILLS_AUDIT.md` + skill data | STRUCTURE CLOSED / B5 CONTRACTS CLOSED / CONTENT NEEDED |
| 08 Status Effects | `docs/systems/combat/` | B4 CLOSED / FORMAL SPECIFICATION NEEDED |
| 09 Enemies | `docs/systems/combat/` + `data/enemies/` | ARCHITECTURE CLOSED / CONTENT NEEDED |
| 10 Items | `docs/systems/items/` + `data/items/` | B9 PARTIALLY CLOSED / SPECIFICATION + CONTENT NEEDED |
| 11 Economy | `docs/systems/economy/` | B16 MACRO CLOSED / SPECIFICATION NEEDED |
| 12 Resources | `docs/systems/resources/` | B16 MACRO CLOSED / SPECIFICATION NEEDED |
| 13 Buildings | `docs/systems/community/` | B15 MACRO CLOSED / CONTENT NEEDED |
| 14 Community | `docs/systems/community/` | B13–B15 MACRO CLOSED / SPECIFICATION NEEDED |
| 15 Exploration | `docs/systems/exploration/` | B17 MACRO CLOSED / SPECIFICATION NEEDED |
| 16 Quests | `docs/systems/quests/` | B18 MACRO CLOSED / SPECIFICATION NEEDED |
| 17 Progression | `docs/systems/progression/` | B10–B12 MACRO CLOSED / SPECIFICATION NEEDED |
| 18 Time | `docs/systems/time/` | B14 MACRO CLOSED / SPECIFICATION NEEDED |
| 19 Recruitment | `docs/systems/recruitment/` | SPECIFICATION NEEDED |
| 20 Rehabilitation | `docs/systems/recruitment/` or community docs | SPECIFICATION NEEDED |
| 21 Transmutation | `docs/systems/items/` / resources docs | SPECIFICATION NEEDED |
| 22 Information Architecture | `docs/systems/ux/` | SPECIFICATION NEEDED |
| 23 UI/UX | `docs/systems/ux/` | CONTENT NEEDED |
| 24 Save/Persistence | `docs/systems/persistence/` | SPECIFICATION NEEDED |
| 25 Audio | `docs/audio/` | SPECIFICATION NEEDED |
| 26 Art Direction | `docs/art/` | SPECIFICATION NEEDED |
| 27 Localization | `docs/localization/` | OPEN DECISION |
| 28 Accessibility | `docs/systems/ux/` | OPEN DECISION |
| 29 Implementation Contracts | `docs/implementation/` | SPECIFICATION NEEDED |
| 30 QA / Definition of Done | `docs/qa/` | SPECIFICATION NEEDED |

## Completion gates

### Checkpoint A — Architecture Complete
Macro architecture closed. **COMPLETE.**

### Checkpoint B — Rules Complete
Deterministic rules, formulas, state transitions, edge cases, and system interfaces closed. **IN PROGRESS.** B4–B18 macro decisions are consolidated; detailed contracts/formulas remain.

### Checkpoint C — Content Complete
Complete game content catalog and dependency graph closed. **PENDING.**

### Checkpoint D — Production Complete
Implementation, UI, art, audio, localization, persistence, and QA requirements closed for every planned content item. **PENDING.**

## Content/data principle

The GDD should explain what the game means and how it behaves. Large concrete catalogs should remain in structured data where practical. Stable IDs must connect narrative, systems, data, UI, assets, and QA.

## Maintenance rule

Whenever a planning decision is finalized, update the relevant domain source first and then update this index/audit status. Historical batch logs are secondary context only and must not become competing sources of truth.
