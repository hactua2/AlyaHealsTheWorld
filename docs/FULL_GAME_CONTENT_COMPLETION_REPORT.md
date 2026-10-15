# AHTW — Full-Game Content Completion Report

**Report date:** 2026-10-15  
**Scope:** Base-game content definition and content-lock readiness.  
**Overall verdict:** The full-game content-lock baseline is authored and internally cross-checked. **Formal Checkpoint C is not yet fully closed**, because final dialogue coverage, legacy-data reconciliation, detailed effect/reward implementation fields, asset mapping, and production review remain. Checkpoint D is still pending.

## 1. Executive summary

The repository now has a single canonical full-game content lock and three structured stable-ID catalogs. This converts the prior high-level narrative/system design into a concrete base-game plan suitable for implementation planning without inventing the core roster or act progression again.

Canonical reference:
- `docs/FULL_GAME_CONTENT_LOCK.md`

Structured catalogs:
- `data/content/full_game_world_catalog.json`
- `data/content/full_game_gameplay_catalog.json`
- `data/content/full_game_character_arcs.json`

The first eleven main quest stages retain cross-references to the existing vertical-slice IDs `VS1_Q01`–`VS1_Q11`; do not migrate or delete those IDs until save/data migration is explicitly designed.

## 2. Content inventory now defined

| Domain | Locked inventory |
|---|---:|
| Acts | 5 |
| Main quest stages | 47 |
| Authored sidequests | 25 |
| Regions | 7 |
| Factions | 6 |
| Recruitable allies | 10 |
| Named recurring NPCs | 21 |
| Generic NPC templates | 12 |
| Enemy archetypes | 35 |
| Major bosses | 9 |
| Special encounters | 8 |
| Facilities | 12 |
| Resources | 8 |
| Canonical item/equipment records | 36 |
| Alya base outfits | 8 |
| Expedition templates | 8 |
| Ending families | 5 |
| Canonical skill records | 67 existing catalog records |

The 47-stage quest graph supersedes the earlier estimate of 45. Q01–Q11 correspond to the Act I vertical slice. The three last stages of Act I remain distinct: loss acknowledgement, leadership/facility choice, and first autonomous Expedition.

## 3. Narrative completion

The five-act progression is locked at the content-definition level:

1. **Foundation — The Water We Share:** Brackenford, the Red Thread, a defensible but unjust containment proposal, a third solution, mandatory seed-reserve loss, leadership and first Expedition.
2. **Construction — A Place for the Uncounted:** refuge growth, assignments, representation, the Organization's pilot proposal, relocation conflict, and the institutional rupture.
3. **Consequences — The Cost of Being Free:** resource scarcity, trade leverage, regional disagreements, Mycelian memory, institutional pluralism and a three-region mutual-aid compact.
4. **Escalation — What the Wound Learns:** manipulated signals, evacuation, triage, Alya's return to over-centralization, the Shattered Archive and systemic Ferida pressure.
5. **Revelation and Resolution — A Future Without a Center:** Alya's past, the Ferida Manipulator, coalition commitments, distributed responsibility, the Confluence encounter and five world-state ending families.

The core narrative canon is preserved: the Organization remains internally diverse and sometimes necessary; the Ferida exploits existing vulnerabilities rather than explaining every injustice; Alya cannot solve the world alone; the final victory creates conditions for recovery without guaranteeing permanent eradication.

## 4. Character coverage

- All ten recruitable allies now have explicit recruitment concepts, personal arcs, signature identity, late-game contribution, and epilogue state.
- All twenty-one canonical named NPCs now have a game-long narrative function.
- Twelve reusable population templates cover common services and regional populations without inflating the named roster.
- NPCs do not take combat turns while functioning as NPCs. Recurring NPCs with boss/encounter roles use separate combat records.
- Adult content remains optional, adult-only, consent-aware, and never required for main-quest completion or ending access.
- NPC-020 remains intentionally retired and must not be reused.

## 5. Gameplay-content coverage

The gameplay catalog defines enemy family/role/signature hook for 35 archetypes; nine major bosses with explicit objective goals; eight special encounters; twelve facilities; eight resources; thirty-six canonical items; and eight retained Alya outfit sets.

Important locked guardrails:
- Encounters use authored power bands, not universal level scaling.
- Bosses with objective mechanics cannot be defeated solely by reducing enemy Vitality.
- Inventory has no fixed capacity limit.
- Main-path construction must always remain feasible; optional crafting cannot consume reserved mandatory materials.
- Expeditions are autonomous NPC/community activities. Assigned allies are unavailable to the active party until return. Sidequests require Alya.
- The Act I seed-reserve loss is mandatory and cannot be removed by an optional route.
- Facility choice does not gate the basic assignment or Expedition systems.

## 6. Validation performed in this pass

The three JSON catalogs were fetched back from the repository and parsed. A cross-reference audit then checked:

- valid act references for all main quests;
- valid region references for all main quests;
- valid sequential prerequisite references;
- valid encounter references from main quests;
- valid prerequisite references for sidequests;
- valid enemy references in boss compositions;
- expected ally/NPC counts;
- duplicate stable IDs within each catalog.

**Result: all checks passed** in this one-off audit.

This was a content-structure validation performed during this work. A reusable structural validator (`tools/validate_full_game_content.py`), regression tests (`tests/test_full_game_content.py`), and a CI workflow step have now been added. The new Python validator/tests and the updated workflow have **not yet been executed in this session**. No Unity runtime test, numerical balance test, or manual playtest was performed.

## 7. Remaining work before formally closing Checkpoint C

These are production-detail tasks, not reasons to reopen the five-act premise or the locked roster unless a concrete contradiction is found.

1. Run the newly committed `tools/validate_full_game_content.py` and `python -m unittest discover -s tests -p 'test_*.py' -v`; verify the updated GitHub Actions workflow passes.
2. Reconcile the new canonical IDs with legacy `data/enemies/enemies.csv`, `data/items/items.csv`, `data/characters/characters.csv`, and the skill catalog. Preserve useful legacy content; do not silently overwrite or discard it.
3. Expand every main quest and sidequest into final authored dialogue, explicit choice labels, precise state mutations, reward IDs/amounts, and failure/recovery transitions. The catalog currently contains objective steps, key choices, consequence intent, reward intent, exit flags, and dialogue key slots; it does not yet contain all final dialogue text or balanced reward values.
4. Finalize item stat/effect records, facility costs/upgrades, resource production/upkeep rates, and encounter AI parameters after the runtime data schema is established.
5. Build the asset registry: every stable content ID should map to `KEEP`, `REFINE`, `REPLACE`, `MISSING`, or `NOT REQUIRED` for relevant portraits, sprites, enemy visuals, icons, cut-ins, CGs, UI, audio and localization.
6. Define exact optional adult-scene unlock flags and scene scripts against character arcs; do not generate CGs merely to satisfy quotas.
7. Conduct content review for narrative continuity, accessibility, consent framing, localization readiness and edge cases.

## 8. Recommended next steps

1. Execute the new content validator and regression tests, then verify CI passes.
2. Reconcile legacy CSV data into the canonical IDs with a migration table.
3. Complete the detailed data for Act I first, keeping the existing vertical-slice package as the implementation test case.
4. Implement and playtest the vertical slice.
5. Apply validated schema and workflow patterns to Acts II–V, then complete asset mapping and production QA.

Do not start mass CG production, expand the enemy/item/skill count, or create additional systems until these tasks reveal a specific need.

## 9. Final status

**Content scope and content-lock baseline: AUTHORED.**  
**One-off static JSON and cross-reference audit in this pass: PASSED. Validator/tests/CI step: AUTHORED, execution pending.**  
**Formal Checkpoint C: NOT YET CLOSED.**  
**Runtime implementation, balance, asset production, localization, QA and release readiness: PENDING.**

This status is deliberately conservative: the project now has a much more complete, stable content plan, but a content catalog is not the same thing as a playable, balanced, fully produced game.
