# Skill Catalog Framework

The skill catalog is the concrete data source for skills. It uses shared tags, declarative requirements, and reusable effect primitives rather than bespoke behavior.

## Source-of-truth hierarchy
1. `data/skills/skills.csv`: primary concrete inventory, stable IDs, tier, requirements, categories, and links to mechanics/presentation.
2. Companion skill-definition files: complex ordered effects, formulas, targeting rules, requirement graphs, or reusable effect sequences that are unsuitable as opaque CSV strings.
3. This file: schema and constraints.
4. `implementation_spec/COMBAT.md`, `STATUS_EFFECTS.md`, `TURN_RESOLUTION.md`, `CONTENT_CONTRACTS.md`, and `PROGRESSION_AND_GATING.md`: runtime semantics and shared contracts.

Descriptions and display labels are not runtime source-of-truth. Presentation names may be localized or themed independently from stable IDs.

## Approved functional families
- Control: generate/spend Command, alter intent or resistance, and prepare Break.
- Reactive: convert a declared recent event or exposure into a response.
- Fortification: mitigate damage and generate/spend Fortitude.
- Exploitation: gain bonuses against tagged states/aspects or convert damage channels.
- Recovery: reduce Strain or remove selected negative effects.
- Support: improve an ally's next action or grant a tactical action only when action-economy rules permit it.
- Overflow: transform a declared Overflow condition into a defined effect.
- HighRisk: creates significant impact on both sides and must include counterplay/eligibility constraints.
- Damage, Debuff, Mobility/Positioning, Utility, Finisher, Passive, Capability/Transformation: additional functional tags where relevant; these are tags, not rigid classes.

## Canonical neutral IDs for the fourteen approved additions
- `SKILL_PROVOKE`
- `SKILL_ENDURE`
- `SKILL_COUNTER`
- `SKILL_COMMAND`
- `SKILL_RECOVER_COMPOSURE`
- `SKILL_EXPLOIT_WEAKNESS`
- `SKILL_BREAK_RESISTANCE`
- `SKILL_TURN_THE_TABLES`
- `SKILL_FOCUS_SURGE`
- `SKILL_DIRECT_ALLY`
- `SKILL_ABSOLUTE_CONTROL`
- `SKILL_UNBROKEN`
- `SKILL_OVERFLOW_ENGINE`
- `SKILL_MUTUAL_RUIN`

These IDs are proposed canonical identifiers; use them in production data only when the corresponding reconciled skill record is approved. Display names may differ.

## Required schema

Every CSV record must support these logical fields. Fields with complex nested data may point to companion definitions by stable ID.

| Field | Requirement |
|---|---|
| `id` | Required, unique, stable ID such as `SKILL_PROVOKE`. |
| `display_name` | Required presentation label; not used as identity. |
| `kind` | Required: Active, Passive, Capability/Transformation, or another explicitly registered kind. |
| `tier` | Required for tiered skills; Tier 1, Tier 2, or Tier 3. A deliberately untiered definition must state why. |
| `skill_point_cost` | Required numeric unlock cost. |
| `requirements_ref` | Required reference to declarative requirements; use an explicit no-requirements value when none apply. |
| `milestone_gate` | Optional milestone/content gate reference. |
| `family_tags` | Required normalized tags, not prose. |
| `targeting_ref` | Required target query/reference. |
| `resource_costs` | Structured costs for meters/resources. |
| `generated_resources` | Structured resource generation. |
| `conditions_ref` | Optional condition definition. |
| `effects_ref` | Required ordered effect definition/reference. |
| `cooldown` | Explicit numeric value or explicit no-cooldown value. |
| `chain_rule_ref` | Optional Chain definition. |
| `threshold_rule_ref` | Optional Threshold definition. |
| `overflow_rule_ref` | Optional Overflow definition. |
| `outcome_interactions` | Declared interaction with Defeat, Disable, Capture, Yield, Retreat, or ObjectiveComplete. |
| `aspect_tags` | Optional target-domain tags such as Body Part, Mind, or other supported Aspect. |
| `presentation_ref` | Optional icon, cut-in, animation, VFX, SFX, localization, and descriptive text reference. |

The physical CSV header may use compact names, but it must map unambiguously to this logical schema. Avoid storing arbitrary nested JSON in a single cell when a stable companion ID will be clearer.

## Canonical meter migration rules

- Legacy `H-gauge` maps to canonical `Strain`.
- Legacy `Health Damage` maps to damage to `Vitality`.
- These are vocabulary mappings, not blind text substitutions. Every legacy effect must be checked for target, direction, timing, scaling, mitigation, duration, stacking, trigger ordering, and encounter-outcome semantics.
- If a legacy description combines Strain damage, Vitality damage, state changes, or an outcome, split it into explicit ordered effects.
- Overflow is the defined condition/event associated with Strain exceeding its limit; it is not an independent meter unless a separate rule explicitly introduces one.
- “Heal” must resolve to a specific operation: restore Vitality, reduce Strain, or remove eligible effects.

## Capability/Transformation contract

A Capability/Transformation is a registered skill kind or a skill carrying that explicit kind. It grants a stable capability tag and changes eligibility for skills/actions/content. It is not assumed to be a temporary status effect.

Every capability definition must declare:
- capability ID/tag granted;
- actor/target scope;
- acquisition requirements, tier/cost, and optional milestone gate;
- persistence and save/load behavior;
- removal/revocation conditions, if any;
- dependent skill/content references;
- interactions with cleansing, dispelling, transformation, equipment, and character configuration.

P-growth is the current example. The proposed stable capability is `CAPABILITY_P_GROWTH`; Autof, F-fk, Penetrate, and A-penetration are dependency candidates. Target scope and persistence still require content confirmation.

## Requirements and progression

Unlocks combine Skill Points, declarative prerequisites, and optional milestone/content gates. Requirements use the shared predicates and logical composition defined in `CONTENT_CONTRACTS.md` (AllOf, AnyOf, NoneOf, Not). Use milestone gates when early access would destabilize pacing or when a skill represents a capability discovered in the world. Avoid arbitrary level-only rules and hidden mandatory requirements.

Tiers represent both progression expectation and expected power:
- Tier 1: foundational and reliable, early access, limited setup.
- Tier 2: specialization, synergy, or efficiency requiring meaningful investment.
- Tier 3: build-defining impact, major conversion/utility, or exceptional risk/reward.

Tier is not a damage ranking. Compare reliability, action economy, cost, setup, flexibility, encounter relevance, and availability.

## Approved shared primitives
Use existing deterministic effects and resource rules, including ModifyMeter, ModifyResource, ApplyEffect, RemoveEffect, AddStack, RemoveStack, ModifyStat, ChangeIntent, ChangeState, GrantCapability, and UnlockContent. Any additional effect type requires a stable type ID and deterministic handler.

## Validation requirements

A catalog validator should reject:
- duplicate/missing IDs or display names;
- invalid tier/kind values;
- negative or missing costs where required;
- unresolved requirement/effect/targeting/presentation references;
- unregistered family or Aspect tags;
- malformed resource expressions;
- passive definitions that duplicate the same modifier already owned elsewhere without an explicit stacking rule;
- finisher or defeat-prevention effects that bypass encounter outcome contracts;
- action grants that violate action economy;
- named rows with missing required fields;
- Capability/Transformation definitions with missing granted tags, target scope, persistence/removal policy, or dependent references;
- Overflow effects without trigger scope, recursion/cap behavior, or deterministic event ordering;
- migrated legacy skills whose Strain/Vitality mapping has not been semantically reviewed.

A skill should reuse shared primitives before introducing a custom mechanic.
