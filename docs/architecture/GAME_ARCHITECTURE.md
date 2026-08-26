# Ayla Heals the World — Architecture Source of Truth

## Status
This document consolidates the approved high-level architecture from the narrative work, Skills Audit, resource/ecology audits A1–A10, audits B–J, and the final architecture decision checkpoint. It is the primary reference for future structural decisions. Concrete rosters, recipes, maps, species, quests, and balance values remain intentionally deferred.

# 1. Game Identity
A narrative RPG with light base/community management. The world is structurally sexualized: sexuality is material, cultural, magical, biological, economic, and narrative, not a separate subsystem. Adult content should remain consent-oriented and use the same architecture as other gameplay.

The player follows Alya's effort to create conditions under which harmony can exist. The ultimate healing of the world's deep wound is not guaranteed to be witnessed by anyone alive during the story; the outcome depends on long-term change rather than a simple measurable endpoint.

The Wound modifies relationships, ecologies, characters, opportunities, and regions. It is not a default currency, separate economy, or excuse for non-consensual sexualization.

# 2. Macro Narrative and Gameplay Principle
The game should repeatedly express the verbs:
Explore, encounter, understand, negotiate, care for, transform, confront, integrate, build, assign, specialize, and restore or redirect relationships.

The community becomes increasingly important, with Alya eventually functioning as its leader and the base-management layer becoming a meaningful expression of the narrative.

Narrative, community growth, exploration, and combat must form one progression cycle rather than independent tracks.

# 3. Canonical System Loop
Narrative Progress
-> unlocks regions, resources, possibilities, facilities, and content
-> Exploration / Encounters / Quests / Expeditions
-> Rewards and discoveries
-> Resources / Items / Gold
-> Buildings / Production / Equipment / Transmutation / Community assignments
-> New capabilities and specializations
-> Further narrative progress.

No major system should become an isolated progression path.

# 4. Combat and Skills
The Skills Audit is authoritative for the shared combat vocabulary and approved skill set.

Core shared mechanics include Control, Surrender, Cruelty, Endurance, Exploit, Consume, Chain, Threshold, and Overflow. Emergent identities combine Dominant/Submissive with Sadist/Masochist rather than using rigid classes.

Combat distinguishes Health Damage and H-damage and supports different victory outcomes such as Kill, Knockout, Capture, Submission, Escape, and Objective Complete.

Stats follow the established source-of-truth rule. Equipment-derived effects disappear immediately when the equipment is removed. Do not create duplicate status-effect lifecycles or parallel combat currencies.

Enemy difficulty should primarily use fixed/content-authored power bands plus behavioral and encounter variation rather than universal level scaling.

# 5. Resources and Economy
Recurring resources are intentionally few.

Common Materials:
- Timber
- Stone
- Metal
- Fiber

Special Materials:
- Essence: power, vitality, specialization
- Nectar: botany, cultivation, consumption
- Musk: sensory influence and specialized biological expression
- Estrus: fertility, cycles, transformation

Components:
- Arcane Component
- Organic Component

Unique Resources are individually named and context-specific.

Gold is the common currency for conventional purchases such as items, seeds, and trade goods. It complements material resources and does not replace specialized resource requirements.

Primary acquisition modes are:
- Exploration
- Production
- Expedition
- Quest
- Encounter

Preferred chains are short: Explore -> Obtain -> Use, or Obtain -> Process -> Use. Avoid mandatory long refinement chains.

Consumption destinations are Buildings, Equipment, Transmutation, and Specialized Content/Unlocks.

# 6. Ecology and Renewal
Productive ecology consists of flora, organisms, environments/phenomena, and managed community ecology.

Useful roles include structural, sensory, transformative, magical, exceptional, and productive organisms. Resource acquisition can involve cooperation, care, exchange, natural collection, biological cycles, or encounters; it is not inherently violent extraction.

Common materials are abstractly renewable. Special materials are cyclical, variable, or contextual. Rare opportunities may rotate. Unique resources are contextual.

Do not implement permanent individual-node depletion, mandatory ecological chores, a detailed farming simulator, universal depletion bars, or sustainability taxes.

Community production provides stability and predictability rather than upkeep punishment.

Ecological pressure should change content through states such as Normal, Disturbed, and Altered rather than simply punishing the player.

# 7. Regions and Exploration
Use five reusable productive profiles:
1. Settlement / Managed Landscape
2. Wild Sensory Growth
3. Living / Biological Territory
4. Mineral / Ancient Territory
5. Wound-Influenced modifier

A region normally has one primary profile, optional secondary influence, and optional major modifier. Wound influence usually modifies an existing profile rather than becoming a separate biome.

Exploration uses a hybrid presentation: strategic region/destination selection plus explorable maps and encounters. Procedural generation is a major tool for repeatable exploration, gathering maps, and potentially selected quests. Hand-authored maps are reserved for story-critical levels and cases where authored structure adds clear value.

Encounter categories include combat, social, ecological, adult/intimate, narrative, discovery, danger, and opportunity. Categories may combine.

Unique encounters resolve permanently or transform. Repeatable activities use variable states or reward pools.

Retreat is possible. Failure should normally create contextual lost opportunities, changed rewards, or future consequences rather than universal game-over punishment.

# 8. Buildings and Facilities
Every resource-facing building should primarily provide one of:
- Access
- Stability
- Conversion
- Specialization

A standalone building must introduce a distinct player choice. Otherwise use an upgrade, module, room, event unlock, or visual variation.

Adult facilities use the same architecture. Taverns, intimacy venues, BDSM-oriented spaces, sensory gardens, aphrodisiac environments, and transformation facilities are not a separate economy.

Only mechanically meaningful adult facilities should become standalone buildings; other functions should be modules or extensions of larger structures.

Prefer a small number of meaningful upgrade tiers. Buildings should usually expand options rather than inflate percentages.

# 9. Items, Equipment, and Transmutation
Item categories are Resources, Components, Consumables, Equipment, and Narrative/Unique Items.

Recurring resources, components, and consumables are stackable. Equipment and unique narrative objects remain individually identifiable. No weight/encumbrance system is required without a proven gameplay need.

Equipment should change choices, playstyle, skill interactions, defenses, roles, or capabilities. Use few impactful equipment slots, with limited specialized slots unlockable through progression where useful.

Older equipment should remain relevant to alternate builds or be evolvable/transmutable when appropriate.

Transmutation is one modification system, not several parallel enhancement trees. Arcane and Organic Components are primary structural inputs. It emphasizes specialization and trade-offs.

Transmutation is reversible with meaningful but non-punitive cost. Saved alternative configurations are desirable where implementation supports them.

Respec and build changes are available through specific facilities or moments with light friction and cost, never as permanent traps.

# 10. Community and Base Management
Member lifecycle:
Recruit/Join -> Integrate -> Assign -> Gain aptitude through experience and time -> Unlock specialization/opportunities -> Personal and narrative development.

Broad work domains include production/ecology, expedition/exploration support, care/recovery, research/transmutation, combat/training, and social/specialized services.

Natural aptitude may accelerate learning or improve performance but does not make other characters invalid.

Experience and learned aptitude are never lost. Changing to a mechanically inferior role does not erase prior expertise.

Aptitude is presented as concise qualitative descriptor plus rank.

Community members are characters, not passive percentage modifiers. Assignments may generate events, relationships, discoveries, conflicts, stories, and opportunities.

# 11. Progression and Gating
Narrative progress is the primary source of new possibility layers.

Use hard gates for milestones that would destabilize pacing and soft gates for curiosity or partial access. The practical anti-overdevelopment model centers on:
- advanced upgrades and possibility layers locked by main-quest progress;
- resources that only appear in regions unlocked during later acts.

The player may see a required resource or upgrade component before discovering its source and infer that main-quest progress or new regions will eventually reveal it.

Players may optimize, stockpile, and experiment inside the currently unlocked layer, but cannot fully access future layers before their narrative gates.

Avoid arbitrary global time limits.

Systemic requirements may be explicit. Narrative discoveries can remain partially mysterious. Quests may preview or hint at major rewards so players can intentionally pursue desired progression.

# 12. Rewards and Loops
Every repeatable activity must answer:
1. What does it reward?
2. Where is that reward used?
3. What player choice does that use create?

Canonical loops include:
Explore -> Resource/Discovery -> Building/Equipment/Content.
Combat -> Component/Reward -> Transmutation/Equipment -> New combat choices.
Community -> Stable output/Opportunity -> Specialization/Content.
Quest -> Unique unlock/change -> Narrative/System expansion.

No recurring resource should lack a consumption destination. No major building should lack a value source. Avoid repeatable activities whose rewards become universally obsolete.

Reward pools may overlap enough to avoid mandatory farming while preserving distinct activity identities.

# 13. Narrative Feedback and Harmony
The player should understand whether their overall journey is trending toward more or less harmony without a deterministic universal percentage.

Use a qualitative global direction indicator plus visible regional consequences. The global signal communicates trajectory; local changes show where consequences are occurring.

The final outcome remains long-term and not fully knowable to living characters, so feedback should indicate direction and conditions rather than guarantee a final cosmic result.

# 14. Scope Guardrails
Do not add without demonstrated need:
- separate NSFW economy or inventory
- separate sexual crafting or management subsystem
- dedicated recurring Wound currency
- biome-specific currencies by default
- detailed farming simulator
- permanent resource depletion simulation
- mandatory ecological maintenance chores
- universal processing/refinement tree
- duplicate combat currencies or status lifecycles
- universal automatic enemy scaling
- excessive building proliferation

# 15. Deferred Content, Not Architectural Gaps
The architecture intentionally does not yet define:
- exact building roster and recipes
- exact equipment roster and slots
- exact consumable families
- exact region roster/world map
- individual flora, fauna, organisms, enemies, or NPCs
- exact procedural-generation rules
- exact quest roster and reward tables
- unique resources and their chains
- numeric costs, rates, durations, drop rates, and balance
- exact community capacity/concurrency and automation details
- exact party size and fog/discovery rules
- exact act pacing and gate schedule

These should now be added as concrete content inside the architecture rather than by inventing new macro-systems.

# 16. Architectural Verdict
PASS. The project has a complete high-level architecture for narrative progression, combat, skills, resources, ecology, exploration, regions, rewards, buildings, items, equipment, transmutation, community management, gating, adult content integration, and player feedback.

Future design should default to the question: Which existing interface does this idea belong to? A new macro-system requires a demonstrated gap that cannot be solved by content, configuration, specialization, or extension of an existing system.
