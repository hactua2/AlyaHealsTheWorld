# AHTW — Game Design & Player Loop Review Pack

**Audience:** game designer, systems designer, progression designer, economy/community designer, producer.  
**Purpose:** provide a reviewable overview of the game's play structure and locked constraints.

## 1. Product definition

AHTW is a single-player, turn-based narrative RPG with light community/base management. The player explores regions, completes direct quests and encounters, recruits and integrates characters, develops skills/equipment, builds facilities, assigns community members, and sends eligible members on autonomous Expeditions.

The game should create meaningful trade-offs without turning into a high-friction colony simulator. Community management exists to make relationships and shared responsibility mechanically visible.

## 2. Core loop

1. Narrative progress opens people, regions, facilities, quests and capabilities.
2. Exploration and direct encounters yield resources, equipment, knowledge, recruitment opportunities and world-state changes.
3. The player invests in recovery, construction, production, equipment, progression, relationships and integration.
4. Assignments and facilities create specialization and opportunity costs.
5. Autonomous Expeditions turn community capacity into delayed outcomes while assigned characters are unavailable to the active party and their normal assignment.
6. These results unlock new narrative choices, regions and challenges.

Sidequests are direct player activities and require Alya/player participation. Expeditions are delegated autonomous activities. They may share content data, but not the same control/resolution loop.

## 3. Party, time, travel and state

- Alya is the fixed protagonist. Standard active party: Alya plus one selected ally, with narrative exceptions.
- One community member has one primary assignment at a time.
- Assignment work stops while a character is away on an Expedition.
- Expedition participants are unavailable to the active party until they return.
- World travel uses a regional/locality graph and consumes game time; there is no tactical world grid.
- Combat has no grid positioning or independent range system; skills define valid targets.
- Inventory has no fixed capacity limit.
- Main-path resource costs must remain feasible. Optional crafting must not consume materials reserved for mandatory progression.
- Use stable IDs for cross-system references and saves; display names are presentation only.
- Discovered requirements should be visible; undiscovered requirements may remain hidden or hinted.

## 4. Locked full-game baseline

| Content family | Baseline |
|---|---:|
| Acts | 5 |
| Main quest stages | 47 |
| Sidequests | 25 |
| Regions | 7 |
| Factions | 6 |
| Recruitable allies | 10 |
| Named recurring NPCs | 21 |
| Generic NPC templates | 12 |
| Enemy archetypes | 35 |
| Major bosses | 9 |
| Special encounters | 8 |
| Facilities | 12 |
| Resources | 8 |
| Items/equipment | 36 |
| Alya base outfits | 8 |
| Expedition templates | 8 |
| Ending families | 5 |
| Canonical skill records | 67 |

This is a baseline content lock, not proof of finished dialogue, balanced numbers, final art, or runtime completeness.

## 5. Community and base management

Community growth is meant to evolve from informal survival to delegated responsibilities, formal representation, and a regional cooperation network. Facilities have clear strategic roles: care/stability, production/conversion, access/coordination, and other locked facility functions in the full-game catalog.

Design should favor a small number of meaningful facilities and assignments over excessive resource trees, universal upkeep, or a detailed farming simulator. Characters' community roles should matter without replacing their distinct narrative identities.

An assignment provides an understandable estimate/range and contributing factors. Aptitude reflects relevant stats/species/experience and time assigned; characters without natural aptitude can improve more slowly. Do not make a character's starting role a permanent hard lock.

## 6. Economy and progression guardrails

- Resource types should have clear sources, sinks and player-facing purposes.
- Do not introduce a new currency or macro-system unless an existing system cannot support the requirement.
- Avoid duplicate combat currencies, a separate adult economy, excessive crafting chains, universal enemy scaling, and building proliferation without demonstrated need.
- Individual adventure experience and shared community upgrades coexist.
- Main path should not soft-lock due to optional spending; mandatory materials need guaranteed sources or explicit fallbacks.
- Recruitment/integration, rehabilitation, and community assignment should connect to narrative consequences rather than only numerical bonuses.
- Exact rates, costs, recipes, caps and progression curves remain subject to implementation/balance QA unless explicitly locked in structured data.

## 7. Act I vertical slice as design test

**“The Water We Share”** tests the whole loop at small scale:
- water scarcity and community conflict predate the Ferida;
- the Red Thread corrupts an old irrigation system;
- the Organization offers a defensible containment plan with unacceptable local costs;
- Alya's third option combines evidence, supplies, care and coordination;
- the lower-terrace seed reserve is unavoidably lost;
- Alya accepts accountable leadership;
- the player chooses one first facility: Recovery Room, Common Workshop, or Coordination Board;
- the first autonomous Expedition is available regardless of facility choice.

The facility choice should matter without making any one option universally optimal. The Coordination Board improves assignment/Expedition visibility but is not a hard gate to the Expedition system.

## 8. Design principles and non-goals

- Decisions should reveal values, risk tolerance, trust and trade-offs rather than just good/evil alignment.
- Consequences should be persistent and legible.
- Victory does not mean all underlying social problems disappear.
- Community growth should distribute responsibility rather than make Alya the only competent actor.
- Keep systems legible; reveal discovered dependencies contextually.
- Avoid speculative macro-systems when content, configuration or an existing interface can solve the problem.

## 9. Review checklist

- Is the core loop clear to a new player?
- Does each system support narrative/community decisions rather than add busywork?
- Can the main path always be completed with required resources?
- Are sidequests and Expeditions clearly distinct?
- Do facilities and assignments create meaningful trade-offs?
- Are characters unavailable when their time is committed elsewhere?
- Are progression rules understandable and not arbitrarily restrictive?
- Are any new mechanics duplicating existing systems?
- Are all numbers labelled as locked, provisional, or awaiting runtime balance?


---

# Complete standalone game-design baseline

This appendix embeds the concrete design inventory so this file can be reviewed offline without opening the data catalogs or architecture document. It distinguishes locked conceptual rules from values still awaiting runtime balance.

## A. Five-act structure
| Act | Title | Theme / end state |
| --- | --- | --- |
| ACT-01 Foundation | The Water We Share | Scarcity, blame, local knowledge, unavoidable loss; Alya becomes Brackenford's recognized leader; first facility and Expedition unlock. |
| ACT-02 Construction | A Place for the Uncounted | Growth, integration, delegated responsibility, institutional rupture; Brackenford shelters people under a documented risk plan and establishes council governance. |
| ACT-03 Consequences | The Cost of Being Free | Autonomy, scarcity, trade leverage, plural regional agreements; Three regions ratify a voluntary mutual-aid compact. |
| ACT-04 Escalation | What the Wound Learns | Systemic exploitation, verification, delegation under pressure; The network survives in a changed form; evidence points toward the Wound's Confluence. |
| ACT-05 Revelation and Resolution | A Future Without a Center | Truth, distributed responsibility, uncertain but durable recovery; The Ferida's sustaining conditions are transformed or constrained; epilogues follow world state. |

## B. Enemy archetype catalogue — all 35 records
| ID / Name | Family / Tier | Role | Signature hook | AI / scaling |
| --- | --- | --- | --- | --- |
| ENM-001 Guard | Civilized / Tier 1 | Defender | Formation and guard interception | AI_ENM-001 / authored_power_band |
| ENM-002 Slime | Savage / Tier 1 | Adaptive mob | Multi-hit and elemental coverage | AI_ENM-002 / authored_power_band |
| ENM-003 Cockatrice | Savage / Tier 1 | Status pressure | Vulnerability and accuracy pressure | AI_ENM-003 / authored_power_band |
| ENM-004 Warrior | Tribal / Tier 1 | Melee baseline | Direct damage and basic intent | AI_ENM-004 / authored_power_band |
| ENM-005 Goblin | Tribal / Tier 1 | Evasive utility | Scavenging and target switching | AI_ENM-005 / authored_power_band |
| ENM-006 Mycelian Sentinel | Tribal / Tier 1 | Territorial defender | Protects a location; not a generic evil tribe | AI_ENM-006 / authored_power_band |
| ENM-007 Zombie | Undead / Tier 1 | Attrition | Slow pressure and undead effects | AI_ENM-007 / authored_power_band |
| ENM-008 Augmented Agent | Civilized / Tier 2 | Elite counter | Adapts against repeated tactics | AI_ENM-008 / authored_power_band |
| ENM-009 Kunoichi | Civilized / Tier 2 | Evasion specialist | Marks and target switching | AI_ENM-009 / authored_power_band |
| ENM-010 Krakenblood | Loner / Tier 2 | Resilient pressure | Sustained pressure with punishable recovery | AI_ENM-010 / authored_power_band |
| ENM-011 Kitsune Trickster | Loner / Tier 2 | Decoy controller | Decoys and intent manipulation | AI_ENM-011 / authored_power_band |
| ENM-012 Barbarian | Tribal / Tier 2 | Heavy attacker | High damage, low flexibility | AI_ENM-012 / authored_power_band |
| ENM-013 Royal Guard | Civilized / Tier 2 | Formation defender | Protects allies and intercepts | AI_ENM-013 / authored_power_band |
| ENM-014 Minotaur | Savage / Tier 2 | Guard breaker | Charge and fortitude pressure | AI_ENM-014 / authored_power_band |
| ENM-015 Wolfkin Stalker | Savage / Tier 2 | Pack hunter | Coordinated attacks and pursuit | AI_ENM-015 / authored_power_band |
| ENM-016 Orc Challenger | Tribal / Tier 2 | Duelist | Resolve pressure; can be neutral in story | AI_ENM-016 / authored_power_band |
| ENM-017 Haunt | Loner / Tier 2 | Reactive spirit | Preparation and knowledge expose weakness | AI_ENM-017 / authored_power_band |
| ENM-018 Witch | Loner / Tier 2 | Curse controller | Control and curse effects; NPC contexts use separate records | AI_ENM-018 / authored_power_band |
| ENM-019 Mummy | Undead / Tier 2 | Endurance | Attrition and seal mechanics | AI_ENM-019 / authored_power_band |
| ENM-020 Dullahan | Undead / Tier 3 | Execution elite | High-threat intent; distinct from Reaper NPC unless explicitly linked | AI_ENM-020 / authored_power_band |
| ENM-021 Angelic Arbiter | Civilized / Tier 3 | Protective judge | Protection and judgment; not automatically evil | AI_ENM-021 / authored_power_band |
| ENM-022 Dragonkin | Loner / Tier 3 | Elemental elite | Strong telegraphed elemental attacks | AI_ENM-022 / authored_power_band |
| ENM-023 Fallen Angel | Loner / Tier 3 | Multi-phase controller | Control and vulnerability cycles | AI_ENM-023 / authored_power_band |
| ENM-024 Lamia Duelist | Loner / Tier 3 | Control specialist | Constriction/control represented without spatial grid assumptions | AI_ENM-024 / authored_power_band |
| ENM-025 Demon | Savage / Tier 3 | Hybrid pressure | Alignment varies by narrative context | AI_ENM-025 / authored_power_band |
| ENM-026 Threadling | Ferida / Tier 1 | Swarm unit | Multiplies if ignored | AI_ENM-026 / authored_power_band |
| ENM-027 Hollow Warden | Ferida / Tier 2 | Objective defender | Linked resistance protects a quest objective | AI_ENM-027 / authored_power_band |
| ENM-028 Root-Knot Anchor | Ferida / Objective | Objective entity | Defeating it alone does not necessarily complete the encounter | AI_ENM-028 / authored_power_band |
| ENM-029 Red-Tide Leech | Ferida / Tier 2 | Resource drainer | Drains pressure/resources; vulnerable after feeding | AI_ENM-029 / authored_power_band |
| ENM-030 Echo Husk | Ferida / Tier 2 | Pattern repeater | Repeats common action patterns; varied tactics counter it | AI_ENM-030 / authored_power_band |
| ENM-031 Guilt Mirror | Ferida / Tier 3 | Relationship pressure | Uses authored relationship flags only | AI_ENM-031 / authored_power_band |
| ENM-032 Ashbound | Ferida / Tier 2 | Hazard fighter | Alternates armor and exposure | AI_ENM-032 / authored_power_band |
| ENM-033 Archive Custodian | Construct / Tier 3 | Research construct | Tests interrupts and source discovery | AI_ENM-033 / authored_power_band |
| ENM-034 Network Eater | Ferida / Tier 3 | Objective attacker | Targets links and encounter objectives, not only Vitality | AI_ENM-034 / authored_power_band |
| ENM-035 Confluence Herald | Ferida / Tier 4 | Late-game manifestation | Multi-target threat with explicit phase conditions | AI_ENM-035 / authored_power_band |

## C. Major bosses — all 9 records
| ID / Name / Act | Composition | Objective | Contract |
| --- | --- | --- | --- |
| BOS-001 Root-Knot at the Sluice / ACT-01 | ENM-027 + ENM-028 | Stabilize diversion, sever filament, secure gate; seed loss is mandatory. | phase required=true; retreat=encounter_defined; world mutation=true |
| BOS-002 The Pilgrim Engine / ACT-02 | ENM-008 + ENM-030 | Protect shelter routes and disable three supply anchors. | phase required=true; retreat=encounter_defined; world mutation=true |
| BOS-003 The Contract Eater / ACT-03 | ENM-011 + ENM-029 | Break exploitative contract seals while keeping caravan escorts safe. | phase required=true; retreat=encounter_defined; world mutation=true |
| BOS-004 The Memory That Bites / ACT-03 | ENM-006 + ENM-031 | Resolve a living-memory crisis without destroying the network. | phase required=true; retreat=encounter_defined; world mutation=true |
| BOS-005 The Ashen Measure / ACT-04 | ENM-032 + ENM-034 | Counter a triage engine that converts people into risk categories. | phase required=true; retreat=encounter_defined; world mutation=true |
| BOS-006 EnemyCommander: Siege of the Broken Route / ACT-04 | NPC-015 combat representation | EnemyCommander may retreat, yield, or be defeated; NPC state follows authored result. | phase required=true; retreat=encounter_defined; world mutation=true |
| BOS-007 The Archive's False Witness / ACT-04 | ENM-033 + ENM-030 | Verify evidence and counter repeated actions. | phase required=true; retreat=encounter_defined; world mutation=true |
| BOS-008 The Ferida Manipulator / ACT-05 | NPC-017 combat representation | Dialogue and combat are separate representations. | phase required=true; retreat=encounter_defined; world mutation=true |
| BOS-009 The Confluence Pattern / ACT-05 | ENM-035 + objective anchors | Disrupt anchors, maintain coalition links, complete world-state objective. | phase required=true; retreat=encounter_defined; world mutation=true |

## D. Special encounters — all 8 records
| ID / Encounter / Act | Purpose | Optional |
| --- | --- | --- |
| SPC-001 The First Threadling Nest / ACT-01 | Teach reinforcement and target prioritization. | true |
| SPC-002 The Sealed Clinic / ACT-01/02 | Optional care/containment dilemma. | true |
| SPC-003 The Caravan in the Salt Storm / ACT-03 | Protect supplies or rescue stragglers. | true |
| SPC-004 The Silent Grove / ACT-03 | Exploration and knowledge check. | true |
| SPC-005 The Broken Lift / ACT-04 | Objective encounter with environmental hazards. | true |
| SPC-006 The Evacuation Clock / ACT-04 | Timed objective, not a pure damage race. | true |
| SPC-007 The Unreliable Signal / ACT-04 | Modifiers change after evidence gathering. | true |
| SPC-008 The Empty Throne / ACT-05 | Optional encounter testing delegation and ally synergy. | true |

## E. Facilities — all 12 records
| ID / Facility | Unlock | Effect | Upgrades |
| --- | --- | --- | --- |
| FAC-001 Recovery Room | Act I choice | Health/status recovery and care route. | 3 |
| FAC-002 Common Workshop | Act I choice | Basic crafting, repairs and equipment modification. | 3 |
| FAC-003 Coordination Board | Act I choice | Assignment visibility and Expedition overview; never gates Expeditions. | 3 |
| FAC-004 Storehouse | Act II | Production buffer and resource reporting; no inventory capacity limit. | 3 |
| FAC-005 Training Yard | Act II | Training assignments and combat aptitude development. | 3 |
| FAC-006 Research Annex | Act II | Ferida research, enemy knowledge and recipe discovery. | 3 |
| FAC-007 Alchemy Bench | Act II | Consumables, botanical processing and controlled transmutation. | 3 |
| FAC-008 Trade Stall | Act II | Local trade and market opportunities. | 3 |
| FAC-009 Community Hall | Act II | Council, representation, grievance review and morale. | 3 |
| FAC-010 Refuge Wing | Act II | Housing, rehabilitation and integration capacity. | 3 |
| FAC-011 Expedition Lodge | Act III | Specialist preparation, route intel and Expedition risk modifiers. | 3 |
| FAC-012 Signal Tower | Act IV | Regional warning network and late-game coalition coordination. | 3 |

## F. Resources — all 8 records
| ID / Resource | Use | Rarity / cap |
| --- | --- | --- |
| RES-001 Timber | Construction and repairs | Common / no cap |
| RES-002 Fiber | Bindings, reinforcement and field kits | Common / no cap |
| RES-003 Botanical Extract | Care, alchemy and stabilization | Common / no cap |
| RES-004 Gold | Trade, wages, contracts and services | Currency / no cap |
| RES-005 Provisions | Community upkeep, travel and evacuation | Common / no cap |
| RES-006 Salvage | Mechanical parts and advanced repairs | Uncommon / no cap |
| RES-007 Research Notes | Knowledge unlocks and controlled research | Uncommon / no cap |
| RES-008 Trust Tokens | Specific reciprocal commitments and coalition actions; never a universal currency | Agreement-bound / no cap |

## G. Items and equipment — all 36 records
| ID / Item | Slot | Identity | Production requirements |
| --- | --- | --- | --- |
| ITM-001 Crux of Enlightenment | Accessory | Balanced Soul/Body and H-damage specialization. | effect contract=true; asset mapping=true |
| ITM-002 Oath of Obedience | Bottom1 | Blessed defensive sustain; unlock through a protection vow. | effect contract=true; asset mapping=true |
| ITM-003 Underwear of Restoration | Bottom1 | Recovery and status-cleansing synergy. | effect contract=true; asset mapping=true |
| ITM-004 Forever Cage | Bottom2 | Cursed evolution from True-Size Cage; Strain interaction. | effect contract=true; asset mapping=true |
| ITM-005 Chastity Belt | Bottom2 | Defensive anti-penetration/anti-control build. | effect contract=true; asset mapping=true |
| ITM-006 Ofuda Chastity | Bottom2 | Blessed defensive counterpart with Soul/Masochism profile. | effect contract=true; asset mapping=true |
| ITM-007 Hypnosis → Reprogram → Slave | Tattoo | Single cursed evolution chain; not three inventory records. | effect contract=true; asset mapping=true |
| ITM-008 Sensitivity → Receptacle → Fulfilled | Tattoo | Cursed incoming-pressure and recent-hit stages. | effect contract=true; asset mapping=true |
| ITM-009 Restraint → Suffer → Canvas | Tattoo | Cursed resistance/effect-conversion chain. | effect contract=true; asset mapping=true |
| ITM-010 Messaging → Sway → Pheromone | Tattoo | Blessed area-support chain with consent-aware presentation. | effect contract=true; asset mapping=true |
| ITM-011 Body Amulet | Accessory | Body-oriented stat profile. | effect contract=true; asset mapping=true |
| ITM-012 Agility Ring | Accessory | Agility-oriented stat profile. | effect contract=true; asset mapping=true |
| ITM-013 Soul Amulet | Accessory | Soul-oriented stat profile. | effect contract=true; asset mapping=true |
| ITM-014 Charm Ring | Accessory | Charm-oriented stat profile. | effect contract=true; asset mapping=true |
| ITM-015 Field Harness | Body | Expedition and repair preparation. | effect contract=true; asset mapping=true |
| ITM-016 Reinforced Boots | Feet | Travel hazard reduction. | effect contract=true; asset mapping=true |
| ITM-017 Sluiceworker Gloves | Hands | Construction and repair bonus. | effect contract=true; asset mapping=true |
| ITM-018 Herbal Satchel | Accessory | Care and alchemy output. | effect contract=true; asset mapping=true |
| ITM-019 Surveyor Lens | Accessory | Discovery and enemy intent information. | effect contract=true; asset mapping=true |
| ITM-020 Archive Seal | Accessory | Research protection and controlled access. | effect contract=true; asset mapping=true |
| ITM-021 Caravan Ledger | Accessory | Contract and trade insight. | effect contract=true; asset mapping=true |
| ITM-022 Guard's Buckler | Hands | Defensive reaction synergy. | effect contract=true; asset mapping=true |
| ITM-023 Thread-Cut Knife | Weapon | Ferida-filament utility; never automatic boss victory. | effect contract=true; asset mapping=true |
| ITM-024 Resonance Charm | Accessory | Research and Strain interaction. | effect contract=true; asset mapping=true |
| ITM-025 Expedition Rations | Consumable | Expedition preparation. | effect contract=true; asset mapping=true |
| ITM-026 Emergency Filter Kit | Consumable | One-use spread-risk mitigation. | effect contract=true; asset mapping=true |
| ITM-027 Healing Draught | Consumable | Restores Vitality within authored limits. | effect contract=true; asset mapping=true |
| ITM-028 Clear-Mind Tonic | Consumable | Reduces a defined control/Strain condition. | effect contract=true; asset mapping=true |
| ITM-029 Field Dressing | Consumable | Treats a defined injury state. | effect contract=true; asset mapping=true |
| ITM-030 Botanical Stabilizer | Consumable | Stabilizes an affected resident or encounter target. | effect contract=true; asset mapping=true |
| ITM-031 Smoke Pellet | Consumable | Supports retreat or encounter reposition abstraction. | effect contract=true; asset mapping=true |
| ITM-032 Thread-Salt | Consumable | Exposes or weakens a Ferida filament. | effect contract=true; asset mapping=true |
| ITM-033 Repair Kit | Consumable | Reduces a repair cost in eligible contexts. | effect contract=true; asset mapping=true |
| ITM-034 Research Sample Case | Quest/Utility | Preserves research samples. | effect contract=true; asset mapping=true |
| ITM-035 Seed-Reserve Ledger | Quest Item | Evidence record; distinct from the seed reserve itself. | effect contract=true; asset mapping=true |
| ITM-036 Coalition Signal Key | Quest Item | Coordination item; cannot bypass all world-state gates. | effect contract=true; asset mapping=true |

## H. Alya base outfits — all 8 records
| ID / Outfit | Role | Slot / battle representation |
| --- | --- | --- |
| OUT-001 Traveler's Lace | Default balanced baseline | Outfit; battle required=true |
| OUT-002 Field Armor | Defensive combat identity | Outfit; battle required=true |
| OUT-003 Witch's Mantle | Magic/research specialization | Outfit; battle required=true |
| OUT-004 Dancer's Regalia | Social/Charm and event presentation | Outfit; battle required=true |
| OUT-005 Nun's Habit | Restraint/protection identity, not a morality marker | Outfit; battle required=true |
| OUT-006 Formal Dress | Diplomacy and civic scenes | Outfit; battle required=true |
| OUT-007 Demon Armor | Late-game Ferida-facing gear with explicit trade-offs | Outfit; battle required=true |
| OUT-008 Shibari Harness | Specialized risk/reaction build with consent-framed presentation | Outfit; battle required=true |

## I. Full-game content counts
Current locked baseline: 5 acts; 47 main quest stages; 25 authored sidequests; 7 regions; 6 factions; 10 recruitable allies; 21 named recurring NPCs; 12 generic NPC templates; 35 enemy archetypes; 9 major bosses; 8 special encounters; 12 facilities; 8 resources; 36 item/equipment records; 8 Alya base outfits; 8 Expedition templates; 5 ending families; 67 canonical skill records. The content lock is design scope, not proof of complete runtime implementation, final balance, final art or finished dialogue.

## J. Additional locked gameplay rules
- Alya is the fixed protagonist; standard active party is Alya plus one selected ally, with narrative exceptions.
- Each community member has one primary assignment at a time. Assignment work pauses during an Expedition. Expedition participants are unavailable to the active party until return.
- Sidequests are direct player activities requiring Alya; Expeditions are autonomous community-delegated activities with delayed results.
- Travel follows a regional/locality graph and consumes game time; there is no tactical world grid. Combat has no grid positioning or independent range system; skills define valid targets.
- Inventory has no fixed capacity ceiling. Resource costs on the main path must remain feasible; optional crafting cannot consume reserved mandatory materials.
- Aptitude combines relevant stats/species/experience and time assigned. Characters without natural aptitude may improve more slowly; no initial assignment is a permanent hard lock.
- Facility/assignment outcomes should expose understandable estimates and contributing factors. Community systems should create meaningful trade-offs, not universal upkeep, excessive resource chains, a detailed farming simulator, or busywork.
- Individual adventure experience and shared community upgrades coexist. Recruitment, rehabilitation, integration and assignments should create narrative consequences, not only numerical bonuses.
- Encounter power bands are authored; do not use universal level scaling. Exact rates, costs, recipes, caps and progression curves require implementation/balance QA unless explicitly locked in a structured record.
- Main quest costs need guaranteed resource sources or explicit fallback rules. Optional content cannot soft-lock main progression.
- Five ending families are state-based, not a binary morality meter; do not show ending percentages.

## K. Complete game-architecture baseline
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


## L. Self-contained review guarantee
A reviewer can evaluate the game loop, content scope, enemy/boss/facility/resource/item/outfit baseline and architecture principles from this document alone. Embedded records are for review continuity; no external file is required to understand the listed decisions.
