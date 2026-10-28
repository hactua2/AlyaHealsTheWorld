# AHTW — Local Knowledge Download Guide

## Recommended: download the complete repository

The safest way to preserve accumulated planning, implementation contracts, structured data, tools, tests, assets and history is to obtain the repository as a whole.

Repository: https://github.com/hactua2/AlyaHealsTheWorld

### Option A — GitHub ZIP (no Git setup required)
1. Open the repository.
2. Click Code → Download ZIP.
3. Extract it into a stable folder, such as D:/Projects/AlyaHealsTheWorld/ or ~/Projects/AlyaHealsTheWorld/.
4. Keep the folder structure intact. Do not move JSON catalogs away from data/ or specs away from implementation_spec/.
5. Give the local coding LLM access to the repository root, not just Markdown documents.

A ZIP is easy but does not include Git history and is inconvenient for pulling later updates.

### Option B — Git clone (recommended for ongoing implementation)
Run in a terminal:
git clone https://github.com/hactua2/AlyaHealsTheWorld.git

Then open the resulting folder in the coding environment. Before work, check:
git status --short
git branch --show-current

Keep changes in version control. Before implementation starts, create a dedicated implementation branch rather than editing a historical snapshot.

## What is the minimum to download?
For durable knowledge and reliable implementation, the recommended minimum is the entire repository. The current repository is the source of truth; a short summary cannot safely replace structured IDs, edge cases, legacy data, tests, prototypes or assets.

If storage/context budget makes the full repository impractical, use this minimum context pack for orientation, but make the full repository available on disk to the coding agent:
- docs/LOCAL_LLM_KNOWLEDGE_PACK.md
- docs/IMPLEMENTATION_LLM_MASTER_HANDOFF.md
- docs/GDD_INDEX.md
- docs/MASTER_PLANNING_AUDIT.md
- docs/architecture/GAME_ARCHITECTURE.md
- docs/NARRATIVE_CANON.md
- docs/IMPLEMENTATION_SPEC.md
- all of implementation_spec/
- docs/FULL_GAME_CONTENT_LOCK.md
- all three data/content/*.json catalogs
- docs/vertical_slice/ and data/vertical_slice/
- data/skills/skills.csv and data/skills/skill_definitions.json
- docs/characters/ and relevant docs/art/ references
- tools/, tests/ and .github/workflows/

This still may not include all runtime dependencies if the local agent needs legacy CSVs, prototypes or assets; full checkout remains recommended.

## How to provide context to a local coding LLM
1. Open the repository root as the workspace.
2. Set docs/LOCAL_LLM_KNOWLEDGE_PACK.md as the first context/readme.
3. Give docs/IMPLEMENTATION_LLM_MASTER_HANDOFF.md as the operating contract.
4. Ask it to follow the first-task prompt at the end of that handoff.
5. Let the agent inspect files on demand; avoid pasting every large JSON into one prompt.
6. Keep these guides in version control and update them when canonical decisions change.

## Important
A knowledge pack is not the runtime. Do not assume the repository contains a working Unity project. The implementer must verify the actual project root, editor version, packages and existing code before changing runtime files.

## Pre-flight checklist
- [ ] Full repository cloned or ZIP extracted.
- [ ] Local working branch created (Git workflow).
- [ ] Knowledge pack read.
- [ ] Master implementation handoff read.
- [ ] Repository reconnaissance completed.
- [ ] Existing validators/tests run and results recorded.
- [ ] Unity root/version verified before runtime changes.
- [ ] No canonical IDs or legacy content overwritten without migration plan.
