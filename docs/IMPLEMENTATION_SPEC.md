# Implementation Specification — Final Integration Status

## Status
**I1–I11 COMPLETE · I12 COMPLETE**

This specification translates the locked game design into implementation contracts. The final integration audit found no blocking cross-system contradiction.

## Core integration rules

### Combat
- Initiative is randomized once at combat start, with Agility modifying the initial result; the resulting order remains stable.
- Turn start processes start-of-turn effects, duration update/expiration and derived-state recalculation before checking whether the actor can act.
- Surrendered and incapacitated combatants do not act and are represented separately from other character state.
- Combat terminates when all members of one team are Surrendered and/or Incapacitated.
- Atomic actions complete their declared resolution pipeline before terminal combat state is committed.

### Actions and effects
- Insufficient resources make an action unselectable.
- AI preserves its selected action/intent when a target becomes invalid and retargets where possible; invalid actions use an explicit fallback policy.
- Effects are instances with definition, source character/definition, duration, stacks and runtime state.
- Effects use configurable stacking policies and event-driven triggers.
- Trigger recursion is bounded by an execution budget.
- Effect provenance can reference a parent execution/effect without copying the full chain.

### Stats and HP
- HP represents physical exertion/exhaustion rather than literal wounds and may be spent by skills.
- HP is clamped to zero; no overkill state is required or persisted.
- Derived stats are invalidated by mutations and recalculated lazily when queried.
- Temporary modifiers are the shared mechanism for temporary item/buff/debuff/stat changes.

### Skills and targeting
- Gameplay, AI and presentation data are separated.
- Targeting is represented by composable queries with per-skill selection policies.
- Formulas are data-driven and use a constrained expression vocabulary.
- Modifier ordering follows the global deterministic formula policy.
- Minimum damage and accuracy rules follow the locked combat design.

### Equipment
- Equipment is exclusive to the protagonist; allied NPCs do not use equipment.
- Equipment changes occur outside combat.
- Equipment can declaratively transform supported skill properties such as targeting, formula or area behavior.
- Transformation conflicts use explicit priority.
- Cursed equipment uses curse definitions plus active effects and preserves curse state when unequipped.

### Character progression
- Characters have level and experience; level-up supplies skill points.
- Natural growth derives from recorded activity/use and periodic growth processing.
- Skill unlock requirements are data-driven and may include level, skill points, character conditions and community/event gates.
- Passives may be permanent or loadout-based according to definition.
- Aptitude is derived from species, attributes, experience and modifiers.

### Community
- Recruitment, eligibility and rehabilitation/integration are separate states/processes.
- Rehabilitation is progress-driven and can use facilities, assignments and events.
- Community members have availability/assignment states.
- Assignment interruption follows the defined progress/output policy.
- **Expedition = NPC-only delegated activity. Sidequest = activity requiring Alya.**

### Time and economy
- Time is represented internally with continuous timestamps.
- Day/night is a gameplay state and can gate availability.
- Time advancement processes intermediate timestamps chronologically; equal timestamps use explicit event priority.
- Waiting supports semantic and custom durations.
- Facilities, skills and statuses can modify recovery.
- Production and upkeep use the defined time/tick model.
- Inventory has no fixed capacity limit.

### Exploration and quests
- World navigation uses a regional/locality graph.
- Travel duration is affected by route and modifiers.
- Encounters use pools, conditions and weights.
- Sidequests require Alya; Expeditions use NPCs only and resolve through checkpoints.
- Quest state uses a graph with objective progress and configurable completion/failure policies.
- Retroactivity is objective-defined.
- World state includes global/local, quest, relationship and simulation state.
- Relationships support values, flags and stages.
- Choices can modify narrative, gameplay and world state.

### Persistence and determinism
- Saves persist everything required to reconstruct gameplay; reconstructible runtime state is not unnecessarily serialized.
- Combat is not saved mid-resolution.
- Autosave and manual-slot boundaries follow the established design.
- Save schema versioning is independent from general game versioning.
- Migrations are automatic and preserve the original save.
- Persistent randomness retains seed/RNG state and execution information sufficient to reproduce relevant bugs.
- Stable identifiers use semantic IDs plus immutable identity where required.
- Gameplay, balance, localization and presentation data remain separated.

### Cross-system architecture
The canonical sequence is:

`Canonical Mutation → Derived State → Domain Event → Event Handlers → Subsequent Canonical Mutation`

Events do not mutate an uncommitted transaction. Canonical multi-mutation operations are atomic by default, while content may explicitly define partial behavior where appropriate.

Each domain has an explicit source of truth. The specification defines contracts, data instantiates them, and runtime code implements them. New behavior requiring a capability not represented by the existing contracts must update the specification/schema rather than introduce ad-hoc special-case code.

## Production interpretation

The specification is closed for planning purposes. Numerical balance, content volume, asset production, implementation details and ordinary bugs remain production work. A discovery that requires a genuinely new gameplay rule reopens the relevant specification section and is recorded explicitly.
