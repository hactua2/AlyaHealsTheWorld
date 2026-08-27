# Ayla Heals the World — Architecture Source of Truth

## Status
This document consolidates the approved high-level architecture from the narrative work, Skills Audit, resource/ecology audits A1–A10, audits B–J, the final architecture decision checkpoint, and the R1–R15 structural gameplay sequence. It is the primary reference for future structural decisions. Concrete rosters, recipes, maps, species, quests, and balance values remain intentionally deferred.

# 1. Game Identity
A narrative RPG with light base/community management. The world is structurally sexualized: sexuality is material, cultural, magical, biological, economic, and narrative, not a separate subsystem. Adult content should remain consent-oriented and use the same architecture as other gameplay.

The player follows Alya's effort to create conditions under which harmony can exist. The ultimate healing of the world's deep wound is not guaranteed to be witnessed by anyone alive during the story; the outcome depends on long-term change rather than a simple measurable endpoint.

The Wound modifies relationships, ecologies, characters, opportunities, and regions. It is not a default currency, separate economy, or excuse for non-consensual sexualization.

# 2. Canonical System Loop
Narrative Progress
-> unlocks regions, resources, possibilities, facilities, characters, and content
-> Exploration / Encounters / Quests / Expeditions
-> Rewards and discoveries
-> Resources / Items / Gold / Knowledge / Recruitment opportunities
-> Buildings / Production / Equipment / Transmutation / Rehabilitation / Community assignments
-> New capabilities and specializations
-> Further narrative progress.

No major system should become an isolated progression path.

# 3. World, Regions and Exploration
The world is divided into structurally distinct regions. Some regions are available initially; others unlock through specific acts or Main Quest progression. Regions may remain relevant through resources, quests, characters, production, and optional exploration.

Procedural generation is a major tool for repeatable exploration, gathering maps, and selected reusable quests. Hand-authored maps are reserved for story-critical levels and cases where authored structure adds clear value.

The standard encounter hierarchy is Normal, Elite, Mini-Boss, and Boss. Power/progression band, encounter class, and narrative role are separate dimensions. The old mixed use of “Tier” as a combination of importance and power is deprecated.

Organization and Wound influence are transversal layers that may modify families, regions, behavior, skills, hazards, and encounter instability.

# 4. Community and Population
Facilities may be specialized rather than universally modular. The player may destroy or relocate constructions. Open-area constructions such as gardens or plantations are valid and multiple constructions of the same category may coexist with different configured outputs.

Community entities are separated by function: main/narrative characters, specialized residents, generic workers, and recruitable combat entities. Alya is the fixed protagonist; standard expeditions use Alya plus one selected ally, with narrative exceptions.

Combat-capable allies combine individual adventure experience, individual development, shared community upgrades, equipment, and skills. Assignment experience and learned aptitude are never lost.

Dedicated facilities may support collective ally development, curse removal, recovery, recruitment/integration, and rehabilitation.

# 5. Combat, Skills and Character Data
The Skills Audit remains authoritative for shared combat vocabulary and approved skill families. Combat distinguishes Health Damage and H-damage and supports Kill, Knockout, Capture, Submission, Escape, and Objective Complete.

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

Equipment-derived effects disappear immediately when equipment is removed. Do not create duplicate status-effect lifecycles or parallel combat currencies.

# 6. Recruitment and Rehabilitation
Combat recruitment does not imply instant membership. A successful combat-specific recruitment condition may instead open an eligibility path for post-encounter rehabilitation.

The canonical flow is:

Encounter
-> Eligibility condition
-> Capture, surrender, recovery, or other post-encounter state as context permits
-> Rehabilitation / integration facility and process
-> Community membership when the process succeeds
-> Assignments and, when eligible, expedition participation.

Rehabilitation is a community system requiring dedicated infrastructure. Its implementation must remain compatible with the project’s consent-oriented boundaries and should not be treated as automatic personality overwrite.

Dialogue and choices may alter eligibility, outcomes, integration paths, and alternative resolutions.

# 7. Items, Equipment, Curses and Transmutation
Item categories are Resources, Components, Consumables, Equipment, and Narrative/Unique Items. Equipment should change choices, playstyle, interactions, defenses, roles, or capabilities.

Transmutation is one modification system emphasizing specialization and trade-offs. Respec and build changes are available through facilities or specific moments with light friction and cost.

Cursed equipment is a meaningful commitment, not a permanent unknowable trap. A dedicated community structure can remove cursed items from the player. Removal does not cleanse the item: the item remains cursed and may be equipped again voluntarily later. Curses therefore remain part of item identity while player commitment to wearing them is reversible through community infrastructure.

# 8. Resources, Economy and Trade
Recurring resources remain intentionally few. Gold is conventional currency for purchases, selected services, selected construction costs, and selected upgrades; it is not universal.

Resources may simultaneously be crafting/production materials, economically valuable goods, strategic progression resources, or flexible multi-use goods. The economy should avoid encouraging accidental loss of irreplaceable progression materials.

Vendors have specialized inventories; basic goods may be unlimited while selected goods are limited or refreshed by cycles/progression. Gold sources include quests, combat rewards, selling resources/items, production, and trade opportunities.

Resource accumulation is controlled primarily through useful sinks: buildings, upgrades, equipment, development, production, trade, and optional optimization.

# 9. Buildings, Ecology and Production
Resource-facing buildings primarily provide Access, Stability, Conversion, or Specialization. A standalone building must introduce a distinct player choice; otherwise prefer upgrades, modules, rooms, event unlocks, or visual variation.

Adult facilities follow the same architectural rules. Community production provides stability and predictability rather than upkeep punishment. Ecology uses renewable, cyclical, variable, contextual, and unique acquisition patterns without mandatory detailed farming simulation or universal depletion bars.

# 10. Quests, Progression and Gating
Quests are Main Quest, Regional Quests, Character Quests, Handcrafted Sidequests, and Reusable/Procedural Tasks.

The Main Quest is the principal progression gate and can unlock regions, systems, constructions, characters, and resources. Regional access, character requirements, resources, knowledge, and system prerequisites support that axis.

Players may optimize and explore within the current layer, but unrestricted grinding should not replace narrative advancement. Advanced content may combine narrative progress, resources, and relevant characters or knowledge.

Some quests reveal rewards; others preserve uncertainty. Major reward categories may be previewed when useful. Content should not disappear arbitrarily, although important choices may create permanent divergent outcomes.

# 11. Time, Defeat and Recovery
The core time model uses a simple explicit day/night cycle. Assignments may be continuous or cycle-based. Configured community processes may continue through controlled progression events without requiring a full real-time simulation.

Waiting is allowed in safe locations. Permanent time pressure is not the default.

Defeat uses narrative retreat/consequence rather than generic Game Over as the primary model. Secured rewards are distinguished from controlled unsecured expedition rewards. Temporary conditions and recovery infrastructure may create meaningful consequences without systemic permadeath.

Voluntary retreat follows safe-location and out-of-combat rules. Leaving before a quest’s required completion does not grant that quest’s completion reward.

A general expedition-fatigue/escalating-risk system remains Maybe / Future Expansion.

# 12. Information Architecture
The player sees known requirements for unavailable content while undiscovered requirements remain hidden or hinted.

The game should expose the eight core stats plus summarized aptitude and role information without requiring excessive stat management. Assignments provide understandable estimates/ranges and contributing factors.

A progressively unlocked codex may cover characters, enemies, resources, regions, buildings, and important discoveries. Once information is discovered, contextual navigation should reveal relevant relationships such as sources, consumers, requirements, and suitable characters.

System rule: discover -> make available -> explain -> reveal additional depth progressively.

# 13. Cross-System Integration Rules
- Main Quest progression gates portions of world access and systemic expansion.
- Regions provide enemies, resources, quests, and progression opportunities.
- Combat can lead to rewards, narrative outcomes, or rehabilitation eligibility.
- Dialogue and choices may alter encounters, quest resolutions, rehabilitation, and recruitment/integration.
- Successfully integrated entities can contribute to the community and, when eligible, expeditions.
- Community facilities support production, recovery, curse removal, rehabilitation/integration, and collective character development.
- Individual adventure experience and shared community upgrades coexist.
- Assignments create opportunity costs because expedition participants pause their community contribution.
- Economy connects exploration, production, vendors, buildings, and optional optimization.
- UX reveals discovered relationships so players can make informed progression decisions.

# 14. Scope Guardrails and Future Candidates
Do not add without demonstrated need: separate adult economy/inventory, separate sexual crafting subsystem, recurring Wound currency, detailed farming simulation, universal processing trees, duplicate combat currencies, universal enemy scaling, or excessive building proliferation.

The following remain possible but non-mandatory:
1. specialized non-combat encounter archetypes such as pursuit or survival systems;
2. alternate narrative versions of bosses;
3. general expedition fatigue or escalating risk.

# 15. Deferred Content
The architecture intentionally does not yet define exact rosters, recipes, maps, species, quest lists, procedural rules, numeric balance, exact capacity limits, or detailed gate schedules. These are content and implementation specifications, not missing macro-systems.

# 16. Architectural Verdict
PASS. The project has a complete high-level architecture for narrative progression, combat, skills, resources, ecology, exploration, encounters, community management, recruitment/rehabilitation, curses, economy, quests, gating, time, defeat/recovery, adult-content integration, and player information.

Future design should default to: Which existing interface does this idea belong to? A new macro-system requires a demonstrated gap that cannot be solved by content, configuration, specialization, or extension of an existing system.
