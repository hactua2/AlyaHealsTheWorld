# Alya Heals The World

Game design repository organized around four active layers:

- `docs/architecture/` — current high-level source-of-truth documents.
- `docs/systems/` — active system specifications.
- `docs/implementation/` — implementation-facing contracts and technical behavior.
- `docs/NARRATIVE_CANON.md` — canonical narrative source of truth.
- `docs/MASTER_PLANNING_AUDIT.md` — master planning checklist and A→D completion gates.
- `docs/GDD_INDEX.md` — reference structure for the eventual complete GDD.

Historical audits, checkpoints, and superseded design material live under `docs/archive/` or are explicitly labeled as historical checkpoints.

Structured content data lives under `data/`; visual and reference assets live under `assets/`; prototype material lives under `prototype/`.

The repository intentionally separates **current decisions** from **decision history**. When documents disagree, `docs/architecture/GAME_ARCHITECTURE.md`, `docs/NARRATIVE_CANON.md`, and current system specifications take precedence according to their domain. Historical checkpoints preserve traceability but do not override the current source of truth.

## Planning gates

- **Checkpoint A — Architecture Complete:** COMPLETE.
- **Checkpoint B — Rules Complete:** NEXT.
- **Checkpoint C — Content Complete:** PENDING.
- **Checkpoint D — Production Complete:** PENDING.

The project should not introduce new macro-systems casually after Checkpoint A. New design proposals must first identify a demonstrated gap that cannot be solved by content, configuration, specialization, or extension of an existing interface.
