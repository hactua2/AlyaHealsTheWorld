# AHTW — Skill Catalog Reconciliation, Pass 1

> First-pass recommendations for review. This document does not silently delete legacy content or assert that proposed changes are already implemented. Final dispositions must be approved before the CSV migration.

## 1. Inventory correction

A fresh line-level check of `data/skills/skills.csv` found **54 named legacy skill rows** and **9 unnamed placeholder rows**. The prior planning estimate of 53 named rows was off by one; this correction supersedes the earlier estimate. Adding the 14 approved candidates gives **68 theoretical entries before reconciliation**, not 67.

The placeholder rows are not skills and should be removed during the actual CSV migration. Do not delete or rewrite legacy records until their dispositions are reviewed.

## 2. Legacy row-by-row recommendations

Disposition vocabulary:
- **Keep / normalize:** distinct role appears worth preserving; clean name/ID and specify mechanics.
- **Rework:** preserve the fantasy/intention but replace ambiguous text with canonical mechanics.
- **Conditional:** retain only if testing shows a distinct choice.
- **Merge candidate:** likely redundant with another skill; preserve useful identity through tags, presentation, or a distinct effect.
- **Move out of combat skill catalog:** effect primarily belongs to economy/reward/progression or a capability definition rather than an ordinary combat action.

| Legacy display name | First-pass disposition | Intended distinct role / audit question |
|---|---|---|
| Sensory Enhancement | Rework | Target vulnerability amplifier. Specify whether it modifies Strain, Vitality, or both and use a tagged effect. |
| Mstrbate | Rework / rename | Self-recovery plus deliberate risk is too broad as written. Separate recovery from enemy-behavior manipulation if both are retained. Normalize the typo in presentation. |
| Dancing moves | Keep / normalize | Active evasion or defensive stance. Define duration, whether it affects intent/accuracy, and its action opportunity cost. |
| Flirt | Conditional | Could be a low-cost Command generator or a direct Strain attack; choose a primary role to avoid overlapping Hypnotize. |
| Hypnotize | Rework | Intent manipulation or a defined disable with resistance/eligibility rules; “stun plus damage-over-time” currently combines unrelated effects. |
| Get Spanked | Rework / merge candidate | Reactive exposure skill that generates Resolve after a declared trigger. Differentiate from Provoke by trigger and reward. |
| Sensory Deprivation | Keep / normalize | Accuracy/evasion or perception debuff; specify affected stats and effect duration. |
| Spank | Keep / normalize | Focused physical attack with its own Aspect tag and damage profile; avoid relying on body-part prose alone. |
| Instill protectiveness | Rework / merge candidate | Ally protection or intent redirection. Compare with Provoke and avoid hidden target-priority manipulation. |
| Bl-job | Conditional | Legacy action with a distinct Aspect identity only if it offers a meaningful tactical effect beyond a generic Strain attack. |
| Lay | Conditional | Same audit standard: preserve if its targeting, cost, risk, or effect creates a different decision. |
| Grope | Conditional | Consider merging into a broader multi-Aspect action if it differs only by flavor and damage. |
| Service | Rework | Ally support/recovery. Specify whether it restores Vitality, reduces Strain, or removes effects; do not conflate them. |
| H-job | Conditional | Preserve only if its Mind/Aspect interaction creates a distinct mechanical role. |
| Bend | Merge candidate | Single-target damage-over-time overlaps AS. Preserve one as a basic application and the other only if its chain/escalation rule is distinct. |
| AS | Rework / merge candidate | Repeated-use Chain candidate. Specify reset conditions and whether it increases Strain dealt or vulnerability to it. |
| S Symbol | Rework | Passive recovery on Overflow. Distinguish from Ecstasy Aftershocks and Overflow Engine; define exact trigger and output. |
| Otherworldy Charm | Keep / normalize | Conditional enemy-behavior or attack-channel modifier. Rename display spelling; specify its scope and stacking policy. |
| Piercing Stares | Keep / normalize | ConditionalPassive linked to an equipment tag. The equipment requirement must be data-driven. |
| Sadism | Rework | BuildPassive that increases a declared exploit/Pressure payoff. Avoid a global unbounded Vitality-damage multiplier. |
| Masochism | Rework | BuildPassive for Fortitude/mitigation loop. Avoid a flat global damage reduction that eclipses Endure. |
| Moans | Rework / merge candidate | Reactive reflect effect. Define trigger, cap, damage channel, and relationship to Counter. |
| Encourage | Keep / normalize | Ally support buff. Specify the next-action scope and expiry. |
| Flaunt | Conditional | Area Strain attack. Compare with other AoE attacks and give it a distinct cost, target filter, or secondary effect. |
| Autof | Rework | Recovery/cleanse dependent on P-growth. Define cleanse whitelist and treat the prerequisite as a capability tag. |
| Aphrodisiac | Rework / conditional | Damage-over-time plus enemy intent modifier. Keep both only if they form a coherent shared effect. |
| P-growth | Reclassify candidate | If it changes available skills/targeting/body configuration, model as Capability/Transformation rather than an ordinary buff. Confirm persistence and removal rules. |
| Facesit | Conditional | Clarify the unusual Enemy + Self target declaration. Preserve only with explicit self-risk/target semantics and a distinct tactical payoff. |
| Bondage | Rework | Self-applied defensive/control state or a target restriction. Define who is bound, what changes, and how it ends. |
| Bully | Keep / normalize | Debuff to enemy offensive stats/intent. It can carry multiple tags, but must remain one record despite appearing in multiple archetype lists. |
| Bite | Keep / normalize | Focused physical attack; retain if its conditional effect or Aspect interaction differs from Spank. |
| Bind | Rework / conditional | Disable or restraint with resistance and duration. Differentiate from Hypnotize and Break preparation. |
| Prolonged Pl- | Rework / rename | Its current text appears to block Overflow and trigger damage under a meter condition. Specify Strain/Overflow semantics; do not use a legacy meter name. |
| F-fk | Conditional | P-growth-gated action. Keep only if its low-Vitality scaling creates a distinct risk/reward decision and is numerically capped. |
| Paizuri | Conditional | Retain as a distinct action only if it differs mechanically from other single-target Strain attacks. |
| Summon c-s | Rework / rename | Summon/capability attack. Fix the truncated name; define target set, scaling by enemy count, and whether targets include allies. |
| Swallow | Rework | Single-target finisher candidate. Eligibility should produce a configured encounter outcome rather than directly ending combat outside the shared outcome system. |
| Extra tips | Move out of ordinary combat catalog / conditional passive | Reward bonus is mainly a reward/economy modifier. Keep in the skill catalog only if it is a learnable passive with explicit reward hooks. |
| Cuteness | Rework | Ally buff; define stat/effect, target scope, duration, and stacking. |
| Naughty Thoughts | Rework | Self/build passive that improves a defined accuracy or Strain effect. Avoid vague “accuracy and damage” bonuses. |
| C-drinker | Rework | On-defeat recovery trigger. Define whether the event is defeated by Strain, defeated by this actor, or any encounter defeat; avoid ambiguous event hooks. |
| Strip | Rework / conditional | Currently combines area damage and self-evasion. Decide whether this is a coherent high-tempo action or split the effects. |
| Pink mist | Keep / normalize | Area debuff/damage-over-time. Define target filters, duration, and interaction with equivalent effects. |
| Penetrate | Conditional | P-growth-gated single-target attack. Differentiate from A-penetration by tactical role rather than name alone. |
| A-penetration | Rework / conditional | If retained, make its disable/Break interaction distinct from Penetrate and use standard resistance/outcome rules. |
| Stomp | Keep / normalize | Conditional Vitality damage based on a declared Strain threshold; use Threshold rather than hard-coded prose. |
| Summon Tentacles | Rework | High-risk area effect with possible friendly fire. Define all valid targets, risk mitigation, and enemy-count scaling explicitly. |
| Enslave | Rework / conditional | Control/finisher fantasy. Do not force a global permanent state; map to encounter-defined Disable, Yield, Capture, or another allowed outcome. |
| G-bang | Conditional / merge candidate | Area Strain attack. Compare with Flaunt and Summon Tentacles; retain only if its target/cost/secondary-effect profile is distinct. |
| Bkakke | Rework / conditional | All-target threshold finisher/high-risk outcome. Must use encounter outcome contracts and clearly define what happens to surviving targets. |
| Deepth | Rework / rename | Normalize truncated display name. Keep only if its trigger/Aspect role differs from generic single-target Strain attacks. |
| Worship C | Conditional | Area debuff/behavior modifier. Clarify whether it increases enemy Strain vulnerability, changes intent, or does both. |
| Ecstasy Aftershocks | Keep / normalize | Reactive area effect triggered by Overflow. Distinguish from S Symbol's recovery and Overflow Engine's conversion. |
| Divine Health | Rework | Passive protection/cleanse. Full debuff immunity may invalidate status systems; consider limited resistance or conditional cleanse with explicit caps. |

## 3. Approved additions: first-pass review

All fourteen previously approved additions remain candidates, with canonical mechanical IDs documented in `SKILLS_AUDIT.md` and `implementation_spec/SKILL_CATALOG.md`. They should be reconciled against legacy candidates before adding records. Particular tests:
- **Provoke vs Get Spanked vs Instill protectiveness:** target intent, self-exposure, and ally protection must be distinct.
- **Endure vs Masochism vs Unbroken:** ordinary mitigation, passive build identity, and emergency defeat prevention must not collapse into the same effect.
- **Counter vs Moans vs Turn the Tables:** define trigger windows and whether the response deals damage, reflects damage, or converts a recent event.
- **Command vs BreakResistance vs AbsoluteControl:** resource generation/control, resistance reduction/Break preparation, and encounter outcome should be separate stages.
- **S Symbol vs Ecstasy Aftershocks vs OverflowEngine:** recovery, reactive area output, and deliberate resource conversion must be distinct.
- **ExploitWeakness vs Sensory Enhancement/Otherworldly Charm:** define whether each creates vulnerability, generates Pressure, or merely modifies a specific action.

## 4. Proposed disposition policy

No skill should be removed solely because its theme is similar to another. Merge/remove only when its player decision and mechanical outcome are redundant. A thematic name can survive as a display label, an animation, a VFX profile, a conditional presentation, or a tag after its mechanics are consolidated.

A retained skill must have:
1. one stable ID;
2. one primary tactical role;
3. explicit target/cost/requirements;
4. declared canonical resources and meters;
5. a distinct effect/trigger or a deliberate reason to be a simple baseline action;
6. a tier and unlock path;
7. outcome behavior compatible with the encounter contract;
8. a testable acceptance condition.

## 5. Recommended next pass

Review the table by clusters rather than making 54 independent decisions in isolation. Suggested order:
1. resource/control/reactive loop;
2. finishers and encounter outcomes;
3. Overflow/threshold/Strain effects;
4. passives and capability/transformation;
5. physical/magical attacks and body/Aspect differentiation;
6. rewards/economy-linked skills;
7. tier, costs, prerequisites, and numeric balance.

Only after this pass should the CSV receive stable IDs and structured fields. Then run validation for duplicate IDs, missing references, invalid requirements, malformed rows, and effect/outcome consistency.
