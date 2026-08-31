# Alya Heals the World — Master Planning Audit

## Purpose

This is the master checklist for reaching **Planning Complete**: the point at which the game's design and content specification are sufficiently closed that implementation/production can proceed without requiring new major design decisions.

This document consolidates the current architecture, narrative canon, R1–R15 checkpoint, Skills Audit, existing structured data, and subsequent planning decisions. It is a planning-status document, not a replacement for domain-specific source-of-truth documents.

## Planning Completion Standard

A domain is **CLOSED** only when a competent implementer can execute it without making a material design decision on the project's behalf.

Statuses:
- **CLOSED** — final decision is established and documented.
- **SPECIFICATION NEEDED** — macro decision exists, but deterministic rules/contracts are missing.
- **CONTENT NEEDED** — system is specified enough structurally, but the complete content set is missing.
- **DEPENDENCY** — cannot be closed until another domain is resolved.
- **OPTIONAL** — deliberately deferred and not required for the base game.
- **OPEN DECISION** — a genuine design choice remains unresolved.

## Gate Model

### Checkpoint A — Architecture Complete
**STATUS: COMPLETE**

The macro architecture is closed. R1–R15 and convergence decisions are closed; `GAME_ARCHITECTURE.md` is the current high-level source of truth.

### Checkpoint B — Rules Complete
**STATUS: NEXT**

All core systems have deterministic rules, state transitions, formulas, interfaces, and edge-case behavior.

### Checkpoint C — Content Complete
**STATUS: NOT STARTED AS A FORMAL GATE**

Every planned region, character, enemy, item, building, quest, encounter, resource, vendor, and narrative sequence exists in the content specification.

### Checkpoint D — Production Complete
**STATUS: NOT STARTED AS A FORMAL GATE**

Every content/system requirement has implementation, UI, art, audio, localization, save, and QA requirements defined.

---

# 1. Master Domain Audit

| # | Domain | Status | Current basis | Remaining work | Gate |
|---|---|---|---|---|---|
| 1 | Game identity / pillars | CLOSED | Architecture + prior decisions | None unless implementation exposes contradiction | A |
| 2 | Core gameplay loop | CLOSED | Architecture + R1–R15 | None | A |
| 3 | World structure | SPECIFICATION NEEDED | Regions and procedural/hand-authored split decided | Final world graph, region rules | B/C |
| 4 | Narrative canon | CLOSED | `NARRATIVE_CANON.md` | Content implementation still needed | A |
| 5 | Narrative implementation | CONTENT NEEDED | Canon establishes macro arcs | Scene/quest/flag graph | C |
| 6 | Character architecture | CLOSED | Population/ally architecture | Concrete roster and data | A/C |
| 7 | Character content | CONTENT NEEDED | Existing character CSV + architecture | Final roster, stats, skills, arcs, recruitment, assets | C |
| 8 | Enemy architecture | CLOSED | Family/role/power/encounter/narrative separation | Concrete data | A/C |
| 9 | Enemy content | CONTENT NEEDED | Existing enemy CSV + architecture | Final roster, AI, stats, drops, variants | C |
| 10 | Combat rules | SPECIFICATION NEEDED | Skills Audit + architecture | Turn, targeting, formulas, intent, victory, edge cases | B |
| 11 | Status/effects | SPECIFICATION NEEDED | Existing lifecycle decisions | Formal effect contract, stacking, timing, cleansing | B |
| 12 | Skills | SPECIFICATION NEEDED | `SKILLS_AUDIT.md` | Final skill schema, formulas, costs, targeting, acquisition, balance | B/C |
| 13 | Equipment/items | SPECIFICATION NEEDED | Item CSV + architecture | Schema, complete catalog, acquisition, evolution, transmutation hooks | B/C |
| 14 | Curses/blessings | SPECIFICATION NEEDED | Architecture decisions | Exact progression/state rules and content | B/C |
| 15 | Recruitment | SPECIFICATION NEEDED | Recruitment architecture | Exact eligibility conditions and transitions | B |
| 16 | Rehabilitation/integration | SPECIFICATION NEEDED | Architecture + mechanics CSV | Facility/process states, requirements, outcomes | B/C |
| 17 | Community architecture | CLOSED | R1–R15 + architecture | None at macro level | A |
| 18 | Buildings/facilities | CONTENT NEEDED | Architectural rules | Final building catalog, costs, upgrades, effects | C |
| 19 | Assignments/aptitude | SPECIFICATION NEEDED | Aptitude decisions | Formula, output, progression, edge cases | B |
| 20 | Resources | SPECIFICATION NEEDED | Resource/ecology architecture | Resource taxonomy, acquisition, rates, sinks | B/C |
| 21 | Economy/trade | SPECIFICATION NEEDED | Economy architecture | Prices, inventories, refresh, reward curves | B/C |
| 22 | Ecology/production | SPECIFICATION NEEDED | Architecture | Production cycles, renewable/unique rules | B/C |
| 23 | Exploration | SPECIFICATION NEEDED | Procedural/hand-authored split | Expedition flow, generation rules, persistence | B |
| 24 | Encounters | SPECIFICATION NEEDED | Encounter hierarchy | Encounter schema, generation, resolution | B |
| 25 | Quests | SPECIFICATION NEEDED | Quest taxonomy | Quest state machine/schema | B |
| 26 | Quest content | CONTENT NEEDED | Narrative canon + quest architecture | Full quest graph and data | C |
| 27 | Time/day-night | SPECIFICATION NEEDED | Simple cycle decided | Exact transitions, assignment ticks, waiting | B |
| 28 | Defeat/recovery | SPECIFICATION NEEDED | Retreat/consequence model | Exact secured rewards, recovery, edge cases | B |
| 29 | Progression | SPECIFICATION NEEDED | Main Quest as principal gate | XP/levels, unlock curves, power bands | B/C |
| 30 | Information architecture | SPECIFICATION NEEDED | Discover→available→explain→depth | Screen-level information flows | B/D |
| 31 | UX/UI | CONTENT NEEDED | IA principles | Screen inventory, wireframes, interaction contracts | C/D |
| 32 | Save/persistence | SPECIFICATION NEEDED | Not yet fully formalized | Persistence model and save boundaries | B/D |
| 33 | Art direction | SPECIFICATION NEEDED | Existing AI/reference assets | Art bible, asset standards, pipeline | D |
| 34 | Audio | SPECIFICATION NEEDED | Existing/legacy audio assets | Audio bible, event mapping, pipeline | D |
| 35 | Localization | OPEN DECISION | Not formally closed | Base language, string architecture, scope | D |
| 36 | Accessibility/settings | OPEN DECISION | Not formally closed | Required options and accessibility targets | D |
| 37 | Technical implementation contracts | SPECIFICATION NEEDED | Repository architecture principles | Data schemas, interfaces, state ownership | B/D |
| 38 | QA/testing | SPECIFICATION NEEDED | Not formally closed | Acceptance tests and regression strategy | D |
| 39 | Tutorial/onboarding | CONTENT NEEDED | Narrative entry and community introduction established | First-session flow and teaching beats | C/D |
| 40 | Release/publishing | OPTIONAL / LATER | Outside core design | Platform/store/release decisions | Post-D |

---

# 2. Decisions Explicitly Closed

These should not be reopened casually:

- Alya is the fixed protagonist.
- Standard expedition structure is Alya + one selected ally, with narrative exceptions.
- The game loop interconnects narrative, exploration, combat, resources, community, and progression.
- Main Quest is the principal structural progression gate.
- Regions remain relevant after unlock where appropriate.
- Procedural generation is used for repeatable exploration/gathering/selected reusable quests; handcrafted maps are reserved for places where authored design adds value.
- Community construction can be destroyed or relocated.
- Assignment experience persists permanently.
- Combat-capable recruited entities enter through eligibility followed by rehabilitation/integration rather than instant membership.
- Cursed equipment can be removed through dedicated community infrastructure but remains cursed and can later be voluntarily re-equipped.
- The primary stat layer contains exactly eight mechanical attributes: Body, Agility, Soul, Charm, Dominance, Submission, Sadism, Masochism.
- Enemy power/progression band, encounter class, and narrative role are separate dimensions; the old mixed Tier terminology is deprecated.
- Encounter hierarchy is Normal → Elite → Mini-Boss → Boss.
- Victory distinguishes Kill, Knockout, Capture, Submission, Escape, and Objective Complete.
- Time uses a simple explicit day/night cycle; waiting is allowed in safe locations; permanent time pressure is exceptional.
- Defeat primarily uses retreat/consequence rather than generic Game Over or systemic permadeath.
- Information is progressively revealed using discover → make available → explain → reveal additional depth.
- New macro-systems require a demonstrated structural gap.

---

# 3. Known Deliberate Deferrals

These are not accidental gaps and should remain out of scope unless later evidence requires them:

1. General expedition fatigue/escalating risk.
2. Specialized non-combat encounter archetypes such as pursuit/survival.
3. Alternate narrative versions of bosses.
4. Detailed farming simulation.
5. Separate adult economy/inventory.
6. Separate sexual crafting subsystem.
7. Recurring Wound currency.
8. Duplicate combat currencies.
9. Universal enemy scaling.
10. Excessive building proliferation.

---

# 4. Critical Dependencies for Checkpoint B

Checkpoint B should proceed in this order:

1. Combat state model and turn lifecycle.
2. Targeting and action resolution.
3. Health/H-gauge and damage formulas.
4. Core combat resources: Control, Surrender, Cruelty, Endurance.
5. Status/effect lifecycle and stacking.
6. Enemy Intent and AI contract.
7. Victory/defeat/escape/capture resolution.
8. Skill implementation schema and resolution contract.
9. Equipment-derived effects and curse/blessing hooks.
10. Recruitment eligibility → rehabilitation handoff.
11. Encounter contract.
12. Exploration/expedition contract.
13. Community assignment/time contracts where combat dependencies exist.

The purpose is to close interfaces, not to balance every content entry immediately.

---

# 5. Content Completion Checklist

Before Checkpoint C can be declared complete, the project must have closed catalogs for:

- [ ] Main Quest graph
- [ ] Regional Quest graph
- [ ] Character Quest graph
- [ ] Handcrafted Sidequests
- [ ] Reusable/Procedural Tasks
- [ ] Alya final progression
- [ ] Major ally roster
- [ ] Specialized resident roster
- [ ] Generic worker rules
- [ ] Recruitable combat entities
- [ ] Enemy roster
- [ ] Boss roster
- [ ] Region/world graph
- [ ] Encounter tables
- [ ] Skills
- [ ] Passives
- [ ] Equipment
- [ ] Consumables
- [ ] Resources/components
- [ ] Recipes/transmutation definitions
- [ ] Buildings/facilities
- [ ] Production chains
- [ ] Vendors/inventories
- [ ] Rewards/drop tables
- [ ] Narrative scenes/dialogues
- [ ] Choices/flags/consequences
- [ ] Endings

---

# 6. Production Completion Checklist

Before Checkpoint D can be declared complete, every implemented content item must have:

- [ ] stable ID
- [ ] implementation specification
- [ ] data schema entry
- [ ] acquisition/unlock conditions
- [ ] UI presentation requirement
- [ ] art requirement
- [ ] audio requirement, if applicable
- [ ] localization strings, if applicable
- [ ] save/persistence behavior, if applicable
- [ ] QA acceptance cases

---

# 7. Working Rule Going Forward

We should stop asking "what other systems could the game have?" unless a real gap appears.

The default question is now:

> **Which existing system/interface owns this requirement, and is that interface specified tightly enough to implement it?**

A proposed new mechanic must identify the gap it solves and why existing systems cannot solve it through content, configuration, specialization, or extension.

## Current verdict

**Checkpoint A: COMPLETE**

**Checkpoint B: NEXT — Rules Complete**

**Checkpoint C: PENDING — Content Complete**

**Checkpoint D: PENDING — Production Complete**
