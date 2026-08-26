# Skill Catalog Framework

Skills are data definitions using shared tags and primitives rather than bespoke logic.

## Approved functional families
- Control: generate Command, alter target intent or resistance, prepare Break.
- Reactive: convert recent damage or exposure into a response.
- Fortification: mitigate damage and generate Fortitude.
- Exploitation: gain bonuses against tagged states or convert damage channels.
- Recovery: reduce Strain and remove selected negative effects.
- Support: improve an ally's next action or grant a tactical action.
- Overflow: transform excess Strain into offensive, defensive, healing, or resource effects.
- HighRisk: creates significant impact on both sides.

## Representative neutral skill IDs
Provoke, Endure, Counter, Command, RecoverComposure, ExploitWeakness, BreakResistance, TurnTheTables, FocusSurge, DirectAlly, AbsoluteControl, Unbroken, OverflowEngine, MutualRuin.

Presentation names may be localized independently from IDs.

## Skill schema minimum
id, familyTags, targeting, meterCosts, generatedResources, conditions, effects, cooldown, chainRule, thresholdRule, overflowRule, outcomeInteractions.

A skill should reuse shared primitives before introducing a custom mechanic.