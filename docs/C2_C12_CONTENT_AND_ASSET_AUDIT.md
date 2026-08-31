# C2–C12 — Content, Roster & Asset Audit

## Purpose

This document consolidates the audits from C2 through C12. Its purpose is to determine whether the existing repository content is sufficient, what still needs to be defined, and what information must exist before a definitive production art list can be generated.

This is intentionally an **audit and production-readiness pass**, not a claim that every still-undefined content item has already been designed. Where upstream content is missing, the audit records the gap instead of inventing content silently.

## Overall conclusion

**Core systems: locked.**

**Content inventory: audited.**

**Content lock: not yet fully achieved.**

The project can now move through the remaining content decisions in a controlled way. The largest unresolved content dependencies are:

1. recruitable ally roster;
2. named/generic NPC roster;
3. enemy encounter-role matrix and boss roster;
4. facilities;
5. world/region/location roster;
6. scene-to-CG mapping;
7. asset registry/classification of existing source art.

Skills, items and Alya's outfit count are comparatively healthy and should be consolidated rather than expanded indiscriminately.

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

## Recommendation

Do not add outfits merely to increase variety. Treat the 11 existing slots as the candidate final set and only add one if a gameplay, narrative or meaningful visual role is uncovered.

## Art requirements to resolve

For each outfit:
- full-body reference;
- battle representation if visible;
- portrait variant if required;
- inventory/equipment icon if gameplay-linked;
- event/CG variant only when the outfit is materially important;
- any special cut-in dependency.

---

# C3 — Recruitable Ally Audit

## Existing baseline

The character catalog contains several ally-oriented entries, including Ranger, WitchAlly, Dancer, Nun, RebelCommander, Wanderer and Monk. However, these records are role/archetype placeholders rather than a complete recruitable roster. fileciteturn104file0L2-L2

## Assessment

**🔴 Not locked.**

Recommended final scope: **8–12 recruitable allies; 10 is the preferred planning target.**

## Required lock fields

Every recruitable ally needs:
- stable character ID;
- species/body archetype;
- natural stats/aptitudes;
- combat role;
- starting skills;
- progression identity;
- AI profile;
- community aptitude;
- recruitment condition;
- narrative role;
- relationship hooks;
- outfit/visual requirements;
- portrait/battle representation requirements;
- H-content applicability where relevant.

## Art implication

Every bespoke ally creates a dependency cluster. Avoid creating ally art before the roster and roles are locked.

---

# C4 — NPC Roster Audit

## Existing baseline

There are 16 character records, but many are generic role labels such as Quest Giver, Quest Target, Ally or Ally that has quest. fileciteturn104file0L2-L2

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

---

# C5 — Enemy & Boss Audit

## Existing baseline

The enemy catalog contains **25 concrete entries** spanning Tier 1–3 and Mob, Elite and Quest Target classifications. Examples include Guard, Slime, Goblin, Augmented, Kunoichi, Krakenblood, Witch, Mummy, Dullahan, Angel, Dragonkin, Fallen Angel, Lamia and Demon. fileciteturn105file0L2-L2

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

---

# C6 — Skill Presentation Audit

## Existing baseline

The skills audit states that the existing catalog plus 14 approved additions has no remaining critical need for generic skills. fileciteturn109file0L2-L2

## Assessment

**🟢 Content quantity; 🟡 asset mapping.**

Recommended final roster: **~55–70 skills**.

## Required presentation classification

Every skill:
- icon;
- name/description UI data;
- VFX/presentation class.

Active combat skills:
- combat presentation requirement.

Signature/H-skills:
- dedicated cut-in when justified.

Passive skills:
- generally no cut-in.

## Production target

Approximately:
- **55–70 skill icons**;
- **~35–45 cut-ins**, subject to actual eligibility.

Do not create a cut-in for every skill automatically.

---

# C7 — Item Audit

## Existing baseline

`items.csv` contains 25 concrete entries, including ordinary equipment, Blessed items, Cursed chains and gameplay-changing effects. fileciteturn106file0L2-L2

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

The source tree already has category areas for characters, enemies, items, main character, cut-ins, mechanics and UI, plus an `audio_legacy` area. fileciteturn103file0L2-L2

## Assessment

**🔴 Registry still required before production can be treated as deterministic.**

Existing source filenames include generated/hash-like identifiers, so filenames alone cannot establish what content an asset belongs to. fileciteturn107file0L2-L2

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
- 11 outfit variants
- required portrait/expression variants
- battle presentation variants
- equipment-linked presentation variants
- relevant event/CG variants

### Skills
- one icon per final skill
- cut-ins for eligible/signature skills
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
