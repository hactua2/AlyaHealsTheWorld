# Status Effects and Lifecycle

## Source of truth
Stats and effects must have one canonical source. Do not duplicate the same modifier in equipment, status, and cached state.

## Effect lifecycle
An effect has source, target, start rule, duration, stacks, strength, tags, and removal conditions.

At the beginning of the affected character's turn:
1. evaluate start-of-turn behavior;
2. decrement duration when the effect uses turn duration;
3. expire the effect immediately when its duration reaches its expiration condition;
4. recompute derived state if required.

## Stack policy
Different effects are processed independently in application order. Equivalent effects keep only the strongest active instance unless the effect definition explicitly allows stacking.

## Equipment rule
Removing equipment immediately removes every effect granted solely by that equipment. Recalculate derived stats immediately.

## Passive categories
CorePassive: persistent identity behavior.
BuildPassive: learned or selected build behavior.
ConditionalPassive: equipment, state, encounter, or context dependent.

## Implementation events
Effect application and removal should emit deterministic events so UI, logs, triggers, and reactions can subscribe without duplicating logic.