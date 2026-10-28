# AHTW — Content Writing Review Pack

**Audience:** quest writer, dialogue writer, editor, localization writer, narrative implementer.  
**Purpose:** establish voice, scene structure, choice-writing rules, and the boundary between prose and game state.

## 1. Writing mission

Write a grounded, compassionate fantasy RPG about community survival, institutional trade-offs, relationships and the difficult work of distributing responsibility. The prose should make social and material conditions specific; the Ferida complicates these conditions but does not explain them away.

The target is not constant melodrama. Let people be practical, tired, funny, defensive, mistaken, competent or conflicted in ordinary ways. Reserve speeches for moments that earn them.

## 2. Voice and dialogue principles

- Character voices should reflect goals, knowledge, social position, temperament and relationship—not merely exposition duties.
- Disagreement should be about evidence, priorities, risk and values. Do not flatten the Organization into villains or community members into moral mouthpieces.
- Let subtext do work. Avoid having every character explain the theme directly.
- Alya's past is suggested early through reactions and omissions; avoid premature exposition.
- The First Ally often notices patterns and practical implications, not just agrees with Alya.
- Cuidadora distinguishes care, stabilization, diagnosis, and recovery; she is compassionate without promising that care can erase consequences.
- The Pragmatic Mentor respects evidence and contingency. The Institutional Representative argues from downstream risk and protocol. Neither should be a caricature.
- Mara Venn accepts responsibility for concealing her choice while explaining the structural conditions that shaped it. Do not write her as either wholly innocent or solely guilty.
- Residents remember past allocation decisions; the crisis did not begin when the Red Thread appeared.

## 3. Choices and branching

- Choice labels must state the player's intended action or priority plainly.
- Do not label choices as good/evil or hide a radically different intention behind a neutral-sounding label.
- Consequences can be uncertain, but the player's intent must not be deceptive.
- A choice should alter a downstream flag, relationship, resource, encounter condition, line variation, recruitment condition, or unlock if the design promises a consequence.
- Do not reverse mandatory story states through optional dialogue. The lower-terrace seed reserve loss in Act I is canonical and unavoidable.
- Keep display text separate from stable IDs. Never use dialogue strings as identity keys.
- When a choice's effect is unclear, flag it for design review rather than inventing state logic in prose.

## 4. Scene-writing workflow

For each scene or quest stage, define:
1. Stable quest/scene/line/choice IDs.
2. Narrative purpose and what changes by the end.
3. Entry conditions and relevant known facts.
4. Characters present and each one's immediate goal.
5. Dialogue beats and optional lines.
6. Choice labels and intended player meaning.
7. Consequence mapping (state, relationship, encounter, reward, unlock).
8. Exit conditions and next stage.
9. Required/optional asset needs.
10. Localization notes and any context needed for short UI strings.

Write prose only after the stage's dramatic function and consequence are clear. Keep IDs in structured data; don't create competing IDs in a prose-only document.

## 5. Act I reference example

In **“The Water We Share,”** the story begins with an empty cistern, accusations against irrigation keeper Mara Venn, and red growth moving around an old water path. The first scene offers three priorities: maintain ration order, share remaining clean water, or delay judgment pending evidence. None is a simplistic morality score.

Later, the Organization proposes closing the lower sluice, isolating exposed workers and burning the root-vault to reduce downstream contamination risk. The alternative is not “ignore the danger”; it is to gather local knowledge, stabilize workers, prepare the channel and coordinate the gate operation. The climax requires an objective, not just defeating enemies. The community survives, but the seed reserve is lost.

The approved first-pass dialogue anchors are in `docs/vertical_slice/ACT_I_DIALOGUE_PACK.md`. They are implementation-ready placeholders, not immutable final prose.

## 6. Content scope and writing status

Full-game baseline:
- 5 acts;
- 47 main quest stages;
- 25 authored sidequests;
- 7 regions and 6 factions;
- 10 recruitable allies;
- 21 named recurring NPCs plus 12 reusable NPC templates;
- 5 ending families.

The content lock defines stage identity, major beats and scope. It does **not** mean all dialogue, branch lines, quest objective text, rewards or localization strings are finished.

## 7. Adult themes and character agency

- All characters are adults and should be presented unambiguously as adults.
- Adult/intimate content is optional, consent-aware and not required for main quest completion, recruitment, or endings.
- Do not treat rescue, rehabilitation, corruption, power imbalance, institutional harm or a character's vulnerability as automatic consent.
- A character's sexual presentation does not determine personality, morality, consent, or narrative function.
- Do not use intimate scenes to erase trauma or bypass relationship development.
- Flag content that needs rating, consent, localization or production review.

## 8. Localization and implementation constraints

- Stable IDs are the identity; localized strings are presentation.
- Keep UI labels concise and context-rich; avoid relying on English wordplay for critical instructions.
- Separate narration, dialogue, choice labels, tooltips, quest objective text and system messages.
- Preserve speaker intent and relationship subtext across localization.
- Do not hard-code line text into game-state logic.
- Mark variables/placeholders and provide context for strings with ambiguous gender/number.
- Do not promise a runtime behavior, reward, or unlock in prose unless the design/data specifies it.

## 9. Review checklist

- Does every scene change knowledge, relationship, pressure, commitment or state?
- Is each character speaking from their own goals and information?
- Are choices honest and distinct in intent?
- Does every promised consequence exist in design/data?
- Is the mandatory loss preserved?
- Are the Organization and community both credible?
- Does the Ferida influence without absolving responsibility?
- Are optional adult themes kept separate from required progression?
- Can strings be localized without breaking logic or UI?

## Canonical references

- `docs/NARRATIVE_CANON.md`
- `docs/FULL_GAME_CONTENT_LOCK.md`
- `docs/vertical_slice/ACT_I_DIALOGUE_PACK.md`
- `docs/vertical_slice/ACT_I_QUEST_GRAPH.md`
- `docs/vertical_slice/ACT_I_QUEST_GRAPH_CONTINUATION.md`
- `data/vertical_slice/act_i_quests.json`
- `data/content/full_game_world_catalog.json`
- `docs/characters/CHARACTER_BIBLE.md`
