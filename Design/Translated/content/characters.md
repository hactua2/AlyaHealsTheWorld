# Translated Character Content

## Translation scope

The source provides a concrete roster and relationship roles but leaves statistics, actions, weaknesses, and descriptions empty. This translation preserves only supported content.

## Character roster

| ID | Source role | Neutral implementation role |
|---|---|---|
| Ranger | Ally | Ally |
| WitchAlly | Ally that has quest | Ally; associated quest content |
| Dancer | Ally that has quest | Ally; associated quest content |
| Nun | Ally that has quest | Ally; associated quest content |
| Reaper | Neutral | Neutral NPC |
| Dryad | Neutral | Neutral NPC |
| Priestess | Quest Giver | Quest Giver |
| Faun | Quest Giver | Quest Giver |
| DemonAlly | Quest Giver | Quest Giver |
| Tavernkeeper | Quest Giver | Quest Giver |
| RebelCommander | Ally but requires quest | Quest-gated Ally |
| Wanderer | Ally but requires quest | Quest-gated Ally |
| Monk | Ally but requires quest | Quest-gated Ally |
| EnemyCommander | QuestTarget | Quest Target |
| Demonkin | QuestTarget | Quest Target |
| Alchemist | Quest Giver | Quest Giver |

## Canonical role interpretation

- `Ally`: available as an allied character according to the broader progression state.
- `AssociatedQuest`: the source establishes that the ally has quest content, but does not specify whether the quest is required for recruitment.
- `QuestGatedAlly`: availability requires completion or resolution of a quest condition.
- `NeutralNPC`: present in the world without an explicit ally/quest-giver role in the source.
- `QuestGiver`: supplies or initiates quest content.
- `QuestTarget`: target of quest content.

## Important limitation

The source does not define quest IDs, quest ordering, recruitment conditions for the three `Ally that has quest` entries, statistics, combat roles, dialogue, or relationships beyond the role labels above. Those details must remain unspecified until supported by another source or explicitly designed later.

## Presentation separation

Character names/IDs above are content identifiers from the source roster. Portraits, sprites, models, outfits, animations, voice, and sound bindings belong to presentation data and may be replaced independently.
