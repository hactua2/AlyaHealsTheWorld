# AHTW — Skill Catalog Reconciliation Pass 6
## Cross-cutting semantics: target resolution, scaling, capabilities, and event atomicity

> **Status:** Updated with the project owner's seven decisions. Pass 4 and Pass 5 decisions remain binding constraints. This pass does not modify `data/skills/skills.csv`, lock numeric coefficients, or finalize the catalog.

## 1. Decisions carried forward

### Pass 4
- Similar basic actions may remain distinct when per-skill body-part affinity/scaling creates meaningful build choices; share effect templates where possible.
- Spank and Bite each have one primary damage channel. A second channel is an explicit conditional rider.
- Flirt generates Command and deals Strain damage; cost, yield, and damage must be balanced together.
- Lay/Facesit self-risk exists only when intentionally defined as a trade-off with a declared payoff.
- AS remains a Chain/sequence skill with explicit reset conditions; if no meaningful Chain behavior can be defined, consolidate with Bend.
- H-job retains Mind as its intended Aspect and must become a genuine mental/sensory interaction.

### Pass 5
- Flaunt, G-bang, and Strip remain mechanically distinct. They need real differentiators beyond labels/animations.
- Summon c-s concentrates output against fewer valid enemies, with a defined curve and cap.
- Summon Tentacles may affect enemies, allies, and the user; each side/effect is declared and resolved deterministically.
- Bkakke allows encounter victory only if every enemy is eligible and every outcome request succeeds; each failed/ineligible target also triggers a defined self-risk consequence, while successful target outcomes persist.
- Enslave and Absolute Control merge into one top-tier finisher identity; no duplicate mechanical records.
- Overflow retains three distinct roles: S Symbol = passive recovery; Ecstasy Aftershocks = automatic area retaliation; Overflow Engine = active/configurable conversion.
- CSV remains unchanged.

## 2. Cross-cutting semantics audit

### 2.1 Action validation and costs

The canonical turn-resolution contract states that invalid actions cannot partially spend costs or mutate state; valid actions commit costs before resolving their effect sequence. Therefore:
- **Invalid before cost commitment:** no costs spent, no effects applied.
- **Valid action that misses, is resisted, or fails a target eligibility/contest check:** costs remain spent unless the skill explicitly defines a refund.
- **Mixed-target area action:** one action cost is committed once; per-target outcomes are resolved independently in deterministic order.
- **Finisher request failure:** default to costs remaining spent after a valid action; any refund must be explicit in the skill data.

This follows the existing atomic-validation contract and avoids treating a failed contest as an invalid action.

### 2.2 Multi-target effect resolution

Recommended common rules:
1. Snapshot the eligible target list after validation and before the first effect resolves.
2. Sort targets by the canonical deterministic ordering (stable combatant ID unless the encounter declares another priority).
3. Resolve accuracy, resistance, damage channel, status application, threshold crossings, and outcome requests per target.
4. Skip a target if it becomes invalid before its turn in the snapshot; do not silently replace it with a new target.
5. Resolve actor-level riders (e.g. temporary evasion on Strip) once per action, not once per target, unless data explicitly says otherwise.
6. Evaluate encounter victory only after the current atomic action completes, consistent with `implementation_spec/TURN_RESOLUTION.md`.

This preserves deterministic results and prevents target-count exploits from multiplying self-buffs or action costs.

### 2.3 Bkakke: strict victory condition with per-failure self-risk

**Owner decision: C.** Resolve each target independently and persist successful per-target outcomes. The encounter counts as won only if every enemy was eligible and every request succeeded. Each failed or ineligible target also triggers a predefined self-risk consequence.

Recommended guardrails:
- Apply the self-risk consequence once per failed/ineligible target, in deterministic target order.
- Declare the consequence's channel, magnitude/scaling, and whether it can itself cause defeat before catalog lock.
- The consequence cannot retroactively invalidate already-resolved successful target outcomes.
- If no targets fail, no self-risk consequence occurs.
- Encounter victory is evaluated only after the atomic action and all target-specific consequences finish.

### 2.4 Overflow event semantics

**Owner decision: A.** Emit at most one Overflow event per affected actor per resolved action when the canonical boundary is crossed. Additional Strain changes to that actor during the same action do not emit duplicate events.
- S Symbol, Ecstasy Aftershocks, and Overflow Engine each listen to that resolved event under their own eligibility conditions.
- Apply listeners in deterministic priority/application order.
- Each listener declares its output cap and cannot recursively trigger itself. Any cross-skill chain depth cap must be explicit in the combat rules.
- A listener cannot implicitly consume or suppress the event for other listeners.

### 2.5 Body-part affinity and attribute scaling

**Owner decision: A.** Use a per-skill calculation profile: compute the weighted contribution of declared primary attributes, then apply only the matching body-part affinity as a separate modifier.
1. `scaling_ref` selects a weighted subset of primary attributes for the action.
2. The skill's declared body-part Aspect selects only the matching affinity/multiplier input(s).
3. Apply the affinity as a separate modifier after the weighted attribute contribution, using a shared documented default operation.
4. Apply skill base power, target resistance/mitigation, vulnerability, and conditional riders in a documented order.
5. For multi-Aspect actions, each skill must explicitly define its combination rule. No implicit multiplication of all Aspects.

No coefficients should be locked in this pass. The goal is to make each skill's calculation auditable and prevent accidental stacking.

### 2.6 P-growth capability

P-growth is a Capability/Transformation that enables dependent skills, but recipient scope and lifecycle remain open. Recommended contract:
- A capability is attached to a specific actor, not silently granted globally.
- It persists until an explicit removal/reversal event or a content-defined condition; it does not expire as a normal short-duration buff unless explicitly defined as temporary.
- Dependent skills check the capability at action validation time. If absent, the action is invalid and no cost is spent.
- Removing the capability disables dependent skills immediately; it does not erase unrelated progress or permanently acquired skill records.
- Granting the capability to an ally must be explicit in the skill target and acquisition event; never infer that "Ally" means every ally.

### 2.7 H-job and Mind Aspect

**Owner decision: C.** Keep Mind as the Aspect and define H-job as a focused Strain damage-over-time effect against a declared mental/sensory vulnerability. Specify tick timing, duration, refresh/stack behavior, and resistance interaction; do not bundle direct intent manipulation or generic stun unless a separate effect is explicitly authored.

## 3. Proposed distinct identities for area actions

The owner decided these three skills remain mechanically distinct. The following division is recommended for approval:

| Skill | Proposed unique rule | Why it is distinct |
|---|---|---|
| Flaunt | Reliable, broad area Strain pressure with stable per-target output and no defensive rider | Baseline area pressure; simple and predictable. |
| G-bang | Area Strain output increases with the number of valid enemy targets, with a cap | Rewards fighting a group; deliberately contrasts with Summon c-s, which concentrates against fewer enemies. |
| Strip | Area Strain pressure plus a temporary self-evasion window | Trades some output/cost budget for defensive tempo; evasion applies once per action. |

These may share an implementation template. “Mechanically distinct” means the target-count rule, rider, requirements, cost, or scaling actually changes the decision; a different label or animation alone is insufficient.

## 4. Remaining decisions requested

### Decision 1 — Bkakke partial target outcomes — DECIDED: C
Successful target outcomes persist; any failed/ineligible target prevents encounter victory and triggers a predefined self-risk consequence once for that target.

- A. Per-target success persists; failure prevents victory without rollback.
- B. Roll back every target outcome if any target fails.
- **C. Successful target outcomes persist, but each failed/ineligible target also triggers a predefined self-risk consequence.**

### Decision 2 — Flaunt/G-bang/Strip differentiators — DECIDED: A
Approve the distinct roles proposed in section 3.

- **A. Flaunt = reliable flat area pressure; G-bang = capped bonus for larger enemy groups; Strip = area pressure + temporary self-evasion.**
- B. Flaunt = bonus against vulnerable targets; G-bang = flat area pressure; Strip = area pressure + temporary self-evasion.
- C. Keep all three distinct, but leave their differentiators unresolved until encounter playtests.

### Decision 3 — Summon Tentacles affected sides — DECIDED: A
Preserve the high-risk identity by declaring all affected sides explicitly, including friendly fire where applicable.

- **A. May affect enemies, allies, and the user; each side/effect is declared in the skill data and resolved deterministically.**
- B. Affects enemies and the user, but never allies.
- C. Affects enemies only; the risk is represented by a drawback other than friendly fire.

### Decision 4 — Overflow event frequency — DECIDED: A
At most one event per affected actor per action when crossing the canonical boundary.

- **A. One Overflow event per affected actor per action; no duplicate triggers from the same action.**
- B. One event for every threshold crossing, even within one action.
- C. One event per turn, even if multiple separate actions trigger Overflow in that turn.

### Decision 5 — P-growth capability scope — DECIDED: A
P-growth is exclusive to Alya; dependent skills are unavailable to allies.

- **A. Alya only; dependent skills can never be used by allies.**
- B. Actor-specific; acquisition can target Alya or an eligible ally when explicitly declared.
- C. Community-wide unlock that automatically enables the skill for every ally.

### Decision 6 — Attribute + body-part affinity composition — DECIDED: A
Use a per-skill scaling profile that computes a declared weighted attribute contribution and then applies only the matching body-part affinity as a separate modifier. Multi-Aspect skills must explicitly define their combination rule.

- **A. Weighted attribute contribution, then matching Aspect modifier; multi-Aspect combination declared per skill.**
- B. Add attribute contribution and affinity as independent additive terms.
- C. Let every skill author a fully custom formula without a shared default.

### Decision 7 — H-job effect identity — DECIDED: C
Focused Strain damage-over-time against a declared mental/sensory vulnerability.

- A. Focused Strain; improved effectiveness against exposed intent or reduced mental/sensory resistance.
- B. Focused Strain plus direct intent manipulation.
- **C. Focused Strain DoT against mental/sensory vulnerability.**

## 5. Catalog-wide ambiguities still open after Pass 6

- Numeric attribute weights, body-part affinity coefficients, base power, caps, and damage rounding.
- The exact primary channel and conditional rider for Spank/Bite/Facesit.
- Flirt's Command yield vs Strain output and action cost.
- AS Chain advancement, qualifying use, and reset conditions.
- The unique rule and target-count cap for G-bang; exact cost/output budgets for Flaunt and Strip.
- Summon c-s scaling curve and behavior when valid target count is zero or changes during resolution.
- Summon Tentacles' exact target/effect matrix, including whether the user and allies receive identical or side-specific effects.
- Bkakke's exact self-risk channel/magnitude and whether it can cause defeat.
- Shared Enslave/Absolute Control finisher requirements, resistance, duration, permitted outcomes, and failure behavior.
- Overflow boundary semantics and cross-listener priority/caps.
- P-growth lifecycle/revocation and dependent-skill prerequisites; recipient scope is now locked to Alya only.
- H-job's DoT tick/duration/refresh/stack/resistance details, plus legacy Aspect/target-field validation for H-job, Encourage, Extra Tips, and C-drinker.
- Skill tiers, Skill Point costs, prerequisite graph, progression gates, cooldowns, and resource costs.
- Final migration from the 54 named legacy rows and 14 proposed additions into the canonical catalog.

## 6. Acceptance gate before CSV migration

Do not migrate `data/skills/skills.csv` until:
1. Decisions 1–7 are answered or explicitly deferred with an owner-approved default.
2. Every skill has a target predicate, primary channel/effect, scaling profile, Aspect combination rule, cost/failure policy, and declared triggers.
3. Every area skill has deterministic target selection and per-target resolution.
4. Every finisher follows the encounter outcome contract, including failure and partial-target behavior.
5. Every Overflow listener has bounded, non-recursive output and deterministic event ordering.
6. Every Capability-gated skill has a clear prerequisite and lifecycle.
