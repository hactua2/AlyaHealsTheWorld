# Turn Resolution Contract

This document defines the canonical order for turn-based encounter resolution.

## Turn phases
1. Select next active actor according to initiative/order rules.
2. Emit TurnStarted(actorId).
3. Resolve start-of-turn effects in deterministic application order.
4. For each affected effect using turn duration, decrement duration after its start behavior resolves.
5. Remove effects whose expiration condition is now satisfied; emit EffectRemoved.
6. Recalculate affected derived state.
7. If the actor is unable to act, resolve the defined skip/forced-action behavior and continue to phase 12.
8. Refresh or expose actor intent when the actor is AI-controlled.
9. Select an action; validate targeting, conditions, cooldown, costs, and gate requirements.
10. Commit costs, then resolve the action through its declared effect sequence.
11. Resolve triggered reactions, chains, thresholds, resource generation, and immediate outcome checks in deterministic order.
12. Resolve end-of-turn effects and emit TurnEnded(actorId).
13. Evaluate encounter terminal conditions. If none apply, advance to the next actor.

## Action resolution
An action is atomic from the perspective of validation: invalid actions must not partially spend costs or mutate state.

Recommended sequence:
Validate -> CommitCosts -> ApplyPrimaryEffects -> ApplySecondaryEffects -> EvaluateTriggers -> RecalculateDerivedState -> EmitEvents -> EvaluateOutcome.

## Ordering rules
- Application order is the default tie-breaker for equivalent priorities.
- Explicit priority overrides application order only when declared by data.
- Reactions created by an event resolve after the event's originating mutation unless explicitly marked interrupting.
- Terminal encounter outcomes stop further ordinary action resolution after the current atomic action completes.

## Required event payload minimum
Every turn/action event should include encounterId, actorId, sequenceNumber, eventType, and enough references to reproduce the state transition in logs.

## Determinism
Given identical canonical state, action selection, random seed/state, content version, and event ordering rules, resolution must produce identical canonical results.