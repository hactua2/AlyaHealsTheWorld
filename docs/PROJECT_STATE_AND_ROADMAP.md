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
