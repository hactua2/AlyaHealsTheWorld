# Translated Enemy Content

## Translation scope

This document preserves the concrete enemy roster, faction/archetype, progression tier, and encounter role from the source. Weakness labels are translated into neutral internal affinity IDs while their final display names remain configurable.

## Stable affinity mapping

The source weakness categories map mechanically as follows:

- `Physical` -> `AFFINITY_PHYSICAL`
- `Magic` -> `AFFINITY_ARCANE`
- `Topping` -> `AFFINITY_STYLE_A`
- `Bottoming` -> `AFFINITY_STYLE_B`

`AFFINITY_STYLE_A` and `AFFINITY_STYLE_B` are deliberately provisional neutral IDs. Their future display names may change without altering enemy records, skills, saves, or combat logic.

## Enemy roster

| ID | Archetype | Tier | Encounter Role | Weakness Affinities |
|---|---|---|---|---|
| Guard | Civilized | 1 | Mob | STYLE_A, ARCANE |
| Slime | Savage | 1 | Mob | STYLE_B, STYLE_A, PHYSICAL |
| Cockatrice | Savage | 1 | Mob | STYLE_A |
| Warrior | Tribal | 1 | Mob | STYLE_A, ARCANE |
| Goblin | Tribal | 1 | Mob | STYLE_B, STYLE_A |
| Mycelia | Tribal | 1 | Quest Target | STYLE_A, PHYSICAL |
| Zombie | Undead | 1 | Mob | STYLE_A, PHYSICAL |
| Augmented | Civilized | 2 | Elite | ARCANE |
| Kunoichi | Civilized | 2 | Elite | STYLE_A, PHYSICAL |
| Krakenblood | Loner | 2 | Elite | STYLE_B, PHYSICAL |
| Kitsune | Loner | 2 | Elite | STYLE_B, STYLE_A |
| Barbarian | Tribal | 2 | Elite | STYLE_B, ARCANE |
| Royal Guard | Civilized | 2 | Mob | STYLE_B |
| Minotaur | Savage | 2 | Mob | STYLE_B, ARCANE |
| Wolfkin | Savage | 2 | Mob | STYLE_B, ARCANE |
| Orc | Tribal | 2 | Mob | STYLE_B, ARCANE |
| Haunt | Loner | 2 | Mob | STYLE_A, ARCANE |
| Witch | Loner | 2 | Quest Target | STYLE_B, STYLE_A, PHYSICAL |
| Mummy | Undead | 2 | Quest Target | STYLE_B, PHYSICAL |
| Dullahan | Undead | 3 | Quest Target | STYLE_B |
| Angel | Civilized | 3 | Quest Target | STYLE_A |
| Dragonkin | Loner | 3 | Quest Target | STYLE_B |
| Fallen Angel | Loner | 3 | Quest Target | STYLE_B, STYLE_A |
| Lamia | Loner | 3 | Quest Target | STYLE_A, PHYSICAL |
| Demon | Savage | 3 | Quest Target | PHYSICAL, ARCANE |

## Canonical implementation requirements

- Enemy ID is stable.
- Archetype/faction and tier are data fields.
- `Mob`, `Elite`, and `QuestTarget` are encounter roles, not display names.
- Weakness resolution depends on affinity IDs, never on source terminology or visual presentation.
- Enemy statistics and action lists are not invented here because the source leaves those fields empty.

## Surrender compatibility

Any enemy definition may support the global Moral-resolution pipeline: Moral defeat -> Surrender -> post-combat narrative resolution. The source roster does not define which enemies are recruitable; therefore recruitability remains unspecified unless defined elsewhere.
