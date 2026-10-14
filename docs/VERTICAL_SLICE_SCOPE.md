# AHTW — Vertical Slice Scope

> **Status:** Scope baseline approved for production planning.
>
> **Purpose:** Define the smallest coherent, representative playable slice of *Alya Heals The World* that validates the game's central promise before content volume expands. This document defines scope and acceptance criteria; it does not claim the slice has been implemented or tested.
>
> **Authority:** This scope must remain consistent with `docs/NARRATIVE_CANON.md`, `docs/architecture/GAME_ARCHITECTURE.md`, `docs/IMPLEMENTATION_SPEC.md`, and the relevant system contracts. If implementation reveals a conflict, update the relevant source of truth rather than silently forking a rule.

---

## 1. Product objective

The vertical slice must demonstrate that AHTW is a **narrative RPG whose combat, exploration, character relationships, and light community management reinforce one another**.

The player should experience the following loop in one coherent story:

**Meet a person in need → investigate a local Ferida manifestation → make preparations and face encounters → obtain knowledge/resources/relationships → decide how to respond collectively → see the community change → unlock the first delegated community activity.**

The slice must also dramatize the core thematic progression:

**Helping one person → accepting consequences for a community → confronting the limits of a technically rational solution → building a costly third option → accepting responsibility without claiming total control.**

This is not a miniature version of every act. It is a complete, deliberately bounded proof of the game's identity.

## 2. Target experience and completion boundary

- **Target first-play duration:** approximately 2–4 hours, including optional exploration and dialogue. This is a planning target, not a guaranteed runtime.
- **Narrative boundary:** one self-contained Act I crisis arc, ending with the community's survival, a consequential loss, and Alya's recognition as its leader.
- **Management boundary:** introduce the initial community-management loop after the Act I resolution, as a consequence of Alya's new responsibility. The slice ends after the player makes at least one meaningful management decision and starts or resolves one small autonomous Expedition.
- **Playable boundary:** one hub, one adjacent explorable region, a compact quest graph, a small representative combat roster, and a small set of facilities/resources.
- **Quality boundary:** functional, coherent and testable; not final balance, exhaustive content, complete art coverage, or release-ready production.

The main path must be completable without optional adult scenes, optional exploration, or perfect combat outcomes.

## 3. Player-facing pillars

### 3.1 Narrative choices have costs

The crisis must not be solved by a single obviously correct dialogue option. The player should understand the competing priorities, have a chance to gather context, and then choose among imperfect responses. The chosen response changes at least one visible or persistent state.

### 3.2 The Ferida amplifies existing vulnerabilities

The local threat must exploit a pre-existing weakness in a person, relationship, or community process. It must not be presented as a random monster attack or as the sole cause of every social problem. The player should see both the supernatural manifestation and the human conditions it worsens.

### 3.3 Institutions are useful and fallible

The Organization's intervention must provide genuine expertise or resources. Its proposed containment/isolation solution must be defensible under its stated risk model, while still imposing a human cost that the player can understand. Institutional characters must disagree in priorities without being reduced to a monolithic evil faction.

### 3.4 Community is a gameplay system and a character

The hub changes as a result of the player's actions. At least one community decision must affect a resource, facility, assignment, relationship, or future opportunity—not only a line of dialogue.

### 3.5 Alya matters, but cannot do everything

Alya is central to the crisis but cannot personally replace local knowledge, collective effort, or delegated responsibility. At least one successful outcome depends on capabilities or contributions from other people.

### 3.6 Adult content supports character and relationships

All characters are adults. Adult scenes are optional, clearly contextualized, and tied to character identity/relationship progression. They must not be required to complete the main crisis or used as a substitute for meaningful characterization. The vertical slice needs only a small representative sample, not the full CG matrix.

## 4. Included content

### 4.1 Locations and world

**Required**
- One starting community hub with readable, reusable spaces for social interaction, basic commerce, and community management.
- One adjacent region with **three compact points of interest**: a route or approach, a site showing the local Ferida impact, and a location used for the climax or its preparation.
- One optional discovery that provides useful context, a modest reward, or a safer/more informed approach to the crisis.
- A small number of traversal states and encounter placements, sufficient to demonstrate exploration without requiring a large world map.

**Explicitly excluded**
- A second full settlement, a regional travel network, multi-region politics, and open-world-scale exploration.

### 4.2 Narrative and quest structure

Required quest sequence:
1. **Arrival and immediate need:** Alya meets a person affected by the community's current scarcity and chooses to help.
2. **Local investigation:** clues connect an individual problem to a manifestation of the Ferida and reveal existing social/material vulnerabilities.
3. **First intervention and consequence:** Alya supports or helps enact a plausible local solution based on incomplete context; it relieves one visible pressure but transfers or worsens another cost.
4. **Decision to stay:** Alya has a credible opportunity to continue her journey, but chooses to remain and help deal with the consequences.
5. **Failed containment:** the community's own response proves insufficient as the Ferida escalates. The failure must arise from limited capacity and incomplete understanding, not from characters behaving foolishly for plot convenience.
6. **Organization intervention:** the Organization supplies real assistance and proposes a technically defensible plan based on containment, exclusion, or sacrifice.
7. **Third-solution preparation:** the player gathers support, materials, and local knowledge. The solution requires more than Alya's exceptional power.
8. **Climax and unavoidable loss:** the community survives the immediate crisis, but a meaningful loss remains. The loss must not be framed as a simple punishment for choosing the “wrong” option.
9. **Recognition and transition:** Alya is formally recognized as a leader; the first community-management decision becomes playable.

The slice must include at least one optional branch or discovery that changes context, preparation, reward, or a later line/choice. Avoid branches that create an entirely separate production path.

### 4.3 Characters

**Core playable/narrative focus**
- Alya.
- **ALLY-001 First Ally / Generalist**, as the initial companion and an embodiment of flexible contribution.
- One additional ally who can credibly support the crisis and later community life. Preferred candidate: **ALLY-005 Cuidadora**, because recovery, diagnosis, and prevention connect the immediate human cost to the community's long-term response. If the detailed quest graph makes her introduction implausible, use her as a key NPC in this slice and defer formal recruitment rather than forcing the roster.

**Required NPC functions**
- A person directly affected by the local crisis.
- A community voice with local memory or mediation capacity (NPC-003 Community Elder or NPC-004 Mediator).
- A practical Organization ally (NPC-005 Pragmatic Mentor).
- An Organization representative who can explain institutional constraints (NPC-006 Institutional Representative).
- One functional hub NPC for rumors or trade (NPC-001 Tavernkeeper or an existing equivalent).

NPCs must retain their locked identities and stable IDs. Do not add a new recurring character merely to fill a role that an existing roster member can perform.

### 4.4 Combat and encounters

**Initial planning target**
- **4 enemy archetypes**, with variants only where they create a distinct tactical purpose.
- **3 standard encounters** and **1 climax encounter** (boss, elite, or multi-stage objective encounter as best fits the locked combat model).
- One encounter emphasizing basic action economy and target selection.
- One encounter emphasizing defense, control, status effects, or intent response.
- One encounter demonstrating a meaningful use of party composition or a learned skill.
- One climax encounter in which defeating enemies alone is insufficient; the party must also complete or protect a crisis objective.

At least one enemy or encounter must demonstrate that the Ferida amplifies a vulnerability rather than acting as a generic damage source. Avoid exposing every advanced mechanic in the slice. Choose a compact set of skills and effects that proves tactical variety while preserving implementation focus.

All outcomes, costs, effect timing, friendly fire, Chain, Overflow, finishers, and capability/P-growth edge cases remain governed by their canonical contracts. Exhaustive system validation and final balance are implementation/QA work, not a prerequisite for authoring this scope.

### 4.5 Rewards, items, and progression

Required:
- A small reward set with stable IDs.
- At least one consumable or recoverable resource that changes preparation or recovery choices.
- At least one material/resource used by the third-solution preparation or the first community improvement.
- At least one persistent unlock (skill, capability, relationship state, facility, assignment, or quest gate) that enables a new option.
- A clear separation between immediate encounter rewards and long-term community value.

Do not create items solely to increase catalog size. Each slice item must serve a defined encounter, recovery, crafting, quest, or community purpose.

### 4.6 Community management

The slice introduces, rather than exhaustively implements, the management loop.

**Required minimum**
- One hub/community state that visibly changes after the crisis.
- **Three facilities or facility states**: a basic common hub, a recovery/health function, and a production/storage/training function. Reuse the canonical facility model and choose the concrete facilities during the content catalog pass.
- **Three core resources**: provisions, materials, and a community-specific recovery/supply resource. Final names and data IDs must align with the resource catalog; do not create duplicate resource concepts.
- One construction, repair, or improvement decision with a cost and visible benefit.
- One character assignment that demonstrates aptitude/function without hard-locking a character to a role.
- A simple summary of current needs, available resources, and the consequence of the player's choice.

The player should face at least one genuine trade-off: spending scarce resources on immediate recovery/security versus investing in a capability that reduces future vulnerability. Neither option should be an obvious universal optimum.

### 4.7 Autonomous Expedition

Include **one low-risk introductory Expedition** if it can reuse the existing Expedition contract without creating a second quest system.

It must demonstrate:
- selecting an eligible community member;
- assigning a purpose or destination;
- committing time and/or a resource cost according to the existing rules;
- autonomous resolution without Alya;
- a result containing at least one reward, discovery, or consequence;
- the assigned ally being unavailable to the active party while away, if that is the canonical rule for the selected assignment.

If the complete Expedition UI would delay the slice, deliver the same contract through a minimal interface rather than removing the system from the data/architecture. Do not substitute an Alya-led Sidequest; those are separate activity types.

### 4.8 Adult-content sample

- Include at most **one optional, character-focused adult scene/CG sequence** in the vertical slice.
- Prefer a scene unlocked by a meaningful relationship state and consistent with the character's personality, rather than by arbitrary completion of the main quest.
- It must be skippable without losing gameplay-critical rewards, allies, or access to the main ending.
- Reuse the existing character/CG planning rules and stable IDs; do not invent a new adult-content subsystem for the slice.
- Full route coverage, multiple variations, and the complete CG matrix are explicitly out of scope.

## 5. Initial content budget

These are **scope caps/targets**, not a mandate to fill every slot if the narrative does not need it.

| Area | Vertical-slice target |
|---|---|
| Hub communities | 1 |
| Adjacent explorable region | 1 |
| Compact points of interest | 3 |
| Main quest stages | 8–9 linked stages/beats |
| Optional discovery/branch | 1 |
| Core allies in the slice | 1 starting companion + up to 1 additional ally |
| NPCs with distinct functions | 4–6 |
| Enemy archetypes | 4 |
| Standard combat encounters | 3 |
| Climax encounter | 1 |
| Core resources | 3 |
| Facilities/states | 3 |
| Meaningful management decision | At least 1 |
| Autonomous Expedition | 1 low-risk example |
| Optional adult scene/CG sequence | 0–1 |
| Main ending states | 1 principal resolution with a persistent consequence; no separate full ending branches |

A target can be reduced if its removal preserves the full core loop and thematic proof. Additions require an explicit reason tied to one of the player-facing pillars.

## 6. Narrative state and consequence requirements

The quest graph must use stable IDs for objectives, flags, choices, rewards, unlocks, and outcomes. At minimum, track state for:
- whether Alya has committed to stay;
- what the player learned about the local manifestation and community vulnerabilities;
- how the player prepared for the third solution;
- the chosen approach or contribution priority;
- the unavoidable loss and its specific narrative consequences;
- the Organization/community relationship after the crisis;
- Alya's recognition as leader;
- the first management improvement/assignment;
- Expedition assignment and result.

Do not expose an exact numeric “ending probability.” Communicate consequences through concise descriptions, dialogue, world changes, and available options, consistent with narrative canon.

## 7. Out of scope

The following are deliberately excluded from this slice:
- Completing all of Act I's optional quests or all five acts.
- All ten allies, all Named NPCs, all factions, or full regional politics.
- A complete open world or multi-region network.
- The full enemy/boss/item/skill/facility catalog.
- Final numerical balance or exhaustive edge-case QA.
- Complete H/relationship routes or full adult CG production.
- Final art/audio coverage for every state, full localization, and release certification.
- Advanced management automation, multi-community coordination, and complex Expedition chains.
- Any redesign of closed core architecture unless a demonstrated contradiction is found.

## 8. Acceptance criteria

The vertical slice is complete only when all applicable criteria below are demonstrated in an integrated build:

1. A new player can start, understand the immediate need, complete the main arc, and reach the management transition without external explanation.
2. The local Ferida threat is causally connected to existing vulnerabilities and social/material fragility.
3. The Organization provides real value and a defensible position while remaining internally plural; the conflict is not a simplistic good-versus-evil choice.
4. The player experiences at least one costly choice and one consequence that cannot be erased by selecting the nominally “correct” option.
5. Combat, exploration, rewards, character progression, and quests exchange state through canonical IDs and contracts.
6. The crisis solution depends on community/ally contribution in addition to Alya's abilities.
7. The community state changes and the player makes a consequential management decision.
8. The introductory Expedition, if included, resolves autonomously and remains distinct from a Sidequest.
9. Save/load preserves quest state, choice consequences, party, inventory, resources, facility/assignment state, and Expedition state.
10. Optional adult content can be skipped without blocking the main arc.
11. The main path can be completed without exhausting all optional content.
12. The slice's content is documented and linked to stable IDs; missing art/audio is represented by explicit placeholders rather than ambiguous references.
13. Known balance and edge-case issues are logged for implementation/QA rather than hidden behind undocumented exceptions.

## 9. Production sequence and dependencies

Follow this sequence to minimize rework:

1. **Quest graph and narrative states:** define stages, objectives, dialogue purposes, choices, prerequisites, flags, and the unavoidable loss.
2. **Encounter plan:** assign each encounter a narrative purpose, enemy composition, objective, and expected party state.
3. **Content selection:** select only the skills, effects, enemies, items, allies, NPCs, resources, and facilities required by the graph.
4. **Stable-ID integration:** connect quest, combat, reward, character, community, and asset references.
5. **UI minimum specification:** hub, dialogue/choice, exploration, combat, inventory/rewards, community management, assignment, and Expedition results.
6. **Asset inventory:** identify required portraits, enemy visuals, environments, cut-ins, UI icons, and the optional CG; assign IDs and placeholders.
7. **Implementation package:** define data validation and integration contracts; implement the slice before expanding content volume.
8. **Playtest and QA:** validate the main path, meaningful choices, state persistence, system integration, and usability. Tune balance here rather than pretending provisional values are final.
9. **Scope review:** only after the slice is playable, decide which systems/content should be expanded next.

## 10. Definition of done

The slice is **production-ready to implement** when:
- the narrative quest graph and all required states are authored;
- every required content entry has a stable ID, owner/source-of-truth, and enough data for implementation;
- every encounter and management decision has a purpose and an acceptance test;
- required UI states and asset placeholders are inventoried;
- dependencies and explicitly deferred work are documented.

The slice is **playable-complete** only after the integrated acceptance criteria in Section 8 pass. These are separate gates: authoring this document does not imply either implementation or runtime validation is complete.

## 11. Relationship to other project documents

- Narrative canon: `docs/NARRATIVE_CANON.md`
- Project state and roadmap: `docs/PROJECT_STATE_AND_ROADMAP.md`
- GDD index: `docs/GDD_INDEX.md`
- Architecture: `docs/architecture/GAME_ARCHITECTURE.md`
- Implementation contracts: `docs/IMPLEMENTATION_SPEC.md`
- Skill catalog and production handoff: `implementation_spec/SKILL_CATALOG.md`, `docs/systems/combat/SKILL_CATALOG_PRODUCTION_HANDOFF.md`
- Character identity and rosters: `docs/characters/CHARACTER_BIBLE.md`, `docs/characters/ALLIES_ROSTER.md`, `docs/characters/NPCS_DESIGN.md`
- Art references: `docs/art/CHARACTER_IMAGE_PROMPTS.md`, `docs/art/CHARACTER_EROTIC_CG_MATRIX.md`

---

**Current decision:** Use this scope as the production baseline for the first vertical slice. The next content-design artifact should be the **Act I vertical-slice quest graph**, followed by encounter definitions and the minimum linked content catalog. Do not reopen closed architecture decisions without concrete evidence of a contradiction.
