# AHTW — Skill Catalog Reconciliation Pass 4
## Focused single-target actions: scaling profiles, effect identity, and redundancy

> **Status:** Review proposal. This pass narrows the audit to focused single-target actions. It does not change data/skills/skills.csv, approve numerical coefficients, or lock the final catalog.

## 1. Decisions already treated as constraints

- The eight primary attributes remain BODY, AGI, SOUL, CHARM, DOM, SUB, SAD, and MAS.
- The body-part affinity used by a skill is a separate scaling input. It can change the effectiveness of otherwise similar actions.
- There is no universal body-part-to-attribute mapping. Each skill or reusable scaling profile declares its own contributors.
- Strain damage and Vitality damage are separate effect channels. Legacy labels must be interpreted semantically, not replaced blindly.
- A shared effect template does not require merging skills if their scaling, body-part affinity, prerequisites, costs, risk, trigger, target state, or synergies make different build choices.
- Names and animations alone do not justify separate mechanical records.
- No coefficients, caps, durations, costs, or unlock prerequisites are approved by this pass.

## 2. Proposed reusable scaling-profile shape

Each profile should declare:
1. **Primary attribute(s):** main contributor(s) to effectiveness.
2. **Secondary attribute(s):** smaller/conditional contributor(s), if any.
3. **Body-part affinity:** one part or an explicitly defined composite.
4. **Effect channel:** Strain, Vitality, mixed, recovery, control, or support.
5. **Context hook:** e.g. target state, vulnerability, consecutive use, P-growth, or threshold.
6. **Guardrails:** cap, resistance check, action-economy rule, and/or explicit target validation.

The words “primary” and “secondary” indicate a proposed profile structure, not numerical weights. Do not assume all listed attributes contribute to every effect in the same way. A future formula should allow different attribute contributions for hit chance, Strain impact, Vitality impact, duration, and control strength where the design needs that distinction.

## 3. Focused-action review matrix

### A. Basic Strain-focused actions

| Skill | Proposed profile | Core effect | Why it may remain distinct | Main unresolved point |
|---|---|---|---|---|
| Bl-job | CHARM + SUB; Mouth | Focused Strain attack | Mouth affinity and a CHARM/SUB profile may support a different build from other actions | Does it have any unique cost, requirement, state interaction, or only a unique profile/animation? |
| Lay | SUB + MAS; Crotch | Focused Strain attack | Could reward exposure/Resolve or a different body-part specialization | Should it carry self-exposure risk, or is it a reliable basic action? |
| Grope | CHARM + AGI; Ass + Breasts composite | Focused Strain attack | A defined multi-part composite can support a distinct affinity build | Should the composite use a fixed declared formula, a chosen part, or be reduced to one part? |
| H-job | AGI + CHARM; **body-part tag unresolved** | Focused Strain attack | Could emphasize accuracy/precision instead of raw Strain output | The CSV says Mind, but the description describes hands/sensitive spots. Confirm Mind as a genuine mental Aspect or change the part to a defined physical part. |
| Paizuri | CHARM + SUB; Breasts | Focused Strain attack | Breast affinity gives a distinct scaling route from Mouth/Crotch/Ass actions | Is affinity alone enough to justify its own unlock, given the action uses the shared basic-attack template? |
| Deepth | SUB + MAS; Mouth | Focused Strain attack | Could reward high SUB/MAS and Mouth affinity | Needs a concrete tactical distinction from Bl-job; otherwise one can be a presentation variant. |
| Flirt | CHARM + DOM; Mouth | Generate Command **or** deal modest Strain | Resource generation has a different role from direct damage and sets up control | Recommendation: make Flirt the early, low-cost Command generator; do not also give it full damage value. |

**Recommendation:** Use one shared FocusedStrainAttack effect template, with a per-skill scaling profile. Retain separate unlockable actions when the body-part affinity, attribute profile, prerequisite, cost, risk, or tactical hook creates a meaningful choice. Do not create a bespoke effect handler per animation.

### B. Focused physical / mixed-channel actions

| Skill | Proposed profile | Core effect | Why it may remain distinct | Main unresolved point |
|---|---|---|---|---|
| Spank | BODY + SAD; Ass | Focused physical action; legacy record lists Strain and Vitality damage | Ass affinity and SAD/BODY scaling can specialize toward physical/Vitality impact | Should it deal both channels, or choose one primary channel with a conditional rider? |
| Bite | BODY + SAD; Mouth | Focused physical action; legacy record lists Strain and Vitality damage | Mouth affinity can create a different scaling path from Spank | If effect/cost/risk are identical, keep separate only if the affinity is a deliberate build choice. |
| Facesit | BODY + SUB; Crotch | Focused mixed-channel action; self-risk only if explicit | Can trade actor exposure for pressure on a vulnerable target | CSV targets both Enemy and Self. Is self-targeting an actual cost/effect, or just a legacy targeting mistake? |
| Penetrate | BODY + DOM; Crotch; requires P-growth | Focused Strain attack | Capability gate and Crotch affinity create a progression specialization | Is it a reliable Strain attack, or should it have a specific interaction with an existing state? |
| A-penetration | BODY + DOM; Crotch; requires P-growth | Focused attack plus a defined control/Break rider | Different from Penetrate if the rider changes turn planning or enables a setup chain | Recommendation: use a named control/Break effect with resistance and duration; avoid an undefined “stun”. |
| F-fk | BODY + DOM; Crotch; requires P-growth | Strain attack that scales against a target below a Vitality threshold | Rewards timing and target selection rather than being a flat upgrade | Define threshold, whose Vitality is checked, scaling cap, and whether it also deals Vitality damage. |
| Get Spanked | MAS + SUB; Ass | Deliberate exposure; gain Resolve after a qualifying enemy event resolves | Not a direct attack: converts chosen risk into future reactive options | Confirm the reward trigger is an actual resolved incoming event, not merely selecting the action. |
| Mstrbate | MAS + CHARM; Crotch | Self-recovery **or** enemy-intent influence | Could create self-sustain or a control loop | Recommendation: choose one main effect per skill. If both are retained, specify a real cost/risk trade-off and separate ordered effects. |

**Recommendation:** Separate the hit/effect calculation from channel conversion. A skill may use a shared hit/scaling profile and then apply Strain, Vitality, or both as explicit ordered effects. Do not infer that “Physical” means Vitality damage or “Magical” means Strain damage.

### C. Single-target sustained damage and control

| Skill | Proposed profile | Core effect | Why it may remain distinct | Main unresolved point |
|---|---|---|---|---|
| Bend | SUB + MAS; Ass | Baseline single-target Strain-over-time | Establishes the basic DoT loop | Define tick timing, duration, refresh, stacking, and expiry in the companion effect definition. |
| AS | SUB + MAS; Ass | Chain/sequence effect tied to consecutive use | Sequence commitment can create a different tactical decision from Bend | Recommendation: keep separate only if consecutive use changes state/output with explicit reset conditions; otherwise merge into Bend as a variant. |
| Sensory Enhancement | SOUL + CHARM; Mind | Apply a tagged vulnerability to a named channel | Sets up Exploit/Pressure and follow-up skills rather than dealing direct damage | Name the vulnerability target: Strain, Vitality, a specific action tag, or a registered damage family. |
| Hypnotize | SOUL + DOM; Mind | Change intent or apply a defined control state | Alters enemy options; not just damage-over-time | Recommendation: remove the ambiguous “stun + DoT” bundle. Choose intent change or a registered control state as primary. |
| Bind | SOUL + DOM; Mind | Restraint/control state limiting declared actions | Can set up Break Resistance, Hypnotize, or outcome requests | Define exactly which action categories are restricted and how the target resists/escapes. The current scaling audit accidentally omitted Bind; it belongs in the control review. |
| Bully | CHARM + SAD; Mouth | Intimidation debuff to named offensive stats | Reduces capability rather than changing intent or applying control | Choose attack effectiveness and/or accuracy; avoid vague “attack and defense” without registered stat IDs. |

**Recommendation:** Treat damage-over-time, vulnerability, intent change, and action restriction as separate effect families. They can share scaling inputs where appropriate, but their state semantics and counterplay should not be conflated.

## 4. Candidate shared effect templates

1. FocusedStrainAttack: target query + hit/accuracy + Strain impact + optional declared rider.
2. FocusedVitalityAttack: target query + hit/accuracy + Vitality impact + mitigation.
3. FocusedMixedChannelAttack: ordered Strain and Vitality effects; each channel declares its own scaling/mitigation rule.
4. ApplyStrainDoT: apply registered effect with explicit tick/duration/refresh/stack rules.
5. ApplyVulnerability: apply a named vulnerability tag/channel with stacking/cap rules.
6. ChangeIntent: deterministic intent-selection modification with eligibility and duration.
7. ApplyControlState: registered state that restricts named action categories, with resistance and expiry.
8. GenerateResourceOnResolvedEvent: resource generation tied to a named event, never to ambiguous action selection alone.

These are proposed templates, not necessarily new runtime effect types. Reuse the existing canonical primitives where possible.

## 5. Cross-skill synergies

- **Command → Break → Control:** Flirt/Command generates Command → Break Resistance lowers a named resistance or adds Break progress → Hypnotize changes intent or Bind restricts declared actions → Enslave/Absolute Control requests an encounter-permitted outcome.
- **Affinity build → specialized attack:** body-part affinity and a declared attribute profile make Bl-job, Paizuri, Deepth, Spank, and Bite valid alternative investments without requiring unique effect code.
- **Exposure → Resolve → reaction:** Get Spanked deliberately accepts a qualifying event → generates Resolve → Counter or Turn the Tables spends/reacts to that opportunity.
- **DoT → vulnerability → exploitation:** Bend/AS applies persistent Strain pressure → Sensory Enhancement exposes a named channel → Exploit Weakness or a threshold action converts the opening.
- **Capability → focused follow-up:** P-growth grants a stable capability → Penetrate becomes available; A-penetration adds a defined control/Break rider; F-fk adds a capped low-Vitality target condition.
- **Control → outcome request:** Bind/Hypnotize create a defined control state → Command/Break investment may enable Enslave or Absolute Control, subject to encounter eligibility and resistance.

## 6. Decisions requested before numerical balancing

### Decision 1 — Similar basic attacks
**Recommended: B.** Keep separate skill records where per-skill body-part affinity/scaling and progression are intended build choices, but share the same effect template.

- A. Merge mechanically identical basic attacks into one skill with presentation variants; affinity does not justify separate unlocks.
- **B. Shared effect template, separate unlockable skills when scaling/affinity creates a meaningful build choice.**
- C. Separate only if each has an additional unique status, resource hook, risk, or tactical rule; scaling alone is not enough.

### Decision 2 — Spank and Bite
**Recommended: B.** Give each one clear primary channel and only add a second channel as an explicit conditional rider.

- A. Both always deal Strain and Vitality damage.
- **B. Each has one primary damage channel; any second channel is conditional and explicitly ordered.**
- C. One is Strain-focused and the other Vitality-focused.

### Decision 3 — Flirt
**Recommended: A.** Make it the basic Command generator; keep Hypnotize as direct control.

- **A. Generate Command, with negligible/no direct damage.**
- B. Deal Strain damage; another skill generates Command.
- C. Generate Command and deal full Strain damage, accepting that it may be overtuned unless costs/setup constrain it.

### Decision 4 — Lay and Facesit risk
**Recommended: B.** Only apply self-risk when it is an explicit mechanical trade-off.

- A. Both are reliable focused attacks without self-risk.
- **B. Self-risk only on the action whose fantasy/identity requires it, with a declared payoff.**
- C. Both are exposure actions that generate Resolve or another resource.

### Decision 5 — AS versus Bend
**Recommended: A.** AS stays separate only as a Chain/sequence skill with reset conditions.

- **A. Keep AS as a Chain mechanic; otherwise merge it into Bend.**
- B. Merge both into one DoT skill.
- C. Keep both as independent DoTs with different duration/stacking profiles.

### Decision 6 — H-job body-part field
**Recommended: A, pending your intent.** Change the legacy Mind tag to a physical body-part affinity; reserve Mind for an actual mental/psychic interaction.

- **A. Correct the body-part field to a physical part (please specify if you have a preference).**
- B. Keep Mind because the intended mechanic targets a mental/sensory Aspect, and revise the description/effect accordingly.
- C. Leave it unresolved until visual/animation design.

## 7. Not yet approved

- Attribute coefficients/curves, affinity multipliers, hit formulas, costs, and caps.
- Exact unlock tiers/prerequisites.
- Whether affinity alone warrants separate Skill Point costs.
- Final choice of damage channels for Spank/Bite/Facesit and related attacks.
- H-job's intended body-part/Aspect.
- P-growth target scope, persistence, and revocation.
- Final merges between Flirt/Command, Bend/AS, and similar basic-action variants.

## 8. Acceptance criteria for the next pass

Before numeric balance:
- Every focused action has an unambiguous actor, target, channel, and effect order.
- Each scaling profile identifies attribute contributors and body-part affinity without invented universal mappings.
- Similar skills are either justified as distinct build choices or marked for consolidation.
- Control states, DoTs, vulnerability, and resource triggers use registered deterministic effect semantics.
- All skill records point to stable scaling/effect/targeting references when the catalog schema migration begins.
