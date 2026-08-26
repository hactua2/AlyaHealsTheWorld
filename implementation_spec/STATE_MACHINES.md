# State Machines

Use explicit state machines for systems with branching lifecycle. Do not encode lifecycle transitions only through scattered booleans.

## Encounter
Available -> Entering -> Active -> ResolvingOutcome -> Resolved | Retreated | Failed

Rules:
- Available encounters may validate requirements before Entering.
- Active owns combat, social, ecological, or mixed interaction state.
- Retreat transitions through cleanup and consequence evaluation before Retreated.
- Terminal states are immutable except through explicitly defined content transformations.
- A resolved repeatable encounter may create a new Available instance with a different state or seed.

## Quest
Locked -> Available -> Accepted -> Active -> Branching -> Completed | Failed | Abandoned

Optional content states may include Suspended or Transformed.

Rules:
- Requirements control Locked -> Available.
- VisibleRewardHints are available before or during acceptance according to content configuration.
- Hidden rewards are never required for interface planning.
- Completed, Failed, Abandoned, and Transformed outcomes emit state-change events and may unlock content.

## Building
Locked -> Available -> Constructing -> Active -> Upgrading | Disabled | Reconfiguring

Terminal removal is optional content behavior and is not required by default.

Rules:
- Available means requirements are visible and construction can be attempted.
- Constructing validates and consumes costs atomically when construction starts unless content explicitly supports staged payment.
- Active exposes capabilities, processing, assignments, modules, and upgrades defined by content.
- Disabled preserves identity but suppresses capabilities according to its reason.

## Assignment
Unassigned -> Assigned -> Active -> Completed | Interrupted | Reassigned

An assignment instance stores start context, member IDs, task ID, timing model, and generated outputs/events. Reassignment must never delete accumulated aptitude or experience.

## Progression gate
Hidden -> VisibleLocked -> Satisfied -> Unlocked

A content entry may skip Hidden and begin VisibleLocked. A satisfied gate may unlock one or more capabilities, regions, resources, upgrades, or content entries.

## Region availability
Hidden -> KnownLocked -> Available -> Explored

Explored is not terminal. Regions may continue producing encounters and procedural instances unless content declares exhaustion or transformation.