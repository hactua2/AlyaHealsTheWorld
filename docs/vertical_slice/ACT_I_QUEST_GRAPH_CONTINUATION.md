# AHTW — Act I Vertical Slice Quest Graph (Continuation)

**Parent:** `docs/vertical_slice/ACT_I_QUEST_GRAPH.md`  
**Content data:** `data/vertical_slice/act_i_content.json`

## VS1_Q06 — The Organization Arrives

**Type:** Main / Social / Faction · **Location:** Brackenford  
The Organization arrives because the waterworks may connect to downstream channels. NPC-005 Pragmatic Mentor provides real assessment, supplies, and a clear account of known and unknown risks. NPC-006 Institutional Representative proposes closing the lower sluice, isolating affected workers, and burning the root-vault. This reduces regional spread risk but abandons lower residents and seed stores.

The Mentor supports the risk assessment but argues that local information is incomplete. The Representative acknowledges the human cost and explains that the Organization cannot risk multiple downstream settlements on an unverified plan. Cuidadora says treatment can stabilize people but cannot make the water system safe by itself.

**Choice**
- Accept the plan in principle: raises institutional trust and grants a safer preparation item, but increases the cost of securing the lower residents later.
- Challenge the plan without an alternative: lowers institutional trust and triggers a request for evidence.
- Ask for time to produce an alternative: preserves access to dialogue and sets the third-solution route.

**State:** Set `VS1_ORG_PLAN_PRESENTED`; set `VS1_ORG_STANCE` to `ACCEPTED`, `CHALLENGED`, or `ALTERNATIVE_REQUESTED`. Unlock Q07. The third-solution route always remains available, but clues and trust change its cost.

## VS1_Q07 — Three Parts of a Third Option

**Type:** Main / Preparation / Community · **Location:** Hub and Ashfen Verge  
The alternative requires three components: local knowledge of the original water path; repair materials (Timber and Fiber plus a filter component); and care/coordination, with Cuidadora stabilizing workers while the Elder and Mara coordinate a controlled evacuation of the lowest terrace.

**Required actions**
1. Secure the repair-resource objective.
2. Obtain local participation from Mara or the Elder; trust affects cost but neither route is mandatory.
3. Complete a short encounter against a Hollow Warden guarding the root-vault.
4. Allocate limited filter material:
   - **Workers first:** lowers encounter pressure, but the final objective requires more defensive progress.
   - **Channel first:** lowers spread risk during the climax, but recovery takes longer.
   - **Staged diversion:** available if `VS1_CHANNEL_CLUE_FOUND`; reduces both costs but does not prevent the seed loss.

**State:** Set `VS1_THIRD_OPTION_READY`, `VS1_PREPARATION_PRIORITY` (WORKERS / CHANNEL / STAGED_DIVERSION), and `VS1_COMMUNITY_CONTRIBUTION`. Unlock Q08.

## VS1_Q08 — Hold the Sluice

**Type:** Main / Climax / Combat + Objective · **Location:** Ashfen Verge, POI 3: Root-Vault Sluice  
**Composition:** one Hollow Warden, one Root-Knot Anchor (objective entity), and optional Threadlings depending on preparation. Use authored power bands and behavior, not universal level scaling.

The player must stabilize the diversion, sever the active filament, and secure the gate. These are objective checks, not spatial movement; the combat model has no grid/range system. Defeating enemies alone does not win while the objective remains incomplete. The community contribution from Q07 reduces one objective requirement or removes one source of pressure. Retreat remains possible with a contextual result.

**Resolution:** The diversion is stabilized and downstream spread is prevented for now. The Root-Knot is contained/destroyed according to encounter outcome rules, without revealing the Ferida's true nature. The lower terrace seed reserve and a substantial part of the next planting cycle are lost regardless of preparation.

**State:** Set `VS1_SLICE_CRISIS_RESOLVED`, `VS1_SEED_RESERVE_LOST`, and `VS1_DOWNSTREAM_CHANNEL_SECURED`. Set `VS1_ORG_OUTCOME` to COOPERATION / STRAINED_COOPERATION / DISTRUST from prior stance and evidence. Unlock Q09.

## VS1_Q09 — What Remains

**Type:** Main / Consequence / Character · **Location:** Brackenford  
Residents learn that the seed reserve is gone and debate whether the effort was worth it. Mara accepts responsibility for her part without being treated as the sole cause. The Organization acknowledges that the third option prevented downstream spread but retains concern about its risk. The Mentor offers continued technical cooperation; the Representative requests documentation and limited oversight. Cuidadora explains that recovery needs routine care, reliable supplies, and delegated responsibility.

**Choice: first recovery priority**
- **Care first:** unlocks the recovery facility state and improves community trust.
- **Repair first:** unlocks the workshop/storage improvement and improves material throughput.
- **Coordination first:** unlocks the assignment/Expedition board earlier, while recovery remains basic.

Each option grants one benefit and delays another. None reverses the seed loss.

**State:** Set `VS1_RECOVERY_PRIORITY` and `VS1_COMMUNITY_LEADERSHIP_OFFERED`. Unlock Q10.

## VS1_Q10 — A Place That Must Continue

**Type:** Main / Leadership / Management transition · **Location:** Brackenford  
Community representatives recognize Alya as the person who coordinated the response and offer her a defined leadership role accountable to the community. Alya accepts; the Elder explicitly rejects the idea that leadership means unilateral control.

The player chooses one initial facility using the canonical building model:
- `FAC_VS1_RECOVERY_ROOM` (Stability): improves recovery access and supports Cuidadora's work.
- `FAC_VS1_COMMON_WORKSHOP` (Conversion): turns Timber/Fiber into repair bundles.
- `FAC_VS1_COORDINATION_BOARD` (Access): unlocks a clearer assignment and Expedition interface.

The other two remain visible future options; they are not granted for free. Cuidadora becomes recruitable if the player chose Care first or invests in the Recovery Room; otherwise she remains a trusted NPC and can be recruited later through a recovery quest. First Ally receives a starter community assignment.

**State:** Set `ACT_I_COMPLETE`, `VS1_ALYA_RECOGNIZED_LEADER`, `VS1_STARTER_FACILITY`, and `VS1_CUIDADORA_RECRUITED` (true/false). Unlock Q11.

## VS1_Q11 — First Delegation

**Type:** Management / Expedition tutorial · **Location:** Community hub  
The settlement needs replacement filter fiber and a survey of a safe upper route. The player assigns an eligible community member to `EXP_VS1_UPPER_ROUTE_SURVEY`, sees the purpose, estimated duration, possible result categories, and resource/time commitment, then launches it.

The Expedition resolves autonomously. The assigned ally is unavailable to the active party while away. At canonical completion time, the player receives a small Fiber cache, route knowledge, or a complication that costs time but does not erase the quest. The result unlocks a future option or reduces the next repair cost.

**State:** Set `VS1_FIRST_EXPEDITION_LAUNCHED`; on resolution set `VS1_FIRST_EXPEDITION_RESOLVED`. The slice is complete only after the result and its community impact are visible.

## State matrix

| Decision | Values | Downstream effect | Guardrail |
|---|---|---|---|
| Ration response | Enforced / Shared / Investigate | Trust, supplies, repair cost | Never blocks main path |
| Gate response | Closed / Temporary diversion / Withdraw | Cost and pressure | No unwinnable hidden state |
| Organization stance | Accepted / Challenged / Alternative requested | Relationship and support | Organization stays morally plural |
| Preparation | Workers / Channel / Staged diversion | Climax pressure and recovery duration | Seed loss remains |
| Recovery priority | Care / Repair / Coordination | Starting capability | No universal optimum |
| Cuidadora | Recruited / Deferred | Party/community options | Preserve later recruitment |
| Initial facility | Recovery Room / Workshop / Board | Immediate capability | Do not grant all three |

## Failure and persistence requirements

- Optional exploration failure costs time/reward, not access to the main quest.
- Retreat from normal encounters returns the party to a safe state with contextual cost and a chance to prepare again.
- The climax can be retried. Once its narrative resolution commits the seed loss, retry does not undo it.
- Invalid combat actions obey atomic validation: no partial cost commitment.
- Required materials have a fallback source; optional spending cannot softlock progress.
- The Expedition cannot block story progression indefinitely; duration and fallback follow the canonical time/Expedition contracts.
- Save/load preserves quest flags, choice consequences, seed loss, party, inventory, resources, facility/assignment state, and Expedition state.

## Graph definition of done

- Every stage has stable IDs, prerequisites, objectives, state transitions, consequences, and exit conditions.
- Every choice has deterministic effects and readable explanation.
- Main path does not require optional discovery, adult content, or perfect combat.
- The Organization's value and limitations are both visible.
- The climax has a combat objective distinct from reducing enemy Vitality to zero.
- The management transition and first autonomous Expedition are implemented as quest state.
- Do not reveal the Ferida's ultimate nature or the full truth of Alya's past in the slice.
