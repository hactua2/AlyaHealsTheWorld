# Content & Asset Master Plan — Alya Heals the World

## Purpose
This is the master production-planning document for concrete game content and the visual/audio/UI assets required to ship it. It is the primary planning reference for **Checkpoint C — Content Lock**.

It does not replace the GDD, system specifications, or implementation contracts. Those define what the systems mean and how they behave. This document answers: **what concrete content do we need, how much of it is enough, and which production assets depend on it?**

## Current status
**Checkpoint C: IN PROGRESS — C1 COMPLETE**

Core rules and implementation contracts are closed. The content inventory has now been audited; the remaining work is to lock the concrete rosters and then derive the definitive asset list.

## C1 baseline

The detailed audit is recorded in `docs/C1_CONTENT_INVENTORY_AUDIT.md`.

Key conclusion: the repository already contains a substantial concrete content base. We should **not expand every category to a numerical quota**. Skills and items are already near healthy scope; enemy expansion should be driven by encounter-role coverage; the largest gaps are recruitable allies, NPC population definitions, explicit boss/encounter structure, facilities, world locations and content-to-asset mapping.

## Content targets

| Category | C1 baseline | Target / healthy range | C1 status |
|---|---:|---:|---|
| Skills | ~50 existing + approved additions | ~55–70 final | 🟢 consolidate, don't inflate |
| Skill icons | Partial | 1 per skill | 🟡 map assets |
| Skill cut-ins | Partial | ~35–45 where presentation warrants | 🟡 map assets |
| Enemy types | 25 concrete entries | ~40–50 if role coverage requires | 🟡 role audit first |
| Bosses | No explicit boss roster | ~8–10 | 🔴 define |
| Mini-boss / elite encounters | Some elites; incomplete encounter roster | ~8–15 | 🟡 define roles |
| Named NPCs | 16 role/archetype entries | ~15–25 important characters | 🟡 refine |
| Recruitable allies | Not explicitly locked | ~8–12 | 🔴 define |
| Generic NPC archetypes | Not explicitly catalogued | ~8–15 | 🔴 define |
| Items | 25 concrete entries | ~35–45 | 🟢/🟡 audit roles |
| Cursed equipment | Multiple concrete chains | ~8–12 meaningful pieces | 🟢 audit |
| Blessed equipment | Multiple concrete entries | ~4–6 meaningful pieces | 🟢 audit |
| Build-defining equipment | Some promising candidates | ~6–10 | 🟡 identify |
| Alya outfits | 11 named slots | ~8–12 meaningful | 🟢/🟡 specify |
| Facilities / buildings | No complete roster | ~10–14 logical facilities | 🔴 define |
| Regions | No complete roster | ~6–8, narrative-driven | 🔴 define |
| Combat/exploration backgrounds | Assets exist but no final mapping | ~10–16 reusable bases | 🔴 map after world lock |
| Major story CGs | No complete mapping | ~15–25, story-driven | 🔴 map |
| Character/relationship CGs | No complete mapping | ~10–20, relationship-driven | 🔴 map |
| Minor event illustrations | No complete mapping | ~10–20 where useful | 🔴 map |
| UI icon families | Partial source assets | Complete system coverage | 🟡 taxonomy + registry |

## Asset registry requirement

Before the definitive art list is generated, establish an asset registry mapping:

`Asset ID → Content ID → Asset Type → Variant → Usage → Status → Source/Reference`

Use these statuses:
- **KEEP** — usable as-is;
- **REFINE** — usable after editing/cleanup;
- **REPLACE** — existing source should not ship;
- **REFERENCE** — visual reference only;
- **LEGACY** — retained for history, not production;
- **MISSING** — required but not present.

This is especially important because existing source assets include generated/hash-like filenames and therefore cannot safely be treated as canonical merely by filename.

## Checkpoint C sequence

- **C1 — Content Inventory:** **COMPLETE.** Existing data/assets compared with required content categories.
- **C2 — Protagonist & Outfits:** lock Alya's visual/gameplay presentation set.
- **C3 — Recruitable Allies:** lock ally roster and dependencies.
- **C4 — NPC Roster:** lock named and generic NPC archetypes.
- **C5 — Enemy Roster:** lock enemy families, encounter roles, elites, mini-bosses and bosses.
- **C6 — Skill Lock:** finalize skill roster and icon/cut-in/VFX requirements.
- **C7 — Item Lock:** finalize equipment, cursed/blessed, consumables and unique items.
- **C8 — Facility Lock:** finalize community buildings and visual progression.
- **C9 — World Lock:** finalize regions, locations and backgrounds.
- **C10 — Narrative/CG Lock:** map scenes/events to required illustrations and special presentation.
- **C11 — Asset Dependency Audit:** verify production assets have no unresolved upstream dependency and classify existing assets.
- **C12 — Content Lock Audit:** produce the definitive missing-art/content list and verify no required category or role is missing.

## Production stop rule

Once a category meets its functional target and has no uncovered gameplay/narrative role, additional content requires an explicit justification such as filling a gameplay gap, improving meaningful build diversity, supporting narrative, improving visual variety, or replacing removed content. "More content" by itself is not sufficient justification.

## Relationship to the GDD

The GDD index points to this document for Checkpoint C. Concrete catalogs remain in `data/` where practical; this document tracks completeness, production scope and dependencies. Final locked content should update the relevant structured data and this plan rather than living only in conversation history.

## Next gate
**C2 — Protagonist & Outfit Lock.**
