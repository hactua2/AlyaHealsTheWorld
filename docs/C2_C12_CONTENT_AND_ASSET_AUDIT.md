# C2–C12 — Content, Roster & Asset Audit

## Purpose

This document consolidates the audits from C2 through C12. Its purpose is to determine whether the existing repository content is sufficient, what still needs to be defined, and what information must exist before a definitive production art list can be generated.

This is intentionally an **audit and production-readiness pass**, not a claim that every still-undefined content item has already been designed. Where upstream content is missing, the audit records the gap instead of inventing content silently.

---

# C2 — Protagonist & Outfit Audit

## Existing baseline

`data/characters/alya.csv` contains 11 outfit slots:

- Normal (Lace)
- Nude
- Slave
- Shibari
- CowPrint
- Dancer
- Witch
- Armor
- Nun
- Dress
- Demon Armor

## Assessment

**🟢 Quantity healthy.** The existing 11 slots already sit inside the planned 8–12 range.

The remaining work is classification rather than expansion:

- gameplay equipment vs cosmetic appearance;
- default vs acquired/unlocked appearance;
- battle-visible variants;
- portrait variants;
- event/CG usage;
- H-content usage;
- required icons and thumbnails;
- asset reuse opportunities.

## Decisions now locked

- Target final scope: **8–10 main outfits**.
- Outfits are a **unified equipment layer**; every outfit occupies the equipment slot and may provide stats/effects.
- Small visual variants may exist, but should remain limited.
- Each outfit is treated as a **separate AI-generated visual asset set**; do not assume modular reuse.
- Every final outfit needs **battle representation**.
- Only narratively special outfits need additional dedicated CG/cut-in treatment.
- The existing 11 slots are **not sacred**; retain, replace or remove them based on final content needs.
- Alya uses **sprite + portrait** in exploration/base presentation.
- Target base expression coverage: **~8–12 expressions**.
- Portraits may vary by outfit/equipment.
- Battle representation should be available per outfit, with shared animations where practical.
- Maintain an internal body/anatomy reference and versions required for CG/H-content production.
- Maintain a full Alya character reference bible covering identity, outfits, expressions, proportions and generation rules.
- Every skill has an icon and **every final skill has a cut-in**; whether cut-ins vary by Alya outfit remains a separate pending decision.
- Only visually important gameplay states require dedicated art.
- Some outfits may have special damaged/altered states.

## Recommendation

Do not add outfits merely to increase variety. Consolidate the existing slots into the 8–10 final candidates after narrative/gameplay mapping.

## Art requirements

For each final outfit:
- full-body reference;
- battle representation;
- portrait variant if required;
- inventory/equipment icon if gameplay-linked;
- event/CG variant only when narratively important;
- cut-in dependency, if any.

---

# C3 — Recruitable Ally Audit

## Existing baseline

The character catalog contains several ally-oriented entries, including Ranger, WitchAlly, Dancer, Nun, RebelCommander, Wanderer and Monk. However, these records are role/archetype placeholders rather than a complete recruitable roster.

## Assessment

**🟡 Strong candidate roster; final character-level specification still in progress.**

Recommended final scope: **8–12 recruitable allies; 10 is the preferred planning target.**

The current candidate roster contains 10 conceptual slots. The roster is treated as a target, not a hard mathematical requirement; a final range of roughly 8–12 remains acceptable if the audit identifies a genuine redundancy or missing role.

## Global ally rules locked so far

- All recruitable allies can participate in H-content.
- H-specialization is a **secondary dimension**, not a formal class.
- Classes/roles are flavor rather than rigid gameplay classes.
- Species influence natural aptitudes but do not rigidly determine builds.
- Characters without natural aptitude take longer to develop a function.
- Allies are special community members and may be assigned to community activities.
- **Expedition = NPC/community-only activity; Alya does not participate.**
- An ally sent on an Expedition is unavailable to the active party while away.
- Sidequests require Alya/player participation.
- Some allies are major narrative characters; others may be more gameplay/community-focused.
- At least one ally is a jack-of-all-trades.
- At least one ally has high potential but poor initial performance and a faster-than-normal development curve.
- At least one ally is an explicit rival and is eventually recruitable.
- Some allies are highly specialized in community functions; community coverage is intentional but does not require one ally per facility.
- Some allies overlap in function, provided their execution and identity differ.

## Candidate roster after C3-A–G

| # | Provisional concept | Species | Presentation | Combat identity | Community identity | Narrative/recruitment role |
|---|---|---|---|---|---|---|
| 1 | First Ally / Generalist | Humanoid | **Femboy** | Generalist | Generalist | First ally; initially joins from a survival-oriented situation |
| 2 | Guardian | **Minotaur-like / strong wild species** | **Futanari** | Tank/Support | Security + training | **First ally recruited through combat**; doubles as an organic combat tutorial |
| 3 | Rival | Species pending | **Feminine** | Bruiser/DPS | Community function unlocks after recruitment | Mid-game recruitable antagonist; ideology/pragmatism/leadership conflict with Alya |
| 4 | Scholar / Erudite | Species pending; elf-like candidate | **Feminine** | Hybrid mage | Research | Fascinated by Alya's healing and treats it as something to understand/study |
| 5 | Caregiver | Species pending | **Futanari** | Healer/Support | Physical health and recovery | Community-focused support specialist |
| 6 | Artisan | Species pending | **Feminine** | Utility/control | Production; improvisation; equipment modification | Unexpected production specialist; initially works for rewards before bonding with the community |
| 7 | Fox Huntress | **Fox beastfolk** | **Futanari** | **Ranged DPS + traps** | Expeditions | Adventurous explorer; high-value Expedition specialist |
| 8 | Merchant | Species pending | **Femboy** | Utility/debuffer | Commerce/economy | Charismatic opportunist; wants to build a commercial empire and believes money solves many problems |
| 9 | Misfit / Inadapted | Species pending | **Futanari** | Generalist with high growth potential | Unexpectedly high aptitude in a specific community area | Optional sidequest recruit; initially poor due to mismatched attributes/aptitudes and lack of training, but develops unusually fast |
| 10 | Devotee / Community Anchor | **Faerie-like species** | **Feminine** | Protection + buffs | Social cohesion, morale, mediation, integration and welfare | Encountered helping people during a crisis; initially shy about H-content but becomes comfortable |

## Roster audit decisions

- Target remains **10 allies**, with **8–12 acceptable** if later evidence justifies adjustment.
- Approximately **8–9 allies should be meaningfully combat-capable**, while 1–2 may be much more community-oriented.
- Approximately **7–8 allies should be excellent community contributors**.
- The first ally and the Misfit are both generalists but deliberately distinct: the first has immediate versatility; the Misfit has unusually high long-term learning/growth.
- The Guardian and Caregiver are considered sufficiently distinct: **Guardian prevents/mitigates harm; Caregiver restores physical condition/recovery**.
- The Huntress and Artisan have utility overlap but different execution and identity; no change required.
- The Merchant should be combat-viable but is not intended to be a specialist; his kit is primarily item/resource-driven. No dedicated combat specialization is required for him.
- No additional melee DPS is currently required; only add one if a concrete later gap appears.
- Magic should be distributed across multiple characters; the Scholar is the most obvious magical specialist but does not need to be a rigid "mage class".
- The Rival should gain a community function only after recruitment, reinforcing the character's transition from antagonist to ally.
- No deliberately useless-in-combat ally is required.
- Community coverage should not be expanded merely to create one ally per facility. Generic NPCs, facilities and systems can cover functions without dedicated allies.
- Species diversity is considered healthy without requiring ten unique species.

## Character specification still required

Every final recruitable ally needs:
- stable character ID;
- exact species;
- sex/presentation classification;
- natural stats/aptitudes;
- combat role;
- starting skills;
- progression identity;
- AI profile;
- community aptitude;
- recruitment condition;
- narrative role;
- relationship hooks;
- visual requirements;
- portrait/battle representation requirements;
- H-content applicability and presentation requirements.

## Art implication

Every bespoke ally creates a dependency cluster. Avoid creating final ally art before the character-level roster is locked.

---

# C4 — NPC Roster Audit

## Existing baseline

There are 16 character records, but many are generic role labels such as Quest Giver, Quest Target, Ally or Ally that has quest.

## Assessment

**🔴/🟡 Skeleton exists; production roster does not.**

Separate the population into:

### Named NPCs
Target: **15–25 important characters**, including allies, recurring NPCs, merchants, leaders, quest-givers and antagonistic representatives.

### Generic community archetypes
Target: **8–15 reusable visual/social archetypes**.

Generic NPCs should not require bespoke art for every generated person.

## Art implication

Named characters require a character package; generic archetypes should be designed as reusable templates with controlled variation.

All NPC sex/presentation remains open at the character level, subject to the global visual direction defined for the project.

---

# C5 — Enemy & Boss Audit

## Existing baseline

The enemy catalog contains **25 concrete entries** spanning Tier 1–3 and Mob, Elite and Quest Target classifications. Examples include Guard, Slime, Goblin, Augmented, Kunoichi, Krakenblood, Witch, Mummy, Dullahan, Angel, Dragonkin, Fallen Angel, Lamia and Demon.

## Assessment

**🟡 Strong base, incomplete encounter taxonomy.**

The current list already has useful visual/species diversity. Do not automatically expand to 50.

### Required classification

Each enemy must be assigned:
- tier;
- encounter role;
- damage profile;
- control/support role;
- H-interaction role;
- AI identity;
- visual family;
- normal/elite/miniboss/boss role;
- quest/world availability.

### Recommended final scope

- **~30–40 normal/elite enemy types**, depending on role coverage;
- **~8–10 bosses**;
- **~4–8 miniboss/special encounters**.

The existing Tier 3 Quest Targets are boss candidates, not automatic bosses.

## Strategic recommendation

Prefer adding enemies to fill tactical gaps over adding species purely for visual novelty. A family can share a visual base while gaining meaningful gameplay/presentation differences.

All enemy sex/presentation remains open until the enemy-level visual audit, while the global aesthetic should remain predominantly feminine/futanari with no masculine male archetypes.

---

# C6 — Skill Presentation Audit

## Existing baseline

The skills audit states that the existing catalog plus 14 approved additions has no remaining critical need for generic skills.

## Assessment

**🟢 Content quantity; 🟡 asset mapping.**

Recommended final roster: **~55–70 skills**.

## Locked presentation rule

**Every final skill requires both:**
1. a skill icon representing the action;
2. a dedicated cut-in.

This supersedes the earlier planning assumption that only selected/signature skills would receive cut-ins.

Whether a cut-in changes based on Alya's equipped outfit remains **pending**.

## Required presentation classification

Every skill:
- icon;
- name/description UI data;
- cut-in;
- VFX/presentation class.

Passive skills also require the icon and cut-in under the global rule; the cut-in can use an appropriate non-combat presentation if a conventional attack animation is not applicable.

## Production target

Approximately:
- **55–70 skill icons**;
- **55–70 cut-ins**, subject to the final skill count.

Do not create additional skill content solely to increase asset volume.

---

# C7 — Item Audit

## Existing baseline

`items.csv` contains 25 concrete entries, including ordinary equipment, Blessed items, Cursed chains and gameplay-changing effects.

## Assessment

**🟢/🟡 Healthy base.**

The existing items already demonstrate meaningful identity rather than simple stat inflation.

## Remaining content roles

Audit for:
- consumables;
- resources/components;
- narrative/key items;
- equipment progression gaps;
- 6–10 build-defining pieces;
- cursed/blessed coverage;
- skill-modifying equipment.

Recommended final scope: **~35–45 meaningful item entries**, not a hard quota.

## Art implication

Every final item needs an icon. Only equipment with a visible character-state consequence needs additional presentation art.

---

# C8 — Facility Audit

## Assessment

**🔴 Real content gap.** No complete facility roster is currently represented in the audited content inventory.

Recommended planning scope: **~10–14 logical facilities**.

For each facility define:
- gameplay purpose;
- construction requirement;
- upgrade path;
- resource effects;
- staffing/assignment interaction;
- unlock dependencies;
- UI icon;
- exterior/interior representation;
- upgrade visual strategy.

## Art strategy

Do not assume 10–14 unique large illustrations. A smaller set of visual building families can support multiple logical facilities and upgrade tiers.

---

# C9 — World & Environment Audit

## Assessment

**🔴 Real content gap.** The repository does not yet provide a complete region/location roster from which a final background list can be derived.

Recommended planning scope: **~6–8 major regions**, driven by narrative rather than a quota.

Each region should define:
- narrative role;
- exploration locations;
- settlements/community locations;
- encounter pool;
- major story locations;
- map representation;
- reusable environmental family.

## Art strategy

Design environment families first. One background should support multiple encounters whenever composition permits.

Recommended initial production target: **~10–16 reusable environment/combat/exploration bases**, adjusted after world lock.

---

# C10 — Narrative / CG Audit

## Assessment

**🔴 Mapping gap.** Narrative canon is substantial, but there is not yet a complete scene-by-scene visual presentation inventory.

Do not lock CG counts independently of scenes.

## Required process

`Narrative Scene List → Character Presence → Outfit → Location → Emotional Beat → Presentation Class → CG / Cut-in / Background / Portrait`

Priority classes:
- major story CG;
- relationship/character CG;
- high-value H-content CG;
- minor event illustration;
- no unique art required.

Planning guardrail:
- **~15–25 major story CGs**;
- **~10–20 relationship/character CGs**;
- **~10–20 minor event illustrations**, only where they add value.

These are planning ranges, not mandatory quotas.

---

# C11 — Asset Dependency & Existing-Asset Audit

## Existing baseline

The source tree already has category areas for characters, enemies, items, main character, cut-ins, mechanics and UI, plus an `audio_legacy` area.

## Assessment

**🔴 Registry still required before production can be treated as deterministic.**

Existing source filenames include generated/hash-like identifiers, so filenames alone cannot establish what content an asset belongs to.

## Required asset registry

`Asset ID → Content ID → Asset Type → Variant → Usage → Status → Source/Reference`

Statuses:
- KEEP
- REFINE
- REPLACE
- REFERENCE
- LEGACY
- MISSING

## Required audit rules

An asset is not considered final merely because a file exists. It must be:
- identified;
- associated with canonical content;
- visually reviewed;
- checked for required dimensions/format;
- checked for variant coverage;
- marked with a production status.

---

# C12 — Content Lock & Definitive Art-List Audit

## Important distinction

A truly definitive per-file missing-art list cannot honestly be produced until C2–C10 have locked the upstream content rosters and C11 has classified the existing binary/source assets.

This audit therefore produces the **definitive requirement matrix** now, and identifies the exact gates needed before converting it into a file-level production checklist.

## Required final asset families

### Main character
- Alya base character package
- 8–10 final outfit variants
- required portrait/expression variants
- battle presentation variants
- equipment-linked presentation variants
- relevant event/CG variants

### Skills
- one icon per final skill
- **one cut-in per final skill**
- VFX/presentation assets according to skill class

### Allies / NPCs
- named character packages
- recruitable ally battle representations
- generic NPC archetype packages
- portraits/expressions as required

### Enemies
- one battle presentation package per final enemy type
- portraits/UI representation where required
- elite/miniboss/boss presentation variants
- H-interaction presentation where applicable

### Items
- one icon per final item
- special visual presentation only for items whose effect warrants it

### Facilities
- one icon per logical facility
- building/background representation
- upgrade variants where visual change is required

### World
- world map representations
- region/location backgrounds
- combat/exploration backgrounds
- special story locations

### Narrative / CG
- major story CGs
- relationship/character CGs
- high-value H-content CGs
- selected event illustrations

### UI
- status/effect icons
- resource icons
- currency icons
- quest icons
- facility icons
- map/location icons
- equipment-slot icons
- H-system UI graphics
- progression graphics
- other system-specific icon families

## C12 gate status

**🟡 Requirement-complete; file-level asset list pending registry and upstream content locks.**

This is the correct stopping point for the audit. Inventing individual missing filenames now would create false certainty.

## Final production workflow

Once C2–C10 content decisions are locked:

1. assign stable IDs to every content record;
2. classify every existing source asset against those IDs;
3. mark KEEP/REFINE/REPLACE/REFERENCE/LEGACY;
4. create MISSING rows for every required asset with no acceptable source;
5. deduplicate reusable assets;
6. record variants and dependencies;
7. export the production checklist sorted by asset type and priority.

## Final conclusion

The project has reached a **well-defined content-production phase**, but the final art shopping list should be generated only after the remaining content rosters are locked and existing assets are mapped. This prevents both underproduction and unnecessary regeneration.

**C2–C12 audit: COMPLETE as a planning audit.**

**Content Lock: PENDING upstream roster decisions + asset registry.**
