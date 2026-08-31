# Alya Heals the World — Master Planning Audit

## Purpose

This is the master checklist for reaching **Planning Complete**: the point at which the game's design and content specification are sufficiently closed that implementation/production can proceed without requiring new major design decisions.

This document consolidates the current architecture, narrative canon, R1–R15 checkpoint, Skills Audit, existing structured data, and Checkpoint B decisions. It is a planning-status document, not a replacement for domain-specific source-of-truth documents.

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
**STATUS: IN PROGRESS**

B4–B18 established a large portion of the rules architecture. Detailed formulas, schemas, exact state transitions, cross-system contracts, and remaining edge cases are still required before B can be declared complete.

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
| 3 | World structure | SPECIFICATION NEEDED | Regions and procedural/hand-authored split + B17 world map | Final world graph, region rules | B/C |
| 4 | Narrative canon | CLOSED | `NARRATIVE_CANON.md` | Content implementation still needed | A |
| 5 | Narrative implementation | CONTENT NEEDED | Canon + B18 quest/event/world-state model | Scene/quest/flag graph | C |
| 6 | Character architecture | CLOSED | Population/ally architecture + B10–B13 | Concrete roster and data | A/C |
| 7 | Character content | CONTENT NEEDED | Existing character CSV + architecture | Final roster, stats, skills, arcs, recruitment, assets | C |
| 8 | Enemy architecture | CLOSED | Family/role/power/encounter/narrative separation + B7 AI contract | Concrete data | A/C |
| 9 | Enemy content | CONTENT NEEDED | Existing enemy CSV + architecture | Final roster, AI, stats, drops, variants | C |
| 10 | Combat rules | SPECIFICATION NEEDED | B5–B8 | Exact formulas, lifecycle, action queue/resolution, full edge cases | B |
| 11 | Status/effects | SPECIFICATION NEEDED | B4 + architecture | Formal effect contract, timing, stacking/cleanse edge cases | B |
| 12 | Skills | SPECIFICATION NEEDED | `SKILLS_AUDIT.md` + B5/B9/B10/B11 | Final schema, formulas, costs, targeting, transformations, acquisition | B/C |
| 13 | Equipment/items | SPECIFICATION NEEDED | Item architecture + B9/B11 | Full schema, transformation vocabulary, catalog, acquisition | B/C |
| 14 | Curses/blessings | SPECIFICATION NEEDED | Architecture + B9 | Exact state/progression rules and content | B/C |
| 15 | Recruitment | SPECIFICATION NEEDED | Recruitment architecture | Exact eligibility conditions and transitions | B |
| 16 | Rehabilitation/integration | SPECIFICATION NEEDED | Architecture + mechanics CSV | Facility/process states, requirements, outcomes | B/C |
| 17 | Community architecture | CLOSED | R1–R15 + architecture + B13–B15 | None at macro level | A |
| 18 | Buildings/facilities | CONTENT NEEDED | B15 + architectural rules | Final building catalog, costs, upgrades, effects | C |
| 19 | Assignments/aptitude | SPECIFICATION NEEDED | B12/B13 | Growth/competence/output formulas and edge cases | B |
| 20 | Resources | SPECIFICATION NEEDED | B16 + resource/ecology architecture | Resource taxonomy, acquisition, rates, storage footprint, sinks | B/C |
| 21 | Economy/trade | SPECIFICATION NEEDED | B16 + economy architecture | Prices, inventories, refresh, reward curves | B/C |
| 22 | Ecology/production | SPECIFICATION NEEDED | Architecture + B15/B16 | Production cycles, renewable/unique rules | B/C |
| 23 | Exploration | SPECIFICATION NEEDED | B17 | Sidequest vs Expedition contracts, travel, generation, persistence | B |
| 24 | Encounters | SPECIFICATION NEEDED | Encounter hierarchy + B17/B18 | Encounter schema, generation, resolution | B |
| 25 | Quests | SPECIFICATION NEEDED | B18 | Quest state machine, objective semantics, trigger contract | B |
| 26 | Quest content | CONTENT NEEDED | Narrative canon + B18 quest architecture | Full quest graph and data | C |
| 27 | Time/day-night | SPECIFICATION NEEDED | B14 | Exact time blocks, ticks, waiting, day/night transitions | B |
| 28 | Defeat/recovery | SPECIFICATION NEEDED | B8 + retreat/consequence model | Exact post-combat/post-defeat resolution, recovery, edge cases | B |
| 29 | Progression | SPECIFICATION NEEDED | B10–B12 | XP/level curves, skill-point rules, natural growth formulas, power bands | B/C |
| 30 | Information architecture | SPECIFICATION NEEDED | Discover→available→explain→depth | Screen-level information flows | B/D |
| 31 | UX/UI | CONTENT NEEDED | IA principles + system decisions | Screen inventory, wireframes, interaction contracts | C/D |
| 32 | Save/persistence | SPECIFICATION NEEDED | Not yet fully formalized | Persistence model and save boundaries | B/D |
| 33 | Art direction | SPECIFICATION NEEDED | Existing AI/reference assets | Art bible, asset standards, pipeline | D |
| 34 | Audio | SPECIFICATION NEEDED | Existing/legacy audio assets | Audio bible, event mapping, pipeline | D |
| 35 | Localization | OPEN DECISION | Not formally closed | Base language, string architecture, scope | D |
| 36 | Accessibility/settings | OPEN DECISION | Not formally closed | Required options and accessibility targets | D |
| 37 | Technical implementation contracts | SPECIFICATION NEEDED | Repository architecture principles + B rules | Data schemas, interfaces, state ownership | B/D |
| 38 | QA/testing | SPECIFICATION NEEDED | Not formally closed | Acceptance tests and regression strategy | D |
| 39 | Tutorial/onboarding | CONTENT NEEDED | Narrative entry and community introduction established | First-session flow and teaching beats | C/D |
| 40 | Release/publishing | OPTIONAL / LATER | Outside core design | Platform/store/release decisions | Post-D |

---

# 2. Interim Audit — B4–B18

## Overall verdict

**No hard architectural contradiction was found between the newly decided B4–B18 rules and the current high-level architecture.** The architecture has been updated to reflect the decisions below.

There are, however, several **reconciliation points that must remain explicit** in future specifications:

1. **Player-controlled expeditions vs delegated Expeditions:** the older architecture phrase "standard expedition" referred to Alya + one selected ally. B17 introduced a distinct autonomous community-delegated Expedition. The architecture now explicitly distinguishes player-controlled sidequest/expedition parties from delegated Expeditions.
2. **Victory taxonomy vs combat termination:** the combat engine ends when one team has no Active combatants because all members are Surrendered or Incapacitated. Kill/Knockout/Capture/Submission/etc. are post-combat/contextual resolution outcomes, not separate engine termination conditions.
3. **HP semantics:** HP remains the combat health/capacity stat, but its design meaning is physical capacity/exhaustion tolerance rather than a literal wound counter. This must be reflected consistently in UI, recovery, damage, and narrative language.
4. **Skill transformations:** equipment may change skill structure/function, especially cursed equipment, but transformations must use a finite declarative vocabulary supported by the skill schema rather than arbitrary item-specific scripts.
5. **Surrendered targets:** Surrendered characters do not act, but may remain targetable by explicitly permitted interactions. Incapacitated characters are not valid targets.
6. **Intent lock:** Enemy Intent is revealed before the enemy acts and remains locked. A later state change can make the intended action invalid; a formal fallback rule is still required.
7. **Time-driven activities:** construction, production, travel, assignments, recovery, and Expeditions continue while explicit time advancement occurs. Exact tick/time-block semantics remain open for B specification.
8. **H-gauge outside combat:** it decays toward a baseline, while contextual modifiers may change its behavior. Exact curve/baseline remain tuning/specification work.

## B4 — Effects and Modifiers

Closed decisions:
- Temporary, Permanent, and Conditional durations.
- Explicit Stacking Groups and Stacking Policies.
- Effects in different stacking groups can coexist and accumulate.
- Strongest Wins is the default competing-effect policy.
- Cleanse/dispel can use tags.
- Source tracking is retained.
- Applicable effects are removed immediately when their source is removed/dead or equipment is removed.

## B5 — Skill/Action Resolution

Closed decisions:
- Skills contain ordered lists of effects.
- Effects can have dependencies.
- Conditions are reusable.
- Skill costs can reference any valid resource, including HP.
- Invalid targets cause action failure rather than automatic retargeting.
- Targeting supports reusable patterns and explicit exceptions.
- Criticals participate in the modifier pipeline.

## B6 — Targeting and Positioning

Closed decisions:
- No spatial/grid positioning.
- No separate range system.
- Manual, automatic, and explicitly random targeting are supported.
- Friendly fire is skill-specific.
- Incapacitated characters are invalid targets.
- Surrendered characters no longer act but remain targetable by explicitly permitted interactions.

## B7 — Enemy Intent / AI

Closed decisions:
- Intent visibility varies by enemy/skill.
- Intent is revealed in the preceding turn.
- AI uses deterministic priorities with controlled weighted/equivalent choices.
- Personality and AI Profile are separate.
- AI considers H-gauge and the full combat state.
- Revealed intent is locked.
- Finisher eligibility is threshold/condition-gated; AI decides whether to use an eligible Finisher.

## B8 — Victory / Defeat / Finisher

Closed decisions:
- 0 HP immediately causes Incapacitated.
- Surrender can happen before 0 HP.
- Surrender remains distinct from Incapacitation.
- Finishers may be powerful ordinary skills or special finalization actions.
- Allies and enemies can use Finishers.
- Finishers become invalid if their action requirements cease to be true before resolution.
- Combat ends when all members of one team are Surrendered or Incapacitated.
- Post-combat resolution determines contextual outcomes.

## B9 — Equipment and Modifiers

Closed decisions:
- Equipment can modify skill values and explicitly supported skill properties/structure.
- Skill property changes are constrained to exposed schema capabilities.
- Modifiers can be absolute or percentage-based.
- Modifier order is deterministic by category.
- Global and specific caps can coexist.
- Effective primary stats do not fall below zero.
- Modifier changes recalculate immediately.

## B10 — Character Progression

Closed decisions:
- Level + XP exist.
- Level provides Skill Points plus limited base growth/unlocks.
- Attributes also develop through natural growth and direct/distributable growth.
- Natural growth is influenced by skill usage, context/results, and community role.
- Skill acquisition is hybrid and may require community buildings/events/context in addition to Skill Points.
- Skills have no levels.
- Active loadouts are limited.
- Passives are a separate limited pool.
- Traits/passives share the Effects/Conditions/Modifiers framework.

## B11 — Loadout

Closed decisions:
- Active skill slots are base + modifiers.
- Passives have a separate limited pool.
- H-skills share normal active skill slots.
- Loadout is locked during combat.
- Loadouts can be changed outside combat and support presets.
- Unlocked skills are permanent.
- Skill Point respec is possible with cost/condition.

## B12 — Species / Aptitude / Growth

Closed decisions:
- Species provides attribute predisposition.
- Aptitude is visible.
- Aptitude influences growth through curves.
- Skill use + context + results influence natural growth.
- Community role influences attributes.
- Characters can exceed natural aptitude with diminishing returns.
- Individual potential exists; training/equipment can temporarily exceed it.

## B13 — Assignments

Closed decisions:
- One primary Assignment per character.
- Assignment stops functioning while the character is outside the community.
- Competence has discrete levels.
- Competence does not decay.
- Assignments grant XP at a lower rate than adventures/combat.
- Assignments may produce resources or support according to function.
- Assignment can be interrupted freely.

## B14 — Time

Closed decisions:
- Multiple time scales with an explicit day/night cycle and calendar.
- Time advances explicitly by player choice.
- Long-running activities continue while time advances.
- Idle menus do not advance the world.
- Production is rate-based per unit of game time.
- HP recovers passively and is modified by facilities/skills/status.
- H-gauge decays toward baseline outside combat, with contextual modifiers.

## B15 — Buildings

Closed decisions:
- Community has a physical layout/map.
- Space is limited but expandable.
- Some buildings have upgrades/tiers; others are unique.
- Construction requires resources, time, and prerequisites.
- Workers can participate and modify construction efficiency/results.
- Buildings may be passive or worker-dependent.
- Destruction/relocation is possible with a cost.

## B16 — Economy / Resources

Closed decisions:
- Layered resource taxonomy: few fundamentals + specialized resources.
- Storage/capacity exists with per-resource footprint behavior where needed.
- Food is continuous community upkeep.
- Currency and barter coexist.
- Resource selling is possible with restrictions.
- External trade exists with potentially variable inventories/prices.
- Resources do not have rarity/quality tiers.

## B17 — Exploration / Expeditions

Closed decisions:
- Abstract regional/locality world map.
- Travel consumes time.
- Sidequests are player-controlled; Expeditions are delegated community activities.
- Expeditions can have non-combat checks and variable composition.
- Region progression gates exist.
- Expeditions return automatically.

## B18 — Quests / Events / Narrative State

Closed decisions:
- Quests have persistent states.
- Quests can have multiple objectives.
- Objective retroactivity is decided per objective.
- Events use deterministic and random mechanisms.
- World changes can be temporary or permanent.
- NPC relationships persist.
- Narrative choices can affect gameplay.
- Global world state coexists with local quest state.

---

# 3. Decisions Explicitly Closed

These should not be reopened casually:

- Alya is the fixed protagonist.
- Standard player-controlled expedition/sidequest structure is Alya + one selected ally, with narrative exceptions; delegated Expeditions are a separate community activity.
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
- Combat termination occurs when all members of one team are Surrendered or Incapacitated; contextual victory/post-combat outcomes retain the Kill, Knockout, Capture, Submission, Escape, and Objective Complete taxonomy where applicable.
- Time uses an explicit day/night cycle with player-controlled advancement; permanent time pressure is exceptional.
- Defeat primarily uses retreat/consequence rather than generic Game Over or systemic permadeath.
- Information is progressively revealed using discover → available → explain → additional depth.
- New macro-systems require a demonstrated structural gap.

---

# 4. Known Deliberate Deferrals

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

# 5. Critical Dependencies for Checkpoint B

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
14. Progression and natural-growth formulas.
15. Quest/event/world-state contract.
16. Persistence/save contract.
17. UX information contracts required by the above rules.

The purpose is to close interfaces, not to balance every content entry immediately.

---

# 6. Content Completion Checklist

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

# 7. Production Completion Checklist

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

# 8. Checkpoint B Batch Register

This is a historical index only. The domain sections above and their linked source documents are authoritative.

| Batch | Primary topic | Result |
|---|---|---|
| B4 | Effects, duration, stacking, cleansing, source tracking | CLOSED |
| B5 | Skill composition, dependencies, conditions, costs, target validation, criticals | CLOSED |
| B6 | Targeting and absence of spatial positioning | CLOSED |
| B7 | Enemy Intent and AI | CLOSED |
| B8 | Victory, defeat, surrender, incapacitation, finishers | CLOSED |
| B9 | Equipment, skill transformation, modifiers, caps | CLOSED |
| B10 | Level, XP, Skill Points, character growth | CLOSED |
| B11 | Skill/passive/H-skill loadouts | CLOSED |
| B12 | Species, aptitude, natural growth, individual potential | CLOSED |
| B13 | Assignments and competence | CLOSED |
| B14 | Time, day/night, recovery, H-gauge decay | CLOSED |
| B15 | Buildings, construction, workers, space | CLOSED |
| B16 | Resources, storage, upkeep, economy, trade | CLOSED |
| B17 | World map, travel, Sidequests vs Expeditions | CLOSED |
| B18 | Quests, objectives, events, relationships, world state | CLOSED |

---

# 9. Working Rule Going Forward

We should stop asking "what other systems could the game have?" unless a real gap appears.

The default question is now:

> **Which existing system/interface owns this requirement, and is that interface specified tightly enough to implement it?**

A proposed new mechanic must identify the gap it solves and why existing systems cannot solve it through content, configuration, specialization, or extension.

## Current verdict

**Checkpoint A: COMPLETE**

**Checkpoint B: IN PROGRESS — macro rules substantially consolidated; deterministic contracts/formulas still required**

**Checkpoint C: PENDING — Content Complete**

**Checkpoint D: PENDING — Production Complete**
