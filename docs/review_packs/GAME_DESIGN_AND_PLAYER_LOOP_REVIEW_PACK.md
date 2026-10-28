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

## Canonical references

- `docs/architecture/GAME_ARCHITECTURE.md`
- `docs/MASTER_PLANNING_AUDIT.md`
- `docs/FULL_GAME_CONTENT_LOCK.md`
- `data/content/full_game_world_catalog.json`
- `data/content/full_game_gameplay_catalog.json`
- `docs/vertical_slice/ACT_I_CONTENT_CATALOG.md`
- `docs/vertical_slice/ACT_I_QUEST_GRAPH.md`
- `docs/PROJECT_STATE_AND_ROADMAP.md`
