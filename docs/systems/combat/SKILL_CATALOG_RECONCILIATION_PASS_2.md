# AHTW — Skill Catalog Reconciliation, Pass 2

> Status: **PROPOSED MECHANICAL DISPOSITION — REVIEW REQUIRED**. Pass 2 applies the three newly approved decisions to every legacy row and the fourteen proposed additions. It is more concrete than Pass 1, but it does not authorize deletion or migration of the CSV yet.

## 1. Decisions now locked

1. **Meter migration:** legacy `H-gauge` maps to canonical `Strain`; legacy `Health Damage` maps to damage to `Vitality`. This is a terminology migration rule, not proof that every old effect was described correctly. Validate each skill's actual trigger, target, direction, scaling, and outcome semantics before converting its effect.
2. **P-growth:** model as a `Capability/Transformation` definition that grants a stable capability tag and enables dependent skills. Do not treat it as a temporary generic buff unless a separate, explicit temporary mode is designed. Persistence, removal, target eligibility, and unlock behavior must be declared.
3. **Consolidation:** review by functional cluster. Merge only where the player decision and mechanical result are genuinely redundant; preserve thematic skills when targeting, timing, resource loop, risk, Aspect, or outcome differs in a meaningful way.

## 2. Migration contract for legacy meters

| Legacy wording | Canonical interpretation | Required validation before migration |
|---|---|---|
| H-gauge / H-damage | Strain meter / Strain damage | Determine whether the old value is a meter change, damage-over-time, threshold check, resistance modifier, or trigger. Normalize to the corresponding structured effect, not just a renamed string. |
| Health Damage | Damage to Vitality | Confirm damage timing, mitigation, scaling, target, and whether it is direct damage or an outcome effect. |
| H-gauge overfills / overfill | Strain reaches/exceeds its defined limit and triggers Overflow | Use the canonical Overflow event/contract. Define once-per-event vs repeated triggers, caps, and ordering. |
| H-gauge threshold | Strain Threshold condition | Reference a named threshold predicate; avoid hard-coded prose-only comparisons. |
| Stun / paralysis / forced submission | Not a meter alias | Reconcile as a state, effect, or encounter outcome with eligibility, resistance, duration, and removal rules. |
| Heal | Restore Vitality, reduce Strain, or remove effects—these are separate operations | Each healing skill must name its exact output; never infer that “heal” means all three. |

**Important:** the two meter mappings are canonical vocabulary only. They do not imply that all H-damage should be copied into Strain damage unchanged. The old descriptions may combine meter damage, Vitality damage, states, or outcome behavior; split them into ordered structured effects when needed.

## 3. Capability/Transformation contract for P-growth

Proposed record: `SKILL_P_GROWTH`, kind `Capability` or registered `CapabilityTransformation` kind, with a stable granted capability such as `CAPABILITY_P_GROWTH`.

- Acquisition: a learnable/unlockable capability with Tier 2 expectation, subject to normal Skill Point, prerequisite, and progression-gate rules.
- Effect: grant the capability and make dependent skills eligible; it should not also deal damage, heal, or apply an unrelated temporary combat buff.
- Dependencies: Autof, F-fk, Penetrate, and A-penetration must reference the capability in declarative requirements. Add further dependencies only if the catalog confirms them.
- Persistence/removal: define whether it is permanent after acquisition, removable by a specific narrative/gameplay event, or mutually exclusive with another capability. Do not let ordinary dispel/cleanse remove it by default.
- Targeting: resolve whether the capability is self-only, character configuration, or can be granted to an ally; the legacy row says Ally, so this remains an explicit content question rather than silently assuming Self.
- Safety/consistency: capability grants must be deterministic and save/load persistent if permanent; presentation can remain thematic while the runtime identifier is neutral.

## 4. Pass 2 matrix — 54 named legacy rows

Disposition meanings: **Retain** = keep as a distinct candidate; **Rework** = preserve intent but change/clarify mechanics; **Conditional** = keep only if playtest shows a distinct decision; **Merge candidate** = compare directly with named cluster members before deciding; **Move** = belongs primarily outside ordinary combat resolution. These are proposed dispositions, not final removals.

| Legacy entry | Proposed Pass 2 disposition | Canonical mechanical intent | Decision / acceptance test |
|---|---|---|---|
| Sensory Enhancement | Rework | Apply a tagged vulnerability effect that increases a declared Strain or Vitality channel | Must state which channel(s), magnitude, duration, stack policy, and eligible targets; compare with Exploit Weakness. |
| Mstrbate | Rework / rename | Self-recovery with a deliberate-risk or enemy-intent component only if they form one coherent choice | Split into separate skills if recovery and intent manipulation have independent value; normalize display name without making the theme the ID. |
| Dancing moves | Retain | Active evasion/defensive stance | Define duration, evasion/accuracy interaction, stacking, and whether using it consumes the normal action. |
| Flirt | Conditional | Generate Command **or** deal focused Strain; choose one primary loop | Retain separately from Hypnotize only if it has a distinct resource/action-economy role. |
| Hypnotize | Rework | Change enemy intent or apply a defined control state | Do not bundle stun, Strain damage-over-time, and intent control without explicit separate effects; specify resistance and duration. |
| Get Spanked | Rework / merge candidate | Voluntary exposure that generates Resolve when the declared incoming-event trigger occurs | Differentiate from Provoke by who controls target intent and what resource/reward is generated. |
| Sensory Deprivation | Retain / normalize | Debuff one or more declared combat stats, likely accuracy/evasion/defense | Exact stat list, duration, and stacking must be explicit; do not treat as generic “weaken.” |
| Spank | Conditional retain | Focused physical action with a specific Aspect interaction | Keep if its damage, trigger, or tag interactions differ from other basic single-target attacks; migrate H-damage to Strain damage and Health Damage to Vitality damage after checking semantics. |
| Instill protectiveness | Rework / merge candidate | Redirect or alter enemy targeting to protect a chosen ally | Target priority must be an explicit intent/AI effect; compare against Provoke and do not silently invert target selection. |
| Bl-job | Conditional | Focused single-target Strain action with a unique Aspect/tactical interaction | Keep only if it creates a different decision from Lay, Grope, H-job, Paizuri, and other baseline actions. |
| Lay | Conditional | Focused single-target Strain action | Same acceptance test: distinct target query, cost, setup, risk, or secondary effect—not just a different animation. |
| Grope | Conditional / merge candidate | Multi-Aspect or utility action | If only a second flavor of Strain damage, merge into a configurable presentation/Aspect variant; preserve separately only with a real mechanical distinction. |
| Service | Rework | Ally support that restores exactly one declared channel or removes a specified effect | Select Vitality recovery, Strain reduction, or cleanse; no vague combined “healing.” |
| H-job | Conditional | Focused action with a possible Mind Aspect interaction | Retain only if its Mind targeting changes eligibility, defense, effect, or resource loop. |
| Bend | Merge candidate | Basic single-target Strain damage-over-time application | Compare against AS; likely baseline DoT if AS retains a Chain mechanic. Define tick timing, duration, stacking, and refresh rules. |
| AS | Rework / merge candidate | Repeated-use Chain or escalating vulnerability | Retain alongside Bend only if the repeated-use condition has a clear reset rule and changes player decisions, not merely damage text. |
| S Symbol | Rework | Recovery triggered by Overflow | Declare whether it restores Vitality, reduces Strain, grants a resource, or cleanses; distinguish from Ecstasy Aftershocks and Overflow Engine. |
| Otherworldy Charm | Retain / normalize | Alter enemy intent or preference for attack channel | Define AI intent semantics, scope, duration, and conflict resolution with other intent effects; fix display spelling. |
| Piercing Stares | Retain / normalize | Conditional passive triggered by an equipment tag | Data-driven equipment predicate; specify whether output is Strain damage, a debuff, or both, plus tick timing/caps. |
| Sadism | Rework | BuildPassive that improves payoff against a declared exploited state or Pressure loop | No uncapped global Vitality damage multiplier; require a tagged trigger and bounded modifier. |
| Masochism | Rework | BuildPassive that interacts with Fortitude, exposure, or mitigation | Must not be a flat always-on reduction that makes Endure irrelevant; define trigger and cap. |
| Moans | Merge candidate | Reactive reflection of a portion of a declared incoming Strain effect | Compare with Counter and Turn the Tables; retain only if reflection (rather than attack/response conversion) is a distinct tactical choice. |
| Encourage | Retain / normalize | Improve an ally's next eligible action | Define effect, eligible action, expiration, refresh/stack behavior, and whether it can target self. |
| Flaunt | Conditional | Area Strain action with a distinct target filter or secondary effect | Compare with G-bang, Pink Mist, and Summon Tentacles; do not keep three interchangeable AoE attacks. |
| Autof | Rework | Capability-gated recovery/cleanse action | Requires CAPABILITY_P_GROWTH; specify exact recovery channel and cleanse whitelist. |
| Aphrodisiac | Rework / conditional | Strain-over-time and/or enemy-intent change | Keep both only if one coherent applied state justifies both; define separate ordered effects and duration. Compare against Bend/AS/Pink Mist. |
| P-growth | Reclassify; retain as Capability/Transformation candidate | Grant CAPABILITY_P_GROWTH and unlock dependent skills | Confirm target scope, persistence, acquisition gate, and removal policy. Not a temporary generic buff. |
| Facesit | Conditional | High-risk single-target action, potentially with explicit self-exposure | Resolve Enemy + Self targeting into a clear actor/target rule; retain only if self-risk is mechanically real and testable. |
| Bondage | Rework | Short defensive/control state with a clearly defined affected actor | Current description says self-binding while row targets Enemy and Self. Correct target schema, effect, duration, and removal trigger before retaining. |
| Bully | Retain / normalize | Debuff enemy offensive stats or declared intent | Choose whether it modifies stats, intent, or both; one canonical record may carry multiple family tags but must not be duplicated. |
| Bite | Conditional retain | Focused physical attack with a distinct conditional or Aspect interaction | Compare against Spank and other baseline attacks; if identical, consolidate mechanics and keep separate presentation only. |
| Bind | Rework / conditional | Restraint/disable state | Specify resistance, duration, removal, and eligible targets. Distinguish from Hypnotize's intent manipulation and BreakResistance's setup. |
| Prolonged Pl- | Rework / rename | Strain/Overflow interaction that triggers a defined Vitality-damage response under a threshold/state | Reconstruct as ordered effects using canonical Strain and Overflow; state whether it prevents Overflow or reacts to it and avoid contradictory triggers. |
| F-fk | Conditional | Capability-gated high-risk attack with low-Vitality scaling | Requires CAPABILITY_P_GROWTH; define whose Vitality drives scaling, cap the multiplier, and preserve counterplay. |
| Paizuri | Conditional | Focused single-target Strain action | Retain only if Aspect/targeting or an additional effect changes tactics relative to other basic actions. |
| Summon c-s | Rework / rename | Summoned multi-target Strain action with enemy-count scaling | Normalize the truncated display label; specify legal targets, target-count formula, friendly fire, minimum/maximum output, and deterministic ordering. |
| Swallow | Rework | Single-target Strain-threshold finisher that requests a configured encounter outcome | Use a named Threshold predicate and shared outcome system; never set global combat victory directly. |
| Extra tips | Move / conditional passive | Reward/economy modifier on a declared victory/reward event | Prefer economy/progression data over combat effects. Keep in skill catalog only if it is an intentionally learnable passive with a stable reward hook. |
| Cuteness | Rework | Ally buff | Name the stat/effect, scope, duration, stack policy, and source; ensure it differs from Encourage. |
| Naughty Thoughts | Rework | BuildPassive modifying a defined accuracy or Strain interaction | Replace vague “accuracy and damage” with exact affected action tags, modifier cap, and stacking rule. |
| C-drinker | Rework | Recovery on a precisely defined defeat event | Specify who defeated the target, which outcome counts, whether it triggers once per encounter/event, and whether it restores Vitality or reduces Strain. |
| Strip | Rework / conditional | Area Strain action with a self-evasion rider, if both are intentionally linked | Test whether AoE damage + self-evasion is one coherent action. If the rider is unrelated, split or remove it; define valid targets and duration. |
| Pink mist | Retain / normalize | Area Strain-over-time plus a declared defense debuff | Define target filter, tick timing, duration, stack/refresh policy, and defense stat; compare with Flaunt/G-bang. |
| Penetrate | Conditional retain | Capability-gated focused attack | Requires CAPABILITY_P_GROWTH; define whether it is a baseline Strain attack, Vitality attack, or a distinct interaction. Compare directly with A-penetration. |
| A-penetration | Rework / conditional | Capability-gated control/Break setup attack | If retained against Penetrate, its disable must use standard state/resistance/outcome rules and have a distinct cost/role. |
| Stomp | Retain / normalize | Conditional Vitality damage based on a Strain Threshold | Use a named threshold predicate; define whether Strain is checked before or after this action and how mitigation applies. |
| Summon Tentacles | Rework | HighRisk area action with explicit friendly-fire/retaliation contract | Define all affected sides, action order, target-count scaling, risk mitigation, and encounter safety; compare with other AoE options. |
| Enslave | Rework / conditional | High-cost control that may request Disable, Yield, or Capture where encounter rules permit | No permanent global control state. Define eligibility, resistance, duration/outcome, and encounter-specific exclusions. Compare with Absolute Control. |
| G-bang | Conditional / merge candidate | Area Strain action | Compare with Flaunt, Pink Mist, and Summon Tentacles; retain only if target filter, cost, risk, or secondary effect is meaningfully distinct. |
| Bkakke | Rework / conditional | All-target Strain-threshold finisher with a risk on survivors | Use per-target Threshold checks and shared outcome contract; define survivor consequence, ordering, and whether the user takes Strain damage or another explicit effect. |
| Deepth | Rework / rename | Focused single-target Strain action, if distinct | Normalize truncated label; preserve only with a distinct trigger, cost, Aspect, Chain, or effect. |
| Worship C | Conditional | Area intent modifier or Strain-vulnerability effect | Choose primary role; if it increases H-attacks/Strain intake, express that as canonical intent/state mechanics and compare with Aphrodisiac/Otherworldly Charm. |
| Ecstasy Aftershocks | Retain / normalize | Reactive area effect on the actor's Overflow event | Define one trigger per Overflow event, target filter, Strain/Vitality output, caps, and interaction with recursive Overflow. |
| Divine Health | Rework | Conditional resistance or capped cleanse support | Replace blanket debuff immunity with explicit resistance/conditional cleanse unless a narrow immunity is intentionally encounter-safe; define whether healing removes one/all eligible effects. |

## 5. Pass 2 matrix — fourteen approved additions

These additions remain candidates until their relationship to the legacy rows is resolved. A proposed new skill must not duplicate a legacy effect that can be retained with a stable ID.

| Proposed ID | Proposed role after Pass 2 | Direct comparisons | Proposed disposition |
|---|---|---|---|
| `SKILL_PROVOKE` | Manipulate enemy intent toward a chosen target/self | Get Spanked; Instill protectiveness | Retain if intent redirection is explicit and distinct from Resolve-generating exposure. |
| `SKILL_ENDURE` | Active mitigation plus Fortitude generation | Masochism; Unbroken | Retain as a timed reactive/defensive action, not passive blanket reduction. |
| `SKILL_COUNTER` | Reaction to a declared incoming action/trigger | Moans; Turn the Tables | Retain if it resolves a direct counter-action, not reflection or event conversion. |
| `SKILL_COMMAND` | Generate or spend the Command resource according to a single declared role | Flirt; BreakResistance; AbsoluteControl | Retain only after deciding whether this is the resource generator or a resource-spend action; avoid a skill that arbitrarily does both. |
| `SKILL_RECOVER_COMPOSURE` | Reduce Strain and/or clear a defined effect | Service; S Symbol; Divine Health | Retain if it offers a clear combat recovery role distinct from ally support and Overflow recovery. |
| `SKILL_EXPLOIT_WEAKNESS` | Consume a tagged weakness for increased payoff and/or Pressure | Sensory Enhancement; Sadism; Aphrodisiac | Retain as a generic exploit primitive only if the specific target-state/tag contract is reusable and not already covered. |
| `SKILL_BREAK_RESISTANCE` | Lower resistance/prepare Break | Hypnotize; Bind; A-penetration; Enslave | Retain as setup rather than a generic disable or outcome. |
| `SKILL_TURN_THE_TABLES` | Convert a defined recent event into a response | Counter; Moans; Get Spanked | Retain if event-history conversion is the distinct mechanic and has a bounded event window. |
| `SKILL_FOCUS_SURGE` | Self-focused temporary boost or resource conversion | Naughty Thoughts; Mstrbate | Retain only after choosing one precise output and duration. |
| `SKILL_DIRECT_ALLY` | Change an ally's next action/target or grant a budgeted action | Encourage; Command | Retain if action selection/commanding differs from a simple next-action buff; never bypass action economy. |
| `SKILL_ABSOLUTE_CONTROL` | Spend substantial control resources to request a permitted encounter outcome | Enslave; Swallow/Bkakke | Retain only if resource conversion and eligibility differ from ordinary finisher thresholds. |
| `SKILL_UNBROKEN` | Prevent one defined defeat/disable event under bounded conditions | Endure; Divine Health | Retain as a rare emergency exception with strict trigger/cooldown/cap; not general immunity. |
| `SKILL_OVERFLOW_ENGINE` | Deliberate conversion of Overflow into one configured output | S Symbol; Ecstasy Aftershocks | Retain if player choice/configuration differs from passive recovery and automatic reaction. |
| `SKILL_MUTUAL_RUIN` | High-risk exchange with explicit consequences on both sides | Summon Tentacles; Bkakke | Retain only if both-side risk is essential to the decision and encounter rules can resolve it deterministically. |

## 6. Proposed cluster decisions

These are recommendations for the next review, not final deletion orders.

### A. Reactive defense and intent
- Keep the concepts separate only if each has a different timing/choice: **Provoke** changes intent; **Get Spanked** invites exposure for Resolve; **Instill protectiveness** redirects protection toward an ally; **Endure** mitigates; **Counter** responds after a trigger; **Moans** reflects; **Turn the Tables** converts recent event history; **Unbroken** prevents one defined defeat condition.
- **Merge candidate:** Moans into Counter if testing shows reflection does not create a distinct build or decision. Do not merge merely because both react to incoming damage.

### B. Control and outcome
- Keep **Command**, **BreakResistance**, and **AbsoluteControl** as separate stages only if their roles are resource/intent management → resistance/Break setup → permitted encounter outcome.
- **Hypnotize**, **Bind**, **A-penetration**, and **Enslave** need distinct roles: intent change, restraint, capability-gated control/setup, and outcome request. Otherwise merge redundant control effects.
- A finisher can request an outcome but cannot independently end the encounter.

### C. Strain, damage-over-time, and vulnerability
- **Bend** is the baseline single-target Strain-over-time candidate; **AS** survives only if its Chain is a genuinely different repeat-use decision.
- **Aphrodisiac** should not carry unrelated damage-over-time and intent changes unless both are one defined state.
- **Pink mist** is the area-over-time candidate; **Flaunt/G-bang** should not remain as duplicate area Strain actions without distinct targeting, risk, cost, or rider.
- **Sensory Enhancement** and **Exploit Weakness** must differ: a persistent vulnerability modifier versus a tagged exploit/Pressure payoff, or one should be consolidated.

### D. Overflow
- **S Symbol** = recovery on Overflow; **Ecstasy Aftershocks** = automatic reactive area output; **Overflow Engine** = deliberate/configured conversion. Each needs a different output and a recursion/cap rule.
- Every effect must declare whether it triggers on entering Overflow, while in Overflow, or once per Overflow event.

### E. Capability and passives
- **P-growth** is a capability/transformation; dependent skills reference its stable tag rather than duplicate narrative conditions.
- **Sadism** and **Masochism** are build passives tied to Pressure/Fortitude loops, not global damage modifiers.
- **Extra tips** is likely economy/reward progression content; **Divine Health** is bounded protection/cleanse, not universal immunity.
- Equipment-linked passives such as **Piercing Stares** must use data-driven predicates.

## 7. Cross-cutting validation checklist before CSV migration

- [ ] Replace H-gauge references with Strain only after effect-by-effect semantic validation.
- [ ] Replace Health Damage with Vitality damage only after checking timing, mitigation, scaling, and outcome interactions.
- [ ] Normalize all Overflow triggers to the shared event contract; prevent accidental recursive triggers.
- [ ] Resolve every legacy row's actor, target set, and target-side inclusion; do not infer Self/Ally/Enemy from prose.
- [ ] Every active skill has explicit action cost, resource costs/generation, requirements, target query, effects, duration/tick rules, and cooldown/chain/threshold/overflow references as applicable.
- [ ] Every passive declares event hooks, scope, stack policy, and whether it is equipment-/capability-/state-gated.
- [ ] Every Capability/Transformation defines granted tag, persistence, removal, target scope, and dependent skill references.
- [ ] All finishers use encounter outcomes; all defeat-prevention effects specify exclusions and caps.
- [ ] Review AoE target counts, friendly fire, and scaling bounds.
- [ ] Compare all conditional/merge candidates in a playable vertical slice before removing thematic identities.
- [ ] Remove the nine unnamed placeholder rows during the actual CSV migration; do not count them as skills.
- [ ] Add stable IDs and structured references only after candidate dispositions are approved.

## 8. Suggested next review sequence

1. Confirm the cluster-level distinctions in section 6 (especially reactive defense, control, and Overflow).
2. Review conditional/merge candidates for single-target and area attacks.
3. Review passive/capability/reward skills.
4. Resolve actor/target and effect semantics.
5. Set tier, Skill Point cost, prerequisites, milestone gates, and numerical tuning.
6. Perform the CSV migration, schema validation, and targeted playtest.

**Current verdict:** skill architecture and meter/capability migration policy are closed; the concrete catalog remains unlocked. This pass narrows the proposed mechanics but does not yet authorize a bulk CSV rewrite.
