# C1 — Content Inventory Audit

## Purpose

C1 establishes the current baseline before we create or commission more content. It compares concrete content already represented in the repository with the functional categories required by the game and with the production guardrails in `CONTENT_AND_ASSET_MASTER_PLAN.md`.

This is an **inventory audit**, not yet a content-lock pass. A category can have a healthy quantity while still lacking roles, narrative identity, gameplay fields or asset requirements.

## Sources inspected

- `data/characters/alya.csv`
- `data/characters/characters.csv`
- `data/enemies/enemies.csv`
- `data/items/items.csv`
- `data/skills/` and the existing skills audit
- `assets/source/` category structure, including characters, enemies, items, main_character, cut_ins, mechanics, UI, audio_legacy and unclassified assets
- GDD index, architecture/system specifications and the Content & Asset Master Plan

## Executive summary

The repository already contains a meaningful concrete content base. The principal problem is **not lack of raw content**; it is that several categories are still represented as archetypes, candidates or partially specified records rather than a deliberately locked production roster.

### Current assessment

| Category | Baseline | Assessment | Action |
|---|---:|---|---|
| Skills | ~50 existing + approved additions | 🟢 Healthy | Consolidate; do not expand without a functional gap |
| Skill icons | Partial | 🟡 | Map every skill to an asset requirement |
| Skill cut-ins | Partial | 🟡 | Decide cut-in eligibility per skill |
| Enemies | 25 concrete entries | 🟡 | Audit encounter roles before adding more |
| Bosses | No explicit boss roster | 🔴 | Promote/define boss candidates |
| Elite/miniboss structure | Some elites, no complete encounter roster | 🟡 | Define encounter-role coverage |
| Named NPCs | 16 entries | 🟡 | Convert archetype/slot list into named roster |
| Recruitable allies | Not explicitly locked | 🔴 | Define final ally roster |
| Generic NPC archetypes | Not explicitly catalogued | 🔴 | Define reusable population archetypes |
| Items | 25 concrete entries | 🟢/🟡 | Audit role coverage; add only real gaps |
| Cursed equipment | Multiple concrete chains | 🟢 | Audit coverage, likely no major expansion |
| Blessed equipment | Multiple concrete entries | 🟢 | Audit coverage |
| Build-defining equipment | Some promising candidates | 🟡 | Identify and lock ~6–10 signature pieces |
| Alya outfits | 11 named outfit slots | 🟢/🟡 | Define gameplay/visual distinction and assets |
| Facilities | No complete concrete roster | 🔴 | Define facility set |
| Regions/locations | No complete concrete roster | 🔴 | Derive from narrative/world structure |
| Combat/exploration backgrounds | Asset folder exists, roster not mapped | 🔴 | Build location-to-asset matrix |
| CG/event art | No complete scene-to-CG inventory | 🔴 | Map after character/world/narrative locks |
| UI/icon families | Partial source assets | 🟡 | Define complete icon taxonomy |
| Audio | Legacy source exists | 🟡/🔴 | Audit and classify; do not assume final |

## Detailed findings

### 1. Skills

The skill system has already reached the point where quantity should stop driving design. The existing catalog plus approved additions is within the intended final range of roughly 55–70 skills.

**Decision:** treat skills as a consolidation problem, not an expansion problem.

Required next work:
- merge approved additions into the canonical catalog;
- verify every gameplay role/build has coverage;
- remove/rework redundant skills if discovered;
- assign stable IDs;
- assign icon requirements;
- assign cut-in eligibility;
- assign VFX/presentation requirements.

### 2. Enemies

`data/enemies/enemies.csv` currently contains 25 concrete entries. The roster already spans civilized, savage, tribal, loner and undead archetypes and Tier 1–3 progression, with Mob, Elite and Quest Target classifications.

**Important finding:** the current classification is not enough to prove encounter coverage. We should not blindly expand the roster to a numerical target.

The next enemy audit must classify every enemy by:
- combat role;
- party composition role;
- H-interaction role;
- tactical identity;
- tier/progression role;
- visual family;
- encounter availability;
- boss/elite/miniboss status.

Existing Tier 3 Quest Targets are natural boss candidates, but should not automatically become bosses.

### 3. Characters / NPCs

`characters.csv` contains 16 entries, but several are clearly role/slot definitions such as Ally, Quest Giver, Quest Target and Ally that requires a quest.

**Finding:** this is a narrative/content skeleton, not a production-ready character roster.

We need three explicit populations:
1. Named characters;
2. Recruitable allies;
3. Generic community NPC archetypes.

This separation will prevent the community system from multiplying bespoke art requirements.

### 4. Protagonist / outfits

`alya.csv` explicitly lists 11 outfit slots: Normal (Lace), Nude, Slave, Shibari, CowPrint, Dancer, Witch, Armor, Nun, Dress and Demon Armor.

This is already within the desired scale for Alya. fileciteturn90file0L2-L2

**Finding:** outfit count is not a major content gap. The missing work is specification:
- which are default/visual;
- which correspond to gameplay equipment;
- which require unique battle presentation;
- which require dedicated event/CG treatment;
- which assets already exist and which must be regenerated/refined.

### 5. Items

`items.csv` contains 25 concrete entries and already demonstrates the intended identity of the equipment system: ordinary equipment, Blessed equipment, Cursed evolving chains and behavior-changing effects. fileciteturn92file0L2-L2

**Finding:** item quantity is healthy. The remaining gap is mostly content-role coverage: consumables, resources, unique/narrative items and a small set of build-defining pieces.

### 6. Assets already in repository

The source tree already separates major visual categories into `characters`, `enemies`, `items`, `main_character`, `cut_ins`, `mechanics`, `ui` and `unclassified`, with a separate `audio_legacy` area. fileciteturn95file0L2-L2

This is useful, but filenames are not sufficient to establish asset ownership. Character source assets, for example, currently include generated/hash-like filenames rather than stable content IDs. fileciteturn96file0L2-L2

**Finding:** before declaring an asset "done", we need an asset registry mapping `Asset ID → Content ID → type → status → variant → usage`.

Recommended statuses:
- KEEP
- REFINE
- REPLACE
- REFERENCE
- LEGACY
- MISSING

### 7. Facilities

No equivalent concrete facility roster was found in the current content inventory.

**Finding:** this is a real content gap, not merely an asset gap. Facilities must be defined before facility art can be enumerated.

### 8. World / locations

No complete region/location catalog is currently sufficient to derive final environment asset requirements.

**Finding:** world content must be locked before backgrounds can be considered complete. Reusable environment bases should be planned deliberately.

### 9. CG / event art

There is no final scene-to-CG mapping in the current inventory.

**Finding:** CG production must wait until character, outfit and narrative scene dependencies are sufficiently stable. We should not create a target number of CGs independently of the story.

## Production dependency graph

The current audit establishes this dependency order:

`Rules → Narrative/World Structure → Content Roster → Gameplay Definition → Visual Specification → Asset Registry → Art Production`

For character-heavy assets:

`Character Roster → Character Design → Outfit Set → Expression/Portrait Set → Event/CG Mapping`

For enemy assets:

`Enemy Roster → Encounter Role → Visual Family → Battle Presentation → Asset`

For skill assets:

`Skill Roster → Skill Role → Presentation Class → Icon/Cut-in/VFX`

## C1 conclusion

The project is **not yet ready for a single final "missing art list"** because several upstream content categories remain unlocked. Producing that list now would cause churn.

However, the audit gives us a clear path:

1. Lock Alya/outfit specification (C2).
2. Lock recruitable allies (C3).
3. Lock named + generic NPC populations (C4).
4. Lock enemy roles and boss structure (C5).
5. Lock skill presentation requirements (C6).
6. Lock items (C7).
7. Lock facilities (C8).
8. Lock world/backgrounds (C9).
9. Map narrative/CGs (C10).
10. Build the final asset dependency registry (C11).
11. Generate the definitive missing-art list and declare Content Lock (C12).

### Key strategic conclusion

**Do not chase numerical quotas.** The existing skills/items are already near healthy scope, while enemies should be expanded only where encounter-role coverage demands it. The largest current gaps are recruitable allies, NPC population definitions, bosses/encounter roles, facilities, world locations, and the mapping of content to assets.

## Status

**C1 COMPLETE — proceed to C2.**
