# AHTW — Skill Catalog Scaling Audit

> **Status:** Proposed content-lock audit for 54 named legacy skills and 14 proposed additions. This does not modify the CSV, approve numeric coefficients, or silently finalize conditional merges.

## 1. Approved design decision

The project owner confirmed that the body part used by a skill can influence effectiveness through attributes associated with that specific skill. Similar-looking actions may therefore remain separate when their scaling profile, target requirements, risks, triggers, resource loops, synergies, or progression choices produce meaningful build decisions.

This audit proposes per-skill attributes, canonical effects, synergies, and distinct identity. These are recommendations, not locked balance values. Exact coefficients, caps, durations, costs, and unlock requirements remain open.

## 2. Attribute vocabulary

The eight primary attributes are:

| Code | Attribute | Existing character-sheet roles |
|---|---|---|
| BODY | Body | Vitality/HP capacity, physical damage and physical damage resistance |
| AGI | Agility | Evasion, accuracy, initiative |
| SOUL | Soul | Magical attack, Strain resistance |
| CHARM | Charm | Strain damage/accuracy and likelihood of eliciting enemy Strain-oriented attacks |
| DOM | Dominance | Strain damage/accuracy and resistance to Strain-oriented attacks |
| SUB | Submission | Enemy Strain-oriented attack likelihood, Strain damage and buff empowerment |
| SAD | Sadism | Physical/Vitality damage and accuracy |
| MAS | Masochism | Strain resistance, physical damage resistance and debuff resistance |

Existing body-part multipliers/affinities on Alya's sheet are Ass, Breasts, Crotch, Mouth, and Mind. Treat these as a distinct per-skill scaling input, not extra primary attributes. Their exact formulas are not yet defined.

Each skill's scaling profile should declare: (1) primary and secondary attributes; (2) relevant body-part affinity; (3) whether the action is physical, magical, Strain-focused, Vitality-focused, support, or mixed; (4) contextual/target-state modifiers; and (5) any cap or safety rule. Attribute-to-body-part mapping is **per skill**, not universal. An Aspect tag or requirement alone does not define scaling.

Conceptually, effectiveness may combine declared attribute contribution, declared body-part affinity, and context modifiers. The implementation must use the project's canonical modifier pipeline; do not automatically multiply every term together. For All-body-part actions, explicitly choose a relevant affinity, a defined composite, or no part multiplier; never silently multiply every affinity together.

## 3. Legacy skill audit — 54 named entries

In each row, the first attributes are suggested leading contributors, not approved weights. Part refers to the existing body-part affinity. Effect and synergy are proposed identities; final values remain open.

### A. Control, charm, intent and mental pressure

| Skill | Suggested scaling | Proposed effect | Synergy / distinct identity |
|---|---|---|---|
| Sensory Enhancement | SOUL / CHARM; Mind | Apply a tagged vulnerability to a named channel: Strain, Vitality, or a specific action tag | Enables Exploit/Pressure and follow-up actions. Amplifies a named channel rather than generally weakening the enemy. |
| Flirt | CHARM / DOM; Mouth | Low-cost Command generator OR modest Strain attack; choose one primary role | Command supports Hypnotize/Break setup. Retain as the accessible control-resource generator if Hypnotize owns direct control. |
| Hypnotize | SOUL + DOM / CHARM; Mind | Change locked enemy intent or apply a defined mental-control state with resistance, eligibility and duration | Combines with Command/Break. Changes enemy options, unlike a damage-only action. |
| Sensory Deprivation | SOUL / DOM; Mind | Debuff named accuracy/evasion/defense stats with duration and stacking rules | Supports evasion/counter and risky follow-ups. Impairs performance rather than amplifying a damage channel. |
| Otherworldy Charm | CHARM / DOM; Mind or declared composite | Conditional/persistent bias toward eligible Strain-oriented actions and away from Vitality attacks | Supports Strain/exposure builds. Keep distinct from Hypnotize only if passive/persistent scope differs from active control. |
| Aphrodisiac | SOUL + CHARM / DOM; Mind | Strain-over-time OR enemy-intent modifier; combine only if a coherent state | Supports DoT or intent builds. Must differ from Otherworldly Charm and generic DoT by scope/trigger/state. |
| Bully | CHARM + SAD / DOM; Mouth | Intimidation debuff to named offensive stats, such as attack effectiveness and accuracy/defense | Sets up damage/control. Weakens capability rather than directly changing intent. |
| Worship C | SUB + CHARM / DOM; Breasts/Mouth | Area intent bias OR a named vulnerability/debuff; choose one primary effect | Supports group Strain strategy. Keep if area scope or ritual setup makes it distinct from Otherworldly Charm/Aphrodisiac. |

### B. Exposure, defense, reactions and protection

| Skill | Suggested scaling | Proposed effect | Synergy / distinct identity |
|---|---|---|---|
| Dancing moves | AGI / MAS; All/composite | Active evasion stance for a declared window and attack set | Pairs with Provoke and visible intent. Proactive avoidance, not mitigation after a hit. |
| Get Spanked | MAS + SUB / BODY; Ass | Deliberate exposure; when a qualifying incoming trigger resolves, generate Resolve or another bounded payoff | Builds Resolve for Counter/Turn the Tables. Risk-for-resource choice, not just intent redirection. |
| Instill protectiveness | SUB + CHARM / MAS; All/composite | Explicit ally protection, guard priority, or target redirection; name beneficiary and exposed actor | Synergy with Guard/interception and Provoke. Legacy wording is ambiguous and must not be copied literally. |
| Spank | BODY + SAD / AGI; Ass | Focused physical action with a declared Vitality/Strain profile | May trigger SAD passives and Ass affinity. Distinct from Bite only if scaling/effect/cost/trigger differs. |
| Bite | BODY + SAD / AGI; Mouth | Focused physical attack; optional secondary state only if supported by the effect system | Supports physical/SAD builds. Mouth affinity can distinguish it from Spank; otherwise share the base template. |
| Masochism | MAS / SUB; Ass/Breasts | BuildPassive giving bounded mitigation/Fortitude benefit under a qualifying exposure/damage trigger | Synergizes with Endure/Get Spanked. Must not duplicate active mitigation or create unlimited passive reduction. |
| Moans | MAS + SUB / CHARM; Mouth | Reflect a bounded portion of qualifying incoming Strain after the original event resolves | Exposure build synergy. Distinct from Counter if automatic reflection differs from an active response. |
| Bondage | MAS + SOUL / SUB; All/composite | Self-restraint stance trading a declared limitation for defense, resistance, or a bounded area effect | Defensive/HighRisk builds. Current wording lacks causal clarity; the trade-off must be real and deterministic. |

### C. Basic physical/Strain actions and sustained effects

| Skill | Suggested scaling | Proposed effect | Synergy / distinct identity |
|---|---|---|---|
| Mstrbate | MAS + CHARM / SOUL; Crotch | Split self-recovery from enemy-intent influence unless a coherent risk/reward loop joins them | Can support self-sustain or intent builds. Retain both effects only if the action creates a testable trade-off. |
| Bl-job | CHARM + SUB / SOUL; Mouth | Focused Strain action using a shared basic-action template | Mouth affinity and SUB/CHARM passives may distinguish it. Separate skill only if scaling, requirement, cost or synergy differs. |
| Lay | SUB + MAS / BODY; Crotch | Focused Strain action with a distinct risk/benefit profile | May support exposure/Resolve builds. Needs a mechanical reason beyond label/animation. |
| Grope | CHARM + AGI / SUB; Ass + Breasts | Focused Strain action; multiple-part scaling only if composite is defined | Supports evasive/teasing builds. Distinct if multi-part affinity or a secondary effect changes tactical use. |
| H-job | AGI + CHARM / SUB; legacy Mind tag needs validation | Focused Strain action; Mind interaction only if mechanically real | Possible accuracy/control synergy. Existing Mind Aspect conflicts with its description; confirm the intended body part. |
| Service | SOUL + SUB / CHARM; Mouth | Ally support restoring a named channel (Vitality or Strain reduction) OR removing a whitelisted effect | Recovery/team sustain. Distinct from buffs because it repairs an existing problem; “heal” must specify the operation. |
| Bend | SUB + MAS / CHARM; Ass | Baseline single-target Strain-over-time with explicit tick timing and duration | Establishes the basic DoT and enables vulnerability/Pressure follow-up. |
| AS | SUB + MAS / CHARM; Ass | Chain/sequence effect rewarding consecutive use, with explicit reset conditions | Distinct from Bend if sequence commitment changes decisions. If it only applies a stronger DoT, merge mechanics. |
| Paizuri | CHARM + SUB / BODY; Breasts | Focused Strain attack on shared basic-action template | Breast affinity/equipment/passive synergies may distinguish it. Identical scaling/effects/costs make it a presentation variant. |
| Deepth | SUB + MAS / CHARM; Mouth | Focused Strain action with a distinct risk, accuracy modifier, state interaction or threshold hook if justified | Supports MAS/SUB and Mouth affinity. Normalize its name; distinguish it from basic attacks mechanically. |
| Facesit | BODY + SUB / MAS; Crotch | Focused action affecting Vitality and/or Strain; if self-exposure is intended, define the incoming risk | Can trade self-risk for pressure or exploit a vulnerable target. Correct actor/target scope so Self is not an accidental damage target. |

### D. Area actions and high-risk effects

| Skill | Suggested scaling | Proposed effect | Synergy / distinct identity |
|---|---|---|---|
| Flaunt | CHARM + DOM / AGI; All/composite | Area Strain action with explicit target set and one distinctive rider/filter | Area pressure. Share mechanics with G-bang/Strip if only damage and presentation differ. |
| Summon c-s | SOUL + SUB / CHARM; Mind | Summoned area Strain effect whose per-target output increases as enemy count falls, with curve/floor/cap | Distinct summon that concentrates force against fewer targets. Define target set and friendly-fire policy. |
| Strip | AGI + CHARM / DOM; All/composite | Area Strain plus temporary evasion only if the combination creates a coherent trade-off | Supports tempo/evasion. Distinct from Flaunt/G-bang if the evasion window changes turn planning. |
| Pink mist | SOUL + DOM / CHARM; Mind | Area Strain-over-time plus one named defense debuff, with duration/ticks/stacking | Persistent area pressure and debuff synergy; distinct from direct AoE because value persists and may be cleansed/resisted. |
| Summon Tentacles | SOUL + DOM + MAS / SUB; Mind/All composite | HighRisk area action affecting explicitly declared sides, with deterministic friendly-fire risk and target-count scaling | Distinct from Summon c-s because risk to allies/self is central. Do not use vague “aggro everyone”; declare targets and consequences. |
| G-bang | SUB + CHARM / SOUL; All/composite | Area Strain attack with declared target set and scaling | Broad pressure. If no unique target rule, cost, risk, scaling or rider distinguishes it from Flaunt, share its template. |

### E. Threshold conversion and finishers

| Skill | Suggested scaling | Proposed effect | Synergy / distinct identity |
|---|---|---|---|
| Prolonged Pl- | DOM + SUB / SOUL; Crotch | Strain threshold/Overflow interaction; decide whether it prevents Overflow, locks a threshold, or converts follow-up attacks into Vitality damage | Threshold build synergy. Current wording is contradictory; choose one deterministic state transition. |
| F-fk | BODY + DOM / SAD; Crotch | P-growth-gated action scaling against target below a declared Vitality threshold, with cap and explicit target check | Capability + execute pressure. Distinct from Penetrate if low-Vitality scaling creates a tactical window, not just a larger number. |
| Penetrate | BODY + DOM / SAD; Crotch | P-growth-gated focused Strain attack | Baseline capability-gated action. Distinct from A-penetration if the latter's control/Break rider matters. |
| A-penetration | BODY + DOM / SAD; Crotch | P-growth-gated focused attack with control rider or Break setup, with resistance/duration | Supports Command/Break investment. Keep separate from Penetrate only if the rider changes the decision. |
| Stomp | BODY + SAD / DOM; Crotch | Convert target Strain at a declared threshold into Vitality damage, with cap and mitigation order | Strain setup becomes primary defeat progress. Distinct due to damage-channel conversion. |
| Swallow | SUB + MAS / CHARM; Mouth | Single-target finisher request at a declared Strain/state threshold; use encounter-permitted outcome | Uses threshold and resistance rules. Never unconditional instant victory. |
| Bkakke | SUB + MAS / SOUL; Mouth + Breasts composite | All-target finisher request resolved per target; survivors trigger a defined self-risk consequence | Distinct from Swallow through multi-target risk. Never directly ends combat; encounter outcome rules decide. |
| Enslave | DOM + SOUL / CHARM; Mind | Control/outcome request with eligibility, resistance, duration and a permitted result such as Yield/Disable/Capture when authored | Supports Command/Break. Keep with Absolute Control only if setup/resource loop or result differs materially. |

### F. Passives, Overflow, capability and team support

| Skill | Suggested scaling | Proposed effect | Synergy / distinct identity |
|---|---|---|---|
| S Symbol | MAS + SOUL / SUB; All/composite | Passive recovery on one defined Overflow event: choose Vitality recovery, Strain reduction or a specific cleanse | Overflow survival build. Must differ from Ecstasy Aftershocks offense and Overflow Engine active conversion. |
| Piercing Stares | CHARM + DOM / SOUL; Breasts | ConditionalPassive triggered by equipment carrying a registered piercing tag; apply declared Strain effect | Equipment-driven identity. Use equipment tags, never hard-coded item IDs. |
| Sadism | SAD / BODY; Crotch/Mouth as action profile requires | BuildPassive improving a named Vitality-damage/exploitation payoff under a qualifying trigger | Synergizes with Pressure/vulnerability and physical attacks. Bounded and conditional, not an uncapped global multiplier. |
| Encourage | CHARM + SUB / SOUL; legacy Ass tag needs validation | Active ally buff for a declared next action or short duration; name affected stat/channel | Ally burst/coordinated turns. Distinct from Cuteness if active timing/action cost differs from passive uptime. |
| Autof | BODY + MAS / SOUL; Breast/Crotch/Mouth per action profile | P-growth-gated self-recovery plus cleanse whitelist; specify Vitality, Strain and removable tags | Capability build. Distinct if the gate and multi-channel recovery create a real commitment. |
| P-growth | SOUL + BODY / DOM; Crotch + Mind as currently listed | Capability/Transformation granting CAPABILITY_P_GROWTH with declared target scope, persistence and revocation | Unlocks Autof/F-fk/Penetrate/A-penetration candidates. Target scope is unresolved; do not silently change Ally to Self. |
| Extra tips | CHARM + SOUL / AGI; legacy Mind tag needs validation | Reward/economy passive on a declared reward event, with cap and stacking policy | Supports economy/exploration, not a combat loop. Move to reward catalog unless passive skills share one unified catalog. |
| Cuteness | CHARM + SUB / SOUL; Breasts + Mouth | Passive ally attack modifier with explicit scope, stat/channel and stacking | Team buff builds. Distinct from Encourage if passive uptime versus active timing is meaningful. |
| Naughty Thoughts | CHARM + SOUL / DOM; Mind | BuildPassive improving named accuracy or Strain effect for explicit action tags, with cap | Mind/CHARM build synergy. Distinct from general damage if it rewards a defined action family. |
| C-drinker | SUB + MAS / CHARM; legacy Mind tag needs validation | On-defeat trigger restoring one declared channel when a qualifying enemy is defeated by a qualifying action | Strain-finisher sustain. Event must identify target, source actor and qualifying action/channel. |
| Ecstasy Aftershocks | SOUL + DOM / SUB; All/composite | ConditionalPassive area effect triggered by one resolved Overflow event, with recursion guard and bounded output | Overflow offense. Distinct from S Symbol recovery and Overflow Engine active conversion. |
| Divine Health | SOUL + MAS / SUB; Mind | Conditional team protection and/or restricted cleanse when a defined recovery action succeeds; no blanket immunity | Support/resilience. Distinct from Service if it conditionally protects/cleanses instead of directly restoring a channel. |

## 4. Fourteen proposed additions

These are candidates from the current audit, not rows currently present in the CSV.

| Candidate | Suggested scaling | Proposed effect | Synergy / distinct identity |
|---|---|---|---|
| SKILL_PROVOKE — Provoke | CHARM + DOM / SUB | Change enemy intent/target preference toward a declared actor for a bounded window | Enables Guard/interception, Dancing Moves and Endure. Redirects threat without inherently rewarding self-exposure. |
| SKILL_ENDURE — Endure | BODY + MAS / SUB | Active mitigation against a declared incoming event; may generate capped Fortitude | Distinct from Masochism because it spends an action and responds to a known threat. |
| SKILL_COUNTER — Counter | AGI + SAD / MAS | Reaction after a qualifying enemy action, with deterministic trigger window and action budget | Distinct from automatic Moans reflection and event-history Turn the Tables. |
| SKILL_COMMAND — Command | DOM + CHARM / SOUL | Explicitly choose generator or spender role; never leave resource function ambiguous | Supports Hypnotize, Break Resistance and Absolute Control without duplicating direct control. |
| SKILL_RECOVER_COMPOSURE — Recover Composure | SOUL + MAS / CHARM | Recover Strain or remove a narrow whitelist of effects; choose a primary operation | Recovery after pressure/control. Distinct from Autof if it lacks P-growth gate and has a different profile. |
| SKILL_EXPLOIT_WEAKNESS — Exploit Weakness | AGI + SAD / SOUL | Exploit a named vulnerability/unstable state for a conditional payoff and/or generate Pressure | Distinct from Sensory Enhancement: exploit an existing opening rather than applying it. |
| SKILL_BREAK_RESISTANCE — Break Resistance | DOM + SOUL / CHARM | Lower a named resistance or add Break progress; does not itself equal disable | Sets up Hypnotize, Bind and outcome requests. Setup role, not the finisher. |
| SKILL_TURN_THE_TABLES — Turn the Tables | AGI + MAS / SAD | Consume a specific recent event to recover, retaliate or reverse a state | Uses event history/resource conversion, unlike an immediate direct counter. |
| SKILL_FOCUS_SURGE — Focus Surge | SOUL + CHARM / DOM | Temporary focus buff to a named action channel, with duration/cost | Setup turns and caster builds. Distinct from Naughty Thoughts if active commitment differs from passive tag bonus. |
| SKILL_DIRECT_ALLY — Direct Ally | CHARM + DOM / SOUL | Improve ally's next action or grant a tactical action only if action-economy rules permit | Coordinated team turns. Distinct from Encourage if it changes action opportunity/targeting, not just buff magnitude. |
| SKILL_ABSOLUTE_CONTROL — Absolute Control | DOM + SOUL / CHARM | High-investment Command/Break conversion into a permitted outcome request with strict eligibility/resistance | Distinct from Enslave only if setup/resource investment or outcome semantics materially differ. |
| SKILL_UNBROKEN — Unbroken | BODY + MAS / SAD | Prevent one narrowly defined defeat/disable event, with strict cooldown/once-per-encounter limit | Emergency exception after mitigation fails, not ordinary damage reduction. |
| SKILL_OVERFLOW_ENGINE — Overflow Engine | SOUL + DOM / MAS | Active/configurable conversion of a resolved Overflow event into one declared output, with recursion/output caps | Distinct from automatic recovery or reactive damage only if player choice matters. |
| SKILL_MUTUAL_RUIN — Mutual Ruin | BODY + SAD + MAS / DOM | HighRisk exchange of a declared self-cost for a bounded substantial target effect | Synergizes with Resolve, Fortitude and Unbroken. Retain only if risk/payoff creates a real decision; never bypass encounter outcomes. |

## 5. Cross-skill synergy map

| Build pattern | Core pieces | Tactical identity |
|---|---|---|
| Command → Break → Outcome | Flirt or Command → Break Resistance → Hypnotize/Enslave/Absolute Control | Invest actions/resources to shape intent, lower resistance, then request a legal outcome. |
| Exposure → Resolve → Reaction | Get Spanked → Resolve → Counter/Turn the Tables; Endure/Masochism for survival | Accept or mitigate known risk to gain a reactive advantage. |
| Evasion and threat control | Provoke → Dancing Moves → Counter | Choose who is threatened, evade the declared attack, punish a qualifying action. |
| Vulnerability → Exploit → Conversion | Sensory Enhancement → Exploit Weakness/Pressure → Stomp or finisher | Create an opening, exploit it, convert Strain into Vitality progress or a permitted outcome. |
| DoT/area pressure | Bend/AS/Pink Mist → vulnerability/debuff → threshold action | Persistent pressure while preparing a threshold payoff. |
| Overflow | Strain buildup → Overflow → S Symbol or Ecstasy Aftershocks or Overflow Engine | Build around recovery, automatic retaliation, or deliberate conversion. |
| Capability specialization | P-growth → Autof/Penetrate/A-penetration/F-fk candidates | Capability changes the available action space. |
| Active/passive team support | Encourage/Direct Ally vs Cuteness/Divine Health | Choose active timing/control or passive-slot investment. |
| Body-part affinity specialization | Distinct scaling profiles plus relevant equipment/passive tags | Similar effects remain separate when their attributes/affinities support different builds. |

## 6. Decisions still open

1. Enslave vs Absolute Control: keep both only if Strain-threshold/state conversion and Command/Break investment create different setup loops or outcomes.
2. Basic action family: keep separate unlockable skills when scaling, requirements, costs, risk, hooks or synergies differ; otherwise use presentation variants over shared effects.
3. AoE: Flaunt/G-bang/Strip may share a template; Summon c-s and Summon Tentacles can differ through target-count scaling and friendly-fire risk.
4. Overflow: recovery, reactive AoE and active conversion should remain separate only if they create different player choices.
5. P-growth target scope, persistence and revocation remain unresolved.
6. The exact relationship between body-part multipliers and attribute contributions remains open; this audit proposes candidates, not formulas.
7. H-job, Encourage, Extra tips and C-drinker have legacy Aspect/part fields that require validation against the intended action.

## 7. Required production pass

Every retained record needs stable ID, display name, kind, tier, cost, requirements, target query, scaling_ref, resource costs/generation, ordered effects/conditions, durations/tick/stack/expiry rules, cooldown, Chain/Threshold/Overflow references, encounter-outcome interactions, presentation reference, and an acceptance test.

**No numeric coefficients are approved here.** Balance should begin after scaling profiles, effect semantics and overlap decisions are explicit.
