# Alya Heals the World — Master Planning Audit

## Purpose

This is the master checklist for reaching **Planning Complete**: the point at which the game's design and content specification are sufficiently closed that implementation/production can proceed without requiring new major design decisions.

This document consolidates the current architecture, narrative canon, R1–R15 checkpoint, Skills Audit, existing structured data, Checkpoint B decisions, and the completed Implementation Specification Pass. It is a planning-status document, not a replacement for domain-specific source-of-truth documents.

## Planning Completion Standard

A domain is **CLOSED** when its design and implementation contract are decided. A domain may still require **content production**, implementation, art, audio, localization, QA, and balance work without reopening its design.

Statuses:
- **CLOSED** — design/specification is established.
- **CONTENT NEEDED** — system is closed but final content set is still missing.
- **DEPENDENCY** — cannot be completed until another domain is resolved.
- **OPTIONAL** — deliberately deferred and not required for the base game.
- **OPEN DECISION** — a genuine design/specification choice remains unresolved.

## Gate Model

### Checkpoint A — Architecture Complete
**STATUS: COMPLETE**

### Checkpoint B — Rules Complete
**STATUS: COMPLETE**

### Implementation Specification I1–I11
**STATUS: COMPLETE**

### I12 — Cross-System Integration & Final Specification Audit
**STATUS: COMPLETE**

### Checkpoint C — Content Complete
**STATUS: NOT STARTED AS A FORMAL GATE**

### Checkpoint D — Production Complete
**STATUS: NOT STARTED AS A FORMAL GATE**

---

# 1. Master Domain Audit

| # | Domain | Status | Remaining work | Gate |
|---|---|---|---|---|
| 1 | Game identity / pillars | CLOSED | None unless implementation exposes contradiction | A |
| 2 | Core gameplay loop | CLOSED | None | A |
| 3 | World structure | CLOSED | Final world graph, region content | C |
| 4 | Narrative canon | CLOSED | Content implementation | A/C |
| 5 | Narrative implementation | CLOSED | Implement scene/quest/flag graph | C/D |
| 6 | Character architecture | CLOSED | Concrete roster/data | C |
| 7 | Character content | CLOSED | Final roster, stats, skills, arcs, recruitment, assets | C/D |
| 8 | Enemy architecture | CLOSED | Concrete data | C |
| 9 | Enemy content | CLOSED | Final roster, AI, stats, drops, variants | C |
| 10 | Combat rules | CLOSED | Implementation, content, balance, QA | D |
| 11 | Status/effects | CLOSED | Content and QA | C/D |
| 12 | Skills | CLOSED | Final catalog/content, implementation, balance | C/D |
| 13 | Equipment/items | CLOSED | Final catalog/content, implementation, balance | C/D |
| 14 | Curses/blessings | CLOSED | Exact content and implementation | C/D |
| 15 | Recruitment | CLOSED | Final content and implementation | C/D |
| 16 | Rehabilitation/integration | CLOSED | Facility/content implementation | C/D |
| 17 | Community architecture | CLOSED | Implementation | D |
| 18 | Buildings/facilities | CLOSED | Final catalog, costs, upgrades, effects | C |
| 19 | Assignments/aptitude | CLOSED | Final tuning/content | C/D |
| 20 | Resources | CLOSED | Final taxonomy/content, rates, sinks | C/D |
| 21 | Economy/trade | CLOSED | Prices, inventories, refresh, reward curves | C/D |
| 22 | Ecology/production | CLOSED | Production content and tuning | C/D |
| 23 | Exploration | CLOSED | Final region/travel content | C/D |
| 24 | Encounters | CLOSED | Final encounter catalog/content | C/D |
| 25 | Quests | CLOSED | Final quest graph/content | C/D |
| 26 | Quest content | CLOSED | Full quest graph and data | C |
| 27 | Time/day-night | CLOSED | Implementation and balance | D |
| 28 | Defeat/recovery | CLOSED | Implementation and content | D |
| 29 | Progression | CLOSED | XP/level curves and balance | C/D |
| 30 | Information architecture | CLOSED | Screen-level production implementation | D |
| 31 | UX/UI | CLOSED | Screen inventory, wireframes, interaction implementation | D |
| 32 | Save/persistence | CLOSED | Implementation, migration tests | D |
| 33 | Art direction | SPECIFICATION NEEDED | Art bible, asset standards, pipeline | D |
| 34 | Audio | SPECIFICATION NEEDED | Audio bible, event mapping, pipeline | D |
| 35 | Localization | OPEN DECISION | Base language, string architecture, scope | D |
| 36 | Accessibility/settings | OPEN DECISION | Required options and accessibility targets | D |
| 37 | Technical implementation contracts | CLOSED | Implementation | D |
| 38 | QA/testing | SPECIFICATION NEEDED | Acceptance tests and regression strategy | D |
| 39 | Tutorial/onboarding | CLOSED | First-session content and implementation | C/D |
| 40 | Release/publishing | OPTIONAL / LATER | Platform/store/release decisions | Post-D |

**Important:** rows 33, 35, 36 and 38 are production/publishing concerns rather than missing core gameplay design. They must be resolved before final production/release, but they do not block the conclusion that the gameplay implementation specification is closed.

---

# 2. Implementation Specification Pass — Final Closure Record

## Overall verdict

**I1–I11 are CLOSED and I12 is COMPLETE.**

The implementation pass converted the macro rules into deterministic contracts and the final integration audit found no blocking cross-system contradiction.

### I1 — Combat State Machine + Turn Lifecycle
- Initiative is randomized once at combat start; Agility modifies the initial result; the resulting order remains stable.
- Turn start processes start-of-turn effects, duration update/expiration and derived-state recalculation before checking whether the actor can act.
- Incapacitated/Surrendered actors cannot select or perform actions.
- Combat terminates when all members of one team are Surrendered and/or Incapacitated.
- Reinforcements enter at the end of the current order.
- An atomic action completes its declared resolution pipeline before terminal combat state is committed.

### I2 — Actions + Resolution Pipeline
- Insufficient resources make an action unselectable.
- Player invalid-action handling requests another action; AI retains the selected action and changes target when possible.
- Costs are validated before action resolution.
- Multi-hit skills resolve as independent sub-actions.
- Randomness uses deterministic per-combat/per-action RNG structures.

### I3 — Effects / Conditions / Triggers
- Effects are instances with definition, source character/definition, duration, stacks and runtime state.
- Stacking policies are data-driven.
- Triggers are event-driven and may chain under an execution budget.
- Effect removal/expiration behavior is definition-driven.
- Source provenance supports parent execution/effect references.

### I4 — Skills / Targeting / Formulas
- Gameplay, AI and presentation data are separated.
- Targeting uses composable queries; selection policy is skill-defined.
- Random targeting supports filters and weights.
- Formulas use constrained data-driven expressions.
- Modifier ordering is deterministic.
- Criticals and accuracy use the established generic result systems.

### I5 — Equipment / Transformations / Curses
- Equipment is exclusive to Alya; allied NPCs do not use equipment.
- Equipment changes occur outside combat.
- Equipment can declaratively transform supported skill properties.
- Transform conflicts use explicit priority.
- Cursed equipment combines curse definition and active effect state and preserves curse state when unequipped.

### I6 — Characters / Progression / Aptitude
- Character architecture separates species/base data, personality, growth and modifiers.
- Natural growth is derived from recorded activity/use and converted through periodic growth processing.
- Skill points are persistent and spendable; skill requirements are data-driven and may include community/event gates.
- Passives may be permanent or loadout-based.
- Aptitude is derived from species, attributes, experience and modifiers.

### I7 — Recruitment / Rehabilitation / Community
- Recruitment, eligibility and rehabilitation/integration are separate states.
- Rehabilitation is progress-driven and can use facilities, assignments and events.
- Community members have availability/assignment states.
- Assignment interruption follows the defined progress/output policy.
- **Expedition = NPC-only delegated activity. Sidequest = activity requiring Alya.**

### I8 — Time / Economy / Production / Assignments
- Time is represented internally with continuous timestamps.
- Day/night is a gameplay state and can gate availability.
- Time advancement processes intermediate timestamps chronologically; same-timestamp events use priority.
- Waiting supports semantic and custom durations.
- Facilities/skills/statuses can modify recovery.
- Production and upkeep use the defined time/tick model.
- Inventory has **no fixed capacity limit**.

### I9 — Exploration / Encounters / Sidequests / Expeditions
- World navigation uses a regional/locality graph.
- Travel duration is affected by route and modifiers.
- Encounters use pools, conditions and weights.
- Sidequests require Alya; Expeditions use NPCs only and resolve through checkpoints.
- Expedition outcomes can include configured success/failure consequences.

### I10 — Quests / Events / World State
- Quest state uses a graph with objective progress and configurable policies.
- Retroactivity is objective-defined.
- Event processing is event-driven with explicit priority.
- World state separates global/local, quest, relationship and simulation state.
- Relationship state supports values, flags and stages.
- Choices can modify narrative, gameplay and world state.

### I11 — Save / Persistence / Data Contracts
- Persistent state contains everything needed to reconstruct gameplay; reconstructible runtime state is not unnecessarily serialized.
- Combat is not saved mid-resolution.
- Autosaves and manual slots follow the established boundaries.
- Save schema versioning is independent from game versioning.
- Migrations are automatic and preserve the original save.
- Randomness persists enough seed/RNG/execution state to reproduce relevant bugs.
- Stable semantic IDs and immutable identity are used where required.
- Gameplay, balance, localization and presentation data remain separated.

---

# 3. I12 — Cross-System Integration & Final Audit

## Final decisions

1. **Turn lifecycle:** `TurnStarted → Start-of-Turn Effects → Duration Update/Expiration → Derived State Recalculation → CanAct Check → Intent/Action Selection → Action Resolution → Triggered Reactions → End-of-Turn Effects → TurnEnded → Terminal Check`.
2. **Atomic actions:** a resolving atomic action completes its declared pipeline before terminal combat state is committed.
3. **Combat state composition:** participation state is distinct from other character state; Surrendered and Incapacitated cannot act.
4. **HP:** current HP is clamped at 0; no overkill value is required or persisted.
5. **Derived stats:** mutations invalidate derived state immediately; effective calculation may be lazy.
6. **Effect provenance:** direct source plus optional parent execution/effect reference is sufficient.
7. **Event ordering:** canonical mutation commits, derived state updates, domain event emits, then handlers cause subsequent mutations.
8. **Transactions:** atomic by default; content may explicitly define partial behavior where appropriate. Inventory has no capacity ceiling.
9. **Time advancement:** process intermediate timestamps chronologically; equal timestamps use explicit priority.
10. **Randomness:** persist seed/RNG state and execution information required for deterministic reproduction/debugging.
11. **AI:** preserve Intent/action when target becomes invalid; retarget if possible; otherwise use explicit fallback policy.
12. **Architecture boundary:** new behavior requiring a new capability must update the specification/schema; ad-hoc special-case behavior is not an accepted design mechanism.

## Audit result

**NO BLOCKING GAPS FOUND.**

The audit did not identify a remaining cross-system contradiction that requires reopening macro design. Remaining production work consists of implementation, content, assets, UX, audio, localization, QA and numerical balancing.

---

# 4. Production Gate — What “Planning Complete” Means Now

The project can now leave the planning/specification phase for the core game systems when:

- the GDD remains aligned with this audit;
- implementation contracts remain the source of truth for runtime behavior;
- content is represented through data rather than one-off code;
- new design decisions are explicitly recorded if implementation exposes a genuine gap;
- production can proceed system-by-system without rediscovering intended game rules.

**Current conclusion: CORE GAME DESIGN + IMPLEMENTATION SPECIFICATION CLOSED. PROCEED TO PRODUCTION.**

This does **not** mean the game is content-complete or release-ready. Checkpoints C and D remain production gates.
