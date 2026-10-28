# AHTW — Complete Implementation & Engineering Dossier

**Audience:** Unity/gameplay programmers, technical designers, technical leads, integration engineers, QA, and coding agents.
**Purpose:** self-contained implementation handoff containing architecture, contracts, acceptance/checkpoint notes, current status, narrative context, full structured content catalogs, Act I vertical-slice data, and normalized skill catalog.
**Critical status warning:** these documents describe intended behavior and an implementation plan. They do **not** prove that a Unity project, runtime systems, scenes, builds, or automated tests already exist or pass. Repository reconnaissance is the first task.

## Non-negotiable first task: inspect the actual checkout
Before creating, moving, or rewriting code, report:
1. Repository root, branch, and Git status.
2. Whether a Unity project exists; locate `Assets/`, `Packages/manifest.json`, `ProjectSettings/ProjectVersion.txt`, and `.asmdef` files.
3. Unity/editor version, packages, input/UI/render pipeline, and target platform assumptions.
4. Existing C# source, scenes, prefabs, ScriptableObjects, tests, CI, and build configuration.
5. Asset folders and import/loading conventions.
6. CSV/JSON catalogs, validators, and legacy ID overlaps.
7. Which acceptance criteria are satisfied, partial, or absent, with path evidence.
8. A concise `RECONNAISSANCE_REPORT.md` or project-state update, including risks and the smallest viable first milestone.

Do not assume a conventional Unity root exists. If it is absent, report that and propose the smallest explicit bootstrap plan before creating one. Do not create a second Unity project beside an existing one. Do not begin broad implementation before reconnaissance.

## Engineering rules
- Preserve canonical IDs and schema contracts. Treat missing or conflicting data as a validation error to report, not an invitation to guess.
- Separate authored content, runtime state, presentation, and save data. Keep one canonical source of truth for stats and effects.
- Prefer data-driven definitions and validators over duplicated hard-coded catalog values.
- Keep gameplay resolution deterministic and testable without UI or scene dependencies.
- Use explicit events/state transitions for quest progression, effects, combat resolution, facilities, resources, expeditions, and endings.
- Do not treat authored JSON or Markdown as proof of runtime integration.
- Skill numeric values are provisional where specified; tune only after integration and balance testing.
- Embedded source sections are included for offline review; the dossier is intended to be independently readable.

## Current baseline
- 5 acts; 47 main quest stages; 25 sidequests; 7 regions; 6 factions; 10 recruitable allies; 21 named recurring NPCs; 12 generic NPC templates; 35 enemy archetypes; 9 major bosses; 8 special encounters; 12 facilities; 8 resources; 36 canonical items/equipment records; 8 Alya outfits; 8 Expedition templates; 5 ending families; 67 canonical skill records.
- Vertical slice: “The Water We Share,” Brackenford in Ashfen Verge, local Ferida manifestation “The Red Thread.”
- The lower-terrace seed reserve and much of the next planting cycle are lost during stabilization; the settlement survives and downstream water is protected. No route is a cost-free victory.
- Communities should become capable of surviving without Alya. Ferida amplifies vulnerability but does not erase agency. The Organization is necessary and competent, internally diverse, and structurally prone to calculation and prioritization.
- Combat: Vitality is the primary defeat meter; Strain is secondary pressure; Command, Resolve, Pressure, and Fortitude are tactical resources. Resolution is deterministic; effect lifecycle and finisher outcomes are explicit.
- All characters are adults. Intimacy is optional and never gates core progression; power imbalance or vulnerability never implies consent.

## Recommended implementation sequence
1. Repository reconnaissance and evidence-based status report.
2. Schema/data validators for world, gameplay, character arcs, skill CSV/JSON, and Act I data.
3. Stable ID registry and migration checks; fail fast on duplicates, missing references, invalid enums, and unresolved dependencies.
4. Pure domain models and deterministic state-transition services for turn resolution, effects, quest flags, inventory/resources, facilities, expeditions, and endings.
5. Unit tests for contracts and edge cases before UI integration.
6. Act I vertical slice: quest graph, dialogue state, choices, effects, encounter, hub/facilities as specified, save/load, and first autonomous Expedition unlock.
7. Content validation tools and QA dashboard for all 5 acts.
8. Only then expand runtime content breadth and tune provisional numbers.

## Acceptance criteria
- A clean checkout can be inspected and launched in the documented Unity version, if a Unity project exists.
- Data catalogs parse with deterministic validators and actionable errors.
- No duplicate canonical IDs; every reference resolves or is marked as an intentional external/runtime dependency.
- Turn resolution follows the documented phase order; identical inputs produce identical outputs.
- Effect duration, stack/strength, expiry, equipment removal, and Overflow guard behavior are covered by automated tests.
- Quest transitions are explicit and replayable; choices change only documented state.
- Ending and finisher outcomes respect encounter permissions and do not imply global victory unless explicitly allowed.
- Save/load preserves canonical state without duplicating derived modifiers.
- Act I mandatory loss and downstream protection are preserved across supported routes.
- Build/test evidence is recorded. Never claim a test passed unless it actually ran and its output was observed.

## Embedded source: Game architecture

# Ayla Heals the World — Architecture Source of Truth

## Status
This document consolidates the approved high-level architecture from the narrative work, Skills Audit, resource/ecology audits A1–A10, audits B–J, the final architecture decision checkpoint, the R1–R15 structural gameplay sequence, and Checkpoint B batches B5–B18. It is the primary reference for future structural decisions. Concrete rosters, recipes, maps, species, quests, and balance values remain intentionally deferred.

# 1. Game Identity
A narrative RPG with light base/community management. The world is structurally sexualized: sexuality is material, cultural, magical, biological, economic, and narrative, not a separate subsystem. Adult content should remain consent-oriented and use the same architecture as other gameplay.

The player follows Alya's effort to create conditions under which harmony can exist. The ultimate healing of the world's deep wound is not guaranteed to be witnessed by anyone alive during the story; the outcome depends on long-term change rather than a simple measurable endpoint.

The Wound modifies relationships, ecologies, characters, opportunities, and regions. It is not a default currency, separate economy, or excuse for non-consensual sexualization.

# 2. Canonical System Loop
Narrative Progress
-> unlocks regions, resources, possibilities, facilities, characters, and content
-> Exploration / Sidequests / Encounters / Expeditions / Quests
-> Rewards and discoveries
-> Resources / Items / Gold / Knowledge / Recruitment opportunities
-> Buildings / Production / Equipment / Transmutation / Rehabilitation / Community assignments
-> New capabilities and specializations
-> Further narrative progress.

No major system should become an isolated progression path.

# 3. World, Regions and Exploration
The world is divided into structurally distinct regions. Some regions are available initially; others unlock through specific acts or Main Quest progression. Regions may remain relevant through resources, quests, characters, production, and optional exploration.

The world map is an abstract regional/locality map rather than a tactical movement space. Travel consumes game time. Procedural generation is a major tool for repeatable exploration, gathering maps, and selected reusable quests. Hand-authored maps are reserved for story-critical levels and cases where authored structure adds clear value.

Two external-activity modes are distinct:
- **Sidequest:** directly played by the player; may include exploration, combat, narrative, or other direct gameplay.
- **Expedition:** delegated to available community members and resolved autonomously over time, producing a result/reward/consequence when complete.

Expeditions may have variable party composition, region/progression requirements, non-combat success checks, and automatic return. An expedition does not require player micromanagement once launched.

The standard encounter hierarchy is Normal, Elite, Mini-Boss, and Boss. Power/progression band, encounter class, and narrative role are separate dimensions. The old mixed use of “Tier” as a combination of importance and power is deprecated.

Organization and Wound influence are transversal layers that may modify families, regions, behavior, skills, hazards, and encounter instability.

# 4. Community and Population
Facilities may be specialized rather than universally modular. The player may destroy or relocate constructions. Open-area constructions such as gardens or plantations are valid and multiple constructions of the same category may coexist with different configured outputs.

Community entities are separated by function: main/narrative characters, specialized residents, generic workers, and recruitable combat entities. Alya is the fixed protagonist. Standard **player-controlled expeditions/sidequest parties** may use Alya plus one selected ally, with narrative exceptions; delegated Expeditions are a separate community-management activity and may use one or more eligible community members depending on the expedition.

Each community member has one primary Assignment at a time. Assignments stop functioning while the character is outside the community. Assignment competence has discrete levels and persists permanently. Assignments can grant XP and/or resources/support according to the function. Assignments can be interrupted freely.

Combat-capable allies combine individual adventure experience, individual development, shared community upgrades, equipment, and skills. Assignment experience and learned aptitude are never lost.

Dedicated facilities may support collective ally development, curse removal, recovery, recruitment/integration, and rehabilitation.

# 5. Combat, Skills and Character Data
The Skills Audit remains authoritative for shared combat vocabulary and approved skill families. Combat distinguishes Health Damage and H-damage and supports Kill, Knockout, Capture, Submission, Escape, and Objective Complete as resolution outcomes where applicable.

Exactly eight attributes are mechanically central and should remain the primary readable stat layer:
- Body
- Agility
- Soul
- Charm
- Dominance
- Submission
- Sadism
- Masochism

Body multipliers, preferences, counters, experiences, histories, and similar values are secondary tracking data. They may influence systems but must not become a competing primary stat layer.

Combat has no spatial/grid positioning and no separate range system. Skills define their targeting directly. Targeting may be manual, automatic, or explicitly random. Friendly fire is allowed only when a skill explicitly permits it. Incapacitated characters are invalid targets; Surrendered characters no longer act but remain available for explicitly permitted interactions.

Combat initiative is randomized once at combat start, with Agility modifying the chance to act earlier. The resulting turn order remains fixed for the encounter.

A skill may contain an ordered list of effects. Effects may have dependencies. Conditions are reusable. Skills may have explicit costs using any valid resource, including HP. Invalid targets cause the action to fail rather than automatically retarget. Targeting supports reusable patterns plus skill-specific exceptions. Criticals are resolved as part of the modifier pipeline.

HP is conceptually the character's remaining physical capacity/exhaustion tolerance, not a literal measure of wounds. Reaching 0 HP immediately causes Incapacitated. HP recovery is passive and may be modified by facilities, skills, and status effects.

Equipment-derived effects disappear immediately when equipment is removed. Do not create duplicate status-effect lifecycles or parallel combat currencies.

# 6. Combat State, Effects and AI
Temporary, Permanent, and Conditional durations are supported. Effects use explicit stacking groups and stacking policies; effects in different stacking groups may coexist and accumulate. Strongest Wins is the default policy where effects compete unless a specific effect defines another policy.

Effects carry source tracking. Cleanse/dispel can operate through tags. Death/removal and equipment removal immediately remove applicable source-bound effects. Effective values recalculate immediately after modifier changes.

Modifiers may be absolute or percentage-based. Modifier ordering is deterministic by modifier category rather than arbitrary per-effect priority. Global safety caps and stat/effect-specific caps may coexist. Effective primary stats do not fall below zero.

Enemy Intent has variable visibility by enemy/skill. The next intent is determined/revealed during the preceding turn, giving the player actionable information. Once revealed, intent is locked. AI uses deterministic priorities plus weighted/equivalent choices and considers the full combat state, including H-gauge. Personality and AI Profile remain separate concepts. Finishers are legal only when their target satisfies the relevant threshold/conditions, while AI choice remains profile-dependent.

A Surrendered combatant no longer acts. Surrender can occur before 0 HP and remains distinct from Incapacitation while both count as being out of active combat.

Combat ends when all members of one team are either Surrendered or Incapacitated, in any combination. Post-combat resolution determines the contextual result such as kill, knockout, capture, submission, or other encounter-specific outcome.

# 7. Character Progression
Characters have Level and XP. Level grants Skill Points and a small amount of base growth/unlocks, but is not the sole source of attribute development.

Attributes have direct/distributable growth plus natural growth. Natural growth is influenced by actual play: skill usage, context/results, and community role. Species provides attribute predisposition rather than a hard lock. Natural Aptitude is visible and influences growth through curves. Characters can exceed natural aptitude with diminishing returns. Each character has individual potential; training/equipment may temporarily exceed that potential.

Skills are learned through a hybrid model: Skill Points are required for activation, while some skills additionally require training, community buildings, events, or other context gates. Skills do not have levels. Unlocked skills remain permanently known.

Characters have a limited active-skill loadout with base slots plus modifiers. Passives use a separate limited pool. H-skills share the normal active-skill slots with all other skills. Loadouts are locked during combat, can be changed outside combat, and support presets. Skill Point respec is possible with cost/condition.

# 8. Recruitment and Rehabilitation
Combat recruitment does not imply instant membership. A successful combat-specific recruitment condition may instead open an eligibility path for post-encounter rehabilitation.

The canonical flow is:

Encounter
-> Eligibility condition
-> Capture, surrender, recovery, or other post-encounter state as context permits
-> Rehabilitation / integration facility and process
-> Community membership when the process succeeds
-> Assignments and, when eligible, delegated Expedition participation.

Rehabilitation is a community system requiring dedicated infrastructure. Its implementation must remain compatible with the project’s consent-oriented boundaries and should not be treated as automatic personality overwrite.

Dialogue and choices may alter eligibility, outcomes, integration paths, and alternative resolutions.

# 9. Items, Equipment, Curses and Transmutation
Item categories are Resources, Components, Consumables, Equipment, and Narrative/Unique Items. Equipment should change choices, playstyle, interactions, defenses, roles, or capabilities.

Equipment may modify skill values and explicitly supported skill properties/structure. Skill transformations must be declarative and constrained to capabilities supported by the skill/effect schema rather than arbitrary per-item scripts. This is particularly important for cursed equipment, where a very powerful transformation can be balanced by a meaningful curse/trade-off.

Transmutation is one modification system emphasizing specialization and trade-offs. Respec and build changes are available through facilities or specific moments with light friction and cost.

Cursed equipment is a meaningful commitment, not a permanent unknowable trap. A dedicated community structure can remove cursed items from the player. Removal does not cleanse the item: the item remains cursed and may be equipped again voluntarily later. Curses therefore remain part of item identity while player commitment to wearing them is reversible through community infrastructure.

# 10. Resources, Economy and Trade
Recurring resources remain intentionally few. Gold is conventional currency for purchases, selected services, selected construction costs, and selected upgrades; it is not universal.

Resources are organized in layers: a small set of fundamental resources plus specialized resources as progression expands. Resources have storage/capacity behavior, with the exact footprint defined per resource type where needed rather than assuming identical storage units for everything.

Food is consumed continuously as community upkeep. Gold and barter coexist in appropriate contexts. Resources can be sold subject to resource-specific restrictions. External trade exists and may have variable inventories/prices. Resources do not have their own quality/rarity tiers; item rarity belongs to items/equipment where applicable.

Resources may simultaneously be crafting/production materials, economically valuable goods, strategic progression resources, or flexible multi-use goods. The economy should avoid encouraging accidental loss of irreplaceable progression materials.

Vendors have specialized inventories; basic goods may be unlimited while selected goods are limited or refreshed by cycles/progression. Gold sources include quests, combat rewards, selling resources/items, production, and trade opportunities.

Resource accumulation is controlled primarily through useful sinks: buildings, upgrades, equipment, development, production, trade, and optional optimization.

# 11. Buildings, Ecology and Production
Resource-facing buildings primarily provide Access, Stability, Conversion, or Specialization. A standalone building must introduce a distinct player choice; otherwise prefer upgrades, modules, rooms, event unlocks, or visual variation.

The community has a physical layout/map with expandable space. Buildings may have upgrades/tiers when appropriate; others are unique. Construction requires resources, time, and prerequisites. Workers can participate and modify construction efficiency/results. Buildings may be passive or worker-dependent according to their design. Destruction/relocation is possible with a cost.

Adult facilities follow the same architectural rules. Community production provides stability and predictability rather than upkeep punishment. Ecology uses renewable, cyclical, variable, contextual, and unique acquisition patterns without mandatory detailed farming simulation or universal depletion bars.

# 12. Quests, Events, Progression and Gating
Quests are Main Quest, Regional Quests, Character Quests, Handcrafted Sidequests, and Reusable/Procedural Tasks. Quests have persistent states and may contain multiple objectives. Objective retroactivity is determined per objective.

Events use a hybrid deterministic/random model. Persistent world changes may be temporary or permanent. NPC relationships are persistent. Narrative choices can have real gameplay consequences. World state is hybrid: global flags/state coexist with local quest state.

The Main Quest is the principal progression gate and can unlock regions, systems, constructions, characters, and resources. Regional access, character requirements, resources, knowledge, and system prerequisites support that axis.

Players may optimize and explore within the current layer, but unrestricted grinding should not replace narrative advancement. Advanced content may combine narrative progress, resources, and relevant characters or knowledge.

Some quests reveal rewards; others preserve uncertainty. Major reward categories may be previewed when useful. Content should not disappear arbitrarily, although important choices may create permanent divergent outcomes.

# 13. Time, Day/Night, Defeat and Recovery
Game time uses multiple scales and includes an explicit day/night cycle and calendar from the start. Time advances only through explicit player-controlled progression; being idle in menus does not advance the world.

The player may advance to a chosen next time boundary such as evening or the following day. Long-running activities such as construction, production, recovery, assignments, travel, and expeditions progress while time advances; they do not require the player to remain on a single screen.

Production is rate-based per unit of game time. Assignments can be continuous/cycle-based according to the activity. Waiting is allowed in safe locations. Permanent time pressure is not the default.

H-gauge decays outside combat toward a baseline. Contextual modifiers can increase or decrease this behavior. The exact decay curve and baseline are tuning/specification work.

Defeat uses narrative retreat/consequence rather than generic Game Over as the primary model. Secured rewards are distinguished from controlled unsecured expedition rewards. Temporary conditions and recovery infrastructure may create meaningful consequences without systemic permadeath.

Voluntary retreat follows safe-location and out-of-combat rules. Leaving before a quest’s required completion does not grant that quest’s completion reward.

A general expedition-fatigue/escalating-risk system remains Maybe / Future Expansion.

# 14. Information Architecture
The player sees known requirements for unavailable content while undiscovered requirements remain hidden or hinted.

The game should expose the eight core stats plus summarized aptitude and role information without requiring excessive stat management. Assignments provide understandable estimates/ranges and contributing factors.

A progressively unlocked codex may cover characters, enemies, resources, regions, buildings, and important discoveries. Once information is discovered, contextual navigation should reveal relevant relationships such as sources, consumers, requirements, and suitable characters.

System rule: discover -> make available -> explain -> reveal additional depth progressively.

# 15. Quests, Narrative State and External Activities
Sidequests are direct player activities. Expeditions are autonomous community-delegated activities. They may share content primitives, encounter definitions, rewards, and world-state effects, but their control/resolution loops remain distinct.

Quest state is persistent and objective-based. Events and narrative choices may read/write global world state and persistent NPC relationships. Event resolution supports deterministic triggers and controlled randomness.

# 16. Cross-System Integration Rules
- Main Quest progression gates portions of world access and systemic expansion.
- Regions provide enemies, resources, quests, and progression opportunities.
- Combat can lead to rewards, narrative outcomes, or rehabilitation eligibility.
- Dialogue and choices may alter encounters, quest resolutions, rehabilitation, and recruitment/integration.
- Successfully integrated entities can contribute to the community and, when eligible, delegated Expeditions.
- Community facilities support production, recovery, curse removal, rehabilitation/integration, and collective character development.
- Individual adventure experience and shared community upgrades coexist.
- Assignments create opportunity costs because Expedition participants pause their community contribution.
- Economy connects exploration, production, vendors, buildings, and optional optimization.
- UX reveals discovered relationships so players can make informed progression decisions.
- Long-running activities are time-driven but do not monopolize the player's attention while time is advanced.

# 17. Scope Guardrails and Future Candidates
Do not add without demonstrated need: separate adult economy/inventory, separate sexual crafting subsystem, recurring Wound currency, detailed farming simulation, universal processing trees, duplicate combat currencies, universal enemy scaling, or excessive building proliferation.

The following remain possible but non-mandatory:
1. specialized non-combat encounter archetypes such as pursuit or survival systems;
2. alternate narrative versions of bosses;
3. general expedition fatigue or escalating risk.

# 18. Deferred Content
The architecture intentionally does not yet define exact rosters, recipes, maps, species, quest lists, procedural rules, numeric balance, exact capacity limits, exact time-block lengths, exact resource rates, or detailed gate schedules. These are content and implementation specifications, not missing macro-systems.

# 19. Architectural Verdict
PASS. The project has a complete high-level architecture for narrative progression, combat, skills, resources, ecology, exploration, encounters, community management, recruitment/rehabilitation, curses, economy, quests, gating, time, defeat/recovery, adult-content integration, and player information.

Future design should default to: Which existing interface does this idea belong to? A new macro-system requires a demonstrated gap that cannot be solved by content, configuration, specialization, or extension of an existing system.


## Embedded source: Implementation specification

# Implementation Specification — Final Integration Status

## Status
**I1–I11 COMPLETE · I12 COMPLETE**

This specification translates the locked game design into implementation contracts. The final integration audit found no blocking cross-system contradiction.

## Core integration rules

### Combat
- Initiative is randomized once at combat start, with Agility modifying the initial result; the resulting order remains stable.
- Turn start processes start-of-turn effects, duration update/expiration and derived-state recalculation before checking whether the actor can act.
- Surrendered and incapacitated combatants do not act and are represented separately from other character state.
- Combat terminates when all members of one team are Surrendered and/or Incapacitated.
- Atomic actions complete their declared resolution pipeline before terminal combat state is committed.

### Actions and effects
- Insufficient resources make an action unselectable.
- AI preserves its selected action/intent when a target becomes invalid and retargets where possible; invalid actions use an explicit fallback policy.
- Effects are instances with definition, source character/definition, duration, stacks and runtime state.
- Effects use configurable stacking policies and event-driven triggers.
- Trigger recursion is bounded by an execution budget.
- Effect provenance can reference a parent execution/effect without copying the full chain.

### Stats and HP
- HP represents physical exertion/exhaustion rather than literal wounds and may be spent by skills.
- HP is clamped to zero; no overkill state is required or persisted.
- Derived stats are invalidated by mutations and recalculated lazily when queried.
- Temporary modifiers are the shared mechanism for temporary item/buff/debuff/stat changes.

### Skills and targeting
- Gameplay, AI and presentation data are separated.
- Targeting is represented by composable queries with per-skill selection policies.
- Formulas are data-driven and use a constrained expression vocabulary.
- Modifier ordering follows the global deterministic formula policy.
- Minimum damage and accuracy rules follow the locked combat design.

### Equipment
- Equipment is exclusive to the protagonist; allied NPCs do not use equipment.
- Equipment changes occur outside combat.
- Equipment can declaratively transform supported skill properties such as targeting, formula or area behavior.
- Transformation conflicts use explicit priority.
- Cursed equipment uses curse definitions plus active effects and preserves curse state when unequipped.

### Character progression
- Characters have level and experience; level-up supplies skill points.
- Natural growth derives from recorded activity/use and periodic growth processing.
- Skill unlock requirements are data-driven and may include level, skill points, character conditions and community/event gates.
- Passives may be permanent or loadout-based according to definition.
- Aptitude is derived from species, attributes, experience and modifiers.

### Community
- Recruitment, eligibility and rehabilitation/integration are separate states/processes.
- Rehabilitation is progress-driven and can use facilities, assignments and events.
- Community members have availability/assignment states.
- Assignment interruption follows the defined progress/output policy.
- **Expedition = NPC-only delegated activity. Sidequest = activity requiring Alya.**

### Time and economy
- Time is represented internally with continuous timestamps.
- Day/night is a gameplay state and can gate availability.
- Time advancement processes intermediate timestamps chronologically; equal timestamps use explicit event priority.
- Waiting supports semantic and custom durations.
- Facilities, skills and statuses can modify recovery.
- Production and upkeep use the defined time/tick model.
- Inventory has no fixed capacity limit.

### Exploration and quests
- World navigation uses a regional/locality graph.
- Travel duration is affected by route and modifiers.
- Encounters use pools, conditions and weights.
- Sidequests require Alya; Expeditions use NPCs only and resolve through checkpoints.
- Quest state uses a graph with objective progress and configurable completion/failure policies.
- Retroactivity is objective-defined.
- World state includes global/local, quest, relationship and simulation state.
- Relationships support values, flags and stages.
- Choices can modify narrative, gameplay and world state.

### Persistence and determinism
- Saves persist everything required to reconstruct gameplay; reconstructible runtime state is not unnecessarily serialized.
- Combat is not saved mid-resolution.
- Autosave and manual-slot boundaries follow the established design.
- Save schema versioning is independent from general game versioning.
- Migrations are automatic and preserve the original save.
- Persistent randomness retains seed/RNG state and execution information sufficient to reproduce relevant bugs.
- Stable identifiers use semantic IDs plus immutable identity where required.
- Gameplay, balance, localization and presentation data remain separated.

### Cross-system architecture
The canonical sequence is:

`Canonical Mutation → Derived State → Domain Event → Event Handlers → Subsequent Canonical Mutation`

Events do not mutate an uncommitted transaction. Canonical multi-mutation operations are atomic by default, while content may explicitly define partial behavior where appropriate.

Each domain has an explicit source of truth. The specification defines contracts, data instantiates them, and runtime code implements them. New behavior requiring a capability not represented by the existing contracts must update the specification/schema rather than introduce ad-hoc special-case code.

## Production interpretation

The specification is closed for planning purposes. Numerical balance, content volume, asset production, implementation details and ordinary bugs remain production work. A discovery that requires a genuinely new gameplay rule reopens the relevant specification section and is recorded explicitly.


## Embedded source: Structural gameplay checkpoint R1–R15

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


## Embedded source: Unity vertical-slice implementation handoff

# AHTW — Unity Vertical Slice Implementation Handoff

**Working title:** The Water We Share  
**Target:** Maintainable indie-scale Unity implementation, testable and extensible without building a generic framework.  
**Status:** Implementation contract proposal. This document does not claim that runtime systems already exist.  
**Audience:** An implementation LLM/developer working incrementally in the existing repository.

## 1. Mission and success boundary

Implement one integrated, playable vertical slice demonstrating:

**Meet a person in need → investigate a local Ferida manifestation → prepare and fight → make a costly collective decision → change the community → delegate the first autonomous Expedition.**

Canonical story:
- Hub: Brackenford.
- Region: Ashfen Verge.
- Local Ferida manifestation: The Red Thread.
- Water scarcity and unequal rationing predate the supernatural manifestation. The Ferida amplifies exhaustion, fear, and distrust; it does not create every social problem or remove characters' agency.
- The Organization provides genuine expertise and proposes a defensible containment plan, but its plan abandons lower residents and their seed reserve.
- Alya's third solution depends on local knowledge, repair materials, care, and collective effort.
- **Mandatory loss:** the lower-terrace seed reserve and a substantial part of the next planting cycle are lost. Brackenford survives and the downstream channel is secured.
- Alya is recognized as leader, makes an initial facility choice, and launches/resolves one autonomous Expedition.

The slice is not complete merely because scenes can be entered. It is complete when quest progression, combat/objective resolution, persistent state, community management, and the Expedition work together in an integrated build and the acceptance criteria in this document pass.

### Source-of-truth documents

Inspect and follow these documents before implementation:
- docs/VERTICAL_SLICE_SCOPE.md
- docs/vertical_slice/ACT_I_QUEST_GRAPH.md
- docs/vertical_slice/ACT_I_QUEST_GRAPH_CONTINUATION.md
- docs/vertical_slice/ACT_I_DIALOGUE_PACK.md
- docs/vertical_slice/ACT_I_CONTENT_CATALOG.md
- data/vertical_slice/act_i_quests.json
- data/vertical_slice/act_i_content.json
- data/vertical_slice/act_i_effects.json
- docs/NARRATIVE_CANON.md
- docs/architecture/GAME_ARCHITECTURE.md
- docs/IMPLEMENTATION_SPEC.md
- implementation_spec/COMBAT.md
- implementation_spec/TURN_RESOLUTION.md
- implementation_spec/STATUS_EFFECTS.md

If this handoff conflicts with a canonical contract, do not silently create a second rule. Report the exact conflict and update the relevant source of truth before implementing a workaround.

## 2. Non-negotiable engineering principles

1. Domain rules must be deterministic and testable outside Unity scenes wherever practical.
2. Unity is the composition and presentation environment, not the source of gameplay truth. MonoBehaviours collect input, render state, and call application services; they do not independently decide costs, quest outcomes, or rewards.
3. Maintain one source of truth for each piece of state. UI is a projection, never a parallel owner.
4. Use stable IDs for content links, events, save data, and tests. Display strings, scene object names, array indexes, and localized text are not identifiers.
5. Validate content at load/build time. Duplicate IDs, missing references, unsupported effect types, and invalid quest links must produce actionable diagnostics.
6. Commit canonical mutations before publishing domain events. Event handlers must never observe a half-committed transaction.
7. Prefer composition and small interfaces over deep inheritance. Use data-driven definitions and registered handlers for variable behavior.
8. Build only the systems needed by this slice, while leaving clean seams for future content. Avoid speculative frameworks and unrelated refactors.
9. Prefer explicit state transitions, clear error results, small methods, meaningful names, and readable code.
10. Automated validation is part of implementation. Use unit tests for rules, integration tests for cross-system contracts, and a small number of PlayMode tests for Unity wiring.

## 3. Inspect the repository before designing the final code layout

The implementation agent must first establish:
- whether a Unity project already exists and its root path;
- the Unity/editor version and current packages;
- current UI/input approach and coding conventions;
- existing runtime systems, tests, assembly definitions, and CI workflows;
- whether the slice JSON files are already included in the Unity content pipeline.

Do not create a second Unity project root or duplicate existing systems. Adapt the suggested logical layout below to the actual repository.

Suggested logical structure:

    Assets/_Project/
      Scenes/ (Bootstrap, Brackenford, AshfenVerge, Combat as needed)
      Prefabs/
      Art/
      Audio/
      UI/
      Scripts/
        Domain/ (Combat, Effects, Quests, Inventory, Community, Expeditions, World, Persistence)
        Application/ (Commands, Queries, Services, Validation)
        Infrastructure/ (Content, Persistence, Events, Logging)
        Presentation/ (Bootstrap, Exploration, Dialogue, Combat, Community, Expeditions, UI)
      Tests/
        EditMode/
        PlayMode/

If useful, create assembly definitions with conceptual boundaries:
- AHTW.Domain: plain C# models and rules; no UnityEngine dependency.
- AHTW.Application: use cases and orchestration; references Domain.
- AHTW.Infrastructure: JSON loading, save storage, event bus, logging; implements application/domain contracts.
- AHTW.Unity: MonoBehaviours, scenes, UI, audio/visual adapters.
- AHTW.Tests.EditMode and AHTW.Tests.PlayMode.

Fewer assemblies are acceptable if they fit the existing project better. Preserve the conceptual dependency direction and avoid cyclic dependencies.

## 4. SOLID architecture, service locator, and event bus

### 4.1 Dependency direction

Use this direction:

Presentation → Application → Domain  
Infrastructure → Domain/Application contracts

- **Domain:** entities/value objects, invariants, deterministic rules, and state transitions.
- **Application:** orchestrates use cases such as selecting a dialogue choice, resolving an encounter, building a facility, launching an Expedition, and saving.
- **Infrastructure:** JSON files, save storage, clocks/RNG adapters, event dispatch, and logging.
- **Presentation:** Unity scene/UI input and rendering; it does not mutate canonical state directly.

Domain code must not depend on Unity scenes, UI, static singletons, or concrete file storage.

### 4.2 SOLID expectations

- **Single Responsibility:** Quest progression, resource transactions, encounter resolution, content loading, and presentation have separate responsibilities. Do not create a single GameManager that owns all rules.
- **Open/Closed:** Add a supported effect handler without changing unrelated systems. Avoid designing a generic plugin framework without a real need.
- **Liskov Substitution:** In-memory and production implementations of repositories, clocks, RNG, and save stores must honor the same contracts and error semantics.
- **Interface Segregation:** Prefer narrow interfaces such as IQuestRepository, IResourceLedger, IGameClock, IRandomSource, and ISaveStore over a giant IGameService.
- **Dependency Inversion:** Application services depend on abstractions; concrete implementations are wired during startup.

Use interfaces when they create a meaningful seam for substitution/testing. Plain data objects and simple methods do not need an interface merely for style.

### 4.3 Service locator: allowed with guardrails

A small service locator is acceptable for this indie project:
- Register services once from a bootstrap/composition root.
- Prefer constructor injection inside Domain/Application code.
- Restrict locator lookups to Unity composition boundaries and adapters; do not let domain entities call ServiceLocator.Get<T>().
- Register required services explicitly and fail fast with actionable diagnostics if a required service is missing.
- Avoid hidden runtime registration and scattered lookups throughout gameplay code.
- Provide a test composition root using fakes and in-memory implementations.
- The locator resolves services; it must not own mutable gameplay state.

Suggested startup order: load content → validate content → create domain state → register services → restore save or create a new game → initialize presentation → enable player input. If validation fails, prevent entry into an invalid game state and expose diagnostics.

### 4.4 Event bus: facts, not commands

Use a typed event bus for decoupled notifications, not as a replacement for direct calls or all application orchestration.

Rules:
- Events are immutable facts describing something that has already happened, e.g. QuestStageCompleted, ResourceChanged, EncounterResolved, FacilityBuilt, ExpeditionLaunched, ExpeditionResolved.
- Commands express intent and call application services, e.g. ChooseDialogueOption, CommitRepairMaterials, LaunchExpedition. Do not publish a command as if it were a completed fact.
- Publish only after canonical state mutations have committed.
- Preserve deterministic ordering wherever event order affects gameplay.
- Subscribers must be disposed/unsubscribed when a service or view is destroyed. Scene reloads must not accumulate duplicate subscriptions.
- Event handlers may request a subsequent use case but must not mutate an uncommitted transaction.
- Bound effect-trigger recursion using the canonical execution budget.
- Do not use the bus for frame updates, every UI property, or data queries; query current state instead.
- In development builds, log event type, stable IDs, and correlation/transaction ID where useful.

## 5. Content pipeline and IDs

### 5.1 Loading pipeline

The three existing JSON files are the authored content baseline. Use this pipeline:

JSON bytes → DTO deserialization → schema/version checks → ID/reference validation → mapping to runtime definitions → immutable content registry.

Do not use mutable runtime objects as deserialization DTOs. Avoid duplicate sources of truth in ScriptableObjects; use ScriptableObjects only for Unity-facing configuration or authoring features that do not conflict with the canonical JSON.

The registry should support efficient stable-ID lookup and return explicit errors for unknown IDs. Never silently return a default definition when a referenced ID is missing.

### 5.2 ID policy

Preserve canonical IDs, including VS1_*, RESOURCE_*, ITEM_*, FAC_*, LOC_*, POI_*, ENEMY_*, ENC_*, EXP_*, ALYA, ALLY-001, and ALLY-005. Names and prose may change independently; IDs must not.

Validate:
- uniqueness in each namespace;
- all quest, effect, resource, item, facility, location, POI, enemy, encounter, and Expedition references;
- supported enum/handler values;
- required fields and valid numeric ranges;
- quest graph reachability and absence of accidental softlocks.

If an ID must change after it has appeared in saves, provide a migration/alias instead of silently orphaning state.

### 5.3 Effect handlers

Effect IDs in act_i_effects.json are content-level IDs, not permission to invent arbitrary global mechanics. Map supported effect types to small registered handlers. Each handler validates its payload, checks preconditions, applies a canonical mutation through the appropriate service, returns a structured result, and emits events only after commit.

If an effect type is unsupported by the existing implementation contracts, implement a contract-compliant handler or update the canonical schema/specification first. Never invoke arbitrary method names from content via reflection.

Prefer typed DTOs and validated effect payloads over unstructured dictionaries. Unknown effect types must fail validation.

## 6. Domain boundaries and state ownership

| Domain | Owns | Does not own |
|---|---|---|
| World/Quest | quest stages/objectives, flags, choice history, narrative/world states | inventory quantities or combat turn state |
| Characters/Party | party membership, availability, slice-relevant progression and relationship state | dialogue UI or transforms |
| Combat | participants, initiative, intent, meters, effects, objective progress, combat outcome | persistent quest completion policy |
| Inventory/Resources | quantities, item stacks, reservations, atomic cost/reward transactions | dialogue choice policy |
| Community | facility state, assignments, member availability, initial management choice | Expedition resolution internals |
| Expedition | activity ID, assigned member, status, game-time timestamps, deterministic result state | character membership or inventory storage |
| Content registry | immutable definitions loaded from content files | mutable playthrough state |
| Persistence | save DTOs, schema version, migrations | gameplay decisions |

A use case may coordinate multiple domains. For example, Q07 preparation may coordinate resource reservations, quest flags, and encounter modifiers through an application service. It must not let a quest object reach into a scene or UI.

### 6.1 Canonical mutation sequence

Follow the implementation contract:

**Canonical Mutation → Derived State → Domain Event → Event Handlers → Subsequent Canonical Mutation**

- Validate preconditions and all costs before committing.
- Multi-step operations are atomic by default.
- Do not publish events for a failed or rolled-back mutation.
- Derived values are recalculated/invalidated according to the canonical contract.
- Event subscribers may initiate subsequent application use cases but cannot observe uncommitted state.

### 6.2 Time and randomness

- Advance game time only through explicit player-controlled progression. Idle menus do not advance the world.
- Use an injectable IGameClock or explicit game-time value for simulation; never use Time.time or wall-clock time as canonical game time.
- Use an injectable deterministic random source for encounter and Expedition rolls. Persist the RNG state needed by the save contract.
- Tests should use a fixed clock and seeded RNG.
- Unity frame time drives animation/presentation only, not canonical simulation timestamps.

## 7. Required systems and slice behavior

### 7.1 Bootstrap and session
- Validate content before enabling player input.
- Create or restore a session through one explicit application entry point.
- Register services/subscribers once.
- Support a clean new-game/restart path for automated tests.
- Show developer diagnostics when content validation fails.

### 7.2 Quest and narrative state
Implement the eleven authored stages, VS1_Q01 through VS1_Q11.

Required behavior:
- The quest domain evaluates prerequisites and completion flags.
- Dialogue choices use stable IDs and are applied once; repeated interaction cannot reapply costs/rewards.
- Persist choice history or equivalent canonical flags.
- Optional discovery may change context, reward, dialogue, cost, or encounter pressure but never blocks the main path.
- Retreat follows the authored failure policy and cannot grant victory rewards or softlock progression.
- Stage transitions have explicit completion criteria and are idempotent where practical.
- Consequences are communicated through dialogue, UI, or world state.

Major choices:
- Q02: enforce rationing / share water / investigate.
- Q04: close gate / temporary diversion / withdraw.
- Q06: accept Organization plan / challenge it / request an alternative.
- Q07: workers first / channel first / staged diversion (the last requires the channel clue).
- Q09: care / repair / coordination as recovery priority.
- Q10: choose Recovery Room / Common Workshop / Coordination Board.

All branches converge on the authored main path. Do not create alternate campaigns.

### 7.3 Dialogue and interaction
- Keep dialogue data and choices separate from dialogue UI.
- Choices declare stable IDs, preconditions, and effect IDs.
- UI asks an application service to choose an option, then refreshes from canonical state.
- Do not encode gameplay rules solely in UnityEvents or button callbacks.
- Provide readable text, speaker identity, clear options, and reasons for known unavailable choices.
- Any optional adult content in the build must be skippable and must not gate the main path or essential rewards.

### 7.4 Exploration
Implement Brackenford, Ashfen Verge, and three POIs: Silt Path, Old Weir, Root-Vault Sluice. A compact location/POI UI or a small set of scenes is sufficient; open-world traversal and grid/range combat are out of scope.

Use stable location IDs from act_i_content.json. Interaction triggers query canonical state and issue application commands; they do not directly mutate quests. Returning to a location preserves discoveries and completed encounters according to quest state.

### 7.5 Combat

Encounters:
- ENC_VS1_01_HUSKS
- ENC_VS1_02_THREADLINGS
- ENC_VS1_03_HOLLOW_WARDEN
- ENC_VS1_04_ROOT_VAULT

Enemy archetypes:
- ENEMY_VS1_FRAYED_HUSK
- ENEMY_VS1_THREADLING
- ENEMY_VS1_HOLLOW_WARDEN
- ENEMY_VS1_ROOT_KNOT

Baseline party: ALYA + ALLY-001. ALLY-005 Cuidadora may join according to the authored care/recovery conditions.

Requirements:
- Implement only the skill/effect subset required by these encounters, but follow canonical combat, turn-resolution, and status-effect contracts.
- Initiative is determined at encounter start and remains stable for that encounter.
- Turn-start effects, duration updates/expiration, derived-state recalculation, action validation, costs, effects, reactions/chains, and terminal checks follow canonical order.
- Insufficient resources make an action unavailable. UI cannot commit invalid actions.
- Each action resolves atomically before terminal combat state is committed.
- Enemy intent visibility follows content definitions and canonical intent rules.
- Retreat is a contextual outcome where specified; retreat is not victory.
- Combat reports an outcome; the quest/application layer decides how that outcome advances the quest.
- Do not introduce grid movement, spatial range, universal level scaling, or new meters for this slice.

**Climax objective encounter:** victory requires explicit progress for all required objectives:
1. VS1_OBJ_STABILIZE_DIVERSION
2. VS1_OBJ_SEVER_FILAMENT
3. VS1_OBJ_SECURE_GATE

Defeating enemies alone is not victory. Q07 community contribution/preparation may reduce an objective requirement or remove/reduce one pressure source according to authored content. The seed-reserve loss and downstream-channel protection are mandatory outcomes regardless of preparation. Commit each outcome exactly once through the quest/outcome service; combat UI must never set those flags directly.

### 7.6 Effects and meters
Follow implementation_spec/COMBAT.md, implementation_spec/TURN_RESOLUTION.md, and implementation_spec/STATUS_EFFECTS.md. Do not invent an independent status timer or stacking model.

Effects must retain the definition ID, source, target, duration, stack state/strength, and runtime provenance required by the canonical contract. Bound trigger recursion using the execution budget. Keep content effect IDs separate from the global set of supported effect handler types.

Where item content modifies Vitality, verify the canonical meter definition before implementation; do not reinterpret it based only on the field name.

### 7.7 Inventory, resources, and rewards

Resources:
- RESOURCE_TIMBER
- RESOURCE_FIBER
- RESOURCE_BOTANICAL_EXTRACT
- RESOURCE_GOLD

Key items:
- ITEM_VS1_FILTER_FIBER
- ITEM_VS1_SOOTHING_TONIC
- ITEM_VS1_REPAIR_BUNDLE
- ITEM_VS1_SEED_RESERVE

Requirements:
- Apply rewards/costs exactly once.
- Validate all costs before committing; no partial deductions on failure unless the canonical contract explicitly allows them.
- Reserve/protect required repair materials from optional crafting while the mandatory repair objective is active.
- Evaluate conditional Q07 costs before committing preparation:
  - Gate closure may add 1 Timber.
  - Accepting the Organization plan may add 2 Gold to resident-support costs.
- Initial authoring baseline: 2 Timber, 2 Fiber, 0 Botanical Extract, 6 Gold. Guaranteed rewards are intended to prevent a mandatory softlock.
- Encounter 1 grants 1 Timber; encounter 2 guarantees at least 1 Fiber; the Hollow Warden encounter guarantees at least 1 Fiber; climax rewards include 2 Timber and 1 Fiber.
- Optional crafting cannot consume mandatory repair stock.
- Numeric values are provisional until runtime balance QA.

### 7.8 Community and facilities

After Q09/Q10, let the player choose one initial facility:
- FAC_VS1_RECOVERY_ROOM — Stability; improves recovery access and supports Cuidadora.
- FAC_VS1_COMMON_WORKSHOP — Conversion; enables a basic Timber/Fiber repair-bundle loop.
- FAC_VS1_COORDINATION_BOARD — Access; improves assignment/Expedition visibility.

The chosen facility is unlocked/selected and persisted. The other two remain visible future options, not free unlocks. Reuse the canonical building/facility model; do not create a parallel slice-only facility system.

Care-first can support Cuidadora's recruitment, and investing in the Recovery Room can also satisfy the authored recruitment condition. Otherwise she remains a trusted NPC and a later recruitment path is outside this slice.

### 7.9 Autonomous Expedition

Implement EXP_VS1_UPPER_ROUTE_SURVEY using the existing Expedition contract:
- choose an eligible community member;
- show purpose, estimated duration, cost/commitment, and result categories;
- validate eligibility and availability;
- launch without Alya;
- mark the assigned member unavailable to the active party while away;
- resolve at canonical game time with deterministic RNG/state;
- grant a small reward, discovery, or modest time-cost complication;
- restore availability according to canonical return rules;
- persist launched/resolved state;
- show the result and its community impact.

This is not a Sidequest. A Sidequest requires Alya; an Expedition is an NPC-only delegated activity. The basic Expedition must be available after Act I regardless of the chosen first facility. The Coordination Board improves visibility but is not a prerequisite.

### 7.10 Persistence

Implement versioned save/load. Persist at least:
- quest stage/objectives/flags/choice history;
- discoveries and optional objectives;
- party membership and relevant character/relationship state;
- inventory, resources, and unique narrative items;
- facility choice/unlocks, assignments, and member availability;
- Expedition status, timestamps, result state, and RNG information needed for reproducibility;
- game time and persistent event state required to reconstruct play.

Do not save mid-combat-resolution. Save at canonical safe boundaries. Use stable IDs in save DTOs; do not serialize GameObject references, delegates, Unity instance IDs, or reconstructible UI state. Add a save schema version and migration seam. A migration must validate the migrated result before replacing the original save.

## 8. Minimum UI/presentation

Build functional UI before final art polish:
1. Main menu or deterministic developer entry point (new game/load/restart).
2. Brackenford hub with interactions and visible community state.
3. Dialogue panel with speaker, text, options, and unavailable-state explanations where appropriate.
4. Ashfen Verge location/POI selection and discovery feedback.
5. Combat UI: party/enemy status, intent where available, action selection, effect feedback, objective progress, retreat, outcome.
6. Reward/quest update summary.
7. Inventory/resource view.
8. Facility selection and basic community status.
9. Expedition assignment/launch and result view.
10. Save/load controls or a test harness using the same persistence service.

Views query/render canonical state. UI callbacks issue commands; they do not own flags, costs, rewards, or progression. Missing art/audio must use explicit placeholders and diagnostics, not broken references or silent failures. Use the UI toolkit already present in the project.

## 9. Automated testing and validation

Use Unity Test Framework or the repository's current test runner. Prefer EditMode/plain C# tests for domain rules; use PlayMode tests for Unity lifecycle and scene wiring.

### 9.1 Unit tests
At minimum:
- registry rejects duplicate IDs, missing references, and unsupported effect types;
- quest prerequisites prevent premature progression;
- each major choice applies consequences once;
- optional clue unlocks staged diversion but is not mandatory;
- resource transactions are atomic on insufficient stock;
- conditional Q07 costs apply only when their flag is true;
- optional crafting cannot consume reserved repair materials;
- retreat does not award victory/completion rewards;
- terminal combat state waits for current atomic action to resolve;
- status duration/stacking/turn-start behavior matches canonical contracts;
- climax enemy defeat without objective completion is not victory;
- completing required objectives resolves the climax;
- mandatory seed loss and downstream protection commit exactly once;
- facility selection unlocks the right state and only one initial option is chosen;
- the basic Expedition remains available regardless of facility choice;
- assigned member cannot enter incompatible availability/activity states;
- Expedition result is deterministic for a fixed seed/state;
- save/load round-trip preserves slice state;
- invalid save schema/content IDs fail safely with diagnostics.

### 9.2 Integration tests
At minimum:
1. New game → Q01–Q03, including optional clue/reward.
2. Every Q02/Q04/Q06 choice path reaches Q07 without softlock.
3. Every Q07 preparation priority applies the correct climax modifiers/objective requirements.
4. Climax resolution applies mandatory loss, secures downstream channel, and advances to Q09.
5. Q09 priority and Q10 facility choice persist and display correctly.
6. Q11 launches/resolves an autonomous Expedition; member availability, reward, time, and quest flags agree.
7. Save at hub → reload → continue without duplicate costs/rewards/events.
8. Main path completes without optional discovery, adult content, or perfect combat outcomes.

### 9.3 PlayMode smoke tests
- Bootstrap validates content before gameplay.
- Required services/views initialize without missing dependencies.
- A dialogue choice triggers one application command and one consequence.
- Combat starts, accepts a valid action, resolves, and returns to quest flow.
- Facility selection and Expedition launch/resolution work.
- Save/load and scene transitions do not duplicate event subscriptions or UI listeners.

### 9.4 Testability rules
- Provide in-memory repositories/ledgers and deterministic clock/RNG implementations.
- Do not depend on wall-clock delays, animation timing, real filesystem paths, or unseeded randomness.
- Do not use Thread.Sleep for game-time progression.
- Prefer explicit AdvanceGameTime, ResolveEncounter, and CompleteExpedition operations.
- Assert canonical state and domain events, not only UI text or GameObject names.
- Include relevant stable IDs and expected/actual values in failures.

## 10. Recommended implementation sequence

Every increment should compile and be reviewable.

### Phase 0 — Repository reconnaissance
Inspect the actual project root, Unity version, packages, UI/input setup, existing code/tests, and current conventions. Identify existing systems before adding alternatives. Confirm the three JSON files are available. Produce a short plan and list any contract conflicts. Do not refactor unrelated code.

**Exit gate:** verified project map and a minimal implementation plan.

### Phase 1 — Bootstrap, content loading, and validation
Define content DTOs, ID/reference validation, content registry, structured result/error types, clock/RNG interfaces, save-store interface, and event interface. Implement the composition root/service locator with fail-fast checks. Add static content validation and unit tests for duplicate IDs, missing references, unsupported effects, and invalid quest links.

**Exit gate:** content loads and validation either passes or produces actionable diagnostics; invalid content cannot start gameplay.

### Phase 2 — Quest, dialogue, inventory/resources
Implement quest/world state, application use cases, typed effect handlers, atomic resource transactions, and a simple dialogue/choice UI. Test all choice consequences and the mandatory-material guarantee.

**Exit gate:** Q01–Q07 progress through a development harness without requiring combat scenes.

### Phase 3 — Exploration and encounter integration
Implement locations/POIs, discoveries, encounter start/return, reward reporting, and retreat policy. Connect encounters by stable IDs. Add tests for optional discovery and returning to the hub/region.

**Exit gate:** location flow works without scene scripts mutating canonical state.

### Phase 4 — Combat subset and climax objective
Implement the required deterministic turn pipeline and only the skills/effects used by the slice. Implement four encounters, intent UI, objective checks, and climax win conditions. Add tests for turn/effect contracts and objective edge cases.

**Exit gate:** all four encounters resolve consistently; defeating the Root-Knot alone cannot win the climax.

### Phase 5 — Community and Expedition
Implement the three facility choices, visible resource/community state, assignments/member availability, and the introductory autonomous Expedition. Use game-time advancement and deterministic resolution; do not create a separate Sidequest loop.

**Exit gate:** Q09–Q11 work and the player sees the community change and Expedition result.

### Phase 6 — Persistence and full-flow integration
Implement versioned save/load and migration validation. Add deterministic full-path tests and PlayMode smoke tests. Save only at canonical safe boundaries. Verify no duplicate rewards/events after load or scene transitions.

**Exit gate:** the main path survives save/load and required automated tests pass.

### Phase 7 — Manual playtest, usability, and balance
Play from a clean save without developer instructions. Confirm consequences are understandable and no branch softlocks. Tune provisional numeric values from actual play. Log issues rather than silently changing canonical design. Add only the polish needed to communicate state and feedback.

**Exit gate:** integrated acceptance criteria pass or remaining exceptions are explicitly documented and approved.

## 11. Integrated acceptance checklist

- [ ] New game, load, and restart work reliably.
- [ ] Content validation runs before gameplay and reports actionable errors.
- [ ] All eleven quest stages have explicit entry/exit criteria and stable IDs.
- [ ] Major choices persist and cannot apply twice.
- [ ] Optional content is optional; the main path remains completable without it.
- [ ] All four encounters use canonical combat contracts and produce correct outcomes/rewards.
- [ ] Climax requires objective checks; enemy defeat alone is insufficient.
- [ ] Mandatory seed-reserve loss and downstream-channel protection occur exactly once.
- [ ] Required Q07 materials cannot be consumed accidentally by optional crafting.
- [ ] One facility is selected and persisted; the other two remain future options.
- [ ] Cuidadora recruitment follows authored care/recovery conditions.
- [ ] First Expedition resolves autonomously and distinctly from a Sidequest.
- [ ] Assigned member availability/return state is correct.
- [ ] Save/load preserves state without duplicating effects, rewards, events, or subscriptions.
- [ ] Unit, integration, and PlayMode smoke tests pass.
- [ ] A fresh manual playthrough reaches the end of Q11 without external instructions.
- [ ] Provisional numeric balance and known limitations are documented.

## 12. Instructions to the implementation LLM

1. **Inspect before editing.** Do not assume this repository already contains a Unity runtime.
2. **Report a concise plan first**, including the first small milestone and expected files to change.
3. **Implement incrementally.** Avoid one enormous patch; compile/test after each milestone.
4. **Preserve source of truth.** If JSON and canonical specs disagree, stop and report the exact IDs/fields plus a proposed resolution.
5. **Never fabricate test results.** State exactly which tests ran, which passed/failed, and what could not run.
6. **Do not claim completion without evidence** from an integrated build and the acceptance checklist.
7. **Keep changes scoped.** No unrelated refactors, new frameworks, extra content, or gameplay systems without a demonstrated need.
8. **Summarize each milestone** with changed files, tests/commands actually run, remaining blockers, and the next smallest step.

### Suggested first task

Begin with Phase 0 and Phase 1 only: inspect the repository and identify the actual Unity project root/test setup, then implement the content-loading/validation seam and bootstrap composition root. Do not attempt the entire game in one pass. The first milestone should be reviewable, testable, and leave the project in a known state.


## Embedded source: Project state and roadmap

# AHTW — Project State, Canon and Roadmap

## Purpose

This is the orientation document for resuming work on **Alya Heals the World (AHTW)**. It summarizes the project's current direction, authoritative documents, locked decisions, narrative spine and remaining work. Domain-specific source-of-truth documents take precedence over this summary.

## 1. What the game is

AHTW is a **narrative RPG with light base/community management** and adult themes. It combines:
- Turn-based RPG combat and character development.
- Exploration, regions, encounters, quests and player-led sidequests.
- Autonomous **Expeditions**, in which assigned community members act without Alya and return with outcomes, rewards or consequences.
- A growing community/base: facilities, assignments, production, resources, trade, recruitment, rehabilitation, training and social cohesion.
- Adult sexuality as part of the world's culture, biology, magic, economics and relationships—not a disconnected minigame.
- Character-specific adult content that should reinforce identity, relationships and narrative rather than flatten the cast into interchangeable scenes.

The design goal is not maximal system complexity. It is a coherent RPG loop in which narrative progress unlocks people, regions, resources and possibilities; exploration and quests provide rewards/discoveries; the community converts them into new capabilities; and those capabilities enable further narrative progress.

## 2. The core loop

**Narrative progress → new regions/resources/characters/facilities → exploration, quests, encounters and Expeditions → rewards and discoveries → construction, production, recruitment, rehabilitation and assignments → new capabilities and specializations → further narrative progress.**

Two external activity types are intentionally distinct:
- **Sidequest:** direct player activity requiring Alya.
- **Expedition:** delegated NPC/community activity that resolves autonomously; an assigned ally is unavailable to the active party while away.

## 3. Story and thematic canon

### Premise

Alya begins as a traveler who helps individual people and gradually learns to build communities, structures and relationships that can help people **without depending on Alya alone**.

The central conflict is **communities versus the Ferida**. The Ferida is widely known but poorly understood; it corrupts, perverts, amplifies and exploits existing vulnerabilities. It escalates from local manifestations to community threats, regional pressure, systemic threats and an Act V apex.

The world is deteriorating, but society has not collapsed. Institutions still provide real protection, infrastructure, expertise and crisis response. They can be necessary and competent while also producing injustice through prioritization, standardization and calculation.

### Alya's arc

- Begins by avoiding responsibility and carrying an unresolved failure.
- Learns to accept responsibility.
- Overcorrects by centralizing too much around herself.
- Learns to distribute responsibility and build durable structures.
- Ultimately seeks conditions that can survive without her.

The final thematic question is not simply whether Alya destroys the Ferida. It is whether people have built something capable of continuing after the exceptional individual is gone.

### Main narrative trajectory

**Act I:** Alya arrives as a newcomer in a struggling community. She helps a specific person, becomes involved in the community's survival, and encounters the Organization when a crisis exceeds local capacity. The Organization offers a technically defensible solution involving isolation, exclusion or sacrifice. Alya contests it and helps create a third option. The community survives, but not without loss; it becomes regionally relevant and Alya is recognized as a leader. Act I ends with the foundation for base management.

**Act II:** The community grows, constructs facilities, delegates responsibilities and encounters a difficult new group of refugees or stigmatized people. Formal politics, integration and risk management become unavoidable. The Organization treats the community as a pilot, training center or subject of study. The point of no return comes when the community violates formal orders to shelter people targeted for relocation, creating a rupture with the Organization.

**Act III:** Autonomy brings resource scarcity, competing requests for help and declining legitimacy. The answer is not isolation but a network of cooperation.

Later acts escalate from local crises to regional and systemic pressure. The story should preserve moral complexity: good intentions have costs; autonomy is not isolation; communities can disagree and still endure; and no institution should become immune to challenge.

## 4. What is already closed

### Architecture and rules
- High-level game architecture and core gameplay loop: closed.
- Core deterministic gameplay rules and implementation contracts I1–I11: closed.
- Cross-system integration audit I12: complete; no blocking cross-system contradiction was identified.
- Major domains including combat, effects, skills architecture, equipment, recruitment, rehabilitation, community assignments, time, economy, exploration, quests and persistence have defined rules. Their content, implementation, tuning and QA are not thereby complete.

### Character architecture and concept rosters
- **10 recruitable allies:** conceptually locked.
- **Named NPC model and roster:** conceptually locked; current canonical list has 21 Named recurring NPCs (IDs include a gap at NPC-020, deliberately removed rather than reused).
- **Character Bible:** conceptually locked.
- Character data alpha exists with starting stat profiles, aptitude profiles and relationship structure; exact balance and skill details remain downstream.
- Adult visual safety and species/design principles are locked: all characters are adults; no child-coded proportions; humanoid fantasy first; beastfolk are a minority; species, culture and function are independent axes.
- NPCs do not participate in combat while functioning as NPCs. A recurring narrative character may have a separate Enemy/Boss representation.
- H-content uses relevance tiers for NPCs and is not a character's class or core gameplay role.

### Visual and adult-content planning
- Character full-body image prompt pack exists at `docs/art/CHARACTER_IMAGE_PROMPTS.md`: tag-oriented prompts, intended 896×1152 portrait, solid white background, medieval/high-fantasy costumes and individual pose/action suggestions.
- The new `docs/art/CHARACTER_EROTIC_CG_MATRIX.md` maps 31 characters to three escalating non-graphic adult situations and three CG beats each.
- Sensuality must fit personality, species, faction and profession. Avoid turning everyone into the same goth/fishnet design.
- The CG matrix is a direction-setting draft, not a finalized scene/asset inventory.

## 5. Canonical character overview

### Recruitable allies (10)
1. **First Ally / Generalist** — Human femboy; flexible companion and first close ally; signature versatility.
2. **Guardiã** — Minotauroid futanari; tank/support, security and training; protective and disciplined.
3. **Rival** — Predatory wolf/feline-inspired beastfolk, feminine; bruiser/DPS, competitive and confrontational.
4. **Erudita** — Original arcane humanoid, feminine; pure mage, research and alchemy; curious and obsessive.
5. **Cuidadora** — Human futanari; healing, prevention and recovery; practical and authoritative.
6. **Artesã** — Goblin feminine; crafting, construction, production and equipment; chaotic inventor.
7. **Caçadora** — Fox beastfolk futanari; ranged damage, traps and exploration; observant and playful.
8. **Mercador** — Feline beastfolk femboy; commerce, economy and opportunities; charming trickster with low combat relevance.
9. **Inadaptada** — Rare/exotic humanoid futanari; initially weak, unusually fast long-term adaptation; shy but determined.
10. **Devoto** — Faerie-like humanoid feminine; protection, buffs, morale and mediation; idealistic and empathetic.

Roster distribution: 4 feminine, 4 futanari, 2 femboy. H-specialization is secondary, not a class. Most allies should contribute meaningfully to combat and community life. Each has a signature identity mechanic and a sparse, deliberate relationship map.

### Named NPCs (21)
Tavernkeeper; Dancer; Community Elder; Mediator; Pragmatic Mentor; Institutional Representative; Ferida Researcher; Hardliner; Regional Authority; Trade Representative; Priestess; Tribal Matriarch; Tribal Guide; War-Chief; EnemyCommander; Faction Dissident; Ferida Manipulator; Reaper; Dryad; Survivor; Demonkin.

Important species/culture decisions:
- Tribe A is **Mycelia**, a matriarchal spiritual society.
- Tribe B is **Orc**, with strength/status, duels and rites of passage.
- Desert Elf is a visual/cultural Elf subspecies only; it does not create separate mechanics.
- Wanderer/NPC-020 was removed because the concept overlapped with First Ally and should not be recreated without new justification.
- NPC H-tier relevance is elastic; H0 background and H1 template characters have no individual H content, while selected named/major NPCs may have authored scenes.

## 6. Key mechanical decisions to remember

- Primary character attributes use an internal **1–100** scale: Body, Agility, Soul, Charm, Dominance, Submission, Sadism and Masochism. Derived values should not become extra primary attributes.
- Species affects natural aptitude but does not hard-lock a build. Lack of natural aptitude means slower development, not impossibility.
- Natural growth derives from recorded activity/use and periodic growth processing.
- Skills have no individual levels; characters unlock skills using Skill Points and data-driven requirements.
- Equipment is exclusive to Alya; allied NPCs do not use equipment.
- Recruitment, eligibility and rehabilitation/integration are separate processes.
- Time is represented internally with continuous timestamps; events at equal timestamps follow explicit priority.
- Combat has a stable turn-order result after initial initiative; effects, durations, derived stats, action resolution and terminal checks follow the defined deterministic pipeline.
- Inventory has no fixed capacity ceiling.
- Save schema versioning is independent from game versioning; migrations preserve the original save.
- Stable semantic IDs connect narrative, systems, data, UI, assets and QA.

For exact rules, consult `docs/architecture/GAME_ARCHITECTURE.md` and `docs/IMPLEMENTATION_SPEC.md`; this summary is not a replacement.

## 7. What remains to determine or produce

The major architecture decisions are not the main bottleneck now. The project is in the transition from **closed rules → content lock → production-ready specification → implementation and asset production**.

### A. Checkpoint C — Content Complete (current planning priority)
- Lock the complete skill catalog and skill definitions: targets, costs, formulas, durations, triggers, AI behavior and presentation.
- Complete enemy and boss roster/data: stats, behaviors, drops, variants, encounter composition and Ferida-linked variants.
- Complete item/equipment/consumable/curse/blessing catalogs and exact effects.
- Define the building/facility catalog: prerequisites, construction costs, upgrades, outputs, upkeep, staffing and effects.
- Finalize resources, recipes, production rates, economy prices/sinks, inventories and reward curves.
- Complete world graph: regions, localities, travel links, unlock requirements, points of interest and encounter pools.
- Complete main/side quest graph, objectives, flags, choices, prerequisites, rewards and consequences.
- Specify concrete encounter catalog, recruitment conditions, rehabilitation routes and Expedition templates.
- Finish character downstream data: exact skills, stats/balance, relationship variables, recruitment scripts and progression values.
- Link narrative beats and character routes to stable quest/flag IDs.

### B. Checkpoint D — Production Complete
- Art direction bible, palettes/materials, silhouette standards, sprite/portrait/CG/cut-in requirements and asset pipeline.
- Character reference approval and actual asset IDs; generate, curate and verify prompts/art rather than treating prompts as finished art.
- For each CG: decide partner, route/relationship, unlock conditions, narrative state, framing, expression, costume state, variants, asset ID and fallback behavior.
- UI/screen inventory, wireframes, interactions and information hierarchy.
- Audio bible, music/SFX needs and event mapping.
- Localization decision: base language, string architecture, translation scope.
- Accessibility/settings decisions.
- Save/persistence implementation, migration tests and failure recovery.
- QA strategy, acceptance criteria, regression tests, content validation and definition of done.

### C. Balance and implementation
- Tune exact damage/healing/H formulas, XP/level curves, skill coefficients, effect durations, SP costs, equipment modifiers, rewards and resource rates.
- Implement deterministic rules and authoring/data validation.
- Test cross-system edge cases, AI fallback, time advancement, save/load and expedition resolution.
- Playtest the community-management loop for meaningful choices without excessive micromanagement.
- Ensure the game remains an RPG first, with base management supporting rather than replacing narrative and combat.

### D. Release decisions (can remain later)
- Target platform/store, release strategy, price/monetization, supported languages, marketing and post-launch scope.

## 8. Recommended next sequence

1. **Finish the content catalog audit** in a stable order: skills → enemies/encounters → items/equipment → facilities/resources/economy → world/quests → recruitment/rehabilitation/Expeditions.
2. Convert each approved catalog into structured, stable-ID data rather than leaving it only in prose.
3. Connect content to narrative flags and system contracts.
4. Close art direction and build an asset inventory keyed to stable IDs.
5. Produce first-pass assets for a small vertical slice: Alya, the first community, the first few allies/NPCs, first enemies, key UI and Act I CGs.
6. Implement and playtest that vertical slice before scaling the full content volume.
7. Complete localization/accessibility/QA/release specifications before production lock.

## 9. Source-of-truth map

- `docs/architecture/GAME_ARCHITECTURE.md` — game identity, architecture and core loop.
- `docs/NARRATIVE_CANON.md` — canonical story and thematic decisions.
- `docs/IMPLEMENTATION_SPEC.md` — implementation contracts.
- `docs/MASTER_PLANNING_AUDIT.md` — master planning checklist and status.
- `docs/GDD_INDEX.md` — index and completion gates.
- `docs/characters/ALLIES_ROSTER.md` — recruitable ally roster.
- `docs/characters/NPCS_DESIGN.md` — NPC model and tiers.
- `docs/characters/CHARACTER_BIBLE.md` — consolidated character identity and Named NPC roster.
- `docs/characters/CHARACTER_DATA_ALPHA.md` — alpha stats, aptitude and relationship data.
- `docs/art/CHARACTER_IMAGE_PROMPTS.md` — character reference image prompts.
- `docs/art/CHARACTER_EROTIC_CG_MATRIX.md` — 31-character situation/CG direction matrix.

## Current verdict

**Core architecture and implementation rules are closed. Character concepts are locked. The full-game content-lock baseline is now authored and indexed, while formal content-gate validation and production readiness remain open.** The repository now contains a five-act content lock and stable-ID catalogs for 47 main quest stages, 25 sidequests, 7 regions, 6 factions, 10 allies, 21 named NPCs, 12 reusable NPC templates, 35 enemy archetypes, 9 major bosses, 8 special encounters, 12 facilities, 8 resources, 36 canonical items, 8 outfits, 8 Expedition templates, and 5 ending families. The next milestone is to validate/reconcile these catalogs and implement the Act I vertical slice; do not start broad asset production or reopen closed systems.


## Full-game content lock update — 2026-10-15

The base-game content scope has been authored in `docs/FULL_GAME_CONTENT_LOCK.md` with structured inventories in `data/content/full_game_world_catalog.json`, `data/content/full_game_gameplay_catalog.json`, and `data/content/full_game_character_arcs.json`. Static JSON parsing and duplicate-ID checks passed. This does not mean all dialogue lines, final numerical tuning, asset files, localization, runtime integration, or QA are finished. Immediate next steps: (1) run the newly authored content validator, regression tests and CI, (2) reconcile legacy CSV/catalog IDs without deleting useful legacy content, (3) finish final dialogue labels and exact reward IDs/amounts for Act I, (4) implement the vertical slice, and (5) use runtime tests/playtests to tune balance.


The content pass also added `tools/validate_full_game_content.py`, `tests/test_full_game_content.py`, and a step in `.github/workflows/skill-catalog-validation.yml`. These are authored but the new validator/tests and workflow have not yet been executed/verified. See `docs/FULL_GAME_CONTENT_COMPLETION_REPORT.md` for the exact boundary between content lock and remaining production work.


## Embedded source: Full-game content lock

# AHTW — Full Game Content Lock

**Status:** Proposed canonical full-game content lock, authored under the project owner's standing instruction to accept recommendations by default. This document closes the *design/content-definition* layer for the base game. It does not claim runtime integration, final numerical balance, art production, localization, or QA completion.

**Authority:** Narrative canon and system contracts remain authoritative for behavior. This document is authoritative for the concrete base-game roster, act structure, content counts, names, narrative beats, unlock dependencies, and intended content coverage. Structured catalogs under `data/content/` carry stable IDs. If a catalog and this document disagree, stop and reconcile rather than silently inventing a third version.

## 1. Product scope and content promise

AHTW is a single-player, turn-based narrative RPG with light community/base management, adult characters and themes, exploration, direct sidequests, and autonomous NPC-only Expeditions. The base game contains five acts, one central home community that evolves politically and mechanically, a six-region cooperation network plus the starting region, ten recruitable allies, twenty-one named recurring NPCs, reusable population templates, a curated enemy/boss roster, and several world-state endings.

### Locked base-game targets

| Content family | Locked target | Notes |
|---|---:|---|
| Acts | 5 | Each has a distinct narrative and management purpose |
| Main quest stages | 45 | 9 per act; stable IDs in the world/narrative catalog |
| Authored sidequests | 25 | Five per act; procedural/repeatable activities are separate |
| Regions | 7 | One starting region + six later regions |
| Recruitable allies | 10 | Canonical roster already locked |
| Named recurring NPCs | 21 | NPC-020 intentionally remains unused; IDs are not recycled |
| Factions | 6 | Independent internal states, not a single reputation meter |
| Enemy archetypes | 35 | Includes the existing legacy types plus defined Ferida-specific roles |
| Major bosses | 9 | One or more per act; some story characters have separate combat representations |
| Special/mini-boss encounters | 8 | Reuse enemy families with encounter-specific rules |
| Facilities | 12 | One initial facility choice; other facilities unlock by progression |
| Resources | 8 | No inventory capacity ceiling |
| Canonical items/equipment | 36 | Legacy items are normalized into stable IDs; new entries fill functional gaps |
| Skill catalog | 67 canonical records | Existing normalized catalog; do not add skills merely to hit a quota |
| Alya outfit slots | 8 retained base outfits | Legacy candidates are reviewed; see section 10 |
| Main endings | 5 state families | Not a binary morality outcome; no exact ending percentages |

This is the intended **base-game** scope, not a promise that every record needs unique bespoke art. Variants should reuse family assets where readable and appropriate. Do not expand these counts without a demonstrated coverage gap.

## 2. Narrative spine and act locks

### Act I — Foundation: “The Water We Share”
**Region:** Ashfen Verge. **Hub:** Brackenford. **Ferida manifestation:** “The Red Thread.”

Alya arrives at Brackenford and becomes involved in a water-allocation dispute involving Mara Venn, the lower terraces, a failing sluice, and a seed reserve. Scarcity and unequal access existed before the Ferida appeared; the manifestation intensifies exhaustion, suspicion, and fixation rather than creating the dispute from nothing. The Organization offers a defensible containment plan that protects downstream settlements by sealing the lower sluice and sacrificing the root-vault. Alya helps construct a third option through local knowledge, repair materials, and coordinated care.

**Mandatory cost:** the lower-terrace seed reserve and a substantial part of the next planting cycle are lost. The downstream channel is protected for the present. No branch removes both costs.

**Act-end state:** Alya is recognized as Brackenford's leader; community management begins; one facility is selected; the first autonomous Expedition is unlocked. The ultimate nature of the Ferida and the full truth of Alya's past remain unrevealed.

### Act II — Construction: “A Place for the Uncounted”
**Region:** Greenwake Basin, with Brackenford as the home hub.

Brackenford grows into a refuge and training site. The player learns construction, production, aptitude-based assignments, rehabilitation, representation, and trade. A displaced group arrives after an official relocation order. Some residents fear resource pressure; others fear repeating the lower-terrace sacrifice. The Organization wants the community to become a replicable pilot and asks for standardization, monitoring, and controlled admissions.

Alya initially tries to personally resolve every dispute. This causes delays and undermines delegates. The act's central crisis concerns a mixed convoy of displaced people and an unstable Ferida-marked patient. The community creates a supervised, voluntary integration process with explicit limits and review rather than either indiscriminate acceptance or collective punishment.

**Point of no return:** Brackenford shelters a group the Organization has formally ordered relocated, after documenting the risk and arranging containment. This creates an institutional rupture without making all Organization members enemies.

**Act-end state:** the community becomes a semi-autonomous regional partner and establishes its first external agreements. Leadership is formalized through a council/delegate model rather than personal rule alone.

### Act III — Consequences: “The Cost of Being Free”
**Regions:** Glassstep March and Mycelian Reach.

Autonomy exposes the community to shortages, contradictory requests for aid, trade leverage, and political resentment. The player cannot maximize every region's welfare simultaneously. A trade blockade and a conflict between two tribal societies reveal that the cooperation network cannot be built by simply exporting Brackenford's rules.

The Organization's internal factions become explicit: pragmatists want evidence and negotiated safeguards; hardliners want enforceable uniformity; reformers argue for plural local authority. Allies and NPC delegates can make decisions Alya would not have chosen if the player has built systems that genuinely distribute responsibility.

**Act-end state:** three regions form a voluntary mutual-aid compact with distinct local rules, shared emergency signals, resource commitments, and dispute resolution. The network is useful but fragile; its existence does not erase regional grievances.

### Act IV — Escalation: “What the Wound Learns”
**Regions:** Cinderfall Reach and the Shattered Archive.

The Ferida begins exploiting not only individual vulnerabilities but the systems created to manage them: reputation, assignments, trade routes, institutional protocols, and the network's own trust. Familiar solutions become dangerous when applied without context. A major attack fractures the network, isolates a region, and forces the community to choose between preserving its own infrastructure and sending people and supplies to a threatened partner.

Alya's flaw returns: she attempts to carry too much herself and becomes vulnerable to the Ferida's amplification of guilt and control. The player must rely on allies, delegates, regional leaders, and prior preparations. No single stat, ally, facility, or faction score can substitute for the network's accumulated readiness.

**Act-end state:** the network survives in a changed form, and the Shattered Archive yields evidence that the Ferida is sustained by recurring patterns of exploitation and failed correction, not by one simple external switch. Alya learns that destroying a visible manifestation is not equivalent to healing the underlying conditions.

### Act V — Revelation and Resolution: “A Future Without a Center”
**Region:** The Wound's Confluence, reached through the Shattered Archive and a multi-region coalition.

The party discovers that the Ferida is a self-reinforcing wound in the world's relational and ecological systems. It amplifies vulnerabilities, turns useful structures into instruments of exclusion, and persists when communities externalize costs and deny correction. Its personification, the Ferida Manipulator, is an antagonist and agent, not the sole origin of every injustice. Alya's past failure involved choosing a narrow containment solution and accepting an institutional account of who could be sacrificed; she survived, but people she was trying to protect did not. The full details are disclosed through evidence and character testimony, not a single exposition dump.

The final confrontation is a multi-stage encounter with combat and world-state objectives. Victory requires disrupting the manifestation, keeping coalition links active, and making local systems capable of responding without Alya's continuous direction. The final choice determines which structures are preserved, reformed, decentralized, or abandoned. It does not guarantee that the Ferida will never return.

**Act-end state:** the wound's sustaining conditions are transformed or constrained; the future remains uncertain but no longer depends on one exceptional individual.

## 3. Main quest graph — 47 stages

Main quests are mandatory in sequence within each act unless a stage explicitly allows a state-dependent variant. Optional discoveries and adult content never gate the main ending. Each quest has a stable ID, a visible objective, a state mutation, and an authored exit condition.

### Act I — Foundation
1. **Q01 The Empty Cistern** — meet Mara and the First Ally; establish the water dispute and first local choice.
2. **Q02 A Ration Is Not a History** — interview residents; uncover that the allocation dispute predates the Red Thread.
3. **Q03 Signs Beneath the Water** — investigate the moving red filaments; introduce the Ferida as an unknown risk.
4. **Q04 A Door Left Open** — stabilize an affected resident and decide how to share scarce clean water.
5. **Q05 The Cost of a Quick Fix** — explore the root-vault approach; discover evidence that the sluice can be repaired but not without sacrifice.
6. **Q06 The Organization Arrives** — meet the Pragmatic Mentor and Institutional Representative; receive the containment proposal.
7. **Q07 Three Parts of a Third Option** — gather repair materials, local knowledge, and coordinated care; choose preparation priority.
8. **Q08 Hold the Sluice** — objective-based climax; stabilize diversion, sever the active filament, and secure the gate.
9. **Q09–Q11 Act I Epilogue Chain** — “What Remains” records the seed loss; “A Place That Must Continue” formalizes leadership and chooses a facility; “First Delegation” launches the first Expedition. These are three implementation stages but share the three final slots in the slice graph. For catalog accounting, Q09, Q10, and Q11 are the stable IDs; the first eight are Q01–Q08.

### Act II — Construction
10. **Q12 A Roof for Strangers** — convert temporary shelter into a permanent refuge; introduce upkeep and space trade-offs.
11. **Q13 The Work Nobody Sees** — assign residents to gathering, care, training, and maintenance; show aptitude and morale.
12. **Q14 The Ledger of Needs** — establish a transparent resource ledger; choose which shortage to address first.
13. **Q15 A Place at the Table** — recruit the Devoto or resolve their introductory mediation arc; introduce social cohesion.
14. **Q16 The Shape of a Promise** — Alya makes a public promise and must define its limits and review conditions.
15. **Q17 A Road with Two Names** — open Greenwake Basin; negotiate access with local stewards and traders.
16. **Q18 The Pilot Community** — Organization proposes standards, reporting, and a supervised pilot arrangement.
17. **Q19 The People Marked for Moving** — discover the relocation order and hear the affected group's own account.
18. **Q20 The Order We Refuse** — shelter the group under a documented risk plan; rupture with the Organization's hardline wing and establish council/delegate governance.

### Act III — Consequences
19. **Q21 Freedom Has a Price** — autonomy removes a support guarantee; choose an initial economic stabilization policy.
20. **Q22 The Glassstep Contract** — negotiate a trade compact with explicit quotas, exceptions, and a dispute clause.
21. **Q23 The Empty Caravan** — investigate a missing shipment; distinguish sabotage from a bad incentive structure.
22. **Q24 Two Fires, One River** — mediate a resource dispute between regional communities; no outcome satisfies every faction.
23. **Q25 A Different Kind of Kinship** — enter Mycelian Reach and negotiate with the Matriarch and Guide.
24. **Q26 What the Roots Remember** — uncover a local memory network that preserves evidence but can also preserve grievance.
25. **Q27 The Price of a Cure** — decide how to share scarce treatment and research access.
26. **Q28 A Voice from the Organization** — cooperate with an internal reformer while protecting local authority.
27. **Q29 The Compact of Three Regions** — ratify the mutual-aid compact with explicit contributions and local exceptions.

### Act IV — Escalation
28. **Q30 When the Signals Lie** — a trusted warning system is manipulated; establish verification and redundancy.
29. **Q31 The Cinderfall Evacuation** — evacuate civilians under limited transport and time.
30. **Q32 The Measure of a Life** — challenge a triage protocol that hides value judgments behind neutral metrics.
31. **Q33 The Delegates Disagree** — resolve a major council dispute without allowing Alya to simply overrule everyone.
32. **Q34 The Broken Route** — reopen a damaged regional corridor through an expedition and a direct mission.
33. **Q35 A Familiar Mistake** — Alya's attempt to control every response causes a setback; allies must intervene.
34. **Q36 The Shattered Archive** — enter the archive and collect records from multiple sources.
35. **Q37 The Wound Learns** — learn how the Ferida exploits systems and feedback loops.
36. **Q38 The Network Under Fire** — defend multiple objectives; prior regional preparation changes support and costs.

### Act V — Revelation and Resolution
37. **Q39 The Promise Alya Buried** — reconstruct Alya's earlier failure from evidence and survivor testimony.
38. **Q40 The Personification** — confront the Ferida Manipulator's account of the world's wound.
39. **Q41 The Coalition's Terms** — negotiate a final coalition with explicit costs and local authority.
40. **Q42 A Road Without a Hero** — distribute final operational responsibilities among allies and delegates.
41. **Q43 Into the Confluence** — reach the Wound's Confluence; optional side paths change support, not basic access.
42. **Q44 The Wound's Heart** — first phase of the final encounter; disrupt the manifestation's anchors.
43. **Q45 The Last Pattern** — final objective phase; preserve coalition links and stop the Ferida from rebuilding its feedback loop.
44. **Q46 What We Leave Running** — choose which institutions and network structures are preserved, reformed, decentralized, or retired.
45. **Q47 A Future Without a Center** — epilogue resolves the world-state ending family and ally/NPC epilogues.

**ID correction rule:** The act list above is the complete 47-stage authored story graph including all three Act I epilogue stages. The initial planning target of 45 is superseded by this explicit graph; do not renumber Q46–Q47 or compress stages to preserve the old estimate. The content catalog uses Q01–Q47. For the first eleven stages, `data/content/full_game_world_catalog.json` includes `verticalSliceId` cross-references to the existing `VS1_Q01`–`VS1_Q11` records. During implementation, preserve both IDs as aliases until save/data migration is explicitly approved.

## 4. Regions and world progression

1. **Ashfen Verge** — starting region; waterworks, farms, damp lowlands, Brackenford; themes of scarcity and blame.
2. **Greenwake Basin** — refuge corridors, reclaimed fields, workshops, trade crossings; themes of growth and capacity.
3. **Glassstep March** — salt-glass flats, caravan roads, market forts; themes of contracts, scarcity pricing, and leverage.
4. **Mycelian Reach** — living forest and fungal memory network; tribal societies, stewardship, and historical grievance.
5. **Cinderfall Reach** — volcanic ashlands and industrial settlements; evacuation, labor, infrastructure, and triage.
6. **The Shattered Archive** — broken research/ritual complex with several competing records of the Ferida; evidence and institutional history.
7. **The Wound's Confluence** — final region where ecological and relational systems converge; access is gated by Act V coalition readiness, not a single numerical reputation score.

Each region has a hub or safe staging point, 3–5 authored POIs, one signature gathering profile, one regional encounter pool, at least one ally/NPC thread, one main-quest chain, and one optional discovery that reveals context rather than a mandatory key. The world map is a regional graph; no tactical grid or freeform open-world traversal is implied.

## 5. Factions

1. **Brackenford Council** — local residents and delegates. States: trust, cohesion, representation quality, and unresolved grievances.
2. **The Organization** — a necessary regional institution. Internal blocs: Pragmatists, Reformers, Hardliners. Track cooperation, oversight pressure, and credibility separately.
3. **Glassstep Caravans** — merchants, carriers, and route stewards. Track contract reliability and route access; do not reduce all merchants to greed.
4. **Mycelian Circles** — distinct tribal communities linked by a living memory tradition. Track consent to share knowledge, stewardship obligations, and grievance.
5. **Cinderfall Works** — industrial and evacuation authorities. Track safety, labor obligations, and public legitimacy.
6. **The Unbound** — displaced people, deserters, stigmatized groups, and mutual-aid cells; not a single ideology. Track safe passage, representation, and internal fragmentation.

The Ferida is not a reputation faction. Its manifestations are world/encounter states driven by authored progression and unresolved conditions. The Organization's blocs must have independent NPCs and quest outcomes; “Organization trust” alone cannot erase their differences.

## 6. Recruitable ally arcs

The ten locked allies keep their established names/concepts and IDs. Each has a recruitment condition, a personal conflict, an Act III/IV contribution, and an Act V epilogue condition. Recruitment is optional except that the First Ally is the initial companion; no single optional ally is required to finish the main story.

- **ALLY-001 First Ally / Generalist:** starts as a survivor who lost their group; learns that adaptability is not the same as having no boundaries. Personal arc: locate the former group's trail, learn why it fractured, and choose a voluntary future with Brackenford. Signature: versatile loadout and development redistribution.
- **ALLY-002 Guardiã:** recruited after protecting a vulnerable settlement and accepting help rather than taking every burden herself. Arc: separate care from control; late-game holds a defensive line only if the player has supported delegation. Signature: Guard/Interception and ally protection.
- **ALLY-003 Rival:** recruited after a competing leader's plan fails and Alya offers partnership without demanding ideological surrender. Arc: transform competitive leadership into accountable challenge; can publicly oppose Alya if the council is being centralized. Signature: pressure, momentum, and disadvantage exploitation.
- **ALLY-004 Erudita:** recruited after a research expedition exposes the cost of treating people as data. Arc: preserve research while adopting consent, review, and transparent risk practices. Signature: creature study, alchemy, and encounter knowledge.
- **ALLY-005 Cuidadora:** conditionally recruited through the Act I care route or Recovery Room investment. Arc: transition from emergency care to prevention and community health; challenges leaders who use treatment to justify preventable risk. Signature: diagnosis, recovery, and health-system resilience.
- **ALLY-006 Artesã:** recruited through a workshop/repair quest. Arc: accept maintenance and safety standards without losing inventive freedom. Signature: construction, modification, and controlled transmutation.
- **ALLY-007 Caçadora:** recruited through an exploration chain after a route rescue. Arc: choose between solitary competence and reciprocal responsibility; her expedition bonuses improve discovery and reduce route risk but never guarantee success. Signature: ranged combat, traps, and exploration.
- **ALLY-008 Mercador:** recruited through a trade dispute after returning a profitable but harmful contract. Arc: distinguish prosperity from extraction and create resilient trade rather than dependency. Signature: better trade access, price negotiation, and commercial opportunities; intentionally lower combat contribution.
- **ALLY-009 Inadaptada:** optional sidequest recruitment after the player follows a series of misunderstood incidents. Arc: build confidence without requiring assimilation; exceptional learning is strong but requires time and support to unlock safely. Signature: accelerated flexible development.
- **ALLY-010 Devoto:** recruited through a mediation and morale chain. Arc: retain idealism while learning that compassion requires boundaries and accountable processes. Signature: protection/buffs tied to morale, integration, and community cohesion.

Relationship clusters remain selective, not a complete matrix: First Ally–Caçadora–Inadaptada; Guardiã–Rival–Cuidadora; Erudita–Artesã; Mercador–Devoto–Inadaptada. These relationships unlock dialogue, support actions, optional adult scenes, or expedition synergies only when the relevant narrative state supports them. Adult content requires adult characters and clear consent; it never gates critical progression.

## 7. Named NPC arcs

The canonical roster remains the 21-entry roster in `docs/characters/NPCS_DESIGN.md` and `docs/characters/CHARACTER_BIBLE.md`. This lock assigns each NPC a game-long purpose:

- **NPC-001 Tavernkeeper:** rumor hub; tracks how local stories change after each act; exposes the difference between a fact and a repeated account.
- **NPC-002 Dancer:** public performance and cultural events; helps morale but refuses to be treated as a universal solution to hardship.
- **NPC-003 Community Elder:** preserves local history; initially supports continuity, later must admit the community's old allocation rules caused harm.
- **NPC-004 Mediator:** helps disputes become explicit agreements; can become a council process lead if the player supports review and records.
- **NPC-005 Pragmatic Mentor:** provides field training and institutional context; remains willing to cooperate after the rupture if local safeguards are credible.
- **NPC-006 Institutional Representative:** negotiates reporting and supervision; can become an intermediary between local autonomy and formal obligations.
- **NPC-007 Ferida Researcher:** develops a safer evidence protocol; must choose between publication, restricted containment, and shared research.
- **NPC-008 Hardliner:** recurring institutional opponent; can be constrained politically or persuaded by evidence, but never converted by one speech.
- **NPC-009 Regional Authority:** grants legitimacy when the network demonstrates accountable governance; also demands transparent cost-sharing.
- **NPC-010 Trade Representative:** negotiates route access, contract clauses, and supply shocks.
- **NPC-011 Priestess:** supports rites of grief, recovery, and community memory; does not replace medical care or political accountability.
- **NPC-012 Tribal Matriarch:** protects Mycelian sovereignty; shares memory only with consent and reciprocity.
- **NPC-013 Tribal Guide:** mediates travel and cultural interpretation; can expose when Alya's assumptions are wrong.
- **NPC-014 War-Chief:** tests agreements through ritualized contest and resource obligations; respects explicit terms over flattery.
- **NPC-015 EnemyCommander:** recurring adversarial leader with separate Enemy/Boss combat records; represents a faction that exploits instability, not the Ferida itself.
- **NPC-016 Faction Dissident:** reveals internal dissent and helps build safe defections without requiring unconditional allegiance.
- **NPC-017 Ferida Manipulator:** major antagonist who uses true grievances to justify destructive absolutes; separate NPC dialogue and boss encounter representations.
- **NPC-018 Reaper:** neutral threshold figure; reveals consequences and mortality without becoming a quest vending machine.
- **NPC-019 Dryad:** regional ecology contact; supports restoration if extraction and stewardship obligations are honored.
- **NPC-021 Survivor:** a living consequence of prior containment; can become a witness, advocate, or leave if repeatedly instrumentalized.
- **NPC-022 Demonkin:** rescue/rehabilitation and legacy conflict; demonstrates that species and origin do not determine consent, allegiance, or moral character.

NPC-020 remains retired and must never be reused. Tavernkeeper, Elder, Mediator, Cuidadora, and other characters may support the same system but cannot erase an ally's distinctive gameplay identity.

## 8. Enemy and boss content lock

### Enemy archetypes (35)

Existing legacy archetypes are preserved where useful and mapped to stable IDs. Enemy names do not imply that a species is inherently hostile. The combat roster uses these roles:

1. ENM-001 Guard — disciplined human/civilized defender.
2. ENM-002 Slime — low-tier adaptive body; tests multi-hit and elemental coverage.
3. ENM-003 Cockatrice — status and vulnerability pressure.
4. ENM-004 Warrior — direct melee baseline.
5. ENM-005 Goblin — evasive utility/scavenger.
6. ENM-006 Mycelian Sentinel — territorial defense; not a generic evil tribe.
7. ENM-007 Zombie — slow attrition/undead effects.
8. ENM-008 Augmented Agent — institutional elite; counters repeated tactics.
9. ENM-009 Kunoichi — evasion, marks, and target switching.
10. ENM-010 Krakenblood — resilient pressure attacker.
11. ENM-011 Kitsune Trickster — decoys and intent manipulation.
12. ENM-012 Barbarian — high damage, low flexibility.
13. ENM-013 Royal Guard — formation and interception.
14. ENM-014 Minotaur — charge/guard-break archetype.
15. ENM-015 Wolfkin Stalker — pack coordination and pursuit.
16. ENM-016 Orc Challenger — duel/resolve pressure; may be neutral in narrative.
17. ENM-017 Haunt — reactive spirit, weak to knowledge and preparation.
18. ENM-018 Witch — curse and control specialist; some are NPCs in separate contexts.
19. ENM-019 Mummy — endurance, attrition, and seal mechanics.
20. ENM-020 Dullahan — elite execution pressure; story counterpart is NPC-018 Reaper only if explicitly authored, otherwise distinct.
21. ENM-021 Angelic Arbiter — protection and judgment effects; not automatically evil.
22. ENM-022 Dragonkin — elemental elite, high threat telegraphs.
23. ENM-023 Fallen Angel — multi-phase control and vulnerability.
24. ENM-024 Lamia Duelist — constriction/control and positional abstraction.
25. ENM-025 Demon — high-pressure hybrid; alignment varies.
26. ENM-026 Threadling — low-health Ferida swarm unit; multiplies when ignored.
27. ENM-027 Hollow Warden — objective defender with linked resistance.
28. ENM-028 Root-Knot Anchor — objective entity; defeating it alone is not necessarily encounter victory.
29. ENM-029 Red-Tide Leech — drains resources/strains; vulnerable after feeding.
30. ENM-030 Echo Husk — repeats the last common action pattern; countered by varied tactics.
31. ENM-031 Guilt Mirror — uses party relationship flags to create pressure, never reveals private player data.
32. ENM-032 Ashbound — Cinderfall hazard fighter; alternates armor and exposure.
33. ENM-033 Archive Custodian — research construct; tests interrupts and source discovery.
34. ENM-034 Network Eater — attacks links/objectives rather than simply Vitality.
35. ENM-035 Confluence Herald — late-game Ferida manifestation; multi-target threat with explicit phase conditions.

### Major bosses (9)

- **BOS-001 Root-Knot at the Sluice** — Act I objective boss; stabilize diversion, sever filament, secure gate.
- **BOS-002 The Pilgrim Engine** — Act II corrupted logistics construct; protect shelter routes and disable three supply anchors.
- **BOS-003 The Contract Eater** — Act III Glassstep boss; break exploitative contract seals while keeping caravan escorts alive.
- **BOS-004 The Memory That Bites** — Act III Mycelian encounter; resolve the living memory crisis without destroying the network.
- **BOS-005 The Ashen Measure** — Act IV Cinderfall boss; counter a triage engine that converts people into risk categories.
- **BOS-006 EnemyCommander: Siege of the Broken Route** — Act IV faction battle; the Commander can retreat, yield, or be defeated; NPC state follows authored result.
- **BOS-007 The Archive's False Witness** — Act IV/early V; tests evidence verification and counters repeated actions.
- **BOS-008 The Ferida Manipulator** — Act V personal confrontation; dialogue and combat are separate representations of NPC-017.
- **BOS-009 The Confluence Pattern** — final multi-phase encounter; disrupt anchors, maintain coalition links, and complete the world-state objective.

### Special encounters (8)
- SPC-001 The First Threadling Nest — teaches enemy reinforcement.
- SPC-002 The Sealed Clinic — optional care/containment dilemma.
- SPC-003 The Caravan in the Salt Storm — protect supplies or rescue stragglers.
- SPC-004 The Silent Grove — exploration/knowledge check.
- SPC-005 The Broken Lift — objective encounter with environmental hazards.
- SPC-006 The Evacuation Clock — timed objective, not a pure damage race.
- SPC-007 The Unreliable Signal — encounter modifiers change after evidence gathering.
- SPC-008 The Empty Throne — late optional encounter testing delegation and ally synergy.

Every boss must have a readable intent/phase contract, a non-damage objective where appropriate, retreat/failure consequences, and a defined post-encounter world-state mutation. Do not scale every encounter universally to player level.

## 9. Facilities, resources, and economy

### Facilities (12)

- **FAC-001 Recovery Room** — recovery, condition stabilization, care route; improves health/status recovery.
- **FAC-002 Common Workshop** — basic crafting, repairs, equipment modification.
- **FAC-003 Coordination Board** — assignment visibility, Expedition overview, delegation reports; does not gate Expeditions.
- **FAC-004 Storehouse** — production buffer and resource reporting; does not create an inventory capacity limit.
- **FAC-005 Training Yard** — training assignment and combat aptitude development.
- **FAC-006 Research Annex** — Ferida research, enemy knowledge, recipe discovery.
- **FAC-007 Alchemy Bench** — consumables, botanical processing, controlled transmutation.
- **FAC-008 Trade Stall** — local trade and market opportunities.
- **FAC-009 Community Hall** — council, representation, grievance review, morale.
- **FAC-010 Refuge Wing** — housing, rehabilitation, and integration capacity.
- **FAC-011 Expedition Lodge** — specialist preparation, route intel, Expedition risk modifiers.
- **FAC-012 Signal Tower** — regional warning network and late-game coalition coordination.

Act I offers a choice among FAC-001, FAC-002, or FAC-003. All three remain constructible later. Basic assignments and Expeditions unlock at Act I completion regardless of facility choice; FAC-003 only improves visibility and coordination.

### Resources (8)

- **RES-001 Timber** — structural construction and repairs.
- **RES-002 Fiber** — bindings, reinforcement, clothing/field kits.
- **RES-003 Botanical Extract** — care, alchemy, and stabilization.
- **RES-004 Gold** — trade, wages, contracts, and selected services.
- **RES-005 Provisions** — community upkeep, travel preparation, and evacuation.
- **RES-006 Salvage** — mechanical parts and advanced repairs.
- **RES-007 Research Notes** — knowledge unlocks and controlled research.
- **RES-008 Trust Tokens** — not a universal currency; represents documented reciprocal commitments used by specific coalition/faction actions and should be capped per agreement, not globally farmed.

Unique narrative resources (e.g., the Act I seed reserve) are quest/world-state objects, not general currencies. Resource values and yields remain provisional until the first integrated economy pass. No inventory capacity ceiling exists.

### Economy guardrails
- Every required construction has a guaranteed feasible route; optional crafting cannot consume reserved main-quest materials.
- Main-quest rewards should not make gathering/Expeditions irrelevant.
- Trade prices use region, contract, reputation state, and stock profile; avoid random price swings that invalidate a promised deal.
- Production/upkeep resolves on the canonical time tick. A missing assigned worker pauses or reduces the authored output according to the recipe; it does not create hidden negative inventory.
- Expeditions can return partial success, delay, injury, lost opportunity, or discovery; failure should not delete a unique character or hard-lock the main quest.

## 10. Items and Alya's outfits

### Item catalog target: 36 canonical items

Retain and normalize the existing useful equipment families; do not preserve ambiguous legacy names as separate items when they are stages of one evolution chain.

**Build-defining equipment (10):**
- ITM-001 Crux of Enlightenment — balanced Soul/Body and H-damage specialization.
- ITM-002 Oath of Obedience — blessed defensive sustain; unlocks through a protection vow.
- ITM-003 Underwear of Restoration — recovery/status-cleansing synergy.
- ITM-004 Forever Cage — cursed risk/reward item evolving from True-Size Cage; Strain interaction.
- ITM-005 Chastity Belt — defensive anti-penetration/anti-control build.
- ITM-006 Ofuda Chastity — blessed defensive counterpart with Soul/Masochism profile.
- ITM-007 Hypnosis → Reprogram → Slave — one cursed evolution chain, not three inventory records.
- ITM-008 Sensitivity → Receptacle → Fulfilled — one cursed evolution chain with incoming-pressure and recent-hit stages.
- ITM-009 Restraint → Suffer → Canvas — one cursed resistance/effect-conversion chain.
- ITM-010 Messaging → Sway → Pheromone — blessed area-support chain; presentation must preserve consent framing.

**Core equipment and utility (16):**
- ITM-011 Body Amulet; ITM-012 Agility Ring; ITM-013 Soul Amulet; ITM-014 Charm Ring.
- ITM-015 Field Harness — expedition/repair preparation.
- ITM-016 Reinforced Boots — travel hazard reduction.
- ITM-017 Sluiceworker Gloves — construction/repair bonus.
- ITM-018 Herbal Satchel — care/alchemy output.
- ITM-019 Surveyor Lens — discovery and enemy intent information.
- ITM-020 Archive Seal — research protection and controlled access.
- ITM-021 Caravan Ledger — contract/trade insight.
- ITM-022 Guard's Buckler — defensive reaction synergy.
- ITM-023 Thread-Cut Knife — Ferida-filament utility; no automatic boss victory.
- ITM-024 Resonance Charm — research/Strain interaction.
- ITM-025 Expedition Rations — preparation item; consumable.
- ITM-026 Emergency Filter Kit — one-use spread-risk mitigation.

**Consumables and quest items (10):**
- ITM-027 Healing Draught.
- ITM-028 Clear-Mind Tonic.
- ITM-029 Field Dressing.
- ITM-030 Botanical Stabilizer.
- ITM-031 Smoke Pellet.
- ITM-032 Thread-Salt.
- ITM-033 Repair Kit.
- ITM-034 Research Sample Case.
- ITM-035 Seed-Reserve Ledger (quest evidence; not the reserve itself).
- ITM-036 Coalition Signal Key (quest/coordination item; no global unlock bypass).

Legacy tattoos, jewelry, plugs, clothing, and transformation chains may be retained when they have distinct mechanics and a consent-aware narrative context. They must receive stable IDs, explicit slot, effects, curse/blessing state, removal/evolution policy, unlock conditions, and asset classification. The 36-item list is the authored core set; additional legacy variants can be retained as sub-variants only if they do not inflate the core catalog or create redundant choices.

### Alya outfits: retain 8 base sets
- **OUT-001 Traveler's Lace** — default, balanced baseline.
- **OUT-002 Field Armor** — defensive combat identity.
- **OUT-003 Witch's Mantle** — magic/research specialization.
- **OUT-004 Dancer's Regalia** — social/Charm and event presentation.
- **OUT-005 Nun's Habit** — restraint/protection visual identity; not a morality marker.
- **OUT-006 Formal Dress** — diplomacy and major civic scenes.
- **OUT-007 Demon Armor** — late-game Ferida-facing equipment, powerful but with explicit trade-offs.
- **OUT-008 Shibari Harness** — specialized risk/reaction build; unlock and presentation remain consent-framed.

**Not retained as independent base outfits:** Nude (presentation state, not equipment); Slave (a narrative/curse state, never a default outfit slot or identity label); CowPrint (cosmetic variant/event unlock unless it receives a genuine mechanical identity). Small cosmetic variants do not become separate equipment systems.

## 11. Sidequests and autonomous Expeditions

### Authored sidequests (25; five per act)

**Act I**
- SQ-001 A Bowl Kept Warm — resolve a food-sharing dispute; unlocks a resident support flag.
- SQ-002 The Missing Filter — recover a lost filter; lowers one Q07 preparation cost.
- SQ-003 The Quiet Room — help exhausted workers establish voluntary recovery space.
- SQ-004 A Map in the Rafters — discover a safer route; grants expedition route knowledge.
- SQ-005 Mara's Ledger — reconstruct water allocation records; changes local trust, not the mandatory seed loss.

**Act II**
- SQ-006 The Unclaimed Bed — determine how refuge spaces are allocated.
- SQ-007 A Tool for Every Hand — help Artesã test a safe repair design.
- SQ-008 The Unfinished Lesson — help Guardiã and Rival establish training rules.
- SQ-009 A Contract in Ink — expose a one-sided trade clause.
- SQ-010 The Names We Keep — create a consent-based resident record.

**Act III**
- SQ-011 Salt on the Road — rescue caravan cargo or stranded travelers.
- SQ-012 The Root That Remembers — decide what memory the Mycelian Circles share.
- SQ-013 A Debt with No Owner — settle a legacy debt without punishing descendants.
- SQ-014 The Broken Bell — restore a warning system with redundant signals.
- SQ-015 The Price of Quiet — address a rumor campaign without suppressing dissent.

**Act IV**
- SQ-016 Ashes in the Clinic — distribute scarce treatment with a public review process.
- SQ-017 The Route Nobody Owns — restore a route with shared maintenance.
- SQ-018 The False Witness — gather evidence before accusing an ally or faction.
- SQ-019 A Seat Left Empty — respond to a delegate's resignation without forcing them back.
- SQ-020 The Last Workshop Shift — save a facility or evacuate its workers.

**Act V**
- SQ-021 The Witnesses' Circle — reconcile contradictory accounts of Alya's past.
- SQ-022 What the Reaper Carries — help a community memorialize a loss.
- SQ-023 A Garden Outside the Wall — establish a recovery plot beyond the hub.
- SQ-024 The Unbound's Terms — negotiate representation for a displaced group.
- SQ-025 A Signal Sent Twice — build redundant coalition communication.

Sidequests may grant items, knowledge, relationships, optional ally scenes, faction changes, or encounter modifiers. They never remove mandatory losses or serve as the only key to the final boss.

### Expedition templates (8 reusable templates)
- EXP-001 Foraging Run — provisions/botanical materials; weather and aptitude modifiers.
- EXP-002 Timber Survey — timber/salvage; route risk and tool quality.
- EXP-003 Safe-Road Survey — reveals POIs and lowers travel uncertainty.
- EXP-004 Resident Escort — protects travelers; morale and trust outcome.
- EXP-005 Research Retrieval — research notes/samples; enemy knowledge and contamination risk.
- EXP-006 Trade Negotiation — gold, contracts, market access; requires a negotiator or preparation.
- EXP-007 Emergency Relief — sends provisions/care to a region; costs resources but can preserve network stability.
- EXP-008 Signal Relay — repairs coalition communications; late-game redundancy.
  
An Expedition uses NPC/community members only. Assigned allies are unavailable to the active party until return. Results are deterministic from seeded resolution, assignment, aptitude, preparation, route, time, and authored modifiers. It cannot silently become a player-controlled Sidequest.

## 12. Endings and world-state outcomes

Five ending families; the game selects a family and composes epilogues from explicit state flags. No exact percentage meter is shown.

1. **END-001 The Shared Table** — strong, accountable network; local autonomy preserved; the Organization is reformed through negotiated oversight. Alya remains a participant, not a central authority.
2. **END-002 The Many Lanterns** — highly decentralized network; weaker central coordination but strong local resilience. Some regions remain distant; the future is plural and uncertain.
3. **END-003 The Necessary Compact** — a more centralized coalition survives with safeguards, appeal routes, and sunset clauses. It is effective but must continue to be questioned.
4. **END-004 The Quiet Refuge** — Brackenford and several partners endure, but broader cooperation remains limited. The local community is safe enough; the world-scale wound is constrained rather than fully addressed.
5. **END-005 The Unfinished Road** — the network fractures under unresolved grievances, but not into total annihilation. Alya prevents immediate collapse; future recovery depends on people who choose to rebuild.

Ending inputs include regional readiness, delegated responsibility, faction agreements, evidence integrity, ally arcs, care/integration policy, and the final choice. No single companion, romance, adult scene, or faction reputation can dictate the ending.

## 13. Adult-content and consent policy for content authoring

All characters are adults. Adult content is optional, character-specific, and gated by relationship/context flags. It must not be required for main progression, critical rewards, or ending access. Consent, boundaries, and consequences remain legible. Curses and supernatural influence are gameplay states and must not be presented as equivalent to consent. NPCs who are not recruited may have lower-tier optional scenes only when their authored relevance supports them; the tier system in `NPCS_DESIGN.md` remains authoritative.

This lock defines adult content *placement and unlock philosophy*, not explicit scene scripts or final CG asset IDs. Those are production items and should be authored against the character's arc, not produced as a quota.

## 14. Content dependencies and production order

1. Lock stable IDs and validate all structured catalogs.
2. Complete main quest graph, sidequest triggers, flags, and ending-state mapping.
3. Normalize enemy/item/facility/resource IDs and link them to existing legacy data.
4. Define encounter phase/objective contracts and quest rewards.
5. Complete ally/NPC recruitment, relationship, and state transitions.
6. Map every content ID to UI, audio, portrait, sprite, combat, CG, and localization needs.
7. Build the vertical slice against this catalog before expanding production art.
8. Run runtime integration, numerical balance, playtest, accessibility, and save migration tests after the implementation foundation exists.

## 15. What this lock does and does not mean

**Closed here:** base-game content scope; five-act narrative sequence; region progression; main quest stages; sidequest set; faction identities; ally and NPC arc assignments; enemy and boss coverage; facility/resource/item roster; outfit scope; Expedition templates; ending families; adult-content integration principles.

**Still production work:** schema implementation and validation; linking IDs to existing CSVs and legacy asset files; exact stat/skill coefficients and encounter tuning; dialogue for every quest stage; all final dialogue localization; audio; final CG scripts and asset IDs; visual asset generation/review; UI implementation; automated and manual QA; accessibility; save migration; performance and release work.

No claim of runtime completeness or release readiness is made by this document.


## Embedded source: Narrative canon

# Narrative Canon — Source of Truth

> **Status:** Canonical narrative source of truth.
>
> This document consolidates the narrative decisions recorded in the historical checkpoints and subsequent narrative decisions. When an older checkpoint conflicts with a later decision, **the later decision wins**. Historical checkpoints are retained for traceability but do not override this document.
>
> **Purpose:** This is the primary reference for narrative design, gameplay integration, character arcs, chapters, quests, encounters, endings, and future narrative expansion.

---

# 1. Narrative Identity

## Core premise

**Alya Heals the World** is the story of a traveler who begins by helping individual people and gradually learns to build communities, structures, and relationships capable of helping people without depending on her alone.

The central conflict is:

> **Communities versus the Ferida.**

The Ferida is the primary antagonistic force. Institutions, organizations, political conflicts, and interpersonal failures matter because they shape how people respond to it, resist it, or become more vulnerable to it.

The final question is not:

> “Did Alya destroy the Ferida?”

It is:

> **“Did we build conditions sufficient for something better to continue existing without us?”**

## Core thematic pillars

- Good intentions do not remove consequences.
- Helping one person can create costs for another.
- Responsibility is necessary; total control is not.
- Autonomy is not isolation.
- Institutions can be necessary, competent, and still cause injustice.
- A community does not need unanimity to survive, but it needs mechanisms capable of surviving disagreement.
- No structure should become incapable of being questioned, corrected, or abandoned.
- A durable solution cannot depend permanently on one exceptional individual.
- The future does not need to be guaranteed to be worth building.

---

# 2. The World

## 2.1 General state

The world is in gradual decline, although much of society still appears functional.

Existing institutions continue to provide:

- protection;
- infrastructure;
- crisis response;
- regional coordination;
- expertise.

Civilization is not already collapsed. The tension comes from deterioration occurring inside systems that still visibly work.

## 2.2 The Ferida

The Ferida is widely known but poorly understood.

Its function throughout the narrative is to act as a force of:

- corruption;
- perversion;
- amplification;
- exploitation of vulnerabilities.

It does not need to create every problem. It finds existing weaknesses in:

- individuals;
- relationships;
- communities;
- institutions;
- social systems;

and makes them worse.

Its importance escalates across the game:

**local manifestation -> community threat -> regional pressure -> systemic threat -> narrative apex in Act V.**

Alya has prior personal experience with the Ferida, but this does not give her privileged knowledge of its true nature.

Alya's powers allow exceptional intervention against it, but:

- she is not immune;
- she can fail;
- she can be corrupted;
- her powers do not grant moral authority;
- they do not make her uniquely capable of solving everything alone.

## 2.3 The true nature of the Ferida

The complete truth is reserved for Act V.

The canonical direction is:

- the Ferida is not reducible to a single villain's deliberate creation;
- it has elements comparable to a natural force;
- its existence, manifestation, spread, and historical consequences are also tied to a complex chain of human decisions and systems.

The final revelation must **recontextualize earlier events**, not simply explain everything through a hidden “master switch.”

---

# 3. Alya

## 3.1 Initial position

Alya arrives as a newcomer to the starting community.

She:

- has no established authority;
- is initially expected to pass through;
- is traveling toward a concrete destination to fulfill a promise or responsibility;
- is also, emotionally, running from something she failed to resolve.

The player learns the community alongside her.

## 3.2 Initial virtues

- Empathy.
- Adaptability.
- A strong tendency to act when someone is suffering.

## 3.3 Initial flaws

- Difficulty accepting long-term responsibility.
- Impulsive intervention when faced with suffering.
- Fear of making decisions that harm others.
- Tendency to believe that direct help and good intentions are sufficient foundations for action.

Her fear of responsibility is connected to a previous experience involving the Ferida and a decision whose consequences she associates with herself.

The exact objective truth of that past event remains open until useful character-level detailing.

## 3.4 Alya's complete macro arc

> **Avoid responsibility -> accept responsibility -> centralize responsibility too much -> learn to distribute responsibility -> build conditions that can survive without depending on her.**

A more detailed progression:

1. She helps people directly.
2. She stays to face consequences.
3. She becomes a member of the community.
4. She accepts formal leadership.
5. She mistakes responsibility for the need to personally control outcomes.
6. She learns delegation.
7. She learns to accept decisions she would not personally make.
8. She learns that even good systems can become harmful.
9. She learns that systems must be corrigible and challengeable.
10. She ends seeking a future that does not require Alya herself to remain indispensable.

Alya remains vulnerable throughout the entire story.

---

# 4. The Starting Community

## 4.1 Initial condition

The game begins with a community already struggling to survive.

It faces:

- material fragility;
- scarcity;
- internal tensions;
- limited capacity to respond to new crises.

The initial question is:

> “Is this place still worth trying to save?”

## 4.2 Alya's integration

Alya's first meaningful action follows:

> **Help one person -> become entangled in a collective survival problem.**

Her first important connection combines:

- an ordinary member of the community;
- someone directly affected by the Ferida.

Alya eventually receives a real opportunity to continue her original journey.

She chooses to remain.

Her transformation at this stage is:

> “I will help while I am here.”
>
> becomes
>
> “I will stay and help deal with what happens afterward.”

## 4.3 First major mistake

Alya:

- trusts an apparently competent person, authority, or solution too much;
- lacks the local historical context;
- acts on incomplete information;
- helps implement a solution that resolves the visible problem while transferring costs elsewhere or worsening existing tensions.

The lesson is:

> **A solution that fixes the problem you can see is not automatically good for the whole system.**

---

# 5. The Organization

## 5.1 Narrative role

The organization is **not the central antagonist**.

It is:

- competent;
- necessary in many contexts;
- capable of saving lives;
- internally diverse;
- structurally prone to prioritization, standardization, and calculation.

Its central moral tension is:

> **A system can work, save lives, and contain good people while still producing decisions that abandon or sacrifice others for reasons considered rational.**

## 5.2 Initial relationship with Alya and the community

The organization initially intervenes because the local crisis exceeds the community's capacity.

It demonstrates:

- real expertise;
- real resources;
- real ability to help;
- pragmatic assessment of costs and risks.

The community later becomes a semi-independent partner and partially supervised experiment.

It receives:

- resources;
- protection;
- infrastructure;
- training;
- specialists;
- regional connections.

In return, it accepts varying degrees of:

- supervision;
- protocols;
- information sharing;
- regional responsibilities.

The organization remains involved because the community has:

- strategic relevance;
- unusual demonstrated potential;
- proximity to or relevance for a manifestation of the Ferida.

## 5.3 Institutional pressure

As the community grows, institutional friction appears around:

- who may enter or remain;
- external priorities for local production and resources;
- protocols for the Ferida;
- requests for people, specialists, or resources to serve regional needs.

The organization increasingly attempts to:

> **study -> formalize -> integrate -> potentially absorb**

what the community has created.

The offer is genuinely attractive. It includes:

- recognized autonomy/protection;
- capacity to help more people;
- privileged access to Ferida research;
- practical resources and infrastructure.

The danger is not that the offer is worthless. The danger is that small administrative concessions gradually influence:

- how success is measured;
- who deserves resources;
- which communities should receive help.

This reconnects the narrative to the logic of the “calculation.”

## 5.4 Internal plurality

The organization must not be treated as monolithic.

It contains:

- pragmatic institutional actors;
- internal allies;
- opponents;
- people who believe in Alya's work;
- people who believe it is dangerous or unsustainable.

At least two early faces embody this:

### Pragmatic mentor
Recognizes Alya's potential, supports her development, respects her, and still disagrees with her on fundamental questions.

### Institutional representative
Competent, less emotionally close, and capable of articulating the genuine costs, risks, and priorities carried by the larger system.

The organization's eventual fate is **not fixed**. Depending on the state of the world, it may be:

- reformed;
- transformed;
- coexist with community networks;
- fragmented;
- gradually replaced in some functions.

---

# 6. The Community's Political and Social Evolution

The community begins pragmatically:

> “We may not like them, but we need to survive.”

Over time, disagreement develops organically.

Important currents include:

- greater institutional integration for security and stability;
- concern that growth is changing the community too quickly;
- greater representation and participation, especially from newer members;
- later, divergent regional interests.

The community must never be treated as having one permanent collective will.

Its evolution is:

**informal survival -> hybrid leadership -> delegated responsibilities -> formal representation -> regional network.**

Alya begins as formal leader after Act I, but she is not a permanent absolute ruler.

Representatives can be selected from recruited allies, allowing character recruitment and political development to intersect.

---

# 7. Act I — Foundation

## 7.1 Opening

Alya arrives as a traveler intending to continue toward her original destination.

A local problem appears manageable at first.

The sequence is:

**local problem -> Ferida amplifies it -> scarcity and social fragility become visible -> external structures become relevant.**

Alya helps a specific person and becomes involved in the community's larger survival problem.

## 7.2 Belonging

Internal conflict develops around:

- scarcity;
- whether to remain or abandon the community;
- whether to accept external help.

Alya makes her first major mistake by supporting a superficially rational solution with incomplete understanding.

She eventually chooses to stay when she could leave.

## 7.3 First major crisis and the organization

The community:

**tries to solve the crisis alone -> partially fails -> the Ferida escalates -> the organization intervenes.**

The organization proposes a technically defensible solution involving isolation, exclusion, or sacrifice of a person or group.

Alya initially accepts or seriously considers it reasonable.

After seeing the human consequences, she:

1. argues within the system;
2. fails to sufficiently change the decision;
3. helps build a third solution using the community's own capabilities.

The choice has real costs:

- material;
- political;
- personal;
- internal.

## 7.4 End of Act I

The community achieves a significant success:

- develops a new capacity;
- uses it to help others;
- successfully integrates new people.

But a structural failure follows: a crisis amplified by the Ferida causes an unavoidable loss despite Alya's efforts.

Alya learns:

- responsibility is not control;
- doing everything “correctly” does not guarantee that everyone survives.

A regional crisis requires action beyond the original settlement.

The community responds successfully enough to become regionally relevant.

Alya's leadership progresses:

> **de facto leader -> formally recognized leader.**

Act II opens with Alya learning to manage the community.

The Base Management tutorial is therefore a direct narrative consequence of her new role.

---

# 8. Act II — Construction, Growth, and Rupture

## 8.1 Early Act II: learning to lead

The initial gameplay/narrative progression is:

**survival -> work organization -> infrastructure -> well-being and relationships.**

Alya must learn that leadership means prioritizing when she cannot be everywhere.

The community seeks to:

- reduce dependence on emergency support;
- prepare for new members;
- create safer external connections.

New members may:

- arrive spontaneously;
- be recruited through missions;
- be relocated by the organization;
- appear because of prior choices and relationships.

## 8.2 Delegation

Aly a initially avoids delegating dangerous responsibilities.

The delegation arc is:

1. Alya keeps a dangerous responsibility for herself.
2. Another person receives space to act differently and succeeds.
3. Another responsible person fails, testing whether Alya will centralize everything again.

The lesson:

> **Delegation does not eliminate risk. It distributes responsibility and accepts that other people may make different decisions and mistakes.**

## 8.3 The first growth crisis

Growth produces:

1. insufficient infrastructure;
2. reduced social cohesion;
3. new interests and social currents;
4. administrative structures that no longer scale.

A difficult group arrives, combining:

- displacement/refuge;
- people directly affected or stigmatized by the Ferida;
- backgrounds shaped by more rigid authority structures.

Alya is pressured to:

- isolate a supposedly risky group;
- centralize decisions for efficiency.

The Ferida amplifies:

- fear;
- paranoia;
- intergroup tension;
- systemic vulnerabilities.

The community responds by creating:

- more formal political structures;
- formal delegation;
- integration and risk-management protocols.

The core lesson:

> **A community does not need agreement on everything, but it needs mechanisms capable of surviving disagreement.**

## 8.4 Representation and regional influence

The community's practices become demonstrably replicable.

Another community adapts part of the model successfully.

This proves the success is not dependent solely on Alya's exceptional abilities.

External reactions include:

- inspiration;
- distrust;
- opportunism;
- superficial appropriation.

The community becomes involved in external crises and must deal with the political consequences of helping.

Representatives:

- publicly disagree with Alya;
- reach conclusions she dislikes;
- make consequential decisions without waiting for her.

Alya accepts that:

> **If everything depends on Alya, then nothing she built can truly survive without her.**

## 8.5 The price of importance

The community's relevance produces:

**influence -> external dependence -> political pressure -> greater supervision -> organized hostility.**

The organization increasingly treats it as:

- a learning/training center;
- a replicable pilot;
- a subject of study regarding the relationship between social structure and the Ferida.

The key tension becomes:

> **If the institution turns Alya's model into protocol, does it remain the same model?**

## 8.6 Point of no return

The organization repeats, at a larger scale, the logic of the calculation that previously led to abandonment elsewhere.

A community is deemed insufficiently viable or insufficiently prioritized.

Alya:

1. contests the decision internally;
2. attempts to save at least some people;
3. achieves only partial success;
4. creates serious secondary consequences.

Her community:

- violates formal orders;
- shelters or protects people targeted for relocation;
- becomes politically associated with the resulting disaster.

The community cannot simply return to its old relationship with the organization.

Alya enters Act III believing that:

- real independence is necessary;
- isolation is not.

The principle is:

> **Independence is necessary; isolation is not. Institutions are necessary; the absence of alternatives and counterpowers is dangerous.**

---

# 9. Act III — Consequences and Network

## 9.1 Autonomy

The immediate problems are:

- resource scarcity;
- growing requests for help;
- declining external legitimacy as a consequence of rupture.

The old question returns at a larger scale:

> **Who do we help when we cannot help everyone?**

The answer is not absolute self-sufficiency.

It is:

> **Build a network of cooperation.**

## 9.2 Network formation

The structure develops organically:

**personal relationships -> mutual aid -> resource sharing -> representatives -> possible later formalization.**

The network creates its own problems:

- unequal access to shared resources;
- conflicting regional interests;
- ideological disagreement;
- risk of dependency;
- adaptation or misuse of Alya's principles.

The organization remains fragmented and context-dependent:

- sometimes adversarial;
- sometimes cooperative;
- still necessary in some places.

## 9.3 End of Act III

The Ferida manifests across multiple regions simultaneously.

It:

- aggravates political conflict;
- destabilizes communities;
- pressures the network;
- exposes institutional weaknesses.

The end-state of Act III establishes:

> **No single community, network, or institution can resolve the crisis alone.**

This transition had already been implicit in the earlier macro escalation and is now a formal act boundary.

---

# 10. Act IV — Escalation and Stress Test

The Ferida becomes increasingly dominant.

Its new narrative role is not merely to become “stronger.”

It begins to exploit and corrupt the very structures created to resist it.

The greatest tests include:

- protective systems causing unexpected harm;
- important allies taking divergent paths;
- decisions without consensus;
- the network compromising some principles to survive.

Alya herself nearly succumbs to the Ferida.

The consequences of this stage may vary according to player state:

- an important community can be lost;
- an ally can be lost or separated;
- principles may be compromised to different degrees.

The major lesson is:

> **Even a good structure can become dangerous if it cannot be questioned, corrected, or abandoned.**

Act IV must significantly raise the stakes and make the Ferida's corrupting/perverting nature impossible to treat as a secondary problem.

---

# 11. Act V — Revelation and Resolution

## 11.1 Final revelations

The major revelations are intentionally reserved for Act V:

- the deeper nature and history of the Ferida;
- the historical chain connecting systems and past decisions to its present manifestation;
- the deeper meaning of Alya's powers;
- the broader context behind the original abandonment and “calculation.”

These revelations should not reduce the story to:

> “One evil person secretly caused everything.”

They should instead reveal a chain of causes, decisions, incentives, and conditions.

## 11.2 Alya's role

Alya discovers that her powers provide unusual capacity to intervene, but not:

- immunity;
- moral infallibility;
- sole authority;
- a solitary solution.

Her role is important without making everyone else irrelevant.

## 11.3 Final confrontation

The climax combines:

- direct confrontation with a **personification of the Ferida**;
- coordinated action among communities and allies;
- transformation of the conditions that allow the Ferida to spread and perpetuate itself.

The personification gives the player a concrete antagonist and confrontation without reducing the entire Ferida to a single boss.

## 11.4 Meaning of victory

Victory is primarily:

- transforming conditions that sustain the Ferida;
- creating conditions for recovery and harmony;
- potentially containing or reducing its capacity to persist.

It is **not necessary** to confirm that the Ferida has been permanently erased.

The people alive during the story do not need to know whether it will someday disappear completely.

The goal is to make harmony possible, not guarantee an eternal utopia.

---

# 12. End States

The game should produce a spectrum of world states rather than one simple “true ending.”

Important dimensions include:

- the state of Alya's original community;
- the state of the broader community network;
- the relationship with and fate of the organization;
- Alya's personal fate;
- the fate and development of recruited allies.

The Ferida does not need an independent ending meter. Its final condition follows from the confrontation and the conditions established through the game.

Before the ending, the player should understand the direction of their choices through:

- short words or phrases;
- visible changes in the world;
- narrative consequences.

The game should **not** present deterministic percentages revealing an exact guaranteed ending.

---

# 13. Macro Progression

## One-line progression

> **Alya helps -> stays -> leads -> builds -> delegates -> grows -> influences -> ruptures -> becomes independent -> connects communities -> faces systemic escalation -> sees her own structures tested and transformed -> confronts the Ferida -> helps create conditions for a better future that does not depend only on her.**

## Five-act layout

### Act I — Foundation
Alya arrives -> helps -> stays -> community crisis -> organization intervenes -> Alya challenges a calculated solution -> community succeeds and suffers loss -> Alya becomes leader.

### Act II — Construction
Leadership -> Base Management -> growth -> delegation -> growth crisis -> representation -> regional influence -> institutional absorption pressure -> calculation repeated -> rupture.

### Act III — Consequences
Independence -> resource pressure -> cooperation network -> regional disagreements -> organization becomes plural -> multi-regional Ferida crisis.

### Act IV — Escalation
The Ferida exploits structures -> communities and allies fracture or adapt -> principles are tested -> Alya nearly falls -> the world enters its highest sustained crisis.

### Act V — Revelation and Resolution
Truth about the Ferida and history -> meaning of Alya's role -> coordinated final confrontation with the personification -> transformation of sustaining conditions -> spectrum of uncertain futures.

---

# 14. Canonical Narrative Rules

The following rules should be preserved unless this document is explicitly revised.

1. **The Ferida is the central antagonistic force.**
2. **The organization is not simply evil and must remain internally diverse.**
3. **Alya is powerful but never immune, infallible, or permanently indispensable.**
4. **The community is a character/system in its own right, not merely a backdrop.**
5. **Growth always creates new forms of complexity rather than simply solving old problems.**
6. **Delegation and representation must have real consequences, including decisions Alya would not choose.**
7. **The player should experience the evolution from managing a community to participating in wider cooperative structures.**
8. **The Ferida escalates from local amplification to systemic corruption, with its narrative apex in Act V.**
9. **Major revelations belong to Act V.**
10. **The final solution cannot depend exclusively on Alya.**
11. **The narrative should preserve uncertainty about whether the Ferida ever disappears completely.**
12. **Endings are world states created by accumulated choices, not merely binary moral rewards.**
13. **Autonomy must not be confused with isolation.**
14. **Institutions are necessary but require alternatives, accountability, and counterpowers.**
15. **No system should be treated as permanently correct or beyond revision.**

---

# 15. Deliberately Open Areas

The following are intentionally not yet fully specified:

- names and identities of most allies and organizational representatives;
- Alya's exact original promise/destination;
- exact truth and details of her prior Ferida-related failure;
- exact sequence of chapters and scenes;
- exact mechanics of the Ferida and its personification;
- exact historical events revealed in Act V;
- exact fate of the organization in each ending state;
- exact composition and failure conditions of the community network;
- specific losses, deaths, separations, and recoveries;
- detailed character arcs for recruited allies;
- exact quest, boss, mission, and chapter structure.

These are not missing pillars. They are implementation/detail layers that must remain consistent with this canon.

---

# 16. Narrative-to-Gameplay Integration Principles

The narrative establishes the following required direction for gameplay integration:

| Narrative evolution | Gameplay implication |
|---|---|
| Alya accepts leadership | Base Management tutorial |
| Scarcity and priorities | Resource and assignment decisions |
| Delegation | Assigning responsibilities and accepting autonomous outcomes |
| Growth | Increasing complexity and infrastructure demands |
| Aptitude and specialization | Character development through roles and time |
| Representation | Allies/community members can gain political or functional authority |
| Regional influence | External missions, sidequests, aid, and relationships |
| Independence | Reduced reliance on institutional support |
| Community network | Systems extending beyond one base |
| Ferida escalation | Increasing pressure on combat and social systems |
| Final confrontation | The accumulated state of communities and allies matters |

The next design phase should audit existing gameplay systems against these requirements rather than invent mechanics independently of narrative purpose.

---

# 17. Source Hierarchy

For narrative questions, use this order:

1. **This document** — current canonical source of truth.
2. Later explicit decisions made after this document — until incorporated here.
3. Historical checkpoints in `docs/checkpoints/` — context and traceability only.

If historical documents disagree with this canon, the canon in this file wins.

---

**End of canonical narrative source of truth.**


## Embedded source: Combat contract

# Combat

## Meters
Vitality: primary defeat meter.
Strain: secondary pressure meter. It supports thresholds, alternate outcomes, reactive mechanics, and Overflow.

Keep damage channels distinct. A skill may affect Vitality, Strain, both, or convert one result into another when explicitly defined.

## Shared resources
Command: target-control resource generated by directive/manipulation actions; spent to alter behavior, reduce resistance, or prepare a Break.
Resolve: reactive resource generated through deliberate exposure or risk; enables responses and alternate finish paths.
Pressure: generated by exploiting weaknesses, vulnerable states, or unstable targets; improves damage and debuffs.
Fortitude: generated by receiving damage, resisting pressure, or surviving critical situations; spent for defense, retaliation, or survival.

## Skill keywords
Exploit: gains conditional bonuses against matching tags/states.
Consume: spends stacks/resources for a stronger effect.
Chain: changes when repeated or sequenced.
Threshold: changes based on a meter boundary.
Overflow: interacts with Strain above its normal threshold.

## Build identity
Do not use rigid classes. Build identity emerges from skill tags, stats, equipment, passives, modifications, and choices.

## Enemy difficulty
Prefer authored power bands plus behavioral variation, encounter composition, modifiers, and objectives. Do not universally scale all enemies to player level.

## Enemy intent
Enemies may expose intended actions. Defensive and reactive skills can inspect or respond to intent.

## Outcome resolution
Combat must support Defeat, Disable, Capture, Yield, Retreat, and ObjectiveComplete. Outcome rules are encounter-defined rather than globally forcing elimination.

## Embedded source: Status-effect contract

# Status Effects and Lifecycle

## Source of truth
Stats and effects must have one canonical source. Do not duplicate the same modifier in equipment, status, and cached state.

## Effect lifecycle
An effect has source, target, start rule, duration, stacks, strength, tags, and removal conditions.

At the beginning of the affected character's turn:
1. evaluate start-of-turn behavior;
2. decrement duration when the effect uses turn duration;
3. expire the effect immediately when its duration reaches its expiration condition;
4. recompute derived state if required.

## Stack policy
Different effects are processed independently in application order. Equivalent effects keep only the strongest active instance unless the effect definition explicitly allows stacking.

## Equipment rule
Removing equipment immediately removes every effect granted solely by that equipment. Recalculate derived stats immediately.

## Passive categories
CorePassive: persistent identity behavior.
BuildPassive: learned or selected build behavior.
ConditionalPassive: equipment, state, encounter, or context dependent.

## Implementation events
Effect application and removal should emit deterministic events so UI, logs, triggers, and reactions can subscribe without duplicating logic.

## Embedded source: Turn-resolution contract

# Turn Resolution Contract

This document defines the canonical order for turn-based encounter resolution.

## Turn phases
1. Select next active actor according to initiative/order rules.
2. Emit TurnStarted(actorId).
3. Resolve start-of-turn effects in deterministic application order.
4. For each affected effect using turn duration, decrement duration after its start behavior resolves.
5. Remove effects whose expiration condition is now satisfied; emit EffectRemoved.
6. Recalculate affected derived state.
7. If the actor is unable to act, resolve the defined skip/forced-action behavior and continue to phase 12.
8. Refresh or expose actor intent when the actor is AI-controlled.
9. Select an action; validate targeting, conditions, cooldown, costs, and gate requirements.
10. Commit costs, then resolve the action through its declared effect sequence.
11. Resolve triggered reactions, chains, thresholds, resource generation, and immediate outcome checks in deterministic order.
12. Resolve end-of-turn effects and emit TurnEnded(actorId).
13. Evaluate encounter terminal conditions. If none apply, advance to the next actor.

## Action resolution
An action is atomic from the perspective of validation: invalid actions must not partially spend costs or mutate state.

Recommended sequence:
Validate -> CommitCosts -> ApplyPrimaryEffects -> ApplySecondaryEffects -> EvaluateTriggers -> RecalculateDerivedState -> EmitEvents -> EvaluateOutcome.

## Ordering rules
- Application order is the default tie-breaker for equivalent priorities.
- Explicit priority overrides application order only when declared by data.
- Reactions created by an event resolve after the event's originating mutation unless explicitly marked interrupting.
- Terminal encounter outcomes stop further ordinary action resolution after the current atomic action completes.

## Required event payload minimum
Every turn/action event should include encounterId, actorId, sequenceNumber, eventType, and enough references to reproduce the state transition in logs.

## Determinism
Given identical canonical state, action selection, random seed/state, content version, and event ordering rules, resolution must produce identical canonical results.

## Embedded source: Full-game world and quest catalog

```json
{
  "schemaVersion": 1,
  "status": "CONTENT_LOCKED_DESIGN_NOT_RUNTIME_VALIDATED",
  "sourceOfTruth": "docs/FULL_GAME_CONTENT_LOCK.md",
  "rules": {
    "mainQuestCount": 47,
    "sidequestCount": 25,
    "regions": 7,
    "acts": 5,
    "expeditions": 8,
    "inventoryCapacity": "unlimited",
    "sidequestRequiresAlya": true,
    "expeditionUsesNPCsOnly": true,
    "optionalAdultContentGatesMainStory": false,
    "mandatoryActOneSeedLoss": true
  },
  "acts": [
    {
      "id": "ACT-01",
      "name": "Foundation",
      "title": "The Water We Share",
      "region": "REG-001",
      "theme": "Scarcity, blame, local knowledge, unavoidable loss",
      "climax": "BOS-001",
      "endState": "Alya becomes Brackenford's recognized leader; first facility and Expedition unlock."
    },
    {
      "id": "ACT-02",
      "name": "Construction",
      "title": "A Place for the Uncounted",
      "region": "REG-002",
      "theme": "Growth, integration, delegated responsibility, institutional rupture",
      "climax": "BOS-002",
      "endState": "Brackenford shelters people under a documented risk plan and establishes council governance."
    },
    {
      "id": "ACT-03",
      "name": "Consequences",
      "title": "The Cost of Being Free",
      "region": "REG-003",
      "theme": "Autonomy, scarcity, trade leverage, plural regional agreements",
      "climax": "BOS-003",
      "endState": "Three regions ratify a voluntary mutual-aid compact."
    },
    {
      "id": "ACT-04",
      "name": "Escalation",
      "title": "What the Wound Learns",
      "region": "REG-005",
      "theme": "Systemic exploitation, verification, delegation under pressure",
      "climax": "BOS-005",
      "endState": "The network survives in a changed form; evidence points toward the Wound's Confluence."
    },
    {
      "id": "ACT-05",
      "name": "Revelation and Resolution",
      "title": "A Future Without a Center",
      "region": "REG-007",
      "theme": "Truth, distributed responsibility, uncertain but durable recovery",
      "climax": "BOS-009",
      "endState": "The Ferida's sustaining conditions are transformed or constrained; epilogues follow world state."
    }
  ],
  "regions": [
    {
      "id": "REG-001",
      "name": "Ashfen Verge",
      "hub": "Brackenford",
      "unlock": "Start",
      "signature": "Waterworks, farms, damp lowlands",
      "gathering": [
        "Timber",
        "Fiber",
        "Botanical Extract"
      ],
      "pois": [
        "Brackenford Cistern",
        "Lower Terraces",
        "Root-Vault Sluice",
        "Old Channel Walk"
      ],
      "questline": "ACT-01",
      "encounterPool": [
        "ENM-002",
        "ENM-026",
        "ENM-027",
        "ENM-028"
      ]
    },
    {
      "id": "REG-002",
      "name": "Greenwake Basin",
      "hub": "Newfield Crossing",
      "unlock": "ACT-01 complete",
      "signature": "Refuge corridors, reclaimed fields, workshops",
      "gathering": [
        "Provisions",
        "Timber",
        "Botanical Extract"
      ],
      "pois": [
        "Refuge Camp",
        "Old Mill",
        "Greenwake Crossing",
        "Surveyor's Rise"
      ],
      "questline": "ACT-02",
      "encounterPool": [
        "ENM-001",
        "ENM-005",
        "ENM-008",
        "ENM-030"
      ]
    },
    {
      "id": "REG-003",
      "name": "Glassstep March",
      "hub": "Saltmarket",
      "unlock": "ACT-02 mid-act",
      "signature": "Salt-glass flats, caravan roads, market forts",
      "gathering": [
        "Gold",
        "Salvage",
        "Provisions"
      ],
      "pois": [
        "Saltmarket",
        "Glass Road",
        "Abandoned Tollhouse",
        "Storm Shelter"
      ],
      "questline": "ACT-03",
      "encounterPool": [
        "ENM-009",
        "ENM-010",
        "ENM-011",
        "ENM-024"
      ]
    },
    {
      "id": "REG-004",
      "name": "Mycelian Reach",
      "hub": "Root-Circle",
      "unlock": "ACT-03 early",
      "signature": "Living forest and fungal memory network",
      "gathering": [
        "Botanical Extract",
        "Research Notes",
        "Fiber"
      ],
      "pois": [
        "Root-Circle",
        "Memory Grove",
        "Moss Bridge",
        "Quiet Hollow"
      ],
      "questline": "ACT-03",
      "encounterPool": [
        "ENM-006",
        "ENM-017",
        "ENM-018",
        "ENM-031"
      ]
    },
    {
      "id": "REG-005",
      "name": "Cinderfall Reach",
      "hub": "Emberline",
      "unlock": "ACT-03 complete",
      "signature": "Volcanic ashlands and industrial settlements",
      "gathering": [
        "Salvage",
        "Timber",
        "Gold"
      ],
      "pois": [
        "Emberline Works",
        "Ash Clinic",
        "Broken Lift",
        "Cinder Road"
      ],
      "questline": "ACT-04",
      "encounterPool": [
        "ENM-012",
        "ENM-014",
        "ENM-032",
        "ENM-034"
      ]
    },
    {
      "id": "REG-006",
      "name": "The Shattered Archive",
      "hub": "Archive Perimeter",
      "unlock": "ACT-04 Q36",
      "signature": "Broken research/ritual complex and conflicting records",
      "gathering": [
        "Research Notes",
        "Salvage"
      ],
      "pois": [
        "Outer Stacks",
        "Witness Chamber",
        "Sealed Laboratory",
        "False Index"
      ],
      "questline": "ACT-04/05",
      "encounterPool": [
        "ENM-018",
        "ENM-033",
        "ENM-035"
      ]
    },
    {
      "id": "REG-007",
      "name": "The Wound's Confluence",
      "hub": "Coalition Staging Ground",
      "unlock": "ACT-05 Q41 plus coalition readiness",
      "signature": "Ecological and relational systems converge",
      "gathering": [
        "Research Notes",
        "Botanical Extract"
      ],
      "pois": [
        "Outer Anchor",
        "Memory Span",
        "Broken Causeway",
        "Confluence Heart"
      ],
      "questline": "ACT-05",
      "encounterPool": [
        "ENM-030",
        "ENM-031",
        "ENM-034",
        "ENM-035"
      ]
    }
  ],
  "factions": [
    {
      "id": "FACN-001",
      "name": "Brackenford Council",
      "tracks": [
        "cohesion",
        "representation_quality",
        "unresolved_grievances"
      ],
      "purpose": "Local governance and shared services"
    },
    {
      "id": "FACN-002",
      "name": "The Organization",
      "tracks": [
        "cooperation",
        "oversight_pressure",
        "credibility"
      ],
      "blocs": [
        "Pragmatists",
        "Reformers",
        "Hardliners"
      ],
      "purpose": "Regional infrastructure, protection, research and crisis response"
    },
    {
      "id": "FACN-003",
      "name": "Glassstep Caravans",
      "tracks": [
        "contract_reliability",
        "route_access"
      ],
      "purpose": "Trade and transportation; internal interests vary"
    },
    {
      "id": "FACN-004",
      "name": "Mycelian Circles",
      "tracks": [
        "knowledge_consent",
        "stewardship",
        "grievance"
      ],
      "purpose": "Distinct communities linked by living memory traditions"
    },
    {
      "id": "FACN-005",
      "name": "Cinderfall Works",
      "tracks": [
        "safety",
        "labor_obligations",
        "legitimacy"
      ],
      "purpose": "Industrial settlements and evacuation infrastructure"
    },
    {
      "id": "FACN-006",
      "name": "The Unbound",
      "tracks": [
        "safe_passage",
        "representation",
        "internal_fragmentation"
      ],
      "purpose": "Displaced people, deserters, stigmatized groups and mutual-aid cells"
    }
  ],
  "mainQuests": [
    {
      "id": "Q01",
      "act": "ACT-01",
      "title": "The Empty Cistern",
      "objective": "Meet Mara and the First Ally; establish the water dispute.",
      "exitFlag": "VS1_WATER_DISPUTE_KNOWN",
      "sequence": 1,
      "optional": false,
      "verticalSliceId": "VS1_Q01",
      "objectiveSteps": "Inspect cistern; speak to Mara and First Ally; record the initial water state.",
      "keyChoice": "Keep the ration schedule / share remaining clean water / delay judgment for evidence.",
      "consequence": "Sets initial community trust and water-sharing flags; no choice identifies a single villain.",
      "rewardIntent": "RES-007: local testimony; basic provisions.",
      "regionIntent": "REG-001",
      "choiceIsExplicit": true,
      "rewardValues": "Exact numeric amounts and item grant IDs must be reconciled against progression/economy balance before implementation; do not infer free rewards.",
      "failurePolicy": "Quest-specific partial failure changes cost, time, faction/relationship flags or encounter state; no optional quest can hard-lock the main story.",
      "dialogueKeyPrefix": "DLG_Q01",
      "regionIds": [
        "REG-001"
      ],
      "prerequisiteQuestIds": [],
      "encounterIds": [],
      "dialogueKeys": [
        "DLG_Q01.intro",
        "DLG_Q01.choice",
        "DLG_Q01.resolution"
      ],
      "implementationNote": "Choice flags and reward IDs must be persisted idempotently; use the documented exitFlag as the canonical completion signal."
    },
    {
      "id": "Q02",
      "act": "ACT-01",
      "title": "A Ration Is Not a History",
      "objective": "Learn that unequal allocation predates the Red Thread.",
      "exitFlag": "VS1_ALLOCATION_HISTORY_KNOWN",
      "sequence": 2,
      "optional": false,
      "verticalSliceId": "VS1_Q02",
      "objectiveSteps": "Interview Elder, residents and Mara; compare ration records with current conditions.",
      "keyChoice": "Prioritize testimony / prioritize records / combine both.",
      "consequence": "Evidence-first path improves later negotiation; dismissing residents creates a repairable grievance.",
      "rewardIntent": "RES-007: allocation ledger clue.",
      "regionIntent": "REG-001",
      "choiceIsExplicit": true,
      "rewardValues": "Exact numeric amounts and item grant IDs must be reconciled against progression/economy balance before implementation; do not infer free rewards.",
      "failurePolicy": "Quest-specific partial failure changes cost, time, faction/relationship flags or encounter state; no optional quest can hard-lock the main story.",
      "dialogueKeyPrefix": "DLG_Q02",
      "regionIds": [
        "REG-001"
      ],
      "prerequisiteQuestIds": [
        "Q01"
      ],
      "encounterIds": [],
      "dialogueKeys": [
        "DLG_Q02.intro",
        "DLG_Q02.choice",
        "DLG_Q02.resolution"
      ],
      "implementationNote": "Choice flags and reward IDs must be persisted idempotently; use the documented exitFlag as the canonical completion signal."
    },
    {
      "id": "Q03",
      "act": "ACT-01",
      "title": "Signs Beneath the Water",
      "objective": "Investigate the moving filaments without overclaiming their origin.",
      "exitFlag": "VS1_RED_THREAD_CONFIRMED",
      "sequence": 3,
      "optional": false,
      "verticalSliceId": "VS1_Q03",
      "objectiveSteps": "Inspect red filaments at two points and return with a sample or observation.",
      "keyChoice": "Collect a sample / mark and avoid the growth.",
      "consequence": "Sample improves research evidence but adds a handling requirement; observation is safer but less precise.",
      "rewardIntent": "ITM-034: protected sample or RES-007: field notes.",
      "regionIntent": "REG-001",
      "choiceIsExplicit": true,
      "rewardValues": "Exact numeric amounts and item grant IDs must be reconciled against progression/economy balance before implementation; do not infer free rewards.",
      "failurePolicy": "Quest-specific partial failure changes cost, time, faction/relationship flags or encounter state; no optional quest can hard-lock the main story.",
      "dialogueKeyPrefix": "DLG_Q03",
      "regionIds": [
        "REG-001"
      ],
      "prerequisiteQuestIds": [
        "Q02"
      ],
      "encounterIds": [
        "SPC-001"
      ],
      "dialogueKeys": [
        "DLG_Q03.intro",
        "DLG_Q03.choice",
        "DLG_Q03.resolution"
      ],
      "implementationNote": "Choice flags and reward IDs must be persisted idempotently; use the documented exitFlag as the canonical completion signal."
    },
    {
      "id": "Q04",
      "act": "ACT-01",
      "title": "A Door Left Open",
      "objective": "Stabilize an affected resident and choose a water-sharing priority.",
      "exitFlag": "VS1_CARE_ROUTE_RESOLVED",
      "sequence": 4,
      "optional": false,
      "verticalSliceId": "VS1_Q04",
      "objectiveSteps": "Stabilize an affected worker and choose how clean water is distributed for the next interval.",
      "keyChoice": "Workers first / household distribution / ask residents to choose a temporary rota.",
      "consequence": "Sets care priority and local cohesion; no option cures the manifestation.",
      "rewardIntent": "RES-003: botanical materials or care support flag.",
      "regionIntent": "REG-001",
      "choiceIsExplicit": true,
      "rewardValues": "Exact numeric amounts and item grant IDs must be reconciled against progression/economy balance before implementation; do not infer free rewards.",
      "failurePolicy": "Quest-specific partial failure changes cost, time, faction/relationship flags or encounter state; no optional quest can hard-lock the main story.",
      "dialogueKeyPrefix": "DLG_Q04",
      "regionIds": [
        "REG-001"
      ],
      "prerequisiteQuestIds": [
        "Q03"
      ],
      "encounterIds": [],
      "dialogueKeys": [
        "DLG_Q04.intro",
        "DLG_Q04.choice",
        "DLG_Q04.resolution"
      ],
      "implementationNote": "Choice flags and reward IDs must be persisted idempotently; use the documented exitFlag as the canonical completion signal."
    },
    {
      "id": "Q05",
      "act": "ACT-01",
      "title": "The Cost of a Quick Fix",
      "objective": "Discover that the sluice can be repaired but the seed reserve cannot be saved.",
      "exitFlag": "VS1_ROOT_VAULT_ROUTE_KNOWN",
      "sequence": 5,
      "optional": false,
      "verticalSliceId": "VS1_Q05",
      "objectiveSteps": "Survey the root-vault and identify a feasible repair route.",
      "keyChoice": "Trust Mara's maintenance notes / verify with a second survey.",
      "consequence": "Verified route unlocks staged diversion; single-source route remains feasible at a higher cost.",
      "rewardIntent": "RES-007: route plan.",
      "regionIntent": "REG-001",
      "choiceIsExplicit": true,
      "rewardValues": "Exact numeric amounts and item grant IDs must be reconciled against progression/economy balance before implementation; do not infer free rewards.",
      "failurePolicy": "Quest-specific partial failure changes cost, time, faction/relationship flags or encounter state; no optional quest can hard-lock the main story.",
      "dialogueKeyPrefix": "DLG_Q05",
      "regionIds": [
        "REG-001"
      ],
      "prerequisiteQuestIds": [
        "Q04"
      ],
      "encounterIds": [],
      "dialogueKeys": [
        "DLG_Q05.intro",
        "DLG_Q05.choice",
        "DLG_Q05.resolution"
      ],
      "implementationNote": "Choice flags and reward IDs must be persisted idempotently; use the documented exitFlag as the canonical completion signal."
    },
    {
      "id": "Q06",
      "act": "ACT-01",
      "title": "The Organization Arrives",
      "objective": "Receive and assess the containment proposal.",
      "exitFlag": "VS1_ORG_PLAN_PRESENTED",
      "sequence": 6,
      "optional": false,
      "verticalSliceId": "VS1_Q06",
      "objectiveSteps": "Hear the Organization's risk case and question assumptions.",
      "keyChoice": "Accept in principle / challenge without a plan / request time for an alternative.",
      "consequence": "Sets institutional stance; third option remains available in every branch.",
      "rewardIntent": "ITM-026: filter kit only on cooperation route; otherwise field notes.",
      "regionIntent": "REG-001",
      "choiceIsExplicit": true,
      "rewardValues": "Exact numeric amounts and item grant IDs must be reconciled against progression/economy balance before implementation; do not infer free rewards.",
      "failurePolicy": "Quest-specific partial failure changes cost, time, faction/relationship flags or encounter state; no optional quest can hard-lock the main story.",
      "dialogueKeyPrefix": "DLG_Q06",
      "regionIds": [
        "REG-001"
      ],
      "prerequisiteQuestIds": [
        "Q05"
      ],
      "encounterIds": [],
      "dialogueKeys": [
        "DLG_Q06.intro",
        "DLG_Q06.choice",
        "DLG_Q06.resolution"
      ],
      "implementationNote": "Choice flags and reward IDs must be persisted idempotently; use the documented exitFlag as the canonical completion signal."
    },
    {
      "id": "Q07",
      "act": "ACT-01",
      "title": "Three Parts of a Third Option",
      "objective": "Gather repair materials, local knowledge and coordinated care.",
      "exitFlag": "VS1_THIRD_OPTION_READY",
      "sequence": 7,
      "optional": false,
      "verticalSliceId": "VS1_Q07",
      "objectiveSteps": "Secure materials, recruit local participation, complete the Hollow Warden encounter, choose preparation priority.",
      "keyChoice": "Workers first / channel first / staged diversion if clue found.",
      "consequence": "Preparation changes climax pressure but cannot prevent seed-reserve loss.",
      "rewardIntent": "RES-001 + RES-002 mandatory repair materials; RES-003 filter support.",
      "regionIntent": "REG-001",
      "choiceIsExplicit": true,
      "rewardValues": "Exact numeric amounts and item grant IDs must be reconciled against progression/economy balance before implementation; do not infer free rewards.",
      "failurePolicy": "Quest-specific partial failure changes cost, time, faction/relationship flags or encounter state; no optional quest can hard-lock the main story.",
      "dialogueKeyPrefix": "DLG_Q07",
      "regionIds": [
        "REG-001"
      ],
      "prerequisiteQuestIds": [
        "Q06"
      ],
      "encounterIds": [
        "ENM-027"
      ],
      "dialogueKeys": [
        "DLG_Q07.intro",
        "DLG_Q07.choice",
        "DLG_Q07.resolution"
      ],
      "implementationNote": "Choice flags and reward IDs must be persisted idempotently; use the documented exitFlag as the canonical completion signal."
    },
    {
      "id": "Q08",
      "act": "ACT-01",
      "title": "Hold the Sluice",
      "objective": "Complete diversion, filament and gate objectives.",
      "exitFlag": "VS1_SLICE_CRISIS_RESOLVED",
      "sequence": 8,
      "optional": false,
      "verticalSliceId": "VS1_Q08",
      "objectiveSteps": "Complete diversion, sever the active filament, secure the gate; check all objective flags.",
      "keyChoice": "Spend community contribution on gate security / filament suppression / spread control.",
      "consequence": "Downstream channel is secured; seed reserve is lost regardless of combat result; retreat produces a costly partial resolution and recovery stage.",
      "rewardIntent": "RES-001 x2 and RES-002 x1 guaranteed after resolution; quest state seed loss.",
      "regionIntent": "REG-001",
      "choiceIsExplicit": true,
      "rewardValues": "Exact numeric amounts and item grant IDs must be reconciled against progression/economy balance before implementation; do not infer free rewards.",
      "failurePolicy": "Retreat or partial resolution leads to recovery/repair state; mandatory story loss persists and the main path remains completable.",
      "dialogueKeyPrefix": "DLG_Q08",
      "regionIds": [
        "REG-001"
      ],
      "prerequisiteQuestIds": [
        "Q07"
      ],
      "encounterIds": [
        "BOS-001"
      ],
      "dialogueKeys": [
        "DLG_Q08.intro",
        "DLG_Q08.choice",
        "DLG_Q08.resolution"
      ],
      "implementationNote": "Choice flags and reward IDs must be persisted idempotently; use the documented exitFlag as the canonical completion signal."
    },
    {
      "id": "Q09",
      "act": "ACT-01",
      "title": "What Remains",
      "objective": "Record seed loss, downstream protection and community costs.",
      "exitFlag": "VS1_LOSS_ACKNOWLEDGED",
      "sequence": 9,
      "optional": false,
      "verticalSliceId": "VS1_Q09",
      "objectiveSteps": "Record losses, hear affected residents and decide what is publicly acknowledged.",
      "keyChoice": "Publish the ledger / hold a community meeting / delay public report until verified.",
      "consequence": "Changes credibility and grievance flags; mandatory loss is never reversed.",
      "rewardIntent": "RES-007: documented loss record.",
      "regionIntent": "REG-001",
      "choiceIsExplicit": true,
      "rewardValues": "Exact numeric amounts and item grant IDs must be reconciled against progression/economy balance before implementation; do not infer free rewards.",
      "failurePolicy": "Quest-specific partial failure changes cost, time, faction/relationship flags or encounter state; no optional quest can hard-lock the main story.",
      "dialogueKeyPrefix": "DLG_Q09",
      "regionIds": [
        "REG-001"
      ],
      "prerequisiteQuestIds": [
        "Q08"
      ],
      "encounterIds": [],
      "dialogueKeys": [
        "DLG_Q09.intro",
        "DLG_Q09.choice",
        "DLG_Q09.resolution"
      ],
      "implementationNote": "Choice flags and reward IDs must be persisted idempotently; use the documented exitFlag as the canonical completion signal."
    },
    {
      "id": "Q10",
      "act": "ACT-01",
      "title": "A Place That Must Continue",
      "objective": "Recognize Alya as leader and choose an initial facility.",
      "exitFlag": "VS1_LEADERSHIP_RECOGNIZED",
      "sequence": 10,
      "optional": false,
      "verticalSliceId": "VS1_Q10",
      "objectiveSteps": "Hold a public meeting, accept leadership with boundaries, select one initial facility.",
      "keyChoice": "Recovery Room / Common Workshop / Coordination Board.",
      "consequence": "Facility choice persists; all other facilities remain unlockable; assignments and Expeditions unlock regardless.",
      "rewardIntent": "One selected facility; RES-004 small civic contribution.",
      "regionIntent": "REG-001",
      "choiceIsExplicit": true,
      "rewardValues": "Exact numeric amounts and item grant IDs must be reconciled against progression/economy balance before implementation; do not infer free rewards.",
      "failurePolicy": "Quest-specific partial failure changes cost, time, faction/relationship flags or encounter state; no optional quest can hard-lock the main story.",
      "dialogueKeyPrefix": "DLG_Q10",
      "regionIds": [
        "REG-001"
      ],
      "prerequisiteQuestIds": [
        "Q09"
      ],
      "encounterIds": [],
      "dialogueKeys": [
        "DLG_Q10.intro",
        "DLG_Q10.choice",
        "DLG_Q10.resolution"
      ],
      "implementationNote": "Choice flags and reward IDs must be persisted idempotently; use the documented exitFlag as the canonical completion signal."
    },
    {
      "id": "Q11",
      "act": "ACT-01",
      "title": "First Delegation",
      "objective": "Launch and resolve the first autonomous Expedition.",
      "exitFlag": "VS1_FIRST_EXPEDITION_RESOLVED",
      "sequence": 11,
      "optional": false,
      "verticalSliceId": "VS1_Q11",
      "objectiveSteps": "Select a team, preparation and destination; resolve the first autonomous Expedition.",
      "keyChoice": "Send for supplies / survey a route / escort a resident group.",
      "consequence": "Demonstrates NPC-only delegation and unavailable assigned allies; all outcomes return to main progression.",
      "rewardIntent": "EXP-001/003/004 outcome reward; no mandatory unique character loss.",
      "regionIntent": "REG-001",
      "choiceIsExplicit": true,
      "rewardValues": "Exact numeric amounts and item grant IDs must be reconciled against progression/economy balance before implementation; do not infer free rewards.",
      "failurePolicy": "Quest-specific partial failure changes cost, time, faction/relationship flags or encounter state; no optional quest can hard-lock the main story.",
      "dialogueKeyPrefix": "DLG_Q11",
      "regionIds": [
        "REG-001"
      ],
      "prerequisiteQuestIds": [
        "Q10"
      ],
      "encounterIds": [],
      "dialogueKeys": [
        "DLG_Q11.intro",
        "DLG_Q11.choice",
        "DLG_Q11.resolution"
      ],
      "implementationNote": "Choice flags and reward IDs must be persisted idempotently; use the documented exitFlag as the canonical completion signal."
    },
    {
      "id": "Q12",
      "act": "ACT-02",
      "title": "A Roof for Strangers",
      "objective": "Convert temporary shelter into a permanent refuge.",
      "exitFlag": "ACT2_REFUGE_ESTABLISHED",
      "sequence": 12,
      "optional": false,
      "objectiveSteps": "Survey shelter capacity, select construction location and move residents safely.",
      "keyChoice": "Build shelter first / prioritize common services / phase construction.",
      "consequence": "Sets refuge layout and upkeep modifiers; each option leaves a viable baseline.",
      "rewardIntent": "RES-001, RES-002; FAC-010 unlock path.",
      "regionIntent": "REG-002",
      "choiceIsExplicit": true,
      "rewardValues": "Exact numeric amounts and item grant IDs must be reconciled against progression/economy balance before implementation; do not infer free rewards.",
      "failurePolicy": "Quest-specific partial failure changes cost, time, faction/relationship flags or encounter state; no optional quest can hard-lock the main story.",
      "dialogueKeyPrefix": "DLG_Q12",
      "regionIds": [
        "REG-002"
      ],
      "prerequisiteQuestIds": [
        "Q11"
      ],
      "encounterIds": [],
      "dialogueKeys": [
        "DLG_Q12.intro",
        "DLG_Q12.choice",
        "DLG_Q12.resolution"
      ],
      "implementationNote": "Choice flags and reward IDs must be persisted idempotently; use the documented exitFlag as the canonical completion signal."
    },
    {
      "id": "Q13",
      "act": "ACT-02",
      "title": "The Work Nobody Sees",
      "objective": "Assign residents to care, gathering, training and maintenance.",
      "exitFlag": "ACT2_ASSIGNMENTS_INTRODUCED",
      "sequence": 13,
      "optional": false,
      "objectiveSteps": "Assign residents and allies to at least two functions; inspect aptitude and availability.",
      "keyChoice": "Optimize immediate output / preserve rest and training / rotate assignments.",
      "consequence": "Creates an early production vs recovery trade-off; no assignment permanently locks a character.",
      "rewardIntent": "RES-005 production and aptitude progress.",
      "regionIntent": "REG-002",
      "choiceIsExplicit": true,
      "rewardValues": "Exact numeric amounts and item grant IDs must be reconciled against progression/economy balance before implementation; do not infer free rewards.",
      "failurePolicy": "Quest-specific partial failure changes cost, time, faction/relationship flags or encounter state; no optional quest can hard-lock the main story.",
      "dialogueKeyPrefix": "DLG_Q13",
      "regionIds": [
        "REG-002"
      ],
      "prerequisiteQuestIds": [
        "Q12"
      ],
      "encounterIds": [],
      "dialogueKeys": [
        "DLG_Q13.intro",
        "DLG_Q13.choice",
        "DLG_Q13.resolution"
      ],
      "implementationNote": "Choice flags and reward IDs must be persisted idempotently; use the documented exitFlag as the canonical completion signal."
    },
    {
      "id": "Q14",
      "act": "ACT-02",
      "title": "The Ledger of Needs",
      "objective": "Create a transparent resource ledger and prioritize a shortage.",
      "exitFlag": "ACT2_RESOURCE_LEDGER_ACTIVE",
      "sequence": 14,
      "optional": false,
      "objectiveSteps": "Compare resource stores, projected upkeep and promised deliveries; choose a priority.",
      "keyChoice": "Housing / care / infrastructure first.",
      "consequence": "Creates a transparent ledger flag that improves later council options.",
      "rewardIntent": "RES-007: ledger method; RES-004 contract rebate if trade-ready.",
      "regionIntent": "REG-002",
      "choiceIsExplicit": true,
      "rewardValues": "Exact numeric amounts and item grant IDs must be reconciled against progression/economy balance before implementation; do not infer free rewards.",
      "failurePolicy": "Quest-specific partial failure changes cost, time, faction/relationship flags or encounter state; no optional quest can hard-lock the main story.",
      "dialogueKeyPrefix": "DLG_Q14",
      "regionIds": [
        "REG-002"
      ],
      "prerequisiteQuestIds": [
        "Q13"
      ],
      "encounterIds": [],
      "dialogueKeys": [
        "DLG_Q14.intro",
        "DLG_Q14.choice",
        "DLG_Q14.resolution"
      ],
      "implementationNote": "Choice flags and reward IDs must be persisted idempotently; use the documented exitFlag as the canonical completion signal."
    },
    {
      "id": "Q15",
      "act": "ACT-02",
      "title": "A Place at the Table",
      "objective": "Resolve a mediation arc and establish a resident voice.",
      "exitFlag": "ACT2_REPRESENTATION_STARTED",
      "sequence": 15,
      "optional": false,
      "objectiveSteps": "Mediate a resident dispute and provide a seat for the Devoto's proposal.",
      "keyChoice": "Temporary compromise / written agreement with review / defer pending evidence.",
      "consequence": "Written review improves representation quality; forced compromise creates a reversible grievance.",
      "rewardIntent": "ALLY-010 recruitment progress; morale flag.",
      "regionIntent": "REG-002",
      "choiceIsExplicit": true,
      "rewardValues": "Exact numeric amounts and item grant IDs must be reconciled against progression/economy balance before implementation; do not infer free rewards.",
      "failurePolicy": "Quest-specific partial failure changes cost, time, faction/relationship flags or encounter state; no optional quest can hard-lock the main story.",
      "dialogueKeyPrefix": "DLG_Q15",
      "regionIds": [
        "REG-002"
      ],
      "prerequisiteQuestIds": [
        "Q14"
      ],
      "encounterIds": [],
      "dialogueKeys": [
        "DLG_Q15.intro",
        "DLG_Q15.choice",
        "DLG_Q15.resolution"
      ],
      "implementationNote": "Choice flags and reward IDs must be persisted idempotently; use the documented exitFlag as the canonical completion signal."
    },
    {
      "id": "Q16",
      "act": "ACT-02",
      "title": "The Shape of a Promise",
      "objective": "Define the scope and review conditions of Alya's public promise.",
      "exitFlag": "ACT2_PROMISE_RECORDED",
      "sequence": 16,
      "optional": false,
      "objectiveSteps": "Make a public promise with scope, limits, owner and review date.",
      "keyChoice": "Promise rapid expansion / promise minimum safety / promise a review process.",
      "consequence": "The review-process option is most resilient but costs time/resources; no promise is consequence-free.",
      "rewardIntent": "RES-007: public commitment record.",
      "regionIntent": "REG-002",
      "choiceIsExplicit": true,
      "rewardValues": "Exact numeric amounts and item grant IDs must be reconciled against progression/economy balance before implementation; do not infer free rewards.",
      "failurePolicy": "Quest-specific partial failure changes cost, time, faction/relationship flags or encounter state; no optional quest can hard-lock the main story.",
      "dialogueKeyPrefix": "DLG_Q16",
      "regionIds": [
        "REG-002"
      ],
      "prerequisiteQuestIds": [
        "Q15"
      ],
      "encounterIds": [],
      "dialogueKeys": [
        "DLG_Q16.intro",
        "DLG_Q16.choice",
        "DLG_Q16.resolution"
      ],
      "implementationNote": "Choice flags and reward IDs must be persisted idempotently; use the documented exitFlag as the canonical completion signal."
    },
    {
      "id": "Q17",
      "act": "ACT-02",
      "title": "A Road with Two Names",
      "objective": "Open Greenwake Basin and negotiate local access.",
      "exitFlag": "REG002_ACCESS_GRANTED",
      "sequence": 17,
      "optional": false,
      "objectiveSteps": "Open a route to Greenwake by negotiating with local stewards and clearing a route hazard.",
      "keyChoice": "Share maintenance / pay a toll / request a trial period.",
      "consequence": "Route access opens; terms affect future trade costs and local legitimacy.",
      "rewardIntent": "REG-002 access; ITM-016 opportunity.",
      "regionIntent": "REG-002",
      "choiceIsExplicit": true,
      "rewardValues": "Exact numeric amounts and item grant IDs must be reconciled against progression/economy balance before implementation; do not infer free rewards.",
      "failurePolicy": "Quest-specific partial failure changes cost, time, faction/relationship flags or encounter state; no optional quest can hard-lock the main story.",
      "dialogueKeyPrefix": "DLG_Q17",
      "regionIds": [
        "REG-002"
      ],
      "prerequisiteQuestIds": [
        "Q16"
      ],
      "encounterIds": [
        "SPC-003"
      ],
      "dialogueKeys": [
        "DLG_Q17.intro",
        "DLG_Q17.choice",
        "DLG_Q17.resolution"
      ],
      "implementationNote": "Choice flags and reward IDs must be persisted idempotently; use the documented exitFlag as the canonical completion signal."
    },
    {
      "id": "Q18",
      "act": "ACT-02",
      "title": "The Pilot Community",
      "objective": "Negotiate Organization reporting and supervision terms.",
      "exitFlag": "ACT2_PILOT_TERMS_PRESENTED",
      "sequence": 18,
      "optional": false,
      "objectiveSteps": "Negotiate the Organization's proposed pilot terms and data access.",
      "keyChoice": "Accept standard reporting / negotiate local veto and review / reject external oversight.",
      "consequence": "Sets oversight pressure and cooperation independently; rejecting terms does not make every Organization NPC hostile.",
      "rewardIntent": "RES-007: pilot agreement or local governance flag.",
      "regionIntent": "REG-002",
      "choiceIsExplicit": true,
      "rewardValues": "Exact numeric amounts and item grant IDs must be reconciled against progression/economy balance before implementation; do not infer free rewards.",
      "failurePolicy": "Quest-specific partial failure changes cost, time, faction/relationship flags or encounter state; no optional quest can hard-lock the main story.",
      "dialogueKeyPrefix": "DLG_Q18",
      "regionIds": [
        "REG-002"
      ],
      "prerequisiteQuestIds": [
        "Q17"
      ],
      "encounterIds": [],
      "dialogueKeys": [
        "DLG_Q18.intro",
        "DLG_Q18.choice",
        "DLG_Q18.resolution"
      ],
      "implementationNote": "Choice flags and reward IDs must be persisted idempotently; use the documented exitFlag as the canonical completion signal."
    },
    {
      "id": "Q19",
      "act": "ACT-02",
      "title": "The People Marked for Moving",
      "objective": "Investigate the relocation order and hear affected residents.",
      "exitFlag": "ACT2_RELOCATION_ORDER_KNOWN",
      "sequence": 19,
      "optional": false,
      "objectiveSteps": "Meet the displaced group and verify the relocation order, risks and available safeguards.",
      "keyChoice": "Prioritize testimony / prioritize risk records / conduct a joint review.",
      "consequence": "Creates evidence and safe-passage flags; the group is not treated as a monolith.",
      "rewardIntent": "FAC-010 capacity progress; RES-005 cost estimate.",
      "regionIntent": "REG-002",
      "choiceIsExplicit": true,
      "rewardValues": "Exact numeric amounts and item grant IDs must be reconciled against progression/economy balance before implementation; do not infer free rewards.",
      "failurePolicy": "Quest-specific partial failure changes cost, time, faction/relationship flags or encounter state; no optional quest can hard-lock the main story.",
      "dialogueKeyPrefix": "DLG_Q19",
      "regionIds": [
        "REG-002"
      ],
      "prerequisiteQuestIds": [
        "Q18"
      ],
      "encounterIds": [],
      "dialogueKeys": [
        "DLG_Q19.intro",
        "DLG_Q19.choice",
        "DLG_Q19.resolution"
      ],
      "implementationNote": "Choice flags and reward IDs must be persisted idempotently; use the documented exitFlag as the canonical completion signal."
    },
    {
      "id": "Q20",
      "act": "ACT-02",
      "title": "The Order We Refuse",
      "objective": "Shelter the group with a documented risk plan; formalize council governance.",
      "exitFlag": "ACT2_INSTITUTIONAL_RUPTURE",
      "sequence": 20,
      "optional": false,
      "objectiveSteps": "Decide whether to shelter the group and formalize council authority.",
      "keyChoice": "Shelter under documented controls / negotiate a time-limited pause / comply with relocation but preserve appeal.",
      "consequence": "All routes advance the act, but only shelter route triggers the canonical institutional rupture; the main arc must still show consequences of exclusion if chosen.",
      "rewardIntent": "FAC-009 council unlock; FACN-002 bloc state mutation.",
      "regionIntent": "REG-002",
      "choiceIsExplicit": true,
      "rewardValues": "Exact numeric amounts and item grant IDs must be reconciled against progression/economy balance before implementation; do not infer free rewards.",
      "failurePolicy": "Quest-specific partial failure changes cost, time, faction/relationship flags or encounter state; no optional quest can hard-lock the main story.",
      "dialogueKeyPrefix": "DLG_Q20",
      "regionIds": [
        "REG-002"
      ],
      "prerequisiteQuestIds": [
        "Q19"
      ],
      "encounterIds": [],
      "dialogueKeys": [
        "DLG_Q20.intro",
        "DLG_Q20.choice",
        "DLG_Q20.resolution"
      ],
      "implementationNote": "Choice flags and reward IDs must be persisted idempotently; use the documented exitFlag as the canonical completion signal."
    },
    {
      "id": "Q21",
      "act": "ACT-03",
      "title": "Freedom Has a Price",
      "objective": "Choose an economic stabilization policy after support guarantees end.",
      "exitFlag": "ACT3_AUTONOMY_COST_ACCEPTED",
      "sequence": 21,
      "optional": false,
      "objectiveSteps": "Review lost support, forecast shortages and choose a stabilization policy.",
      "keyChoice": "Reduce nonessential spending / request reciprocal aid / expand trade exposure.",
      "consequence": "Each route solves one near-term problem while creating a different risk.",
      "rewardIntent": "RES-004 or RES-005 according to route; no free bailout.",
      "regionIntent": "REG-003",
      "choiceIsExplicit": true,
      "rewardValues": "Exact numeric amounts and item grant IDs must be reconciled against progression/economy balance before implementation; do not infer free rewards.",
      "failurePolicy": "Quest-specific partial failure changes cost, time, faction/relationship flags or encounter state; no optional quest can hard-lock the main story.",
      "dialogueKeyPrefix": "DLG_Q21",
      "regionIds": [
        "REG-003",
        "REG-004"
      ],
      "prerequisiteQuestIds": [
        "Q20"
      ],
      "encounterIds": [],
      "dialogueKeys": [
        "DLG_Q21.intro",
        "DLG_Q21.choice",
        "DLG_Q21.resolution"
      ],
      "implementationNote": "Choice flags and reward IDs must be persisted idempotently; use the documented exitFlag as the canonical completion signal."
    },
    {
      "id": "Q22",
      "act": "ACT-03",
      "title": "The Glassstep Contract",
      "objective": "Negotiate a trade compact with quotas, exceptions and dispute clauses.",
      "exitFlag": "ACT3_GLASSSTEP_COMPACT",
      "sequence": 22,
      "optional": false,
      "objectiveSteps": "Negotiate a trade compact with quotas, exceptions, delivery windows and dispute resolution.",
      "keyChoice": "Fixed quota / flexible quota with audit / short trial contract.",
      "consequence": "Contract reliability and route access become independent flags.",
      "rewardIntent": "ITM-021 opportunity; RES-004 trade return.",
      "regionIntent": "REG-003",
      "choiceIsExplicit": true,
      "rewardValues": "Exact numeric amounts and item grant IDs must be reconciled against progression/economy balance before implementation; do not infer free rewards.",
      "failurePolicy": "Quest-specific partial failure changes cost, time, faction/relationship flags or encounter state; no optional quest can hard-lock the main story.",
      "dialogueKeyPrefix": "DLG_Q22",
      "regionIds": [
        "REG-003",
        "REG-004"
      ],
      "prerequisiteQuestIds": [
        "Q21"
      ],
      "encounterIds": [],
      "dialogueKeys": [
        "DLG_Q22.intro",
        "DLG_Q22.choice",
        "DLG_Q22.resolution"
      ],
      "implementationNote": "Choice flags and reward IDs must be persisted idempotently; use the documented exitFlag as the canonical completion signal."
    },
    {
      "id": "Q23",
      "act": "ACT-03",
      "title": "The Empty Caravan",
      "objective": "Investigate a missing shipment and identify the incentive failure.",
      "exitFlag": "ACT3_SHIPMENT_CASE_RESOLVED",
      "sequence": 23,
      "optional": false,
      "objectiveSteps": "Track the missing caravan through witnesses, records and route conditions.",
      "keyChoice": "Accuse sabotage / audit incentives and dispatch / negotiate compensation first.",
      "consequence": "Evidence-led path identifies the structural failure; premature accusation causes a repairable faction penalty.",
      "rewardIntent": "RES-006 salvage or RES-004 compensation depending route.",
      "regionIntent": "REG-003",
      "choiceIsExplicit": true,
      "rewardValues": "Exact numeric amounts and item grant IDs must be reconciled against progression/economy balance before implementation; do not infer free rewards.",
      "failurePolicy": "Quest-specific partial failure changes cost, time, faction/relationship flags or encounter state; no optional quest can hard-lock the main story.",
      "dialogueKeyPrefix": "DLG_Q23",
      "regionIds": [
        "REG-003",
        "REG-004"
      ],
      "prerequisiteQuestIds": [
        "Q22"
      ],
      "encounterIds": [
        "SPC-003"
      ],
      "dialogueKeys": [
        "DLG_Q23.intro",
        "DLG_Q23.choice",
        "DLG_Q23.resolution"
      ],
      "implementationNote": "Choice flags and reward IDs must be persisted idempotently; use the documented exitFlag as the canonical completion signal."
    },
    {
      "id": "Q24",
      "act": "ACT-03",
      "title": "Two Fires, One River",
      "objective": "Mediate a resource dispute with no cost-free outcome.",
      "exitFlag": "ACT3_RIVER_AGREEMENT",
      "sequence": 24,
      "optional": false,
      "objectiveSteps": "Resolve competing water and fuel needs between two settlements.",
      "keyChoice": "Equal split / priority by immediate risk / negotiated rotating access.",
      "consequence": "No branch satisfies all parties; clear review rules preserve future cooperation.",
      "rewardIntent": "RES-005 supplies and a regional agreement flag.",
      "regionIntent": "REG-003",
      "choiceIsExplicit": true,
      "rewardValues": "Exact numeric amounts and item grant IDs must be reconciled against progression/economy balance before implementation; do not infer free rewards.",
      "failurePolicy": "Quest-specific partial failure changes cost, time, faction/relationship flags or encounter state; no optional quest can hard-lock the main story.",
      "dialogueKeyPrefix": "DLG_Q24",
      "regionIds": [
        "REG-003",
        "REG-004"
      ],
      "prerequisiteQuestIds": [
        "Q23"
      ],
      "encounterIds": [],
      "dialogueKeys": [
        "DLG_Q24.intro",
        "DLG_Q24.choice",
        "DLG_Q24.resolution"
      ],
      "implementationNote": "Choice flags and reward IDs must be persisted idempotently; use the documented exitFlag as the canonical completion signal."
    },
    {
      "id": "Q25",
      "act": "ACT-03",
      "title": "A Different Kind of Kinship",
      "objective": "Enter Mycelian Reach and negotiate with its leaders.",
      "exitFlag": "ACT3_MYCELIAN_ACCESS",
      "sequence": 25,
      "optional": false,
      "objectiveSteps": "Enter Mycelian Reach and negotiate access with the Matriarch and Guide.",
      "keyChoice": "Request shared research / request passage only / offer reciprocal stewardship.",
      "consequence": "Knowledge-sharing requires explicit consent and reciprocity; passage can be granted without sharing memory.",
      "rewardIntent": "REG-004 access; RES-007 research opportunity.",
      "regionIntent": "REG-004",
      "choiceIsExplicit": true,
      "rewardValues": "Exact numeric amounts and item grant IDs must be reconciled against progression/economy balance before implementation; do not infer free rewards.",
      "failurePolicy": "Quest-specific partial failure changes cost, time, faction/relationship flags or encounter state; no optional quest can hard-lock the main story.",
      "dialogueKeyPrefix": "DLG_Q25",
      "regionIds": [
        "REG-003",
        "REG-004"
      ],
      "prerequisiteQuestIds": [
        "Q24"
      ],
      "encounterIds": [],
      "dialogueKeys": [
        "DLG_Q25.intro",
        "DLG_Q25.choice",
        "DLG_Q25.resolution"
      ],
      "implementationNote": "Choice flags and reward IDs must be persisted idempotently; use the documented exitFlag as the canonical completion signal."
    },
    {
      "id": "Q26",
      "act": "ACT-03",
      "title": "What the Roots Remember",
      "objective": "Choose consent and reciprocity terms for shared memory.",
      "exitFlag": "ACT3_MEMORY_PROTOCOL",
      "sequence": 26,
      "optional": false,
      "objectiveSteps": "Inspect the memory network and establish what may be recorded, shared and withdrawn.",
      "keyChoice": "Open archive / restricted archive / community-controlled summary.",
      "consequence": "Sets knowledge consent and grievance; no choice erases historical harm.",
      "rewardIntent": "RES-007 research notes; ENM-006 encounter modifier.",
      "regionIntent": "REG-004",
      "choiceIsExplicit": true,
      "rewardValues": "Exact numeric amounts and item grant IDs must be reconciled against progression/economy balance before implementation; do not infer free rewards.",
      "failurePolicy": "Quest-specific partial failure changes cost, time, faction/relationship flags or encounter state; no optional quest can hard-lock the main story.",
      "dialogueKeyPrefix": "DLG_Q26",
      "regionIds": [
        "REG-003",
        "REG-004"
      ],
      "prerequisiteQuestIds": [
        "Q25"
      ],
      "encounterIds": [
        "BOS-004"
      ],
      "dialogueKeys": [
        "DLG_Q26.intro",
        "DLG_Q26.choice",
        "DLG_Q26.resolution"
      ],
      "implementationNote": "Choice flags and reward IDs must be persisted idempotently; use the documented exitFlag as the canonical completion signal."
    },
    {
      "id": "Q27",
      "act": "ACT-03",
      "title": "The Price of a Cure",
      "objective": "Allocate scarce treatment and research access.",
      "exitFlag": "ACT3_TREATMENT_POLICY",
      "sequence": 27,
      "optional": false,
      "objectiveSteps": "Allocate a scarce treatment and research supply under transparent criteria.",
      "keyChoice": "Treat highest immediate risk / distribute minimum treatment / reserve some for research under oversight.",
      "consequence": "Creates a persistent policy flag; research never overrides urgent care without explicit choice.",
      "rewardIntent": "RES-003 stabilizer or RES-007 research progress.",
      "regionIntent": "REG-004",
      "choiceIsExplicit": true,
      "rewardValues": "Exact numeric amounts and item grant IDs must be reconciled against progression/economy balance before implementation; do not infer free rewards.",
      "failurePolicy": "Quest-specific partial failure changes cost, time, faction/relationship flags or encounter state; no optional quest can hard-lock the main story.",
      "dialogueKeyPrefix": "DLG_Q27",
      "regionIds": [
        "REG-003",
        "REG-004"
      ],
      "prerequisiteQuestIds": [
        "Q26"
      ],
      "encounterIds": [],
      "dialogueKeys": [
        "DLG_Q27.intro",
        "DLG_Q27.choice",
        "DLG_Q27.resolution"
      ],
      "implementationNote": "Choice flags and reward IDs must be persisted idempotently; use the documented exitFlag as the canonical completion signal."
    },
    {
      "id": "Q28",
      "act": "ACT-03",
      "title": "A Voice from the Organization",
      "objective": "Cooperate with an internal reformer while protecting local authority.",
      "exitFlag": "ACT3_REFORMER_PACT",
      "sequence": 28,
      "optional": false,
      "objectiveSteps": "Meet an Organization reformer and define safe cooperation terms.",
      "keyChoice": "Share evidence openly / share verified excerpts / decline but preserve a channel.",
      "consequence": "Changes reformer relationship and hardliner suspicion separately.",
      "rewardIntent": "FAC-006 research path; institutional cooperation flag.",
      "regionIntent": "REG-002/004",
      "choiceIsExplicit": true,
      "rewardValues": "Exact numeric amounts and item grant IDs must be reconciled against progression/economy balance before implementation; do not infer free rewards.",
      "failurePolicy": "Quest-specific partial failure changes cost, time, faction/relationship flags or encounter state; no optional quest can hard-lock the main story.",
      "dialogueKeyPrefix": "DLG_Q28",
      "regionIds": [
        "REG-002",
        "REG-004"
      ],
      "prerequisiteQuestIds": [
        "Q27"
      ],
      "encounterIds": [],
      "dialogueKeys": [
        "DLG_Q28.intro",
        "DLG_Q28.choice",
        "DLG_Q28.resolution"
      ],
      "implementationNote": "Choice flags and reward IDs must be persisted idempotently; use the documented exitFlag as the canonical completion signal."
    },
    {
      "id": "Q29",
      "act": "ACT-03",
      "title": "The Compact of Three Regions",
      "objective": "Ratify the mutual-aid compact with explicit local exceptions.",
      "exitFlag": "ACT3_REGIONAL_COMPACT",
      "sequence": 29,
      "optional": false,
      "objectiveSteps": "Ratify mutual aid with three regions, contributions, opt-outs and dispute resolution.",
      "keyChoice": "Strong central dispatch / regional opt-in coordination / minimal compact.",
      "consequence": "Builds network readiness; local exceptions remain enforceable.",
      "rewardIntent": "RES-008 agreement-bound Trust Tokens; coalition flag.",
      "regionIntent": "REG-003/004",
      "choiceIsExplicit": true,
      "rewardValues": "Exact numeric amounts and item grant IDs must be reconciled against progression/economy balance before implementation; do not infer free rewards.",
      "failurePolicy": "Quest-specific partial failure changes cost, time, faction/relationship flags or encounter state; no optional quest can hard-lock the main story.",
      "dialogueKeyPrefix": "DLG_Q29",
      "regionIds": [
        "REG-003",
        "REG-004"
      ],
      "prerequisiteQuestIds": [
        "Q28"
      ],
      "encounterIds": [],
      "dialogueKeys": [
        "DLG_Q29.intro",
        "DLG_Q29.choice",
        "DLG_Q29.resolution"
      ],
      "implementationNote": "Choice flags and reward IDs must be persisted idempotently; use the documented exitFlag as the canonical completion signal."
    },
    {
      "id": "Q30",
      "act": "ACT-04",
      "title": "When the Signals Lie",
      "objective": "Verify a manipulated warning and establish redundancy.",
      "exitFlag": "ACT4_SIGNAL_VERIFICATION",
      "sequence": 30,
      "optional": false,
      "objectiveSteps": "Audit a false warning and build independent verification channels.",
      "keyChoice": "Centralize verification / two-source verification / local confirmation protocol.",
      "consequence": "Two-source redundancy is robust but slower; centralization is faster and vulnerable.",
      "rewardIntent": "FAC-012 signal tower progress; RES-006.",
      "regionIntent": "REG-005",
      "choiceIsExplicit": true,
      "rewardValues": "Exact numeric amounts and item grant IDs must be reconciled against progression/economy balance before implementation; do not infer free rewards.",
      "failurePolicy": "Quest-specific partial failure changes cost, time, faction/relationship flags or encounter state; no optional quest can hard-lock the main story.",
      "dialogueKeyPrefix": "DLG_Q30",
      "regionIds": [
        "REG-005",
        "REG-006"
      ],
      "prerequisiteQuestIds": [
        "Q29"
      ],
      "encounterIds": [
        "SPC-007"
      ],
      "dialogueKeys": [
        "DLG_Q30.intro",
        "DLG_Q30.choice",
        "DLG_Q30.resolution"
      ],
      "implementationNote": "Choice flags and reward IDs must be persisted idempotently; use the documented exitFlag as the canonical completion signal."
    },
    {
      "id": "Q31",
      "act": "ACT-04",
      "title": "The Cinderfall Evacuation",
      "objective": "Evacuate civilians with limited transport and time.",
      "exitFlag": "ACT4_EVACUATION_RESOLVED",
      "sequence": 31,
      "optional": false,
      "objectiveSteps": "Move civilians and critical supplies under limited transport and time.",
      "keyChoice": "Prioritize vulnerable residents / preserve critical infrastructure / split the convoy.",
      "consequence": "Outcome depends on preparation and prior resource decisions; no route saves everything.",
      "rewardIntent": "RES-005; evacuation state.",
      "regionIntent": "REG-005",
      "choiceIsExplicit": true,
      "rewardValues": "Exact numeric amounts and item grant IDs must be reconciled against progression/economy balance before implementation; do not infer free rewards.",
      "failurePolicy": "Quest-specific partial failure changes cost, time, faction/relationship flags or encounter state; no optional quest can hard-lock the main story.",
      "dialogueKeyPrefix": "DLG_Q31",
      "regionIds": [
        "REG-005",
        "REG-006"
      ],
      "prerequisiteQuestIds": [
        "Q30"
      ],
      "encounterIds": [
        "SPC-006"
      ],
      "dialogueKeys": [
        "DLG_Q31.intro",
        "DLG_Q31.choice",
        "DLG_Q31.resolution"
      ],
      "implementationNote": "Choice flags and reward IDs must be persisted idempotently; use the documented exitFlag as the canonical completion signal."
    },
    {
      "id": "Q32",
      "act": "ACT-04",
      "title": "The Measure of a Life",
      "objective": "Challenge a triage protocol that hides value judgments.",
      "exitFlag": "ACT4_TRIAGE_REVIEWED",
      "sequence": 32,
      "optional": false,
      "objectiveSteps": "Audit a triage system and make its hidden values explicit.",
      "keyChoice": "Keep speed-first protocol / add appeal and review / delegate to local clinics.",
      "consequence": "Appeal and review cost time but reduce systemic harm and Ferida leverage.",
      "rewardIntent": "RES-003; evidence integrity flag.",
      "regionIntent": "REG-005",
      "choiceIsExplicit": true,
      "rewardValues": "Exact numeric amounts and item grant IDs must be reconciled against progression/economy balance before implementation; do not infer free rewards.",
      "failurePolicy": "Quest-specific partial failure changes cost, time, faction/relationship flags or encounter state; no optional quest can hard-lock the main story.",
      "dialogueKeyPrefix": "DLG_Q32",
      "regionIds": [
        "REG-005",
        "REG-006"
      ],
      "prerequisiteQuestIds": [
        "Q31"
      ],
      "encounterIds": [],
      "dialogueKeys": [
        "DLG_Q32.intro",
        "DLG_Q32.choice",
        "DLG_Q32.resolution"
      ],
      "implementationNote": "Choice flags and reward IDs must be persisted idempotently; use the documented exitFlag as the canonical completion signal."
    },
    {
      "id": "Q33",
      "act": "ACT-04",
      "title": "The Delegates Disagree",
      "objective": "Resolve a council crisis without Alya simply overruling delegates.",
      "exitFlag": "ACT4_DELEGATE_DISPUTE_RESOLVED",
      "sequence": 33,
      "optional": false,
      "objectiveSteps": "Resolve a council split without Alya issuing a unilateral command.",
      "keyChoice": "Delegate a binding vote / mediate a time-limited compromise / allow a region to dissent and leave temporarily.",
      "consequence": "Tests whether prior governance systems can tolerate disagreement; dissent is not automatically betrayal.",
      "rewardIntent": "Council cohesion or autonomy flags.",
      "regionIntent": "REG-005",
      "choiceIsExplicit": true,
      "rewardValues": "Exact numeric amounts and item grant IDs must be reconciled against progression/economy balance before implementation; do not infer free rewards.",
      "failurePolicy": "Quest-specific partial failure changes cost, time, faction/relationship flags or encounter state; no optional quest can hard-lock the main story.",
      "dialogueKeyPrefix": "DLG_Q33",
      "regionIds": [
        "REG-005",
        "REG-006"
      ],
      "prerequisiteQuestIds": [
        "Q32"
      ],
      "encounterIds": [],
      "dialogueKeys": [
        "DLG_Q33.intro",
        "DLG_Q33.choice",
        "DLG_Q33.resolution"
      ],
      "implementationNote": "Choice flags and reward IDs must be persisted idempotently; use the documented exitFlag as the canonical completion signal."
    },
    {
      "id": "Q34",
      "act": "ACT-04",
      "title": "The Broken Route",
      "objective": "Restore a regional corridor through direct action and an Expedition.",
      "exitFlag": "ACT4_ROUTE_RESTORED",
      "sequence": 34,
      "optional": false,
      "objectiveSteps": "Restore the broken route using direct work and a delegated survey/escort.",
      "keyChoice": "Repair the shortest route / secure a safer detour / split teams with higher coordination cost.",
      "consequence": "Reopens a corridor; route risk and expedition readiness affect future travel.",
      "rewardIntent": "RES-001, RES-006; EXP-003 result.",
      "regionIntent": "REG-005",
      "choiceIsExplicit": true,
      "rewardValues": "Exact numeric amounts and item grant IDs must be reconciled against progression/economy balance before implementation; do not infer free rewards.",
      "failurePolicy": "Quest-specific partial failure changes cost, time, faction/relationship flags or encounter state; no optional quest can hard-lock the main story.",
      "dialogueKeyPrefix": "DLG_Q34",
      "regionIds": [
        "REG-005",
        "REG-006"
      ],
      "prerequisiteQuestIds": [
        "Q33"
      ],
      "encounterIds": [
        "SPC-005"
      ],
      "dialogueKeys": [
        "DLG_Q34.intro",
        "DLG_Q34.choice",
        "DLG_Q34.resolution"
      ],
      "implementationNote": "Choice flags and reward IDs must be persisted idempotently; use the documented exitFlag as the canonical completion signal."
    },
    {
      "id": "Q35",
      "act": "ACT-04",
      "title": "A Familiar Mistake",
      "objective": "Alya over-centralizes; allies and delegates must take responsibility.",
      "exitFlag": "ACT4_CENTRALIZATION_CONSEQUENCE",
      "sequence": 35,
      "optional": false,
      "objectiveSteps": "Confront the cost of Alya centralizing all decisions and let allies take ownership.",
      "keyChoice": "Retain emergency control / delegate specific authorities / call a review and distribute powers.",
      "consequence": "The act's setback occurs regardless; supported delegation reduces recovery cost.",
      "rewardIntent": "Ally arc flags; RES-007 governance review.",
      "regionIntent": "REG-005",
      "choiceIsExplicit": true,
      "rewardValues": "Exact numeric amounts and item grant IDs must be reconciled against progression/economy balance before implementation; do not infer free rewards.",
      "failurePolicy": "Quest-specific partial failure changes cost, time, faction/relationship flags or encounter state; no optional quest can hard-lock the main story.",
      "dialogueKeyPrefix": "DLG_Q35",
      "regionIds": [
        "REG-005",
        "REG-006"
      ],
      "prerequisiteQuestIds": [
        "Q34"
      ],
      "encounterIds": [],
      "dialogueKeys": [
        "DLG_Q35.intro",
        "DLG_Q35.choice",
        "DLG_Q35.resolution"
      ],
      "implementationNote": "Choice flags and reward IDs must be persisted idempotently; use the documented exitFlag as the canonical completion signal."
    },
    {
      "id": "Q36",
      "act": "ACT-04",
      "title": "The Shattered Archive",
      "objective": "Enter the archive and gather records from multiple sources.",
      "exitFlag": "ACT4_ARCHIVE_OPENED",
      "sequence": 36,
      "optional": false,
      "objectiveSteps": "Enter the Archive and recover three independent records.",
      "keyChoice": "Prioritize official records / witness accounts / ecological traces; all three can be recovered in any order.",
      "consequence": "Cross-checked evidence opens the next quest; one source alone remains insufficient.",
      "rewardIntent": "RES-007 research notes; REG-006 access.",
      "regionIntent": "REG-006",
      "choiceIsExplicit": true,
      "rewardValues": "Exact numeric amounts and item grant IDs must be reconciled against progression/economy balance before implementation; do not infer free rewards.",
      "failurePolicy": "Quest-specific partial failure changes cost, time, faction/relationship flags or encounter state; no optional quest can hard-lock the main story.",
      "dialogueKeyPrefix": "DLG_Q36",
      "regionIds": [
        "REG-006"
      ],
      "prerequisiteQuestIds": [
        "Q35"
      ],
      "encounterIds": [
        "BOS-007"
      ],
      "dialogueKeys": [
        "DLG_Q36.intro",
        "DLG_Q36.choice",
        "DLG_Q36.resolution"
      ],
      "implementationNote": "Choice flags and reward IDs must be persisted idempotently; use the documented exitFlag as the canonical completion signal."
    },
    {
      "id": "Q37",
      "act": "ACT-04",
      "title": "The Wound Learns",
      "objective": "Discover how the Ferida exploits systems and feedback loops.",
      "exitFlag": "ACT4_FERIDA_SYSTEMIC_MODEL",
      "sequence": 37,
      "optional": false,
      "objectiveSteps": "Compare evidence and identify how the Ferida exploits feedback systems.",
      "keyChoice": "Publish a provisional model / keep the model restricted / share with regional reviewers.",
      "consequence": "Truth becomes actionable but remains incomplete; prevents a premature claim that one villain explains all harm.",
      "rewardIntent": "ENM-033 knowledge advantage; evidence integrity flag.",
      "regionIntent": "REG-006",
      "choiceIsExplicit": true,
      "rewardValues": "Exact numeric amounts and item grant IDs must be reconciled against progression/economy balance before implementation; do not infer free rewards.",
      "failurePolicy": "Quest-specific partial failure changes cost, time, faction/relationship flags or encounter state; no optional quest can hard-lock the main story.",
      "dialogueKeyPrefix": "DLG_Q37",
      "regionIds": [
        "REG-006"
      ],
      "prerequisiteQuestIds": [
        "Q36"
      ],
      "encounterIds": [],
      "dialogueKeys": [
        "DLG_Q37.intro",
        "DLG_Q37.choice",
        "DLG_Q37.resolution"
      ],
      "implementationNote": "Choice flags and reward IDs must be persisted idempotently; use the documented exitFlag as the canonical completion signal."
    },
    {
      "id": "Q38",
      "act": "ACT-04",
      "title": "The Network Under Fire",
      "objective": "Defend multiple objectives; prior regional preparation changes support.",
      "exitFlag": "ACT4_NETWORK_SURVIVED",
      "sequence": 38,
      "optional": false,
      "objectiveSteps": "Defend network objectives across multiple fronts.",
      "keyChoice": "Protect the hub / protect partner routes / split forces based on delegate readiness.",
      "consequence": "At least one cost is incurred; prior regional preparation changes casualties, resource loss and coalition readiness.",
      "rewardIntent": "RES-005 or RES-006 based on outcome; network survives in changed form.",
      "regionIntent": "REG-005/006",
      "choiceIsExplicit": true,
      "rewardValues": "Exact numeric amounts and item grant IDs must be reconciled against progression/economy balance before implementation; do not infer free rewards.",
      "failurePolicy": "Quest-specific partial failure changes cost, time, faction/relationship flags or encounter state; no optional quest can hard-lock the main story.",
      "dialogueKeyPrefix": "DLG_Q38",
      "regionIds": [
        "REG-005",
        "REG-006"
      ],
      "prerequisiteQuestIds": [
        "Q37"
      ],
      "encounterIds": [
        "BOS-006"
      ],
      "dialogueKeys": [
        "DLG_Q38.intro",
        "DLG_Q38.choice",
        "DLG_Q38.resolution"
      ],
      "implementationNote": "Choice flags and reward IDs must be persisted idempotently; use the documented exitFlag as the canonical completion signal."
    },
    {
      "id": "Q39",
      "act": "ACT-05",
      "title": "The Promise Alya Buried",
      "objective": "Reconstruct Alya's prior failure from evidence and testimony.",
      "exitFlag": "ACT5_ALYA_PAST_REVEALED",
      "sequence": 39,
      "optional": false,
      "objectiveSteps": "Reconstruct Alya's prior failure through evidence and survivor testimony.",
      "keyChoice": "Accept institutional account / accept survivor account / publish conflicting evidence and uncertainty.",
      "consequence": "Reveals Alya's responsibility without reducing the past to one scapegoat.",
      "rewardIntent": "ALLY arc support flags; evidence integrity.",
      "regionIntent": "REG-006",
      "choiceIsExplicit": true,
      "rewardValues": "Exact numeric amounts and item grant IDs must be reconciled against progression/economy balance before implementation; do not infer free rewards.",
      "failurePolicy": "Quest-specific partial failure changes cost, time, faction/relationship flags or encounter state; no optional quest can hard-lock the main story.",
      "dialogueKeyPrefix": "DLG_Q39",
      "regionIds": [
        "REG-006"
      ],
      "prerequisiteQuestIds": [
        "Q38"
      ],
      "encounterIds": [],
      "dialogueKeys": [
        "DLG_Q39.intro",
        "DLG_Q39.choice",
        "DLG_Q39.resolution"
      ],
      "implementationNote": "Choice flags and reward IDs must be persisted idempotently; use the documented exitFlag as the canonical completion signal."
    },
    {
      "id": "Q40",
      "act": "ACT-05",
      "title": "The Personification",
      "objective": "Confront the Ferida Manipulator's interpretation of the wound.",
      "exitFlag": "ACT5_ANTAGONIST_REVEALED",
      "sequence": 40,
      "optional": false,
      "objectiveSteps": "Hear the Ferida Manipulator's case and test its claims against evidence.",
      "keyChoice": "Reject the framing / challenge specific claims / offer a conditional alternative before combat.",
      "consequence": "Dialogue changes initial phase modifiers, not the existence of the boss encounter.",
      "rewardIntent": "BOS-008 encounter modifier; RES-007.",
      "regionIntent": "REG-006/007",
      "choiceIsExplicit": true,
      "rewardValues": "Exact numeric amounts and item grant IDs must be reconciled against progression/economy balance before implementation; do not infer free rewards.",
      "failurePolicy": "Quest-specific partial failure changes cost, time, faction/relationship flags or encounter state; no optional quest can hard-lock the main story.",
      "dialogueKeyPrefix": "DLG_Q40",
      "regionIds": [
        "REG-006",
        "REG-007"
      ],
      "prerequisiteQuestIds": [
        "Q39"
      ],
      "encounterIds": [
        "BOS-008"
      ],
      "dialogueKeys": [
        "DLG_Q40.intro",
        "DLG_Q40.choice",
        "DLG_Q40.resolution"
      ],
      "implementationNote": "Choice flags and reward IDs must be persisted idempotently; use the documented exitFlag as the canonical completion signal."
    },
    {
      "id": "Q41",
      "act": "ACT-05",
      "title": "The Coalition's Terms",
      "objective": "Negotiate a final coalition with explicit costs and local authority.",
      "exitFlag": "ACT5_COALITION_READY",
      "sequence": 41,
      "optional": false,
      "objectiveSteps": "Negotiate final coalition obligations, limits and local decision rights.",
      "keyChoice": "Central command / distributed command with shared signals / loose emergency pact.",
      "consequence": "Coalition readiness is derived from explicit commitments and preparation, not one reputation score.",
      "rewardIntent": "RES-008 agreements; coalition state.",
      "regionIntent": "REG-007 access gate",
      "choiceIsExplicit": true,
      "rewardValues": "Exact numeric amounts and item grant IDs must be reconciled against progression/economy balance before implementation; do not infer free rewards.",
      "failurePolicy": "Quest-specific partial failure changes cost, time, faction/relationship flags or encounter state; no optional quest can hard-lock the main story.",
      "dialogueKeyPrefix": "DLG_Q41",
      "regionIds": [
        "REG-003",
        "REG-004",
        "REG-005"
      ],
      "prerequisiteQuestIds": [
        "Q40"
      ],
      "encounterIds": [],
      "dialogueKeys": [
        "DLG_Q41.intro",
        "DLG_Q41.choice",
        "DLG_Q41.resolution"
      ],
      "implementationNote": "Choice flags and reward IDs must be persisted idempotently; use the documented exitFlag as the canonical completion signal."
    },
    {
      "id": "Q42",
      "act": "ACT-05",
      "title": "A Road Without a Hero",
      "objective": "Assign final responsibilities to allies, delegates and regions.",
      "exitFlag": "ACT5_RESPONSIBILITIES_DISTRIBUTED",
      "sequence": 42,
      "optional": false,
      "objectiveSteps": "Assign final responsibilities to allies, delegates and regional leaders.",
      "keyChoice": "Optimize for strength / balance aptitude and relationships / prioritize local ownership.",
      "consequence": "Creates final encounter support packages; no single ally is mandatory.",
      "rewardIntent": "Ally epilogue flags; encounter support.",
      "regionIntent": "REG-007",
      "choiceIsExplicit": true,
      "rewardValues": "Exact numeric amounts and item grant IDs must be reconciled against progression/economy balance before implementation; do not infer free rewards.",
      "failurePolicy": "Quest-specific partial failure changes cost, time, faction/relationship flags or encounter state; no optional quest can hard-lock the main story.",
      "dialogueKeyPrefix": "DLG_Q42",
      "regionIds": [
        "REG-007"
      ],
      "prerequisiteQuestIds": [
        "Q41"
      ],
      "encounterIds": [],
      "dialogueKeys": [
        "DLG_Q42.intro",
        "DLG_Q42.choice",
        "DLG_Q42.resolution"
      ],
      "implementationNote": "Choice flags and reward IDs must be persisted idempotently; use the documented exitFlag as the canonical completion signal."
    },
    {
      "id": "Q43",
      "act": "ACT-05",
      "title": "Into the Confluence",
      "objective": "Reach the final region; optional paths affect support, not access.",
      "exitFlag": "ACT5_CONFLUENCE_ENTERED",
      "sequence": 43,
      "optional": false,
      "objectiveSteps": "Reach the Confluence and choose optional approach preparations.",
      "keyChoice": "Research route / stewardship route / direct route.",
      "consequence": "Optional route changes starting resources and phase pressure; does not gate access once Q41 is complete.",
      "rewardIntent": "ITM-032 or RES-007 depending route.",
      "regionIntent": "REG-007",
      "choiceIsExplicit": true,
      "rewardValues": "Exact numeric amounts and item grant IDs must be reconciled against progression/economy balance before implementation; do not infer free rewards.",
      "failurePolicy": "Quest-specific partial failure changes cost, time, faction/relationship flags or encounter state; no optional quest can hard-lock the main story.",
      "dialogueKeyPrefix": "DLG_Q43",
      "regionIds": [
        "REG-007"
      ],
      "prerequisiteQuestIds": [
        "Q42"
      ],
      "encounterIds": [],
      "dialogueKeys": [
        "DLG_Q43.intro",
        "DLG_Q43.choice",
        "DLG_Q43.resolution"
      ],
      "implementationNote": "Choice flags and reward IDs must be persisted idempotently; use the documented exitFlag as the canonical completion signal."
    },
    {
      "id": "Q44",
      "act": "ACT-05",
      "title": "The Wound's Heart",
      "objective": "Disrupt the manifestation's anchors in the first final phase.",
      "exitFlag": "ACT5_FINAL_ANCHORS_DISRUPTED",
      "sequence": 44,
      "optional": false,
      "objectiveSteps": "Disrupt the first set of Ferida anchors while keeping the party stable.",
      "keyChoice": "Assign anchors to prepared allies / use research advantage / use community support.",
      "consequence": "First phase requires objective progress; Vitality defeat alone cannot resolve it.",
      "rewardIntent": "BOS-009 phase transition; coalition link state.",
      "regionIntent": "REG-007",
      "choiceIsExplicit": true,
      "rewardValues": "Exact numeric amounts and item grant IDs must be reconciled against progression/economy balance before implementation; do not infer free rewards.",
      "failurePolicy": "Quest-specific partial failure changes cost, time, faction/relationship flags or encounter state; no optional quest can hard-lock the main story.",
      "dialogueKeyPrefix": "DLG_Q44",
      "regionIds": [
        "REG-007"
      ],
      "prerequisiteQuestIds": [
        "Q43"
      ],
      "encounterIds": [
        "BOS-009"
      ],
      "dialogueKeys": [
        "DLG_Q44.intro",
        "DLG_Q44.choice",
        "DLG_Q44.resolution"
      ],
      "implementationNote": "Choice flags and reward IDs must be persisted idempotently; use the documented exitFlag as the canonical completion signal."
    },
    {
      "id": "Q45",
      "act": "ACT-05",
      "title": "The Last Pattern",
      "objective": "Maintain coalition links and stop the feedback loop.",
      "exitFlag": "ACT5_FINAL_OBJECTIVE_RESOLVED",
      "sequence": 45,
      "optional": false,
      "objectiveSteps": "Complete the final objective while maintaining coalition links and interrupting the feedback loop.",
      "keyChoice": "Preserve all links at higher resource cost / sacrifice one link to protect another / distribute risk across prepared regions.",
      "consequence": "Sets final world-state resolution; no route guarantees permanent eradication.",
      "rewardIntent": "ACT5_FINAL_OBJECTIVE_RESOLVED; ending inputs committed.",
      "regionIntent": "REG-007",
      "choiceIsExplicit": true,
      "rewardValues": "Exact numeric amounts and item grant IDs must be reconciled against progression/economy balance before implementation; do not infer free rewards.",
      "failurePolicy": "Quest-specific partial failure changes cost, time, faction/relationship flags or encounter state; no optional quest can hard-lock the main story.",
      "dialogueKeyPrefix": "DLG_Q45",
      "regionIds": [
        "REG-007"
      ],
      "prerequisiteQuestIds": [
        "Q44"
      ],
      "encounterIds": [
        "BOS-009"
      ],
      "dialogueKeys": [
        "DLG_Q45.intro",
        "DLG_Q45.choice",
        "DLG_Q45.resolution"
      ],
      "implementationNote": "Choice flags and reward IDs must be persisted idempotently; use the documented exitFlag as the canonical completion signal."
    },
    {
      "id": "Q46",
      "act": "ACT-05",
      "title": "What We Leave Running",
      "objective": "Choose which structures are preserved, reformed, decentralized or retired.",
      "exitFlag": "ACT5_WORLD_STATE_CHOSEN",
      "sequence": 46,
      "optional": false,
      "objectiveSteps": "Choose which structures to preserve, reform, decentralize or retire.",
      "keyChoice": "Preserve Organization / reform Organization / retire selected centralized structures.",
      "consequence": "Locks ending family inputs; no exact ending percentage is shown.",
      "rewardIntent": "ACT5_WORLD_STATE_CHOSEN.",
      "regionIntent": "REG-007",
      "choiceIsExplicit": true,
      "rewardValues": "Exact numeric amounts and item grant IDs must be reconciled against progression/economy balance before implementation; do not infer free rewards.",
      "failurePolicy": "Quest-specific partial failure changes cost, time, faction/relationship flags or encounter state; no optional quest can hard-lock the main story.",
      "dialogueKeyPrefix": "DLG_Q46",
      "regionIds": [
        "REG-007"
      ],
      "prerequisiteQuestIds": [
        "Q45"
      ],
      "encounterIds": [],
      "dialogueKeys": [
        "DLG_Q46.intro",
        "DLG_Q46.choice",
        "DLG_Q46.resolution"
      ],
      "implementationNote": "Choice flags and reward IDs must be persisted idempotently; use the documented exitFlag as the canonical completion signal."
    },
    {
      "id": "Q47",
      "act": "ACT-05",
      "title": "A Future Without a Center",
      "objective": "Resolve ending family and character epilogues.",
      "exitFlag": "GAME_COMPLETED",
      "sequence": 47,
      "optional": false,
      "objectiveSteps": "Resolve ally, faction and regional epilogues from accumulated states.",
      "keyChoice": "No final binary moral choice; player confirms the future direction already built.",
      "consequence": "Writes the ending family and epilogue flags; save becomes completed-game state.",
      "rewardIntent": "GAME_COMPLETED; replay/continue policy handled by persistence spec.",
      "regionIntent": "REG-007",
      "choiceIsExplicit": true,
      "rewardValues": "Exact numeric amounts and item grant IDs must be reconciled against progression/economy balance before implementation; do not infer free rewards.",
      "failurePolicy": "Quest-specific partial failure changes cost, time, faction/relationship flags or encounter state; no optional quest can hard-lock the main story.",
      "dialogueKeyPrefix": "DLG_Q47",
      "regionIds": [
        "REG-007"
      ],
      "prerequisiteQuestIds": [
        "Q46"
      ],
      "encounterIds": [],
      "dialogueKeys": [
        "DLG_Q47.intro",
        "DLG_Q47.choice",
        "DLG_Q47.resolution"
      ],
      "implementationNote": "Choice flags and reward IDs must be persisted idempotently; use the documented exitFlag as the canonical completion signal."
    }
  ],
  "sidequests": [
    {
      "id": "SQ-001",
      "act": "ACT-01",
      "title": "A Bowl Kept Warm",
      "optional": true,
      "designRule": "Reward knowledge, resources, relationship, faction state, or encounter preparation; never gate the main ending.",
      "objective": "Resolve a food-sharing dispute and record the residents' temporary agreement.",
      "rewardIntent": "Morale flag and resident support.",
      "choice": {
        "prompt": "Choose a response that makes the trade-off explicit; exact labels belong to the authored dialogue pack.",
        "outcomeRule": "Choices update only the named quest, relationship, resource, faction or preparation flags."
      },
      "failurePolicy": "Can be declined or left incomplete; no main quest or ending is blocked.",
      "dialogueKeyPrefix": "DLG_SQ-001",
      "assetNeed": "Reusable location/NPC presentation unless the asset registry proves a dedicated visual is required.",
      "regionIds": [
        "REG-001"
      ],
      "prerequisiteQuestIds": [
        "Q01"
      ],
      "dialogueKeys": [
        "DLG_SQ-001.intro",
        "DLG_SQ-001.choice",
        "DLG_SQ-001.resolution"
      ]
    },
    {
      "id": "SQ-002",
      "act": "ACT-01",
      "title": "The Missing Filter",
      "optional": true,
      "designRule": "Reward knowledge, resources, relationship, faction state, or encounter preparation; never gate the main ending.",
      "objective": "Find the missing filter and establish whether it was lost, stolen or misallocated.",
      "rewardIntent": "Reduce one Q07 preparation cost.",
      "choice": {
        "prompt": "Choose a response that makes the trade-off explicit; exact labels belong to the authored dialogue pack.",
        "outcomeRule": "Choices update only the named quest, relationship, resource, faction or preparation flags."
      },
      "failurePolicy": "Can be declined or left incomplete; no main quest or ending is blocked.",
      "dialogueKeyPrefix": "DLG_SQ-002",
      "assetNeed": "Reusable location/NPC presentation unless the asset registry proves a dedicated visual is required.",
      "regionIds": [
        "REG-001"
      ],
      "prerequisiteQuestIds": [
        "Q01"
      ],
      "dialogueKeys": [
        "DLG_SQ-002.intro",
        "DLG_SQ-002.choice",
        "DLG_SQ-002.resolution"
      ]
    },
    {
      "id": "SQ-003",
      "act": "ACT-01",
      "title": "The Quiet Room",
      "optional": true,
      "designRule": "Reward knowledge, resources, relationship, faction state, or encounter preparation; never gate the main ending.",
      "objective": "Create a voluntary recovery space with clear access and privacy rules.",
      "rewardIntent": "Care-route support and recovery modifier.",
      "choice": {
        "prompt": "Choose a response that makes the trade-off explicit; exact labels belong to the authored dialogue pack.",
        "outcomeRule": "Choices update only the named quest, relationship, resource, faction or preparation flags."
      },
      "failurePolicy": "Can be declined or left incomplete; no main quest or ending is blocked.",
      "dialogueKeyPrefix": "DLG_SQ-003",
      "assetNeed": "Reusable location/NPC presentation unless the asset registry proves a dedicated visual is required.",
      "regionIds": [
        "REG-001"
      ],
      "prerequisiteQuestIds": [
        "Q01"
      ],
      "dialogueKeys": [
        "DLG_SQ-003.intro",
        "DLG_SQ-003.choice",
        "DLG_SQ-003.resolution"
      ]
    },
    {
      "id": "SQ-004",
      "act": "ACT-01",
      "title": "A Map in the Rafters",
      "optional": true,
      "designRule": "Reward knowledge, resources, relationship, faction state, or encounter preparation; never gate the main ending.",
      "objective": "Recover a map hidden in the rafters and compare it to the current route.",
      "rewardIntent": "Safe route knowledge for an Expedition.",
      "choice": {
        "prompt": "Choose a response that makes the trade-off explicit; exact labels belong to the authored dialogue pack.",
        "outcomeRule": "Choices update only the named quest, relationship, resource, faction or preparation flags."
      },
      "failurePolicy": "Can be declined or left incomplete; no main quest or ending is blocked.",
      "dialogueKeyPrefix": "DLG_SQ-004",
      "assetNeed": "Reusable location/NPC presentation unless the asset registry proves a dedicated visual is required.",
      "regionIds": [
        "REG-001"
      ],
      "prerequisiteQuestIds": [
        "Q01"
      ],
      "dialogueKeys": [
        "DLG_SQ-004.intro",
        "DLG_SQ-004.choice",
        "DLG_SQ-004.resolution"
      ]
    },
    {
      "id": "SQ-005",
      "act": "ACT-01",
      "title": "Mara's Ledger",
      "optional": true,
      "designRule": "Reward knowledge, resources, relationship, faction state, or encounter preparation; never gate the main ending.",
      "objective": "Reconstruct water allocation records without treating Mara as the sole cause.",
      "rewardIntent": "Local trust and evidence-integrity flag.",
      "choice": {
        "prompt": "Choose a response that makes the trade-off explicit; exact labels belong to the authored dialogue pack.",
        "outcomeRule": "Choices update only the named quest, relationship, resource, faction or preparation flags."
      },
      "failurePolicy": "Can be declined or left incomplete; no main quest or ending is blocked.",
      "dialogueKeyPrefix": "DLG_SQ-005",
      "assetNeed": "Reusable location/NPC presentation unless the asset registry proves a dedicated visual is required.",
      "regionIds": [
        "REG-001"
      ],
      "prerequisiteQuestIds": [
        "Q01"
      ],
      "dialogueKeys": [
        "DLG_SQ-005.intro",
        "DLG_SQ-005.choice",
        "DLG_SQ-005.resolution"
      ]
    },
    {
      "id": "SQ-006",
      "act": "ACT-02",
      "title": "The Unclaimed Bed",
      "optional": true,
      "designRule": "Reward knowledge, resources, relationship, faction state, or encounter preparation; never gate the main ending.",
      "objective": "Decide how beds are assigned when refuge capacity is insufficient.",
      "rewardIntent": "Representation and housing policy flag.",
      "choice": {
        "prompt": "Choose a response that makes the trade-off explicit; exact labels belong to the authored dialogue pack.",
        "outcomeRule": "Choices update only the named quest, relationship, resource, faction or preparation flags."
      },
      "failurePolicy": "Can be declined or left incomplete; no main quest or ending is blocked.",
      "dialogueKeyPrefix": "DLG_SQ-006",
      "assetNeed": "Reusable location/NPC presentation unless the asset registry proves a dedicated visual is required.",
      "regionIds": [
        "REG-002"
      ],
      "prerequisiteQuestIds": [
        "Q12"
      ],
      "dialogueKeys": [
        "DLG_SQ-006.intro",
        "DLG_SQ-006.choice",
        "DLG_SQ-006.resolution"
      ]
    },
    {
      "id": "SQ-007",
      "act": "ACT-02",
      "title": "A Tool for Every Hand",
      "optional": true,
      "designRule": "Reward knowledge, resources, relationship, faction state, or encounter preparation; never gate the main ending.",
      "objective": "Test a repair design and choose between speed and maintainability.",
      "rewardIntent": "Workshop recipe or repair discount.",
      "choice": {
        "prompt": "Choose a response that makes the trade-off explicit; exact labels belong to the authored dialogue pack.",
        "outcomeRule": "Choices update only the named quest, relationship, resource, faction or preparation flags."
      },
      "failurePolicy": "Can be declined or left incomplete; no main quest or ending is blocked.",
      "dialogueKeyPrefix": "DLG_SQ-007",
      "assetNeed": "Reusable location/NPC presentation unless the asset registry proves a dedicated visual is required.",
      "regionIds": [
        "REG-002"
      ],
      "prerequisiteQuestIds": [
        "Q12"
      ],
      "dialogueKeys": [
        "DLG_SQ-007.intro",
        "DLG_SQ-007.choice",
        "DLG_SQ-007.resolution"
      ]
    },
    {
      "id": "SQ-008",
      "act": "ACT-02",
      "title": "The Unfinished Lesson",
      "optional": true,
      "designRule": "Reward knowledge, resources, relationship, faction state, or encounter preparation; never gate the main ending.",
      "objective": "Help Guardiã and Rival agree on training and accountability rules.",
      "rewardIntent": "Relationship scene and Training Yard modifier.",
      "choice": {
        "prompt": "Choose a response that makes the trade-off explicit; exact labels belong to the authored dialogue pack.",
        "outcomeRule": "Choices update only the named quest, relationship, resource, faction or preparation flags."
      },
      "failurePolicy": "Can be declined or left incomplete; no main quest or ending is blocked.",
      "dialogueKeyPrefix": "DLG_SQ-008",
      "assetNeed": "Reusable location/NPC presentation unless the asset registry proves a dedicated visual is required.",
      "regionIds": [
        "REG-002"
      ],
      "prerequisiteQuestIds": [
        "Q12"
      ],
      "dialogueKeys": [
        "DLG_SQ-008.intro",
        "DLG_SQ-008.choice",
        "DLG_SQ-008.resolution"
      ]
    },
    {
      "id": "SQ-009",
      "act": "ACT-02",
      "title": "A Contract in Ink",
      "optional": true,
      "designRule": "Reward knowledge, resources, relationship, faction state, or encounter preparation; never gate the main ending.",
      "objective": "Identify an unfair clause and negotiate an enforceable revision.",
      "rewardIntent": "Trade contract reliability.",
      "choice": {
        "prompt": "Choose a response that makes the trade-off explicit; exact labels belong to the authored dialogue pack.",
        "outcomeRule": "Choices update only the named quest, relationship, resource, faction or preparation flags."
      },
      "failurePolicy": "Can be declined or left incomplete; no main quest or ending is blocked.",
      "dialogueKeyPrefix": "DLG_SQ-009",
      "assetNeed": "Reusable location/NPC presentation unless the asset registry proves a dedicated visual is required.",
      "regionIds": [
        "REG-002"
      ],
      "prerequisiteQuestIds": [
        "Q12"
      ],
      "dialogueKeys": [
        "DLG_SQ-009.intro",
        "DLG_SQ-009.choice",
        "DLG_SQ-009.resolution"
      ]
    },
    {
      "id": "SQ-010",
      "act": "ACT-02",
      "title": "The Names We Keep",
      "optional": true,
      "designRule": "Reward knowledge, resources, relationship, faction state, or encounter preparation; never gate the main ending.",
      "objective": "Create a resident record with consent, access limits and correction rights.",
      "rewardIntent": "Community Hall governance modifier.",
      "choice": {
        "prompt": "Choose a response that makes the trade-off explicit; exact labels belong to the authored dialogue pack.",
        "outcomeRule": "Choices update only the named quest, relationship, resource, faction or preparation flags."
      },
      "failurePolicy": "Can be declined or left incomplete; no main quest or ending is blocked.",
      "dialogueKeyPrefix": "DLG_SQ-010",
      "assetNeed": "Reusable location/NPC presentation unless the asset registry proves a dedicated visual is required.",
      "regionIds": [
        "REG-002"
      ],
      "prerequisiteQuestIds": [
        "Q12"
      ],
      "dialogueKeys": [
        "DLG_SQ-010.intro",
        "DLG_SQ-010.choice",
        "DLG_SQ-010.resolution"
      ]
    },
    {
      "id": "SQ-011",
      "act": "ACT-03",
      "title": "Salt on the Road",
      "optional": true,
      "designRule": "Reward knowledge, resources, relationship, faction state, or encounter preparation; never gate the main ending.",
      "objective": "During a salt storm, choose cargo protection, rescue or split resources.",
      "rewardIntent": "Trade reputation or safe-passage support.",
      "choice": {
        "prompt": "Choose a response that makes the trade-off explicit; exact labels belong to the authored dialogue pack.",
        "outcomeRule": "Choices update only the named quest, relationship, resource, faction or preparation flags."
      },
      "failurePolicy": "Can be declined or left incomplete; no main quest or ending is blocked.",
      "dialogueKeyPrefix": "DLG_SQ-011",
      "assetNeed": "Reusable location/NPC presentation unless the asset registry proves a dedicated visual is required.",
      "regionIds": [
        "REG-003",
        "REG-004"
      ],
      "prerequisiteQuestIds": [
        "Q21"
      ],
      "dialogueKeys": [
        "DLG_SQ-011.intro",
        "DLG_SQ-011.choice",
        "DLG_SQ-011.resolution"
      ]
    },
    {
      "id": "SQ-012",
      "act": "ACT-03",
      "title": "The Root That Remembers",
      "optional": true,
      "designRule": "Reward knowledge, resources, relationship, faction state, or encounter preparation; never gate the main ending.",
      "objective": "Negotiate what the Mycelian memory network may share and retain.",
      "rewardIntent": "Research Notes and knowledge-consent state.",
      "choice": {
        "prompt": "Choose a response that makes the trade-off explicit; exact labels belong to the authored dialogue pack.",
        "outcomeRule": "Choices update only the named quest, relationship, resource, faction or preparation flags."
      },
      "failurePolicy": "Can be declined or left incomplete; no main quest or ending is blocked.",
      "dialogueKeyPrefix": "DLG_SQ-012",
      "assetNeed": "Reusable location/NPC presentation unless the asset registry proves a dedicated visual is required.",
      "regionIds": [
        "REG-003",
        "REG-004"
      ],
      "prerequisiteQuestIds": [
        "Q21"
      ],
      "dialogueKeys": [
        "DLG_SQ-012.intro",
        "DLG_SQ-012.choice",
        "DLG_SQ-012.resolution"
      ]
    },
    {
      "id": "SQ-013",
      "act": "ACT-03",
      "title": "A Debt with No Owner",
      "optional": true,
      "designRule": "Reward knowledge, resources, relationship, faction state, or encounter preparation; never gate the main ending.",
      "objective": "Resolve an inherited debt without punishing people who did not incur it.",
      "rewardIntent": "Faction agreement and a modest trade reward.",
      "choice": {
        "prompt": "Choose a response that makes the trade-off explicit; exact labels belong to the authored dialogue pack.",
        "outcomeRule": "Choices update only the named quest, relationship, resource, faction or preparation flags."
      },
      "failurePolicy": "Can be declined or left incomplete; no main quest or ending is blocked.",
      "dialogueKeyPrefix": "DLG_SQ-013",
      "assetNeed": "Reusable location/NPC presentation unless the asset registry proves a dedicated visual is required.",
      "regionIds": [
        "REG-003",
        "REG-004"
      ],
      "prerequisiteQuestIds": [
        "Q21"
      ],
      "dialogueKeys": [
        "DLG_SQ-013.intro",
        "DLG_SQ-013.choice",
        "DLG_SQ-013.resolution"
      ]
    },
    {
      "id": "SQ-014",
      "act": "ACT-03",
      "title": "The Broken Bell",
      "optional": true,
      "designRule": "Reward knowledge, resources, relationship, faction state, or encounter preparation; never gate the main ending.",
      "objective": "Restore a warning bell and create a second independent signal.",
      "rewardIntent": "Regional warning redundancy.",
      "choice": {
        "prompt": "Choose a response that makes the trade-off explicit; exact labels belong to the authored dialogue pack.",
        "outcomeRule": "Choices update only the named quest, relationship, resource, faction or preparation flags."
      },
      "failurePolicy": "Can be declined or left incomplete; no main quest or ending is blocked.",
      "dialogueKeyPrefix": "DLG_SQ-014",
      "assetNeed": "Reusable location/NPC presentation unless the asset registry proves a dedicated visual is required.",
      "regionIds": [
        "REG-003",
        "REG-004"
      ],
      "prerequisiteQuestIds": [
        "Q21"
      ],
      "dialogueKeys": [
        "DLG_SQ-014.intro",
        "DLG_SQ-014.choice",
        "DLG_SQ-014.resolution"
      ]
    },
    {
      "id": "SQ-015",
      "act": "ACT-03",
      "title": "The Price of Quiet",
      "optional": true,
      "designRule": "Reward knowledge, resources, relationship, faction state, or encounter preparation; never gate the main ending.",
      "objective": "Counter a rumor campaign without suppressing legitimate dissent.",
      "rewardIntent": "Evidence integrity and faction credibility.",
      "choice": {
        "prompt": "Choose a response that makes the trade-off explicit; exact labels belong to the authored dialogue pack.",
        "outcomeRule": "Choices update only the named quest, relationship, resource, faction or preparation flags."
      },
      "failurePolicy": "Can be declined or left incomplete; no main quest or ending is blocked.",
      "dialogueKeyPrefix": "DLG_SQ-015",
      "assetNeed": "Reusable location/NPC presentation unless the asset registry proves a dedicated visual is required.",
      "regionIds": [
        "REG-003",
        "REG-004"
      ],
      "prerequisiteQuestIds": [
        "Q21"
      ],
      "dialogueKeys": [
        "DLG_SQ-015.intro",
        "DLG_SQ-015.choice",
        "DLG_SQ-015.resolution"
      ]
    },
    {
      "id": "SQ-016",
      "act": "ACT-04",
      "title": "Ashes in the Clinic",
      "optional": true,
      "designRule": "Reward knowledge, resources, relationship, faction state, or encounter preparation; never gate the main ending.",
      "objective": "Allocate scarce treatment and establish a reviewable clinic policy.",
      "rewardIntent": "Care support and a future encounter modifier.",
      "choice": {
        "prompt": "Choose a response that makes the trade-off explicit; exact labels belong to the authored dialogue pack.",
        "outcomeRule": "Choices update only the named quest, relationship, resource, faction or preparation flags."
      },
      "failurePolicy": "Can be declined or left incomplete; no main quest or ending is blocked.",
      "dialogueKeyPrefix": "DLG_SQ-016",
      "assetNeed": "Reusable location/NPC presentation unless the asset registry proves a dedicated visual is required.",
      "regionIds": [
        "REG-005",
        "REG-006"
      ],
      "prerequisiteQuestIds": [
        "Q30"
      ],
      "dialogueKeys": [
        "DLG_SQ-016.intro",
        "DLG_SQ-016.choice",
        "DLG_SQ-016.resolution"
      ]
    },
    {
      "id": "SQ-017",
      "act": "ACT-04",
      "title": "The Route Nobody Owns",
      "optional": true,
      "designRule": "Reward knowledge, resources, relationship, faction state, or encounter preparation; never gate the main ending.",
      "objective": "Restore a route with a shared maintenance plan instead of one owner.",
      "rewardIntent": "Travel risk reduction.",
      "choice": {
        "prompt": "Choose a response that makes the trade-off explicit; exact labels belong to the authored dialogue pack.",
        "outcomeRule": "Choices update only the named quest, relationship, resource, faction or preparation flags."
      },
      "failurePolicy": "Can be declined or left incomplete; no main quest or ending is blocked.",
      "dialogueKeyPrefix": "DLG_SQ-017",
      "assetNeed": "Reusable location/NPC presentation unless the asset registry proves a dedicated visual is required.",
      "regionIds": [
        "REG-005",
        "REG-006"
      ],
      "prerequisiteQuestIds": [
        "Q30"
      ],
      "dialogueKeys": [
        "DLG_SQ-017.intro",
        "DLG_SQ-017.choice",
        "DLG_SQ-017.resolution"
      ]
    },
    {
      "id": "SQ-018",
      "act": "ACT-04",
      "title": "The False Witness",
      "optional": true,
      "designRule": "Reward knowledge, resources, relationship, faction state, or encounter preparation; never gate the main ending.",
      "objective": "Collect independent evidence before accusing an ally or faction.",
      "rewardIntent": "Evidence integrity; prevent an avoidable relationship penalty.",
      "choice": {
        "prompt": "Choose a response that makes the trade-off explicit; exact labels belong to the authored dialogue pack.",
        "outcomeRule": "Choices update only the named quest, relationship, resource, faction or preparation flags."
      },
      "failurePolicy": "Can be declined or left incomplete; no main quest or ending is blocked.",
      "dialogueKeyPrefix": "DLG_SQ-018",
      "assetNeed": "Reusable location/NPC presentation unless the asset registry proves a dedicated visual is required.",
      "regionIds": [
        "REG-005",
        "REG-006"
      ],
      "prerequisiteQuestIds": [
        "Q30"
      ],
      "dialogueKeys": [
        "DLG_SQ-018.intro",
        "DLG_SQ-018.choice",
        "DLG_SQ-018.resolution"
      ]
    },
    {
      "id": "SQ-019",
      "act": "ACT-04",
      "title": "A Seat Left Empty",
      "optional": true,
      "designRule": "Reward knowledge, resources, relationship, faction state, or encounter preparation; never gate the main ending.",
      "objective": "Respond to a delegate's resignation without coercing their return.",
      "rewardIntent": "Representation quality and a new delegate candidate.",
      "choice": {
        "prompt": "Choose a response that makes the trade-off explicit; exact labels belong to the authored dialogue pack.",
        "outcomeRule": "Choices update only the named quest, relationship, resource, faction or preparation flags."
      },
      "failurePolicy": "Can be declined or left incomplete; no main quest or ending is blocked.",
      "dialogueKeyPrefix": "DLG_SQ-019",
      "assetNeed": "Reusable location/NPC presentation unless the asset registry proves a dedicated visual is required.",
      "regionIds": [
        "REG-005",
        "REG-006"
      ],
      "prerequisiteQuestIds": [
        "Q30"
      ],
      "dialogueKeys": [
        "DLG_SQ-019.intro",
        "DLG_SQ-019.choice",
        "DLG_SQ-019.resolution"
      ]
    },
    {
      "id": "SQ-020",
      "act": "ACT-04",
      "title": "The Last Workshop Shift",
      "optional": true,
      "designRule": "Reward knowledge, resources, relationship, faction state, or encounter preparation; never gate the main ending.",
      "objective": "Choose between saving a workshop and evacuating its workers under time pressure.",
      "rewardIntent": "Salvage or resident-safety state; one cost is unavoidable.",
      "choice": {
        "prompt": "Choose a response that makes the trade-off explicit; exact labels belong to the authored dialogue pack.",
        "outcomeRule": "Choices update only the named quest, relationship, resource, faction or preparation flags."
      },
      "failurePolicy": "Can be declined or left incomplete; no main quest or ending is blocked.",
      "dialogueKeyPrefix": "DLG_SQ-020",
      "assetNeed": "Reusable location/NPC presentation unless the asset registry proves a dedicated visual is required.",
      "regionIds": [
        "REG-005",
        "REG-006"
      ],
      "prerequisiteQuestIds": [
        "Q30"
      ],
      "dialogueKeys": [
        "DLG_SQ-020.intro",
        "DLG_SQ-020.choice",
        "DLG_SQ-020.resolution"
      ]
    },
    {
      "id": "SQ-021",
      "act": "ACT-05",
      "title": "The Witnesses' Circle",
      "optional": true,
      "designRule": "Reward knowledge, resources, relationship, faction state, or encounter preparation; never gate the main ending.",
      "objective": "Reconcile conflicting accounts of Alya's past and document uncertainty.",
      "rewardIntent": "Evidence integrity and final dialogue option.",
      "choice": {
        "prompt": "Choose a response that makes the trade-off explicit; exact labels belong to the authored dialogue pack.",
        "outcomeRule": "Choices update only the named quest, relationship, resource, faction or preparation flags."
      },
      "failurePolicy": "Can be declined or left incomplete; no main quest or ending is blocked.",
      "dialogueKeyPrefix": "DLG_SQ-021",
      "assetNeed": "Reusable location/NPC presentation unless the asset registry proves a dedicated visual is required.",
      "regionIds": [
        "REG-006",
        "REG-007"
      ],
      "prerequisiteQuestIds": [
        "Q39"
      ],
      "dialogueKeys": [
        "DLG_SQ-021.intro",
        "DLG_SQ-021.choice",
        "DLG_SQ-021.resolution"
      ]
    },
    {
      "id": "SQ-022",
      "act": "ACT-05",
      "title": "What the Reaper Carries",
      "optional": true,
      "designRule": "Reward knowledge, resources, relationship, faction state, or encounter preparation; never gate the main ending.",
      "objective": "Help a community memorialize loss with a rite chosen by those affected.",
      "rewardIntent": "Morale and Reaper relationship flag.",
      "choice": {
        "prompt": "Choose a response that makes the trade-off explicit; exact labels belong to the authored dialogue pack.",
        "outcomeRule": "Choices update only the named quest, relationship, resource, faction or preparation flags."
      },
      "failurePolicy": "Can be declined or left incomplete; no main quest or ending is blocked.",
      "dialogueKeyPrefix": "DLG_SQ-022",
      "assetNeed": "Reusable location/NPC presentation unless the asset registry proves a dedicated visual is required.",
      "regionIds": [
        "REG-006",
        "REG-007"
      ],
      "prerequisiteQuestIds": [
        "Q39"
      ],
      "dialogueKeys": [
        "DLG_SQ-022.intro",
        "DLG_SQ-022.choice",
        "DLG_SQ-022.resolution"
      ]
    },
    {
      "id": "SQ-023",
      "act": "ACT-05",
      "title": "A Garden Outside the Wall",
      "optional": true,
      "designRule": "Reward knowledge, resources, relationship, faction state, or encounter preparation; never gate the main ending.",
      "objective": "Establish a recovery garden outside the hub and share stewardship.",
      "rewardIntent": "Botanical Extract over time and local cohesion.",
      "choice": {
        "prompt": "Choose a response that makes the trade-off explicit; exact labels belong to the authored dialogue pack.",
        "outcomeRule": "Choices update only the named quest, relationship, resource, faction or preparation flags."
      },
      "failurePolicy": "Can be declined or left incomplete; no main quest or ending is blocked.",
      "dialogueKeyPrefix": "DLG_SQ-023",
      "assetNeed": "Reusable location/NPC presentation unless the asset registry proves a dedicated visual is required.",
      "regionIds": [
        "REG-006",
        "REG-007"
      ],
      "prerequisiteQuestIds": [
        "Q39"
      ],
      "dialogueKeys": [
        "DLG_SQ-023.intro",
        "DLG_SQ-023.choice",
        "DLG_SQ-023.resolution"
      ]
    },
    {
      "id": "SQ-024",
      "act": "ACT-05",
      "title": "The Unbound's Terms",
      "optional": true,
      "designRule": "Reward knowledge, resources, relationship, faction state, or encounter preparation; never gate the main ending.",
      "objective": "Negotiate representation terms for the Unbound, including opt-outs and appeal.",
      "rewardIntent": "Safe-passage and coalition readiness.",
      "choice": {
        "prompt": "Choose a response that makes the trade-off explicit; exact labels belong to the authored dialogue pack.",
        "outcomeRule": "Choices update only the named quest, relationship, resource, faction or preparation flags."
      },
      "failurePolicy": "Can be declined or left incomplete; no main quest or ending is blocked.",
      "dialogueKeyPrefix": "DLG_SQ-024",
      "assetNeed": "Reusable location/NPC presentation unless the asset registry proves a dedicated visual is required.",
      "regionIds": [
        "REG-006",
        "REG-007"
      ],
      "prerequisiteQuestIds": [
        "Q39"
      ],
      "dialogueKeys": [
        "DLG_SQ-024.intro",
        "DLG_SQ-024.choice",
        "DLG_SQ-024.resolution"
      ]
    },
    {
      "id": "SQ-025",
      "act": "ACT-05",
      "title": "A Signal Sent Twice",
      "optional": true,
      "designRule": "Reward knowledge, resources, relationship, faction state, or encounter preparation; never gate the main ending.",
      "objective": "Create redundant coalition communication and test a false-signal drill.",
      "rewardIntent": "Signal Relay readiness and final encounter support.",
      "choice": {
        "prompt": "Choose a response that makes the trade-off explicit; exact labels belong to the authored dialogue pack.",
        "outcomeRule": "Choices update only the named quest, relationship, resource, faction or preparation flags."
      },
      "failurePolicy": "Can be declined or left incomplete; no main quest or ending is blocked.",
      "dialogueKeyPrefix": "DLG_SQ-025",
      "assetNeed": "Reusable location/NPC presentation unless the asset registry proves a dedicated visual is required.",
      "regionIds": [
        "REG-006",
        "REG-007"
      ],
      "prerequisiteQuestIds": [
        "Q39"
      ],
      "dialogueKeys": [
        "DLG_SQ-025.intro",
        "DLG_SQ-025.choice",
        "DLG_SQ-025.resolution"
      ]
    }
  ],
  "expeditions": [
    {
      "id": "EXP-001",
      "title": "Foraging Run",
      "rewards": "Provisions and Botanical Extract",
      "rule": "Weather and aptitude affect yield.",
      "npcOnly": true,
      "assignedAlliesUnavailable": true
    },
    {
      "id": "EXP-002",
      "title": "Timber Survey",
      "rewards": "Timber and Salvage",
      "rule": "Route risk and tool quality affect yield.",
      "npcOnly": true,
      "assignedAlliesUnavailable": true
    },
    {
      "id": "EXP-003",
      "title": "Safe-Road Survey",
      "rewards": "POIs and route knowledge",
      "rule": "Reduces travel uncertainty; does not guarantee safety.",
      "npcOnly": true,
      "assignedAlliesUnavailable": true
    },
    {
      "id": "EXP-004",
      "title": "Resident Escort",
      "rewards": "Trust and safe-passage state",
      "rule": "Can return partial success or delay.",
      "npcOnly": true,
      "assignedAlliesUnavailable": true
    },
    {
      "id": "EXP-005",
      "title": "Research Retrieval",
      "rewards": "Research Notes and samples",
      "rule": "Contamination risk depends on preparation.",
      "npcOnly": true,
      "assignedAlliesUnavailable": true
    },
    {
      "id": "EXP-006",
      "title": "Trade Negotiation",
      "rewards": "Gold and market access",
      "rule": "Requires a negotiator or relevant preparation.",
      "npcOnly": true,
      "assignedAlliesUnavailable": true
    },
    {
      "id": "EXP-007",
      "title": "Emergency Relief",
      "rewards": "Regional stability",
      "rule": "Consumes supplies; can preserve network readiness.",
      "npcOnly": true,
      "assignedAlliesUnavailable": true
    },
    {
      "id": "EXP-008",
      "title": "Signal Relay",
      "rewards": "Coalition communication",
      "rule": "Late-game redundancy and warning coverage.",
      "npcOnly": true,
      "assignedAlliesUnavailable": true
    }
  ],
  "endings": [
    {
      "id": "END-001",
      "title": "The Shared Table",
      "summary": "Strong accountable network; Organization reformed by negotiated oversight.",
      "inputs": [
        "regional_readiness",
        "delegated_responsibility",
        "faction_agreements",
        "evidence_integrity",
        "ally_arcs",
        "care_and_integration_policy",
        "final_choice"
      ],
      "showPercentage": false
    },
    {
      "id": "END-002",
      "title": "The Many Lanterns",
      "summary": "Decentralized resilient regions with weaker central coordination.",
      "inputs": [
        "regional_readiness",
        "delegated_responsibility",
        "faction_agreements",
        "evidence_integrity",
        "ally_arcs",
        "care_and_integration_policy",
        "final_choice"
      ],
      "showPercentage": false
    },
    {
      "id": "END-003",
      "title": "The Necessary Compact",
      "summary": "Centralized coalition with safeguards, appeals and sunset clauses.",
      "inputs": [
        "regional_readiness",
        "delegated_responsibility",
        "faction_agreements",
        "evidence_integrity",
        "ally_arcs",
        "care_and_integration_policy",
        "final_choice"
      ],
      "showPercentage": false
    },
    {
      "id": "END-004",
      "title": "The Quiet Refuge",
      "summary": "Brackenford and several partners endure; world-scale wound remains constrained.",
      "inputs": [
        "regional_readiness",
        "delegated_responsibility",
        "faction_agreements",
        "evidence_integrity",
        "ally_arcs",
        "care_and_integration_policy",
        "final_choice"
      ],
      "showPercentage": false
    },
    {
      "id": "END-005",
      "title": "The Unfinished Road",
      "summary": "Network fractures but avoids total annihilation; recovery remains possible.",
      "inputs": [
        "regional_readiness",
        "delegated_responsibility",
        "faction_agreements",
        "evidence_integrity",
        "ally_arcs",
        "care_and_integration_policy",
        "final_choice"
      ],
      "showPercentage": false
    }
  ]
}
```

## Embedded source: Full-game gameplay catalog

```json
{
  "schemaVersion": 1,
  "status": "CONTENT_LOCKED_DESIGN_NOT_RUNTIME_VALIDATED",
  "sourceOfTruth": "docs/FULL_GAME_CONTENT_LOCK.md",
  "counts": {
    "enemyArchetypes": 35,
    "majorBosses": 9,
    "specialEncounters": 8,
    "facilities": 12,
    "resources": 8,
    "canonicalItems": 36,
    "alyaOutfits": 8,
    "skillRecords": 67
  },
  "combatGuardrails": [
    "Authored encounter power bands; no universal level scaling.",
    "Bosses require phase/intent contracts and explicit objective checks.",
    "NPC and enemy/boss representations are separate records.",
    "Retreat and non-defeat outcomes are encounter-defined.",
    "Cursed/blessed evolution, removal and persistence are explicit per item."
  ],
  "enemies": [
    {
      "id": "ENM-001",
      "name": "Guard",
      "family": "Civilized",
      "tier": "Tier 1",
      "role": "Defender",
      "signatureHook": "Formation and guard interception",
      "combatant": true,
      "aiProfile": "AI_ENM-001",
      "scaling": "authored_power_band",
      "drops": "encounter_specific"
    },
    {
      "id": "ENM-002",
      "name": "Slime",
      "family": "Savage",
      "tier": "Tier 1",
      "role": "Adaptive mob",
      "signatureHook": "Multi-hit and elemental coverage",
      "combatant": true,
      "aiProfile": "AI_ENM-002",
      "scaling": "authored_power_band",
      "drops": "encounter_specific"
    },
    {
      "id": "ENM-003",
      "name": "Cockatrice",
      "family": "Savage",
      "tier": "Tier 1",
      "role": "Status pressure",
      "signatureHook": "Vulnerability and accuracy pressure",
      "combatant": true,
      "aiProfile": "AI_ENM-003",
      "scaling": "authored_power_band",
      "drops": "encounter_specific"
    },
    {
      "id": "ENM-004",
      "name": "Warrior",
      "family": "Tribal",
      "tier": "Tier 1",
      "role": "Melee baseline",
      "signatureHook": "Direct damage and basic intent",
      "combatant": true,
      "aiProfile": "AI_ENM-004",
      "scaling": "authored_power_band",
      "drops": "encounter_specific"
    },
    {
      "id": "ENM-005",
      "name": "Goblin",
      "family": "Tribal",
      "tier": "Tier 1",
      "role": "Evasive utility",
      "signatureHook": "Scavenging and target switching",
      "combatant": true,
      "aiProfile": "AI_ENM-005",
      "scaling": "authored_power_band",
      "drops": "encounter_specific"
    },
    {
      "id": "ENM-006",
      "name": "Mycelian Sentinel",
      "family": "Tribal",
      "tier": "Tier 1",
      "role": "Territorial defender",
      "signatureHook": "Protects a location; not a generic evil tribe",
      "combatant": true,
      "aiProfile": "AI_ENM-006",
      "scaling": "authored_power_band",
      "drops": "encounter_specific"
    },
    {
      "id": "ENM-007",
      "name": "Zombie",
      "family": "Undead",
      "tier": "Tier 1",
      "role": "Attrition",
      "signatureHook": "Slow pressure and undead effects",
      "combatant": true,
      "aiProfile": "AI_ENM-007",
      "scaling": "authored_power_band",
      "drops": "encounter_specific"
    },
    {
      "id": "ENM-008",
      "name": "Augmented Agent",
      "family": "Civilized",
      "tier": "Tier 2",
      "role": "Elite counter",
      "signatureHook": "Adapts against repeated tactics",
      "combatant": true,
      "aiProfile": "AI_ENM-008",
      "scaling": "authored_power_band",
      "drops": "encounter_specific"
    },
    {
      "id": "ENM-009",
      "name": "Kunoichi",
      "family": "Civilized",
      "tier": "Tier 2",
      "role": "Evasion specialist",
      "signatureHook": "Marks and target switching",
      "combatant": true,
      "aiProfile": "AI_ENM-009",
      "scaling": "authored_power_band",
      "drops": "encounter_specific"
    },
    {
      "id": "ENM-010",
      "name": "Krakenblood",
      "family": "Loner",
      "tier": "Tier 2",
      "role": "Resilient pressure",
      "signatureHook": "Sustained pressure with punishable recovery",
      "combatant": true,
      "aiProfile": "AI_ENM-010",
      "scaling": "authored_power_band",
      "drops": "encounter_specific"
    },
    {
      "id": "ENM-011",
      "name": "Kitsune Trickster",
      "family": "Loner",
      "tier": "Tier 2",
      "role": "Decoy controller",
      "signatureHook": "Decoys and intent manipulation",
      "combatant": true,
      "aiProfile": "AI_ENM-011",
      "scaling": "authored_power_band",
      "drops": "encounter_specific"
    },
    {
      "id": "ENM-012",
      "name": "Barbarian",
      "family": "Tribal",
      "tier": "Tier 2",
      "role": "Heavy attacker",
      "signatureHook": "High damage, low flexibility",
      "combatant": true,
      "aiProfile": "AI_ENM-012",
      "scaling": "authored_power_band",
      "drops": "encounter_specific"
    },
    {
      "id": "ENM-013",
      "name": "Royal Guard",
      "family": "Civilized",
      "tier": "Tier 2",
      "role": "Formation defender",
      "signatureHook": "Protects allies and intercepts",
      "combatant": true,
      "aiProfile": "AI_ENM-013",
      "scaling": "authored_power_band",
      "drops": "encounter_specific"
    },
    {
      "id": "ENM-014",
      "name": "Minotaur",
      "family": "Savage",
      "tier": "Tier 2",
      "role": "Guard breaker",
      "signatureHook": "Charge and fortitude pressure",
      "combatant": true,
      "aiProfile": "AI_ENM-014",
      "scaling": "authored_power_band",
      "drops": "encounter_specific"
    },
    {
      "id": "ENM-015",
      "name": "Wolfkin Stalker",
      "family": "Savage",
      "tier": "Tier 2",
      "role": "Pack hunter",
      "signatureHook": "Coordinated attacks and pursuit",
      "combatant": true,
      "aiProfile": "AI_ENM-015",
      "scaling": "authored_power_band",
      "drops": "encounter_specific"
    },
    {
      "id": "ENM-016",
      "name": "Orc Challenger",
      "family": "Tribal",
      "tier": "Tier 2",
      "role": "Duelist",
      "signatureHook": "Resolve pressure; can be neutral in story",
      "combatant": true,
      "aiProfile": "AI_ENM-016",
      "scaling": "authored_power_band",
      "drops": "encounter_specific"
    },
    {
      "id": "ENM-017",
      "name": "Haunt",
      "family": "Loner",
      "tier": "Tier 2",
      "role": "Reactive spirit",
      "signatureHook": "Preparation and knowledge expose weakness",
      "combatant": true,
      "aiProfile": "AI_ENM-017",
      "scaling": "authored_power_band",
      "drops": "encounter_specific"
    },
    {
      "id": "ENM-018",
      "name": "Witch",
      "family": "Loner",
      "tier": "Tier 2",
      "role": "Curse controller",
      "signatureHook": "Control and curse effects; NPC contexts use separate records",
      "combatant": true,
      "aiProfile": "AI_ENM-018",
      "scaling": "authored_power_band",
      "drops": "encounter_specific"
    },
    {
      "id": "ENM-019",
      "name": "Mummy",
      "family": "Undead",
      "tier": "Tier 2",
      "role": "Endurance",
      "signatureHook": "Attrition and seal mechanics",
      "combatant": true,
      "aiProfile": "AI_ENM-019",
      "scaling": "authored_power_band",
      "drops": "encounter_specific"
    },
    {
      "id": "ENM-020",
      "name": "Dullahan",
      "family": "Undead",
      "tier": "Tier 3",
      "role": "Execution elite",
      "signatureHook": "High-threat intent; distinct from Reaper NPC unless explicitly linked",
      "combatant": true,
      "aiProfile": "AI_ENM-020",
      "scaling": "authored_power_band",
      "drops": "encounter_specific"
    },
    {
      "id": "ENM-021",
      "name": "Angelic Arbiter",
      "family": "Civilized",
      "tier": "Tier 3",
      "role": "Protective judge",
      "signatureHook": "Protection and judgment; not automatically evil",
      "combatant": true,
      "aiProfile": "AI_ENM-021",
      "scaling": "authored_power_band",
      "drops": "encounter_specific"
    },
    {
      "id": "ENM-022",
      "name": "Dragonkin",
      "family": "Loner",
      "tier": "Tier 3",
      "role": "Elemental elite",
      "signatureHook": "Strong telegraphed elemental attacks",
      "combatant": true,
      "aiProfile": "AI_ENM-022",
      "scaling": "authored_power_band",
      "drops": "encounter_specific"
    },
    {
      "id": "ENM-023",
      "name": "Fallen Angel",
      "family": "Loner",
      "tier": "Tier 3",
      "role": "Multi-phase controller",
      "signatureHook": "Control and vulnerability cycles",
      "combatant": true,
      "aiProfile": "AI_ENM-023",
      "scaling": "authored_power_band",
      "drops": "encounter_specific"
    },
    {
      "id": "ENM-024",
      "name": "Lamia Duelist",
      "family": "Loner",
      "tier": "Tier 3",
      "role": "Control specialist",
      "signatureHook": "Constriction/control represented without spatial grid assumptions",
      "combatant": true,
      "aiProfile": "AI_ENM-024",
      "scaling": "authored_power_band",
      "drops": "encounter_specific"
    },
    {
      "id": "ENM-025",
      "name": "Demon",
      "family": "Savage",
      "tier": "Tier 3",
      "role": "Hybrid pressure",
      "signatureHook": "Alignment varies by narrative context",
      "combatant": true,
      "aiProfile": "AI_ENM-025",
      "scaling": "authored_power_band",
      "drops": "encounter_specific"
    },
    {
      "id": "ENM-026",
      "name": "Threadling",
      "family": "Ferida",
      "tier": "Tier 1",
      "role": "Swarm unit",
      "signatureHook": "Multiplies if ignored",
      "combatant": true,
      "aiProfile": "AI_ENM-026",
      "scaling": "authored_power_band",
      "drops": "encounter_specific"
    },
    {
      "id": "ENM-027",
      "name": "Hollow Warden",
      "family": "Ferida",
      "tier": "Tier 2",
      "role": "Objective defender",
      "signatureHook": "Linked resistance protects a quest objective",
      "combatant": true,
      "aiProfile": "AI_ENM-027",
      "scaling": "authored_power_band",
      "drops": "encounter_specific"
    },
    {
      "id": "ENM-028",
      "name": "Root-Knot Anchor",
      "family": "Ferida",
      "tier": "Objective",
      "role": "Objective entity",
      "signatureHook": "Defeating it alone does not necessarily complete the encounter",
      "combatant": true,
      "aiProfile": "AI_ENM-028",
      "scaling": "authored_power_band",
      "drops": "encounter_specific"
    },
    {
      "id": "ENM-029",
      "name": "Red-Tide Leech",
      "family": "Ferida",
      "tier": "Tier 2",
      "role": "Resource drainer",
      "signatureHook": "Drains pressure/resources; vulnerable after feeding",
      "combatant": true,
      "aiProfile": "AI_ENM-029",
      "scaling": "authored_power_band",
      "drops": "encounter_specific"
    },
    {
      "id": "ENM-030",
      "name": "Echo Husk",
      "family": "Ferida",
      "tier": "Tier 2",
      "role": "Pattern repeater",
      "signatureHook": "Repeats common action patterns; varied tactics counter it",
      "combatant": true,
      "aiProfile": "AI_ENM-030",
      "scaling": "authored_power_band",
      "drops": "encounter_specific"
    },
    {
      "id": "ENM-031",
      "name": "Guilt Mirror",
      "family": "Ferida",
      "tier": "Tier 3",
      "role": "Relationship pressure",
      "signatureHook": "Uses authored relationship flags only",
      "combatant": true,
      "aiProfile": "AI_ENM-031",
      "scaling": "authored_power_band",
      "drops": "encounter_specific"
    },
    {
      "id": "ENM-032",
      "name": "Ashbound",
      "family": "Ferida",
      "tier": "Tier 2",
      "role": "Hazard fighter",
      "signatureHook": "Alternates armor and exposure",
      "combatant": true,
      "aiProfile": "AI_ENM-032",
      "scaling": "authored_power_band",
      "drops": "encounter_specific"
    },
    {
      "id": "ENM-033",
      "name": "Archive Custodian",
      "family": "Construct",
      "tier": "Tier 3",
      "role": "Research construct",
      "signatureHook": "Tests interrupts and source discovery",
      "combatant": true,
      "aiProfile": "AI_ENM-033",
      "scaling": "authored_power_band",
      "drops": "encounter_specific"
    },
    {
      "id": "ENM-034",
      "name": "Network Eater",
      "family": "Ferida",
      "tier": "Tier 3",
      "role": "Objective attacker",
      "signatureHook": "Targets links and encounter objectives, not only Vitality",
      "combatant": true,
      "aiProfile": "AI_ENM-034",
      "scaling": "authored_power_band",
      "drops": "encounter_specific"
    },
    {
      "id": "ENM-035",
      "name": "Confluence Herald",
      "family": "Ferida",
      "tier": "Tier 4",
      "role": "Late-game manifestation",
      "signatureHook": "Multi-target threat with explicit phase conditions",
      "combatant": true,
      "aiProfile": "AI_ENM-035",
      "scaling": "authored_power_band",
      "drops": "encounter_specific"
    }
  ],
  "bosses": [
    {
      "id": "BOS-001",
      "name": "Root-Knot at the Sluice",
      "act": "ACT-01",
      "composition": "ENM-027 + ENM-028",
      "objective": "Stabilize diversion, sever filament, secure gate; seed loss is mandatory.",
      "phaseContractRequired": true,
      "retreatPolicy": "encounter_defined",
      "postEncounterWorldMutation": true
    },
    {
      "id": "BOS-002",
      "name": "The Pilgrim Engine",
      "act": "ACT-02",
      "composition": "ENM-008 + ENM-030",
      "objective": "Protect shelter routes and disable three supply anchors.",
      "phaseContractRequired": true,
      "retreatPolicy": "encounter_defined",
      "postEncounterWorldMutation": true
    },
    {
      "id": "BOS-003",
      "name": "The Contract Eater",
      "act": "ACT-03",
      "composition": "ENM-011 + ENM-029",
      "objective": "Break exploitative contract seals while keeping caravan escorts safe.",
      "phaseContractRequired": true,
      "retreatPolicy": "encounter_defined",
      "postEncounterWorldMutation": true
    },
    {
      "id": "BOS-004",
      "name": "The Memory That Bites",
      "act": "ACT-03",
      "composition": "ENM-006 + ENM-031",
      "objective": "Resolve a living-memory crisis without destroying the network.",
      "phaseContractRequired": true,
      "retreatPolicy": "encounter_defined",
      "postEncounterWorldMutation": true
    },
    {
      "id": "BOS-005",
      "name": "The Ashen Measure",
      "act": "ACT-04",
      "composition": "ENM-032 + ENM-034",
      "objective": "Counter a triage engine that converts people into risk categories.",
      "phaseContractRequired": true,
      "retreatPolicy": "encounter_defined",
      "postEncounterWorldMutation": true
    },
    {
      "id": "BOS-006",
      "name": "EnemyCommander: Siege of the Broken Route",
      "act": "ACT-04",
      "composition": "NPC-015 combat representation",
      "objective": "EnemyCommander may retreat, yield, or be defeated; NPC state follows authored result.",
      "phaseContractRequired": true,
      "retreatPolicy": "encounter_defined",
      "postEncounterWorldMutation": true
    },
    {
      "id": "BOS-007",
      "name": "The Archive's False Witness",
      "act": "ACT-04",
      "composition": "ENM-033 + ENM-030",
      "objective": "Verify evidence and counter repeated actions.",
      "phaseContractRequired": true,
      "retreatPolicy": "encounter_defined",
      "postEncounterWorldMutation": true
    },
    {
      "id": "BOS-008",
      "name": "The Ferida Manipulator",
      "act": "ACT-05",
      "composition": "NPC-017 combat representation",
      "objective": "Dialogue and combat are separate representations.",
      "phaseContractRequired": true,
      "retreatPolicy": "encounter_defined",
      "postEncounterWorldMutation": true
    },
    {
      "id": "BOS-009",
      "name": "The Confluence Pattern",
      "act": "ACT-05",
      "composition": "ENM-035 + objective anchors",
      "objective": "Disrupt anchors, maintain coalition links, complete world-state objective.",
      "phaseContractRequired": true,
      "retreatPolicy": "encounter_defined",
      "postEncounterWorldMutation": true
    }
  ],
  "specialEncounters": [
    {
      "id": "SPC-001",
      "name": "The First Threadling Nest",
      "act": "ACT-01",
      "purpose": "Teach reinforcement and target prioritization.",
      "optional": true
    },
    {
      "id": "SPC-002",
      "name": "The Sealed Clinic",
      "act": "ACT-01/02",
      "purpose": "Optional care/containment dilemma.",
      "optional": true
    },
    {
      "id": "SPC-003",
      "name": "The Caravan in the Salt Storm",
      "act": "ACT-03",
      "purpose": "Protect supplies or rescue stragglers.",
      "optional": true
    },
    {
      "id": "SPC-004",
      "name": "The Silent Grove",
      "act": "ACT-03",
      "purpose": "Exploration and knowledge check.",
      "optional": true
    },
    {
      "id": "SPC-005",
      "name": "The Broken Lift",
      "act": "ACT-04",
      "purpose": "Objective encounter with environmental hazards.",
      "optional": true
    },
    {
      "id": "SPC-006",
      "name": "The Evacuation Clock",
      "act": "ACT-04",
      "purpose": "Timed objective, not a pure damage race.",
      "optional": true
    },
    {
      "id": "SPC-007",
      "name": "The Unreliable Signal",
      "act": "ACT-04",
      "purpose": "Modifiers change after evidence gathering.",
      "optional": true
    },
    {
      "id": "SPC-008",
      "name": "The Empty Throne",
      "act": "ACT-05",
      "purpose": "Optional encounter testing delegation and ally synergy.",
      "optional": true
    }
  ],
  "facilities": [
    {
      "id": "FAC-001",
      "name": "Recovery Room",
      "unlock": "Act I choice",
      "effect": "Health/status recovery and care route.",
      "upgradeTiers": 3,
      "buildCost": "defined by progression tier; guaranteed main-path feasibility"
    },
    {
      "id": "FAC-002",
      "name": "Common Workshop",
      "unlock": "Act I choice",
      "effect": "Basic crafting, repairs and equipment modification.",
      "upgradeTiers": 3,
      "buildCost": "defined by progression tier; guaranteed main-path feasibility"
    },
    {
      "id": "FAC-003",
      "name": "Coordination Board",
      "unlock": "Act I choice",
      "effect": "Assignment visibility and Expedition overview; never gates Expeditions.",
      "upgradeTiers": 3,
      "buildCost": "defined by progression tier; guaranteed main-path feasibility"
    },
    {
      "id": "FAC-004",
      "name": "Storehouse",
      "unlock": "Act II",
      "effect": "Production buffer and resource reporting; no inventory capacity limit.",
      "upgradeTiers": 3,
      "buildCost": "defined by progression tier; guaranteed main-path feasibility"
    },
    {
      "id": "FAC-005",
      "name": "Training Yard",
      "unlock": "Act II",
      "effect": "Training assignments and combat aptitude development.",
      "upgradeTiers": 3,
      "buildCost": "defined by progression tier; guaranteed main-path feasibility"
    },
    {
      "id": "FAC-006",
      "name": "Research Annex",
      "unlock": "Act II",
      "effect": "Ferida research, enemy knowledge and recipe discovery.",
      "upgradeTiers": 3,
      "buildCost": "defined by progression tier; guaranteed main-path feasibility"
    },
    {
      "id": "FAC-007",
      "name": "Alchemy Bench",
      "unlock": "Act II",
      "effect": "Consumables, botanical processing and controlled transmutation.",
      "upgradeTiers": 3,
      "buildCost": "defined by progression tier; guaranteed main-path feasibility"
    },
    {
      "id": "FAC-008",
      "name": "Trade Stall",
      "unlock": "Act II",
      "effect": "Local trade and market opportunities.",
      "upgradeTiers": 3,
      "buildCost": "defined by progression tier; guaranteed main-path feasibility"
    },
    {
      "id": "FAC-009",
      "name": "Community Hall",
      "unlock": "Act II",
      "effect": "Council, representation, grievance review and morale.",
      "upgradeTiers": 3,
      "buildCost": "defined by progression tier; guaranteed main-path feasibility"
    },
    {
      "id": "FAC-010",
      "name": "Refuge Wing",
      "unlock": "Act II",
      "effect": "Housing, rehabilitation and integration capacity.",
      "upgradeTiers": 3,
      "buildCost": "defined by progression tier; guaranteed main-path feasibility"
    },
    {
      "id": "FAC-011",
      "name": "Expedition Lodge",
      "unlock": "Act III",
      "effect": "Specialist preparation, route intel and Expedition risk modifiers.",
      "upgradeTiers": 3,
      "buildCost": "defined by progression tier; guaranteed main-path feasibility"
    },
    {
      "id": "FAC-012",
      "name": "Signal Tower",
      "unlock": "Act IV",
      "effect": "Regional warning network and late-game coalition coordination.",
      "upgradeTiers": 3,
      "buildCost": "defined by progression tier; guaranteed main-path feasibility"
    }
  ],
  "resources": [
    {
      "id": "RES-001",
      "name": "Timber",
      "use": "Construction and repairs",
      "rarity": "Common",
      "capacityLimit": null
    },
    {
      "id": "RES-002",
      "name": "Fiber",
      "use": "Bindings, reinforcement and field kits",
      "rarity": "Common",
      "capacityLimit": null
    },
    {
      "id": "RES-003",
      "name": "Botanical Extract",
      "use": "Care, alchemy and stabilization",
      "rarity": "Common",
      "capacityLimit": null
    },
    {
      "id": "RES-004",
      "name": "Gold",
      "use": "Trade, wages, contracts and services",
      "rarity": "Currency",
      "capacityLimit": null
    },
    {
      "id": "RES-005",
      "name": "Provisions",
      "use": "Community upkeep, travel and evacuation",
      "rarity": "Common",
      "capacityLimit": null
    },
    {
      "id": "RES-006",
      "name": "Salvage",
      "use": "Mechanical parts and advanced repairs",
      "rarity": "Uncommon",
      "capacityLimit": null
    },
    {
      "id": "RES-007",
      "name": "Research Notes",
      "use": "Knowledge unlocks and controlled research",
      "rarity": "Uncommon",
      "capacityLimit": null
    },
    {
      "id": "RES-008",
      "name": "Trust Tokens",
      "use": "Specific reciprocal commitments and coalition actions; never a universal currency",
      "rarity": "Agreement-bound",
      "capacityLimit": null
    }
  ],
  "items": [
    {
      "id": "ITM-001",
      "name": "Crux of Enlightenment",
      "slot": "Accessory",
      "identity": "Balanced Soul/Body and H-damage specialization.",
      "stableId": true,
      "requiresEffectContract": true,
      "requiresAssetMapping": true
    },
    {
      "id": "ITM-002",
      "name": "Oath of Obedience",
      "slot": "Bottom1",
      "identity": "Blessed defensive sustain; unlock through a protection vow.",
      "stableId": true,
      "requiresEffectContract": true,
      "requiresAssetMapping": true
    },
    {
      "id": "ITM-003",
      "name": "Underwear of Restoration",
      "slot": "Bottom1",
      "identity": "Recovery and status-cleansing synergy.",
      "stableId": true,
      "requiresEffectContract": true,
      "requiresAssetMapping": true
    },
    {
      "id": "ITM-004",
      "name": "Forever Cage",
      "slot": "Bottom2",
      "identity": "Cursed evolution from True-Size Cage; Strain interaction.",
      "stableId": true,
      "requiresEffectContract": true,
      "requiresAssetMapping": true
    },
    {
      "id": "ITM-005",
      "name": "Chastity Belt",
      "slot": "Bottom2",
      "identity": "Defensive anti-penetration/anti-control build.",
      "stableId": true,
      "requiresEffectContract": true,
      "requiresAssetMapping": true
    },
    {
      "id": "ITM-006",
      "name": "Ofuda Chastity",
      "slot": "Bottom2",
      "identity": "Blessed defensive counterpart with Soul/Masochism profile.",
      "stableId": true,
      "requiresEffectContract": true,
      "requiresAssetMapping": true
    },
    {
      "id": "ITM-007",
      "name": "Hypnosis → Reprogram → Slave",
      "slot": "Tattoo",
      "identity": "Single cursed evolution chain; not three inventory records.",
      "stableId": true,
      "requiresEffectContract": true,
      "requiresAssetMapping": true
    },
    {
      "id": "ITM-008",
      "name": "Sensitivity → Receptacle → Fulfilled",
      "slot": "Tattoo",
      "identity": "Cursed incoming-pressure and recent-hit stages.",
      "stableId": true,
      "requiresEffectContract": true,
      "requiresAssetMapping": true
    },
    {
      "id": "ITM-009",
      "name": "Restraint → Suffer → Canvas",
      "slot": "Tattoo",
      "identity": "Cursed resistance/effect-conversion chain.",
      "stableId": true,
      "requiresEffectContract": true,
      "requiresAssetMapping": true
    },
    {
      "id": "ITM-010",
      "name": "Messaging → Sway → Pheromone",
      "slot": "Tattoo",
      "identity": "Blessed area-support chain with consent-aware presentation.",
      "stableId": true,
      "requiresEffectContract": true,
      "requiresAssetMapping": true
    },
    {
      "id": "ITM-011",
      "name": "Body Amulet",
      "slot": "Accessory",
      "identity": "Body-oriented stat profile.",
      "stableId": true,
      "requiresEffectContract": true,
      "requiresAssetMapping": true
    },
    {
      "id": "ITM-012",
      "name": "Agility Ring",
      "slot": "Accessory",
      "identity": "Agility-oriented stat profile.",
      "stableId": true,
      "requiresEffectContract": true,
      "requiresAssetMapping": true
    },
    {
      "id": "ITM-013",
      "name": "Soul Amulet",
      "slot": "Accessory",
      "identity": "Soul-oriented stat profile.",
      "stableId": true,
      "requiresEffectContract": true,
      "requiresAssetMapping": true
    },
    {
      "id": "ITM-014",
      "name": "Charm Ring",
      "slot": "Accessory",
      "identity": "Charm-oriented stat profile.",
      "stableId": true,
      "requiresEffectContract": true,
      "requiresAssetMapping": true
    },
    {
      "id": "ITM-015",
      "name": "Field Harness",
      "slot": "Body",
      "identity": "Expedition and repair preparation.",
      "stableId": true,
      "requiresEffectContract": true,
      "requiresAssetMapping": true
    },
    {
      "id": "ITM-016",
      "name": "Reinforced Boots",
      "slot": "Feet",
      "identity": "Travel hazard reduction.",
      "stableId": true,
      "requiresEffectContract": true,
      "requiresAssetMapping": true
    },
    {
      "id": "ITM-017",
      "name": "Sluiceworker Gloves",
      "slot": "Hands",
      "identity": "Construction and repair bonus.",
      "stableId": true,
      "requiresEffectContract": true,
      "requiresAssetMapping": true
    },
    {
      "id": "ITM-018",
      "name": "Herbal Satchel",
      "slot": "Accessory",
      "identity": "Care and alchemy output.",
      "stableId": true,
      "requiresEffectContract": true,
      "requiresAssetMapping": true
    },
    {
      "id": "ITM-019",
      "name": "Surveyor Lens",
      "slot": "Accessory",
      "identity": "Discovery and enemy intent information.",
      "stableId": true,
      "requiresEffectContract": true,
      "requiresAssetMapping": true
    },
    {
      "id": "ITM-020",
      "name": "Archive Seal",
      "slot": "Accessory",
      "identity": "Research protection and controlled access.",
      "stableId": true,
      "requiresEffectContract": true,
      "requiresAssetMapping": true
    },
    {
      "id": "ITM-021",
      "name": "Caravan Ledger",
      "slot": "Accessory",
      "identity": "Contract and trade insight.",
      "stableId": true,
      "requiresEffectContract": true,
      "requiresAssetMapping": true
    },
    {
      "id": "ITM-022",
      "name": "Guard's Buckler",
      "slot": "Hands",
      "identity": "Defensive reaction synergy.",
      "stableId": true,
      "requiresEffectContract": true,
      "requiresAssetMapping": true
    },
    {
      "id": "ITM-023",
      "name": "Thread-Cut Knife",
      "slot": "Weapon",
      "identity": "Ferida-filament utility; never automatic boss victory.",
      "stableId": true,
      "requiresEffectContract": true,
      "requiresAssetMapping": true
    },
    {
      "id": "ITM-024",
      "name": "Resonance Charm",
      "slot": "Accessory",
      "identity": "Research and Strain interaction.",
      "stableId": true,
      "requiresEffectContract": true,
      "requiresAssetMapping": true
    },
    {
      "id": "ITM-025",
      "name": "Expedition Rations",
      "slot": "Consumable",
      "identity": "Expedition preparation.",
      "stableId": true,
      "requiresEffectContract": true,
      "requiresAssetMapping": true
    },
    {
      "id": "ITM-026",
      "name": "Emergency Filter Kit",
      "slot": "Consumable",
      "identity": "One-use spread-risk mitigation.",
      "stableId": true,
      "requiresEffectContract": true,
      "requiresAssetMapping": true
    },
    {
      "id": "ITM-027",
      "name": "Healing Draught",
      "slot": "Consumable",
      "identity": "Restores Vitality within authored limits.",
      "stableId": true,
      "requiresEffectContract": true,
      "requiresAssetMapping": true
    },
    {
      "id": "ITM-028",
      "name": "Clear-Mind Tonic",
      "slot": "Consumable",
      "identity": "Reduces a defined control/Strain condition.",
      "stableId": true,
      "requiresEffectContract": true,
      "requiresAssetMapping": true
    },
    {
      "id": "ITM-029",
      "name": "Field Dressing",
      "slot": "Consumable",
      "identity": "Treats a defined injury state.",
      "stableId": true,
      "requiresEffectContract": true,
      "requiresAssetMapping": true
    },
    {
      "id": "ITM-030",
      "name": "Botanical Stabilizer",
      "slot": "Consumable",
      "identity": "Stabilizes an affected resident or encounter target.",
      "stableId": true,
      "requiresEffectContract": true,
      "requiresAssetMapping": true
    },
    {
      "id": "ITM-031",
      "name": "Smoke Pellet",
      "slot": "Consumable",
      "identity": "Supports retreat or encounter reposition abstraction.",
      "stableId": true,
      "requiresEffectContract": true,
      "requiresAssetMapping": true
    },
    {
      "id": "ITM-032",
      "name": "Thread-Salt",
      "slot": "Consumable",
      "identity": "Exposes or weakens a Ferida filament.",
      "stableId": true,
      "requiresEffectContract": true,
      "requiresAssetMapping": true
    },
    {
      "id": "ITM-033",
      "name": "Repair Kit",
      "slot": "Consumable",
      "identity": "Reduces a repair cost in eligible contexts.",
      "stableId": true,
      "requiresEffectContract": true,
      "requiresAssetMapping": true
    },
    {
      "id": "ITM-034",
      "name": "Research Sample Case",
      "slot": "Quest/Utility",
      "identity": "Preserves research samples.",
      "stableId": true,
      "requiresEffectContract": true,
      "requiresAssetMapping": true
    },
    {
      "id": "ITM-035",
      "name": "Seed-Reserve Ledger",
      "slot": "Quest Item",
      "identity": "Evidence record; distinct from the seed reserve itself.",
      "stableId": true,
      "requiresEffectContract": true,
      "requiresAssetMapping": true
    },
    {
      "id": "ITM-036",
      "name": "Coalition Signal Key",
      "slot": "Quest Item",
      "identity": "Coordination item; cannot bypass all world-state gates.",
      "stableId": true,
      "requiresEffectContract": true,
      "requiresAssetMapping": true
    }
  ],
  "outfits": [
    {
      "id": "OUT-001",
      "name": "Traveler's Lace",
      "role": "Default balanced baseline",
      "slot": "Outfit",
      "battleRepresentationRequired": true
    },
    {
      "id": "OUT-002",
      "name": "Field Armor",
      "role": "Defensive combat identity",
      "slot": "Outfit",
      "battleRepresentationRequired": true
    },
    {
      "id": "OUT-003",
      "name": "Witch's Mantle",
      "role": "Magic/research specialization",
      "slot": "Outfit",
      "battleRepresentationRequired": true
    },
    {
      "id": "OUT-004",
      "name": "Dancer's Regalia",
      "role": "Social/Charm and event presentation",
      "slot": "Outfit",
      "battleRepresentationRequired": true
    },
    {
      "id": "OUT-005",
      "name": "Nun's Habit",
      "role": "Restraint/protection identity, not a morality marker",
      "slot": "Outfit",
      "battleRepresentationRequired": true
    },
    {
      "id": "OUT-006",
      "name": "Formal Dress",
      "role": "Diplomacy and civic scenes",
      "slot": "Outfit",
      "battleRepresentationRequired": true
    },
    {
      "id": "OUT-007",
      "name": "Demon Armor",
      "role": "Late-game Ferida-facing gear with explicit trade-offs",
      "slot": "Outfit",
      "battleRepresentationRequired": true
    },
    {
      "id": "OUT-008",
      "name": "Shibari Harness",
      "role": "Specialized risk/reaction build with consent-framed presentation",
      "slot": "Outfit",
      "battleRepresentationRequired": true
    }
  ]
}
```

## Embedded source: Full-game character arcs

```json
{
  "schemaVersion": 1,
  "status": "CONTENT_LOCKED_DESIGN_NOT_RUNTIME_VALIDATED",
  "sourceOfTruth": "docs/FULL_GAME_CONTENT_LOCK.md",
  "rules": {
    "allCharactersAdults": true,
    "npcCombatTurns": false,
    "sidequestRequiresAlya": true,
    "expeditionNpcOnly": true,
    "relationshipGraphSelective": true,
    "adultContentOptional": true,
    "adultContentGatesMainStory": false,
    "npcIdNPC020": "retired; never reuse"
  },
  "allies": [
    {
      "id": "ALLY-001",
      "name": "First Ally / Generalist",
      "species": "Human",
      "presentation": "Femboy",
      "adult": true,
      "recruitment": "Starts with Alya; survivor who lost their group.",
      "personalArc": "Locate the former group's trail and choose a voluntary future with Brackenford.",
      "signatureMechanic": "Versatile loadout and development redistribution.",
      "arcTheme": "Adaptability is not the same as having no boundaries.",
      "act3Contribution": "Offers a distinctive system or political perspective; never required as the only solution.",
      "act4Contribution": "May challenge Alya or lead an independent response if supported.",
      "act5EpilogueFlag": "ALLY-001_ARC_RESOLVED",
      "adultContentOptional": true
    },
    {
      "id": "ALLY-002",
      "name": "Guardiã",
      "species": "Minotauroid",
      "presentation": "Futanari",
      "adult": true,
      "recruitment": "Recruit after protecting a vulnerable settlement and accepting help.",
      "personalArc": "Separate care from control; learn to share defensive responsibility.",
      "signatureMechanic": "Guard and Interception; ally protection.",
      "arcTheme": "Protection must not become ownership of every burden.",
      "act3Contribution": "Offers a distinctive system or political perspective; never required as the only solution.",
      "act4Contribution": "May challenge Alya or lead an independent response if supported.",
      "act5EpilogueFlag": "ALLY-002_ARC_RESOLVED",
      "adultContentOptional": true
    },
    {
      "id": "ALLY-003",
      "name": "Rival",
      "species": "Predatory beastfolk",
      "presentation": "Feminine",
      "adult": true,
      "recruitment": "Recruit after a competing leader's plan fails and Alya offers partnership without demanding ideological surrender.",
      "personalArc": "Turn competitive leadership into accountable challenge; can oppose Alya's centralization.",
      "signatureMechanic": "Pressure, momentum and disadvantage exploitation.",
      "arcTheme": "A useful rival can challenge the leader without becoming an enemy.",
      "act3Contribution": "Offers a distinctive system or political perspective; never required as the only solution.",
      "act4Contribution": "May challenge Alya or lead an independent response if supported.",
      "act5EpilogueFlag": "ALLY-003_ARC_RESOLVED",
      "adultContentOptional": true
    },
    {
      "id": "ALLY-004",
      "name": "Erudita",
      "species": "Original arcane species",
      "presentation": "Feminine",
      "adult": true,
      "recruitment": "Recruit after a research expedition exposes the cost of treating people as data.",
      "personalArc": "Preserve research through consent, review and transparent risk.",
      "signatureMechanic": "Creature study, alchemy and encounter knowledge.",
      "arcTheme": "Knowledge without accountability reproduces the harm it studies.",
      "act3Contribution": "Offers a distinctive system or political perspective; never required as the only solution.",
      "act4Contribution": "May challenge Alya or lead an independent response if supported.",
      "act5EpilogueFlag": "ALLY-004_ARC_RESOLVED",
      "adultContentOptional": true
    },
    {
      "id": "ALLY-005",
      "name": "Cuidadora",
      "species": "Human",
      "presentation": "Futanari",
      "adult": true,
      "recruitment": "Conditional Act I care route or Recovery Room investment.",
      "personalArc": "Move from emergency response to prevention and community health.",
      "signatureMechanic": "Diagnosis, recovery and health resilience.",
      "arcTheme": "Treatment cannot justify preventable harm.",
      "act3Contribution": "Offers a distinctive system or political perspective; never required as the only solution.",
      "act4Contribution": "May challenge Alya or lead an independent response if supported.",
      "act5EpilogueFlag": "ALLY-005_ARC_RESOLVED",
      "adultContentOptional": true
    },
    {
      "id": "ALLY-006",
      "name": "Artesã",
      "species": "Goblin",
      "presentation": "Feminine",
      "adult": true,
      "recruitment": "Recruit through workshop and repair chain.",
      "personalArc": "Accept maintenance and safety standards without losing inventive freedom.",
      "signatureMechanic": "Construction, modification and controlled transmutation.",
      "arcTheme": "Reliability is part of invention, not its enemy.",
      "act3Contribution": "Offers a distinctive system or political perspective; never required as the only solution.",
      "act4Contribution": "May challenge Alya or lead an independent response if supported.",
      "act5EpilogueFlag": "ALLY-006_ARC_RESOLVED",
      "adultContentOptional": true
    },
    {
      "id": "ALLY-007",
      "name": "Caçadora",
      "species": "Fox beastfolk",
      "presentation": "Futanari",
      "adult": true,
      "recruitment": "Recruit through exploration route-rescue chain.",
      "personalArc": "Choose reciprocal responsibility over solitary competence.",
      "signatureMechanic": "Ranged combat, traps, discovery and route-risk reduction.",
      "arcTheme": "Self-reliance can be a skill, not a permanent exile.",
      "act3Contribution": "Offers a distinctive system or political perspective; never required as the only solution.",
      "act4Contribution": "May challenge Alya or lead an independent response if supported.",
      "act5EpilogueFlag": "ALLY-007_ARC_RESOLVED",
      "adultContentOptional": true
    },
    {
      "id": "ALLY-008",
      "name": "Mercador",
      "species": "Feline beastfolk",
      "presentation": "Femboy",
      "adult": true,
      "recruitment": "Recruit after a trade dispute and return of a profitable but harmful contract.",
      "personalArc": "Build resilient trade rather than dependency and extraction.",
      "signatureMechanic": "Trade access, negotiation and commercial opportunities; low combat emphasis is intentional.",
      "arcTheme": "Prosperity needs reciprocal obligations.",
      "act3Contribution": "Offers a distinctive system or political perspective; never required as the only solution.",
      "act4Contribution": "May challenge Alya or lead an independent response if supported.",
      "act5EpilogueFlag": "ALLY-008_ARC_RESOLVED",
      "adultContentOptional": true
    },
    {
      "id": "ALLY-009",
      "name": "Inadaptada",
      "species": "Rare/exotic species",
      "presentation": "Futanari",
      "adult": true,
      "recruitment": "Optional recruitment through misunderstood-incident sidequest chain.",
      "personalArc": "Build confidence without requiring assimilation; learning speed requires time and support.",
      "signatureMechanic": "Exceptional Learning and flexible long-term development.",
      "arcTheme": "Belonging does not require becoming ordinary.",
      "act3Contribution": "Offers a distinctive system or political perspective; never required as the only solution.",
      "act4Contribution": "May challenge Alya or lead an independent response if supported.",
      "act5EpilogueFlag": "ALLY-009_ARC_RESOLVED",
      "adultContentOptional": true
    },
    {
      "id": "ALLY-010",
      "name": "Devoto",
      "species": "Faerie-like humanoid",
      "presentation": "Feminine",
      "adult": true,
      "recruitment": "Recruit through mediation and morale chain.",
      "personalArc": "Retain idealism while learning boundaries and accountable processes.",
      "signatureMechanic": "Protection/buffs tied to morale, integration and cohesion.",
      "arcTheme": "Compassion needs boundaries to endure.",
      "act3Contribution": "Offers a distinctive system or political perspective; never required as the only solution.",
      "act4Contribution": "May challenge Alya or lead an independent response if supported.",
      "act5EpilogueFlag": "ALLY-010_ARC_RESOLVED",
      "adultContentOptional": true
    }
  ],
  "namedNpcs": [
    {
      "id": "NPC-001",
      "name": "Tavernkeeper",
      "group": "Community",
      "species": "Human",
      "presentation": "Futanari",
      "adult": true,
      "tier": "H3",
      "arc": "Rumor hub; tracks how local stories change and distinguishes facts from repeated accounts.",
      "relationships": "Only authored relationship edges; no full cast matrix.",
      "combatRule": "No combat turns while functioning as NPC; any boss uses a separate combat record.",
      "adultContentRule": "Tier-gated, optional, adult, consent-aware; never main-quest required."
    },
    {
      "id": "NPC-002",
      "name": "Dancer",
      "group": "Community",
      "species": "Desert Elf",
      "presentation": "Feminine",
      "adult": true,
      "tier": "H2/H3",
      "arc": "Public performance and cultural events; supports morale but refuses to be treated as a universal solution.",
      "relationships": "Only authored relationship edges; no full cast matrix.",
      "combatRule": "No combat turns while functioning as NPC; any boss uses a separate combat record.",
      "adultContentRule": "Tier-gated, optional, adult, consent-aware; never main-quest required."
    },
    {
      "id": "NPC-003",
      "name": "Community Elder",
      "group": "Community",
      "species": "Human",
      "presentation": "Feminine",
      "adult": true,
      "tier": "H3",
      "arc": "Preserves local history and eventually admits the old allocation rules caused harm.",
      "relationships": "Only authored relationship edges; no full cast matrix.",
      "combatRule": "No combat turns while functioning as NPC; any boss uses a separate combat record.",
      "adultContentRule": "Tier-gated, optional, adult, consent-aware; never main-quest required."
    },
    {
      "id": "NPC-004",
      "name": "Mediator",
      "group": "Community",
      "species": "Human",
      "presentation": "Futanari",
      "adult": true,
      "tier": "H2/H3",
      "arc": "Turns disputes into explicit agreements; can lead council process and review.",
      "relationships": "Only authored relationship edges; no full cast matrix.",
      "combatRule": "No combat turns while functioning as NPC; any boss uses a separate combat record.",
      "adultContentRule": "Tier-gated, optional, adult, consent-aware; never main-quest required."
    },
    {
      "id": "NPC-005",
      "name": "Pragmatic Mentor",
      "group": "Organization",
      "species": "Human",
      "presentation": "Feminine",
      "adult": true,
      "tier": "H3",
      "arc": "Provides training and institutional context; cooperates after rupture if local safeguards are credible.",
      "relationships": "Only authored relationship edges; no full cast matrix.",
      "combatRule": "No combat turns while functioning as NPC; any boss uses a separate combat record.",
      "adultContentRule": "Tier-gated, optional, adult, consent-aware; never main-quest required."
    },
    {
      "id": "NPC-006",
      "name": "Institutional Representative",
      "group": "Organization",
      "species": "Human",
      "presentation": "Femboy",
      "adult": true,
      "tier": "H3",
      "arc": "Negotiates reporting and supervision; may become an intermediary across the institutional rupture.",
      "relationships": "Only authored relationship edges; no full cast matrix.",
      "combatRule": "No combat turns while functioning as NPC; any boss uses a separate combat record.",
      "adultContentRule": "Tier-gated, optional, adult, consent-aware; never main-quest required."
    },
    {
      "id": "NPC-007",
      "name": "Ferida Researcher",
      "group": "Organization",
      "species": "Augmented",
      "presentation": "Feminine",
      "adult": true,
      "tier": "H3",
      "arc": "Creates safer evidence protocols; chooses between publication, restricted containment and shared research.",
      "relationships": "Only authored relationship edges; no full cast matrix.",
      "combatRule": "No combat turns while functioning as NPC; any boss uses a separate combat record.",
      "adultContentRule": "Tier-gated, optional, adult, consent-aware; never main-quest required."
    },
    {
      "id": "NPC-008",
      "name": "Hardliner",
      "group": "Organization",
      "species": "Human",
      "presentation": "Futanari",
      "adult": true,
      "tier": "H3/H4",
      "arc": "Recurring institutional opponent; can be constrained or persuaded by evidence, never by one speech.",
      "relationships": "Only authored relationship edges; no full cast matrix.",
      "combatRule": "No combat turns while functioning as NPC; any boss uses a separate combat record.",
      "adultContentRule": "Tier-gated, optional, adult, consent-aware; never main-quest required."
    },
    {
      "id": "NPC-009",
      "name": "Regional Authority",
      "group": "Regional Center",
      "species": "Angel",
      "presentation": "Feminine",
      "adult": true,
      "tier": "H3",
      "arc": "Grants legitimacy when governance is accountable and demands transparent cost-sharing.",
      "relationships": "Only authored relationship edges; no full cast matrix.",
      "combatRule": "No combat turns while functioning as NPC; any boss uses a separate combat record.",
      "adultContentRule": "Tier-gated, optional, adult, consent-aware; never main-quest required."
    },
    {
      "id": "NPC-010",
      "name": "Trade Representative",
      "group": "Regional Center",
      "species": "Lamia",
      "presentation": "Futanari",
      "adult": true,
      "tier": "H2/H3",
      "arc": "Negotiates route access, contract clauses and supply shocks.",
      "relationships": "Only authored relationship edges; no full cast matrix.",
      "combatRule": "No combat turns while functioning as NPC; any boss uses a separate combat record.",
      "adultContentRule": "Tier-gated, optional, adult, consent-aware; never main-quest required."
    },
    {
      "id": "NPC-011",
      "name": "Priestess",
      "group": "Regional Center",
      "species": "Human",
      "presentation": "Feminine",
      "adult": true,
      "tier": "H3",
      "arc": "Supports grief, recovery and community memory without replacing care or accountability.",
      "relationships": "Only authored relationship edges; no full cast matrix.",
      "combatRule": "No combat turns while functioning as NPC; any boss uses a separate combat record.",
      "adultContentRule": "Tier-gated, optional, adult, consent-aware; never main-quest required."
    },
    {
      "id": "NPC-012",
      "name": "Tribal Matriarch",
      "group": "Tribe A",
      "species": "Mycelia",
      "presentation": "Feminine",
      "adult": true,
      "tier": "H3",
      "arc": "Protects Mycelian sovereignty; shares memory only with consent and reciprocity.",
      "relationships": "Only authored relationship edges; no full cast matrix.",
      "combatRule": "No combat turns while functioning as NPC; any boss uses a separate combat record.",
      "adultContentRule": "Tier-gated, optional, adult, consent-aware; never main-quest required."
    },
    {
      "id": "NPC-013",
      "name": "Tribal Guide",
      "group": "Tribe A",
      "species": "Mycelia",
      "presentation": "Futanari",
      "adult": true,
      "tier": "H2/H3",
      "arc": "Mediates travel and cultural interpretation; challenges Alya's assumptions.",
      "relationships": "Only authored relationship edges; no full cast matrix.",
      "combatRule": "No combat turns while functioning as NPC; any boss uses a separate combat record.",
      "adultContentRule": "Tier-gated, optional, adult, consent-aware; never main-quest required."
    },
    {
      "id": "NPC-014",
      "name": "War-Chief",
      "group": "Tribe B",
      "species": "Orc",
      "presentation": "Futanari",
      "adult": true,
      "tier": "H3",
      "arc": "Tests agreements through ritualized contest and resource obligations; values explicit terms.",
      "relationships": "Only authored relationship edges; no full cast matrix.",
      "combatRule": "No combat turns while functioning as NPC; any boss uses a separate combat record.",
      "adultContentRule": "Tier-gated, optional, adult, consent-aware; never main-quest required."
    },
    {
      "id": "NPC-015",
      "name": "EnemyCommander",
      "group": "Adversarial",
      "species": "Human",
      "presentation": "Futanari",
      "adult": true,
      "tier": "H3/H4",
      "arc": "Recurring faction commander with separate combat representation; exploits instability but is not the Ferida.",
      "relationships": "Only authored relationship edges; no full cast matrix.",
      "combatRule": "No combat turns while functioning as NPC; any boss uses a separate combat record.",
      "adultContentRule": "Tier-gated, optional, adult, consent-aware; never main-quest required."
    },
    {
      "id": "NPC-016",
      "name": "Faction Dissident",
      "group": "Adversarial",
      "species": "Human",
      "presentation": "Femboy",
      "adult": true,
      "tier": "H3",
      "arc": "Reveals internal dissent and supports safe defections without demanding unconditional allegiance.",
      "relationships": "Only authored relationship edges; no full cast matrix.",
      "combatRule": "No combat turns while functioning as NPC; any boss uses a separate combat record.",
      "adultContentRule": "Tier-gated, optional, adult, consent-aware; never main-quest required."
    },
    {
      "id": "NPC-017",
      "name": "Ferida Manipulator",
      "group": "Adversarial",
      "species": "Fallen Angel",
      "presentation": "Feminine",
      "adult": true,
      "tier": "H4",
      "arc": "Major antagonist who weaponizes real grievances to justify destructive absolutes; separate dialogue and boss records.",
      "relationships": "Only authored relationship edges; no full cast matrix.",
      "combatRule": "No combat turns while functioning as NPC; any boss uses a separate combat record.",
      "adultContentRule": "Tier-gated, optional, adult, consent-aware; never main-quest required."
    },
    {
      "id": "NPC-018",
      "name": "Reaper",
      "group": "World",
      "species": "Dullahan",
      "presentation": "Feminine",
      "adult": true,
      "tier": "H3/H4",
      "arc": "Neutral threshold figure who reveals consequences and mortality without becoming a quest vending machine.",
      "relationships": "Only authored relationship edges; no full cast matrix.",
      "combatRule": "No combat turns while functioning as NPC; any boss uses a separate combat record.",
      "adultContentRule": "Tier-gated, optional, adult, consent-aware; never main-quest required."
    },
    {
      "id": "NPC-019",
      "name": "Dryad",
      "group": "World",
      "species": "Dryad",
      "presentation": "Feminine",
      "adult": true,
      "tier": "H3",
      "arc": "Supports ecological restoration when extraction and stewardship obligations are honored.",
      "relationships": "Only authored relationship edges; no full cast matrix.",
      "combatRule": "No combat turns while functioning as NPC; any boss uses a separate combat record.",
      "adultContentRule": "Tier-gated, optional, adult, consent-aware; never main-quest required."
    },
    {
      "id": "NPC-021",
      "name": "Survivor",
      "group": "World",
      "species": "Orc",
      "presentation": "Futanari",
      "adult": true,
      "tier": "H2/H3",
      "arc": "Living consequence of earlier containment; can become witness/advocate or leave if instrumentalized.",
      "relationships": "Only authored relationship edges; no full cast matrix.",
      "combatRule": "No combat turns while functioning as NPC; any boss uses a separate combat record.",
      "adultContentRule": "Tier-gated, optional, adult, consent-aware; never main-quest required."
    },
    {
      "id": "NPC-022",
      "name": "Demonkin",
      "group": "Demon/World",
      "species": "Demon",
      "presentation": "Futanari",
      "adult": true,
      "tier": "H3/H4",
      "arc": "Rescue and rehabilitation arc demonstrating that origin does not determine consent, allegiance or moral character.",
      "relationships": "Only authored relationship edges; no full cast matrix.",
      "combatRule": "No combat turns while functioning as NPC; any boss uses a separate combat record.",
      "adultContentRule": "Tier-gated, optional, adult, consent-aware; never main-quest required."
    }
  ],
  "genericNpcTemplates": [
    {
      "id": "TPL-001",
      "name": "Farm and field worker",
      "role": "Community labor, gathering, seasonal upkeep",
      "individualHContent": false,
      "variationAxes": [
        "species",
        "clothing",
        "age within adult range",
        "voice",
        "local allegiance"
      ],
      "visualRule": "Adult humanoid fantasy first; avoid child-coded proportions; species, culture and role are independent axes."
    },
    {
      "id": "TPL-002",
      "name": "Craftsperson",
      "role": "Workshop, repairs, production",
      "individualHContent": false,
      "variationAxes": [
        "species",
        "clothing",
        "age within adult range",
        "voice",
        "local allegiance"
      ],
      "visualRule": "Adult humanoid fantasy first; avoid child-coded proportions; species, culture and role are independent axes."
    },
    {
      "id": "TPL-003",
      "name": "Caravan guard",
      "role": "Trade route security, escort",
      "individualHContent": false,
      "variationAxes": [
        "species",
        "clothing",
        "age within adult range",
        "voice",
        "local allegiance"
      ],
      "visualRule": "Adult humanoid fantasy first; avoid child-coded proportions; species, culture and role are independent axes."
    },
    {
      "id": "TPL-004",
      "name": "Caravan merchant",
      "role": "Vendor, contracts, market variation",
      "individualHContent": false,
      "variationAxes": [
        "species",
        "clothing",
        "age within adult range",
        "voice",
        "local allegiance"
      ],
      "visualRule": "Adult humanoid fantasy first; avoid child-coded proportions; species, culture and role are independent axes."
    },
    {
      "id": "TPL-005",
      "name": "Refugee household member",
      "role": "Integration, housing, representation",
      "individualHContent": false,
      "variationAxes": [
        "species",
        "clothing",
        "age within adult range",
        "voice",
        "local allegiance"
      ],
      "visualRule": "Adult humanoid fantasy first; avoid child-coded proportions; species, culture and role are independent axes."
    },
    {
      "id": "TPL-006",
      "name": "Local healer",
      "role": "Basic care service; does not replace Cuidadora identity",
      "individualHContent": false,
      "variationAxes": [
        "species",
        "clothing",
        "age within adult range",
        "voice",
        "local allegiance"
      ],
      "visualRule": "Adult humanoid fantasy first; avoid child-coded proportions; species, culture and role are independent axes."
    },
    {
      "id": "TPL-007",
      "name": "Research assistant",
      "role": "Research Annex, sample handling",
      "individualHContent": false,
      "variationAxes": [
        "species",
        "clothing",
        "age within adult range",
        "voice",
        "local allegiance"
      ],
      "visualRule": "Adult humanoid fantasy first; avoid child-coded proportions; species, culture and role are independent axes."
    },
    {
      "id": "TPL-008",
      "name": "Organization field agent",
      "role": "Reporting, logistics, crisis response",
      "individualHContent": false,
      "variationAxes": [
        "species",
        "clothing",
        "age within adult range",
        "voice",
        "local allegiance"
      ],
      "visualRule": "Adult humanoid fantasy first; avoid child-coded proportions; species, culture and role are independent axes."
    },
    {
      "id": "TPL-009",
      "name": "Organization reformer",
      "role": "Internal plurality, procedural challenge",
      "individualHContent": false,
      "variationAxes": [
        "species",
        "clothing",
        "age within adult range",
        "voice",
        "local allegiance"
      ],
      "visualRule": "Adult humanoid fantasy first; avoid child-coded proportions; species, culture and role are independent axes."
    },
    {
      "id": "TPL-010",
      "name": "Tribal steward",
      "role": "Local custom and resource stewardship",
      "individualHContent": false,
      "variationAxes": [
        "species",
        "clothing",
        "age within adult range",
        "voice",
        "local allegiance"
      ],
      "visualRule": "Adult humanoid fantasy first; avoid child-coded proportions; species, culture and role are independent axes."
    },
    {
      "id": "TPL-011",
      "name": "Cinderfall worker",
      "role": "Industrial upkeep, safety and evacuation",
      "individualHContent": false,
      "variationAxes": [
        "species",
        "clothing",
        "age within adult range",
        "voice",
        "local allegiance"
      ],
      "visualRule": "Adult humanoid fantasy first; avoid child-coded proportions; species, culture and role are independent axes."
    },
    {
      "id": "TPL-012",
      "name": "Traveling storyteller",
      "role": "Rumors, regional lore, optional encounters",
      "individualHContent": false,
      "variationAxes": [
        "species",
        "clothing",
        "age within adult range",
        "voice",
        "local allegiance"
      ],
      "visualRule": "Adult humanoid fantasy first; avoid child-coded proportions; species, culture and role are independent axes."
    }
  ],
  "relationshipClusters": [
    {
      "id": "REL-001",
      "members": [
        "ALLY-001",
        "ALLY-007",
        "ALLY-009"
      ],
      "theme": "Adaptation, exploration, belonging"
    },
    {
      "id": "REL-002",
      "members": [
        "ALLY-002",
        "ALLY-003",
        "ALLY-005"
      ],
      "theme": "Protection, competition, care"
    },
    {
      "id": "REL-003",
      "members": [
        "ALLY-004",
        "ALLY-006"
      ],
      "theme": "Research, invention, accountability"
    },
    {
      "id": "REL-004",
      "members": [
        "ALLY-008",
        "ALLY-010",
        "ALLY-009"
      ],
      "theme": "Trade, idealism, integration"
    }
  ],
  "productionNotes": [
    "Named NPCs may have multiple functional tags; do not add duplicate named roles to satisfy service coverage.",
    "Ally combat/community identity must remain distinct even where NPC services overlap.",
    "NPC-015 and NPC-017 require separate NPC and Enemy/Boss records.",
    "Adult content must be authored against arc/state and consent; no quota-driven scenes."
  ]
}
```

## Embedded source: Act I structured quests

```json
{
  "schema_version": "1.0.0",
  "content_pack_id": "CONTENT_PACK_VS1_ACT_I",
  "status": "content_design_baseline_provisional_values",
  "source_documents": [
    "docs/VERTICAL_SLICE_SCOPE.md",
    "docs/vertical_slice/ACT_I_QUEST_GRAPH.md",
    "docs/vertical_slice/ACT_I_QUEST_GRAPH_CONTINUATION.md",
    "docs/NARRATIVE_CANON.md"
  ],
  "ids_policy": "VS1_* IDs are stable slice IDs; presentation strings may be localized independently.",
  "start_quest_id": "VS1_Q01",
  "quests": [
    {
      "id": "VS1_Q01",
      "title": "Arrival and the Empty Cistern",
      "type": [
        "Main",
        "Social",
        "Tutorial"
      ],
      "location_id": "LOC_VS1_BRACKENFORD",
      "prerequisites": [],
      "objectives": [
        "Meet Mara Venn",
        "Inspect the cistern",
        "Ask one local for context"
      ],
      "set_flags": [
        "VS1_MARA_MET",
        "VS1_CISTERN_INSPECTED"
      ],
      "next_quest_id": "VS1_Q02",
      "optional_content_ids": [],
      "failure_policy": "No hard failure; allow revisiting conversations."
    },
    {
      "id": "VS1_Q02",
      "title": "A Ration Is Not a History",
      "type": [
        "Main",
        "Investigation",
        "Social"
      ],
      "location_id": "LOC_VS1_BRACKENFORD",
      "prerequisites": [
        "VS1_Q01_COMPLETE"
      ],
      "objectives": [
        "Hear the rationing history",
        "Learn why Mara diverted water",
        "Choose a provisional response"
      ],
      "choices": [
        {
          "id": "VS1_CHOICE_RATION_ENFORCE",
          "flag": "VS1_RATION_ENFORCED",
          "effects": [
            "MARA_TRUST_DOWN",
            "REPAIR_COST_UP"
          ],
          "benefit": "Small immediate supply benefit"
        },
        {
          "id": "VS1_CHOICE_RATION_SHARE",
          "flag": "VS1_RATION_SHARED",
          "effects": [
            "COMMUNITY_TRUST_UP",
            "SUPPLY_BUFFER_DOWN"
          ],
          "benefit": "Improves local trust"
        },
        {
          "id": "VS1_CHOICE_RATION_INVESTIGATE",
          "flag": "VS1_RATION_INVESTIGATE",
          "effects": [
            "CLUE_RELIABILITY_UP"
          ],
          "benefit": "Preserves relationship options"
        }
      ],
      "next_quest_id": "VS1_Q03",
      "failure_policy": "All choices continue the main quest."
    },
    {
      "id": "VS1_Q03",
      "title": "The Red Thread",
      "type": [
        "Main",
        "Exploration",
        "Combat"
      ],
      "location_id": "LOC_VS1_ASHFEN_VERGE",
      "poi_id": "POI_VS1_SILT_PATH",
      "prerequisites": [
        "VS1_Q02_COMPLETE"
      ],
      "objectives": [
        "Reach the old irrigation route",
        "Resolve the Frayed Husk encounter",
        "Inspect or bypass the blocked channel"
      ],
      "set_flags": [
        "VS1_RED_THREAD_CONFIRMED"
      ],
      "optional_objectives": [
        {
          "id": "VS1_OBJ_CHANNEL_CLUE",
          "flag": "VS1_CHANNEL_CLUE_FOUND",
          "reward_id": "ITEM_VS1_FILTER_FIBER",
          "discovery_id": "VS1_DISCOVERY_CHANNEL_SAMPLE"
        }
      ],
      "encounter_ids": [
        "ENC_VS1_01_HUSKS",
        "ENC_VS1_02_THREADLINGS"
      ],
      "next_quest_id": "VS1_Q04",
      "failure_policy": "Retreat costs time or a modest reward opportunity; main path remains available."
    },
    {
      "id": "VS1_Q04",
      "title": "The Cost of a Quick Fix",
      "type": [
        "Main",
        "Encounter",
        "Consequence"
      ],
      "location_id": "LOC_VS1_ASHFEN_VERGE",
      "poi_id": "POI_VS1_OLD_WEIR",
      "prerequisites": [
        "VS1_Q03_COMPLETE"
      ],
      "choices": [
        {
          "id": "VS1_CHOICE_GATE_CLOSE",
          "flag": "VS1_GATE_CLOSED",
          "effects": [
            "UPPER_CHANNEL_TEMP_SAFE",
            "LOWER_RESERVE_DRYING",
            "TIMBER_REPAIR_COST_PLUS_1"
          ]
        },
        {
          "id": "VS1_CHOICE_GATE_DIVERT",
          "flag": "VS1_TEMP_DIVERSION",
          "costs": [
            {
              "resource_id": "RESOURCE_FIBER",
              "quantity": 1
            }
          ],
          "effects": [
            "LOWER_CHANNEL_ACCESS_PRESERVED",
            "TIME_COST_SMALL"
          ]
        },
        {
          "id": "VS1_CHOICE_GATE_WITHDRAW",
          "flag": "VS1_WITHDREW",
          "effects": [
            "THREAT_PRESSURE_UP"
          ]
        }
      ],
      "set_flags": [
        "VS1_QUICK_FIX_COST_REVEALED"
      ],
      "next_quest_id": "VS1_Q05",
      "failure_policy": "Choice affects later cost and pressure, never creates a softlock."
    },
    {
      "id": "VS1_Q05",
      "title": "The Road Is Still Open",
      "type": [
        "Main",
        "Character",
        "Commitment"
      ],
      "location_id": "LOC_VS1_BRACKENFORD",
      "prerequisites": [
        "VS1_Q04_COMPLETE"
      ],
      "objectives": [
        "Hear that Alya can still continue her journey",
        "Choose to stay"
      ],
      "set_flags": [
        "VS1_ALYA_STAYS",
        "VS1_RESPONSIBILITY_ACCEPTED"
      ],
      "next_quest_id": "VS1_Q06",
      "failure_policy": "Departure is acknowledged as an emotional possibility; the slice's canonical path continues with Alya staying."
    },
    {
      "id": "VS1_Q06",
      "title": "The Organization Arrives",
      "type": [
        "Main",
        "Social",
        "Faction"
      ],
      "location_id": "LOC_VS1_BRACKENFORD",
      "prerequisites": [
        "VS1_Q05_COMPLETE"
      ],
      "objectives": [
        "Hear the risk assessment",
        "Understand the containment proposal",
        "Choose an initial stance"
      ],
      "set_flags": [
        "VS1_ORG_PLAN_PRESENTED"
      ],
      "choices": [
        {
          "id": "VS1_CHOICE_ORG_ACCEPT",
          "flag": "VS1_ORG_STANCE_ACCEPTED",
          "effects": [
            "INSTITUTIONAL_TRUST_UP",
            "PREPARATION_ITEM_GRANTED",
            "LOWER_RESIDENT_SUPPORT_COST_UP"
          ]
        },
        {
          "id": "VS1_CHOICE_ORG_CHALLENGE",
          "flag": "VS1_ORG_STANCE_CHALLENGED",
          "effects": [
            "INSTITUTIONAL_TRUST_DOWN",
            "EVIDENCE_REQUESTED"
          ]
        },
        {
          "id": "VS1_CHOICE_ORG_ALTERNATIVE",
          "flag": "VS1_ORG_STANCE_ALTERNATIVE_REQUESTED",
          "effects": [
            "THIRD_SOLUTION_ROUTE_OPEN"
          ]
        }
      ],
      "next_quest_id": "VS1_Q07",
      "failure_policy": "The Organization remains useful and internally plural under every stance."
    },
    {
      "id": "VS1_Q07",
      "title": "Three Parts of a Third Option",
      "type": [
        "Main",
        "Preparation",
        "Community"
      ],
      "location_id": "LOC_VS1_ASHFEN_VERGE",
      "prerequisites": [
        "VS1_Q06_COMPLETE"
      ],
      "objectives": [
        "Secure repair materials",
        "Secure local participation",
        "Resolve the Hollow Warden encounter",
        "Choose a preparation priority"
      ],
      "required_resources": [
        {
          "resource_id": "RESOURCE_TIMBER",
          "quantity": 2
        },
        {
          "resource_id": "RESOURCE_FIBER",
          "quantity": 2
        }
      ],
      "optional_requirements": [
        {
          "id": "VS1_REQ_CHANNEL_CLUE",
          "all_of": [
            "VS1_CHANNEL_CLUE_FOUND"
          ],
          "unlocks_choice": "VS1_CHOICE_STAGED_DIVERSION"
        }
      ],
      "choices": [
        {
          "id": "VS1_CHOICE_PREP_WORKERS",
          "value": "WORKERS",
          "effects": [
            "CLIMAX_PRESSURE_DOWN",
            "OBJECTIVE_DEFENSE_STEPS_PLUS_1"
          ],
          "set_flags": [
            "VS1_PREPARATION_PRIORITY_WORKERS"
          ]
        },
        {
          "id": "VS1_CHOICE_PREP_CHANNEL",
          "value": "CHANNEL",
          "effects": [
            "CLIMAX_SPREAD_PRESSURE_DOWN",
            "RECOVERY_DURATION_UP"
          ],
          "set_flags": [
            "VS1_PREPARATION_PRIORITY_CHANNEL"
          ]
        },
        {
          "id": "VS1_CHOICE_STAGED_DIVERSION",
          "value": "STAGED_DIVERSION",
          "effects": [
            "CLIMAX_SPREAD_PRESSURE_DOWN",
            "RECOVERY_DURATION_DOWN"
          ],
          "requirements": [
            "VS1_CHANNEL_CLUE_FOUND"
          ],
          "costs": [
            {
              "item_id": "ITEM_VS1_FILTER_FIBER",
              "quantity": 1
            }
          ],
          "set_flags": [
            "VS1_PREPARATION_PRIORITY_STAGED_DIVERSION"
          ]
        }
      ],
      "set_flags": [
        "VS1_THIRD_OPTION_READY",
        "VS1_COMMUNITY_CONTRIBUTION"
      ],
      "encounter_ids": [
        "ENC_VS1_03_HOLLOW_WARDEN"
      ],
      "next_quest_id": "VS1_Q08",
      "failure_policy": "Required materials have fallback sources and cannot be permanently lost to optional interactions.",
      "conditional_cost_refs": [
        "COST_VS1_GATE_REPAIR_SURCHARGE",
        "COST_VS1_ORG_SUPPORT"
      ]
    },
    {
      "id": "VS1_Q08",
      "title": "Hold the Sluice",
      "type": [
        "Main",
        "Climax",
        "Combat",
        "Objective"
      ],
      "location_id": "LOC_VS1_ASHFEN_VERGE",
      "poi_id": "POI_VS1_ROOT_VAULT",
      "prerequisites": [
        "VS1_Q07_COMPLETE",
        "VS1_THIRD_OPTION_READY"
      ],
      "encounter_ids": [
        "ENC_VS1_04_ROOT_VAULT"
      ],
      "objectives": [
        {
          "id": "VS1_OBJ_STABILIZE_DIVERSION",
          "kind": "EncounterObjective"
        },
        {
          "id": "VS1_OBJ_SEVER_FILAMENT",
          "kind": "EncounterObjective"
        },
        {
          "id": "VS1_OBJ_SECURE_GATE",
          "kind": "EncounterObjective"
        }
      ],
      "mandatory_consequences": [
        "VS1_SEED_RESERVE_LOST",
        "VS1_DOWNSTREAM_CHANNEL_SECURED"
      ],
      "set_flags": [
        "VS1_SLICE_CRISIS_RESOLVED"
      ],
      "next_quest_id": "VS1_Q09",
      "failure_policy": "Retreat is allowed; retry is allowed. Once resolution commits the seed loss, retries do not reverse it."
    },
    {
      "id": "VS1_Q09",
      "title": "What Remains",
      "type": [
        "Main",
        "Consequence",
        "Character"
      ],
      "location_id": "LOC_VS1_BRACKENFORD",
      "prerequisites": [
        "VS1_Q08_COMPLETE"
      ],
      "objectives": [
        "Witness the loss of the seed reserve",
        "Resolve the community's immediate priorities",
        "Choose the first recovery priority"
      ],
      "choices": [
        {
          "id": "VS1_CHOICE_RECOVERY_CARE",
          "value": "CARE",
          "effects": [
            "RECOVERY_FACILITY_STATE_UNLOCKED",
            "COMMUNITY_TRUST_UP"
          ],
          "set_flags": [
            "VS1_RECOVERY_PRIORITY_CARE"
          ]
        },
        {
          "id": "VS1_CHOICE_RECOVERY_REPAIR",
          "value": "REPAIR",
          "effects": [
            "WORKSHOP_IMPROVEMENT_UNLOCKED",
            "MATERIAL_THROUGHPUT_UP"
          ],
          "set_flags": [
            "VS1_RECOVERY_PRIORITY_REPAIR"
          ]
        },
        {
          "id": "VS1_CHOICE_RECOVERY_COORDINATION",
          "value": "COORDINATION",
          "effects": [
            "EXPEDITION_BOARD_UNLOCKED",
            "RECOVERY_FACILITY_BASIC"
          ],
          "set_flags": [
            "VS1_RECOVERY_PRIORITY_COORDINATION"
          ]
        }
      ],
      "set_flags": [
        "VS1_COMMUNITY_LEADERSHIP_OFFERED"
      ],
      "next_quest_id": "VS1_Q10"
    },
    {
      "id": "VS1_Q10",
      "title": "A Place That Must Continue",
      "type": [
        "Main",
        "Leadership",
        "Management"
      ],
      "location_id": "LOC_VS1_BRACKENFORD",
      "prerequisites": [
        "VS1_Q09_COMPLETE"
      ],
      "objectives": [
        "Accept accountable community leadership",
        "Choose one initial facility",
        "Assign First Ally to a starter task"
      ],
      "choices": [
        {
          "id": "VS1_CHOICE_FACILITY_RECOVERY",
          "facility_id": "FAC_VS1_RECOVERY_ROOM",
          "set_flags": [
            "FAC_VS1_RECOVERY_ROOM_BUILT"
          ]
        },
        {
          "id": "VS1_CHOICE_FACILITY_WORKSHOP",
          "facility_id": "FAC_VS1_COMMON_WORKSHOP",
          "set_flags": [
            "FAC_VS1_COMMON_WORKSHOP_BUILT"
          ]
        },
        {
          "id": "VS1_CHOICE_FACILITY_COORDINATION",
          "facility_id": "FAC_VS1_COORDINATION_BOARD",
          "set_flags": [
            "FAC_VS1_COORDINATION_BOARD_BUILT"
          ]
        }
      ],
      "set_flags": [
        "ACT_I_COMPLETE",
        "VS1_ALYA_RECOGNIZED_LEADER"
      ],
      "conditional_flags": [
        {
          "if_all": [
            "VS1_RECOVERY_PRIORITY_CARE"
          ],
          "set": [
            "VS1_CUIDADORA_RECRUITED"
          ]
        },
        {
          "if_all": [
            "FAC_VS1_RECOVERY_ROOM_BUILT"
          ],
          "set": [
            "VS1_CUIDADORA_RECRUITED"
          ]
        }
      ],
      "next_quest_id": "VS1_Q11"
    },
    {
      "id": "VS1_Q11",
      "title": "First Delegation",
      "type": [
        "Management",
        "ExpeditionTutorial"
      ],
      "location_id": "LOC_VS1_BRACKENFORD",
      "prerequisites": [
        "ACT_I_COMPLETE"
      ],
      "objectives": [
        "Assign an eligible community member",
        "Launch the upper route survey",
        "Receive and review the autonomous result"
      ],
      "expedition_id": "EXP_VS1_UPPER_ROUTE_SURVEY",
      "set_flags_on_launch": [
        "VS1_FIRST_EXPEDITION_LAUNCHED"
      ],
      "set_flags_on_resolution": [
        "VS1_FIRST_EXPEDITION_RESOLVED"
      ],
      "completion_condition": "Player has seen the result and its community impact."
    }
  ],
  "starting_state": {
    "party": [
      "ALYA",
      "ALLY-001"
    ],
    "resources": [
      {
        "resource_id": "RESOURCE_TIMBER",
        "quantity": 2
      },
      {
        "resource_id": "RESOURCE_FIBER",
        "quantity": 2
      },
      {
        "resource_id": "RESOURCE_BOTANICAL_EXTRACT",
        "quantity": 0
      },
      {
        "resource_id": "RESOURCE_GOLD",
        "quantity": 6
      }
    ],
    "unique_resources": [
      {
        "item_id": "ITEM_VS1_SEED_RESERVE",
        "state": "Present"
      }
    ],
    "mandatory_material_policy": "Optional crafting cannot consume materials reserved for VS1_Q07. If the player chose to close the gate, an additional guaranteed Timber reward from ENC_VS1_01_HUSKS covers the extra repair cost. Fiber from ENC_VS1_02_THREADLINGS has a guaranteed minimum of one."
  },
  "effect_catalog_ref": "data/vertical_slice/act_i_effects.json"
}

```

## Embedded source: Act I structured content

```json
{"schema_version":"1.0.0","content_pack_id":"CONTENT_PACK_VS1_ACT_I","status":"content_design_baseline_provisional_numbers","numeric_policy":"Enemy values, costs, durations, and rewards are authoring baselines. Runtime integration and balance QA remain pending.","resources":[{"id":"RESOURCE_TIMBER","canonical_name":"Timber","family":"CommonMaterial","sources":["Quest","Encounter","Expedition"],"sinks":["FAC_VS1_COMMON_WORKSHOP","VS1_Q07_REPAIR"],"slice_role":"Repairing the diversion and workshop"},{"id":"RESOURCE_FIBER","canonical_name":"Fiber","family":"CommonMaterial","sources":["Exploration","Encounter","Expedition"],"sinks":["VS1_Q04_TEMP_DIVERSION","VS1_Q07_REPAIR"],"slice_role":"Filter material and repair bindings"},{"id":"RESOURCE_BOTANICAL_EXTRACT","canonical_name":"Botanical Extract","family":"SpecialMaterial","sources":["Quest","Gathering"],"sinks":["ITEM_VS1_SOOTHING_TONIC"],"slice_role":"Recovery preparation"},{"id":"RESOURCE_GOLD","canonical_name":"Gold","family":"Currency","sources":["Quest","Trade"],"sinks":["Vendor"],"slice_role":"Small-scale trade and optional supplies"}],"locations":[{"id":"LOC_VS1_BRACKENFORD","name":"Brackenford","kind":"Settlement","region_profile":"Settlement","ecology_state":"Disturbed","tags":["Hub","Community","WaterScarcity"],"connections":["LOC_VS1_ASHFEN_VERGE"]},{"id":"LOC_VS1_ASHFEN_VERGE","name":"Ashfen Verge","kind":"Region","region_profile":"WildGrowth","ecology_state":"Disturbed","tags":["Exploration","FeridaManifestation"],"connections":["LOC_VS1_BRACKENFORD"],"points_of_interest":["POI_VS1_SILT_PATH","POI_VS1_OLD_WEIR","POI_VS1_ROOT_VAULT"]},{"id":"POI_VS1_SILT_PATH","name":"Silt Path","kind":"ExplorationPoint","encounters":["ENC_VS1_01_HUSKS","ENC_VS1_02_THREADLINGS"]},{"id":"POI_VS1_OLD_WEIR","name":"Old Weir","kind":"StoryPoint","encounters":[]},{"id":"POI_VS1_ROOT_VAULT","name":"Root-Vault Sluice","kind":"ClimaxPoint","encounters":["ENC_VS1_03_HOLLOW_WARDEN","ENC_VS1_04_ROOT_VAULT"]}],"enemy_archetypes":[{"id":"ENEMY_VS1_FRAYED_HUSK","name":"Frayed Husk","family":"FeridaTouchedGrowth","encounter_role":"BasicPressure","provisional_stats":{"Body":32,"Agility":24,"Soul":18,"Charm":8,"Dominance":18,"Submission":8,"Sadism":18,"Masochism":16},"provisional_meters":{"vitality_cap":34,"strain_threshold":28},"behavior_profile":"AI_VS1_HUSK","intent_visibility":"VisibleAfterFirstEncounter","tags":["FeridaTouched","RootBound","Basic"],"drops":[{"resource_id":"RESOURCE_FIBER","min":0,"max":1,"chance":0.35}],"design_note":"Slow direct pressure; establishes basic target selection."},{"id":"ENEMY_VS1_THREADLING","name":"Threadling Swarm","family":"FeridaTouchedGrowth","encounter_role":"StrainPressure","provisional_stats":{"Body":20,"Agility":42,"Soul":28,"Charm":10,"Dominance":22,"Submission":12,"Sadism":26,"Masochism":18},"provisional_meters":{"vitality_cap":24,"strain_threshold":22},"behavior_profile":"AI_VS1_THREADLING","intent_visibility":"VisibleAfterFirstEncounter","tags":["FeridaTouched","Swarm","StrainPressure"],"drops":[{"resource_id":"RESOURCE_FIBER","min":0,"max":1,"chance":0.45}],"design_note":"Fragile but quick; pressures Strain or applies a brief pressure effect."},{"id":"ENEMY_VS1_HOLLOW_WARDEN","name":"Hollow Warden","family":"FeridaTouchedGrowth","encounter_role":"EliteGuard","provisional_stats":{"Body":48,"Agility":28,"Soul":42,"Charm":12,"Dominance":34,"Submission":16,"Sadism":32,"Masochism":30},"provisional_meters":{"vitality_cap":58,"strain_threshold":42},"behavior_profile":"AI_VS1_WARDEN","intent_visibility":"VisibleAfterFirstEncounter","tags":["FeridaTouched","Elite","Guard","Resistant"],"drops":[{"resource_id":"RESOURCE_FIBER","min":1,"max":2,"chance":1}],"design_note":"Defensive guard that protects the root-vault; teaches defense/control and readable intent."},{"id":"ENEMY_VS1_ROOT_KNOT","name":"Root-Knot Anchor","family":"FeridaManifestation","encounter_role":"ObjectiveEntity","provisional_stats":{"Body":40,"Agility":8,"Soul":55,"Charm":8,"Dominance":40,"Submission":18,"Sadism":28,"Masochism":38},"provisional_meters":{"vitality_cap":50,"strain_threshold":50},"behavior_profile":"AI_VS1_ROOT_KNOT","intent_visibility":"Telegraphed","tags":["FeridaManifestation","Objective","RootBound"],"drops":[{"resource_id":"RESOURCE_BOTANICAL_EXTRACT","min":1,"max":1,"chance":0.5}],"design_note":"Its presence drives the objective clock/pressure. Defeating it alone is not victory until the sluice objective is complete."}],"encounters":[{"id":"ENC_VS1_01_HUSKS","category":["Combat","Tutorial"],"location_id":"POI_VS1_SILT_PATH","composition":[{"enemy_id":"ENEMY_VS1_FRAYED_HUSK","count":2}],"objective":"Defeat or disable threats","retreat_allowed":true,"reward":{"RESOURCE_FIBER":{"min":0,"max":1},"RESOURCE_GOLD":{"min":2,"max":4},"RESOURCE_TIMBER":{"min":1,"max":1}},"expected_party":["ALYA","ALLY-001"]},{"id":"ENC_VS1_02_THREADLINGS","category":["Combat","Ecological"],"location_id":"POI_VS1_SILT_PATH","composition":[{"enemy_id":"ENEMY_VS1_THREADLING","count":2},{"enemy_id":"ENEMY_VS1_FRAYED_HUSK","count":1}],"objective":"Defeat or disable threats","retreat_allowed":true,"reward":{"RESOURCE_FIBER":{"min":1,"max":2}},"expected_party":["ALYA","ALLY-001"]},{"id":"ENC_VS1_03_HOLLOW_WARDEN","category":["Combat","Elite","Preparation"],"location_id":"POI_VS1_ROOT_VAULT","composition":[{"enemy_id":"ENEMY_VS1_HOLLOW_WARDEN","count":1}],"objective":"Clear the guard and secure filter access","retreat_allowed":true,"reward":{"RESOURCE_FIBER":{"min":1,"max":2},"RESOURCE_BOTANICAL_EXTRACT":{"min":0,"max":1}},"expected_party":["ALYA","ALLY-001"],"failure_consequence":"Lose time; return to a safe state; no permanent quest lock."},{"id":"ENC_VS1_04_ROOT_VAULT","category":["Combat","Boss","Objective"],"location_id":"POI_VS1_ROOT_VAULT","composition":[{"enemy_id":"ENEMY_VS1_HOLLOW_WARDEN","count":1},{"enemy_id":"ENEMY_VS1_ROOT_KNOT","count":1},{"enemy_id":"ENEMY_VS1_THREADLING","count":1}],"objective_steps":["VS1_OBJ_STABILIZE_DIVERSION","VS1_OBJ_SEVER_FILAMENT","VS1_OBJ_SECURE_GATE"],"objective_progress_rule":"Progress uses explicit action/objective checks; no grid or range. Community contribution reduces one requirement or one pressure source.","retreat_allowed":true,"mandatory_outcomes":["VS1_DOWNSTREAM_CHANNEL_SECURED","VS1_SEED_RESERVE_LOST"],"reward":{"RESOURCE_GOLD":{"min":8,"max":12},"RESOURCE_BOTANICAL_EXTRACT":{"min":1,"max":1},"RESOURCE_TIMBER":{"min":2,"max":2},"RESOURCE_FIBER":{"min":1,"max":1}}}],"items":[{"id":"ITEM_VS1_FILTER_FIBER","name":"Filtered Root-Fiber","kind":"QuestMaterial","stack_limit":10,"consumable":false,"sources":["VS1_DISCOVERY_CHANNEL_SAMPLE","ENC_VS1_02_THREADLINGS","EXP_VS1_UPPER_ROUTE_SURVEY"],"sinks":["VS1_Q07"],"description":"A cleaned filament sample used to prepare the staged diversion."},{"id":"ITEM_VS1_SOOTHING_TONIC","name":"Soothing Tonic","kind":"Consumable","stack_limit":5,"consumable":true,"effects":[{"type":"ModifyMeter","meter":"Vitality","operation":"Restore","amount":12}],"craft_inputs":[{"resource_id":"RESOURCE_BOTANICAL_EXTRACT","quantity":1},{"resource_id":"RESOURCE_FIBER","quantity":1}],"description":"A modest recovery item; provisional effect value pending runtime balance."},{"id":"ITEM_VS1_REPAIR_BUNDLE","name":"Sluice Repair Bundle","kind":"QuestMaterial","stack_limit":5,"consumable":true,"effects":[{"type":"QuestProgress","target":"VS1_OBJ_STABILIZE_DIVERSION","amount":1}],"craft_inputs":[{"resource_id":"RESOURCE_TIMBER","quantity":1},{"resource_id":"RESOURCE_FIBER","quantity":1}],"description":"A bundle of timber braces and fiber bindings for the waterworks."},{"id":"ITEM_VS1_SEED_RESERVE","name":"Lower Terrace Seed Reserve","kind":"UniqueResource","stack_limit":1,"consumable":false,"initial_state":"Present","final_state":"Lost","description":"Narrative resource representing the next planting cycle; its loss is mandatory at the climax."}],"facilities":[{"id":"FAC_VS1_RECOVERY_ROOM","name":"Recovery Room","role":"Stability","tier":1,"costs":[{"resource_id":"RESOURCE_TIMBER","quantity":1},{"resource_id":"RESOURCE_FIBER","quantity":1},{"resource_id":"RESOURCE_GOLD","quantity":3}],"outputs":["Recovery access","Cuidadora recruitment eligibility"],"assignment_slots":1,"upgrade_targets":[],"visible_benefit":"Makes recovery support a repeatable community capability."},{"id":"FAC_VS1_COMMON_WORKSHOP","name":"Common Workshop","role":"Conversion","tier":1,"costs":[{"resource_id":"RESOURCE_TIMBER","quantity":2},{"resource_id":"RESOURCE_FIBER","quantity":1}],"processes":[{"process_id":"PROC_VS1_REPAIR_BUNDLE","inputs":[{"resource_id":"RESOURCE_TIMBER","quantity":1},{"resource_id":"RESOURCE_FIBER","quantity":1}],"outputs":[{"item_id":"ITEM_VS1_REPAIR_BUNDLE","quantity":1}],"duration_model":"Immediate","capacity":1}],"assignment_slots":1,"upgrade_targets":[],"visible_benefit":"Converts common materials into repair bundles."},{"id":"FAC_VS1_COORDINATION_BOARD","name":"Coordination Board","role":"Access","tier":1,"costs":[{"resource_id":"RESOURCE_TIMBER","quantity":1},{"resource_id":"RESOURCE_FIBER","quantity":1},{"resource_id":"RESOURCE_GOLD","quantity":2}],"unlocked_capabilities":["CAPABILITY_EXPEDITION_OVERVIEW"],"assignment_slots":0,"upgrade_targets":[],"visible_benefit":"Improves assignment and Expedition visibility; basic autonomous Expeditions remain available after Act I even if this facility is not chosen."}],"expeditions":[{"id":"EXP_VS1_UPPER_ROUTE_SURVEY","name":"Survey the Upper Route","activity_type":"Expedition","region_id":"LOC_VS1_ASHFEN_VERGE","requirements":["ACT_I_COMPLETE","eligible_community_member_available"],"duration_hours":6,"costs":[{"resource_id":"RESOURCE_GOLD","quantity":1}],"assigned_member_unavailable_to_active_party":true,"outcomes":[{"id":"EXP_VS1_OUTCOME_FIBER_CACHE","weight":50,"rewards":[{"resource_id":"RESOURCE_FIBER","quantity":2}],"flags":["VS1_UPPER_ROUTE_MAPPED"]},{"id":"EXP_VS1_OUTCOME_ROUTE_KNOWLEDGE","weight":35,"rewards":[{"resource_id":"RESOURCE_GOLD","quantity":2}],"flags":["VS1_UPPER_ROUTE_MAPPED","VS1_NEXT_REPAIR_COST_REDUCED"]},{"id":"EXP_VS1_OUTCOME_DELAY","weight":15,"rewards":[],"flags":["VS1_EXPEDITION_DELAYED"],"duration_extension_hours":2}],"design_note":"Illustrative initial weights; use the canonical seeded/deterministic resolution and actual time contracts. Expedition resolves without Alya and is not a Sidequest."}],"discoveries":[{"id":"VS1_DISCOVERY_CHANNEL_SAMPLE","location_id":"POI_VS1_SILT_PATH","requirements":["VS1_RED_THREAD_CONFIRMED"],"rewards":[{"item_id":"ITEM_VS1_FILTER_FIBER","quantity":1}],"flags":["VS1_CHANNEL_CLUE_FOUND"],"purpose":"Provides local evidence and unlocks the staged-diversion preparation option."}],"asset_requirements":[{"id":"ASSET_VS1_BRACKENFORD_HUB_BG","kind":"Background","priority":"P0","reuse_candidate":"Existing village/town background","fallback":"Static placeholder"},{"id":"ASSET_VS1_ASHFEN_EXPLORATION_BG","kind":"Background","priority":"P0","reuse_candidate":"Existing forest/ruin background","fallback":"Static placeholder"},{"id":"ASSET_VS1_ROOT_VAULT_BG","kind":"Background","priority":"P0","reuse_candidate":"Existing corrupted ruin background","fallback":"Static placeholder"},{"id":"ASSET_VS1_MARA_PORTRAIT","kind":"Portrait","priority":"P1","fallback":"Generic adult resident portrait"},{"id":"ASSET_VS1_ORG_REP_PORTRAIT","kind":"Portrait","priority":"P1","reuse_candidate":"NPC-006 portrait"},{"id":"ASSET_VS1_PRAGMATIC_MENTOR_PORTRAIT","kind":"Portrait","priority":"P1","reuse_candidate":"NPC-005 portrait"},{"id":"ASSET_VS1_ENEMY_FRAYED_HUSK","kind":"EnemyVisual","priority":"P0","fallback":"Shared corrupted-root placeholder"},{"id":"ASSET_VS1_ENEMY_THREADLING","kind":"EnemyVisual","priority":"P0","fallback":"Small corrupted-growth placeholder"},{"id":"ASSET_VS1_ENEMY_HOLLOW_WARDEN","kind":"EnemyVisual","priority":"P0","fallback":"Armored root-growth placeholder"},{"id":"ASSET_VS1_ENEMY_ROOT_KNOT","kind":"EnemyVisual","priority":"P0","fallback":"Root-anchor illustration"},{"id":"ASSET_VS1_SEED_LOSS_CG","kind":"StoryIllustration","priority":"P2","optional":true,"fallback":"Narrative text plus changed hub background"},{"id":"ASSET_VS1_OPTIONAL_ADULT_CG","kind":"AdultCG","priority":"P3","optional":true,"fallback":"Omit from first playable build"}],"capabilities":[{"id":"CAPABILITY_COMMUNITY_ASSIGNMENTS","scope":"Community","persistence":"Permanent after Act I transition","granted_by":"ACT_I_COMPLETE"},{"id":"CAPABILITY_EXPEDITIONS","scope":"Community","persistence":"Permanent after Act I transition","granted_by":"ACT_I_COMPLETE"},{"id":"CAPABILITY_EXPEDITION_OVERVIEW","scope":"Community","persistence":"Permanent after Coordination Board construction","granted_by":"FAC_VS1_COORDINATION_BOARD"}],"ai_profiles":[{"id":"AI_VS1_HUSK","priority":["Attack highest-priority active target","Use pressure action when available"],"intent":"Telegraphed after the first encounter"},{"id":"AI_VS1_THREADLING","priority":["Apply Strain/pressure to vulnerable target","Otherwise attack"],"intent":"Telegraphed after the first encounter"},{"id":"AI_VS1_WARDEN","priority":["Protect Root-Knot or objective","Use defensive intent when pressure is high","Attack"],"intent":"Always telegraphed"},{"id":"AI_VS1_ROOT_KNOT","priority":["Increase objective pressure","Trigger an eligible spawn/empower effect if its cap allows","Defend"],"intent":"Telegraphed; objective pressure has a deterministic cap"}]}

```

## Embedded source: Act I structured effects

```json
{
  "schema_version": "1.0.0",
  "content_pack_id": "CONTENT_PACK_VS1_ACT_I",
  "status": "content_design_baseline",
  "source_quest_data": "data/vertical_slice/act_i_quests.json",
  "effects": [
    {
      "id": "MARA_TRUST_DOWN",
      "type": "SetState",
      "target": "VS1_MARA_TRUST",
      "value": "LOW"
    },
    {
      "id": "REPAIR_COST_UP",
      "type": "SetFlag",
      "flag": "VS1_REPAIR_SURCHARGE",
      "value": true
    },
    {
      "id": "COMMUNITY_TRUST_UP",
      "type": "SetState",
      "target": "VS1_COMMUNITY_TRUST",
      "value": "HIGH"
    },
    {
      "id": "SUPPLY_BUFFER_DOWN",
      "type": "ModifyResource",
      "resource_id": "RESOURCE_GOLD",
      "operation": "Subtract",
      "quantity": 1
    },
    {
      "id": "CLUE_RELIABILITY_UP",
      "type": "SetFlag",
      "flag": "VS1_INVESTIGATION_CONTEXT",
      "value": "FULL"
    },
    {
      "id": "UPPER_CHANNEL_TEMP_SAFE",
      "type": "SetFlag",
      "flag": "VS1_UPPER_CHANNEL_TEMP_SAFE",
      "value": true
    },
    {
      "id": "LOWER_RESERVE_DRYING",
      "type": "SetFlag",
      "flag": "VS1_LOWER_RESERVE_AT_RISK",
      "value": true
    },
    {
      "id": "TIMBER_REPAIR_COST_PLUS_1",
      "type": "SetFlag",
      "flag": "VS1_REPAIR_SURCHARGE",
      "value": true
    },
    {
      "id": "LOWER_CHANNEL_ACCESS_PRESERVED",
      "type": "SetFlag",
      "flag": "VS1_LOWER_CHANNEL_ACCESS_PRESERVED",
      "value": true
    },
    {
      "id": "TIME_COST_SMALL",
      "type": "AdvanceGameTime",
      "hours": 1
    },
    {
      "id": "THREAT_PRESSURE_UP",
      "type": "SetFlag",
      "flag": "VS1_EXTRA_THREADLING_CLIMAX",
      "value": true
    },
    {
      "id": "INSTITUTIONAL_TRUST_UP",
      "type": "SetState",
      "target": "VS1_ORG_TRUST",
      "value": "HIGH"
    },
    {
      "id": "PREPARATION_ITEM_GRANTED",
      "type": "GrantItem",
      "item_id": "ITEM_VS1_SOOTHING_TONIC",
      "quantity": 1
    },
    {
      "id": "LOWER_RESIDENT_SUPPORT_COST_UP",
      "type": "SetFlag",
      "flag": "VS1_RESIDENT_SUPPORT_COST_UP",
      "value": true
    },
    {
      "id": "INSTITUTIONAL_TRUST_DOWN",
      "type": "SetState",
      "target": "VS1_ORG_TRUST",
      "value": "LOW"
    },
    {
      "id": "EVIDENCE_REQUESTED",
      "type": "SetFlag",
      "flag": "VS1_ORG_REQUIRES_EVIDENCE",
      "value": true
    },
    {
      "id": "THIRD_SOLUTION_ROUTE_OPEN",
      "type": "SetFlag",
      "flag": "VS1_THIRD_SOLUTION_ROUTE_OPEN",
      "value": true
    },
    {
      "id": "CLIMAX_PRESSURE_DOWN",
      "type": "EncounterModifier",
      "target": "ENC_VS1_04_ROOT_VAULT",
      "modifier": "RemoveOneThreadling"
    },
    {
      "id": "OBJECTIVE_DEFENSE_STEPS_PLUS_1",
      "type": "ModifyObjectiveRequirement",
      "target": "VS1_OBJ_STABILIZE_DIVERSION",
      "operation": "Add",
      "quantity": 1
    },
    {
      "id": "CLIMAX_SPREAD_PRESSURE_DOWN",
      "type": "EncounterModifier",
      "target": "ENC_VS1_04_ROOT_VAULT",
      "modifier": "ReduceRootKnotPressureFrequency",
      "value": "ONE_STEP"
    },
    {
      "id": "RECOVERY_DURATION_UP",
      "type": "SetFlag",
      "flag": "VS1_RECOVERY_DURATION",
      "value": "EXTENDED"
    },
    {
      "id": "RECOVERY_DURATION_DOWN",
      "type": "SetFlag",
      "flag": "VS1_RECOVERY_DURATION",
      "value": "STANDARD"
    },
    {
      "id": "RECOVERY_FACILITY_STATE_UNLOCKED",
      "type": "UnlockFacilityState",
      "facility_id": "FAC_VS1_RECOVERY_ROOM"
    },
    {
      "id": "WORKSHOP_IMPROVEMENT_UNLOCKED",
      "type": "UnlockFacilityState",
      "facility_id": "FAC_VS1_COMMON_WORKSHOP"
    },
    {
      "id": "MATERIAL_THROUGHPUT_UP",
      "type": "SetFlag",
      "flag": "VS1_WORKSHOP_THROUGHPUT",
      "value": "IMPROVED"
    },
    {
      "id": "EXPEDITION_BOARD_UNLOCKED",
      "type": "UnlockFacilityState",
      "facility_id": "FAC_VS1_COORDINATION_BOARD"
    },
    {
      "id": "RECOVERY_FACILITY_BASIC",
      "type": "SetFlag",
      "flag": "VS1_RECOVERY_ACCESS",
      "value": "BASIC"
    }
  ],
  "conditional_costs": [
    {
      "id": "COST_VS1_GATE_REPAIR_SURCHARGE",
      "quest_id": "VS1_Q07",
      "when": {
        "flag": "VS1_REPAIR_SURCHARGE",
        "equals": true
      },
      "costs": [
        {
          "resource_id": "RESOURCE_TIMBER",
          "quantity": 1
        }
      ]
    },
    {
      "id": "COST_VS1_ORG_SUPPORT",
      "quest_id": "VS1_Q07",
      "when": {
        "flag": "VS1_RESIDENT_SUPPORT_COST_UP",
        "equals": true
      },
      "costs": [
        {
          "resource_id": "RESOURCE_GOLD",
          "quantity": 2
        }
      ]
    }
  ],
  "conditional_encounter_modifiers": [
    {
      "id": "MOD_VS1_WITHDRAWN_PRESSURE",
      "encounter_id": "ENC_VS1_04_ROOT_VAULT",
      "when": {
        "flag": "VS1_EXTRA_THREADLING_CLIMAX",
        "equals": true
      },
      "operation": "AddEnemy",
      "enemy_id": "ENEMY_VS1_THREADLING",
      "quantity": 1
    }
  ],
  "implementation_notes": [
    "These are slice-level effect IDs, not new global effect primitives. Each type must map to the existing deterministic content/effect contracts or a registered handler.",
    "Conditional costs are evaluated before committing the required quest preparation. Required materials cannot be consumed by optional crafting while reserved.",
    "If two encounter modifiers conflict, resolve in declared order: base composition, withdrawal pressure, then preparation mitigation.",
    "The mandatory seed-reserve loss is not affected by these modifiers."
  ]
}

```

## Embedded source: Canonical skill CSV

```csv
id,display_name,legacy_aliases,kind,tier,skill_point_cost,requirements_ref,milestone_gate,family_tags,targeting_ref,resource_costs_ref,generated_resources_ref,conditions_ref,effects_ref,cooldown,chain_rule_ref,threshold_rule_ref,overflow_rule_ref,outcome_interactions_ref,aspect_tags,scaling_ref,presentation_ref
SENSORY_ENHANCEMENT,Sensory Enhancement,,Active,Tier 1,1,REQ_SENSORY_ENHANCEMENT,none,Damage;Debuff,TARGET_SENSORY_ENHANCEMENT,COST_SENSORY_ENHANCEMENT,GEN_SENSORY_ENHANCEMENT,COND_SENSORY_ENHANCEMENT,FX_SENSORY_ENHANCEMENT,0,none,none,none,none,Mind,SCALE_STRAIN_CONTROL,PRES_SENSORY_ENHANCEMENT
MSTRBATE,Mstrbate,,Active,Tier 1,1,REQ_MSTRBATE,none,Recovery;Control,TARGET_MSTRBATE,COST_MSTRBATE,GEN_MSTRBATE,COND_MSTRBATE,FX_MSTRBATE,0,none,none,none,none,Crotch,SCALE_STRAIN_CONTROL,PRES_MSTRBATE
DANCING_MOVES,Dancing Moves,,Active,Tier 1,1,REQ_DANCING_MOVES,none,Mobility;Fortification,TARGET_DANCING_MOVES,COST_DANCING_MOVES,GEN_DANCING_MOVES,COND_DANCING_MOVES,FX_DANCING_MOVES,0,none,none,none,none,All,SCALE_AGILITY_DEFENSE,PRES_DANCING_MOVES
FLIRT,Flirt,,Active,Tier 1,1,REQ_FLIRT,none,Damage;Control,TARGET_FLIRT,COST_FLIRT,GEN_FLIRT,COND_FLIRT,FX_FLIRT,0,none,none,none,none,Mouth,SCALE_CHARM_SKILL_COMMAND,PRES_FLIRT
HYPNOTIZE,Hypnotize,,Active,Tier 1,1,REQ_HYPNOTIZE,none,Control,TARGET_HYPNOTIZE,COST_HYPNOTIZE,GEN_HYPNOTIZE,COND_HYPNOTIZE,FX_HYPNOTIZE,0,none,none,none,none,Mind,SCALE_SOUL_CONTROL,PRES_HYPNOTIZE
GET_SPANKED,Get Spanked,,Active,Tier 1,1,REQ_GET_SPANKED,none,Reactive;Resource,TARGET_GET_SPANKED,COST_GET_SPANKED,GEN_GET_SPANKED,COND_GET_SPANKED,FX_GET_SPANKED,0,none,none,none,none,Ass,SCALE_RESOLVE_RISK,PRES_GET_SPANKED
SENSORY_DEPRIVATION,Sensory Deprivation,,Active,Tier 1,1,REQ_SENSORY_DEPRIVATION,none,Debuff;Control,TARGET_SENSORY_DEPRIVATION,COST_SENSORY_DEPRIVATION,GEN_SENSORY_DEPRIVATION,COND_SENSORY_DEPRIVATION,FX_SENSORY_DEPRIVATION,0,none,none,none,none,Mind,SCALE_SOUL_CONTROL,PRES_SENSORY_DEPRIVATION
SPANK,Spank,,Active,Tier 1,1,REQ_SPANK,none,Damage,TARGET_SPANK,COST_SPANK,GEN_SPANK,COND_SPANK,FX_SPANK,0,none,none,none,none,Ass,SCALE_STRAIN_ATTACK,PRES_SPANK
INSTILL_PROTECTIVENESS,Instill Protectiveness,,Active,Tier 1,1,REQ_INSTILL_PROTECTIVENESS,none,Support;Control,TARGET_INSTILL_PROTECTIVENESS,COST_INSTILL_PROTECTIVENESS,GEN_INSTILL_PROTECTIVENESS,COND_INSTILL_PROTECTIVENESS,FX_INSTILL_PROTECTIVENESS,0,none,none,none,none,All,SCALE_CHARM_SKILL_COMMAND,PRES_INSTILL_PROTECTIVENESS
BLOWJOB,Bl-job,,Active,Tier 1,1,REQ_BLOWJOB,none,Damage,TARGET_BLOWJOB,COST_BLOWJOB,GEN_BLOWJOB,COND_BLOWJOB,FX_BLOWJOB,0,none,none,none,none,Mouth,SCALE_STRAIN_ATTACK,PRES_BLOWJOB
LAY,Lay,,Active,Tier 1,1,REQ_LAY,none,Damage,TARGET_LAY,COST_LAY,GEN_LAY,COND_LAY,FX_LAY,0,none,none,none,none,Crotch,SCALE_STRAIN_ATTACK,PRES_LAY
GROPE,Grope,,Active,Tier 1,1,REQ_GROPE,none,Damage,TARGET_GROPE,COST_GROPE,GEN_GROPE,COND_GROPE,FX_GROPE,0,none,none,none,none,Ass;Breasts,SCALE_STRAIN_ATTACK,PRES_GROPE
SERVICE,Service,,Active,Tier 1,1,REQ_SERVICE,none,Recovery;Support,TARGET_SERVICE,COST_SERVICE,GEN_SERVICE,COND_SERVICE,FX_SERVICE,0,none,none,none,none,Mouth,SCALE_SUPPORT_RECOVERY,PRES_SERVICE
H_JOB,H-job,,Active,Tier 1,1,REQ_H_JOB,none,Damage;DoT,TARGET_H_JOB,COST_H_JOB,GEN_H_JOB,COND_H_JOB,FX_H_JOB,0,none,none,none,none,Mind,SCALE_SOUL_DOT,PRES_H_JOB
BEND,Bend,,Active,Tier 1,1,REQ_BEND,none,Damage;DoT,TARGET_BEND,COST_BEND,GEN_BEND,COND_BEND,FX_BEND,0,none,none,none,none,Ass,SCALE_STRAIN_ATTACK,PRES_BEND
AS_CHAIN,AS,,Active,Tier 1,1,REQ_AS_CHAIN,none,Damage;DoT;Chain,TARGET_AS_CHAIN,COST_AS_CHAIN,GEN_AS_CHAIN,COND_AS_CHAIN,FX_AS_CHAIN,0,CHAIN_AS_CHAIN,none,none,none,Ass,SCALE_STRAIN_ATTACK,PRES_AS_CHAIN
S_SYMBOL,S Symbol,,Passive,Tier 1,1,REQ_S_SYMBOL,none,Overflow;Recovery,TARGET_S_SYMBOL,COST_S_SYMBOL,GEN_S_SYMBOL,COND_S_SYMBOL,FX_S_SYMBOL,0,none,none,OVERFLOW_S_SYMBOL,none,All,SCALE_SOUL_OVERFLOW,PRES_S_SYMBOL
OTHERWORLDLY_CHARM,Otherworldly Charm,,Passive,Tier 1,1,REQ_OTHERWORLDLY_CHARM,none,Control,TARGET_OTHERWORLDLY_CHARM,COST_OTHERWORLDLY_CHARM,GEN_OTHERWORLDLY_CHARM,COND_OTHERWORLDLY_CHARM,FX_OTHERWORLDLY_CHARM,0,none,none,none,none,All,SCALE_CHARM_SKILL_COMMAND,PRES_OTHERWORLDLY_CHARM
PIERCING_STARES,Piercing Stares,,Passive,Tier 1,1,REQ_PIERCING_STARES,none,Damage;Conditional,TARGET_PIERCING_STARES,COST_PIERCING_STARES,GEN_PIERCING_STARES,COND_PIERCING_STARES,FX_PIERCING_STARES,0,none,none,none,none,Breasts,SCALE_STRAIN_ATTACK,PRES_PIERCING_STARES
SADISM,Sadism,,Passive,Tier 1,1,REQ_SADISM,none,Damage;BuildPassive,TARGET_SADISM,COST_SADISM,GEN_SADISM,COND_SADISM,FX_SADISM,0,none,none,none,none,Crotch;Mouth,SCALE_VITALITY_ATTACK,PRES_SADISM
MASOCHISM,Masochism,,Passive,Tier 1,1,REQ_MASOCHISM,none,Fortification;BuildPassive,TARGET_MASOCHISM,COST_MASOCHISM,GEN_MASOCHISM,COND_MASOCHISM,FX_MASOCHISM,0,none,none,none,none,Ass;Breasts,SCALE_AGILITY_DEFENSE,PRES_MASOCHISM
MOANS,Moans,,Passive,Tier 1,1,REQ_MOANS,none,Reactive,TARGET_MOANS,COST_MOANS,GEN_MOANS,COND_MOANS,FX_MOANS,0,none,none,none,none,Mouth,SCALE_STRAIN_CONTROL,PRES_MOANS
ENCOURAGE,Encourage,,Active,Tier 2,2,REQ_ENCOURAGE,ACT_I_COMPLETE,Support;Buff,TARGET_ENCOURAGE,COST_ENCOURAGE,GEN_ENCOURAGE,COND_ENCOURAGE,FX_ENCOURAGE,0,none,none,none,none,Ass,SCALE_SUPPORT_RECOVERY,PRES_ENCOURAGE
FLAUNT,Flaunt,,Active,Tier 2,2,REQ_FLAUNT,ACT_I_COMPLETE,Damage;AoE,TARGET_FLAUNT,COST_FLAUNT,GEN_FLAUNT,COND_FLAUNT,FX_FLAUNT,1,none,none,none,none,All,SCALE_AREA_STRAIN,PRES_FLAUNT
AUTOF,Autof,,Active,Tier 2,2,REQ_AUTOF,ACT_I_COMPLETE,Recovery;Capability,TARGET_AUTOF,COST_AUTOF,GEN_AUTOF,COND_AUTOF,FX_AUTOF,0,none,none,none,none,Breasts;Crotch;Mouth,SCALE_SUPPORT_RECOVERY,PRES_AUTOF
APHRODISIAC,Aphrodisiac,,Active,Tier 2,2,REQ_APHRODISIAC,ACT_I_COMPLETE,Damage;DoT;Control,TARGET_APHRODISIAC,COST_APHRODISIAC,GEN_APHRODISIAC,COND_APHRODISIAC,FX_APHRODISIAC,0,none,none,none,none,Mind,SCALE_SOUL_DOT,PRES_APHRODISIAC
P_GROWTH,P-growth,,Capability/Transformation,Tier 2,2,REQ_P_GROWTH,ACT_I_COMPLETE,Capability,TARGET_P_GROWTH,COST_P_GROWTH,GEN_P_GROWTH,COND_P_GROWTH,FX_P_GROWTH,0,none,none,none,none,Crotch;Mind,SCALE_CAPABILITY,PRES_P_GROWTH
FACESIT,Facesit,,Active,Tier 2,2,REQ_FACESIT,ACT_I_COMPLETE,Damage,TARGET_FACESIT,COST_FACESIT,GEN_FACESIT,COND_FACESIT,FX_FACESIT,0,none,none,none,none,Crotch,SCALE_STRAIN_ATTACK,PRES_FACESIT
BONDAGE,Bondage,,Active,Tier 2,2,REQ_BONDAGE,ACT_I_COMPLETE,HighRisk;Buff,TARGET_BONDAGE,COST_BONDAGE,GEN_BONDAGE,COND_BONDAGE,FX_BONDAGE,0,none,none,none,none,All,SCALE_RESOLVE_RISK,PRES_BONDAGE
BULLY,Bully,,Active,Tier 2,2,REQ_BULLY,ACT_I_COMPLETE,Debuff,TARGET_BULLY,COST_BULLY,GEN_BULLY,COND_BULLY,FX_BULLY,0,none,none,none,none,Mouth,SCALE_CHARM_SKILL_COMMAND,PRES_BULLY
BITE,Bite,,Active,Tier 2,2,REQ_BITE,ACT_I_COMPLETE,Damage,TARGET_BITE,COST_BITE,GEN_BITE,COND_BITE,FX_BITE,0,none,none,none,none,Mouth,SCALE_VITALITY_ATTACK,PRES_BITE
BIND,Bind,,Active,Tier 2,2,REQ_BIND,ACT_I_COMPLETE,Control;Debuff,TARGET_BIND,COST_BIND,GEN_BIND,COND_BIND,FX_BIND,0,none,none,none,none,Mind,SCALE_SOUL_CONTROL,PRES_BIND
PROLONGED_PL,Prolonged Pl-,,Active,Tier 2,2,REQ_PROLONGED_PL,ACT_I_COMPLETE,Threshold;Control,TARGET_PROLONGED_PL,COST_PROLONGED_PL,GEN_PROLONGED_PL,COND_PROLONGED_PL,FX_PROLONGED_PL,0,none,none,OVERFLOW_LOCK_PROLONGED_PL,none,Crotch,SCALE_SOUL_CONTROL,PRES_PROLONGED_PL
F_FK,F-fk,,Active,Tier 2,2,REQ_F_FK,ACT_I_COMPLETE,Damage;Capability,TARGET_F_FK,COST_F_FK,GEN_F_FK,COND_F_FK,FX_F_FK,0,none,none,none,none,Crotch,SCALE_STRAIN_ATTACK,PRES_F_FK
PAIZURI,Paizuri,,Active,Tier 2,2,REQ_PAIZURI,ACT_I_COMPLETE,Damage,TARGET_PAIZURI,COST_PAIZURI,GEN_PAIZURI,COND_PAIZURI,FX_PAIZURI,0,none,none,none,none,Breasts,SCALE_STRAIN_ATTACK,PRES_PAIZURI
SUMMON_CS,Summon c-s,,Active,Tier 2,2,REQ_SUMMON_CS,ACT_I_COMPLETE,Damage;AoE;HighRisk,TARGET_SUMMON_CS,COST_SUMMON_CS,GEN_SUMMON_CS,COND_SUMMON_CS,FX_SUMMON_CS,2,none,none,none,none,Mind,SCALE_AREA_STRAIN,PRES_SUMMON_CS
SWALLOW,Swallow,,Active,Tier 2,2,REQ_SWALLOW,ACT_I_COMPLETE,Finisher;Outcome,TARGET_SWALLOW,COST_SWALLOW,GEN_SWALLOW,COND_SWALLOW,FX_SWALLOW,3,none,THRESHOLD_SWALLOW,none,OUTCOME_SWALLOW,Mouth,SCALE_FINISHER,PRES_SWALLOW
EXTRA_TIPS,Extra tips,,Passive,Tier 2,2,REQ_EXTRA_TIPS,ACT_I_COMPLETE,Economy;Conditional,TARGET_EXTRA_TIPS,COST_EXTRA_TIPS,GEN_EXTRA_TIPS,COND_EXTRA_TIPS,FX_EXTRA_TIPS,0,none,none,none,none,Mind,SCALE_CHARM_SKILL_COMMAND,PRES_EXTRA_TIPS
CUTENESS,Cuteness,,Passive,Tier 2,2,REQ_CUTENESS,ACT_I_COMPLETE,Support;BuildPassive,TARGET_CUTENESS,COST_CUTENESS,GEN_CUTENESS,COND_CUTENESS,FX_CUTENESS,0,none,none,none,none,Breasts;Mouth,SCALE_SUPPORT_RECOVERY,PRES_CUTENESS
NAUGHTY_THOUGHTS,Naughty Thoughts,,Passive,Tier 2,2,REQ_NAUGHTY_THOUGHTS,ACT_I_COMPLETE,Damage;BuildPassive,TARGET_NAUGHTY_THOUGHTS,COST_NAUGHTY_THOUGHTS,GEN_NAUGHTY_THOUGHTS,COND_NAUGHTY_THOUGHTS,FX_NAUGHTY_THOUGHTS,0,none,none,none,none,Mind,SCALE_SOUL_DOT,PRES_NAUGHTY_THOUGHTS
C_DRINKER,C-drinker,,Passive,Tier 2,2,REQ_C_DRINKER,ACT_I_COMPLETE,Recovery;Conditional,TARGET_C_DRINKER,COST_C_DRINKER,GEN_C_DRINKER,COND_C_DRINKER,FX_C_DRINKER,0,none,none,none,none,Mind,SCALE_SUPPORT_RECOVERY,PRES_C_DRINKER
STRIP,Strip,,Active,Tier 3,3,REQ_STRIP,ACT_II_COMPLETE,Damage;AoE;Mobility,TARGET_STRIP,COST_STRIP,GEN_STRIP,COND_STRIP,FX_STRIP,2,none,none,none,none,All,SCALE_AREA_STRAIN,PRES_STRIP
PINK_MIST,Pink Mist,,Active,Tier 3,3,REQ_PINK_MIST,ACT_II_COMPLETE,Damage;DoT;AoE;Debuff,TARGET_PINK_MIST,COST_PINK_MIST,GEN_PINK_MIST,COND_PINK_MIST,FX_PINK_MIST,3,none,none,none,none,Mind,SCALE_SOUL_DOT,PRES_PINK_MIST
PENETRATE,Penetrate,,Active,Tier 3,3,REQ_PENETRATE,ACT_II_COMPLETE,Damage;Capability,TARGET_PENETRATE,COST_PENETRATE,GEN_PENETRATE,COND_PENETRATE,FX_PENETRATE,2,none,none,none,none,Crotch,SCALE_STRAIN_ATTACK,PRES_PENETRATE
A_PENETRATION,A-penetration,,Active,Tier 3,3,REQ_A_PENETRATION,ACT_II_COMPLETE,Damage;Control;Capability,TARGET_A_PENETRATION,COST_A_PENETRATION,GEN_A_PENETRATION,COND_A_PENETRATION,FX_A_PENETRATION,2,none,none,none,none,Crotch,SCALE_STRAIN_CONTROL,PRES_A_PENETRATION
STOMP,Stomp,,Active,Tier 3,3,REQ_STOMP,ACT_II_COMPLETE,Damage;Threshold,TARGET_STOMP,COST_STOMP,GEN_STOMP,COND_STOMP,FX_STOMP,2,none,THRESHOLD_STOMP,none,none,Crotch,SCALE_VITALITY_ATTACK,PRES_STOMP
SUMMON_TENTACLES,Summon Tentacles,,Active,Tier 3,3,REQ_SUMMON_TENTACLES,ACT_II_COMPLETE,Damage;AoE;HighRisk,TARGET_SUMMON_TENTACLES,COST_SUMMON_TENTACLES,GEN_SUMMON_TENTACLES,COND_SUMMON_TENTACLES,FX_SUMMON_TENTACLES,3,none,none,none,none,All,SCALE_AREA_STRAIN,PRES_SUMMON_TENTACLES
SKILL_ABSOLUTE_CONTROL,Absolute Control,Enslave,Active,Tier 3,3,REQ_SKILL_ABSOLUTE_CONTROL,ACT_II_COMPLETE,Finisher;Control;Outcome,TARGET_SKILL_ABSOLUTE_CONTROL,COST_SKILL_ABSOLUTE_CONTROL,GEN_SKILL_ABSOLUTE_CONTROL,COND_SKILL_ABSOLUTE_CONTROL,FX_SKILL_ABSOLUTE_CONTROL,4,none,none,none,OUTCOME_SKILL_ABSOLUTE_CONTROL,Mind,SCALE_FINISHER,PRES_SKILL_ABSOLUTE_CONTROL
G_BANG,G-bang,,Active,Tier 3,3,REQ_G_BANG,ACT_II_COMPLETE,Damage;AoE,TARGET_G_BANG,COST_G_BANG,GEN_G_BANG,COND_G_BANG,FX_G_BANG,2,none,none,none,none,All,SCALE_AREA_STRAIN,PRES_G_BANG
BKKAKE,Bkakke,,Active,Tier 3,3,REQ_BKKAKE,ACT_II_COMPLETE,Finisher;AoE;HighRisk;Outcome,TARGET_BKKAKE,COST_BKKAKE,GEN_BKKAKE,COND_BKKAKE,FX_BKKAKE,4,none,THRESHOLD_BKKAKE,none,OUTCOME_BKKAKE,Mouth;Breasts,SCALE_FINISHER,PRES_BKKAKE
DEEPTH,Deepth,,Active,Tier 3,3,REQ_DEEPTH,ACT_II_COMPLETE,Damage,TARGET_DEEPTH,COST_DEEPTH,GEN_DEEPTH,COND_DEEPTH,FX_DEEPTH,2,none,none,none,none,Mouth,SCALE_STRAIN_ATTACK,PRES_DEEPTH
WORSHIP_C,Worship C,,Active,Tier 3,3,REQ_WORSHIP_C,ACT_II_COMPLETE,Control;AoE,TARGET_WORSHIP_C,COST_WORSHIP_C,GEN_WORSHIP_C,COND_WORSHIP_C,FX_WORSHIP_C,2,none,none,none,none,Breasts;Mouth,SCALE_CHARM_SKILL_COMMAND,PRES_WORSHIP_C
ECSTASY_AFTERSHOCKS,Ecstasy Aftershocks,,Passive,Tier 3,3,REQ_ECSTASY_AFTERSHOCKS,ACT_II_COMPLETE,Overflow;Damage;AoE,TARGET_ECSTASY_AFTERSHOCKS,COST_ECSTASY_AFTERSHOCKS,GEN_ECSTASY_AFTERSHOCKS,COND_ECSTASY_AFTERSHOCKS,FX_ECSTASY_AFTERSHOCKS,0,none,none,OVERFLOW_ECSTASY_AFTERSHOCKS,none,All,SCALE_SOUL_OVERFLOW,PRES_ECSTASY_AFTERSHOCKS
DIVINE_HEALTH,Divine Health,,Passive,Tier 3,3,REQ_DIVINE_HEALTH,ACT_II_COMPLETE,Fortification;Support;Conditional,TARGET_DIVINE_HEALTH,COST_DIVINE_HEALTH,GEN_DIVINE_HEALTH,COND_DIVINE_HEALTH,FX_DIVINE_HEALTH,0,none,none,none,none,Mind,SCALE_SUPPORT_RECOVERY,PRES_DIVINE_HEALTH
SKILL_PROVOKE,Provoke,,Active,Tier 1,1,REQ_SKILL_PROVOKE,none,Control,TARGET_SKILL_PROVOKE,COST_SKILL_PROVOKE,GEN_SKILL_PROVOKE,COND_SKILL_PROVOKE,FX_SKILL_PROVOKE,0,none,none,none,none,Mind,SCALE_CHARM_SKILL_COMMAND,PRES_SKILL_PROVOKE
SKILL_ENDURE,Endure,,Active,Tier 1,1,REQ_SKILL_ENDURE,none,Fortification;Reactive,TARGET_SKILL_ENDURE,COST_SKILL_ENDURE,GEN_SKILL_ENDURE,COND_SKILL_ENDURE,FX_SKILL_ENDURE,0,none,none,none,none,All,SCALE_AGILITY_DEFENSE,PRES_SKILL_ENDURE
SKILL_COUNTER,Counter,,Active,Tier 2,2,REQ_SKILL_COUNTER,ACT_I_COMPLETE,Reactive;Damage,TARGET_SKILL_COUNTER,COST_SKILL_COUNTER,GEN_SKILL_COUNTER,COND_SKILL_COUNTER,FX_SKILL_COUNTER,0,none,none,none,none,All,SCALE_AGILITY_DEFENSE,PRES_SKILL_COUNTER
SKILL_COMMAND,Command,,Active,Tier 1,1,REQ_SKILL_COMMAND,none,Control;Resource,TARGET_SKILL_COMMAND,COST_SKILL_COMMAND,GEN_SKILL_COMMAND,COND_SKILL_COMMAND,FX_SKILL_COMMAND,0,none,none,none,none,Mind,SCALE_CHARM_SKILL_COMMAND,PRES_SKILL_COMMAND
SKILL_RECOVER_COMPOSURE,Recover Composure,,Active,Tier 1,1,REQ_SKILL_RECOVER_COMPOSURE,none,Recovery,TARGET_SKILL_RECOVER_COMPOSURE,COST_SKILL_RECOVER_COMPOSURE,GEN_SKILL_RECOVER_COMPOSURE,COND_SKILL_RECOVER_COMPOSURE,FX_SKILL_RECOVER_COMPOSURE,0,none,none,none,none,Mind,SCALE_SUPPORT_RECOVERY,PRES_SKILL_RECOVER_COMPOSURE
SKILL_EXPLOIT_WEAKNESS,Exploit Weakness,,Active,Tier 2,2,REQ_SKILL_EXPLOIT_WEAKNESS,ACT_I_COMPLETE,Exploitation;Resource,TARGET_SKILL_EXPLOIT_WEAKNESS,COST_SKILL_EXPLOIT_WEAKNESS,GEN_SKILL_EXPLOIT_WEAKNESS,COND_SKILL_EXPLOIT_WEAKNESS,FX_SKILL_EXPLOIT_WEAKNESS,0,none,none,none,none,Mind,SCALE_STRAIN_CONTROL,PRES_SKILL_EXPLOIT_WEAKNESS
SKILL_BREAK_RESISTANCE,Break Resistance,,Active,Tier 2,2,REQ_SKILL_BREAK_RESISTANCE,ACT_I_COMPLETE,Control;Debuff,TARGET_SKILL_BREAK_RESISTANCE,COST_SKILL_BREAK_RESISTANCE,GEN_SKILL_BREAK_RESISTANCE,COND_SKILL_BREAK_RESISTANCE,FX_SKILL_BREAK_RESISTANCE,0,none,none,none,none,Mind,SCALE_SOUL_CONTROL,PRES_SKILL_BREAK_RESISTANCE
SKILL_TURN_THE_TABLES,Turn the Tables,,Active,Tier 2,2,REQ_SKILL_TURN_THE_TABLES,ACT_I_COMPLETE,Reactive;Recovery,TARGET_SKILL_TURN_THE_TABLES,COST_SKILL_TURN_THE_TABLES,GEN_SKILL_TURN_THE_TABLES,COND_SKILL_TURN_THE_TABLES,FX_SKILL_TURN_THE_TABLES,0,none,none,none,none,All,SCALE_AGILITY_DEFENSE,PRES_SKILL_TURN_THE_TABLES
SKILL_FOCUS_SURGE,Focus Surge,,Active,Tier 2,2,REQ_SKILL_FOCUS_SURGE,ACT_I_COMPLETE,Buff;Setup,TARGET_SKILL_FOCUS_SURGE,COST_SKILL_FOCUS_SURGE,GEN_SKILL_FOCUS_SURGE,COND_SKILL_FOCUS_SURGE,FX_SKILL_FOCUS_SURGE,0,none,none,none,none,Mind,SCALE_SOUL_DOT,PRES_SKILL_FOCUS_SURGE
SKILL_DIRECT_ALLY,Direct Ally,,Active,Tier 2,2,REQ_SKILL_DIRECT_ALLY,ACT_I_COMPLETE,Support;Buff,TARGET_SKILL_DIRECT_ALLY,COST_SKILL_DIRECT_ALLY,GEN_SKILL_DIRECT_ALLY,COND_SKILL_DIRECT_ALLY,FX_SKILL_DIRECT_ALLY,0,none,none,none,none,Mind,SCALE_CHARM_SKILL_COMMAND,PRES_SKILL_DIRECT_ALLY
SKILL_UNBROKEN,Unbroken,,Passive,Tier 3,3,REQ_SKILL_UNBROKEN,ACT_II_COMPLETE,Fortification;Reactive,TARGET_SKILL_UNBROKEN,COST_SKILL_UNBROKEN,GEN_SKILL_UNBROKEN,COND_SKILL_UNBROKEN,FX_SKILL_UNBROKEN,0,none,none,none,none,All,SCALE_AGILITY_DEFENSE,PRES_SKILL_UNBROKEN
SKILL_OVERFLOW_ENGINE,Overflow Engine,,Active,Tier 3,3,REQ_SKILL_OVERFLOW_ENGINE,ACT_II_COMPLETE,Overflow;Utility,TARGET_SKILL_OVERFLOW_ENGINE,COST_SKILL_OVERFLOW_ENGINE,GEN_SKILL_OVERFLOW_ENGINE,COND_SKILL_OVERFLOW_ENGINE,FX_SKILL_OVERFLOW_ENGINE,3,none,none,OVERFLOW_SKILL_OVERFLOW_ENGINE,none,Mind,SCALE_SOUL_OVERFLOW,PRES_SKILL_OVERFLOW_ENGINE
SKILL_MUTUAL_RUIN,Mutual Ruin,,Active,Tier 3,3,REQ_SKILL_MUTUAL_RUIN,ACT_II_COMPLETE,HighRisk;Damage;Outcome,TARGET_SKILL_MUTUAL_RUIN,COST_SKILL_MUTUAL_RUIN,GEN_SKILL_MUTUAL_RUIN,COND_SKILL_MUTUAL_RUIN,FX_SKILL_MUTUAL_RUIN,4,none,none,none,none,All,SCALE_VITALITY_ATTACK,PRES_SKILL_MUTUAL_RUIN

```

## Embedded source: Full normalized skill definitions

```json
{
  "schema_version": "1.0.0",
  "catalog_version": "1.0.0-provisional",
  "status": "normalized_candidate_requires_runtime_integration_and_encounter_balance_QA",
  "source": "data/skills/skills.csv",
  "numeric_policy": {
    "all_numbers_provisional": true,
    "aspect_affinity": "after weighted primary attributes: clamp(1 + affinity_percent/200, 1.0, 1.5)",
    "dot": "tick at affected target start of turn; decrement after tick; refresh max remaining/new; strongest equivalent only",
    "overflow": "once per affected actor per resolved action on threshold crossing; recursion guard; lock removal re-evaluates threshold",
    "action_economy": "one action point per Active skill; no extra actions",
    "p_growth": "CAPABILITY_P_GROWTH is Alya-only; validate before costs commit",
    "finishers": "encounter-permitted outcomes only; no implicit Defeat/global victory"
  },
  "progression": {
    "skill_points": {
      "Tier1": 1,
      "Tier2": 2,
      "Tier3": 3
    },
    "tier_gates": {
      "Tier1": "none",
      "Tier2": "ACT_I_COMPLETE",
      "Tier3": "ACT_II_COMPLETE"
    }
  },
  "scaling_profiles": {
    "SCALE_STRAIN_CONTROL": {
      "profile_id": "SCALE_STRAIN_CONTROL",
      "primary_attributes": [
        {
          "attribute": "Charm",
          "weight": 0.35
        },
        {
          "attribute": "Dominance",
          "weight": 0.35
        },
        {
          "attribute": "Soul",
          "weight": 0.3
        }
      ],
      "weighted_attribute_formula": "sum(attribute_value * weight)",
      "aspect_affinity": {
        "mode": "single",
        "aspects": [
          "Mind"
        ],
        "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
      },
      "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
      "base_power": 8,
      "output_cap": 32,
      "rounding": "nearest_integer_halves_away_from_zero",
      "resistance_order": [
        "base",
        "aspect_affinity",
        "target_resistance",
        "vulnerability_and_debuff",
        "cap",
        "meter_mutation"
      ]
    },
    "SCALE_AGILITY_DEFENSE": {
      "profile_id": "SCALE_AGILITY_DEFENSE",
      "primary_attributes": [
        {
          "attribute": "Agility",
          "weight": 0.45
        },
        {
          "attribute": "Body",
          "weight": 0.3
        },
        {
          "attribute": "Masochism",
          "weight": 0.25
        }
      ],
      "weighted_attribute_formula": "sum(attribute_value * weight)",
      "aspect_affinity": {
        "mode": "none",
        "aspects": [],
        "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
      },
      "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
      "base_power": 6,
      "output_cap": 40,
      "rounding": "nearest_integer_halves_away_from_zero",
      "resistance_order": [
        "base",
        "aspect_affinity",
        "target_resistance",
        "vulnerability_and_debuff",
        "cap",
        "meter_mutation"
      ]
    },
    "SCALE_CHARM_SKILL_COMMAND": {
      "profile_id": "SCALE_CHARM_SKILL_COMMAND",
      "primary_attributes": [
        {
          "attribute": "Charm",
          "weight": 0.5
        },
        {
          "attribute": "Dominance",
          "weight": 0.3
        },
        {
          "attribute": "Soul",
          "weight": 0.2
        }
      ],
      "weighted_attribute_formula": "sum(attribute_value * weight)",
      "aspect_affinity": {
        "mode": "single",
        "aspects": [
          "Mind"
        ],
        "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
      },
      "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
      "base_power": 6,
      "output_cap": 32,
      "rounding": "nearest_integer_halves_away_from_zero",
      "resistance_order": [
        "base",
        "aspect_affinity",
        "target_resistance",
        "vulnerability_and_debuff",
        "cap",
        "meter_mutation"
      ]
    },
    "SCALE_SOUL_CONTROL": {
      "profile_id": "SCALE_SOUL_CONTROL",
      "primary_attributes": [
        {
          "attribute": "Soul",
          "weight": 0.55
        },
        {
          "attribute": "Dominance",
          "weight": 0.25
        },
        {
          "attribute": "Charm",
          "weight": 0.2
        }
      ],
      "weighted_attribute_formula": "sum(attribute_value * weight)",
      "aspect_affinity": {
        "mode": "single",
        "aspects": [
          "Mind"
        ],
        "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
      },
      "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
      "base_power": 7,
      "output_cap": 32,
      "rounding": "nearest_integer_halves_away_from_zero",
      "resistance_order": [
        "base",
        "aspect_affinity",
        "target_resistance",
        "vulnerability_and_debuff",
        "cap",
        "meter_mutation"
      ]
    },
    "SCALE_RESOLVE_RISK": {
      "profile_id": "SCALE_RESOLVE_RISK",
      "primary_attributes": [
        {
          "attribute": "Masochism",
          "weight": 0.4
        },
        {
          "attribute": "Submission",
          "weight": 0.35
        },
        {
          "attribute": "Body",
          "weight": 0.25
        }
      ],
      "weighted_attribute_formula": "sum(attribute_value * weight)",
      "aspect_affinity": {
        "mode": "none",
        "aspects": [],
        "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
      },
      "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
      "base_power": 6,
      "output_cap": 32,
      "rounding": "nearest_integer_halves_away_from_zero",
      "resistance_order": [
        "base",
        "aspect_affinity",
        "target_resistance",
        "vulnerability_and_debuff",
        "cap",
        "meter_mutation"
      ]
    },
    "SCALE_STRAIN_ATTACK": {
      "profile_id": "SCALE_STRAIN_ATTACK",
      "primary_attributes": [
        {
          "attribute": "Charm",
          "weight": 0.55
        },
        {
          "attribute": "Dominance",
          "weight": 0.25
        },
        {
          "attribute": "Submission",
          "weight": 0.2
        }
      ],
      "weighted_attribute_formula": "sum(attribute_value * weight)",
      "aspect_affinity": {
        "mode": "single",
        "aspects": [
          "Mouth"
        ],
        "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
      },
      "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
      "base_power": 10,
      "output_cap": 40,
      "rounding": "nearest_integer_halves_away_from_zero",
      "resistance_order": [
        "base",
        "aspect_affinity",
        "target_resistance",
        "vulnerability_and_debuff",
        "cap",
        "meter_mutation"
      ]
    },
    "SCALE_SUPPORT_RECOVERY": {
      "profile_id": "SCALE_SUPPORT_RECOVERY",
      "primary_attributes": [
        {
          "attribute": "Soul",
          "weight": 0.35
        },
        {
          "attribute": "Vitality",
          "weight": 0.35
        },
        {
          "attribute": "Submission",
          "weight": 0.3
        }
      ],
      "weighted_attribute_formula": "sum(attribute_value * weight)",
      "aspect_affinity": {
        "mode": "single",
        "aspects": [
          "Mind"
        ],
        "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
      },
      "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
      "base_power": 8,
      "output_cap": 24,
      "rounding": "nearest_integer_halves_away_from_zero",
      "resistance_order": [
        "base",
        "aspect_affinity",
        "target_resistance",
        "vulnerability_and_debuff",
        "cap",
        "meter_mutation"
      ]
    },
    "SCALE_SOUL_DOT": {
      "profile_id": "SCALE_SOUL_DOT",
      "primary_attributes": [
        {
          "attribute": "Soul",
          "weight": 0.45
        },
        {
          "attribute": "Charm",
          "weight": 0.3
        },
        {
          "attribute": "Dominance",
          "weight": 0.25
        }
      ],
      "weighted_attribute_formula": "sum(attribute_value * weight)",
      "aspect_affinity": {
        "mode": "single",
        "aspects": [
          "Mind"
        ],
        "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
      },
      "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
      "base_power": 5,
      "output_cap": 32,
      "rounding": "nearest_integer_halves_away_from_zero",
      "resistance_order": [
        "base",
        "aspect_affinity",
        "target_resistance",
        "vulnerability_and_debuff",
        "cap",
        "meter_mutation"
      ]
    },
    "SCALE_SOUL_OVERFLOW": {
      "profile_id": "SCALE_SOUL_OVERFLOW",
      "primary_attributes": [
        {
          "attribute": "Soul",
          "weight": 0.45
        },
        {
          "attribute": "Dominance",
          "weight": 0.3
        },
        {
          "attribute": "Masochism",
          "weight": 0.25
        }
      ],
      "weighted_attribute_formula": "sum(attribute_value * weight)",
      "aspect_affinity": {
        "mode": "single",
        "aspects": [
          "Mind"
        ],
        "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
      },
      "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
      "base_power": 6,
      "output_cap": 40,
      "rounding": "nearest_integer_halves_away_from_zero",
      "resistance_order": [
        "base",
        "aspect_affinity",
        "target_resistance",
        "vulnerability_and_debuff",
        "cap",
        "meter_mutation"
      ]
    },
    "SCALE_VITALITY_ATTACK": {
      "profile_id": "SCALE_VITALITY_ATTACK",
      "primary_attributes": [
        {
          "attribute": "Body",
          "weight": 0.45
        },
        {
          "attribute": "Sadism",
          "weight": 0.35
        },
        {
          "attribute": "Agility",
          "weight": 0.2
        }
      ],
      "weighted_attribute_formula": "sum(attribute_value * weight)",
      "aspect_affinity": {
        "mode": "none",
        "aspects": [],
        "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
      },
      "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
      "base_power": 9,
      "output_cap": 40,
      "rounding": "nearest_integer_halves_away_from_zero",
      "resistance_order": [
        "base",
        "aspect_affinity",
        "target_resistance",
        "vulnerability_and_debuff",
        "cap",
        "meter_mutation"
      ]
    },
    "SCALE_AREA_STRAIN": {
      "profile_id": "SCALE_AREA_STRAIN",
      "primary_attributes": [
        {
          "attribute": "Charm",
          "weight": 0.4
        },
        {
          "attribute": "Dominance",
          "weight": 0.35
        },
        {
          "attribute": "Submission",
          "weight": 0.25
        }
      ],
      "weighted_attribute_formula": "sum(attribute_value * weight)",
      "aspect_affinity": {
        "mode": "none",
        "aspects": [],
        "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
      },
      "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
      "base_power": 6,
      "output_cap": 40,
      "rounding": "nearest_integer_halves_away_from_zero",
      "resistance_order": [
        "base",
        "aspect_affinity",
        "target_resistance",
        "vulnerability_and_debuff",
        "cap",
        "meter_mutation"
      ]
    },
    "SCALE_CAPABILITY": {
      "profile_id": "SCALE_CAPABILITY",
      "primary_attributes": [
        {
          "attribute": "Soul",
          "weight": 0.4
        },
        {
          "attribute": "Body",
          "weight": 0.3
        },
        {
          "attribute": "Dominance",
          "weight": 0.3
        }
      ],
      "weighted_attribute_formula": "sum(attribute_value * weight)",
      "aspect_affinity": {
        "mode": "arithmetic_mean",
        "aspects": [
          "Crotch",
          "Mind"
        ],
        "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
      },
      "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
      "base_power": 0,
      "output_cap": 32,
      "rounding": "nearest_integer_halves_away_from_zero",
      "resistance_order": [
        "base",
        "aspect_affinity",
        "target_resistance",
        "vulnerability_and_debuff",
        "cap",
        "meter_mutation"
      ]
    },
    "SCALE_FINISHER": {
      "profile_id": "SCALE_FINISHER",
      "primary_attributes": [
        {
          "attribute": "Dominance",
          "weight": 0.4
        },
        {
          "attribute": "Soul",
          "weight": 0.35
        },
        {
          "attribute": "Charm",
          "weight": 0.25
        }
      ],
      "weighted_attribute_formula": "sum(attribute_value * weight)",
      "aspect_affinity": {
        "mode": "arithmetic_mean",
        "aspects": [
          "Mouth",
          "Breasts"
        ],
        "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
      },
      "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
      "base_power": 12,
      "output_cap": 40,
      "rounding": "nearest_integer_halves_away_from_zero",
      "resistance_order": [
        "base",
        "aspect_affinity",
        "target_resistance",
        "vulnerability_and_debuff",
        "cap",
        "meter_mutation"
      ]
    }
  },
  "skills": {
    "SENSORY_ENHANCEMENT": {
      "id": "SENSORY_ENHANCEMENT",
      "display_name": "Sensory Enhancement",
      "legacy_aliases": [],
      "kind": "Active",
      "tier": "Tier 1",
      "skill_point_cost": 1,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "none",
      "targeting": {
        "ref": "TARGET_SENSORY_ENHANCEMENT",
        "scope": [
          "Enemy"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": true,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 1,
        "resource_costs": {}
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_SENSORY_ENHANCEMENT",
          "template": "vulnerability",
          "ordered_steps": [
            {
              "type": "ApplyEffect",
              "effect_kind": "TaggedVulnerability",
              "tags": [
                "strain_damage",
                "strain_dot"
              ],
              "magnitude": 0.25,
              "duration_turns": 2,
              "refresh": "max_remaining_or_new",
              "stack_policy": "strongest_equivalent_only"
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_STRAIN_CONTROL",
        "primary_attributes": [
          {
            "attribute": "Charm",
            "weight": 0.35
          },
          {
            "attribute": "Dominance",
            "weight": 0.35
          },
          {
            "attribute": "Soul",
            "weight": 0.3
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "single",
          "aspects": [
            "Mind"
          ],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 8,
        "output_cap": 24,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 0,
        "action_cost": 1
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_SENSORY_ENHANCEMENT",
        "display_name": "Sensory Enhancement",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "Tagged vulnerability amplifier; duration 2; +25% qualifying Strain effects"
    },
    "MSTRBATE": {
      "id": "MSTRBATE",
      "display_name": "Mstrbate",
      "legacy_aliases": [],
      "kind": "Active",
      "tier": "Tier 1",
      "skill_point_cost": 1,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "none",
      "targeting": {
        "ref": "TARGET_MSTRBATE",
        "scope": [
          "Enemy",
          "Self"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": false,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 1,
        "resource_costs": {}
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_MSTRBATE",
          "template": "risk_recovery",
          "ordered_steps": [
            {
              "type": "ModifyMeter",
              "meter": "Strain",
              "direction": "restore",
              "amount": 18,
              "target": "self"
            },
            {
              "type": "ChangeIntent",
              "target": "selected_enemy",
              "bias": "StrainOriented",
              "duration_turns": 2
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_STRAIN_CONTROL",
        "primary_attributes": [
          {
            "attribute": "Charm",
            "weight": 0.35
          },
          {
            "attribute": "Dominance",
            "weight": 0.35
          },
          {
            "attribute": "Soul",
            "weight": 0.3
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "single",
          "aspects": [
            "Crotch"
          ],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 8,
        "output_cap": 24,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 0,
        "action_cost": 1
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_MSTRBATE",
        "display_name": "Mstrbate",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "Reduce Alya Strain 18 and bias target toward Strain-oriented intent for 2 turns"
    },
    "DANCING_MOVES": {
      "id": "DANCING_MOVES",
      "display_name": "Dancing Moves",
      "legacy_aliases": [],
      "kind": "Active",
      "tier": "Tier 1",
      "skill_point_cost": 1,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "none",
      "targeting": {
        "ref": "TARGET_DANCING_MOVES",
        "scope": [
          "Self"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": false,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 1,
        "resource_costs": {}
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_DANCING_MOVES",
          "template": "evasion_stance",
          "ordered_steps": [
            {
              "type": "ApplyEffect",
              "effect_kind": "EvasionBonus",
              "magnitude": 25,
              "duration_turns": 1,
              "expires_after": "one_enemy_action",
              "stack_policy": "refresh"
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_AGILITY_DEFENSE",
        "primary_attributes": [
          {
            "attribute": "Agility",
            "weight": 0.45
          },
          {
            "attribute": "Body",
            "weight": 0.3
          },
          {
            "attribute": "Masochism",
            "weight": 0.25
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "none",
          "aspects": [],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 6,
        "output_cap": 24,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 0,
        "action_cost": 1
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_DANCING_MOVES",
        "display_name": "Dancing Moves",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "+25 evasion for 1 enemy action or 1 turn"
    },
    "FLIRT": {
      "id": "FLIRT",
      "display_name": "Flirt",
      "legacy_aliases": [],
      "kind": "Active",
      "tier": "Tier 1",
      "skill_point_cost": 1,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "none",
      "targeting": {
        "ref": "TARGET_FLIRT",
        "scope": [
          "Enemy"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": true,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 1,
        "resource_costs": {}
      },
      "generated_resources": {
        "Command": {
          "amount": 2,
          "cap": 8
        }
      },
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_FLIRT",
          "template": "flirt_hybrid",
          "ordered_steps": [
            {
              "type": "ModifyMeter",
              "meter": "Strain",
              "direction": "damage",
              "formula": "round(base_effectiveness*0.65)",
              "target": "selected_enemy",
              "cap": 14
            },
            {
              "type": "ModifyResource",
              "resource": "Command",
              "direction": "gain",
              "amount": 2,
              "cap": 8
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_CHARM_SKILL_COMMAND",
        "primary_attributes": [
          {
            "attribute": "Charm",
            "weight": 0.5
          },
          {
            "attribute": "Dominance",
            "weight": 0.3
          },
          {
            "attribute": "Soul",
            "weight": 0.2
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "single",
          "aspects": [
            "Mouth"
          ],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 6,
        "output_cap": 24,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 0,
        "action_cost": 1
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_FLIRT",
        "display_name": "Flirt",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "Deal 0.65x Strain and generate 2 Command; below specialized actions"
    },
    "HYPNOTIZE": {
      "id": "HYPNOTIZE",
      "display_name": "Hypnotize",
      "legacy_aliases": [],
      "kind": "Active",
      "tier": "Tier 1",
      "skill_point_cost": 1,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "none",
      "targeting": {
        "ref": "TARGET_HYPNOTIZE",
        "scope": [
          "Enemy"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": true,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 1,
        "resource_costs": {}
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_HYPNOTIZE",
          "template": "intent_control",
          "ordered_steps": [
            {
              "type": "ChangeIntent",
              "target": "selected_enemy",
              "bias": "authored_intent_bias",
              "duration_turns": 1,
              "resistance": "MentalControlResistance"
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_SOUL_CONTROL",
        "primary_attributes": [
          {
            "attribute": "Soul",
            "weight": 0.55
          },
          {
            "attribute": "Dominance",
            "weight": 0.25
          },
          {
            "attribute": "Charm",
            "weight": 0.2
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "single",
          "aspects": [
            "Mind"
          ],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 7,
        "output_cap": 24,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 0,
        "action_cost": 1
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_HYPNOTIZE",
        "display_name": "Hypnotize",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "Resisted intent manipulation for 1 turn; not stun or DoT"
    },
    "GET_SPANKED": {
      "id": "GET_SPANKED",
      "display_name": "Get Spanked",
      "legacy_aliases": [],
      "kind": "Active",
      "tier": "Tier 1",
      "skill_point_cost": 1,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "none",
      "targeting": {
        "ref": "TARGET_GET_SPANKED",
        "scope": [
          "Enemy",
          "Self"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": false,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 1,
        "resource_costs": {}
      },
      "generated_resources": {
        "Resolve": {
          "amount": 2,
          "cap": 4,
          "trigger": "qualifying_incoming_strain_action_resolved"
        }
      },
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_GET_SPANKED",
          "template": "exposure_resolve",
          "ordered_steps": [
            {
              "type": "ApplyEffect",
              "effect_kind": "ExposureWindow",
              "target": "self",
              "trigger": "next_qualifying_incoming_strain_action",
              "max_triggers": 1
            },
            {
              "type": "OnTrigger",
              "event": "QualifyingIncomingStrainActionResolved",
              "effect": {
                "type": "ModifyResource",
                "resource": "Resolve",
                "direction": "gain",
                "amount": 2,
                "cap": 4
              }
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_RESOLVE_RISK",
        "primary_attributes": [
          {
            "attribute": "Masochism",
            "weight": 0.4
          },
          {
            "attribute": "Submission",
            "weight": 0.35
          },
          {
            "attribute": "Body",
            "weight": 0.25
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "single",
          "aspects": [
            "Ass"
          ],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 6,
        "output_cap": 24,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 0,
        "action_cost": 1
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_GET_SPANKED",
        "display_name": "Get Spanked",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "Expose Alya; gain 2 Resolve after qualifying incoming enemy Strain action"
    },
    "SENSORY_DEPRIVATION": {
      "id": "SENSORY_DEPRIVATION",
      "display_name": "Sensory Deprivation",
      "legacy_aliases": [],
      "kind": "Active",
      "tier": "Tier 1",
      "skill_point_cost": 1,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "none",
      "targeting": {
        "ref": "TARGET_SENSORY_DEPRIVATION",
        "scope": [
          "Enemy"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": true,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 1,
        "resource_costs": {}
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_SENSORY_DEPRIVATION",
          "template": "stat_debuff",
          "ordered_steps": [
            {
              "type": "ModifyStat",
              "target": "selected_enemy",
              "stat": "Accuracy",
              "operation": "multiply",
              "value": 0.85,
              "duration_turns": 2
            },
            {
              "type": "ModifyStat",
              "target": "selected_enemy",
              "stat": "Evasion",
              "operation": "multiply",
              "value": 0.85,
              "duration_turns": 2
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_SOUL_CONTROL",
        "primary_attributes": [
          {
            "attribute": "Soul",
            "weight": 0.55
          },
          {
            "attribute": "Dominance",
            "weight": 0.25
          },
          {
            "attribute": "Charm",
            "weight": 0.2
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "single",
          "aspects": [
            "Mind"
          ],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 7,
        "output_cap": 24,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 0,
        "action_cost": 1
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_SENSORY_DEPRIVATION",
        "display_name": "Sensory Deprivation",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "Reduce target accuracy and evasion by 15% for 2 turns"
    },
    "SPANK": {
      "id": "SPANK",
      "display_name": "Spank",
      "legacy_aliases": [],
      "kind": "Active",
      "tier": "Tier 1",
      "skill_point_cost": 1,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "none",
      "targeting": {
        "ref": "TARGET_SPANK",
        "scope": [
          "Enemy"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": true,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 1,
        "resource_costs": {}
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_SPANK",
          "template": "focused_strain",
          "ordered_steps": [
            {
              "type": "ModifyMeter",
              "meter": "Strain",
              "direction": "damage",
              "formula": "base_effectiveness",
              "target": "selected_enemy"
            },
            {
              "type": "ConditionalEffect",
              "condition": "target_has_explicit_vulnerability_tag",
              "effect": {
                "type": "ModifyMeter",
                "meter": "Vitality",
                "direction": "damage",
                "formula": "0.2*base_effectiveness",
                "cap": 4
              }
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_STRAIN_ATTACK",
        "primary_attributes": [
          {
            "attribute": "Charm",
            "weight": 0.55
          },
          {
            "attribute": "Dominance",
            "weight": 0.25
          },
          {
            "attribute": "Submission",
            "weight": 0.2
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "single",
          "aspects": [
            "Ass"
          ],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 10,
        "output_cap": 24,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 0,
        "action_cost": 1
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_SPANK",
        "display_name": "Spank",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "Focused Strain; Vitality rider only against tagged vulnerability"
    },
    "INSTILL_PROTECTIVENESS": {
      "id": "INSTILL_PROTECTIVENESS",
      "display_name": "Instill Protectiveness",
      "legacy_aliases": [],
      "kind": "Active",
      "tier": "Tier 1",
      "skill_point_cost": 1,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "none",
      "targeting": {
        "ref": "TARGET_INSTILL_PROTECTIVENESS",
        "scope": [
          "Ally"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": true,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 1,
        "resource_costs": {}
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_INSTILL_PROTECTIVENESS",
          "template": "protect_ally",
          "ordered_steps": [
            {
              "type": "ChangeIntent",
              "target": "selected_enemy",
              "beneficiary": "selected_ally",
              "bias": "prefer_protected_ally",
              "duration_turns": 2
            },
            {
              "type": "ApplyEffect",
              "effect_kind": "AllyProtection",
              "target": "selected_ally",
              "duration_turns": 2
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_CHARM_SKILL_COMMAND",
        "primary_attributes": [
          {
            "attribute": "Charm",
            "weight": 0.5
          },
          {
            "attribute": "Dominance",
            "weight": 0.3
          },
          {
            "attribute": "Soul",
            "weight": 0.2
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "none",
          "aspects": [],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 6,
        "output_cap": 24,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 0,
        "action_cost": 1
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_INSTILL_PROTECTIVENESS",
        "display_name": "Instill Protectiveness",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "Selected ally gains threat-preference protection for 2 rounds"
    },
    "BLOWJOB": {
      "id": "BLOWJOB",
      "display_name": "Bl-job",
      "legacy_aliases": [],
      "kind": "Active",
      "tier": "Tier 1",
      "skill_point_cost": 1,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "none",
      "targeting": {
        "ref": "TARGET_BLOWJOB",
        "scope": [
          "Enemy"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": true,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 1,
        "resource_costs": {}
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_BLOWJOB",
          "template": "focused_strain",
          "ordered_steps": [
            {
              "type": "ModifyMeter",
              "meter": "Strain",
              "direction": "damage",
              "formula": "base_effectiveness",
              "target": "selected_enemy"
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_STRAIN_ATTACK",
        "primary_attributes": [
          {
            "attribute": "Charm",
            "weight": 0.55
          },
          {
            "attribute": "Dominance",
            "weight": 0.25
          },
          {
            "attribute": "Submission",
            "weight": 0.2
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "single",
          "aspects": [
            "Mouth"
          ],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 10,
        "output_cap": 24,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 0,
        "action_cost": 1
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_BLOWJOB",
        "display_name": "Bl-job",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "Basic focused Strain action"
    },
    "LAY": {
      "id": "LAY",
      "display_name": "Lay",
      "legacy_aliases": [],
      "kind": "Active",
      "tier": "Tier 1",
      "skill_point_cost": 1,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "none",
      "targeting": {
        "ref": "TARGET_LAY",
        "scope": [
          "Enemy"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": true,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 1,
        "resource_costs": {}
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_LAY",
          "template": "focused_strain",
          "ordered_steps": [
            {
              "type": "ModifyMeter",
              "meter": "Strain",
              "direction": "damage",
              "formula": "base_effectiveness",
              "target": "selected_enemy"
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_STRAIN_ATTACK",
        "primary_attributes": [
          {
            "attribute": "Charm",
            "weight": 0.55
          },
          {
            "attribute": "Dominance",
            "weight": 0.25
          },
          {
            "attribute": "Submission",
            "weight": 0.2
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "single",
          "aspects": [
            "Crotch"
          ],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 10,
        "output_cap": 24,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 0,
        "action_cost": 1
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_LAY",
        "display_name": "Lay",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "Focused Strain action; no default self-risk"
    },
    "GROPE": {
      "id": "GROPE",
      "display_name": "Grope",
      "legacy_aliases": [],
      "kind": "Active",
      "tier": "Tier 1",
      "skill_point_cost": 1,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "none",
      "targeting": {
        "ref": "TARGET_GROPE",
        "scope": [
          "Enemy"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": true,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 1,
        "resource_costs": {}
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_GROPE",
          "template": "focused_strain_multi",
          "ordered_steps": [
            {
              "type": "ModifyMeter",
              "meter": "Strain",
              "direction": "damage",
              "formula": "base_effectiveness",
              "target": "selected_enemy",
              "aspect_affinity_combination": "arithmetic_mean"
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_STRAIN_ATTACK",
        "primary_attributes": [
          {
            "attribute": "Charm",
            "weight": 0.55
          },
          {
            "attribute": "Dominance",
            "weight": 0.25
          },
          {
            "attribute": "Submission",
            "weight": 0.2
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "arithmetic_mean",
          "aspects": [
            "Ass",
            "Breasts"
          ],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 10,
        "output_cap": 24,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 0,
        "action_cost": 1
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_GROPE",
        "display_name": "Grope",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "Focused Strain; mean affinity across declared Aspects"
    },
    "SERVICE": {
      "id": "SERVICE",
      "display_name": "Service",
      "legacy_aliases": [],
      "kind": "Active",
      "tier": "Tier 1",
      "skill_point_cost": 1,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "none",
      "targeting": {
        "ref": "TARGET_SERVICE",
        "scope": [
          "Ally"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": true,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 1,
        "resource_costs": {}
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_SERVICE",
          "template": "vitality_recovery",
          "ordered_steps": [
            {
              "type": "ModifyMeter",
              "meter": "Vitality",
              "direction": "restore",
              "formula": "base_effectiveness",
              "cap": 24,
              "target": "selected_ally"
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_SUPPORT_RECOVERY",
        "primary_attributes": [
          {
            "attribute": "Soul",
            "weight": 0.35
          },
          {
            "attribute": "Vitality",
            "weight": 0.35
          },
          {
            "attribute": "Submission",
            "weight": 0.3
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "single",
          "aspects": [
            "Mouth"
          ],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 8,
        "output_cap": 24,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 0,
        "action_cost": 1
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_SERVICE",
        "display_name": "Service",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "Restore ally Vitality"
    },
    "H_JOB": {
      "id": "H_JOB",
      "display_name": "H-job",
      "legacy_aliases": [],
      "kind": "Active",
      "tier": "Tier 1",
      "skill_point_cost": 1,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "none",
      "targeting": {
        "ref": "TARGET_H_JOB",
        "scope": [
          "Enemy"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": true,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 1,
        "resource_costs": {}
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_H_JOB",
          "template": "strain_dot",
          "ordered_steps": [
            {
              "type": "ModifyMeter",
              "meter": "Strain",
              "direction": "damage",
              "formula": "base_effectiveness",
              "target": "selected_enemy"
            },
            {
              "type": "ApplyEffect",
              "effect_kind": "StrainDoT",
              "magnitude": 4,
              "duration_turns": 2,
              "tick": "target_turn_start",
              "decrement_after_tick": true,
              "refresh": "max_remaining_or_new",
              "stack_policy": "strongest_equivalent_only",
              "resistance": "MentalSensoryResistance"
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_SOUL_DOT",
        "primary_attributes": [
          {
            "attribute": "Soul",
            "weight": 0.45
          },
          {
            "attribute": "Charm",
            "weight": 0.3
          },
          {
            "attribute": "Dominance",
            "weight": 0.25
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "single",
          "aspects": [
            "Mind"
          ],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 5,
        "output_cap": 24,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 2,
        "tick": "target_turn_start",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "max_remaining_or_new",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 0,
        "action_cost": 1
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_H_JOB",
        "display_name": "H-job",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "Mental/sensory Strain DoT; tick at target turn start; refresh max duration"
    },
    "BEND": {
      "id": "BEND",
      "display_name": "Bend",
      "legacy_aliases": [],
      "kind": "Active",
      "tier": "Tier 1",
      "skill_point_cost": 1,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "none",
      "targeting": {
        "ref": "TARGET_BEND",
        "scope": [
          "Enemy"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": true,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 1,
        "resource_costs": {}
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_BEND",
          "template": "strain_dot",
          "ordered_steps": [
            {
              "type": "ApplyEffect",
              "effect_kind": "StrainDoT",
              "magnitude": 4,
              "duration_turns": 2,
              "tick": "target_turn_start",
              "decrement_after_tick": true,
              "refresh": "max_remaining_or_new",
              "stack_policy": "strongest_equivalent_only"
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_STRAIN_ATTACK",
        "primary_attributes": [
          {
            "attribute": "Charm",
            "weight": 0.55
          },
          {
            "attribute": "Dominance",
            "weight": 0.25
          },
          {
            "attribute": "Submission",
            "weight": 0.2
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "single",
          "aspects": [
            "Ass"
          ],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 10,
        "output_cap": 24,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 2,
        "tick": "target_turn_start",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "max_remaining_or_new",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 0,
        "action_cost": 1
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_BEND",
        "display_name": "Bend",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "Baseline single-target Strain DoT"
    },
    "AS_CHAIN": {
      "id": "AS_CHAIN",
      "display_name": "AS",
      "legacy_aliases": [],
      "kind": "Active",
      "tier": "Tier 1",
      "skill_point_cost": 1,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "none",
      "targeting": {
        "ref": "TARGET_AS_CHAIN",
        "scope": [
          "Enemy"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": true,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 1,
        "resource_costs": {}
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_AS_CHAIN",
          "template": "chain_dot",
          "ordered_steps": [
            {
              "type": "ApplyEffect",
              "effect_kind": "StrainDoT",
              "magnitude": "4 + 2*chain_count",
              "cap": 10,
              "duration_turns": 2,
              "tick": "target_turn_start",
              "decrement_after_tick": true,
              "refresh": "max_remaining_or_new",
              "stack_policy": "strongest_equivalent_only"
            },
            {
              "type": "Chain",
              "advance_when": "primary_effect_applies_to_at_least_one_valid_target",
              "max_count": 3,
              "reset_on": [
                "non_chain_action",
                "invalid_action",
                "encounter_end",
                "required_capability_or_state_lost"
              ]
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_STRAIN_ATTACK",
        "primary_attributes": [
          {
            "attribute": "Charm",
            "weight": 0.55
          },
          {
            "attribute": "Dominance",
            "weight": 0.25
          },
          {
            "attribute": "Submission",
            "weight": 0.2
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "single",
          "aspects": [
            "Ass"
          ],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 10,
        "output_cap": 24,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 2,
        "tick": "target_turn_start",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "max_remaining_or_new",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 0,
        "action_cost": 1
      },
      "rules": {
        "chain": {
          "max_count": 3,
          "advance_on": "primary_effect_applied",
          "reset_on": [
            "non_chain_action",
            "invalid_action",
            "encounter_end",
            "required_capability_or_state_lost"
          ]
        },
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_AS_CHAIN",
        "display_name": "AS",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "Chain advances only if primary effect applies; resets on non-chain, invalid, encounter end, capability loss"
    },
    "S_SYMBOL": {
      "id": "S_SYMBOL",
      "display_name": "S Symbol",
      "legacy_aliases": [],
      "kind": "Passive",
      "tier": "Tier 1",
      "skill_point_cost": 1,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "none",
      "targeting": {
        "ref": "TARGET_S_SYMBOL",
        "scope": [
          "Ally",
          "Self"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": false,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 0,
        "resource_costs": {}
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_S_SYMBOL",
          "template": "overflow_recovery",
          "ordered_steps": [
            {
              "type": "ListenEvent",
              "event": "OverflowResolved",
              "frequency": "once_per_affected_actor_per_resolved_action",
              "recursion_guard": true,
              "max_chain_depth": 1,
              "output_cap": 15,
              "listener_priority": 10
            },
            {
              "type": "ModifyMeter",
              "meter": "Strain",
              "direction": "restore",
              "amount": 10,
              "target": "owner"
            },
            {
              "type": "ModifyMeter",
              "meter": "Strain",
              "direction": "restore",
              "amount": 5,
              "target": "lowest_strain_ally"
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_SOUL_OVERFLOW",
        "primary_attributes": [
          {
            "attribute": "Soul",
            "weight": 0.45
          },
          {
            "attribute": "Dominance",
            "weight": 0.3
          },
          {
            "attribute": "Masochism",
            "weight": 0.25
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "none",
          "aspects": [],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 6,
        "output_cap": 24,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 0,
        "action_cost": 0
      },
      "rules": {
        "chain": null,
        "overflow": {
          "event": "OverflowResolved",
          "frequency": "once_per_affected_actor_per_resolved_action",
          "max_chain_depth": 1,
          "recursion_guard": true,
          "listener_priority": 10
        },
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_S_SYMBOL",
        "display_name": "S Symbol",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "Overflow listener restores Strain"
    },
    "OTHERWORLDLY_CHARM": {
      "id": "OTHERWORLDLY_CHARM",
      "display_name": "Otherworldly Charm",
      "legacy_aliases": [],
      "kind": "Passive",
      "tier": "Tier 1",
      "skill_point_cost": 1,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "none",
      "targeting": {
        "ref": "TARGET_OTHERWORLDLY_CHARM",
        "scope": [
          "Enemy"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": false,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 0,
        "resource_costs": {}
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_OTHERWORLDLY_CHARM",
          "template": "intent_bias",
          "ordered_steps": [
            {
              "type": "ConditionalPassive",
              "condition": "enemy_ai_selects_intent",
              "effect": {
                "type": "ModifyIntentWeight",
                "intent_family": "StrainOriented",
                "value": 0.15
              },
              "stack_policy": "unique"
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_CHARM_SKILL_COMMAND",
        "primary_attributes": [
          {
            "attribute": "Charm",
            "weight": 0.5
          },
          {
            "attribute": "Dominance",
            "weight": 0.3
          },
          {
            "attribute": "Soul",
            "weight": 0.2
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "none",
          "aspects": [],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 6,
        "output_cap": 24,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 0,
        "action_cost": 0
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_OTHERWORLDLY_CHARM",
        "display_name": "Otherworldly Charm",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "Passive bias toward Strain-oriented enemy intent; not active control"
    },
    "PIERCING_STARES": {
      "id": "PIERCING_STARES",
      "display_name": "Piercing Stares",
      "legacy_aliases": [],
      "kind": "Passive",
      "tier": "Tier 1",
      "skill_point_cost": 1,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "none",
      "targeting": {
        "ref": "TARGET_PIERCING_STARES",
        "scope": [
          "Enemy"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": false,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 0,
        "resource_costs": {}
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_PIERCING_STARES",
          "template": "equipment_dot",
          "ordered_steps": [
            {
              "type": "ConditionalPassive",
              "condition": "required_piercing_equipment_equipped",
              "effect": {
                "type": "ApplyEffect",
                "effect_kind": "StrainDoT",
                "magnitude": 4,
                "duration_turns": 2,
                "tick": "target_turn_start",
                "decrement_after_tick": true,
                "refresh": "max_remaining_or_new",
                "stack_policy": "strongest_equivalent_only"
              }
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_STRAIN_ATTACK",
        "primary_attributes": [
          {
            "attribute": "Charm",
            "weight": 0.55
          },
          {
            "attribute": "Dominance",
            "weight": 0.25
          },
          {
            "attribute": "Submission",
            "weight": 0.2
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "single",
          "aspects": [
            "Breasts"
          ],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 10,
        "output_cap": 24,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 2,
        "tick": "target_turn_start",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "max_remaining_or_new",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 0,
        "action_cost": 0
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_PIERCING_STARES",
        "display_name": "Piercing Stares",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "If declared piercing equipment equipped, apply Strain DoT"
    },
    "SADISM": {
      "id": "SADISM",
      "display_name": "Sadism",
      "legacy_aliases": [],
      "kind": "Passive",
      "tier": "Tier 1",
      "skill_point_cost": 1,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "none",
      "targeting": {
        "ref": "TARGET_SADISM",
        "scope": [
          "Self"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": false,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 0,
        "resource_costs": {}
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_SADISM",
          "template": "damage_passive",
          "ordered_steps": [
            {
              "type": "ModifyStat",
              "target": "self",
              "stat": "VitalityDamageDealt",
              "operation": "add_percent",
              "value": 0.12,
              "stack_group": "SADISM_DAMAGE",
              "stack_cap": 0.3
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_VITALITY_ATTACK",
        "primary_attributes": [
          {
            "attribute": "Body",
            "weight": 0.45
          },
          {
            "attribute": "Sadism",
            "weight": 0.35
          },
          {
            "attribute": "Agility",
            "weight": 0.2
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "arithmetic_mean",
          "aspects": [
            "Crotch",
            "Mouth"
          ],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 9,
        "output_cap": 24,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 0,
        "action_cost": 0
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_SADISM",
        "display_name": "Sadism",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "+12% Vitality damage; stacking cap +30%"
    },
    "MASOCHISM": {
      "id": "MASOCHISM",
      "display_name": "Masochism",
      "legacy_aliases": [],
      "kind": "Passive",
      "tier": "Tier 1",
      "skill_point_cost": 1,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "none",
      "targeting": {
        "ref": "TARGET_MASOCHISM",
        "scope": [
          "Self"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": false,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 0,
        "resource_costs": {}
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_MASOCHISM",
          "template": "resistance_passive",
          "ordered_steps": [
            {
              "type": "ModifyStat",
              "target": "self",
              "stat": "VitalityResistance",
              "operation": "add_percent",
              "value": 0.1,
              "stack_group": "MASOCHISM_RESISTANCE",
              "stack_cap": 0.25
            },
            {
              "type": "ModifyStat",
              "target": "self",
              "stat": "StrainResistance",
              "operation": "add_percent",
              "value": 0.1,
              "stack_group": "MASOCHISM_RESISTANCE",
              "stack_cap": 0.25
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_AGILITY_DEFENSE",
        "primary_attributes": [
          {
            "attribute": "Agility",
            "weight": 0.45
          },
          {
            "attribute": "Body",
            "weight": 0.3
          },
          {
            "attribute": "Masochism",
            "weight": 0.25
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "arithmetic_mean",
          "aspects": [
            "Ass",
            "Breasts"
          ],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 6,
        "output_cap": 24,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 0,
        "action_cost": 0
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_MASOCHISM",
        "display_name": "Masochism",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "+10% Vitality/Strain resistance; cap 25%"
    },
    "MOANS": {
      "id": "MOANS",
      "display_name": "Moans",
      "legacy_aliases": [],
      "kind": "Passive",
      "tier": "Tier 1",
      "skill_point_cost": 1,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "none",
      "targeting": {
        "ref": "TARGET_MOANS",
        "scope": [
          "Enemy"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": false,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 0,
        "resource_costs": {}
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_MOANS",
          "template": "strain_reflect",
          "ordered_steps": [
            {
              "type": "ListenEvent",
              "event": "QualifyingIncomingStrainDamageResolved",
              "max_triggers_per_enemy_action": 1,
              "recursion_guard": true,
              "output_cap": 8
            },
            {
              "type": "ModifyMeter",
              "meter": "Strain",
              "direction": "damage",
              "target": "source_enemy",
              "formula": "min(0.2*incoming_strain,8)"
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_STRAIN_CONTROL",
        "primary_attributes": [
          {
            "attribute": "Charm",
            "weight": 0.35
          },
          {
            "attribute": "Dominance",
            "weight": 0.35
          },
          {
            "attribute": "Soul",
            "weight": 0.3
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "single",
          "aspects": [
            "Mouth"
          ],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 8,
        "output_cap": 24,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 0,
        "action_cost": 0
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_MOANS",
        "display_name": "Moans",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "Reflect 20% incoming Strain once per enemy action; cap 8"
    },
    "ENCOURAGE": {
      "id": "ENCOURAGE",
      "display_name": "Encourage",
      "legacy_aliases": [],
      "kind": "Active",
      "tier": "Tier 2",
      "skill_point_cost": 2,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "ACT_I_COMPLETE",
      "targeting": {
        "ref": "TARGET_ENCOURAGE",
        "scope": [
          "Ally"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": true,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 1,
        "resource_costs": {}
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_ENCOURAGE",
          "template": "next_attack_buff",
          "ordered_steps": [
            {
              "type": "ApplyEffect",
              "effect_kind": "NextQualifyingAttackBonus",
              "target": "selected_ally",
              "magnitude": 0.2,
              "expires_after": "next_qualifying_attack",
              "duration_turns": 2,
              "stack_policy": "refresh"
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_SUPPORT_RECOVERY",
        "primary_attributes": [
          {
            "attribute": "Soul",
            "weight": 0.35
          },
          {
            "attribute": "Vitality",
            "weight": 0.35
          },
          {
            "attribute": "Submission",
            "weight": 0.3
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "single",
          "aspects": [
            "Ass"
          ],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 8,
        "output_cap": 32,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 0,
        "action_cost": 1
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_ENCOURAGE",
        "display_name": "Encourage",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "Ally next qualifying attack +20%; expires after action or 2 turns"
    },
    "FLAUNT": {
      "id": "FLAUNT",
      "display_name": "Flaunt",
      "legacy_aliases": [],
      "kind": "Active",
      "tier": "Tier 2",
      "skill_point_cost": 2,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "ACT_I_COMPLETE",
      "targeting": {
        "ref": "TARGET_FLAUNT",
        "scope": [
          "Enemies"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": true,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 1,
        "resource_costs": {}
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_FLAUNT",
          "template": "area_flat",
          "ordered_steps": [
            {
              "type": "SnapshotTargets",
              "scope": "valid_enemies",
              "at": "validation"
            },
            {
              "type": "ModifyMeter",
              "meter": "Strain",
              "direction": "damage",
              "formula": "base_effectiveness",
              "target_snapshot": "validation",
              "per_target_cap": 18,
              "total_cap": 36
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_AREA_STRAIN",
        "primary_attributes": [
          {
            "attribute": "Charm",
            "weight": 0.4
          },
          {
            "attribute": "Dominance",
            "weight": 0.35
          },
          {
            "attribute": "Submission",
            "weight": 0.25
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "none",
          "aspects": [],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 6,
        "output_cap": 32,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 1,
        "action_cost": 1
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_FLAUNT",
        "display_name": "Flaunt",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "Reliable flat Strain pressure to all valid enemies"
    },
    "AUTOF": {
      "id": "AUTOF",
      "display_name": "Autof",
      "legacy_aliases": [],
      "kind": "Active",
      "tier": "Tier 2",
      "skill_point_cost": 2,
      "requirements": {
        "all_of": [
          {
            "type": "capability",
            "id": "CAPABILITY_P_GROWTH",
            "scope": "actor",
            "owner": "Alya"
          }
        ],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "ACT_I_COMPLETE",
      "targeting": {
        "ref": "TARGET_AUTOF",
        "scope": [
          "Self"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": false,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 1,
        "resource_costs": {}
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_AUTOF",
          "template": "self_recovery_cleanse",
          "ordered_steps": [
            {
              "type": "ModifyMeter",
              "meter": "Vitality",
              "direction": "restore",
              "amount": 20,
              "target": "self"
            },
            {
              "type": "RemoveEffect",
              "target": "self",
              "filter": {
                "tags": [
                  "debuff"
                ],
                "removable_categories": [
                  "stat_debuff",
                  "dot",
                  "intent_bias"
                ]
              },
              "max_count": 1
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_SUPPORT_RECOVERY",
        "primary_attributes": [
          {
            "attribute": "Soul",
            "weight": 0.35
          },
          {
            "attribute": "Vitality",
            "weight": 0.35
          },
          {
            "attribute": "Submission",
            "weight": 0.3
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "arithmetic_mean",
          "aspects": [
            "Breasts",
            "Crotch",
            "Mouth"
          ],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 8,
        "output_cap": 32,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 0,
        "action_cost": 1
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": {
          "required": "CAPABILITY_P_GROWTH",
          "owner": "Alya"
        }
      },
      "presentation": {
        "ref": "PRES_AUTOF",
        "display_name": "Autof",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "Requires P-growth; restore 20 Vitality and remove one eligible debuff"
    },
    "APHRODISIAC": {
      "id": "APHRODISIAC",
      "display_name": "Aphrodisiac",
      "legacy_aliases": [],
      "kind": "Active",
      "tier": "Tier 2",
      "skill_point_cost": 2,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "ACT_I_COMPLETE",
      "targeting": {
        "ref": "TARGET_APHRODISIAC",
        "scope": [
          "Enemy"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": true,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 1,
        "resource_costs": {}
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_APHRODISIAC",
          "template": "dot_intent_bias",
          "ordered_steps": [
            {
              "type": "ApplyEffect",
              "effect_kind": "StrainDoT",
              "magnitude": 4,
              "duration_turns": 2,
              "tick": "target_turn_start",
              "decrement_after_tick": true,
              "refresh": "max_remaining_or_new",
              "stack_policy": "strongest_equivalent_only"
            },
            {
              "type": "ChangeIntent",
              "target": "selected_enemy",
              "bias": "StrainOriented",
              "duration_turns": 2,
              "resistance": "MentalControlResistance"
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_SOUL_DOT",
        "primary_attributes": [
          {
            "attribute": "Soul",
            "weight": 0.45
          },
          {
            "attribute": "Charm",
            "weight": 0.3
          },
          {
            "attribute": "Dominance",
            "weight": 0.25
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "single",
          "aspects": [
            "Mind"
          ],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 5,
        "output_cap": 32,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 2,
        "tick": "target_turn_start",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "max_remaining_or_new",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 0,
        "action_cost": 1
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_APHRODISIAC",
        "display_name": "Aphrodisiac",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "Strain DoT plus bounded Strain-intent bias; same duration"
    },
    "P_GROWTH": {
      "id": "P_GROWTH",
      "display_name": "P-growth",
      "legacy_aliases": [],
      "kind": "Capability/Transformation",
      "tier": "Tier 2",
      "skill_point_cost": 2,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "ACT_I_COMPLETE",
      "targeting": {
        "ref": "TARGET_P_GROWTH",
        "scope": [
          "Self"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": false,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 0,
        "resource_costs": {}
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_P_GROWTH",
          "template": "grant_capability",
          "ordered_steps": [
            {
              "type": "GrantCapability",
              "capability": "CAPABILITY_P_GROWTH",
              "target": "Alya",
              "persistence": "persistent",
              "revocation": "explicit_story_or_configuration_event"
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_CAPABILITY",
        "primary_attributes": [
          {
            "attribute": "Soul",
            "weight": 0.4
          },
          {
            "attribute": "Body",
            "weight": 0.3
          },
          {
            "attribute": "Dominance",
            "weight": 0.3
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "arithmetic_mean",
          "aspects": [
            "Crotch",
            "Mind"
          ],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 0,
        "output_cap": 32,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 0,
        "action_cost": 0
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": {
          "granted": "CAPABILITY_P_GROWTH",
          "owner": "Alya",
          "persistence": "persistent",
          "revocation": "explicit"
        }
      },
      "presentation": {
        "ref": "PRES_P_GROWTH",
        "display_name": "P-growth",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "Grants CAPABILITY_P_GROWTH to Alya only; persistent until explicit revocation"
    },
    "FACESIT": {
      "id": "FACESIT",
      "display_name": "Facesit",
      "legacy_aliases": [],
      "kind": "Active",
      "tier": "Tier 2",
      "skill_point_cost": 2,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "ACT_I_COMPLETE",
      "targeting": {
        "ref": "TARGET_FACESIT",
        "scope": [
          "Enemy"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": true,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 1,
        "resource_costs": {}
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_FACESIT",
          "template": "focused_strain",
          "ordered_steps": [
            {
              "type": "ModifyMeter",
              "meter": "Strain",
              "direction": "damage",
              "formula": "base_effectiveness",
              "target": "selected_enemy"
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_STRAIN_ATTACK",
        "primary_attributes": [
          {
            "attribute": "Charm",
            "weight": 0.55
          },
          {
            "attribute": "Dominance",
            "weight": 0.25
          },
          {
            "attribute": "Submission",
            "weight": 0.2
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "single",
          "aspects": [
            "Crotch"
          ],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 10,
        "output_cap": 32,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 0,
        "action_cost": 1
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_FACESIT",
        "display_name": "Facesit",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "Focused Strain; no default self-damage"
    },
    "BONDAGE": {
      "id": "BONDAGE",
      "display_name": "Bondage",
      "legacy_aliases": [],
      "kind": "Active",
      "tier": "Tier 2",
      "skill_point_cost": 2,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "ACT_I_COMPLETE",
      "targeting": {
        "ref": "TARGET_BONDAGE",
        "scope": [
          "Self"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": false,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 1,
        "resource_costs": {}
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_BONDAGE",
          "template": "self_restraint_tradeoff",
          "ordered_steps": [
            {
              "type": "ApplyEffect",
              "effect_kind": "SelfRestraint",
              "target": "self",
              "duration_turns": 2,
              "stat_modifiers": {
                "Evasion": -10
              },
              "next_qualifying_strain_action_bonus": 0.25,
              "stack_policy": "refresh"
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_RESOLVE_RISK",
        "primary_attributes": [
          {
            "attribute": "Masochism",
            "weight": 0.4
          },
          {
            "attribute": "Submission",
            "weight": 0.35
          },
          {
            "attribute": "Body",
            "weight": 0.25
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "none",
          "aspects": [],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 6,
        "output_cap": 32,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 0,
        "action_cost": 1
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_BONDAGE",
        "display_name": "Bondage",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "Self restraint lowers evasion 10 and boosts next Strain action 25%; 2 turns"
    },
    "BULLY": {
      "id": "BULLY",
      "display_name": "Bully",
      "legacy_aliases": [],
      "kind": "Active",
      "tier": "Tier 2",
      "skill_point_cost": 2,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "ACT_I_COMPLETE",
      "targeting": {
        "ref": "TARGET_BULLY",
        "scope": [
          "Enemy"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": true,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 1,
        "resource_costs": {}
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_BULLY",
          "template": "attack_defense_debuff",
          "ordered_steps": [
            {
              "type": "ModifyStat",
              "target": "selected_enemy",
              "stat": "Attack",
              "operation": "multiply",
              "value": 0.88,
              "duration_turns": 2
            },
            {
              "type": "ModifyStat",
              "target": "selected_enemy",
              "stat": "Defense",
              "operation": "multiply",
              "value": 0.88,
              "duration_turns": 2
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_CHARM_SKILL_COMMAND",
        "primary_attributes": [
          {
            "attribute": "Charm",
            "weight": 0.5
          },
          {
            "attribute": "Dominance",
            "weight": 0.3
          },
          {
            "attribute": "Soul",
            "weight": 0.2
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "single",
          "aspects": [
            "Mouth"
          ],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 6,
        "output_cap": 32,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 0,
        "action_cost": 1
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_BULLY",
        "display_name": "Bully",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "Reduce target attack and defense by 12% for 2 turns"
    },
    "BITE": {
      "id": "BITE",
      "display_name": "Bite",
      "legacy_aliases": [],
      "kind": "Active",
      "tier": "Tier 2",
      "skill_point_cost": 2,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "ACT_I_COMPLETE",
      "targeting": {
        "ref": "TARGET_BITE",
        "scope": [
          "Enemy"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": true,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 1,
        "resource_costs": {}
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_BITE",
          "template": "focused_vitality",
          "ordered_steps": [
            {
              "type": "ModifyMeter",
              "meter": "Vitality",
              "direction": "damage",
              "formula": "base_effectiveness",
              "target": "selected_enemy"
            },
            {
              "type": "ConditionalEffect",
              "condition": "target_has_explicit_vulnerability_tag",
              "effect": {
                "type": "ModifyMeter",
                "meter": "Strain",
                "direction": "damage",
                "formula": "0.2*base_effectiveness",
                "cap": 4
              }
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_VITALITY_ATTACK",
        "primary_attributes": [
          {
            "attribute": "Body",
            "weight": 0.45
          },
          {
            "attribute": "Sadism",
            "weight": 0.35
          },
          {
            "attribute": "Agility",
            "weight": 0.2
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "single",
          "aspects": [
            "Mouth"
          ],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 9,
        "output_cap": 32,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 0,
        "action_cost": 1
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_BITE",
        "display_name": "Bite",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "Focused Vitality attack; Strain rider only under explicit vulnerability"
    },
    "BIND": {
      "id": "BIND",
      "display_name": "Bind",
      "legacy_aliases": [],
      "kind": "Active",
      "tier": "Tier 2",
      "skill_point_cost": 2,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "ACT_I_COMPLETE",
      "targeting": {
        "ref": "TARGET_BIND",
        "scope": [
          "Enemy"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": true,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 1,
        "resource_costs": {}
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_BIND",
          "template": "restraint",
          "ordered_steps": [
            {
              "type": "ApplyEffect",
              "effect_kind": "Restraint",
              "target": "selected_enemy",
              "duration_turns": 1,
              "blocked_action_tags": [
                "Mobility"
              ],
              "resistance": "ControlResistance",
              "removal": [
                "duration_expiry",
                "cleanse",
                "source_removed"
              ]
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_SOUL_CONTROL",
        "primary_attributes": [
          {
            "attribute": "Soul",
            "weight": 0.55
          },
          {
            "attribute": "Dominance",
            "weight": 0.25
          },
          {
            "attribute": "Charm",
            "weight": 0.2
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "single",
          "aspects": [
            "Mind"
          ],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 7,
        "output_cap": 32,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 0,
        "action_cost": 1
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_BIND",
        "display_name": "Bind",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "Resisted restraint blocks Mobility actions for 1 turn; not full disable"
    },
    "PROLONGED_PL": {
      "id": "PROLONGED_PL",
      "display_name": "Prolonged Pl-",
      "legacy_aliases": [],
      "kind": "Active",
      "tier": "Tier 2",
      "skill_point_cost": 2,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "ACT_I_COMPLETE",
      "targeting": {
        "ref": "TARGET_PROLONGED_PL",
        "scope": [
          "Enemy"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": true,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 1,
        "resource_costs": {}
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_PROLONGED_PL",
          "template": "overflow_lock",
          "ordered_steps": [
            {
              "type": "ApplyEffect",
              "effect_kind": "OverflowLock",
              "target": "selected_enemy",
              "duration_turns": 2,
              "prevents_overflow": true,
              "does_not_change_strain": true,
              "on_remove": "reevaluate_threshold_and_emit_overflow"
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_SOUL_CONTROL",
        "primary_attributes": [
          {
            "attribute": "Soul",
            "weight": 0.55
          },
          {
            "attribute": "Dominance",
            "weight": 0.25
          },
          {
            "attribute": "Charm",
            "weight": 0.2
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "single",
          "aspects": [
            "Crotch"
          ],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 7,
        "output_cap": 32,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 0,
        "action_cost": 1
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_PROLONGED_PL",
        "display_name": "Prolonged Pl-",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "Prevents target Overflow while active; reevaluate on removal/expiry"
    },
    "F_FK": {
      "id": "F_FK",
      "display_name": "F-fk",
      "legacy_aliases": [],
      "kind": "Active",
      "tier": "Tier 2",
      "skill_point_cost": 2,
      "requirements": {
        "all_of": [
          {
            "type": "capability",
            "id": "CAPABILITY_P_GROWTH",
            "scope": "actor",
            "owner": "Alya"
          }
        ],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "ACT_I_COMPLETE",
      "targeting": {
        "ref": "TARGET_F_FK",
        "scope": [
          "Enemy"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": true,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 1,
        "resource_costs": {}
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_F_FK",
          "template": "missing_vitality_bonus",
          "ordered_steps": [
            {
              "type": "ModifyMeter",
              "meter": "Strain",
              "direction": "damage",
              "target": "selected_enemy",
              "formula": "base_effectiveness*(1+min(0.5,missing_vitality_ratio*0.5))",
              "snapshot": "target_vitality_at_validation",
              "order": "before_target_resistance"
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_STRAIN_ATTACK",
        "primary_attributes": [
          {
            "attribute": "Charm",
            "weight": 0.55
          },
          {
            "attribute": "Dominance",
            "weight": 0.25
          },
          {
            "attribute": "Submission",
            "weight": 0.2
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "single",
          "aspects": [
            "Crotch"
          ],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 10,
        "output_cap": 32,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 0,
        "action_cost": 1
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": {
          "required": "CAPABILITY_P_GROWTH",
          "owner": "Alya"
        }
      },
      "presentation": {
        "ref": "PRES_F_FK",
        "display_name": "F-fk",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "Requires P-growth; Strain bonus from target missing Vitality, capped +50%"
    },
    "PAIZURI": {
      "id": "PAIZURI",
      "display_name": "Paizuri",
      "legacy_aliases": [],
      "kind": "Active",
      "tier": "Tier 2",
      "skill_point_cost": 2,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "ACT_I_COMPLETE",
      "targeting": {
        "ref": "TARGET_PAIZURI",
        "scope": [
          "Enemy"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": true,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 1,
        "resource_costs": {}
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_PAIZURI",
          "template": "focused_strain",
          "ordered_steps": [
            {
              "type": "ModifyMeter",
              "meter": "Strain",
              "direction": "damage",
              "formula": "base_effectiveness",
              "target": "selected_enemy"
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_STRAIN_ATTACK",
        "primary_attributes": [
          {
            "attribute": "Charm",
            "weight": 0.55
          },
          {
            "attribute": "Dominance",
            "weight": 0.25
          },
          {
            "attribute": "Submission",
            "weight": 0.2
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "single",
          "aspects": [
            "Breasts"
          ],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 10,
        "output_cap": 32,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 0,
        "action_cost": 1
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_PAIZURI",
        "display_name": "Paizuri",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "Basic focused Strain action with distinct Breast affinity"
    },
    "SUMMON_CS": {
      "id": "SUMMON_CS",
      "display_name": "Summon c-s",
      "legacy_aliases": [],
      "kind": "Active",
      "tier": "Tier 2",
      "skill_point_cost": 2,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "ACT_I_COMPLETE",
      "targeting": {
        "ref": "TARGET_SUMMON_CS",
        "scope": [
          "Enemies"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": true,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 1,
        "resource_costs": {}
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_SUMMON_CS",
          "template": "concentrated_area",
          "ordered_steps": [
            {
              "type": "SnapshotTargets",
              "scope": "valid_enemies",
              "at": "validation",
              "max_targets": 6
            },
            {
              "type": "ModifyMeter",
              "meter": "Strain",
              "direction": "damage",
              "formula": "min(48/N,base_effectiveness*(1+0.25*(6-N)))",
              "per_target_cap": 24,
              "total_cap": 48,
              "target_snapshot": "validation",
              "invalid_if_N_zero": true
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_AREA_STRAIN",
        "primary_attributes": [
          {
            "attribute": "Charm",
            "weight": 0.4
          },
          {
            "attribute": "Dominance",
            "weight": 0.35
          },
          {
            "attribute": "Submission",
            "weight": 0.25
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "single",
          "aspects": [
            "Mind"
          ],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 6,
        "output_cap": 32,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 2,
        "action_cost": 1
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_SUMMON_CS",
        "display_name": "Summon c-s",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "Per-target output rises as enemy count falls; total cap 48; snapshot at validation"
    },
    "SWALLOW": {
      "id": "SWALLOW",
      "display_name": "Swallow",
      "legacy_aliases": [],
      "kind": "Active",
      "tier": "Tier 2",
      "skill_point_cost": 2,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "ACT_I_COMPLETE",
      "targeting": {
        "ref": "TARGET_SWALLOW",
        "scope": [
          "Enemy"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": true,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 1,
        "resource_costs": {
          "Command": 3,
          "Pressure": 2
        }
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_SWALLOW",
          "template": "single_finisher",
          "ordered_steps": [
            {
              "type": "RequestOutcome",
              "target": "selected_enemy",
              "outcome": "authored_permitted_outcome",
              "threshold_ratio": 0.8,
              "allowed_outcomes": [
                "Yield",
                "Disable",
                "Capture"
              ],
              "invalid_if_outcome_not_permitted": true,
              "no_implicit_defeat": true
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_FINISHER",
        "primary_attributes": [
          {
            "attribute": "Dominance",
            "weight": 0.4
          },
          {
            "attribute": "Soul",
            "weight": 0.35
          },
          {
            "attribute": "Charm",
            "weight": 0.25
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "single",
          "aspects": [
            "Mouth"
          ],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 12,
        "output_cap": 32,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 3,
        "action_cost": 1
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": {
          "allowed_outcomes": [
            "Yield",
            "Disable",
            "Capture"
          ],
          "never_force_global_victory": true
        },
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_SWALLOW",
        "display_name": "Swallow",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "At Strain >= 80%, request encounter-permitted authored outcome; no implicit Defeat"
    },
    "EXTRA_TIPS": {
      "id": "EXTRA_TIPS",
      "display_name": "Extra tips",
      "legacy_aliases": [],
      "kind": "Passive",
      "tier": "Tier 2",
      "skill_point_cost": 2,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "ACT_I_COMPLETE",
      "targeting": {
        "ref": "TARGET_EXTRA_TIPS",
        "scope": [
          "Self"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": false,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 0,
        "resource_costs": {}
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_EXTRA_TIPS",
          "template": "reward_bonus",
          "ordered_steps": [
            {
              "type": "ModifyReward",
              "target": "encounter_reward",
              "operation": "multiply",
              "value": 1.1,
              "stack_group": "EXTRA_TIPS_REWARD",
              "stack_cap": 1.2,
              "event": "RewardResolution",
              "no_extra_roll": true
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_CHARM_SKILL_COMMAND",
        "primary_attributes": [
          {
            "attribute": "Charm",
            "weight": 0.5
          },
          {
            "attribute": "Dominance",
            "weight": 0.3
          },
          {
            "attribute": "Soul",
            "weight": 0.2
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "single",
          "aspects": [
            "Mind"
          ],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 6,
        "output_cap": 32,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 0,
        "action_cost": 0
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_EXTRA_TIPS",
        "display_name": "Extra tips",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "+10% reward value; cap +20%; no extra reward roll"
    },
    "CUTENESS": {
      "id": "CUTENESS",
      "display_name": "Cuteness",
      "legacy_aliases": [],
      "kind": "Passive",
      "tier": "Tier 2",
      "skill_point_cost": 2,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "ACT_I_COMPLETE",
      "targeting": {
        "ref": "TARGET_CUTENESS",
        "scope": [
          "Ally"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": false,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 0,
        "resource_costs": {}
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_CUTENESS",
          "template": "ally_attack_passive",
          "ordered_steps": [
            {
              "type": "ModifyStat",
              "target": "all_allies",
              "stat": "DamageDealt",
              "operation": "add_percent",
              "value": 0.08,
              "stack_group": "ALLY_DAMAGE_PASSIVES",
              "stack_cap": 0.2
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_SUPPORT_RECOVERY",
        "primary_attributes": [
          {
            "attribute": "Soul",
            "weight": 0.35
          },
          {
            "attribute": "Vitality",
            "weight": 0.35
          },
          {
            "attribute": "Submission",
            "weight": 0.3
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "arithmetic_mean",
          "aspects": [
            "Breasts",
            "Mouth"
          ],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 8,
        "output_cap": 32,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 0,
        "action_cost": 0
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_CUTENESS",
        "display_name": "Cuteness",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "Allies +8% damage; stacking cap +20%"
    },
    "NAUGHTY_THOUGHTS": {
      "id": "NAUGHTY_THOUGHTS",
      "display_name": "Naughty Thoughts",
      "legacy_aliases": [],
      "kind": "Passive",
      "tier": "Tier 2",
      "skill_point_cost": 2,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "ACT_I_COMPLETE",
      "targeting": {
        "ref": "TARGET_NAUGHTY_THOUGHTS",
        "scope": [
          "Self"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": false,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 0,
        "resource_costs": {}
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_NAUGHTY_THOUGHTS",
          "template": "strain_accuracy_passive",
          "ordered_steps": [
            {
              "type": "ModifyStat",
              "target": "self",
              "stat": "StrainAccuracyAndEffectiveness",
              "operation": "add_percent",
              "value": 0.1,
              "stack_group": "NAUGHTY_THOUGHTS",
              "stack_cap": 0.2
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_SOUL_DOT",
        "primary_attributes": [
          {
            "attribute": "Soul",
            "weight": 0.45
          },
          {
            "attribute": "Charm",
            "weight": 0.3
          },
          {
            "attribute": "Dominance",
            "weight": 0.25
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "single",
          "aspects": [
            "Mind"
          ],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 5,
        "output_cap": 32,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 0,
        "action_cost": 0
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_NAUGHTY_THOUGHTS",
        "display_name": "Naughty Thoughts",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "+10% Strain accuracy/effectiveness; cap +20%"
    },
    "C_DRINKER": {
      "id": "C_DRINKER",
      "display_name": "C-drinker",
      "legacy_aliases": [],
      "kind": "Passive",
      "tier": "Tier 2",
      "skill_point_cost": 2,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "ACT_I_COMPLETE",
      "targeting": {
        "ref": "TARGET_C_DRINKER",
        "scope": [
          "Ally"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": false,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 0,
        "resource_costs": {}
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_C_DRINKER",
          "template": "defeat_recovery",
          "ordered_steps": [
            {
              "type": "ListenEvent",
              "event": "QualifyingEnemyDefeated",
              "predicate": "defeating_skill_has_eligible_tag",
              "once_per_event": true
            },
            {
              "type": "ModifyMeter",
              "meter": "Strain",
              "direction": "restore",
              "amount": 8,
              "target": "lowest_strain_ally"
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_SUPPORT_RECOVERY",
        "primary_attributes": [
          {
            "attribute": "Soul",
            "weight": 0.35
          },
          {
            "attribute": "Vitality",
            "weight": 0.35
          },
          {
            "attribute": "Submission",
            "weight": 0.3
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "single",
          "aspects": [
            "Mind"
          ],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 8,
        "output_cap": 32,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 0,
        "action_cost": 0
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_C_DRINKER",
        "display_name": "C-drinker",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "After qualifying enemy defeat, restore 8 Strain to lowest-Strain ally once per event"
    },
    "STRIP": {
      "id": "STRIP",
      "display_name": "Strip",
      "legacy_aliases": [],
      "kind": "Active",
      "tier": "Tier 3",
      "skill_point_cost": 3,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "ACT_II_COMPLETE",
      "targeting": {
        "ref": "TARGET_STRIP",
        "scope": [
          "Enemies",
          "Self"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": false,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 1,
        "resource_costs": {}
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_STRIP",
          "template": "area_evasion",
          "ordered_steps": [
            {
              "type": "ModifyMeter",
              "meter": "Strain",
              "direction": "damage",
              "formula": "base_effectiveness",
              "target": "all_valid_enemies"
            },
            {
              "type": "ApplyEffect",
              "effect_kind": "EvasionBonus",
              "magnitude": 20,
              "duration_turns": 1,
              "target": "self"
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_AREA_STRAIN",
        "primary_attributes": [
          {
            "attribute": "Charm",
            "weight": 0.4
          },
          {
            "attribute": "Dominance",
            "weight": 0.35
          },
          {
            "attribute": "Submission",
            "weight": 0.25
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "none",
          "aspects": [],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 6,
        "output_cap": 40,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 2,
        "action_cost": 1
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_STRIP",
        "display_name": "Strip",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "Area Strain plus +20 evasion against next enemy action"
    },
    "PINK_MIST": {
      "id": "PINK_MIST",
      "display_name": "Pink Mist",
      "legacy_aliases": [],
      "kind": "Active",
      "tier": "Tier 3",
      "skill_point_cost": 3,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "ACT_II_COMPLETE",
      "targeting": {
        "ref": "TARGET_PINK_MIST",
        "scope": [
          "Enemies"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": true,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 1,
        "resource_costs": {}
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_PINK_MIST",
          "template": "area_dot_debuff",
          "ordered_steps": [
            {
              "type": "SnapshotTargets",
              "scope": "valid_enemies",
              "at": "validation"
            },
            {
              "type": "ApplyEffect",
              "effect_kind": "StrainDoT",
              "target_snapshot": "validation",
              "magnitude": 5,
              "duration_turns": 2,
              "tick": "target_turn_start",
              "decrement_after_tick": true,
              "refresh": "max_remaining_or_new",
              "stack_policy": "strongest_equivalent_only"
            },
            {
              "type": "ModifyStat",
              "target_snapshot": "validation",
              "stat": "Defense",
              "operation": "multiply",
              "value": 0.9,
              "duration_turns": 2
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_SOUL_DOT",
        "primary_attributes": [
          {
            "attribute": "Soul",
            "weight": 0.45
          },
          {
            "attribute": "Charm",
            "weight": 0.3
          },
          {
            "attribute": "Dominance",
            "weight": 0.25
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "single",
          "aspects": [
            "Mind"
          ],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 5,
        "output_cap": 40,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 2,
        "tick": "target_turn_start",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "max_remaining_or_new",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 3,
        "action_cost": 1
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_PINK_MIST",
        "display_name": "Pink Mist",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "Area Strain DoT 5 per turn for 2 turns and defense -10%; no duplicate stack"
    },
    "PENETRATE": {
      "id": "PENETRATE",
      "display_name": "Penetrate",
      "legacy_aliases": [],
      "kind": "Active",
      "tier": "Tier 3",
      "skill_point_cost": 3,
      "requirements": {
        "all_of": [
          {
            "type": "capability",
            "id": "CAPABILITY_P_GROWTH",
            "scope": "actor",
            "owner": "Alya"
          }
        ],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "ACT_II_COMPLETE",
      "targeting": {
        "ref": "TARGET_PENETRATE",
        "scope": [
          "Enemy"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": true,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 1,
        "resource_costs": {}
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_PENETRATE",
          "template": "focused_strain",
          "ordered_steps": [
            {
              "type": "ModifyMeter",
              "meter": "Strain",
              "direction": "damage",
              "formula": "base_effectiveness",
              "target": "selected_enemy"
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_STRAIN_ATTACK",
        "primary_attributes": [
          {
            "attribute": "Charm",
            "weight": 0.55
          },
          {
            "attribute": "Dominance",
            "weight": 0.25
          },
          {
            "attribute": "Submission",
            "weight": 0.2
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "single",
          "aspects": [
            "Crotch"
          ],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 10,
        "output_cap": 40,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 2,
        "action_cost": 1
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": {
          "required": "CAPABILITY_P_GROWTH",
          "owner": "Alya"
        }
      },
      "presentation": {
        "ref": "PRES_PENETRATE",
        "display_name": "Penetrate",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "Requires P-growth; focused Strain attack"
    },
    "A_PENETRATION": {
      "id": "A_PENETRATION",
      "display_name": "A-penetration",
      "legacy_aliases": [],
      "kind": "Active",
      "tier": "Tier 3",
      "skill_point_cost": 3,
      "requirements": {
        "all_of": [
          {
            "type": "capability",
            "id": "CAPABILITY_P_GROWTH",
            "scope": "actor",
            "owner": "Alya"
          }
        ],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "ACT_II_COMPLETE",
      "targeting": {
        "ref": "TARGET_A_PENETRATION",
        "scope": [
          "Enemy"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": true,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 1,
        "resource_costs": {}
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_A_PENETRATION",
          "template": "strain_control_rider",
          "ordered_steps": [
            {
              "type": "ModifyMeter",
              "meter": "Strain",
              "direction": "damage",
              "formula": "base_effectiveness",
              "target": "selected_enemy"
            },
            {
              "type": "ApplyEffect",
              "effect_kind": "ControlState",
              "target": "selected_enemy",
              "duration_turns": 1,
              "resistance": "ControlResistance",
              "blocked_action_tags": [
                "Mobility"
              ],
              "not_full_disable": true
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_STRAIN_CONTROL",
        "primary_attributes": [
          {
            "attribute": "Charm",
            "weight": 0.35
          },
          {
            "attribute": "Dominance",
            "weight": 0.35
          },
          {
            "attribute": "Soul",
            "weight": 0.3
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "single",
          "aspects": [
            "Crotch"
          ],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 8,
        "output_cap": 40,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 2,
        "action_cost": 1
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": {
          "required": "CAPABILITY_P_GROWTH",
          "owner": "Alya"
        }
      },
      "presentation": {
        "ref": "PRES_A_PENETRATION",
        "display_name": "A-penetration",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "Requires P-growth; Strain plus resisted control rider for 1 turn"
    },
    "STOMP": {
      "id": "STOMP",
      "display_name": "Stomp",
      "legacy_aliases": [],
      "kind": "Active",
      "tier": "Tier 3",
      "skill_point_cost": 3,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "ACT_II_COMPLETE",
      "targeting": {
        "ref": "TARGET_STOMP",
        "scope": [
          "Enemy"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": true,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 1,
        "resource_costs": {}
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_STOMP",
          "template": "strain_to_vitality",
          "ordered_steps": [
            {
              "type": "ModifyMeter",
              "meter": "Vitality",
              "direction": "damage",
              "target": "selected_enemy",
              "formula": "base_effectiveness*(1+min(0.5,0.4*target_strain_ratio))",
              "threshold": {
                "meter": "Strain",
                "minimum_ratio": 0.6
              },
              "bonus_cap": 0.5,
              "snapshot": "target_strain_at_validation"
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_VITALITY_ATTACK",
        "primary_attributes": [
          {
            "attribute": "Body",
            "weight": 0.45
          },
          {
            "attribute": "Sadism",
            "weight": 0.35
          },
          {
            "attribute": "Agility",
            "weight": 0.2
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "single",
          "aspects": [
            "Crotch"
          ],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 9,
        "output_cap": 40,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 2,
        "action_cost": 1
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_STOMP",
        "display_name": "Stomp",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "Vitality damage +0.4x at target Strain >= 60%; bonus cap +50%"
    },
    "SUMMON_TENTACLES": {
      "id": "SUMMON_TENTACLES",
      "display_name": "Summon Tentacles",
      "legacy_aliases": [],
      "kind": "Active",
      "tier": "Tier 3",
      "skill_point_cost": 3,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "ACT_II_COMPLETE",
      "targeting": {
        "ref": "TARGET_SUMMON_TENTACLES",
        "scope": [
          "Enemies",
          "Allies",
          "Self"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": false,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 1,
        "resource_costs": {
          "Resolve": 2
        }
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_SUMMON_TENTACLES",
          "template": "all_sides_area",
          "ordered_steps": [
            {
              "type": "SnapshotTargets",
              "scope": "enabled_sides",
              "at": "validation",
              "sides": [
                "Enemies",
                "Allies",
                "Self"
              ]
            },
            {
              "type": "ModifyMeter",
              "meter": "Strain",
              "direction": "damage",
              "formula": "base_effectiveness",
              "per_target_cap": 18,
              "target_snapshot": "validation",
              "deterministic_order": [
                "enemies",
                "allies",
                "self"
              ],
              "friendly_fire": true
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_AREA_STRAIN",
        "primary_attributes": [
          {
            "attribute": "Charm",
            "weight": 0.4
          },
          {
            "attribute": "Dominance",
            "weight": 0.35
          },
          {
            "attribute": "Submission",
            "weight": 0.25
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "none",
          "aspects": [],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 6,
        "output_cap": 40,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 3,
        "action_cost": 1
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_SUMMON_TENTACLES",
        "display_name": "Summon Tentacles",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "Strain to validation snapshot of enabled sides; deterministic order"
    },
    "SKILL_ABSOLUTE_CONTROL": {
      "id": "SKILL_ABSOLUTE_CONTROL",
      "display_name": "Absolute Control",
      "legacy_aliases": [
        "Enslave"
      ],
      "kind": "Active",
      "tier": "Tier 3",
      "skill_point_cost": 3,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "ACT_II_COMPLETE",
      "targeting": {
        "ref": "TARGET_SKILL_ABSOLUTE_CONTROL",
        "scope": [
          "Enemy"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": true,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 1,
        "resource_costs": {
          "Command": 3,
          "Pressure": 2
        }
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_SKILL_ABSOLUTE_CONTROL",
          "template": "absolute_control",
          "ordered_steps": [
            {
              "type": "RequestOutcome",
              "target": "selected_enemy",
              "outcome": "authored_one_of_Yield_Disable_Capture",
              "threshold_ratio": 0.8,
              "resistance": "ControlResistance",
              "invalid_if_outcome_not_permitted": true,
              "no_implicit_defeat": true,
              "no_global_victory": true
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_FINISHER",
        "primary_attributes": [
          {
            "attribute": "Dominance",
            "weight": 0.4
          },
          {
            "attribute": "Soul",
            "weight": 0.35
          },
          {
            "attribute": "Charm",
            "weight": 0.25
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "single",
          "aspects": [
            "Mind"
          ],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 12,
        "output_cap": 40,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 4,
        "action_cost": 1
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": {
          "allowed_outcomes": [
            "Yield",
            "Disable",
            "Capture"
          ],
          "never_force_global_victory": true
        },
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_SKILL_ABSOLUTE_CONTROL",
        "display_name": "Absolute Control",
        "legacy_aliases": [
          "Enslave"
        ]
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "Merged Enslave identity; requests one authored Yield, Disable, or Capture outcome"
    },
    "G_BANG": {
      "id": "G_BANG",
      "display_name": "G-bang",
      "legacy_aliases": [],
      "kind": "Active",
      "tier": "Tier 3",
      "skill_point_cost": 3,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "ACT_II_COMPLETE",
      "targeting": {
        "ref": "TARGET_G_BANG",
        "scope": [
          "Enemies"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": true,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 1,
        "resource_costs": {}
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_G_BANG",
          "template": "group_bonus_area",
          "ordered_steps": [
            {
              "type": "SnapshotTargets",
              "scope": "valid_enemies",
              "at": "validation"
            },
            {
              "type": "ModifyMeter",
              "meter": "Strain",
              "direction": "damage",
              "formula": "base_effectiveness*min(1+0.10*(N-1),1.30)",
              "target_snapshot": "validation",
              "total_cap": 36
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_AREA_STRAIN",
        "primary_attributes": [
          {
            "attribute": "Charm",
            "weight": 0.4
          },
          {
            "attribute": "Dominance",
            "weight": 0.35
          },
          {
            "attribute": "Submission",
            "weight": 0.25
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "none",
          "aspects": [],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 6,
        "output_cap": 40,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 2,
        "action_cost": 1
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_G_BANG",
        "display_name": "G-bang",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "Area Strain; +10% per additional enemy, max +30%; total cap"
    },
    "BKKAKE": {
      "id": "BKKAKE",
      "display_name": "Bkakke",
      "legacy_aliases": [],
      "kind": "Active",
      "tier": "Tier 3",
      "skill_point_cost": 3,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "ACT_II_COMPLETE",
      "targeting": {
        "ref": "TARGET_BKKAKE",
        "scope": [
          "Enemies",
          "Self"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": false,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 1,
        "resource_costs": {
          "Command": 3,
          "Pressure": 2
        }
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_BKKAKE",
          "template": "all_target_finisher",
          "ordered_steps": [
            {
              "type": "SnapshotTargets",
              "scope": "valid_enemies",
              "at": "validation"
            },
            {
              "type": "RequestOutcomePerTarget",
              "outcome": "authored_per_target_outcome",
              "threshold_ratio": 0.8,
              "allowed_outcomes": [
                "Yield",
                "Disable",
                "Capture"
              ],
              "partial_success_persists": true
            },
            {
              "type": "OnEachFailedTarget",
              "type2": "ModifyMeter",
              "target": "self",
              "meter": "Strain",
              "direction": "damage",
              "amount": 12,
              "can_trigger_overflow": true
            },
            {
              "type": "GlobalVictory",
              "requires": "all_target_requests_succeeded"
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_FINISHER",
        "primary_attributes": [
          {
            "attribute": "Dominance",
            "weight": 0.4
          },
          {
            "attribute": "Soul",
            "weight": 0.35
          },
          {
            "attribute": "Charm",
            "weight": 0.25
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "arithmetic_mean",
          "aspects": [
            "Mouth",
            "Breasts"
          ],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 12,
        "output_cap": 40,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 4,
        "action_cost": 1
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": {
          "allowed_outcomes": [
            "Yield",
            "Disable",
            "Capture"
          ],
          "never_force_global_victory": true
        },
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_BKKAKE",
        "display_name": "Bkakke",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "Successful outcomes persist; each failed target adds 12 Strain to Alya; all must succeed for victory"
    },
    "DEEPTH": {
      "id": "DEEPTH",
      "display_name": "Deepth",
      "legacy_aliases": [],
      "kind": "Active",
      "tier": "Tier 3",
      "skill_point_cost": 3,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "ACT_II_COMPLETE",
      "targeting": {
        "ref": "TARGET_DEEPTH",
        "scope": [
          "Enemy"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": true,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 1,
        "resource_costs": {}
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_DEEPTH",
          "template": "focused_strain",
          "ordered_steps": [
            {
              "type": "ModifyMeter",
              "meter": "Strain",
              "direction": "damage",
              "formula": "base_effectiveness",
              "target": "selected_enemy"
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_STRAIN_ATTACK",
        "primary_attributes": [
          {
            "attribute": "Charm",
            "weight": 0.55
          },
          {
            "attribute": "Dominance",
            "weight": 0.25
          },
          {
            "attribute": "Submission",
            "weight": 0.2
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "single",
          "aspects": [
            "Mouth"
          ],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 10,
        "output_cap": 40,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 2,
        "action_cost": 1
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_DEEPTH",
        "display_name": "Deepth",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "Basic focused Strain with distinct Mouth affinity"
    },
    "WORSHIP_C": {
      "id": "WORSHIP_C",
      "display_name": "Worship C",
      "legacy_aliases": [],
      "kind": "Active",
      "tier": "Tier 3",
      "skill_point_cost": 3,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "ACT_II_COMPLETE",
      "targeting": {
        "ref": "TARGET_WORSHIP_C",
        "scope": [
          "Enemies"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": true,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 1,
        "resource_costs": {}
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_WORSHIP_C",
          "template": "area_intent_bias",
          "ordered_steps": [
            {
              "type": "SnapshotTargets",
              "scope": "valid_enemies",
              "at": "validation"
            },
            {
              "type": "ChangeIntent",
              "target_snapshot": "validation",
              "bias": "StrainOriented",
              "duration_turns": 2,
              "resistance": "MentalControlResistance"
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_CHARM_SKILL_COMMAND",
        "primary_attributes": [
          {
            "attribute": "Charm",
            "weight": 0.5
          },
          {
            "attribute": "Dominance",
            "weight": 0.3
          },
          {
            "attribute": "Soul",
            "weight": 0.2
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "arithmetic_mean",
          "aspects": [
            "Breasts",
            "Mouth"
          ],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 6,
        "output_cap": 40,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 2,
        "action_cost": 1
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_WORSHIP_C",
        "display_name": "Worship C",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "Area intent bias only; no unrelated vulnerability effect"
    },
    "ECSTASY_AFTERSHOCKS": {
      "id": "ECSTASY_AFTERSHOCKS",
      "display_name": "Ecstasy Aftershocks",
      "legacy_aliases": [],
      "kind": "Passive",
      "tier": "Tier 3",
      "skill_point_cost": 3,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "ACT_II_COMPLETE",
      "targeting": {
        "ref": "TARGET_ECSTASY_AFTERSHOCKS",
        "scope": [
          "Enemies"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": false,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 0,
        "resource_costs": {}
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_ECSTASY_AFTERSHOCKS",
          "template": "overflow_retaliation",
          "ordered_steps": [
            {
              "type": "ListenEvent",
              "event": "OverflowResolved",
              "frequency": "once_per_affected_actor_per_resolved_action",
              "recursion_guard": true,
              "max_chain_depth": 1,
              "output_cap": 12,
              "listener_priority": 20
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_SOUL_OVERFLOW",
        "primary_attributes": [
          {
            "attribute": "Soul",
            "weight": 0.45
          },
          {
            "attribute": "Dominance",
            "weight": 0.3
          },
          {
            "attribute": "Masochism",
            "weight": 0.25
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "none",
          "aspects": [],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 6,
        "output_cap": 40,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 0,
        "action_cost": 0
      },
      "rules": {
        "chain": null,
        "overflow": {
          "event": "OverflowResolved",
          "frequency": "once_per_affected_actor_per_resolved_action",
          "max_chain_depth": 1,
          "recursion_guard": true,
          "listener_priority": 20
        },
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_ECSTASY_AFTERSHOCKS",
        "display_name": "Ecstasy Aftershocks",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "Overflow listener retaliates against enemies; cap 12 per event"
    },
    "DIVINE_HEALTH": {
      "id": "DIVINE_HEALTH",
      "display_name": "Divine Health",
      "legacy_aliases": [],
      "kind": "Passive",
      "tier": "Tier 3",
      "skill_point_cost": 3,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "ACT_II_COMPLETE",
      "targeting": {
        "ref": "TARGET_DIVINE_HEALTH",
        "scope": [
          "Allies"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": false,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 0,
        "resource_costs": {}
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_DIVINE_HEALTH",
          "template": "recovery_resistance",
          "ordered_steps": [
            {
              "type": "ListenEvent",
              "event": "AllyRecoverySucceeded",
              "predicate": "recovered_ally_is_target",
              "once_per_recovery": true
            },
            {
              "type": "ApplyEffect",
              "effect_kind": "DebuffResistance",
              "target": "recovered_ally",
              "magnitude": 0.15,
              "duration_turns": 1,
              "stack_policy": "refresh"
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_SUPPORT_RECOVERY",
        "primary_attributes": [
          {
            "attribute": "Soul",
            "weight": 0.35
          },
          {
            "attribute": "Vitality",
            "weight": 0.35
          },
          {
            "attribute": "Submission",
            "weight": 0.3
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "single",
          "aspects": [
            "Mind"
          ],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 8,
        "output_cap": 40,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 0,
        "action_cost": 0
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_DIVINE_HEALTH",
        "display_name": "Divine Health",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "After successful recovery, ally gains 15% debuff resistance for 1 turn"
    },
    "SKILL_PROVOKE": {
      "id": "SKILL_PROVOKE",
      "display_name": "Provoke",
      "legacy_aliases": [],
      "kind": "Active",
      "tier": "Tier 1",
      "skill_point_cost": 1,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "none",
      "targeting": {
        "ref": "TARGET_SKILL_PROVOKE",
        "scope": [
          "Enemy"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": true,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 1,
        "resource_costs": {}
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_SKILL_PROVOKE",
          "template": "provoke",
          "ordered_steps": [
            {
              "type": "ChangeIntent",
              "target": "selected_enemy",
              "preferred_target": "selected_actor",
              "bias": "PreferDeclaredActor",
              "duration_turns": 1,
              "resistance": "TauntResistance"
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_CHARM_SKILL_COMMAND",
        "primary_attributes": [
          {
            "attribute": "Charm",
            "weight": 0.5
          },
          {
            "attribute": "Dominance",
            "weight": 0.3
          },
          {
            "attribute": "Soul",
            "weight": 0.2
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "single",
          "aspects": [
            "Mind"
          ],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 6,
        "output_cap": 24,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 0,
        "action_cost": 1
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_SKILL_PROVOKE",
        "display_name": "Provoke",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "Change enemy target preference toward selected actor for 1 turn"
    },
    "SKILL_ENDURE": {
      "id": "SKILL_ENDURE",
      "display_name": "Endure",
      "legacy_aliases": [],
      "kind": "Active",
      "tier": "Tier 1",
      "skill_point_cost": 1,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "none",
      "targeting": {
        "ref": "TARGET_SKILL_ENDURE",
        "scope": [
          "Self"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": false,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 1,
        "resource_costs": {
          "Resolve": 1
        }
      },
      "generated_resources": {
        "Fortitude": {
          "amount": 1,
          "cap": 2
        }
      },
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_SKILL_ENDURE",
          "template": "endure",
          "ordered_steps": [
            {
              "type": "ApplyEffect",
              "effect_kind": "IncomingVitalityDamageReduction",
              "target": "self",
              "magnitude": 0.3,
              "expires_after": "next_incoming_vitality_hit",
              "duration_turns": 1
            },
            {
              "type": "ModifyResource",
              "resource": "Fortitude",
              "direction": "gain",
              "amount": 1,
              "cap": 2
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_AGILITY_DEFENSE",
        "primary_attributes": [
          {
            "attribute": "Agility",
            "weight": 0.45
          },
          {
            "attribute": "Body",
            "weight": 0.3
          },
          {
            "attribute": "Masochism",
            "weight": 0.25
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "none",
          "aspects": [],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 6,
        "output_cap": 24,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 0,
        "action_cost": 1
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_SKILL_ENDURE",
        "display_name": "Endure",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "Reduce next incoming Vitality damage 30%; generate 1 Fortitude, cap 2"
    },
    "SKILL_COUNTER": {
      "id": "SKILL_COUNTER",
      "display_name": "Counter",
      "legacy_aliases": [],
      "kind": "Active",
      "tier": "Tier 2",
      "skill_point_cost": 2,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "ACT_I_COMPLETE",
      "targeting": {
        "ref": "TARGET_SKILL_COUNTER",
        "scope": [
          "Enemy"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": true,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 1,
        "resource_costs": {
          "Resolve": 1
        }
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_SKILL_COUNTER",
          "template": "counter",
          "ordered_steps": [
            {
              "type": "ApplyEffect",
              "effect_kind": "CounterWindow",
              "target": "self",
              "trigger": "declared_enemy_action_resolves",
              "duration_turns": 1,
              "max_triggers": 1
            },
            {
              "type": "OnTrigger",
              "event": "DeclaredEnemyActionResolved",
              "effect": {
                "type": "ModifyMeter",
                "meter": "Vitality",
                "direction": "damage",
                "target": "source_enemy",
                "formula": "min(0.5*base_effectiveness,12)"
              }
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_AGILITY_DEFENSE",
        "primary_attributes": [
          {
            "attribute": "Agility",
            "weight": 0.45
          },
          {
            "attribute": "Body",
            "weight": 0.3
          },
          {
            "attribute": "Masochism",
            "weight": 0.25
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "none",
          "aspects": [],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 6,
        "output_cap": 32,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 0,
        "action_cost": 1
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_SKILL_COUNTER",
        "display_name": "Counter",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "After declared enemy action, retaliate once for bounded Vitality damage"
    },
    "SKILL_COMMAND": {
      "id": "SKILL_COMMAND",
      "display_name": "Command",
      "legacy_aliases": [],
      "kind": "Active",
      "tier": "Tier 1",
      "skill_point_cost": 1,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "none",
      "targeting": {
        "ref": "TARGET_SKILL_COMMAND",
        "scope": [
          "Self"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": false,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 1,
        "resource_costs": {}
      },
      "generated_resources": {
        "Command": {
          "amount": 4,
          "cap": 8
        }
      },
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_SKILL_COMMAND",
          "template": "command_generator",
          "ordered_steps": [
            {
              "type": "ModifyResource",
              "resource": "Command",
              "direction": "gain",
              "amount": 4,
              "cap": 8
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_CHARM_SKILL_COMMAND",
        "primary_attributes": [
          {
            "attribute": "Charm",
            "weight": 0.5
          },
          {
            "attribute": "Dominance",
            "weight": 0.3
          },
          {
            "attribute": "Soul",
            "weight": 0.2
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "single",
          "aspects": [
            "Mind"
          ],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 6,
        "output_cap": 24,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 0,
        "action_cost": 1
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_SKILL_COMMAND",
        "display_name": "Command",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "Generate 4 Command; does not spend Command"
    },
    "SKILL_RECOVER_COMPOSURE": {
      "id": "SKILL_RECOVER_COMPOSURE",
      "display_name": "Recover Composure",
      "legacy_aliases": [],
      "kind": "Active",
      "tier": "Tier 1",
      "skill_point_cost": 1,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "none",
      "targeting": {
        "ref": "TARGET_SKILL_RECOVER_COMPOSURE",
        "scope": [
          "Self"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": false,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 1,
        "resource_costs": {}
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_SKILL_RECOVER_COMPOSURE",
          "template": "recover_strain",
          "ordered_steps": [
            {
              "type": "ModifyMeter",
              "meter": "Strain",
              "direction": "restore",
              "amount": 20,
              "target": "self"
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_SUPPORT_RECOVERY",
        "primary_attributes": [
          {
            "attribute": "Soul",
            "weight": 0.35
          },
          {
            "attribute": "Vitality",
            "weight": 0.35
          },
          {
            "attribute": "Submission",
            "weight": 0.3
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "single",
          "aspects": [
            "Mind"
          ],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 8,
        "output_cap": 24,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 0,
        "action_cost": 1
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_SKILL_RECOVER_COMPOSURE",
        "display_name": "Recover Composure",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "Reduce own Strain by 20; no cleanse by default"
    },
    "SKILL_EXPLOIT_WEAKNESS": {
      "id": "SKILL_EXPLOIT_WEAKNESS",
      "display_name": "Exploit Weakness",
      "legacy_aliases": [],
      "kind": "Active",
      "tier": "Tier 2",
      "skill_point_cost": 2,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "ACT_I_COMPLETE",
      "targeting": {
        "ref": "TARGET_SKILL_EXPLOIT_WEAKNESS",
        "scope": [
          "Enemy"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": true,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 1,
        "resource_costs": {
          "Pressure": 1
        }
      },
      "generated_resources": {
        "Pressure": {
          "amount": 2,
          "cap": 6
        }
      },
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_SKILL_EXPLOIT_WEAKNESS",
          "template": "exploit_weakness",
          "ordered_steps": [
            {
              "type": "ConsumeTag",
              "target": "selected_enemy",
              "tag": "Vulnerability",
              "max_stacks": 1
            },
            {
              "type": "ModifyResource",
              "resource": "Pressure",
              "direction": "gain",
              "amount": 2,
              "cap": 6
            },
            {
              "type": "ApplyEffect",
              "effect_kind": "NextQualifyingEffectBonus",
              "target": "self",
              "magnitude": 0.25,
              "duration_turns": 1,
              "expires_after": "next_qualifying_effect"
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_STRAIN_CONTROL",
        "primary_attributes": [
          {
            "attribute": "Charm",
            "weight": 0.35
          },
          {
            "attribute": "Dominance",
            "weight": 0.35
          },
          {
            "attribute": "Soul",
            "weight": 0.3
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "single",
          "aspects": [
            "Mind"
          ],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 8,
        "output_cap": 32,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 0,
        "action_cost": 1
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_SKILL_EXPLOIT_WEAKNESS",
        "display_name": "Exploit Weakness",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "Consume tagged vulnerability; generate 2 Pressure and boost next qualifying effect 25%"
    },
    "SKILL_BREAK_RESISTANCE": {
      "id": "SKILL_BREAK_RESISTANCE",
      "display_name": "Break Resistance",
      "legacy_aliases": [],
      "kind": "Active",
      "tier": "Tier 2",
      "skill_point_cost": 2,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "ACT_I_COMPLETE",
      "targeting": {
        "ref": "TARGET_SKILL_BREAK_RESISTANCE",
        "scope": [
          "Enemy"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": true,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 1,
        "resource_costs": {
          "Pressure": 1
        }
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_SKILL_BREAK_RESISTANCE",
          "template": "break_resistance",
          "ordered_steps": [
            {
              "type": "ModifyStat",
              "target": "selected_enemy",
              "stat": "RelevantControlResistance",
              "operation": "multiply",
              "value": 0.8,
              "duration_turns": 2
            },
            {
              "type": "ModifyResource",
              "resource": "BreakProgress",
              "direction": "gain",
              "amount": 1,
              "target": "selected_enemy"
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_SOUL_CONTROL",
        "primary_attributes": [
          {
            "attribute": "Soul",
            "weight": 0.55
          },
          {
            "attribute": "Dominance",
            "weight": 0.25
          },
          {
            "attribute": "Charm",
            "weight": 0.2
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "single",
          "aspects": [
            "Mind"
          ],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 7,
        "output_cap": 32,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 0,
        "action_cost": 1
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_SKILL_BREAK_RESISTANCE",
        "display_name": "Break Resistance",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "Reduce relevant resistance 20% and add 1 Break progress for 2 turns; not disable"
    },
    "SKILL_TURN_THE_TABLES": {
      "id": "SKILL_TURN_THE_TABLES",
      "display_name": "Turn the Tables",
      "legacy_aliases": [],
      "kind": "Active",
      "tier": "Tier 2",
      "skill_point_cost": 2,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "ACT_I_COMPLETE",
      "targeting": {
        "ref": "TARGET_SKILL_TURN_THE_TABLES",
        "scope": [
          "Self"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": false,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 1,
        "resource_costs": {
          "Resolve": 1
        }
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_SKILL_TURN_THE_TABLES",
          "template": "turn_tables",
          "ordered_steps": [
            {
              "type": "ConsumeEvent",
              "event": "QualifyingRecentEnemyHit",
              "max_age_actions": 1,
              "max_uses": 1
            },
            {
              "type": "ModifyMeter",
              "meter": "Strain",
              "direction": "restore",
              "amount": 10,
              "target": "self"
            },
            {
              "type": "ModifyMeter",
              "meter": "Vitality",
              "direction": "damage",
              "formula": "0.5*base_effectiveness",
              "target": "source_enemy"
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_AGILITY_DEFENSE",
        "primary_attributes": [
          {
            "attribute": "Agility",
            "weight": 0.45
          },
          {
            "attribute": "Body",
            "weight": 0.3
          },
          {
            "attribute": "Masochism",
            "weight": 0.25
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "none",
          "aspects": [],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 6,
        "output_cap": 32,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 0,
        "action_cost": 1
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_SKILL_TURN_THE_TABLES",
        "display_name": "Turn the Tables",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "Once after qualifying recent enemy hit, recover 10 Strain and retaliate at 0.5x"
    },
    "SKILL_FOCUS_SURGE": {
      "id": "SKILL_FOCUS_SURGE",
      "display_name": "Focus Surge",
      "legacy_aliases": [],
      "kind": "Active",
      "tier": "Tier 2",
      "skill_point_cost": 2,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "ACT_I_COMPLETE",
      "targeting": {
        "ref": "TARGET_SKILL_FOCUS_SURGE",
        "scope": [
          "Self"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": false,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 1,
        "resource_costs": {
          "Pressure": 1
        }
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_SKILL_FOCUS_SURGE",
          "template": "focus_surge",
          "ordered_steps": [
            {
              "type": "ApplyEffect",
              "effect_kind": "NextQualifyingActionBonus",
              "target": "self",
              "magnitude": 0.25,
              "duration_turns": 2,
              "expires_after": "next_qualifying_action",
              "stack_policy": "refresh"
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_SOUL_DOT",
        "primary_attributes": [
          {
            "attribute": "Soul",
            "weight": 0.45
          },
          {
            "attribute": "Charm",
            "weight": 0.3
          },
          {
            "attribute": "Dominance",
            "weight": 0.25
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "single",
          "aspects": [
            "Mind"
          ],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 5,
        "output_cap": 32,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 0,
        "action_cost": 1
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_SKILL_FOCUS_SURGE",
        "display_name": "Focus Surge",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "Next qualifying action +25%; expires after action or 2 turns; no stacking"
    },
    "SKILL_DIRECT_ALLY": {
      "id": "SKILL_DIRECT_ALLY",
      "display_name": "Direct Ally",
      "legacy_aliases": [],
      "kind": "Active",
      "tier": "Tier 2",
      "skill_point_cost": 2,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "ACT_I_COMPLETE",
      "targeting": {
        "ref": "TARGET_SKILL_DIRECT_ALLY",
        "scope": [
          "Ally"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": true,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 1,
        "resource_costs": {}
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_SKILL_DIRECT_ALLY",
          "template": "direct_ally",
          "ordered_steps": [
            {
              "type": "ApplyEffect",
              "effect_kind": "NextActionBonus",
              "target": "selected_ally",
              "magnitude": 0.15,
              "duration_turns": 2,
              "expires_after": "next_action",
              "grants_extra_action": false
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_CHARM_SKILL_COMMAND",
        "primary_attributes": [
          {
            "attribute": "Charm",
            "weight": 0.5
          },
          {
            "attribute": "Dominance",
            "weight": 0.3
          },
          {
            "attribute": "Soul",
            "weight": 0.2
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "single",
          "aspects": [
            "Mind"
          ],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 6,
        "output_cap": 32,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 0,
        "action_cost": 1
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_SKILL_DIRECT_ALLY",
        "display_name": "Direct Ally",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "Next ally action +15%; never grants extra action; 2 turns"
    },
    "SKILL_UNBROKEN": {
      "id": "SKILL_UNBROKEN",
      "display_name": "Unbroken",
      "legacy_aliases": [],
      "kind": "Passive",
      "tier": "Tier 3",
      "skill_point_cost": 3,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "ACT_II_COMPLETE",
      "targeting": {
        "ref": "TARGET_SKILL_UNBROKEN",
        "scope": [
          "Self"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": false,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 0,
        "resource_costs": {}
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_SKILL_UNBROKEN",
          "template": "unbroken",
          "ordered_steps": [
            {
              "type": "PreventOutcome",
              "target": "self",
              "outcomes": [
                "Defeat",
                "Disable"
              ],
              "max_triggers_per_encounter": 1,
              "only_if": "explicitly_eligible_event",
              "never_grants_immunity": true
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_AGILITY_DEFENSE",
        "primary_attributes": [
          {
            "attribute": "Agility",
            "weight": 0.45
          },
          {
            "attribute": "Body",
            "weight": 0.3
          },
          {
            "attribute": "Masochism",
            "weight": 0.25
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "none",
          "aspects": [],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 6,
        "output_cap": 40,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 0,
        "action_cost": 0
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_SKILL_UNBROKEN",
        "display_name": "Unbroken",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "Prevent one eligible defeat/disable per encounter; no general immunity"
    },
    "SKILL_OVERFLOW_ENGINE": {
      "id": "SKILL_OVERFLOW_ENGINE",
      "display_name": "Overflow Engine",
      "legacy_aliases": [],
      "kind": "Active",
      "tier": "Tier 3",
      "skill_point_cost": 3,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "ACT_II_COMPLETE",
      "targeting": {
        "ref": "TARGET_SKILL_OVERFLOW_ENGINE",
        "scope": [
          "Self"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": false,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 1,
        "resource_costs": {
          "Command": 2
        }
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_SKILL_OVERFLOW_ENGINE",
          "template": "overflow_engine",
          "ordered_steps": [
            {
              "type": "ListenEvent",
              "event": "OverflowResolved",
              "frequency": "once_per_affected_actor_per_resolved_action",
              "recursion_guard": true,
              "max_chain_depth": 1,
              "output_cap": 16,
              "listener_priority": 30
            },
            {
              "type": "ConfiguredConversion",
              "allowed_outputs": [
                "restore_strain",
                "enemy_strain_damage",
                "gain_command"
              ],
              "max_chain_depth": 1
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_SOUL_OVERFLOW",
        "primary_attributes": [
          {
            "attribute": "Soul",
            "weight": 0.45
          },
          {
            "attribute": "Dominance",
            "weight": 0.3
          },
          {
            "attribute": "Masochism",
            "weight": 0.25
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "single",
          "aspects": [
            "Mind"
          ],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 6,
        "output_cap": 40,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 3,
        "action_cost": 1
      },
      "rules": {
        "chain": null,
        "overflow": {
          "event": "OverflowResolved",
          "frequency": "once_per_affected_actor_per_resolved_action",
          "max_chain_depth": 1,
          "recursion_guard": true,
          "listener_priority": 30
        },
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_SKILL_OVERFLOW_ENGINE",
        "display_name": "Overflow Engine",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "Configured conversion of next Overflow event; cap 16"
    },
    "SKILL_MUTUAL_RUIN": {
      "id": "SKILL_MUTUAL_RUIN",
      "display_name": "Mutual Ruin",
      "legacy_aliases": [],
      "kind": "Active",
      "tier": "Tier 3",
      "skill_point_cost": 3,
      "requirements": {
        "all_of": [],
        "any_of": [],
        "none_of": []
      },
      "milestone_gate": "ACT_II_COMPLETE",
      "targeting": {
        "ref": "TARGET_SKILL_MUTUAL_RUIN",
        "scope": [
          "Enemy",
          "Self"
        ],
        "validation_snapshot": true,
        "invalid_if_no_valid_targets": false,
        "target_order": "stable_actor_id_ascending"
      },
      "costs": {
        "action_points": 1,
        "resource_costs": {
          "Resolve": 2
        }
      },
      "generated_resources": {},
      "conditions": {},
      "effects": [
        {
          "effect_id": "FX_SKILL_MUTUAL_RUIN",
          "template": "mutual_ruin",
          "ordered_steps": [
            {
              "type": "ModifyMeter",
              "meter": "Vitality",
              "direction": "damage",
              "amount": 15,
              "target": "self"
            },
            {
              "type": "ModifyMeter",
              "meter": "Strain",
              "direction": "damage",
              "amount": 10,
              "target": "self"
            },
            {
              "type": "ModifyMeter",
              "meter": "Vitality",
              "direction": "damage",
              "formula": "min(1.5*base_effectiveness,36)",
              "target": "selected_enemy"
            },
            {
              "type": "EvaluateOutcome",
              "respect_encounter_contract": true,
              "no_implicit_defeat": true
            }
          ]
        }
      ],
      "scaling": {
        "profile_id": "SCALE_VITALITY_ATTACK",
        "primary_attributes": [
          {
            "attribute": "Body",
            "weight": 0.45
          },
          {
            "attribute": "Sadism",
            "weight": 0.35
          },
          {
            "attribute": "Agility",
            "weight": 0.2
          }
        ],
        "weighted_attribute_formula": "sum(attribute_value * weight)",
        "aspect_affinity": {
          "mode": "none",
          "aspects": [],
          "formula": "clamp(1 + affinity_percent/200, 1.0, 1.5)"
        },
        "effectiveness_formula": "round((base_power + weighted_sum) * aspect_multiplier)",
        "base_power": 9,
        "output_cap": 40,
        "rounding": "nearest_integer_halves_away_from_zero",
        "resistance_order": [
          "base",
          "aspect_affinity",
          "target_resistance",
          "vulnerability_and_debuff",
          "cap",
          "meter_mutation"
        ]
      },
      "timing": {
        "duration_turns": 0,
        "tick": "none",
        "duration_decrement": "after_start_behavior",
        "refresh_policy": "replace_or_refresh",
        "stack_policy": "strongest_equivalent_only",
        "cooldown_actions": 4,
        "action_cost": 1
      },
      "rules": {
        "chain": null,
        "overflow": null,
        "outcome_interactions": [],
        "p_growth": null
      },
      "presentation": {
        "ref": "PRES_SKILL_MUTUAL_RUIN",
        "display_name": "Mutual Ruin",
        "legacy_aliases": []
      },
      "balance_status": "provisional_numeric_baseline_not_playtest_balanced",
      "semantic_note": "Pay 15 Vitality and 10 Strain for bounded high damage; cannot bypass encounter outcomes"
    }
  },
  "reference_index": {
    "REQ_SENSORY_ENHANCEMENT": "skills.SENSORY_ENHANCEMENT.requirements",
    "TARGET_SENSORY_ENHANCEMENT": "skills.SENSORY_ENHANCEMENT.targeting",
    "COST_SENSORY_ENHANCEMENT": "skills.SENSORY_ENHANCEMENT.costs",
    "GEN_SENSORY_ENHANCEMENT": "skills.SENSORY_ENHANCEMENT.generated_resources",
    "COND_SENSORY_ENHANCEMENT": "skills.SENSORY_ENHANCEMENT.conditions",
    "FX_SENSORY_ENHANCEMENT": "skills.SENSORY_ENHANCEMENT.effects",
    "PRES_SENSORY_ENHANCEMENT": "skills.SENSORY_ENHANCEMENT.presentation",
    "SCALE_STRAIN_CONTROL": "scaling_profiles.SCALE_STRAIN_CONTROL",
    "REQ_MSTRBATE": "skills.MSTRBATE.requirements",
    "TARGET_MSTRBATE": "skills.MSTRBATE.targeting",
    "COST_MSTRBATE": "skills.MSTRBATE.costs",
    "GEN_MSTRBATE": "skills.MSTRBATE.generated_resources",
    "COND_MSTRBATE": "skills.MSTRBATE.conditions",
    "FX_MSTRBATE": "skills.MSTRBATE.effects",
    "PRES_MSTRBATE": "skills.MSTRBATE.presentation",
    "REQ_DANCING_MOVES": "skills.DANCING_MOVES.requirements",
    "TARGET_DANCING_MOVES": "skills.DANCING_MOVES.targeting",
    "COST_DANCING_MOVES": "skills.DANCING_MOVES.costs",
    "GEN_DANCING_MOVES": "skills.DANCING_MOVES.generated_resources",
    "COND_DANCING_MOVES": "skills.DANCING_MOVES.conditions",
    "FX_DANCING_MOVES": "skills.DANCING_MOVES.effects",
    "PRES_DANCING_MOVES": "skills.DANCING_MOVES.presentation",
    "SCALE_AGILITY_DEFENSE": "scaling_profiles.SCALE_AGILITY_DEFENSE",
    "REQ_FLIRT": "skills.FLIRT.requirements",
    "TARGET_FLIRT": "skills.FLIRT.targeting",
    "COST_FLIRT": "skills.FLIRT.costs",
    "GEN_FLIRT": "skills.FLIRT.generated_resources",
    "COND_FLIRT": "skills.FLIRT.conditions",
    "FX_FLIRT": "skills.FLIRT.effects",
    "PRES_FLIRT": "skills.FLIRT.presentation",
    "SCALE_CHARM_SKILL_COMMAND": "scaling_profiles.SCALE_CHARM_SKILL_COMMAND",
    "REQ_HYPNOTIZE": "skills.HYPNOTIZE.requirements",
    "TARGET_HYPNOTIZE": "skills.HYPNOTIZE.targeting",
    "COST_HYPNOTIZE": "skills.HYPNOTIZE.costs",
    "GEN_HYPNOTIZE": "skills.HYPNOTIZE.generated_resources",
    "COND_HYPNOTIZE": "skills.HYPNOTIZE.conditions",
    "FX_HYPNOTIZE": "skills.HYPNOTIZE.effects",
    "PRES_HYPNOTIZE": "skills.HYPNOTIZE.presentation",
    "SCALE_SOUL_CONTROL": "scaling_profiles.SCALE_SOUL_CONTROL",
    "REQ_GET_SPANKED": "skills.GET_SPANKED.requirements",
    "TARGET_GET_SPANKED": "skills.GET_SPANKED.targeting",
    "COST_GET_SPANKED": "skills.GET_SPANKED.costs",
    "GEN_GET_SPANKED": "skills.GET_SPANKED.generated_resources",
    "COND_GET_SPANKED": "skills.GET_SPANKED.conditions",
    "FX_GET_SPANKED": "skills.GET_SPANKED.effects",
    "PRES_GET_SPANKED": "skills.GET_SPANKED.presentation",
    "SCALE_RESOLVE_RISK": "scaling_profiles.SCALE_RESOLVE_RISK",
    "REQ_SENSORY_DEPRIVATION": "skills.SENSORY_DEPRIVATION.requirements",
    "TARGET_SENSORY_DEPRIVATION": "skills.SENSORY_DEPRIVATION.targeting",
    "COST_SENSORY_DEPRIVATION": "skills.SENSORY_DEPRIVATION.costs",
    "GEN_SENSORY_DEPRIVATION": "skills.SENSORY_DEPRIVATION.generated_resources",
    "COND_SENSORY_DEPRIVATION": "skills.SENSORY_DEPRIVATION.conditions",
    "FX_SENSORY_DEPRIVATION": "skills.SENSORY_DEPRIVATION.effects",
    "PRES_SENSORY_DEPRIVATION": "skills.SENSORY_DEPRIVATION.presentation",
    "REQ_SPANK": "skills.SPANK.requirements",
    "TARGET_SPANK": "skills.SPANK.targeting",
    "COST_SPANK": "skills.SPANK.costs",
    "GEN_SPANK": "skills.SPANK.generated_resources",
    "COND_SPANK": "skills.SPANK.conditions",
    "FX_SPANK": "skills.SPANK.effects",
    "PRES_SPANK": "skills.SPANK.presentation",
    "SCALE_STRAIN_ATTACK": "scaling_profiles.SCALE_STRAIN_ATTACK",
    "REQ_INSTILL_PROTECTIVENESS": "skills.INSTILL_PROTECTIVENESS.requirements",
    "TARGET_INSTILL_PROTECTIVENESS": "skills.INSTILL_PROTECTIVENESS.targeting",
    "COST_INSTILL_PROTECTIVENESS": "skills.INSTILL_PROTECTIVENESS.costs",
    "GEN_INSTILL_PROTECTIVENESS": "skills.INSTILL_PROTECTIVENESS.generated_resources",
    "COND_INSTILL_PROTECTIVENESS": "skills.INSTILL_PROTECTIVENESS.conditions",
    "FX_INSTILL_PROTECTIVENESS": "skills.INSTILL_PROTECTIVENESS.effects",
    "PRES_INSTILL_PROTECTIVENESS": "skills.INSTILL_PROTECTIVENESS.presentation",
    "REQ_BLOWJOB": "skills.BLOWJOB.requirements",
    "TARGET_BLOWJOB": "skills.BLOWJOB.targeting",
    "COST_BLOWJOB": "skills.BLOWJOB.costs",
    "GEN_BLOWJOB": "skills.BLOWJOB.generated_resources",
    "COND_BLOWJOB": "skills.BLOWJOB.conditions",
    "FX_BLOWJOB": "skills.BLOWJOB.effects",
    "PRES_BLOWJOB": "skills.BLOWJOB.presentation",
    "REQ_LAY": "skills.LAY.requirements",
    "TARGET_LAY": "skills.LAY.targeting",
    "COST_LAY": "skills.LAY.costs",
    "GEN_LAY": "skills.LAY.generated_resources",
    "COND_LAY": "skills.LAY.conditions",
    "FX_LAY": "skills.LAY.effects",
    "PRES_LAY": "skills.LAY.presentation",
    "REQ_GROPE": "skills.GROPE.requirements",
    "TARGET_GROPE": "skills.GROPE.targeting",
    "COST_GROPE": "skills.GROPE.costs",
    "GEN_GROPE": "skills.GROPE.generated_resources",
    "COND_GROPE": "skills.GROPE.conditions",
    "FX_GROPE": "skills.GROPE.effects",
    "PRES_GROPE": "skills.GROPE.presentation",
    "REQ_SERVICE": "skills.SERVICE.requirements",
    "TARGET_SERVICE": "skills.SERVICE.targeting",
    "COST_SERVICE": "skills.SERVICE.costs",
    "GEN_SERVICE": "skills.SERVICE.generated_resources",
    "COND_SERVICE": "skills.SERVICE.conditions",
    "FX_SERVICE": "skills.SERVICE.effects",
    "PRES_SERVICE": "skills.SERVICE.presentation",
    "SCALE_SUPPORT_RECOVERY": "scaling_profiles.SCALE_SUPPORT_RECOVERY",
    "REQ_H_JOB": "skills.H_JOB.requirements",
    "TARGET_H_JOB": "skills.H_JOB.targeting",
    "COST_H_JOB": "skills.H_JOB.costs",
    "GEN_H_JOB": "skills.H_JOB.generated_resources",
    "COND_H_JOB": "skills.H_JOB.conditions",
    "FX_H_JOB": "skills.H_JOB.effects",
    "PRES_H_JOB": "skills.H_JOB.presentation",
    "SCALE_SOUL_DOT": "scaling_profiles.SCALE_SOUL_DOT",
    "REQ_BEND": "skills.BEND.requirements",
    "TARGET_BEND": "skills.BEND.targeting",
    "COST_BEND": "skills.BEND.costs",
    "GEN_BEND": "skills.BEND.generated_resources",
    "COND_BEND": "skills.BEND.conditions",
    "FX_BEND": "skills.BEND.effects",
    "PRES_BEND": "skills.BEND.presentation",
    "REQ_AS_CHAIN": "skills.AS_CHAIN.requirements",
    "TARGET_AS_CHAIN": "skills.AS_CHAIN.targeting",
    "COST_AS_CHAIN": "skills.AS_CHAIN.costs",
    "GEN_AS_CHAIN": "skills.AS_CHAIN.generated_resources",
    "COND_AS_CHAIN": "skills.AS_CHAIN.conditions",
    "FX_AS_CHAIN": "skills.AS_CHAIN.effects",
    "CHAIN_AS_CHAIN": "skills.AS_CHAIN.rules.chain",
    "PRES_AS_CHAIN": "skills.AS_CHAIN.presentation",
    "REQ_S_SYMBOL": "skills.S_SYMBOL.requirements",
    "TARGET_S_SYMBOL": "skills.S_SYMBOL.targeting",
    "COST_S_SYMBOL": "skills.S_SYMBOL.costs",
    "GEN_S_SYMBOL": "skills.S_SYMBOL.generated_resources",
    "COND_S_SYMBOL": "skills.S_SYMBOL.conditions",
    "FX_S_SYMBOL": "skills.S_SYMBOL.effects",
    "OVERFLOW_S_SYMBOL": "skills.S_SYMBOL.rules.overflow",
    "PRES_S_SYMBOL": "skills.S_SYMBOL.presentation",
    "SCALE_SOUL_OVERFLOW": "scaling_profiles.SCALE_SOUL_OVERFLOW",
    "REQ_OTHERWORLDLY_CHARM": "skills.OTHERWORLDLY_CHARM.requirements",
    "TARGET_OTHERWORLDLY_CHARM": "skills.OTHERWORLDLY_CHARM.targeting",
    "COST_OTHERWORLDLY_CHARM": "skills.OTHERWORLDLY_CHARM.costs",
    "GEN_OTHERWORLDLY_CHARM": "skills.OTHERWORLDLY_CHARM.generated_resources",
    "COND_OTHERWORLDLY_CHARM": "skills.OTHERWORLDLY_CHARM.conditions",
    "FX_OTHERWORLDLY_CHARM": "skills.OTHERWORLDLY_CHARM.effects",
    "PRES_OTHERWORLDLY_CHARM": "skills.OTHERWORLDLY_CHARM.presentation",
    "REQ_PIERCING_STARES": "skills.PIERCING_STARES.requirements",
    "TARGET_PIERCING_STARES": "skills.PIERCING_STARES.targeting",
    "COST_PIERCING_STARES": "skills.PIERCING_STARES.costs",
    "GEN_PIERCING_STARES": "skills.PIERCING_STARES.generated_resources",
    "COND_PIERCING_STARES": "skills.PIERCING_STARES.conditions",
    "FX_PIERCING_STARES": "skills.PIERCING_STARES.effects",
    "PRES_PIERCING_STARES": "skills.PIERCING_STARES.presentation",
    "REQ_SADISM": "skills.SADISM.requirements",
    "TARGET_SADISM": "skills.SADISM.targeting",
    "COST_SADISM": "skills.SADISM.costs",
    "GEN_SADISM": "skills.SADISM.generated_resources",
    "COND_SADISM": "skills.SADISM.conditions",
    "FX_SADISM": "skills.SADISM.effects",
    "PRES_SADISM": "skills.SADISM.presentation",
    "SCALE_VITALITY_ATTACK": "scaling_profiles.SCALE_VITALITY_ATTACK",
    "REQ_MASOCHISM": "skills.MASOCHISM.requirements",
    "TARGET_MASOCHISM": "skills.MASOCHISM.targeting",
    "COST_MASOCHISM": "skills.MASOCHISM.costs",
    "GEN_MASOCHISM": "skills.MASOCHISM.generated_resources",
    "COND_MASOCHISM": "skills.MASOCHISM.conditions",
    "FX_MASOCHISM": "skills.MASOCHISM.effects",
    "PRES_MASOCHISM": "skills.MASOCHISM.presentation",
    "REQ_MOANS": "skills.MOANS.requirements",
    "TARGET_MOANS": "skills.MOANS.targeting",
    "COST_MOANS": "skills.MOANS.costs",
    "GEN_MOANS": "skills.MOANS.generated_resources",
    "COND_MOANS": "skills.MOANS.conditions",
    "FX_MOANS": "skills.MOANS.effects",
    "PRES_MOANS": "skills.MOANS.presentation",
    "REQ_ENCOURAGE": "skills.ENCOURAGE.requirements",
    "TARGET_ENCOURAGE": "skills.ENCOURAGE.targeting",
    "COST_ENCOURAGE": "skills.ENCOURAGE.costs",
    "GEN_ENCOURAGE": "skills.ENCOURAGE.generated_resources",
    "COND_ENCOURAGE": "skills.ENCOURAGE.conditions",
    "FX_ENCOURAGE": "skills.ENCOURAGE.effects",
    "PRES_ENCOURAGE": "skills.ENCOURAGE.presentation",
    "REQ_FLAUNT": "skills.FLAUNT.requirements",
    "TARGET_FLAUNT": "skills.FLAUNT.targeting",
    "COST_FLAUNT": "skills.FLAUNT.costs",
    "GEN_FLAUNT": "skills.FLAUNT.generated_resources",
    "COND_FLAUNT": "skills.FLAUNT.conditions",
    "FX_FLAUNT": "skills.FLAUNT.effects",
    "PRES_FLAUNT": "skills.FLAUNT.presentation",
    "SCALE_AREA_STRAIN": "scaling_profiles.SCALE_AREA_STRAIN",
    "REQ_AUTOF": "skills.AUTOF.requirements",
    "TARGET_AUTOF": "skills.AUTOF.targeting",
    "COST_AUTOF": "skills.AUTOF.costs",
    "GEN_AUTOF": "skills.AUTOF.generated_resources",
    "COND_AUTOF": "skills.AUTOF.conditions",
    "FX_AUTOF": "skills.AUTOF.effects",
    "PRES_AUTOF": "skills.AUTOF.presentation",
    "REQ_APHRODISIAC": "skills.APHRODISIAC.requirements",
    "TARGET_APHRODISIAC": "skills.APHRODISIAC.targeting",
    "COST_APHRODISIAC": "skills.APHRODISIAC.costs",
    "GEN_APHRODISIAC": "skills.APHRODISIAC.generated_resources",
    "COND_APHRODISIAC": "skills.APHRODISIAC.conditions",
    "FX_APHRODISIAC": "skills.APHRODISIAC.effects",
    "PRES_APHRODISIAC": "skills.APHRODISIAC.presentation",
    "REQ_P_GROWTH": "skills.P_GROWTH.requirements",
    "TARGET_P_GROWTH": "skills.P_GROWTH.targeting",
    "COST_P_GROWTH": "skills.P_GROWTH.costs",
    "GEN_P_GROWTH": "skills.P_GROWTH.generated_resources",
    "COND_P_GROWTH": "skills.P_GROWTH.conditions",
    "FX_P_GROWTH": "skills.P_GROWTH.effects",
    "PRES_P_GROWTH": "skills.P_GROWTH.presentation",
    "SCALE_CAPABILITY": "scaling_profiles.SCALE_CAPABILITY",
    "REQ_FACESIT": "skills.FACESIT.requirements",
    "TARGET_FACESIT": "skills.FACESIT.targeting",
    "COST_FACESIT": "skills.FACESIT.costs",
    "GEN_FACESIT": "skills.FACESIT.generated_resources",
    "COND_FACESIT": "skills.FACESIT.conditions",
    "FX_FACESIT": "skills.FACESIT.effects",
    "PRES_FACESIT": "skills.FACESIT.presentation",
    "REQ_BONDAGE": "skills.BONDAGE.requirements",
    "TARGET_BONDAGE": "skills.BONDAGE.targeting",
    "COST_BONDAGE": "skills.BONDAGE.costs",
    "GEN_BONDAGE": "skills.BONDAGE.generated_resources",
    "COND_BONDAGE": "skills.BONDAGE.conditions",
    "FX_BONDAGE": "skills.BONDAGE.effects",
    "PRES_BONDAGE": "skills.BONDAGE.presentation",
    "REQ_BULLY": "skills.BULLY.requirements",
    "TARGET_BULLY": "skills.BULLY.targeting",
    "COST_BULLY": "skills.BULLY.costs",
    "GEN_BULLY": "skills.BULLY.generated_resources",
    "COND_BULLY": "skills.BULLY.conditions",
    "FX_BULLY": "skills.BULLY.effects",
    "PRES_BULLY": "skills.BULLY.presentation",
    "REQ_BITE": "skills.BITE.requirements",
    "TARGET_BITE": "skills.BITE.targeting",
    "COST_BITE": "skills.BITE.costs",
    "GEN_BITE": "skills.BITE.generated_resources",
    "COND_BITE": "skills.BITE.conditions",
    "FX_BITE": "skills.BITE.effects",
    "PRES_BITE": "skills.BITE.presentation",
    "REQ_BIND": "skills.BIND.requirements",
    "TARGET_BIND": "skills.BIND.targeting",
    "COST_BIND": "skills.BIND.costs",
    "GEN_BIND": "skills.BIND.generated_resources",
    "COND_BIND": "skills.BIND.conditions",
    "FX_BIND": "skills.BIND.effects",
    "PRES_BIND": "skills.BIND.presentation",
    "REQ_PROLONGED_PL": "skills.PROLONGED_PL.requirements",
    "TARGET_PROLONGED_PL": "skills.PROLONGED_PL.targeting",
    "COST_PROLONGED_PL": "skills.PROLONGED_PL.costs",
    "GEN_PROLONGED_PL": "skills.PROLONGED_PL.generated_resources",
    "COND_PROLONGED_PL": "skills.PROLONGED_PL.conditions",
    "FX_PROLONGED_PL": "skills.PROLONGED_PL.effects",
    "OVERFLOW_LOCK_PROLONGED_PL": "skills.PROLONGED_PL.effects",
    "PRES_PROLONGED_PL": "skills.PROLONGED_PL.presentation",
    "REQ_F_FK": "skills.F_FK.requirements",
    "TARGET_F_FK": "skills.F_FK.targeting",
    "COST_F_FK": "skills.F_FK.costs",
    "GEN_F_FK": "skills.F_FK.generated_resources",
    "COND_F_FK": "skills.F_FK.conditions",
    "FX_F_FK": "skills.F_FK.effects",
    "PRES_F_FK": "skills.F_FK.presentation",
    "REQ_PAIZURI": "skills.PAIZURI.requirements",
    "TARGET_PAIZURI": "skills.PAIZURI.targeting",
    "COST_PAIZURI": "skills.PAIZURI.costs",
    "GEN_PAIZURI": "skills.PAIZURI.generated_resources",
    "COND_PAIZURI": "skills.PAIZURI.conditions",
    "FX_PAIZURI": "skills.PAIZURI.effects",
    "PRES_PAIZURI": "skills.PAIZURI.presentation",
    "REQ_SUMMON_CS": "skills.SUMMON_CS.requirements",
    "TARGET_SUMMON_CS": "skills.SUMMON_CS.targeting",
    "COST_SUMMON_CS": "skills.SUMMON_CS.costs",
    "GEN_SUMMON_CS": "skills.SUMMON_CS.generated_resources",
    "COND_SUMMON_CS": "skills.SUMMON_CS.conditions",
    "FX_SUMMON_CS": "skills.SUMMON_CS.effects",
    "PRES_SUMMON_CS": "skills.SUMMON_CS.presentation",
    "REQ_SWALLOW": "skills.SWALLOW.requirements",
    "TARGET_SWALLOW": "skills.SWALLOW.targeting",
    "COST_SWALLOW": "skills.SWALLOW.costs",
    "GEN_SWALLOW": "skills.SWALLOW.generated_resources",
    "COND_SWALLOW": "skills.SWALLOW.conditions",
    "FX_SWALLOW": "skills.SWALLOW.effects",
    "THRESHOLD_SWALLOW": "skills.SWALLOW.effects",
    "OUTCOME_SWALLOW": "skills.SWALLOW.rules.outcome_interactions",
    "PRES_SWALLOW": "skills.SWALLOW.presentation",
    "SCALE_FINISHER": "scaling_profiles.SCALE_FINISHER",
    "REQ_EXTRA_TIPS": "skills.EXTRA_TIPS.requirements",
    "TARGET_EXTRA_TIPS": "skills.EXTRA_TIPS.targeting",
    "COST_EXTRA_TIPS": "skills.EXTRA_TIPS.costs",
    "GEN_EXTRA_TIPS": "skills.EXTRA_TIPS.generated_resources",
    "COND_EXTRA_TIPS": "skills.EXTRA_TIPS.conditions",
    "FX_EXTRA_TIPS": "skills.EXTRA_TIPS.effects",
    "PRES_EXTRA_TIPS": "skills.EXTRA_TIPS.presentation",
    "REQ_CUTENESS": "skills.CUTENESS.requirements",
    "TARGET_CUTENESS": "skills.CUTENESS.targeting",
    "COST_CUTENESS": "skills.CUTENESS.costs",
    "GEN_CUTENESS": "skills.CUTENESS.generated_resources",
    "COND_CUTENESS": "skills.CUTENESS.conditions",
    "FX_CUTENESS": "skills.CUTENESS.effects",
    "PRES_CUTENESS": "skills.CUTENESS.presentation",
    "REQ_NAUGHTY_THOUGHTS": "skills.NAUGHTY_THOUGHTS.requirements",
    "TARGET_NAUGHTY_THOUGHTS": "skills.NAUGHTY_THOUGHTS.targeting",
    "COST_NAUGHTY_THOUGHTS": "skills.NAUGHTY_THOUGHTS.costs",
    "GEN_NAUGHTY_THOUGHTS": "skills.NAUGHTY_THOUGHTS.generated_resources",
    "COND_NAUGHTY_THOUGHTS": "skills.NAUGHTY_THOUGHTS.conditions",
    "FX_NAUGHTY_THOUGHTS": "skills.NAUGHTY_THOUGHTS.effects",
    "PRES_NAUGHTY_THOUGHTS": "skills.NAUGHTY_THOUGHTS.presentation",
    "REQ_C_DRINKER": "skills.C_DRINKER.requirements",
    "TARGET_C_DRINKER": "skills.C_DRINKER.targeting",
    "COST_C_DRINKER": "skills.C_DRINKER.costs",
    "GEN_C_DRINKER": "skills.C_DRINKER.generated_resources",
    "COND_C_DRINKER": "skills.C_DRINKER.conditions",
    "FX_C_DRINKER": "skills.C_DRINKER.effects",
    "PRES_C_DRINKER": "skills.C_DRINKER.presentation",
    "REQ_STRIP": "skills.STRIP.requirements",
    "TARGET_STRIP": "skills.STRIP.targeting",
    "COST_STRIP": "skills.STRIP.costs",
    "GEN_STRIP": "skills.STRIP.generated_resources",
    "COND_STRIP": "skills.STRIP.conditions",
    "FX_STRIP": "skills.STRIP.effects",
    "PRES_STRIP": "skills.STRIP.presentation",
    "REQ_PINK_MIST": "skills.PINK_MIST.requirements",
    "TARGET_PINK_MIST": "skills.PINK_MIST.targeting",
    "COST_PINK_MIST": "skills.PINK_MIST.costs",
    "GEN_PINK_MIST": "skills.PINK_MIST.generated_resources",
    "COND_PINK_MIST": "skills.PINK_MIST.conditions",
    "FX_PINK_MIST": "skills.PINK_MIST.effects",
    "PRES_PINK_MIST": "skills.PINK_MIST.presentation",
    "REQ_PENETRATE": "skills.PENETRATE.requirements",
    "TARGET_PENETRATE": "skills.PENETRATE.targeting",
    "COST_PENETRATE": "skills.PENETRATE.costs",
    "GEN_PENETRATE": "skills.PENETRATE.generated_resources",
    "COND_PENETRATE": "skills.PENETRATE.conditions",
    "FX_PENETRATE": "skills.PENETRATE.effects",
    "PRES_PENETRATE": "skills.PENETRATE.presentation",
    "REQ_A_PENETRATION": "skills.A_PENETRATION.requirements",
    "TARGET_A_PENETRATION": "skills.A_PENETRATION.targeting",
    "COST_A_PENETRATION": "skills.A_PENETRATION.costs",
    "GEN_A_PENETRATION": "skills.A_PENETRATION.generated_resources",
    "COND_A_PENETRATION": "skills.A_PENETRATION.conditions",
    "FX_A_PENETRATION": "skills.A_PENETRATION.effects",
    "PRES_A_PENETRATION": "skills.A_PENETRATION.presentation",
    "REQ_STOMP": "skills.STOMP.requirements",
    "TARGET_STOMP": "skills.STOMP.targeting",
    "COST_STOMP": "skills.STOMP.costs",
    "GEN_STOMP": "skills.STOMP.generated_resources",
    "COND_STOMP": "skills.STOMP.conditions",
    "FX_STOMP": "skills.STOMP.effects",
    "THRESHOLD_STOMP": "skills.STOMP.effects",
    "PRES_STOMP": "skills.STOMP.presentation",
    "REQ_SUMMON_TENTACLES": "skills.SUMMON_TENTACLES.requirements",
    "TARGET_SUMMON_TENTACLES": "skills.SUMMON_TENTACLES.targeting",
    "COST_SUMMON_TENTACLES": "skills.SUMMON_TENTACLES.costs",
    "GEN_SUMMON_TENTACLES": "skills.SUMMON_TENTACLES.generated_resources",
    "COND_SUMMON_TENTACLES": "skills.SUMMON_TENTACLES.conditions",
    "FX_SUMMON_TENTACLES": "skills.SUMMON_TENTACLES.effects",
    "PRES_SUMMON_TENTACLES": "skills.SUMMON_TENTACLES.presentation",
    "REQ_SKILL_ABSOLUTE_CONTROL": "skills.SKILL_ABSOLUTE_CONTROL.requirements",
    "TARGET_SKILL_ABSOLUTE_CONTROL": "skills.SKILL_ABSOLUTE_CONTROL.targeting",
    "COST_SKILL_ABSOLUTE_CONTROL": "skills.SKILL_ABSOLUTE_CONTROL.costs",
    "GEN_SKILL_ABSOLUTE_CONTROL": "skills.SKILL_ABSOLUTE_CONTROL.generated_resources",
    "COND_SKILL_ABSOLUTE_CONTROL": "skills.SKILL_ABSOLUTE_CONTROL.conditions",
    "FX_SKILL_ABSOLUTE_CONTROL": "skills.SKILL_ABSOLUTE_CONTROL.effects",
    "OUTCOME_SKILL_ABSOLUTE_CONTROL": "skills.SKILL_ABSOLUTE_CONTROL.rules.outcome_interactions",
    "PRES_SKILL_ABSOLUTE_CONTROL": "skills.SKILL_ABSOLUTE_CONTROL.presentation",
    "REQ_G_BANG": "skills.G_BANG.requirements",
    "TARGET_G_BANG": "skills.G_BANG.targeting",
    "COST_G_BANG": "skills.G_BANG.costs",
    "GEN_G_BANG": "skills.G_BANG.generated_resources",
    "COND_G_BANG": "skills.G_BANG.conditions",
    "FX_G_BANG": "skills.G_BANG.effects",
    "PRES_G_BANG": "skills.G_BANG.presentation",
    "REQ_BKKAKE": "skills.BKKAKE.requirements",
    "TARGET_BKKAKE": "skills.BKKAKE.targeting",
    "COST_BKKAKE": "skills.BKKAKE.costs",
    "GEN_BKKAKE": "skills.BKKAKE.generated_resources",
    "COND_BKKAKE": "skills.BKKAKE.conditions",
    "FX_BKKAKE": "skills.BKKAKE.effects",
    "THRESHOLD_BKKAKE": "skills.BKKAKE.effects",
    "OUTCOME_BKKAKE": "skills.BKKAKE.rules.outcome_interactions",
    "PRES_BKKAKE": "skills.BKKAKE.presentation",
    "REQ_DEEPTH": "skills.DEEPTH.requirements",
    "TARGET_DEEPTH": "skills.DEEPTH.targeting",
    "COST_DEEPTH": "skills.DEEPTH.costs",
    "GEN_DEEPTH": "skills.DEEPTH.generated_resources",
    "COND_DEEPTH": "skills.DEEPTH.conditions",
    "FX_DEEPTH": "skills.DEEPTH.effects",
    "PRES_DEEPTH": "skills.DEEPTH.presentation",
    "REQ_WORSHIP_C": "skills.WORSHIP_C.requirements",
    "TARGET_WORSHIP_C": "skills.WORSHIP_C.targeting",
    "COST_WORSHIP_C": "skills.WORSHIP_C.costs",
    "GEN_WORSHIP_C": "skills.WORSHIP_C.generated_resources",
    "COND_WORSHIP_C": "skills.WORSHIP_C.conditions",
    "FX_WORSHIP_C": "skills.WORSHIP_C.effects",
    "PRES_WORSHIP_C": "skills.WORSHIP_C.presentation",
    "REQ_ECSTASY_AFTERSHOCKS": "skills.ECSTASY_AFTERSHOCKS.requirements",
    "TARGET_ECSTASY_AFTERSHOCKS": "skills.ECSTASY_AFTERSHOCKS.targeting",
    "COST_ECSTASY_AFTERSHOCKS": "skills.ECSTASY_AFTERSHOCKS.costs",
    "GEN_ECSTASY_AFTERSHOCKS": "skills.ECSTASY_AFTERSHOCKS.generated_resources",
    "COND_ECSTASY_AFTERSHOCKS": "skills.ECSTASY_AFTERSHOCKS.conditions",
    "FX_ECSTASY_AFTERSHOCKS": "skills.ECSTASY_AFTERSHOCKS.effects",
    "OVERFLOW_ECSTASY_AFTERSHOCKS": "skills.ECSTASY_AFTERSHOCKS.rules.overflow",
    "PRES_ECSTASY_AFTERSHOCKS": "skills.ECSTASY_AFTERSHOCKS.presentation",
    "REQ_DIVINE_HEALTH": "skills.DIVINE_HEALTH.requirements",
    "TARGET_DIVINE_HEALTH": "skills.DIVINE_HEALTH.targeting",
    "COST_DIVINE_HEALTH": "skills.DIVINE_HEALTH.costs",
    "GEN_DIVINE_HEALTH": "skills.DIVINE_HEALTH.generated_resources",
    "COND_DIVINE_HEALTH": "skills.DIVINE_HEALTH.conditions",
    "FX_DIVINE_HEALTH": "skills.DIVINE_HEALTH.effects",
    "PRES_DIVINE_HEALTH": "skills.DIVINE_HEALTH.presentation",
    "REQ_SKILL_PROVOKE": "skills.SKILL_PROVOKE.requirements",
    "TARGET_SKILL_PROVOKE": "skills.SKILL_PROVOKE.targeting",
    "COST_SKILL_PROVOKE": "skills.SKILL_PROVOKE.costs",
    "GEN_SKILL_PROVOKE": "skills.SKILL_PROVOKE.generated_resources",
    "COND_SKILL_PROVOKE": "skills.SKILL_PROVOKE.conditions",
    "FX_SKILL_PROVOKE": "skills.SKILL_PROVOKE.effects",
    "PRES_SKILL_PROVOKE": "skills.SKILL_PROVOKE.presentation",
    "REQ_SKILL_ENDURE": "skills.SKILL_ENDURE.requirements",
    "TARGET_SKILL_ENDURE": "skills.SKILL_ENDURE.targeting",
    "COST_SKILL_ENDURE": "skills.SKILL_ENDURE.costs",
    "GEN_SKILL_ENDURE": "skills.SKILL_ENDURE.generated_resources",
    "COND_SKILL_ENDURE": "skills.SKILL_ENDURE.conditions",
    "FX_SKILL_ENDURE": "skills.SKILL_ENDURE.effects",
    "PRES_SKILL_ENDURE": "skills.SKILL_ENDURE.presentation",
    "REQ_SKILL_COUNTER": "skills.SKILL_COUNTER.requirements",
    "TARGET_SKILL_COUNTER": "skills.SKILL_COUNTER.targeting",
    "COST_SKILL_COUNTER": "skills.SKILL_COUNTER.costs",
    "GEN_SKILL_COUNTER": "skills.SKILL_COUNTER.generated_resources",
    "COND_SKILL_COUNTER": "skills.SKILL_COUNTER.conditions",
    "FX_SKILL_COUNTER": "skills.SKILL_COUNTER.effects",
    "PRES_SKILL_COUNTER": "skills.SKILL_COUNTER.presentation",
    "REQ_SKILL_COMMAND": "skills.SKILL_COMMAND.requirements",
    "TARGET_SKILL_COMMAND": "skills.SKILL_COMMAND.targeting",
    "COST_SKILL_COMMAND": "skills.SKILL_COMMAND.costs",
    "GEN_SKILL_COMMAND": "skills.SKILL_COMMAND.generated_resources",
    "COND_SKILL_COMMAND": "skills.SKILL_COMMAND.conditions",
    "FX_SKILL_COMMAND": "skills.SKILL_COMMAND.effects",
    "PRES_SKILL_COMMAND": "skills.SKILL_COMMAND.presentation",
    "REQ_SKILL_RECOVER_COMPOSURE": "skills.SKILL_RECOVER_COMPOSURE.requirements",
    "TARGET_SKILL_RECOVER_COMPOSURE": "skills.SKILL_RECOVER_COMPOSURE.targeting",
    "COST_SKILL_RECOVER_COMPOSURE": "skills.SKILL_RECOVER_COMPOSURE.costs",
    "GEN_SKILL_RECOVER_COMPOSURE": "skills.SKILL_RECOVER_COMPOSURE.generated_resources",
    "COND_SKILL_RECOVER_COMPOSURE": "skills.SKILL_RECOVER_COMPOSURE.conditions",
    "FX_SKILL_RECOVER_COMPOSURE": "skills.SKILL_RECOVER_COMPOSURE.effects",
    "PRES_SKILL_RECOVER_COMPOSURE": "skills.SKILL_RECOVER_COMPOSURE.presentation",
    "REQ_SKILL_EXPLOIT_WEAKNESS": "skills.SKILL_EXPLOIT_WEAKNESS.requirements",
    "TARGET_SKILL_EXPLOIT_WEAKNESS": "skills.SKILL_EXPLOIT_WEAKNESS.targeting",
    "COST_SKILL_EXPLOIT_WEAKNESS": "skills.SKILL_EXPLOIT_WEAKNESS.costs",
    "GEN_SKILL_EXPLOIT_WEAKNESS": "skills.SKILL_EXPLOIT_WEAKNESS.generated_resources",
    "COND_SKILL_EXPLOIT_WEAKNESS": "skills.SKILL_EXPLOIT_WEAKNESS.conditions",
    "FX_SKILL_EXPLOIT_WEAKNESS": "skills.SKILL_EXPLOIT_WEAKNESS.effects",
    "PRES_SKILL_EXPLOIT_WEAKNESS": "skills.SKILL_EXPLOIT_WEAKNESS.presentation",
    "REQ_SKILL_BREAK_RESISTANCE": "skills.SKILL_BREAK_RESISTANCE.requirements",
    "TARGET_SKILL_BREAK_RESISTANCE": "skills.SKILL_BREAK_RESISTANCE.targeting",
    "COST_SKILL_BREAK_RESISTANCE": "skills.SKILL_BREAK_RESISTANCE.costs",
    "GEN_SKILL_BREAK_RESISTANCE": "skills.SKILL_BREAK_RESISTANCE.generated_resources",
    "COND_SKILL_BREAK_RESISTANCE": "skills.SKILL_BREAK_RESISTANCE.conditions",
    "FX_SKILL_BREAK_RESISTANCE": "skills.SKILL_BREAK_RESISTANCE.effects",
    "PRES_SKILL_BREAK_RESISTANCE": "skills.SKILL_BREAK_RESISTANCE.presentation",
    "REQ_SKILL_TURN_THE_TABLES": "skills.SKILL_TURN_THE_TABLES.requirements",
    "TARGET_SKILL_TURN_THE_TABLES": "skills.SKILL_TURN_THE_TABLES.targeting",
    "COST_SKILL_TURN_THE_TABLES": "skills.SKILL_TURN_THE_TABLES.costs",
    "GEN_SKILL_TURN_THE_TABLES": "skills.SKILL_TURN_THE_TABLES.generated_resources",
    "COND_SKILL_TURN_THE_TABLES": "skills.SKILL_TURN_THE_TABLES.conditions",
    "FX_SKILL_TURN_THE_TABLES": "skills.SKILL_TURN_THE_TABLES.effects",
    "PRES_SKILL_TURN_THE_TABLES": "skills.SKILL_TURN_THE_TABLES.presentation",
    "REQ_SKILL_FOCUS_SURGE": "skills.SKILL_FOCUS_SURGE.requirements",
    "TARGET_SKILL_FOCUS_SURGE": "skills.SKILL_FOCUS_SURGE.targeting",
    "COST_SKILL_FOCUS_SURGE": "skills.SKILL_FOCUS_SURGE.costs",
    "GEN_SKILL_FOCUS_SURGE": "skills.SKILL_FOCUS_SURGE.generated_resources",
    "COND_SKILL_FOCUS_SURGE": "skills.SKILL_FOCUS_SURGE.conditions",
    "FX_SKILL_FOCUS_SURGE": "skills.SKILL_FOCUS_SURGE.effects",
    "PRES_SKILL_FOCUS_SURGE": "skills.SKILL_FOCUS_SURGE.presentation",
    "REQ_SKILL_DIRECT_ALLY": "skills.SKILL_DIRECT_ALLY.requirements",
    "TARGET_SKILL_DIRECT_ALLY": "skills.SKILL_DIRECT_ALLY.targeting",
    "COST_SKILL_DIRECT_ALLY": "skills.SKILL_DIRECT_ALLY.costs",
    "GEN_SKILL_DIRECT_ALLY": "skills.SKILL_DIRECT_ALLY.generated_resources",
    "COND_SKILL_DIRECT_ALLY": "skills.SKILL_DIRECT_ALLY.conditions",
    "FX_SKILL_DIRECT_ALLY": "skills.SKILL_DIRECT_ALLY.effects",
    "PRES_SKILL_DIRECT_ALLY": "skills.SKILL_DIRECT_ALLY.presentation",
    "REQ_SKILL_UNBROKEN": "skills.SKILL_UNBROKEN.requirements",
    "TARGET_SKILL_UNBROKEN": "skills.SKILL_UNBROKEN.targeting",
    "COST_SKILL_UNBROKEN": "skills.SKILL_UNBROKEN.costs",
    "GEN_SKILL_UNBROKEN": "skills.SKILL_UNBROKEN.generated_resources",
    "COND_SKILL_UNBROKEN": "skills.SKILL_UNBROKEN.conditions",
    "FX_SKILL_UNBROKEN": "skills.SKILL_UNBROKEN.effects",
    "PRES_SKILL_UNBROKEN": "skills.SKILL_UNBROKEN.presentation",
    "REQ_SKILL_OVERFLOW_ENGINE": "skills.SKILL_OVERFLOW_ENGINE.requirements",
    "TARGET_SKILL_OVERFLOW_ENGINE": "skills.SKILL_OVERFLOW_ENGINE.targeting",
    "COST_SKILL_OVERFLOW_ENGINE": "skills.SKILL_OVERFLOW_ENGINE.costs",
    "GEN_SKILL_OVERFLOW_ENGINE": "skills.SKILL_OVERFLOW_ENGINE.generated_resources",
    "COND_SKILL_OVERFLOW_ENGINE": "skills.SKILL_OVERFLOW_ENGINE.conditions",
    "FX_SKILL_OVERFLOW_ENGINE": "skills.SKILL_OVERFLOW_ENGINE.effects",
    "OVERFLOW_SKILL_OVERFLOW_ENGINE": "skills.SKILL_OVERFLOW_ENGINE.rules.overflow",
    "PRES_SKILL_OVERFLOW_ENGINE": "skills.SKILL_OVERFLOW_ENGINE.presentation",
    "REQ_SKILL_MUTUAL_RUIN": "skills.SKILL_MUTUAL_RUIN.requirements",
    "TARGET_SKILL_MUTUAL_RUIN": "skills.SKILL_MUTUAL_RUIN.targeting",
    "COST_SKILL_MUTUAL_RUIN": "skills.SKILL_MUTUAL_RUIN.costs",
    "GEN_SKILL_MUTUAL_RUIN": "skills.SKILL_MUTUAL_RUIN.generated_resources",
    "COND_SKILL_MUTUAL_RUIN": "skills.SKILL_MUTUAL_RUIN.conditions",
    "FX_SKILL_MUTUAL_RUIN": "skills.SKILL_MUTUAL_RUIN.effects",
    "PRES_SKILL_MUTUAL_RUIN": "skills.SKILL_MUTUAL_RUIN.presentation"
  }
}

```

