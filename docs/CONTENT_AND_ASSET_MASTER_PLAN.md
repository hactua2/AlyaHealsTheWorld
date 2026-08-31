# Content & Asset Master Plan — Alya Heals the World

## Purpose
This is the master production-planning document for concrete game content and the visual/audio/UI assets required to ship it. It is the primary planning reference for **Checkpoint C — Content Lock**.

It does not replace the GDD, system specifications, or implementation contracts. Those define what the systems mean and how they behave. This document answers: **what concrete content do we need, how much of it is enough, and which production assets depend on it?**

## Current status
**Content & Asset Audit C1–C12: COMPLETE.**

**Content Lock: PENDING upstream roster locks and asset registry reconciliation.**

Core rules and implementation contracts are closed. The full C1–C12 audit established the content baseline, production guardrails, dependency order and asset requirement matrix. The next work is not another broad audit; it is closing the identified content decisions and then converting the requirement matrix into a file-level production checklist.

## Audit references

- `docs/C1_CONTENT_INVENTORY_AUDIT.md` — repository baseline.
- `docs/C2_C12_CONTENT_AND_ASSET_AUDIT.md` — consolidated C2–C12 audit.
- `docs/ASSET_GAP_LIST.md` — current production asset requirement baseline.

## Key conclusion

We should **not expand every category to a numerical quota**. Skills, items and Alya's outfit count are already near healthy scope. Enemy expansion should be driven by encounter-role coverage. The largest unresolved content gaps are recruitable allies, named/generic NPC populations, explicit boss/encounter structure, facilities, world locations and scene-to-asset mapping.

## Content targets / guardrails

| Category | C1–C12 baseline | Target / healthy range | Status |
|---|---:|---:|---|
| Skills | ~50 existing + approved additions | ~55–70 final | 🟢 consolidate |
| Skill icons | Partial | 1 per final skill | 🟡 registry |
| Skill cut-ins | Partial | ~35–45 where presentation warrants | 🟡 classify |
| Enemy types | 25 concrete entries | ~30–40 normal/elite if roles require | 🟡 role lock |
| Bosses | Candidates exist, no final roster | ~8–10 | 🔴 define |
| Mini-boss/special encounters | Incomplete | ~4–8 | 🟡 define |
| Named NPCs | 16 role/archetype entries | ~15–25 | 🔴 refine |
| Recruitable allies | Not explicitly locked | ~8–12 | 🔴 define |
| Generic NPC archetypes | Not explicitly locked | ~8–15 | 🔴 define |
| Items | 25 concrete entries | ~35–45 if roles require | 🟢/🟡 audit |
| Cursed equipment | Multiple chains | ~8–12 meaningful | 🟢 |
| Blessed equipment | Multiple entries | ~4–6 meaningful | 🟢 |
| Build-defining equipment | Some candidates | ~6–10 | 🟡 identify |
| Alya outfits | 11 named slots | ~8–12 meaningful | 🟢/🟡 specify |
| Facilities | No complete roster | ~10–14 logical | 🔴 define |
| Regions | No complete roster | ~6–8, narrative-driven | 🔴 define |
| Environment bases | Existing source assets, no final mapping | ~10–16 reusable bases | 🔴 map |
| Major story CGs | No final scene map | ~15–25, story-driven | 🔴 map |
| Character/relationship CGs | No final scene map | ~10–20 | 🔴 map |
| Minor event illustrations | No final scene map | ~10–20 where useful | 🔴 map |
| UI icon families | Partial | complete system coverage | 🟡 taxonomy |

These are **guardrails**, not quotas. A category is allowed to finish below or above a range when the gameplay and narrative justify it.

## Asset registry requirement

Before the definitive file-level art list is generated, establish:

`Asset ID → Content ID → Asset Type → Variant → Usage → Status → Source/Reference`

Statuses:
- **KEEP** — usable as-is;
- **REFINE** — usable after editing/cleanup;
- **REPLACE** — existing source should not ship;
- **REFERENCE** — visual reference only;
- **LEGACY** — retained for history, not production;
- **MISSING** — required but not present;
- **NOT REQUIRED** — requirement eliminated by reuse/scope decision.

Existing files with generated/hash-like names must be mapped to canonical content before they are considered production assets.

## Checkpoint C audit sequence

- **C1 — Content Inventory:** **COMPLETE.**
- **C2 — Protagonist & Outfits:** **AUDITED.** 11 existing outfit slots are within healthy scope; specification/classification remains to be locked.
- **C3 — Recruitable Allies:** **AUDITED.** Roster is the major unresolved character-content dependency.
- **C4 — NPC Roster:** **AUDITED.** Existing records are mostly archetype/role slots; named and generic populations must be separated and locked.
- **C5 — Enemy Roster:** **AUDITED.** 25 concrete enemies provide a strong base; role coverage and boss structure must determine expansion.
- **C6 — Skill Lock:** **AUDITED.** Quantity is healthy; presentation classes and asset mapping remain.
- **C7 — Item Lock:** **AUDITED.** Quantity and identity are healthy; remaining work is role coverage and final additions only where justified.
- **C8 — Facility Lock:** **AUDITED.** Concrete facility roster is still missing.
- **C9 — World Lock:** **AUDITED.** Region/location roster is still missing.
- **C10 — Narrative/CG Lock:** **AUDITED.** Scene-to-art mapping is still missing.
- **C11 — Asset Dependency Audit:** **AUDITED.** Registry/classification of existing source assets remains required.
- **C12 — Content Lock Audit:** **COMPLETE AS AUDIT.** Requirement matrix and asset gap baseline are established; file-level checklist awaits upstream locks + registry.

## Production dependency graph

`Rules → Narrative/World Structure → Content Roster → Gameplay Definition → Visual Specification → Asset Registry → Art Production`

## Production stop rule

Once a category meets its functional target and has no uncovered gameplay/narrative role, additional content requires explicit justification: a gameplay gap, meaningful build diversity, narrative need, visual variety problem, or replacement of removed content. "More content" alone is not sufficient.

## Next phase

The broad audit phase is complete. The project should now resolve the concrete roster decisions in this order:

**Protagonist/Outfits → Recruitable Allies → NPCs → Enemies/Bosses → Skills → Items → Facilities → World → Narrative/CG → Asset Registry → Final Missing-Art Checklist.**

The final deliverable of this phase is a production checklist in which every required visual asset is classified as **KEEP / REFINE / REPLACE / MISSING / NOT REQUIRED**, linked to a stable content ID and production priority.
