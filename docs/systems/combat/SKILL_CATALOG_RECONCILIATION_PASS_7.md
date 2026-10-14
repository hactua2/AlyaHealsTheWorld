# AHTW — Skill Catalog Reconciliation Pass 7
## Skill-level semantic gaps and proposed content defaults

> **Status:** Proposed next review. Passes 4–6 owner decisions are binding. This pass does not modify `data/skills/skills.csv`, lock numerical coefficients, or authorize catalog migration.

## 1. Locked constraints carried forward

- Similar basic actions may remain separate records when their body-part affinities/scaling create meaningful build choices; implementation templates can be shared.
- Spank and Bite each have one primary damage channel; any secondary channel must be a conditional rider.
- Flirt generates Command and deals Strain damage; balance must consider both outputs and the action cost together.
- Lay/Facesit self-risk exists only when explicitly authored as a trade-off with a defined payoff.
- AS remains a Chain/sequence skill with explicit reset conditions; merge with Bend only if a meaningful chain cannot be specified.
- H-job is a focused Strain DoT against a declared mental/sensory vulnerability.
- Flaunt = reliable flat area Strain pressure; G-bang = capped bonus for larger enemy groups; Strip = area Strain + temporary self-evasion.
- Summon c-s concentrates output against fewer valid enemies; Summon Tentacles can affect enemies, allies, and the user, with each side/effect declared.
- Bkakke: successful target outcomes persist; each failed/ineligible target triggers a declared self-risk consequence; encounter victory requires every target request to succeed.
- Enslave and Absolute Control are one shared top-tier finisher identity.
- Overflow has three distinct roles and emits at most one event per affected actor per resolved action.
- P-growth is exclusive to Alya.
- Skill scaling uses weighted primary attributes, then the matching body-part affinity as a separate modifier; multi-Aspect combination must be explicit.
- `data/skills/skills.csv` remains unchanged.

## 2. Proposed semantic defaults

### 2.1 Spank and Bite — primary channel
**Recommendation: A.** Spank's primary channel is Strain; Bite's primary channel is Vitality. Each may have a secondary channel only through an explicit condition (e.g., a declared vulnerability/stance), never as unconditional dual-channel damage.

- A. Spank = Strain; Bite = Vitality; conditional riders only.
- B. Spank = Vitality; Bite = Strain; conditional riders only.
- C. Both are single-channel actions, but leave the primary channels unresolved until playtesting.

### 2.2 Flirt — hybrid Command + Strain
**Recommendation: A.** Treat Flirt as a low-to-moderate Strain attack and a modest Command generator in the same action, with a shared action-cost budget. It should be less efficient than a dedicated Strain attack at pressure and less efficient than a dedicated Command action at resource generation.

- A. Both effects occur on a successful action; each has a separate coefficient and the combined efficiency is intentionally below specialized actions.
- B. Command is generated only when the target has exposed intent; otherwise Flirt deals Strain only.
- C. Flirt deals Strain; Command generation is a conditional rider after exploiting a vulnerability.

### 2.3 AS — Chain advancement and reset
**Recommendation: A.** Chain advances only when AS successfully applies its primary effect to at least one valid target. It resets when the user uses a non-chain action, the action is invalid, the encounter ends, or the user loses the required capability/state. Misses/resistance that still leave the action valid do not reset the chain unless no target receives the primary effect.

- A. Explicit successful-effect Chain with the reset conditions above.
- B. Chain advances on action use, even if the primary effect is fully resisted.
- C. Chain is a per-target sequence and resets separately for each target.

### 2.4 Prolonged Pl- — Overflow interaction
**Recommendation: A.** Make it a Threshold lock: while active, it prevents the affected actor's Strain from crossing the Overflow boundary, but it does not erase Strain or convert it to Vitality damage. On expiry/removal, immediately evaluate the current Strain value and emit the normal Overflow event if the actor is still at/over the boundary. This creates a clear interaction without inventing a second meter.

- A. Temporarily prevents Overflow; re-evaluate on removal/expiry.
- B. Converts Strain that would cause Overflow into Vitality damage.
- C. Extends/locks the threshold and converts subsequent attacks into Vitality damage.

### 2.5 Summon c-s — target-count scaling
**Recommendation: A.** Let `N` be the count of valid enemy targets snapshotted at validation. Use a monotonic capped concentration curve: per-target output increases as N falls, but the action's total output cannot exceed a fixed maximum. If N = 0, the action is invalid and costs are not spent. Changes after the snapshot do not retarget or recalculate the curve during the same action.

- A. Capped concentration curve, target count snapshotted at validation, invalid at N=0.
- B. Fixed total output distributed across valid targets.
- C. Fixed per-target output, with no target-count modifier.

### 2.6 Shared Enslave/Absolute Control — permitted outcome
**Recommendation: A.** The shared skill requests exactly one authored outcome from the permitted set `Yield`, `Disable`, or `Capture`, selected by the skill's data/variant and target eligibility. It never directly ends an encounter, never requests `Defeat` implicitly, and always follows the encounter outcome contract. Invalid eligibility prevents action commitment; a valid request that is resisted spends costs unless explicit refund data says otherwise.

- A. One declared outcome request per use from Yield/Disable/Capture; no implicit Defeat/global victory.
- B. Always requests Capture; other outcomes are narrative-only.
- C. Outcome is selected dynamically by the encounter, with skill data providing only the eligibility gate.

### 2.7 Summon Tentacles — per-side effect matrix
**Recommendation: A.** Declare separate target-side entries for enemies, allies, and user. The default is the same primary Strain channel for all valid targets, but ally/user hits are allowed only when their side is explicitly enabled; any side-specific mitigation/rider must be explicit. Target list and side flags are snapshotted at validation.

- A. Separate side flags and explicit effects; all sides can be included.
- B. Enemies receive full effect; allies/user receive a reduced version by default.
- C. Always affects all sides identically, with no per-side configuration.

### 2.8 H-job — DoT behavior
**Recommendation: A.** Use the standard DoT lifecycle: tick at the affected target's start of turn, decrement duration after the tick, expire after the final tick, refresh duration to the greater remaining/new duration on reapplication, and do not stack duplicate instances by default. Mental/sensory resistance reduces or blocks application according to the standard resistance rule; exact numbers remain balance work.

- A. Standard start-of-turn tick, duration decrement after tick, refresh to max duration, no duplicate stacking.
- B. Tick immediately on application and at each start of turn thereafter.
- C. New applications stack separate DoT instances with independent durations.

## 3. Still-open numeric/balance work (not decisions for this pass)

- Attribute weights, Aspect coefficients, base power, output caps, damage rounding, and resistance curves.
- Flirt's exact action cost, Command yield, and Strain output.
- Summon c-s's exact concentration curve and cap.
- G-bang's exact group bonus and cap; Flaunt/Strip cost and output budgets.
- Bkakke's self-risk channel/magnitude and whether the consequence can defeat its user.
- Summon Tentacles' exact per-side effects, costs, and consequences.
- Overflow listener priorities, output caps, and maximum cross-listener chain depth.
- P-growth persistence/revocation and the final dependency list for Autof/F-fk/Penetrate/A-penetration.
- Skill tiers, Skill Point costs, prerequisites, progression gates, cooldowns, and resource costs.
- Validation of legacy Aspect/target fields for Encourage, Extra Tips, and C-drinker.

## 4. Migration gate

Do not change `data/skills/skills.csv` until:
1. The semantic defaults in this pass are approved or replaced by explicit owner decisions.
2. Every retained skill has a target predicate, primary channel/effect, scaling profile, Aspect-combination rule, cost/failure policy, duration/stack/tick rules where relevant, and declared triggers.
3. Multi-target actions, finishers, Overflow listeners, and capability gates pass deterministic resolution checks.
4. Duplicate mechanical identities are consolidated while preserving intentional build choices from scaling, requirements, or tactical behavior.
5. The project owner explicitly authorizes the CSV migration.
