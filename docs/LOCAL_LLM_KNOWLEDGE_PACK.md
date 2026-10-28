# AHTW — Local LLM Knowledge Pack

Purpose: a compact orientation artifact for any local LLM/developer continuing AHTW without chat history. This is a map and executive synthesis, not a replacement for canonical specs or structured data.

## Read first
1. This file — product identity, approved decisions, content inventory, source hierarchy.
2. docs/IMPLEMENTATION_LLM_MASTER_HANDOFF.md — implementation sequence, engineering constraints, test gates and instructions to the implementer.
3. docs/LOCAL_KNOWLEDGE_DOWNLOAD_GUIDE.md — download and workspace setup.
4. docs/GDD_INDEX.md — domain-document map.
5. docs/MASTER_PLANNING_AUDIT.md — specification closure status.
6. docs/FULL_GAME_CONTENT_LOCK.md and data/content/*.json — concrete content and stable IDs.
7. docs/vertical_slice/UNITY_IMPLEMENTATION_HANDOFF.md — detailed first-slice implementation contract.

## Product definition
Alya Heals The World (AHTW) is a single-player, turn-based narrative RPG with light community/base management, exploration, direct sidequests, combat, equipment/skill progression, recruitment and rehabilitation/integration, production/assignments, and autonomous NPC-only Expeditions. Adult themes are part of the world's culture, relationships, biology, magic and narrative. Intimate content is optional, adult-only, consent-aware and not required for main-quest completion or endings.

The central character arc is not “Alya fixes everything herself.” Alya moves from avoiding responsibility, to accepting it, to over-centralizing decisions, to distributing responsibility, and finally to creating conditions that can survive without her as the center.

## Canonical conflict
- The Ferida amplifies vulnerabilities, fear, exploitation and failed correction. It does not explain every injustice or remove community agency.
- The Organization is necessary and competent in many contexts, internally diverse, and capable of protection as well as harmful standardization. It is not a monolithic evil faction.
- Communities face real scarcity, political disagreement and institutional incentives before supernatural pressure escalates them.
- Victory is not guaranteed permanent eradication of the Ferida. The durable outcome is a world more capable of correction, cooperation and local responsibility.

## Core loop and boundaries
Narrative progress unlocks regions, people, facilities and capabilities. Exploration, sidequests, encounters, Expeditions and quests produce resources, items, knowledge, recruitment opportunities and state changes. Those feed equipment, transmutation, construction, production, recovery, rehabilitation, assignments and specialization, which unlock further narrative possibilities.

- Sidequest: direct player activity; requires Alya/player participation.
- Expedition: delegated autonomous activity performed by eligible NPC/community members. Assigned allies are unavailable to the active party until return.
- NPCs do not take combat turns while functioning as NPCs. A recurring narrative identity can have a separate Enemy/Boss combat representation.
- Alya is the fixed protagonist. The standard direct party is Alya plus one selected ally, with narrative exceptions.
- One community member has one primary assignment at a time. Assignments stop operating while the character is away.
- Inventory has no fixed capacity limit.
- World travel uses a regional/locality graph and consumes game time; it is not a tactical grid.
- Combat has no grid positioning or independent range system. Skills define valid targets.
- Main-path resource costs must remain feasible; optional crafting cannot consume reserved mandatory materials.
- Use stable IDs, not display text or array indices, for cross-system references and saves.

## Combat and implementation invariants
Canonical turn lifecycle:
TurnStarted → Start-of-Turn Effects → Duration Update/Expiration → Derived State Recalculation → CanAct Check → Intent/Action Selection → Action Resolution → Triggered Reactions → End-of-Turn Effects → TurnEnded → Terminal Check.

- Initiative is randomized once at encounter start; Agility modifies the initial result; turn order remains fixed.
- Surrendered and Incapacitated are separate. Both prevent acting and both count as out of active combat.
- Combat ends when every member of one side is Surrendered and/or Incapacitated.
- An atomic action completes its declared pipeline before terminal state is committed.
- Insufficient resources make an action unavailable.
- AI preserves intent/action if a target becomes invalid, retargeting where possible; otherwise use explicit fallback.
- Effects have definitions and runtime instances with source, duration, stacks, state and optional provenance. Stacking is data-driven; strongest equivalent wins by default unless overridden.
- Equipment-derived effects disappear immediately when that equipment is removed. Cursed equipment preserves curse state as specified.
- Mutations commit before domain events publish. Events are immutable facts, not commands.
- Randomness must be deterministic/injectable for tests and sufficiently recorded for reproduction.
- Derived stats update immediately after relevant mutations; effective values may be calculated lazily after invalidation.

### Skills
The existing canonical skill catalog has 67 records. Do not invent replacement terminology or expand it just to meet a quota. Canonical mechanical vocabulary and meter migration are documented in docs/systems/combat/SKILLS_AUDIT.md, implementation_spec/SKILL_CATALOG.md, implementation_spec/COMBAT.md, implementation_spec/STATUS_EFFECTS.md and implementation_spec/TURN_RESOLUTION.md.

Neutral implementation vocabulary is the mechanical source of truth; thematic labels are presentation/localization. The approved migration maps H-gauge semantics to Strain where applicable and Health Damage to Vitality damage after validating each skill's meaning. P-growth is a capability/transformation enabling dependent skills. Skill tier conveys unlock/progression and power expectation. Unlocks combine Skill Points, prerequisites and progression gates. CSV is the primary catalog; complex mechanics live in structured companion data.

## Architecture
Use a maintainable indie-scale Unity architecture:
- Domain: plain C# entities/value objects, invariants and deterministic rules; no Unity scene/UI or service-locator calls.
- Application: use cases and orchestration.
- Infrastructure: JSON content, repositories, persistence, clocks/RNG adapters, logging, event bus.
- Presentation: Unity scene/UI/input/rendering adapters; no duplicate gameplay authority.

Dependency direction: Presentation → Application → Domain; Infrastructure implements contracts used by Domain/Application.

SOLID, composition, small interfaces, explicit state transitions and one source of truth. A service locator is acceptable only at the composition/bootstrap boundary, with explicit registration and fail-fast diagnostics. Prefer constructor injection within Domain/Application. Use a typed event bus for committed facts; never use events as a blanket substitute for direct calls or queries. Avoid speculative frameworks.

## Locked base-game inventory
| Family | Baseline |
|---|---:|
| Acts | 5 |
| Main quest stages | 47 |
| Authored sidequests | 25 |
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
| Items/equipment records | 36 |
| Alya base outfits | 8 |
| Expedition templates | 8 |
| Ending families | 5 |
| Existing canonical skill records | 67 |

The 47-stage graph supersedes an earlier 45-stage estimate. The first eleven main quest stages correspond to the Act I vertical slice and retain aliases VS1_Q01–VS1_Q11. Do not remove or rename these IDs without a migration plan.

## Five-act narrative spine
1. Foundation — The Water We Share: Brackenford, Ashfen Verge, Red Thread; water allocation dispute; the Organization's defensible but unjust containment proposal; Alya's third solution; mandatory loss of the lower-terrace seed reserve; leadership and first Expedition.
2. Construction — A Place for the Uncounted: refuge growth, assignments, representation, Organization pilot terms, relocation dispute and institutional rupture when Brackenford shelters people ordered relocated.
3. Consequences — The Cost of Being Free: shortages, trade leverage, regional disagreements, Mycelian memory and voluntary mutual-aid compact across three regions.
4. Escalation — What the Wound Learns: the Ferida exploits signals, governance, trust and triage; evacuation and network fracture; Alya's over-centralization returns; the Shattered Archive.
5. Revelation and Resolution — A Future Without a Center: Alya's past, Ferida Manipulator, coalition commitments, Confluence encounter, distributed responsibility and five ending families.

## Character guardrails
- The ten allies have non-redundant identities: generalist versatility; mitigation/interception; bruiser momentum; pure mage; treatment/recovery; construction/modification; ranged hunting/exploration; economy; adaptive long-term learning; protection/buffs and collective cohesion.
- NPCs are a separate role model, not substitute allies. NPC-020 is intentionally retired and must not be reused.
- All characters are adults with unambiguous adult visual presentation. Avoid child-coded proportions/terms. The world is humanoid fantasy first; beastfolk remain a minority.
- Species, culture, presentation and gameplay function are independent axes. Do not infer age, consent, role or personality from presentation category.
- Optional adult content is not a main-path gate. Use consent-aware framing; do not add scenes merely to satisfy a CG quota.

## Full-game source files
- docs/FULL_GAME_CONTENT_LOCK.md — act, quest, roster and content lock.
- data/content/full_game_world_catalog.json — quests, regions, factions, Expeditions and ending graph.
- data/content/full_game_gameplay_catalog.json — enemies, bosses, encounters, facilities, resources, items and outfits.
- data/content/full_game_character_arcs.json — allies, named NPCs and templates.
- data/vertical_slice/act_i_quests.json, act_i_content.json, act_i_effects.json — Act I implementation dataset.
- docs/vertical_slice/ACT_I_DIALOGUE_PACK.md, ACT_I_QUEST_GRAPH.md, ACT_I_QUEST_GRAPH_CONTINUATION.md, ACT_I_CONTENT_CATALOG.md — authored slice content.
- data/skills/skills.csv and data/skills/skill_definitions.json — canonical skill catalog.

## Art and production
Use docs/art/CHARACTER_IMAGE_PROMPTS.md for character prompt references and docs/art/CHARACTER_EROTIC_CG_MATRIX.md for the first-pass adult/sensual CG plan. These complement, but do not replace, docs/characters/CHARACTER_BIBLE.md, ALLIES_ROSTER.md and NPCS_DESIGN.md.

The asset list is not yet a verified file-by-file production inventory. Map every canonical ID/scene requirement to KEEP / REFINE / REPLACE / MISSING / NOT REQUIRED before mass asset generation, including portraits, sprites, icons, CGs, UI, audio and localization. Do not claim an asset exists merely because a prompt or requirement exists.

## Status and remaining gates
- Architecture checkpoint A: complete.
- Rules checkpoint B: complete.
- Implementation specification I1–I11: complete.
- Cross-system audit I12: complete.
- Full-game content-lock baseline: authored.
- Structural validator/tests: authored; execution/CI result must be checked.
- Checkpoint C (Content Complete): not formally closed. Remaining: run validator/tests/CI; reconcile legacy CSV/catalog IDs; finish exact dialogue, choice state mutations and reward IDs/values; finalize encounter/facility/economy parameters; asset registry.
- Checkpoint D (Production Complete): pending implementation, art/audio, localization, accessibility, integration tests, numerical balance, playtesting and QA.
- Do not state that a playable Unity runtime exists until repository reconnaissance confirms it.

## Source hierarchy and conflict policy
1. docs/architecture/GAME_ARCHITECTURE.md — high-level architecture.
2. docs/NARRATIVE_CANON.md — narrative truth.
3. docs/systems/ and implementation_spec/ — behavior and implementation contracts.
4. docs/FULL_GAME_CONTENT_LOCK.md — concrete content scope, identities and narrative beats.
5. data/ — structured content, stable IDs and exact records.
6. docs/characters/, docs/art/ and vertical-slice docs — specialized detail.
7. docs/archive/ — historical only; never overrides current sources.

If current sources disagree, do not silently pick one or invent a third rule. Identify the exact conflict, locate the authoritative domain, propose a minimal correction and record it. Never silently change stable IDs, save contracts, skill semantics, mandatory losses or character identities.

## Required behavior for a continuing LLM
- Read this pack, then the master implementation handoff and source docs relevant to the current phase.
- Inspect the actual repository before editing. Verify Unity root/version, packages, existing code, tests and CI; do not create a second project by assumption.
- Work in small milestones. First report the plan and likely files to change.
- Do not implement the whole game in one pass. Start with reconnaissance, content validation and bootstrap, then integrate the vertical slice.
- Add/update tests alongside behavior. Report exact commands/results; never fabricate execution results.
- Preserve legacy content; create explicit migration maps before replacement.
- After each milestone, report changed files, decisions, tests actually run, limitations and the next smallest task.
