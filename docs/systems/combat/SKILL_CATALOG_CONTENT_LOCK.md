# AHTW — Skill Catalog Content Lock
## Final semantic dispositions and production handoff

> **Status:** **DESIGN/SEMANTIC RECONCILIATION CLOSED** under the project owner's standing instruction to accept recommendations from this point forward. This lock settles skill identity, effect roles, target/outcome contracts, and consolidation policy. It does not claim numerical balance, runtime implementation, or QA are complete. The legacy `data/skills/skills.csv` is intentionally not migrated in this design-lock commit.

## 1. Canonical system rules

- Vitality is the primary defeat meter; Strain is the pressure/alternate-outcome meter.
- Command is a tactical control resource; Resolve supports deliberate exposure and reactions; Pressure rewards exploiting weaknesses; Fortitude supports defense and retaliation.
- Break is a prepared state, not a synonym for stun, disable, capture, or defeat.
- H-gauge maps semantically to Strain; Health Damage maps to Vitality damage. No blind text substitution.
- Tiers express progression expectation and expected power. Unlocks combine Skill Points, prerequisites, and optional milestone gates.
- Every skill uses a stable ID, explicit actor/target scope, canonical costs/generation, declared effects, scaling profile, requirements, timing, stack/refresh rules, outcome interactions, and presentation reference.
- Primary attributes are weighted first; the matching body-part affinity is then applied as a separate modifier. Multi-Aspect skills must explicitly define their combination rule.
- Similar actions can share effect templates while remaining distinct records when affinity/scaling, requirements, tactical role, cost, or risk changes player decisions.
- No finisher, passive, or reaction may bypass the encounter outcome contract or force global victory.
- Deterministic ordering, explicit caps, and recursion guards are required for multi-target actions, reactions, Chain, and Overflow.
- P-growth grants `CAPABILITY_P_GROWTH` to Alya only. Dependent skills require that capability at action-validation time.
- CSV migration remains a separate production operation; no schema rewrite is performed by this design lock.

## 2. Final legacy dispositions

All 54 named legacy rows have been reviewed. The nine unnamed placeholder rows are not skills and must be removed during eventual migration.

| Legacy entry | Final semantic disposition |
|---|---|
| Sensory Enhancement | Retain as a tagged vulnerability amplifier for explicitly named channels/effects. |
| Mstrbate | Retain as a self-recovery/risk action only if recovery and intent influence are represented as one explicit trade-off; otherwise split into separate records. The production record must not keep an unstructured effect bundle. |
| Dancing moves | Retain as an active, time-bounded evasion stance. |
| Flirt | Retain as a hybrid low-to-moderate Strain action and modest Command generator; combined efficiency is below specialized actions. |
| Hypnotize | Retain as intent manipulation or a defined resisted mental-control state; no implicit stun/DoT bundle. |
| Get Spanked | Retain as voluntary exposure that grants Resolve or a bounded reactive payoff when its declared incoming-event trigger resolves. |
| Sensory Deprivation | Retain as a debuff to explicitly named accuracy/evasion/defense stats. |
| Spank | Retain as a focused Strain attack; any Vitality damage is a conditional rider only. |
| Instill protectiveness | Retain as an explicit target-preference/ally-protection effect with named beneficiary and duration. |
| Bl-job | Retain as a basic focused Strain action with its own Aspect/scaling profile. |
| Lay | Retain as a focused Strain action; self-risk is absent unless authored as an explicit trade-off with payoff. |
| Grope | Retain as a focused Strain action with its declared multi-Aspect scaling rule. |
| Service | Retain as a support action with a declared recovery channel; default to Vitality recovery, not ambiguous “healing.” |
| H-job | Retain as a Mind-Aspect Strain DoT against mental/sensory vulnerability; use standard DoT lifecycle. |
| Bend | Retain as the baseline single-target Strain DoT. |
| AS | Retain as a Chain/sequence skill. Advance only when its primary effect applies to at least one valid target; reset on non-chain action, invalid action, encounter end, or loss of required capability/state. |
| S Symbol | Retain as a passive recovery listener on the canonical Overflow event. |
| Otherworldy Charm | Retain as a passive enemy-intent bias; do not duplicate Hypnotize's active control state. |
| Piercing Stares | Retain as a conditional passive Strain effect requiring its declared equipment condition. |
| Sadism | Retain as a passive modifier to Vitality damage dealt, with explicit stacking and cap. |
| Masochism | Retain as a passive modifier to declared mitigation/resistance channels, with explicit stacking and cap. |
| Moans | Retain as a bounded reactive reflection of qualifying incoming Strain; it is not a generic second Counter. |
| Encourage | Retain as an active, time-bounded buff to an ally's next qualifying attack. |
| Flaunt | Retain as reliable area Strain pressure without Strip's evasion rider or G-bang's group-size bonus. |
| Autof | Retain as a P-growth-gated self-recovery/cleanse action; declare each removable effect category. |
| Aphrodisiac | Retain as a single-target Strain DoT plus an explicitly bounded intent-bias rider only if both are one coherent action. |
| P-growth | Retain as Alya-only Capability/Transformation; declare persistence, revocation, and dependent skills. |
| Facesit | Retain as a focused action; self-risk only when explicit, with defined payoff and target-side semantics. |
| Bondage | Retain as a self-applied restraint/high-risk state with a declared payoff and deterministic expiry. |
| Bully | Retain as a named-stat debuff; do not use generic “weaken” semantics. |
| Bite | Retain as a focused Vitality attack; any Strain effect is conditional only. |
| Bind | Retain as a restraint/control state with explicit blocked actions, resistance, duration, and removal rules. |
| Prolonged Pl- | Retain as a temporary Overflow lock. On expiry/removal, re-evaluate Strain and emit the normal Overflow event if the boundary is met. |
| F-fk | Retain as a P-growth-gated focused Strain action with a capped bonus based on the target's remaining Vitality; declare calculation order. |
| Paizuri | Retain as a basic focused Strain action with its own Aspect/scaling profile. |
| Summon c-s | Retain as an area action with a capped concentration curve: fewer valid enemies increases per-target output, total output remains capped, target count is snapshotted at validation, and zero valid targets invalidates the action without cost. |
| Swallow | Retain as a single-target finisher request gated by Strain threshold/state and the encounter's permitted outcomes. |
| Extra tips | Retain as a passive reward modifier evaluated at encounter reward resolution, with a cap and no duplicate reward roll. |
| Cuteness | Retain as a passive ally attack modifier, with explicit scope and stacking. |
| Naughty Thoughts | Retain as a self-passive Strain accuracy/effectiveness modifier, with explicit cap. |
| C-drinker | Retain as a passive recovery trigger after a qualifying enemy defeat caused by an eligible skill; define recovery channel and event timing. |
| Strip | Retain as area Strain pressure plus a temporary self-evasion window against declared incoming attacks. |
| Pink mist | Retain as area Strain DoT plus a named defense debuff; use standard DoT and stat-debuff lifecycles. |
| Penetrate | Retain as a P-growth-gated focused Strain action; no implied stun. |
| A-penetration | Retain as a P-growth-gated focused Strain action with a defined control rider, subject to resistance and duration. |
| Stomp | Retain as a threshold conversion: Strain state increases Vitality damage under an explicit cap. |
| Summon Tentacles | Retain as a HighRisk area action that may affect enemies, allies, and the user. Declare each side's target/effect entry; use a validation-time target snapshot and deterministic ordering. |
| Enslave | Merge into the canonical `SKILL_ABSOLUTE_CONTROL` identity. Keep Enslave only as a presentation alias/legacy label, not a duplicate mechanical record. |
| G-bang | Retain as area Strain pressure with a capped bonus that increases with the number of valid enemies; distinct from Flaunt and Summon c-s. |
| Bkakke | Retain as an all-target finisher request. Resolve each target independently; successful outcomes persist. Each failed/ineligible target triggers a declared self-risk consequence. Victory requires every target request to succeed. |
| Deepth | Retain as a basic focused Strain action with its own Aspect/scaling profile. |
| Worship C | Retain as an area intent-bias action; do not also apply an unrelated vulnerability bundle. |
| Ecstasy Aftershocks | Retain as a passive area retaliation listener on the canonical Overflow event. |
| Divine Health | Rework as conditional resistance and/or a restricted cleanse tied to a declared recovery event; no blanket debuff immunity. |

## 3. Fourteen proposed additions — final disposition

| Canonical ID | Display role | Disposition |
|---|---|---|
| `SKILL_PROVOKE` | Provoke | Retain: changes enemy target preference/intent toward a declared actor. |
| `SKILL_ENDURE` | Endure | Retain: active mitigation and bounded Fortitude generation. |
| `SKILL_COUNTER` | Counter | Retain: deterministic response to a qualifying declared enemy action/intent. |
| `SKILL_COMMAND` | Command | Retain as a Command-resource generator; it does not also spend Command. |
| `SKILL_RECOVER_COMPOSURE` | Recover Composure | Retain: reduce Strain or remove a narrowly declared eligible state; channel is explicit. |
| `SKILL_EXPLOIT_WEAKNESS` | Exploit Weakness | Retain: consumes/exploits a tagged vulnerability to generate Pressure or amplify a declared channel. |
| `SKILL_BREAK_RESISTANCE` | Break Resistance | Retain as setup that lowers resistance/prepares Break; not a full disable. |
| `SKILL_TURN_THE_TABLES` | Turn the Tables | Retain: converts a specific recent combat event into a bounded response/recovery/retaliation. |
| `SKILL_FOCUS_SURGE` | Focus Surge | Retain: bounded self-buff to the next qualifying action; explicit expiry and no stacking by default. |
| `SKILL_DIRECT_ALLY` | Direct Ally | Retain: improves or redirects one ally action only if action-economy rules permit it. |
| `SKILL_ABSOLUTE_CONTROL` | Absolute Control | Canonical merged Enslave identity: high-investment finisher requesting one authored permitted outcome (Yield, Disable, or Capture). |
| `SKILL_UNBROKEN` | Unbroken | Retain: narrowly prevents one declared defeat/disable event with strict frequency/cooldown limits; never grants general immunity. |
| `SKILL_OVERFLOW_ENGINE` | Overflow Engine | Retain: active/configurable conversion of a canonical Overflow event into one declared output. |
| `SKILL_MUTUAL_RUIN` | Mutual Ruin | Retain as a HighRisk mutual-outcome action with explicit eligibility, both-side consequences, caps, and encounter-outcome validation. |

## 4. Shared rules for the three Overflow skills

- A canonical Overflow event is emitted at most once per affected actor per resolved action when the boundary is crossed.
- S Symbol recovers; Ecstasy Aftershocks retaliates against the declared area; Overflow Engine converts Overflow through a player-configured output.
- Listener order is deterministic. Each listener declares an output cap and cannot recursively trigger itself. A global cross-listener chain-depth cap is required.
- One listener does not consume or suppress the event for other listeners unless its own definition explicitly says so.

## 5. Remaining production work (not unresolved semantic design)

The design/reconciliation section is closed. The following tasks remain for production and must not be mislabeled as open design decisions:

1. **Numeric balance:** coefficients, base powers, resource costs/yields, Skill Point costs, cooldowns, durations, resistance curves, caps, and rounding.
2. **Schema migration:** add stable IDs and normalized logical fields; remove nine blank placeholder rows; represent the Enslave/Absolute Control merge as one record with a presentation alias.
3. **Companion data:** author deterministic target queries, effect sequences, scaling profiles, requirements, Chain/Threshold/Overflow rules, capability dependencies, and presentation references.
4. **Validation:** schema checks for IDs, fields, references, tags, and formulas; encounter-level tests for multi-target resolution, partial finisher success, DoT timing, Overflow listeners, Chain reset, and P-growth gating.
5. **Balance QA:** test single-target, group, high-risk, support, control, recovery, and resource-loop builds. Verify Flirt cannot dominate both dedicated Command generation and dedicated Strain damage.
6. **Documentation synchronization:** after migration, update the implementation spec and project roadmap to distinguish design lock from implementation readiness.

## 6. Exit criteria

The **skill design section** is complete when this lock and Passes 1–7 are treated as the approved semantic baseline. The implementation catalog is complete only after the production work above is finished and validated. This distinction avoids claiming an unbalanced or untested CSV is production-ready.
