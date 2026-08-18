# Translated Item Content

## Translation scope

Items preserve stable item identity, mechanical stat changes, secondary-trait changes, evolution behavior, removal restrictions, and supported conditional effects. Source names and descriptions that encode theme-specific presentation are replaced by neutral IDs where necessary.

## Stable slot IDs

Source slot labels map to stable internal IDs:

- `Accessories` -> `SLOT_ACCESSORY`
- `Bottom1` -> `SLOT_EQUIPMENT_A`
- `Bottom2` -> `SLOT_EQUIPMENT_B`
- `Tattoo` -> `SLOT_MARK`
- `Key Item` -> `SLOT_KEY_ITEM`
- `Top` -> `SLOT_EQUIPMENT_C`

Display names are configurable and do not define mechanics.

## Item records

| Neutral ID | Slot | Primary effects | Secondary effects | Progression | Functional special effect |
|---|---|---|---|---|---|
| ITEM_CRUX_ENLIGHTENMENT | ACCESSORY | Soul+, Body+ | TraitD+ | None | Increase Health damage dealt |
| ITEM_STAT_AMULET | ACCESSORY | Variable stat modifier | — | None | — |
| ITEM_STAT_RING | ACCESSORY | Variable stat modifier | — | None | — |
| ITEM_OATH | EQUIPMENT_A | Body+ | TraitC+ | Blessed/evolving | Restore Health when receiving qualifying attacks |
| ITEM_RESTORATION | EQUIPMENT_A | Soul+, Body+ | TraitC+ | None | Remove stat debuffs when Moral overfill occurs |
| ITEM_FOCUS_01 | EQUIPMENT_A | Soul+ | TraitC+ | None | — |
| ITEM_FOCUS_02 | EQUIPMENT_A | Soul+ | TraitC+, TraitB+ | None | — |
| ITEM_CONFINEMENT | EQUIPMENT_B | Agility+ | TraitC+, TraitB+, TraitD-, TraitA- | Cursed/evolving; restricted removal | Moral increases when taking Health damage |
| ITEM_RESTRAINT | EQUIPMENT_B | Agility+ | TraitB+, TraitD+ | None | Restricts a source-specific action category; exact neutral action mapping remains unresolved |
| ITEM_WARD_RESTRAINT | EQUIPMENT_B | Charm+, Soul+ | TraitB+, TraitD+ | Blessed/evolving | Same action restriction as ITEM_RESTRAINT |
| ITEM_PRIVATE_TIME | KEY_ITEM | — | — | None | Enables a source-specific recovery/activity action; neutral subsystem mapping pending |
| ITEM_PRIVATE_TIME_ENHANCER | KEY_ITEM | — | — | None | Enhances ITEM_PRIVATE_TIME action |
| MARK_REPROGRAMMING | MARK | Charm+, Agility- | TraitC+, TraitB+, TraitD-, TraitA- | Cursed/evolving; restricted removal | Reduces ability to refuse/resist qualifying requests or attacks |
| MARK_RECEPTACLE | MARK | Charm+ | TraitC+, TraitB+ | Cursed/evolving; restricted removal | Increases Moral damage taken; grants temporary escalating stat buffs after a qualifying fill state |
| MARK_CANVAS | MARK | Charm+, Body+ | TraitC+, TraitB+ | Cursed/evolving; restricted removal | Increase damage resistance |
| MARK_ABANDON | MARK | Charm+, Soul- | TraitB+, TraitA- | Cursed/evolving; restricted removal | Increase stats when debuffed |
| MARK_MINDMELT | MARK | Charm+, Soul- | TraitC+ | Cursed/evolving; restricted removal | Apply debuffs when a qualifying Moral-positive event occurs |
| MARK_SWAY | MARK | Charm+, Body+ | TraitD+ | Blessed/evolving | Deal Moral damage to nearby targets |
| MARK_SIPHONING | MARK | Charm+ | TraitD+ | Blessed/evolving | Stats increase as Moral fills |
| MARK_CONDITION_01 | MARK | Charm+ | TraitC+, TraitD- | Cursed/evolving; restricted removal | Requires source-specific prerequisite state; neutral mapping unresolved |
| ITEM_PEARLS | EQUIPMENT_C | Charm+ | TraitC+, TraitB+ | None | Increase Moral damage dealt and received |
| ITEM_PIERCING_01 | EQUIPMENT_C | Charm+ | TraitC+, TraitB+ | None | — |
| ITEM_RING_SET | EQUIPMENT_C | Charm+ | TraitC+, TraitB+ | None | — |
| ITEM_CHAIN | EQUIPMENT_C | Charm+ | TraitC+, TraitB+ | None | — |
| ITEM_CHARM_FOCUS | EQUIPMENT_C | Charm+ | TraitD+ | None | — |
| ITEM_WARD_CHARM | EQUIPMENT_C | Charm+, Soul+ | TraitB+, TraitD+ | Blessed/evolving | — |

## Canonical progression behavior

- `Blessed/evolving`: the source states the item evolves the longer it is used.
- `Cursed/evolving`: the source states the item evolves the longer it is used and cannot normally be removed.
- Exact stages, thresholds, formulas, and transformed record names are not defined here unless separately supported.

## Unresolved source-specific mechanics

The source contains several special effects whose literal framing does not reveal a complete neutral subsystem contract:

- the action restriction used by `ITEM_RESTRAINT` and `ITEM_WARD_RESTRAINT`;
- the activity enabled by `ITEM_PRIVATE_TIME` and enhanced by `ITEM_PRIVATE_TIME_ENHANCER`;
- the prerequisite referenced by `MARK_CONDITION_01`.

These effects are preserved as explicit data hooks rather than silently reinterpreted. They are not new canonical mechanics.
