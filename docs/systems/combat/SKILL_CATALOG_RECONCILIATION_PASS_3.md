# AHTW — Skill Catalog Reconciliation, Pass 3: High-Impact Clusters

> Status: **THEMATIC/FUNCTIONAL REVIEW — PROPOSED, NOT YET FINAL CONTENT LOCK**. This pass interprets the legacy skills by their apparent fantasy, action represented, and intended player fantasy, then maps that intent onto the canonical combat system. It does not authorize deleting or rewriting CSV rows.

## 1. Review principle: preserve fantasy, not accidental implementation

The legacy catalog mixes three layers:
1. **Action fantasy:** what the player imagines Alya doing (tempt, distract, expose herself to danger, protect an ally, endure, retaliate, overwhelm, transform, finish).
2. **Tactical decision:** why the player chooses the skill now (manipulate intent, build a resource, mitigate, apply a state, exploit a threshold, request an outcome).
3. **Legacy effect wording:** old H-gauge/health terminology, mixed target fields, and bundled effects.

The action fantasy is worth preserving when it gives the game personality. It does not, by itself, justify a separate mechanical skill. Two differently themed actions should remain separate if their target, timing, resource loop, risk, Aspect, setup, or outcome creates a different decision. Conversely, two actions that only deal the same Strain damage to the same target with no distinct hook can share a mechanical definition and vary presentation.

All H-gauge references are mapped to Strain and Health Damage to Vitality damage, but each effect must be reconstructed semantically. The thematic labels below are descriptive candidates, not approved final names.

## 2. Cluster A — Intent manipulation, control, and ally protection

This is a high-impact cluster because it determines whether the player is controlling enemy choices, preparing control, or merely inflicting Strain. These should not collapse into a generic “control” action.

| Skill / candidate | Perceived fantasy and action | Recommended tactical identity | Disposition |
|---|---|---|---|
| Flirt | Entice an enemy through charm | Low-cost social/magical action that generates Command, or a modest Strain attack; choose one primary loop | **Conditional retain**: prefer Command generation if Hypnotize owns direct control |
| Hypnotize | Enchant the enemy's mind | Intent manipulation or a defined control state with resistance and duration | **Rework/retain**: no arbitrary bundle of stun + DoT + intent |
| Otherworldly Charm | Make an enemy prefer one kind of behavior/attack | Persistent or passive enemy-intent bias | **Retain** if its scope/duration differs from active Hypnotize |
| Bully | Intimidate and undermine an enemy | Lower offense and/or defense through a named debuff | **Retain**: physical/social intimidation is distinct from mind magic; choose explicit stat effects |
| Bind | Magically restrain the enemy | Apply a restraint state that limits a defined action or movement | **Rework**: state-based control, not generic H-damage |
| A-penetration | Forceful, capability-gated attack that stuns | Focused attack with a control rider or Break setup | **Conditional retain**: if its only result is stun, compare directly with Bind/Hypnotize and merge redundant mechanics |
| Break Resistance | Break down resistance | Setup: lower resistance or prepare Break; should not itself equal a full disable | **Retain as separate proposed addition** if Break is a real intermediate state |
| Command | Command-resource action | Explicitly decide whether this is a generator or a spender; don't let the same skill ambiguously do both | **Needs role selection**; not a second generic control status |
| Absolute Control | High-investment culmination of control | Spend resources and request an encounter-permitted outcome (Disable/Yield/Capture, as authored) | **Conditional retain**: distinct only as a costly outcome conversion, never a global victory command |
| Enslave | Force submission | Thematic finisher that requests a permitted encounter outcome under strict eligibility/resistance rules | **Rework**; compare against Absolute Control. Keep both only if one is Strain-threshold based and the other is Command/Break investment based |
| Worship C | Devotional/ritual action that influences enemy behavior | Area intent bias or vulnerability state | **Choose one primary function**; likely merge with Otherworldly Charm/Aphrodisiac if identical after mechanics are specified |

### Recommended separation
- **Charm/temptation**: Flirt = build Command; Otherworldly Charm = passive/ongoing intent bias.
- **Mind control**: Hypnotize = alter intent or apply a defined temporary mental state.
- **Physical intimidation**: Bully = named stat debuff.
- **Restraint**: Bind = restrict a declared action set.
- **Break setup**: Break Resistance = reduce resistance/prepare Break.
- **Outcome conversion**: Enslave or Absolute Control = request a permitted outcome, not a generic stun.

Do not keep all six as separate entries if their final effect data cannot support these differences.

## 3. Cluster B — Reactive defense, exposure, retaliation, and protection

The intended fantasy here is not just “defend.” The player may invite danger, redirect danger, endure it, or turn it back on the enemy. Those are different tactical identities.

| Skill / candidate | Perceived fantasy and action | Recommended tactical identity | Disposition |
|---|---|---|---|
| Get Spanked | Alya deliberately invites an enemy attack/exposure | Intentional-risk action; if the enemy resolves the declared trigger, gain Resolve or another bounded reactive benefit | **Retain/rework** as the risk-for-resource action |
| Provoke | Draw the enemy's attention | Change enemy intent/target preference toward a declared actor | **Retain**; it changes who is threatened, not how the threat is mitigated |
| Instill Protectiveness | Encourage an ally to protect someone / redirect aggression | Protection or target-priority effect; the legacy wording says it increases the chance allies are targeted, so resolve the intended beneficiary explicitly | **Rework**; do not implement the ambiguous wording literally |
| Dancing Moves | Dodge gracefully | Active evasion stance with a defined window and action cost | **Retain** as proactive avoidance |
| Endure | Take a hit and remain standing | Active mitigation plus Fortitude generation or a bounded survival benefit | **Retain** as defensive response, not passive reduction |
| Masochism | Become more effective while receiving/withstanding pain | BuildPassive that rewards Fortitude/exposure or grants a conditional defensive benefit | **Rework**; must have trigger/cap and must not duplicate Endure |
| Counter | Respond to an enemy's declared action | Reaction/counter-action after a qualifying trigger, with explicit timing and action budget | **Retain** if a reaction can be resolved deterministically |
| Moans | Turn incoming Strain into reflected Strain | Reflection passive: return a bounded portion of the qualifying incoming effect | **Conditional retain**; merge into Counter only if reflection offers no distinct build choice |
| Turn the Tables | Convert what just happened into a reversal | Consume a specific recent-event record to respond, recover, or retaliate | **Retain** if event-history conversion is materially different from a direct counter |
| Unbroken | Refuse a defeat or disabling event | One narrowly defined emergency prevention effect with cooldown/once-per-encounter constraints | **Conditional retain**; must not create general immunity |
| Divine Health | Exceptional resilience and recovery | Conditional resistance or a restricted cleanse, not blanket immunity to all debuffs | **Rework** as support/passive protection |
| S Symbol | Recover when Strain overflows | Recovery triggered by an Overflow event | **Retain** if it restores a distinct channel (choose Vitality, Strain reduction, or a specific cleanse) |
| Ecstasy Aftershocks | Overflow spills into an area reaction | Automatic, bounded area effect on a single Overflow event | **Retain** as reactive offensive build hook |
| Overflow Engine | Intentionally convert Overflow into a chosen result | Active/configurable conversion of an Overflow event into one declared output | **Retain as proposed addition** only if player choice differs from automatic reaction/recovery |

### Recommended reactive loop
1. **Provoke** determines who the enemy intends to attack.
2. **Dancing Moves** avoids an attack before it lands.
3. **Endure** reduces the consequences of an incoming hit and may generate Fortitude.
4. **Get Spanked** is a deliberate exposure choice that generates Resolve when its condition actually resolves.
5. **Counter** reacts to a defined event; **Moans** reflects; **Turn the Tables** uses event history. These remain separate only if their timing/output differs.
6. **Unbroken** is an emergency exception, not another mitigation layer.

Avoid stacking multiple passive “take less damage” effects without caps or diminishing returns. Reactive skills need a precise trigger window and deterministic ordering.

## 4. Cluster C — Strain application, damage-over-time, vulnerability, and finishers

This cluster is the greatest risk for duplicate actions because many legacy skills describe a thematic action but only specify “H-Damage.” Preserve distinct animations and thematic actions, but require a distinct tactical hook for a separate mechanical record.

| Skill / candidate | Perceived fantasy and action | Recommended tactical identity | Disposition |
|---|---|---|---|
| Sensory Enhancement | Heighten sensitivity/vulnerability | Apply a tagged vulnerability effect to a named channel (Strain or Vitality, or both only if explicitly justified) | **Rework**; compare with Exploit Weakness |
| Sensory Deprivation | Overwhelm or suppress senses | Debuff a named subset of accuracy/evasion/defense | **Retain**; multi-stat effect needs cost/duration justification |
| Bend | Prolonged single-target pressure | Baseline single-target Strain-over-time | **Retain** as the simplest DoT candidate |
| AS | Escalate pressure when repeated | Chain/sequence mechanic that rewards repeated use and defines reset conditions | **Conditional retain**; not merely a stronger Bend |
| Aphrodisiac | Sustain Strain and influence behavior | Applied state with explicit tick effect and/or intent bias | **Rework**; preserve both only if the combined state is coherent |
| Pink Mist | Spread prolonged pressure to many enemies | Area Strain-over-time plus one named defense debuff | **Retain** as the area DoT candidate |
| Flaunt | Draw attention and overwhelm the group | Area Strain action with an explicit target filter or rider | **Conditional retain** vs G-bang; no generic duplicate AoE |
| G-bang | Group-focused overwhelming action | Area Strain attack | **Merge candidate** with Flaunt if no different risk/targeting/rider exists |
| Summon C-S | Magical group-wide pressure that scales with target count | Summoned area action with declared scaling, target set, and friendly-fire policy | **Retain/rework** if the summon/scaling decision is unique |
| Summon Tentacles | Uncontrolled otherworldly force threatens everyone | High-risk area action affecting explicitly listed sides; retaliation/friendly fire is core to the fantasy | **Retain/rework** if the risk is real, bounded, and deterministic |
| Spank / Bite | Focused physical attacks using different Aspects | Basic focused attack candidates | **Conditional**: keep separately only if Aspect, trigger, cost, or state interaction matters |
| Bl-job / Lay / Grope / H-job / Paizuri / Deepth | Different intimate actions, but legacy data mostly gives the same Strain damage role | Shared baseline action family with distinct presentation/Aspect variants unless one has a unique tactical effect | **Consolidate mechanics first**; do not assume six separate skill records are justified by animation alone |
| Facesit | Smother the target with a clear self-positioning risk | Focused action with a self-exposure/positioning consequence only if mechanically real | **Conditional retain**; correct actor/target schema |
| Prolonged Pl- | Sustain pressure at a full Strain state and punish further actions | Threshold/Overflow interaction with a clear trigger and ordered Vitality-damage consequence | **Rework**; the legacy text both prevents Overflow and refers to a filled gauge—resolve the intended state machine |
| Stomp | Punish a highly strained target with Vitality damage | Threshold-based conversion from Strain state to Vitality damage | **Retain** if Strain level changes the action's role, not just its output number |
| Swallow | Finish a weakened target | Single-target threshold finisher that requests a permitted encounter outcome | **Retain/rework**; threshold must be explicit and encounter-defined |
| Bkakke | Attempt a group finisher and suffer a consequence if anyone survives | All-target threshold finisher with a clear survivor-risk clause | **Rework/conditional**; resolve each target deterministically and never directly force combat victory |
| Strip | Area pressure paired with evasive flair | AoE Strain plus evasion only if the combination creates a coherent risk/reward turn | **Conditional retain** vs Flaunt/G-bang; split or remove unrelated rider if not |
| F-fk | High-risk capability-gated action that becomes stronger against a weakened target | Capability-gated execute/Strain scaling with a bounded Vitality threshold | **Conditional retain**; declare whose Vitality is checked and cap the scaling |
| Penetrate | Capability-gated focused action | Focused Strain attack with a distinct capability fantasy | **Conditional** vs A-penetration; keep both only if the latter's control rider materially changes tactical role |
| Cuteness | Supportive appeal that boosts allies | Passive ally attack buff with defined scope and stacking | **Retain/rework**; compare with Encourage |
| Encourage | Directly inspire an ally | Active next-action buff | **Retain**; action vs passive distinction is meaningful if durations/economy differ |
| Service | Intimate support directed at an ally | Restore one explicitly named channel or remove a whitelisted effect | **Rework**; don't leave generic “heals ally” |
| C-drinker | Recover after an enemy is defeated using a certain action family | Event-triggered recovery passive | **Retain/rework** if the trigger rewards a build; exact recovery channel required |

### Proposed baseline attack policy
Create a small number of shared mechanical templates (e.g. Focused Strain Attack, Focused Vitality Attack, Single-Target DoT, Area Strain, Area DoT, Threshold Conversion, Finisher Request). Presentation/Aspect variants can reuse them. Promote a variant to a separate skill only if it changes a tactical decision, unlock, resource loop, risk, or effect.

This is not a command to delete the legacy action names; it is a recommendation to separate mechanical identity from presentation identity.

## 5. Cluster D — Capability, passives, and economy

| Skill | Perceived fantasy and action | Recommended tactical identity | Disposition |
|---|---|---|---|
| P-growth | Transform/gain a new capability that enables other actions | Capability/Transformation granting CAPABILITY_P_GROWTH | **Retain/reclassify**; target scope, persistence, acquisition, and removal remain unresolved |
| Autof | Use the gained capability for self-recovery and cleansing | Capability-gated recovery action; choose Vitality restoration, Strain reduction, and/or a limited cleanse explicitly | **Retain/rework** |
| Extra Tips | Earn better rewards after victory | Economy/reward passive triggered by a declared victory/reward event | **Move out of combat catalog** unless passives intentionally live there as a unified catalog |
| Piercing Stares | Equipment-specific pressure from piercings | Equipment-predicate passive applying a declared effect | **Retain/rework**; use equipment tags rather than hard-coded item IDs |
| Sadism | Gain offensive benefit from a particular playstyle/state | BuildPassive tied to Pressure/exploited states | **Retain/rework**; cap modifier and declare triggers |
| Naughty Thoughts | Mental focus increases accuracy/effectiveness of certain actions | BuildPassive restricted to explicit action tags and bounded modifiers | **Retain/rework** |
| Mstrbate | Self-directed recovery combined with influencing enemy behavior | Split candidate: self-recovery and enemy-intent manipulation are separate decisions unless a single risk/reward loop links them | **Rework**; don't keep the bundled effect merely because the theme is coherent |
| Divine Health | Protect allies from harmful effects while helping them recover | Conditional resistance or targeted cleanse support | **Rework**; avoid blanket debuff immunity |

## 6. High-impact disposition summary

### Strong candidates to retain as distinct mechanics
- Dancing Moves (proactive evasion)
- Hypnotize (intent/state control)
- Bully (named stat debuff)
- Bind (restraint state)
- Break Resistance (setup)
- Provoke (intent redirection)
- Get Spanked (deliberate exposure/Resolve)
- Endure (mitigation/Fortitude)
- Counter (triggered response)
- Turn the Tables (event-history conversion)
- Bend (baseline DoT)
- Pink Mist (area DoT)
- Summon Tentacles (explicit high-risk area action)
- Stomp (Strain-threshold Vitality conversion)
- Swallow (single-target outcome request)
- P-growth (capability)

“Strong candidate” does not mean final numbers or requirements are approved.

### Conditional/merge-review candidates
- Flirt vs Hypnotize
- Instill Protectiveness vs Provoke
- Moans vs Counter
- AS vs Bend
- Sensory Enhancement vs Exploit Weakness
- Aphrodisiac vs Otherworldly Charm/Worship C
- Flaunt vs G-bang vs Strip
- Spank/Bite and the mostly flavor-based single-target actions
- Penetrate vs A-penetration
- Enslave vs Absolute Control
- S Symbol vs Ecstasy Aftershocks vs Overflow Engine (retain only as distinct recovery/reactive/active conversion roles)
- Cuteness vs Encourage
- Mstrbate's recovery vs intent effect

### Rules to apply before migration
- No skill should directly force global combat victory.
- No finisher may bypass the encounter's outcome contract.
- Every reaction needs a deterministic trigger, trigger window, and action/resource budget.
- Every DoT needs tick timing, duration, refresh/stack rules, and expiry.
- Every debuff needs named affected stats/states and stacking policy.
- Every area skill needs a legal target set, target-count scaling, and friendly-fire rule.
- Every capability-gated skill needs a declarative capability requirement.
- Every passive needs a defined event hook or predicate and bounded output.
- Separate Strain and Vitality effects; “heal” must specify its channel.
- Keep thematic labels where useful, but don't equate every presentation animation with a unique mechanical skill.

## 7. Recommended review decisions for the next user pass

The highest-value decisions to close next are:
1. **Control/outcome:** should Enslave and Absolute Control be distinct via different resource loops (Strain threshold vs Command/Break investment), or should one be the sole top-tier control finisher?
2. **Basic intimate action family:** should baseline actions that differ only by animation/Aspect be separate unlockable skills, or be presentation variants of shared mechanics?
3. **AoE identity:** should Flaunt/G-bang/Strip become one base AoE family with variants, while Summon C-S and Summon Tentacles remain distinct due to scaling/risk?
4. **Overflow:** keep three roles (recovery, reactive AoE, active conversion) or reduce to two if active conversion cannot offer a meaningful choice?
5. **P-growth target scope:** self-only transformation, or a capability that can be granted to allies? The old CSV says Ally but the described fantasy is a transformation; this is not safe to infer.

No answers are assumed by this document. The concrete catalog remains unlocked until these questions are resolved.
