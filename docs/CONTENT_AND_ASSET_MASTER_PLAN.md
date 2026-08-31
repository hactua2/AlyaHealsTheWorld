# Content & Asset Master Plan — Alya Heals the World

## Purpose

This is the master production-planning document for concrete game content and the visual/audio/UI assets required to ship it. It is the primary planning reference for **Checkpoint C — Content Lock**.

It does not replace the GDD, system specifications, or implementation contracts. Those define what the systems mean and how they behave. This document answers: **what concrete content do we need, how much of it is enough, and which production assets depend on it?**

## Current status

**Checkpoint C: IN PROGRESS**

Core rules and implementation contracts are closed. Content is now being inventoried, completed and locked.

## Scope principle

Targets below are planning guardrails, not mandatory quotas. We stop adding content when every gameplay/narrative role is adequately represented and the content has sufficient variety. Avoid quantity-for-quantity's-sake, reskins without gameplay or presentation value, and redundant content.

## Content targets

| Category | Current planning inventory | Target / healthy range | Lock status |
|---|---:|---:|---|
| Skills | ~50 existing + approved additions | ~55–70 final | Audit/lock needed |
| Skill icons | Partial | 1 per skill | Production needed |
| Skill cut-ins | Partial | ~35–45 where presentation warrants | Production needed |
| Enemy types | ~25 | ~40–55 | Expand + lock |
| Bosses | Not fully catalogued | ~8–12 | Define |
| Mini-boss / elite encounters | Not fully catalogued | ~8–15 | Define |
| Named NPCs | ~16 archetype/slot entries | ~15–25 important characters | Refine + lock |
| Recruitable allies | Not fully locked | ~8–12 | Define + lock |
| Generic NPC archetypes | Limited | ~8–15 | Define |
| Items | ~25 | ~35–50 | Expand + lock |
| Cursed equipment | Existing subset | ~8–12 meaningful pieces | Audit |
| Blessed equipment | Existing subset | ~4–6 meaningful pieces | Audit |
| Build-defining equipment | Limited | ~6–10 | Define |
| Outfits for protagonist | Not fully catalogued | ~8–12 | Define |
| Facilities / buildings | Not fully catalogued | ~12–18 logical facility entries; fewer unique visual bases acceptable | Define |
| Regions | Not fully locked | ~6–8 | Define |
| Combat/exploration backgrounds | Not fully catalogued | ~10–16 reusable locations/bases | Define |
| Major story CGs | Not fully catalogued | ~15–25 | Narrative mapping |
| Character/relationship CGs | Not fully catalogued | ~10–20 | Narrative mapping |
| Minor event illustrations | Not fully catalogued | ~10–20 | Narrative mapping |
| UI icon families | Partial | Complete system coverage | Production spec |

## Asset rules by content type

### Skills

Every skill should have:
- stable ID;
- icon;
- name/description presentation;
- gameplay/VFX specification.

Active combat skills require combat presentation requirements. Signature/H-skills may receive dedicated cut-ins. Passive skills generally do not need cut-ins.

Planning target: roughly **55–70 skill icons** and **35–45 cut-ins**, rather than a one-to-one cut-in requirement for every skill.

### Enemies

Every enemy type needs:
- stable ID;
- combat role;
- visual archetype/family;
- portrait or equivalent UI representation;
- battle presentation requirements;
- animation/VFX requirements;
- H-interaction presentation requirements when applicable.

Enemy families may share visual bases/rigs when this provides production value without making the roster feel redundant.

### Characters / NPCs

Named characters should have, as applicable:
- visual reference;
- portrait;
- expression set;
- battle representation if combatant;
- outfit variants;
- event/CG requirements;
- relationship/H-content presentation requirements where applicable.

Generic community NPCs should use reusable archetypes rather than requiring a fully bespoke character package each time.

### Protagonist outfits

Separate:
1. gameplay equipment;
2. purely visual outfits;
3. outfits that also function as gameplay-affecting equipment.

Target approximately **8–12 meaningful protagonist outfits**, with variants sharing production resources where sensible.

### Items

Each item requires:
- icon;
- category;
- acquisition/source definition;
- gameplay effect or narrative purpose;
- presentation requirements.

Special attention should be given to cursed/blessed equipment and the planned **build-defining equipment** that can materially transform skill behavior (for example targeting, area, costs or effects).

### Facilities

Each facility requires:
- stable ID;
- gameplay role;
- upgrade/progression definition;
- icon/UI representation;
- visual representation/background as needed.

A facility tier may reuse a visual base where appropriate; logical facility count should not be confused with number of unique illustrations/models.

### World

Each region/location needs:
- stable ID;
- narrative role;
- gameplay role;
- map representation;
- environment/background requirements;
- encounter/content dependencies.

### CGs / event art

CGs should be mapped from narrative and gameplay importance, not generated mechanically for every quest. Major story beats, key relationships and high-value H-content should receive priority.

## Asset dependency principle

Before an asset enters production, its upstream content must be locked. Typical dependency chain:

`System Rule → Content Definition → Character/Enemy/Item/Skill Identity → Presentation Requirements → Asset`

Do not finalize expensive assets while their source content is still expected to change materially.

## Content lock definition

A category is **LOCKED** when:

- its roster is complete for the intended game scope;
- every entry has a stable ID;
- required gameplay fields are defined;
- narrative dependencies are known;
- AI/gameplay dependencies are known where applicable;
- visual asset requirements are enumerated;
- variants/reuse strategy is defined;
- no unresolved design decision can invalidate the roster.

## Checkpoint C sequence

- **C1 — Content Inventory:** audit existing data against all gameplay systems and narrative.
- **C2 — Protagonist & Outfits:** lock Alya's visual/gameplay presentation set.
- **C3 — Recruitable Allies:** lock ally roster and dependencies.
- **C4 — NPC Roster:** lock named and generic NPC archetypes.
- **C5 — Enemy Roster:** lock enemy families, elites, mini-bosses and bosses.
- **C6 — Skill Lock:** finalize skill roster and icon/cut-in/VFX requirements.
- **C7 — Item Lock:** finalize equipment, cursed/blessed, consumables and unique items.
- **C8 — Facility Lock:** finalize community buildings and visual progression.
- **C9 — World Lock:** finalize regions, locations and backgrounds.
- **C10 — Narrative/CG Lock:** map scenes/events to required illustrations and special presentation.
- **C11 — Asset Dependency Audit:** verify that production assets have no unresolved upstream dependency.
- **C12 — Content Lock Audit:** verify that all gameplay roles are covered and no required content/asset category is missing.

## Production stop rule

Once a category meets its functional target and has no uncovered gameplay/narrative role, additional content requires an explicit justification such as:

- filling a real gameplay gap;
- improving meaningful build diversity;
- supporting a narrative requirement;
- improving visual variety where repetition is a problem;
- or replacing content removed during production.

"More content" by itself is not sufficient justification.

## Relationship to the GDD

The GDD index points to this document for Checkpoint C. Concrete catalogs remain in `data/` where practical; this document tracks completeness, production scope and dependencies. Final locked content should update the relevant structured data and this plan rather than living only in conversation history.
