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
