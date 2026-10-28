# AHTW — Discipline Review Packs

These packs exist so external reviewers can assess one discipline without navigating the full repository. Each is a **self-contained review brief**: it includes the approved baseline, scope, constraints, open questions, and a short list of canonical deep sources. It is not a replacement for structured source data when a reviewer needs exact IDs or full records.

## Choose only what you need

| Reviewer / purpose | Start with | Optional second file |
|---|---|---|
| Art director / character artist / CG artist | `ART_DIRECTION_AND_ASSET_REVIEW_PACK.md` | `CHARACTER_DESIGN_REVIEW_PACK.md` |
| Character designer / cast reviewer | `CHARACTER_DESIGN_REVIEW_PACK.md` | `STORY_AND_NARRATIVE_REVIEW_PACK.md` |
| Story editor / narrative designer | `STORY_AND_NARRATIVE_REVIEW_PACK.md` | `CONTENT_WRITING_REVIEW_PACK.md` |
| Quest/dialogue/content writer | `CONTENT_WRITING_REVIEW_PACK.md` | `STORY_AND_NARRATIVE_REVIEW_PACK.md` |
| Game designer / systems designer | `GAME_DESIGN_AND_PLAYER_LOOP_REVIEW_PACK.md` | `COMBAT_AND_SKILLS_REVIEW_PACK.md` |
| Combat / skill designer | `COMBAT_AND_SKILLS_REVIEW_PACK.md` | `GAME_DESIGN_AND_PLAYER_LOOP_REVIEW_PACK.md` |
| Economy / community / progression designer | `GAME_DESIGN_AND_PLAYER_LOOP_REVIEW_PACK.md` | `COMBAT_AND_SKILLS_REVIEW_PACK.md` |
| Unity / implementation LLM | `../IMPLEMENTATION_LLM_MASTER_HANDOFF.md` | `../vertical_slice/UNITY_IMPLEMENTATION_HANDOFF.md` |
| Producer / project auditor | `../LOCAL_LLM_KNOWLEDGE_PACK.md` | `../PROJECT_STATE_AND_ROADMAP.md` |

## Minimal download strategy

Download **only the relevant review pack(s)** for a manual discipline review. The packs are intended to be readable as standalone Markdown documents. If the reviewer needs exact stable IDs, full quest records, skill definitions, or asset prompts, use the linked canonical sources listed at the end of that pack.

For implementation, the current handoff is intentionally separate: a coding LLM must inspect the real repository and must not assume that a playable Unity project already exists.

## Authority and conflict policy

- These packs are review-oriented syntheses, not new sources of truth.
- Story truth is governed by `docs/NARRATIVE_CANON.md`.
- High-level gameplay architecture is governed by `docs/architecture/GAME_ARCHITECTURE.md`; detailed mechanics by current system specifications and implementation contracts.
- Concrete full-game scope and stable IDs are governed by `docs/FULL_GAME_CONTENT_LOCK.md` and `data/`.
- Character identity and roster details are governed by `docs/characters/`; visual direction by `docs/art/`.
- The Act I vertical slice is governed by its quest graph, dialogue pack, content catalog, and structured JSON.
- Historical/archive documents do not override current canonical sources.

If a reviewer finds a conflict, they should report the file/section/ID and propose a correction; they should not silently create a third version.
