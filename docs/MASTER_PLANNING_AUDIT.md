# Alya Heals the World — Master Planning Audit

## Purpose

This is the master checklist for reaching **Planning Complete**: the point at which the game's design and content specification are sufficiently closed that implementation/production can proceed without requiring new major design decisions.

This document consolidates the current architecture, narrative canon, R1–R15 checkpoint, Skills Audit, existing structured data, and Checkpoint B decisions. It is a planning-status document, not a replacement for domain-specific source-of-truth documents.

## Planning Completion Standard

A domain is **CLOSED** when its design contract is decided. A domain may still require a later **implementation specification** (schemas, formulas, interfaces, exact state transitions, edge cases) or **content production** without reopening its design.

Statuses:
- **CLOSED** — design decision is established.
- **SPECIFICATION NEEDED** — design is closed, but the implementation contract still needs to be written.
- **CONTENT NEEDED** — system design is closed enough structurally, but the complete content set is missing.
- **DEPENDENCY** — cannot be completed until another domain is resolved.
- **OPTIONAL** — deliberately deferred and not required for the base game.
- **OPEN DECISION** — a genuine design choice remains unresolved.

## Gate Model

### Checkpoint A — Architecture Complete
**STATUS: COMPLETE**

The macro architecture is closed. R1–R15 and convergence decisions are closed; `GAME_ARCHITECTURE.md` is the current high-level source of truth.

### Checkpoint B — Rules Complete
**STATUS: COMPLETE**

B4–B18 and the Checkpoint B Mega-Batch closed the remaining macro gameplay decisions. Remaining work under domains marked **SPECIFICATION NEEDED** is implementation specification, not new design discovery: exact schemas, formulas, interfaces, deterministic lifecycle contracts, and edge cases must still be written before production implementation.

### Checkpoint C — Content Complete
**STATUS: NOT STARTED AS A FORMAL GATE**

Every planned region, character, enemy, item, building, quest, encounter, resource, vendor, and narrative sequence exists in the content specification.

### Checkpoint D — Production Complete
**STATUS: NOT STARTED AS A FORMAL GATE**

Every content/system requirement has implementation, UI, art, audio, localization, save, and QA requirements defined.

---

# 1. Master Domain Audit

| # | Domain | Status | Remaining work | Gate |
|---|---|---|---|---|
| 1 | Game identity / pillars | CLOSED | None unless implementation exposes contradiction | A |
| 2 | Core gameplay loop | CLOSED | None | A |
| 3 | World structure | CLOSED | Final world graph, region rules | C |
| 4 | Narrative canon | CLOSED | Content implementation | A/C |
| 5 | Narrative implementation | CLOSED | Scene/quest/flag graph | B/C |
| 6 | Character architecture | CLOSED | Concrete roster and data | C |
| 7 | Character content | CLOSED | Final roster, stats, skills, arcs, recruitment, assets | C |
| 8 | Enemy architecture | CLOSED | Concrete data | C |
| 9 | Enemy content | CLOSED | Final roster, AI, stats, drops, variants | C |
| 10 | Combat rules | CLOSED | Formal formulas, lifecycle, action queue/resolution, edge-case spec | B-spec |
| 11 | Status/effects | CLOSED | Formal effect contract, timing, stacking/cleanse edge-case spec | B-spec |
| 12 | Skills | CLOSED | Final data schema, formulas, costs, targeting, transformations, acquisition content | B-spec/C |
| 13 | Equipment/items | CLOSED | Final schema, transformation vocabulary, catalog, acquisition | B-spec/C |
| 14 | Curses/blessings | CLOSED | Exact state/progression specification and content | B-spec/C |
| 15 | Recruitment | CLOSED | Exact data contract and content | B-spec/C |
| 16 | Rehabilitation/integration | CLOSED | Facility/process state contract and content | B-spec/C |
| 17 | Community architecture | CLOSED | None at macro level | A |
| 18 | Buildings/facilities | CLOSED | Final building catalog, costs, upgrades, effects | C |
| 19 | Assignments/aptitude | CLOSED | Growth/competence/output formulas and edge-case spec | B-spec |
| 20 | Resources | CLOSED | Resource taxonomy, acquisition, rates, storage footprint, sinks | B-spec/C |
| 21 | Economy/trade | CLOSED | Prices, inventories, refresh, reward curves | B-spec/C |
| 22 | Ecology/production | CLOSED | Production cycles, renewable/unique rules | B-spec/C |
| 23 | Exploration | CLOSED | Sidequest vs Expedition contracts, travel, generation, persistence spec | B-spec/C |
| 24 | Encounters | CLOSED | Encounter schema, generation, resolution spec | B-spec/C |
| 25 | Quests | CLOSED | Quest state machine, objective semantics, trigger contract | B-spec/C |
| 26 | Quest content | CLOSED | Full quest graph and data | C |
| 27 | Time/day-night | CLOSED | Exact time blocks, ticks, waiting, day/night transitions | B-spec |
| 28 | Defeat/recovery | CLOSED | Exact post-combat/post-defeat resolution, recovery, edge cases | B-spec |
| 29 | Progression | CLOSED | XP/level curves, skill-point rules, natural growth formulas, power bands | B-spec/C |
| 30 | Information architecture | CLOSED | Screen-level information flows | B-spec/D |
| 31 | UX/UI | CLOSED | Screen inventory, wireframes, interaction contracts | C/D |
| 32 | Save/persistence | CLOSED | Persistence model, save boundaries, migration details | B-spec/D |
| 33 | Art direction | SPECIFICATION NEEDED | Art bible, asset standards, pipeline | D |
| 34 | Audio | SPECIFICATION NEEDED | Audio bible, event mapping, pipeline | D |
| 35 | Localization | OPEN DECISION | Base language, string architecture, scope | D |
| 36 | Accessibility/settings | OPEN DECISION | Required options and accessibility targets | D |
| 37 | Technical implementation contracts | CLOSED | Concrete schemas, interfaces, state ownership | B-spec/D |
| 38 | QA/testing | SPECIFICATION NEEDED | Acceptance tests and regression strategy | D |
| 39 | Tutorial/onboarding | CLOSED | First-session flow and teaching content | C/D |
| 40 | Release/publishing | OPTIONAL / LATER | Platform/store/release decisions | Post-D |

---

# 2. Checkpoint B — Final Closure Record

## Overall verdict

**CHECKPOINT B IS CLOSED.**

The Checkpoint B Mega-Batch completed the remaining macro gameplay decisions. No hard architectural contradiction was identified against the established architecture. The project can now move from **design discovery** to **implementation specification** without reopening the core gameplay model.

The batches B4–B18 remain useful as decision history, but the domain documents and this audit are the source of truth. Do not create separate B-batch documents unless a later audit specifically requires one.

## Final reconciliation points

1. **Sidequest vs Expedition:** Sidequests are player-controlled activities involving Alya and normally one selected ally, with explicit narrative exceptions. Expeditions are delegated community activities performed by NPCs without Alya.
2. **Combat termination vs outcome taxonomy:** combat ends when all members of one team are Surrendered or Incapacitated. Kill, Knockout, Capture, Submission, Escape, and Objective Complete remain contextual post-combat/result outcomes where applicable.
3. **HP semantics:** HP represents physical capacity/exhaustion tolerance rather than a literal wound counter. HP-cost skills cannot reduce their user below 1 HP.
4. **Initiative:** Agility influences the initial initiative roll; the result is determined once at combat start and produces a fixed full combatant order for the combat.
5. **Turn lifecycle:** the game uses rounds/timeline semantics; each active combatant receives its action according to the established order. Incapacitated/Surrendered combatants do not act.
6. **Actions:** the action economy supports normal actions plus explicitly defined free/reaction behavior. H-skills share normal active skill slots.
7. **Targeting:** targeting is skill-defined and supports manual, automatic, and explicit random targeting. Invalid targets cause action failure unless the skill's explicit policy says otherwise. Incapacitated targets are invalid; Surrendered targets are valid only for explicitly permitted interactions.
8. **Damage:** skills use reusable formula templates plus explicit skill parameters. Modifier order is deterministic; damage cannot resolve below 1 after mitigation unless a future explicit system rule introduces an exception.
9. **Effects:** application is immediate; duration follows the established start-of-turn/decrement lifecycle; explicit stacking groups govern coexistence; source tracking is retained; effect-specific removal policies are supported.
10. **Enemy Intent:** Intent is the planned action/goal, not necessarily an immutable target/action script. Intent visibility varies. Revealed Intent is locked. If it becomes invalid, resolution uses the defined fallback target policy rather than silently rewriting the prior turn's intent.
11. **H-system:** H-gauge is one combat value per combatant; Flirt/Intercourse/Finisher use separate acceptance thresholds. Thresholds can be adjusted per combat. H-gauge resets between combats and decays toward baseline outside combat. Overflow is part of the H-system state, not a fifth economy resource.
12. **Defeat:** 0 HP causes Incapacitation immediately; Surrender is distinct and can occur before 0 HP. Combat ends when one team has no active members because all members are Surrendered or Incapacitated.
13. **Equipment:** equipment belongs exclusively to Alya; allied NPCs do not use the equipment system. Equipment may modify/transform supported skill properties, including cursed equipment, using a finite declarative transformation vocabulary rather than arbitrary scripts.
14. **Progression:** XP is individual; levels award Skill Points; skills have no levels; active/passive loadouts are limited; natural attribute growth depends on use/context/results; skill acquisition can additionally require community buildings/events/context.
15. **Assignments:** each character has one primary Assignment; competence is discrete and non-decaying; assignment XP is below adventure/combat XP; production depends on competence, facilities, and conditions; assignment can be interrupted freely.
16. **Time:** explicit player-controlled advancement drives a day/night cycle and calendar. Long-running activities continue during advancement. Menus do not advance time. Completion ordering uses timestamp plus priority.
17. **Buildings:** the community has a physical layout with expandable space. Buildings may have tiers or be unique. Construction uses resources, time, and prerequisites; workers can affect construction; destruction/relocation has a cost.
18. **Economy:** resources use layered taxonomy; storage exists; Food is continuous upkeep; Currency and barter coexist; selling is possible with restrictions; external trade exists with variable market state; resources do not have rarity/quality tiers.
19. **Exploration:** the world uses an abstract regional/locality map. Travel consumes time. Sidequests are direct player activities; Expeditions are delegated NPC activities. Expeditions use stats/competence/context with controlled randomness and return automatically.
20. **Narrative:** quests have persistent state and multiple objectives; objective retroactivity is defined per objective; events can be deterministic or random; world changes may be temporary or permanent; relationships persist; choices can affect gameplay; global and local state coexist.
21. **Save:** autosave plus manual slots; saving is not permitted during combat; critical decision boundaries use explicit save/checkpoint handling.
22. **Content architecture:** content is data-driven, uses stable semantic IDs, stores balance in data/configuration, and supports content versioning/migration.

## Remaining work after Checkpoint B

The following are **not new gameplay decisions**. They are implementation-specification or content tasks:

- Formal combat state machine + turn-resolution contract.
- Effect/condition/trigger schemas and ordering rules.
- Skill schema, formula templates, cost/targeting contracts, and transformation vocabulary.
- Item/equipment/cursed-item schemas.
- Recruitment/rehabilitation state machines.
- Assignment/aptitude/growth formulas.
- Resource/economy/production schemas and rates.
- Sidequest and delegated Expedition schemas.
- Encounter and quest state-machine schemas.
- Time tick/block contract.
- Defeat/recovery resolution contract.
- XP/level/natural-growth formulas and power bands.
- Information/UI screen contracts.
- Save schema and migration implementation.
- Concrete content catalogs and assets.

These should be handled as **Implementation Specification Pass**, not another round of macro design discovery unless implementation exposes a genuine contradiction or structural gap.

---

# 3. Decision History — B4–B18 + Mega-Batch

The B batches are retained here as traceability rather than as independent specifications.

| Batch | Scope | Result |
|---|---|---|
| B4 | Effects / modifiers | Closed |
| B5 | Skills / action resolution | Closed |
| B6 | Targeting / positioning | Closed |
| B7 | Enemy Intent / AI | Closed |
| B8 | Victory / defeat / finisher | Closed |
| B9 | Equipment / modifiers | Closed |
| B10 | Character progression | Closed |
| B11 | Loadout | Closed |
| B12 | Species / aptitude / growth | Closed |
| B13 | Assignments | Closed |
| B14 | Time | Closed |
| B15 | Buildings | Closed |
| B16 | Economy / resources | Closed |
| B17 | Exploration / Expeditions | Closed |
| B18 | Quests / events / narrative state | Closed |
| B19 | Checkpoint B Mega-Batch | Closed; final macro rules consolidated |

---

# 4. Explicitly Closed Decisions

These should not be reopened casually:

- Alya is the fixed protagonist.
- Standard player-controlled sidequest/expedition structure is Alya + one selected ally, with narrative exceptions; delegated Expeditions are a separate community activity and do not include Alya.
- The game loop interconnects narrative, exploration, combat, resources, community, and progression.
- Main Quest is the principal structural progression gate.
- Regions remain relevant after unlock where appropriate.
- Procedural generation is used for repeatable exploration/gathering/selected reusable quests; handcrafted maps are reserved for places where authored design adds value.
- Community construction can be destroyed or relocated.
- Assignment experience persists permanently.
- Combat-capable recruited entities enter through eligibility followed by rehabilitation/integration rather than instant membership.
- Cursed equipment can be removed through dedicated community infrastructure but remains cursed and can later be voluntarily re-equipped.
- Equipment is exclusive to Alya; allied NPCs do not use equipment.
- The primary stat layer contains exactly eight mechanical attributes: Body, Agility, Soul, Charm, Dominance, Submission, Sadism, Masochism.
- Enemy power/progression band, encounter class, and narrative role are separate dimensions; the old mixed Tier terminology is deprecated.
- Encounter hierarchy is Normal → Elite → Mini-Boss → Boss.
- Combat termination occurs when all members of one team are Surrendered or Incapacitated; contextual victory/post-combat outcomes retain the Kill, Knockout, Capture, Submission, Escape, and Objective Complete taxonomy where applicable.
- Time uses an explicit day/night cycle with player-controlled advancement; permanent time pressure is exceptional.
- Defeat primarily uses retreat/consequence rather than generic Game Over or systemic permadeath.
- Information is progressively revealed using discover → available → explain → additional depth.
- New macro-systems require a demonstrated structural gap.

---

# 5. Next Gate — Implementation Specification Pass

**Objective:** turn the closed Checkpoint B rules into deterministic implementation contracts without reopening macro design.

Recommended order:

1. Combat state machine + turn lifecycle.
2. Effects / Conditions / Triggers.
3. Skill / Action schema.
4. Equipment / transformations / curses.
5. Character / progression / aptitude.
6. Recruitment / rehabilitation / community.
7. Time / production / economy.
8. Exploration / encounters / Sidequests / Expeditions.
9. Quests / events / world state.
10. Save / persistence / migration.
11. Information architecture / UX contracts.

**Checkpoint B exit condition:** every system above has a deterministic contract; any remaining unknowns are tuning or content, not design decisions.
