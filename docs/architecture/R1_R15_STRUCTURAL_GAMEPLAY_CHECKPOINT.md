# R1–R15 Structural Gameplay Checkpoint

## Purpose and status

This document records the structural decisions established during the R1–R15 decision sequence. It is a historical checkpoint for traceability and does not replace `GAME_ARCHITECTURE.md` as the current architecture source of truth.

Where specialized documents already exist, they remain the source for concrete content. This checkpoint defines the decision state reached at the end of R1–R15; later convergence decisions are recorded below and consolidated into the current architecture.

---

# 1. Core playable structure

The game is built around an interconnected loop:

1. advance the narrative and unlock the world;
2. explore regions and complete encounters;
3. acquire resources, characters, equipment, knowledge and opportunities;
4. return to the community;
5. assign residents, develop facilities and improve the roster;
6. choose the next direction of progression.

Narrative progression, exploration, combat and community management are intentionally interdependent. No major subsystem should exist as an isolated minigame.

## Scope principle

The project should prefer reusable systemic structures over a large number of bespoke mechanics. A feature that requires a new UI layer, balancing model, failure model, content pipeline and testing burden should not be added without a clear structural need.

---

# 2. World, regions and exploration

- The world is divided into structurally distinct regions.
- Some regions are available from the beginning; others unlock through specific acts or Main Quest progression.
- Regions may remain relevant after later acts through resources, quests, characters, production or optional exploration.
- The project uses procedural generation extensively for general exploration, collection maps and some quests.
- Handcrafted maps are reserved for narratively important locations, important exploration spaces and encounters where bespoke design materially improves the experience.
- Regional access is one of the primary tools for progression gating.
- Some resources should visibly remain unavailable until the player progresses far enough to reach their associated region, allowing the player to infer that Main Quest advancement is required.
- Areas strongly influenced by the Organization or the Wound may use more unusual or unstable encounter structures, but broad systemic escalation should remain controlled.

---

# 3. Community and facilities

Facilities may be specialized rather than universally modular. Some buildings justify modules or tiers; others should perform their complete role as soon as they are built.

The player can destroy or relocate constructions. Community layout should therefore remain adjustable rather than permanently locked after placement.

Open-area constructions such as gardens or plantations are valid facility types. Multiple constructions of the same general category may coexist when they support different planted or configured outputs.

Some functions deserve dedicated structures, including major recruitment, quest, community-state and development functions.

## Character development facility

A dedicated community facility supports shared development of combat-capable allies. It provides collective upgrades, training infrastructure and unlock opportunities, while preserving individual character progression.

---

# 4. Population architecture

Community entities are separated by function rather than by whether they originated as NPCs or enemies.

## Main categories

### Main and narrative characters
Important named characters with significant narrative identity.

### Specialized residents
Named or mechanically distinctive residents with specific roles, aptitudes, services or production functions.

### Generic workers
Less individually developed residents intended primarily for assignments and scalable community work.

### Recruitable combat entities
Entities whose combat or narrative conditions can open a recruitment path. Recruitment origin does not prevent combat participation.

## Assignment and aptitude
Characters may have natural aptitudes for particular community functions. Experience gained while performing a role remains permanently acquired even if the character later changes assignment.

---

# 5. Ally and party structure

Alya is the fixed protagonist. Standard expeditions use Alya plus one selected ally, with narrative exceptions.

The structural target is approximately 6–8 major allies in addition to Alya, supplemented by eligible integrated entities and selected combat-capable NPCs.

Character power combines individual adventure experience, individual development, shared community upgrades, equipment, skills, and build choices. Expedition participation pauses the character’s community assignment for that expedition.

---

# 6. Enemy architecture

The current model separates:
1. identity/family;
2. combat role;
3. power/progression band;
4. encounter class;
5. narrative role;
6. regional or special variants;
7. recruitment/rehabilitation eligibility.

The old mixed use of “Tier” as both importance and power is deprecated.

Organization and Wound are transversal influences. Encounters may resolve through dialogue, choices, avoidance, alternative resolution, combat, or recruitment/rehabilitation paths.

---

# 7. Encounter hierarchy

Normal -> Elite -> Mini-Boss -> Boss.

Elites may be strengthened base enemies, procedural variants, or occasional unique entities. Mini-bosses may be unique, recurring, or procedural. Bosses use distinctive skills, behavior, selective mechanics, and narrative/environmental context rather than inflated stats alone.

Non-combat encounter archetypes and broad alternate boss versions remain Maybe / Future Expansion.

---

# 8. Quest architecture

Quests are Main Quest, Regional Quests, Character Quests, Handcrafted Sidequests, and Reusable/Procedural Tasks.

Some optional quests may permanently unlock characters, facilities, regions, vendors, production options, or other opportunities. Narrative quests generally are not artificially capped; reusable tasks may be.

Some rewards are revealed while others remain uncertain. Content should not disappear arbitrarily, although meaningful choices may produce permanent divergent outcomes.

---

# 9. Economy and trade

Gold supports purchases, seeds/materials, services, selected construction costs, and selected upgrades or fees without becoming universal.

Resources may combine crafting, economic, strategic, and flexible roles. Vendors have specialized inventories; basic goods may be unlimited while selected goods are limited or refreshed.

Resource sinks include buildings, upgrades, equipment, development, production, trade, and optional optimization.

---

# 10. Progression and gating

The Main Quest is the principal progression gate, supported by regions, characters, resources, knowledge, and system prerequisites.

Exploration and investment strengthen the player but do not replace structural narrative advancement. Advanced facilities may require combinations of narrative progress, resources, and relevant characters or knowledge.

---

# 11. Time, cycles and assignments

The core model uses a simple day/night cycle. Assignments may be continuous or cycle-based. Configured community processes can advance through controlled events without a full real-time simulation.

Waiting is allowed in safe locations. Permanent time pressure is exceptional rather than default.

---

# 12. Defeat, risk and recovery

Defeat primarily uses a narrative retreat/consequence model. Secured and unsecured expedition rewards may be distinguished. Temporary conditions and community recovery infrastructure create consequences without systemic permadeath.

Voluntary retreat follows safe-location and out-of-combat rules and does not grant quest completion rewards when the quest requires successful completion.

A general expedition fatigue/escalating-risk system remains Maybe / Future Expansion.

---

# 13. Information architecture and UX principles

Known requirements are shown; undiscovered requirements remain hidden or hinted. The primary readable stat layer is deliberately small. Assignments provide understandable estimates and contributing factors.

A progressively unlocked codex and contextual cross-system navigation become available after discovery. System rule: discover -> make available -> explain -> reveal additional depth progressively.

---

# 14. Cross-system integration rules

- Main Quest progression gates world and systemic expansion.
- Regions provide enemies, resources, quests, and opportunities.
- Combat can lead to rewards, narrative outcomes, or rehabilitation eligibility.
- Dialogue and choices may alter encounters, quest resolutions, rehabilitation, and integration.
- Integrated entities can contribute to the community and, when eligible, expeditions.
- Community facilities improve production, recovery, curse removal, rehabilitation/integration, and collective development.
- Individual adventure experience and shared community upgrades coexist.
- Assignments create opportunity costs because expedition participants pause community work.
- Quests bridge narrative and permanent systemic unlocks.
- Economy connects exploration, production, vendors, buildings, and optimization.

---

# 15. Scope-controlled future candidates

1. specialized non-combat encounter archetypes such as pursuit or survival;
2. alternate narrative versions of bosses;
3. general expedition fatigue or escalating risk.

These are possibilities, not current mandatory features.

---

# 16. Post-convergence resolutions

The convergence audit identified two genuine conflicts and several documentation/schema inconsistencies. The following decisions resolve them:

## Cursed equipment
A dedicated community structure can remove a cursed item from the player. Removal does not cleanse or destroy the curse: the item remains cursed and can be voluntarily equipped again later. Cursed equipment is therefore a meaningful commitment but not a permanent player trap.

## Combat recruitment and rehabilitation
A successful combat recruitment condition opens eligibility for a rehabilitation path rather than granting instant community membership. Rehabilitation requires dedicated community infrastructure and may include recovery, dialogue, integration, and other context-appropriate steps. It should not be modeled as automatic personality overwrite.

## Enemy classification
The old mixed “Tier” terminology is retired. Enemy data should distinguish power/progression band, encounter class, and narrative role.

## Character stats
Only eight values are mechanically central: Body, Agility, Soul, Charm, Dominance, Submission, Sadism, and Masochism. Other values are secondary tracking/history data and must not form a competing primary stat layer.

## Governance
`GAME_ARCHITECTURE.md` is the current high-level architecture source of truth. This file remains a historical checkpoint for traceability.

---

# 17. Checkpoint state

R1–R15 and the immediate convergence resolutions are closed. Remaining work should focus on genuine specification gaps and implementation contracts rather than reopening settled macro-systems without evidence.
