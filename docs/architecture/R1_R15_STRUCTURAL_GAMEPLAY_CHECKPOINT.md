# R1–R15 Structural Gameplay Checkpoint

## Purpose and status

This document records the structural decisions established during the R1–R15 decision sequence. It is a checkpoint and architectural reference, not a replacement for specialized source documents covering narrative, skills, resources, enemies, buildings, NPCs, or implementation details.

Where specialized documents already exist, they remain the source for concrete content. This checkpoint defines how those content domains fit together.

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

## Facility principles

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

Important named characters with significant narrative identity. Some may be combat-capable; others may remain community or narrative focused.

### Specialized residents

Named or mechanically distinctive residents with specific roles, aptitudes, services or production functions.

### Generic workers

Less individually developed residents intended primarily for assignments and scalable community work.

### Recruitable combat entities

Entities recruited through special combat or narrative conditions. Recruitment origin does not prevent combat participation.

A recruitable enemy can therefore become a normal community member with assignments and, when appropriate, expedition capability.

## Assignment and aptitude

Characters may have natural aptitudes for particular community functions. Experience gained while performing a role should remain permanently acquired even if the character later spends time in a less suitable assignment.

Natural aptitude affects efficiency or learning, but should not erase the value of accumulated experience.

---

# 5. Ally and party structure

## Expedition party

Alya is the fixed protagonist. Standard expeditions use:

- Alya;
- one selected ally.

Some narrative segments may require a specific companion, provide a temporary ally, separate the usual partner or otherwise override the standard composition.

## Combat-capable roster

The structural target is approximately 6–8 major allies in addition to Alya, supplemented by eligible recruitable entities and selected combat-capable NPCs.

Examples already identified as appropriate combat-capable NPC types include the Ranger and Witch.

Not every important character must be a combat companion.

## Identity

Allies have distinct combat identities but may partially overlap. Identity should be based on primary tendencies, secondary tendencies, signature mechanics and character-specific skills rather than rigid class exclusivity.

## Progression

Character power is composed of:

- individual adventure experience;
- individual character development;
- shared community upgrades;
- equipment;
- skills and build choices.

Individual experience is gained through adventures and relevant gameplay. Shared development infrastructure helps the roster progress collectively and prevents newly acquired characters from being permanently unusable simply because they were recruited later.

## Assignments versus expeditions

A character accompanying Alya has their community assignment paused for the duration of the expedition.

---

# 6. Enemy architecture

Concrete enemy content must build on the specialized enemy documents and roster already present in the repository.

The structural model is:

1. identity or family/type;
2. combat role;
3. tier or threat level;
4. regional or special variants.

Existing categories such as Civilized, Tribal, Savage, Undead and Loner should be treated as useful identity foundations rather than discarded and replaced by an unrelated taxonomy.

## Regional reuse

Base enemy entities may reappear across regions with meaningful regional variants, altered behavior, modified skills or different rewards.

The target is roughly 6–8 broad conceptual families, interpreted through the existing roster rather than requiring a complete rewrite of it.

## Recruitment

Recruitment can occur across multiple families when their specific conditions are satisfied. It is not restricted to a single biological or social category.

## Organization and Wound layers

The Organization and the Wound are primarily transversal influences rather than mandatory peer families.

The Organization may provide:

- unique enemy archetypes;
- modified or aligned variants of existing entities.

The Wound may provide:

- unique entities;
- altered existing entities;
- environmental effects and hazards;
- encounter instability.

## Non-hostile entities

An encounter does not have to resolve automatically through combat. Depending on entity state and context, available resolutions may include:

- dialogue;
- choices;
- avoidance;
- alternative resolution;
- combat;
- recruitment paths.

This explicitly integrates the existing dialogue and choice architecture with enemy encounters.

---

# 7. Encounter hierarchy

The standard threat hierarchy is:

1. Normal;
2. Elite;
3. Mini-Boss;
4. Boss.

## Elites

Elites may be:

- strengthened versions of normal enemies;
- variants with additional skills or modifiers;
- procedurally generated variants;
- occasional handcrafted unique entities.

## Mini-bosses

Mini-bosses may be:

- unique;
- recurring;
- procedural.

## Bosses

Bosses should have recognizable identity through a combination of:

- unique skill sets;
- distinct behavior;
- selective encounter mechanics when justified;
- narrative or environmental context.

Bosses should not be defined merely as enemies with inflated statistics.

Boss defeat is not necessarily the permanent disappearance of the entity. Selected bosses may later return narratively, appear in optional content or become recruitable allies.

## Explicit scope controls

The following are not part of the mandatory core architecture:

- a broad catalog of non-combat encounter archetypes such as pursuit or survival systems;
- alternate versions of every boss tied to narrative progression.

Both remain **Maybe / Future Expansion**. They may be added selectively if a later need justifies the implementation cost.

---

# 8. Quest architecture

Quests are divided into:

- Main Quest;
- Regional Quests;
- Character Quests;
- Handcrafted Sidequests;
- Reusable / Procedural Tasks.

## Main Quest

The primary narrative and structural progression axis.

## Regional Quests

Important content tied to particular world regions.

## Character Quests

Content centered on individual characters and potentially requiring the relevant character to participate.

## Handcrafted Sidequests

Optional authored content. Some may permanently unlock characters, facilities, regions, vendors, production options or other systemic opportunities.

## Procedural tasks

Reusable tasks or events support ongoing activity without replacing authored narrative content. These may have active-task limits, while narrative quests generally should not be artificially capped.

## Reward information

Some quests reveal rewards while others preserve uncertainty. When appropriate, the player should at least know the reward category or major progression opportunity.

## Failure and choices

The general rule is that content should not disappear arbitrarily. Important choices may nevertheless create permanent divergent outcomes.

## Companion relevance

Quests may:

- require a specific character;
- provide benefits for bringing a specific character;
- unlock alternate dialogue;
- alter rewards or resolutions.

---

# 9. Economy and trade

## Gold

Gold is a conventional currency used for:

- item purchases;
- seeds and selected materials;
- services;
- selected construction costs;
- selected upgrades or fees.

Gold should not become a universal requirement for every system.

## Resource categories

Resources may combine roles:

- crafting or production materials;
- economically valuable goods that can be sold;
- strategic progression resources;
- flexible multi-use resources.

The economy should avoid encouraging the accidental sale of irreplaceable progression materials.

## Vendors

Vendors have their own specializations and inventories while some broader progression may affect availability.

Stock behavior is mixed:

- basic goods may be unlimited;
- selected goods may have limited stock;
- selected stock may refresh through cycles or progression.

## Gold sources

Relevant sources include:

- quests;
- combat rewards;
- selling resources or items;
- production;
- trade opportunities.

No single source should invalidate the others.

## Resource sinks

Resource accumulation is controlled primarily through useful sinks rather than hard storage limits:

- buildings;
- upgrades;
- equipment;
- character development;
- production;
- trade;
- optional optimization.

Costs may scale selectively where useful.

---

# 10. Progression and gating

The Main Quest is the principal progression gate, supported by:

- regional access;
- character requirements;
- resources;
- system prerequisites.

Advanced facilities may require a combination of narrative progress, resources and relevant characters or knowledge.

The player should be able to become stronger through exploration and investment, but unrestricted grinding should not replace structural narrative advancement. Soft caps and structural unlocks are preferred over rigid level gating or universal world scaling.

The Main Quest can unlock:

- regions;
- systems;
- constructions;
- characters;
- resources.

The player should receive systemic and narrative hints when further Main Quest progress is required, without relying on constant explicit warnings.

Older content should remain selectively relevant without requiring every region to receive a full redesign in each act.

---

# 11. Time, cycles and assignments

The core time model uses a simple explicit day/night cycle rather than a detailed calendar.

Assignments can be either:

- continuous;
- cycle-based.

While Alya is away, previously configured community processes may continue according to controlled progression events or time advancement rules. The game should not require a full real-time simulation of the community.

Waiting or time acceleration is permitted in safe locations rather than universally.

Permanent time pressure is not the default. Specific events may create urgency, but ordinary exploration should not cause arbitrary quest loss.

---

# 12. Defeat, risk and recovery

## Standard defeat philosophy

Defeat should use a narrative retreat/consequence model rather than a generic Game Over as the primary result.

The defeat and recovery presentation should remain consistent with the game's established adult/lewd thematic direction, while preserving the previously established non-consensual-content boundaries.

## Resource loss

The recommended model distinguishes:

- secured rewards;
- unsecured rewards obtained during the current expedition.

Failure may cost controlled expedition progress rather than permanently deleting broad player progress.

## Temporary consequences

Characters may receive temporary conditions or require recovery through community infrastructure. The consequence should create meaningful recovery decisions without becoming devastating persistence.

## Permadeath

There is no systemic permadeath for the standard gameplay loop.

## Voluntary retreat

The player may leave an expedition according to safe-location and out-of-combat rules.

Leaving an expedition before its required completion does not grant quest rewards when the relevant quest requires successful completion.

## Explicit scope control

A general risk-escalation or expedition-fatigue system is not currently part of the mandatory architecture. It remains **Maybe / Future Expansion**.

---

# 13. Information architecture and UX principles

## Construction requirements

The player sees known requirements for unavailable content. Unknown requirements remain hidden or are represented through hints rather than fully exposing undiscovered systems.

## Character and assignment information

The game should expose both:

- a deliberately small, readable set of core stats;
- summarized aptitude and role information.

The player should not need to manage an excessive number of statistics, but important underlying values should remain inspectable where useful.

## Assignment prediction

Assignments should provide estimates or ranges rather than always presenting exact deterministic output. Relevant positive and negative contributing factors should be understandable.

## Codex

A progressively unlocked codex may cover:

- characters;
- enemies;
- resources;
- regions;
- buildings;
- important discoveries.

The codex is a player memory and navigation tool, not a requirement to create an exhaustive encyclopedia.

## Cross-system navigation

Once information has been discovered, the player should be able to navigate relevant relationships, such as:

- where a resource can be obtained;
- which facilities use it;
- which characters are suitable for an assignment.

Discovery precedes convenient systemic navigation.

## Notifications

Notifications should prioritize important community events and allow configuration of notification detail where practical.

## System discovery rule

The general rule is:

1. discover a system;
2. make it available;
3. provide an explanation;
4. reveal additional depth progressively.

The game should avoid both hiding critical mechanics indefinitely and overwhelming the player with a large tutorial dump.

---

# 14. Cross-system integration rules

The following relationships are intentional architectural rules:

- Main Quest progression gates portions of world access and systemic expansion.
- Regions provide enemies, resources, quests and progression opportunities.
- Combat can lead to rewards, narrative outcomes or recruitment.
- Dialogue and choices may alter enemy encounters, quest resolutions and recruitment.
- Recruited entities can contribute to the community and, when eligible, the combat roster.
- Community facilities improve production, progression and collective character development.
- Individual adventure experience and shared community upgrades coexist.
- Assignments create opportunity costs because expedition participants pause their community contribution.
- Quests can bridge narrative and permanent systemic unlocks.
- Economy connects exploration, production, vendors, buildings and optional optimization.
- UX should reveal discovered relationships so the player can make informed progression decisions.

---

# 15. Scope-controlled future candidates

The following concepts are explicitly preserved as possibilities rather than current mandatory features:

1. specialized non-combat encounter archetypes such as pursuit or survival systems;
2. alternate narrative versions of bosses;
3. a general expedition fatigue or escalating-risk system.

These features should only be promoted into the implementation plan after a concrete gameplay need demonstrates that the existing architecture cannot satisfy the intended experience.

---

# 16. Final checkpoint state

R1–R15 closes the current structural gameplay-planning sequence.

The next recommended stage is not another open-ended series of feature batches. It is a convergence audit that cross-checks this checkpoint against the existing repository sources for:

- narrative;
- skills;
- resources and ecology;
- buildings and facilities;
- population and NPCs;
- enemies;
- quests;
- regions and procedural generation;
- economy;
- progression and gating.

The goal of that audit is to identify genuine contradictions, redundant structures, missing interfaces between systems and remaining architectural decisions—not to reopen settled decisions without evidence that they conflict with the project as a whole.
