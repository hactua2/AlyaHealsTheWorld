# AHTW — Skill Catalog Reconciliation Pass 5
## Area actions, finishers, Overflow, and encounter-outcome boundaries

> **Status:** Proposed next-stage audit. Pass 4 decisions are constraints. This document does not modify data/skills/skills.csv, approve numeric coefficients, or finalize the skill catalog.

## 1. Constraints carried forward from Pass 4

- Basic attacks may remain separate unlockable skills when body-part affinity/scaling creates meaningful build choices; use shared effect templates.
- Spank and Bite each have one primary damage channel. A second channel requires an explicit conditional rider and ordered effect resolution.
- Flirt generates Command and deals Strain damage. Its cost, resource yield, and damage output must be balanced together.
- Lay/Facesit self-risk exists only when explicitly designed as a trade-off with a declared payoff.
- AS remains a Chain/sequence skill with explicit reset conditions; if its Chain has no meaningful tactical behavior, consolidate with Bend.
- H-job retains Mind as its intended Aspect and must be rewritten as a genuine mental/sensory interaction.
- Strain and Vitality are distinct channels. Finishers request an encounter-permitted outcome; they do not bypass the encounter-outcome contract.
- CSV remains unchanged until ambiguities are resolved.

## 2. Area-action review

| Skill | Proposed identity | Required semantics | Distinctness recommendation |
|---|---|---|---|
| Flaunt | Area Strain pressure | Explicit target query, hit/accuracy policy, per-target scaling, resistance, and one declared rider at most | Keep as a broad, reliable area action. Share its effect template with other area attacks unless a unique rule changes decisions. |
| G-bang | Area Strain pressure | Same base requirements as Flaunt; declare target count/scaling and any special target filter | Conditional separate skill. Its own record is justified by distinct affinity/progression or a real targeting/cost/risk difference, not by name alone. |
| Strip | Area Strain plus temporary evasion | Resolve the area effect and evasion effect in a fixed order; define evasion duration and eligible incoming attacks | Keep distinct only if the defensive window changes turn planning and is balanced against the area output/action cost. Otherwise use the area template without the evasion rider. |
| Summon c-s | Area Strain summon that concentrates as fewer enemies remain | Target set; formula/curve for target-count scaling; minimum/maximum output; behavior when targets die or enter/leave the set; friendly-fire policy | Keep distinct for target-count scaling. Do not let damage rise without a floor/cap or a defined number of eligible enemies. |
| Summon Tentacles | HighRisk area action with explicit side exposure | Explicit affected sides and targets; per-target resolution; self/ally consequences; target-count scaling; interrupt/resistance/counterplay; recursion guard if it triggers other effects | Keep distinct from Summon c-s because the risk to allies/self is central. “Aggro everyone” is not a complete target or effect rule. |
| Pink Mist | Area Strain DoT plus named defense debuff | Explicit DoT tick/duration/refresh/stack rules and separately named debuff with its own duration/stacking/cleanse rules | Keep distinct from direct area attacks because persistent pressure and debuff maintenance create different decisions. |
| Worship C | Area intent bias OR named vulnerability/debuff | Select one primary function; explicit eligible targets and duration; avoid bundling an area attack, intent change, and vulnerability without a coherent sequence | Keep if it offers a group-control/ritual role distinct from Otherworldly Charm and Aphrodisiac; otherwise consolidate the redundant effect. |

### Recommended shared templates

- `AreaStrainAttack`: target query + per-target hit/impact + target-count rule + declared optional rider.
- `AreaStrainDoT`: target query + per-target application of a registered DoT + explicit tick/stack/expiry policy.
- `AreaHighRiskAction`: explicit target sets on each side + deterministic per-target resolution + self/ally risk + caps/counterplay.
- `AreaIntentEffect`: declared intent change/bias over eligible targets with duration and resistance.
- `ApplyTemporaryEvasion`: explicit attack eligibility, duration, and timing.

These are logical templates, not automatic requests to add custom runtime handlers. Reuse canonical primitives where possible.

## 3. Area scaling and targeting rules to close

1. **Target selection:** distinguish “all enemies,” “all combatants,” “all valid targets,” and “all other actors.” Never infer target sides from a display label.
2. **Per-target calculation:** each target resolves its own accuracy, resistance, damage channel, vulnerability, and outcome check unless the effect explicitly specifies a shared roll.
3. **Target-count scaling:** declare whether output scales per target, inversely with target count, or concentrates a fixed budget across remaining targets. Define min/max and rounding.
4. **Friendly fire:** if allies/self are eligible, state whether they receive the full effect, a reduced effect, a different channel, or a separate consequence. No implicit friendly fire.
5. **Deaths/disable during resolution:** define whether the target list is snapshotted at action start or recomputed after each target; recommendation: snapshot eligible targets at action resolution start, then skip actors no longer valid when their turn in the list arrives.
6. **Ordering:** target ordering must be deterministic, such as stable combatant ID order after the target query is evaluated.
7. **Riders:** a defensive or debuff rider should apply once to the actor or separately per target, explicitly. Do not accidentally multiply a self-buff by target count.
8. **Overflow triggers:** an area effect that causes multiple targets to cross Strain thresholds must specify whether each target can trigger an Overflow event independently and how chained effects are capped.

## 4. Finisher and outcome review

| Skill | Proposed identity | Required semantics | Recommendation |
|---|---|---|---|
| Swallow | Single-target finisher request at a Strain/state threshold | Eligibility predicate, resistance/contest, outcome request, fallback if target is ineligible, and resource/cost behavior on failure | Keep as a focused threshold finisher. Request only an encounter-permitted outcome such as Disable, Capture, Yield, or another explicitly authored result. |
| Bkakke | Multi-target finisher request | Resolve independently per target; define whether all targets must meet the threshold; define survivor consequence, self-risk, and partial success behavior | Do not use “wins combat” as a direct effect. Replace it with a batch of per-target outcome requests and a defined risk consequence if one or more targets survive. |
| Enslave | High-investment control/outcome request | Eligibility, resistance, duration, allowed outcomes, Command/Break costs, failure behavior, and target immunity/exception tags | Keep as a control route only if its setup/resource loop differs from Absolute Control or its outcome semantics are distinct. |
| Absolute Control | High-investment Command/Break conversion | Same shared outcome contract as Enslave; explicit resource spend and prerequisite state; deterministic failure result | Keep separately only if it represents a materially different investment path or allowed outcome. Otherwise combine under a shared finisher effect definition with different requirements/scaling profiles. |
| Stomp | Convert target Strain threshold into Vitality damage | Threshold, conversion cap, mitigation order, target validity, and whether the threshold is consumed | Keep distinct: it converts progress between damage channels rather than requesting an encounter outcome. |
| F-fk | Capped bonus against low-Vitality target | State whose Vitality is checked, threshold, scaling cap, order relative to mitigation, and interaction with Strain threshold | Keep distinct from a generic attack only if the threshold window changes target priority and timing. |

### Outcome contract for every finisher

A finisher must declare:
- the target predicate and threshold/state requirement;
- resistance or contest procedure;
- the exact requested outcome, chosen from the encounter's permitted outcomes;
- whether the request can partially succeed for area finishers;
- resource/cost handling on success and failure;
- fallback behavior when the target becomes invalid before resolution;
- effects on surviving targets and the user;
- deterministic event ordering.

A finisher may request an outcome but may not independently end the encounter or override an encounter's allowed outcomes.

## 5. Overflow cluster review

| Skill | Proposed role | Trigger/output contract | Keep distinct if… |
|---|---|---|---|
| S Symbol | Passive recovery | One resolved Overflow event triggers one declared recovery output: restore Vitality, reduce Strain, or remove an eligible effect | It chooses a different recovery channel from the other Overflow options or has a distinct trigger/eligibility profile. |
| Ecstasy Aftershocks | Passive area retaliation | One resolved Overflow event produces a bounded area effect against a declared target set; cannot recursively trigger itself | Automatic offensive retaliation is distinct from recovery and requires no player choice after activation. |
| Overflow Engine | Active/configurable conversion | Converts a resolved Overflow event into one selected output; declare selection timing, allowed outputs, cost, cap, and recursion behavior | Player configuration materially changes the build or response. If it merely duplicates one passive output, merge or redesign. |
| Prolonged Pl- | Threshold/Overflow manipulation | Must choose a single coherent transition: prevent Overflow, lock at a threshold, or convert qualifying follow-up actions. No contradictory combination | Keep only if the transition creates a clear control strategy distinct from ordinary Strain damage. |

### Recommended Overflow event contract

1. Determine Strain changes from the resolved action.
2. Evaluate whether each affected actor crossed the defined Overflow boundary.
3. Emit one resolved Overflow event per qualifying actor and threshold crossing according to the canonical meter rules.
4. Trigger eligible listeners in deterministic priority order.
5. Prevent a listener from recursively triggering itself indefinitely; enforce explicit chain depth/output caps.
6. Apply recovery/retaliation/conversion effects and then evaluate encounter outcomes.
7. If multiple listeners compete for the same event, each must specify whether it observes the original event or a modified state; do not consume the same event implicitly.

This sequence is a proposal for content definition and must be reconciled with the canonical turn-resolution contract before implementation.

## 6. Cross-skill synergies

- **Area pressure → persistent control:** Flaunt/G-bang → Pink Mist → vulnerability or intent effect → threshold conversion.
- **Risk/reward summon:** Summon Tentacles exposes declared sides to risk → Fortitude/mitigation builds reduce the cost → area pressure can accelerate Strain thresholds on both sides.
- **Concentrated summon:** Summon c-s becomes stronger against fewer eligible enemies → use target priority to finish a dangerous survivor rather than maximizing raw total damage.
- **Threshold conversion:** Bend/AS/Pink Mist build Strain → Stomp converts a defined threshold into Vitality progress; Swallow requests an allowed outcome.
- **Single vs multi-target finisher:** Swallow focuses setup on one eligible target; Bkakke requires group threshold preparation and carries survivor risk.
- **Overflow build choice:** S Symbol for recovery, Ecstasy Aftershocks for automatic retaliation, Overflow Engine for configured conversion.
- **Control investment:** Command generation → Break setup → Enslave/Absolute Control outcome request, with encounter-specific eligibility and failure handling.

## 7. Decisions requested before numerical balancing

### Decision 1 — Flaunt, G-bang, and Strip
**Recommended: B.** Share the AreaStrainAttack template; keep Strip distinct only if its evasion window is a meaningful tactical trade-off.

- A. Keep all three as mechanically unique actions.
- **B. Shared area template; Strip keeps its defensive rider if balanced.**
- C. Merge all three into one skill with presentation variants.

### Decision 2 — Summon c-s scaling
**Recommended: A.** Preserve the “fewer enemies = stronger summon” identity, with explicit floor/cap and a per-target rule.

- **A. Concentrates output against fewer valid enemies; define curve and cap.**
- B. Fixed total output distributed across current targets.
- C. Remove target-count scaling and differentiate it through another tactical hook.

### Decision 3 — Summon Tentacles friendly fire
**Recommended: B.** Explicitly expose allies/self only if they are named in the action's target query and consequence rules.

- A. Always affects all combatants equally.
- **B. Declared target sides and deterministic friendly-fire consequences.**
- C. Enemies only; “aggro everyone” becomes visual flavor, not mechanical targeting.

### Decision 4 — Bkakke partial success
**Recommended: B.** Resolve the finisher request per target and apply the survivor consequence if any eligible target survives.

- A. Combat victory only if every enemy is eligible and the request succeeds on every target.
- **B. Per-target outcomes; survivor consequence when one or more targets remain.**
- C. Single group-level contest with all-or-nothing outcome.

### Decision 5 — Enslave vs Absolute Control
**Recommended: B.** Keep both only if the investment path differs: Enslave is a target/state eligibility control route; Absolute Control is the expensive Command + Break conversion route.

- A. Merge into one top-tier finisher.
- **B. Keep distinct through different setup/resource loops and declared outcome requests.**
- C. Keep both only if they request different permitted outcomes; otherwise merge.

### Decision 6 — Overflow architecture
**Recommended: A.** Preserve three roles: recovery (S Symbol), automatic area retaliation (Ecstasy Aftershocks), and player-configured conversion (Overflow Engine), all with caps and recursion guards.

- **A. Keep all three roles distinct.**
- B. Reduce to two roles by merging recovery and active conversion.
- C. Reduce to two roles by merging retaliation and active conversion.

## 8. Still open after this pass

- Numerical scaling curves, target-count formulas, caps, costs, thresholds, and duration.
- Exact allowed outcome per encounter and per finisher.
- Overflow boundary and event order as reconciled with turn-resolution.
- Exact Strain/Vitality channel and conditional rider for Spank/Bite/Facesit.
- Flirt's combined Command + Strain tuning.
- AS Chain/reset behavior.
- H-job's precise mental/sensory effect.
- P-growth target scope, persistence, and revocation.
- Whether scaling/affinity alone justifies every basic skill's unlock cost.

## 9. Acceptance criteria

Before CSV migration:
- Every area action defines its target set, per-target resolution, target-count scaling, rider scope, friendly fire, and deterministic ordering.
- Every finisher obeys the encounter outcome contract and defines failure/partial success.
- Every Overflow listener has a single trigger contract, bounded output, and recursion behavior.
- No numeric balancing occurs before target semantics and distinctness decisions are closed.
