# Alya Heals the World — Character Bible

## Status
**Character Content Audit — Conceptually LOCKED.** This document consolidates the current character-identity rules and the canonical concrete NPC roster. Recruitable allies remain sourced from `ALLIES_ROSTER.md`; NPC architecture remains sourced from `NPCS_DESIGN.md`.

## Global Character Identity & Visual Safety Rules

1. **All characters are adults.** Every character must have an unambiguous adult visual read. Young-adult characters must still look clearly adult.
2. **No child-coded body archetypes.** `petite` is not a valid character-design category. Do not use infantilized proportions or minor-coded presentation, including loli/shota or adolescent-coded visual language.
3. **Adult body diversity is encouraged.** Slim, athletic, curvy, voluptuous, muscular, tall, average-height and mature silhouettes are valid when clearly adult.
4. **Humanoid fantasy first.** AHTW is not a furry-focused setting. Beastfolk/animal-derived species are minority elements and remain clearly humanoid rather than animal-dominant.
5. **Avoid beastfolk saturation.** Prefer Human, Elf/subspecies, supernatural humanoid and other humanoid species where appropriate.
6. **Species, culture and function are independent axes.** Species must not automatically determine faction, culture, personality or gameplay role.
7. **Subspecies may be visual/cultural only.** `Desert Elf` is a visual/cultural subspecies of Elf with no mechanical differentiation.
8. **Visual taxonomy does not create unnecessary mechanics.** Purely visual/cultural distinctions do not create new stat, aptitude, combat or progression branches unless a later system decision explicitly requires it.
9. **Character reference requirements.** For each Named character, the production reference should record at minimum: species/subspecies, presentation, adult age bracket, height class, body type, distinctive visual traits and relevant visual-generation constraints.
10. **Presentation is not age.** Feminine, Futanari and Femboy are presentation categories and never imply a younger age bracket.

## Canonical NPC Roster — C4

Target finalized at **21 Named recurring NPCs**. The roster deliberately does not maintain an arbitrary count; `Wanderer` was removed because its narrative concept overlaps the already-locked First Ally.

| ID | Concept | Faction / Scope | Species | Presentation | H Tier | Core function |
|---|---|---|---|---|---|---|
| NPC-001 | Tavernkeeper | Community | Human | Futanari | H3 | Tavern, social hub, rumors and community information |
| NPC-002 | Dancer | Community | Desert Elf | Feminine | H2/H3 | Entertainment, social events and world-event participation |
| NPC-003 | Community Elder | Community | Human | Feminine | H3 | Community memory, mediation and historical context |
| NPC-004 | Mediator | Community | Human | Futanari | H2/H3 | Interpersonal disputes and community mediation |
| NPC-005 | Pragmatic Mentor | Organization | Human | Feminine | H3 | Practical institutional guidance and training |
| NPC-006 | Institutional Representative | Organization | Human | Femboy | H3 | Formal organizational interface, supervision and negotiation |
| NPC-007 | Ferida Researcher | Organization | Augmented | Feminine | H3 | Ferida research, investigation and specialist information |
| NPC-008 | Hardliner | Organization | Human | Futanari | H3/H4 | Institutional opposition, enforcement and political pressure |
| NPC-009 | Regional Authority | Regional Center | Angel | Feminine | H3 | Regional governance and political legitimacy |
| NPC-010 | Trade Representative | Regional Center | Lamia | Futanari | H2/H3 | Trade, routes, commerce and regional opportunities |
| NPC-011 | Priestess | Regional Center | Human | Feminine | H3 | Spiritual community, compassionate counsel and rites |
| NPC-012 | Tribal Matriarch | Tribe A | Mycelia | Feminine | H3 | Tribal leadership, spiritual authority and culture |
| NPC-013 | Tribal Guide | Tribe A | Mycelia | Futanari | H2/H3 | Exploration, cultural mediation and tribal guidance |
| NPC-014 | War-Chief | Tribe B | Orc | Futanari | H3 | Strength/status culture, duels and rites of passage |
| NPC-015 | EnemyCommander | Adversarial | Human | Futanari | H3/H4 | Recurring faction commander; separate Enemy/Boss representation |
| NPC-016 | Faction Dissident | Adversarial | Human | Femboy | H3 | Internal faction conflict and alternative perspective |
| NPC-017 | Ferida Manipulator | Adversarial | Fallen Angel | Feminine | H4 | Major Ferida-linked antagonist and psychological manipulation |
| NPC-018 | Reaper | World | Dullahan | Feminine | H3/H4 | Neutral mystery, death/threshold themes and recurring encounters |
| NPC-019 | Dryad | World | Dryad | Feminine | H3 | Nature, exploration and multi-function quest hooks |
| NPC-021 | Survivor | World | Orc | Futanari | H2/H3 | Vulnerability, recovery and consequences of regional conflict |
| NPC-022 | Demonkin | Demon / World | Demon | Futanari | H3/H4 | Rescue, rehabilitation and legacy conflict |

`NPC-020 Wanderer` is intentionally retired and must not be recreated as a separate Named identity without a new narrative/system justification. The First Ally already owns the lost-group/wanderer concept.

## Species / setting decisions

- **Tribe A = Mycelia.** Tribe A is a distinct species-based tribal society with matriarchal spiritual organization.
- **Tribe B = Orc.** Tribe B is a distinct species-based tribal society centered on strength, status, duels and rites of passage.
- The two tribes therefore remain mechanically and culturally distinguishable without requiring every tribe member to receive unique mechanics.
- **Desert Elf** is an Elf subspecies distinguished visually/culturally, not mechanically. Darker skin and an athletic adult body are part of the Dancer's visual direction.
- Existing CSV species/concepts are treated as seeds rather than mandatory limits. The current enemy catalog includes Mycelia, Augmented, Minotaur, Orc, Dullahan, Angel, Fallen Angel, Lamia and Demon among other concepts; this supports a humanoid/supernatural-heavy roster without forcing beastfolk saturation.

## Cross-roster audit

The 21-NPC roster complements the 10 locked recruitable allies rather than replacing them.

- **Combat boundary:** NPCs never participate in combat while functioning as NPCs. Enemy/Boss representations are separate when a narrative identity requires combat representation.
- **Ally boundary:** persistent combat-capable community identity remains concentrated in the recruitable ally roster.
- **Functional overlap:** NPCs may perform services that overlap with ally community functions, but must not erase a distinctive ally identity.
- **Species balance:** the NPC roster is intentionally human/humanoid/supernatural-heavy, with beastfolk-like species limited to a small minority.
- **Visual safety:** no `petite` category; no child-coded proportions; all characters require an unmistakably adult read.
- **Relationship density:** only meaningful recurring relationships should receive dedicated treatment; avoid a complete matrix by default.
- **H-content:** tier is relevance-driven; H4 is reserved for major NPCs and dedicated CG scope.

## Production fields still downstream

The following are implementation/production data and do not reopen the conceptual roster by themselves:

- Stable data schema and final machine IDs.
- Exact base stats and growth values for recruitable allies.
- Exact NPC relationship variables and state transitions.
- Recruitment, rehabilitation and quest-state implementation.
- Exact H scene definitions, triggers and asset dependencies.
- Final visual references, portraits, sprites, CGs and asset IDs.
- Dialogue, localization and voice/audio mapping.

## Lock verdict

**Character Bible conceptually LOCKED.** The next work should proceed downstream into concrete data, quest hooks, relationship states, visual references and production assets. Reopen the character roster only when a concrete narrative/system gap is demonstrated.
