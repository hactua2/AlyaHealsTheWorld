# AHTW — Act I Vertical Slice Content Catalog

**Status:** First complete content-design pass for the vertical slice. Values are provisional and require runtime integration/balance QA.  
**Scope:** `docs/VERTICAL_SLICE_SCOPE.md`  
**Quest graph:** `docs/vertical_slice/ACT_I_QUEST_GRAPH.md` and `docs/vertical_slice/ACT_I_QUEST_GRAPH_CONTINUATION.md`  
**Dialogue:** `docs/vertical_slice/ACT_I_DIALOGUE_PACK.md`  
**Structured data:** `data/vertical_slice/act_i_quests.json` and `data/vertical_slice/act_i_content.json`

## 1. Locked slice decisions

- **Story:** *The Water We Share*, a local crisis in Brackenford and the adjacent Ashfen Verge.
- **Ferida manifestation:** locally called **the Red Thread**, visible red filament-like growth around an old irrigation system. The name is local shorthand, not an explanation of the Ferida's true nature.
- **Core dilemma:** the Organization's containment plan reduces downstream risk but abandons lower residents and the seed reserve; the third option requires local knowledge, supplies, care, and coordinated effort.
- **Mandatory loss:** the lower terrace seed reserve and part of the next planting cycle are lost, even after a successful climax. The story does not add a character death merely to make the cost feel serious.
- **End state:** the downstream channel is secured for now, Alya accepts accountable leadership, one facility is selected, and the player launches and receives the result of one autonomous Expedition.

## 2. Content inventory

| Content family | Included |
|---|---|
| Quest stages | 11 stable-ID stages from arrival through first delegation |
| Locations | Brackenford hub, Ashfen Verge, Silt Path, Old Weir, Root-Vault Sluice |
| Enemy archetypes | Frayed Husk, Threadling Swarm, Hollow Warden, Root-Knot Anchor |
| Encounters | 3 standard/preparation encounters and 1 objective-based climax |
| Resources | Timber, Fiber, Botanical Extract, Gold |
| Items | Filtered Root-Fiber, Soothing Tonic, Sluice Repair Bundle, Lower Terrace Seed Reserve |
| Facilities | Recovery Room, Common Workshop, Coordination Board |
| Expedition | Survey the Upper Route, with autonomous outcomes |
| Main characters | Alya, First Ally, Cuidadora |
| NPCs | Tavernkeeper, Community Elder, Pragmatic Mentor, Institutional Representative, one-off adult resident Mara Venn |
| Optional discovery | Channel Sample; enables the more efficient staged-diversion preparation |
| Optional art | One story illustration and at most one optional adult CG; neither is required for completion |

## 3. Enemy and encounter purpose

| Enemy | Tactical purpose | Introduced |
|---|---|---|
| Frayed Husk | Slow direct pressure; teaches target selection | First encounter |
| Threadling Swarm | Faster Strain/pressure application | Second encounter |
| Hollow Warden | Defensive elite with visible intent; rewards control/preparation | Preparation encounter |
| Root-Knot Anchor | Objective entity whose pressure continues until the sluice objective is completed | Climax |

The climax is not a normal elimination-only fight. The player must stabilize the diversion, sever the active filament, and secure the gate. Community contribution reduces one requirement or one pressure source. Exact meters and rewards are authored as provisional values in the structured catalog.

## 4. Resource and facility economy

The recurring resource set is intentionally small:
- **Timber:** repair and facility construction.
- **Fiber:** bindings, filters, repair bundles.
- **Botanical Extract:** recovery item crafting and contextual reward.
- **Gold:** conventional trade and small expedition cost.

The seed reserve is a unique narrative resource/state, not a recurring economy currency. No universal upkeep tax or per-node depletion simulation is introduced.

Facilities have distinct architectural roles:
- **Recovery Room — Stability:** repeatable recovery access and Cuidadora recruitment eligibility.
- **Common Workshop — Conversion:** transforms Timber + Fiber into repair bundles.
- **Coordination Board — Access:** makes assignments and autonomous Expeditions legible.

Only one facility is selected initially. The others remain visible future investments, making the choice consequential without making any option universally optimal.

## 5. Data contract and caveats

- Canonical quest IDs, flags, content IDs, and cross-references live in the two JSON files. Dialogue labels and display names are presentation, not identity.
- All provisional numeric values must be tuned against the actual resolver and encounter playtests; this pack is not evidence of runtime balance.
- Skill references should resolve to the canonical skill catalog on the production branch. Do not duplicate skill mechanics inside the slice content pack.
- Community resource/facility behavior must use `implementation_spec/ECONOMY.md` and `implementation_spec/BUILDINGS.md`; no parallel system is introduced.
- Encounter outcomes, turn ordering, effect lifecycle, and action atomicity must use the existing combat contracts.
- All characters are adults. Adult content is optional and not a reward for coercion, contamination, or institutional harm.

## 6. Next implementation gate

Before coding this slice, implement a static content-integrity check for:
1. unique IDs within and across namespaces;
2. every quest, location, enemy, encounter, item, resource, facility, discovery, and Expedition reference resolving;
3. all mandatory quest prerequisites reachable;
4. every mandatory resource having a fallback source;
5. the mandatory seed-loss state being set exactly on the climax resolution;
6. all choice flags being consumed by a downstream state, dialogue variation, reward, or unlock;
7. save/load coverage for quest flags, inventory, party, facility state, assignment, and Expedition state.

Then implement the vertical slice and perform runtime tests and balance tuning during implementation, as agreed.
