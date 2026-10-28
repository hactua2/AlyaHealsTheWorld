# AHTW — Discipline Review Dossiers

This index is designed for manual review without requiring the reviewer to navigate the full repository. Use the complete dossier for the relevant discipline. Each dossier includes its domain's current decisions, inventories, rules, structured content and open work; references are retained for traceability, not as required reading.

## Choose one dossier

| Reviewer / purpose | Self-contained dossier | Scope |
|---|---|---|
| Art director / character artist / CG artist | [ART_DIRECTION_AND_ASSET_REVIEW_PACK.md](ART_DIRECTION_AND_ASSET_REVIEW_PACK.md) | Visual direction, cast visual anchors, visual safety rules, CG/asset planning, production gaps. |
| Character designer / cast reviewer | [CHARACTER_DESIGN_REVIEW_PACK.md](CHARACTER_DESIGN_REVIEW_PACK.md) | Ten allies, named NPC roster, relationship constraints, H-content tiers, character guardrails. |
| Story editor / narrative designer | [STORY_AND_NARRATIVE_REVIEW_PACK.md](STORY_AND_NARRATIVE_REVIEW_PACK.md) | Canon, character arcs, five-act story, all 47 main quest stages, 25 sidequests, regions, factions, Expeditions and ending families. |
| Quest/dialogue/content writer | [WRITING_AND_DIALOGUE_DOSSIER.md](WRITING_AND_DIALOGUE_DOSSIER.md) | Editorial rules, voice, narrative canon, full world/quest catalog, authored Act I dialogue, quest graphs and Act I structured records. |
| Game designer / systems / economy / progression | [GAME_DESIGN_AND_PLAYER_LOOP_REVIEW_PACK.md](GAME_DESIGN_AND_PLAYER_LOOP_REVIEW_PACK.md) | Player loop, base/community management, progression/economy, enemies, bosses, encounters, facilities, resources, items and outfits. |
| Combat / skill designer / balance reviewer | [COMBAT_SKILLS_DOSSIER.md](COMBAT_SKILLS_DOSSIER.md) | Combat, effects and turn-resolution contracts; all 67 skill records; scaling profiles; semantic lock; reconciliation trail. |
| Unity / implementation / technical lead / coding agent | [IMPLEMENTATION_AND_ENGINEERING_DOSSIER.md](IMPLEMENTATION_AND_ENGINEERING_DOSSIER.md) | Architecture, implementation contracts, acceptance criteria, full structured catalogs, Act I data and skill data. Starts with repository reconnaissance. |
| Producer / project auditor | [../PROJECT_STATE_AND_ROADMAP.md](../PROJECT_STATE_AND_ROADMAP.md) and [../LOCAL_LLM_KNOWLEDGE_PACK.md](../LOCAL_LLM_KNOWLEDGE_PACK.md) | Status overview and project gates; these are concise orientation docs rather than full discipline dossiers. |

## Minimal download strategy

- For manual review, download **only the one dossier** matching the reviewer's discipline.
- Writing, combat, and implementation dossiers are larger because they embed full catalogs/contracts to avoid dependencies on other files.
- The art, character, story, and game-design packs also contain their domain inventories and constraints.
- For actual coding, a full repository checkout is still strongly recommended. A Markdown dossier cannot replace runtime code, Unity project settings, assets, tests, build scripts, or Git history.

## Authority and conflict policy

These dossiers preserve the distinction between designed/locked content and runtime-validated behavior. They are intended to be self-contained review copies; if a canonical source is later changed, update the relevant dossier to keep the offline copy current.

- Story truth: narrative canon and full-game content lock, embedded in the story/writing dossiers.
- High-level gameplay: architecture and game-design decisions, embedded in the game-design/implementation dossiers.
- Combat behavior: turn, status-effect, and combat contracts, embedded in the combat/implementation dossiers.
- Exact content: stable IDs and structured records are embedded in the relevant dossiers.
- Historical reconciliation passes provide decision history; the semantic lock and current normalized catalog define the combat baseline.
- Runtime readiness is not implied. The implementation dossier requires repository reconnaissance and evidence before any claim that a Unity project or tests are ready.

If a reviewer finds a conflict, report the exact ID/section and propose a correction; do not silently create a third version.
