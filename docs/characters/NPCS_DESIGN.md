# Alya Heals the World — NPC Design & Tier System

## Status
**C4 — Conceptually LOCKED.** Source of truth for NPC structure, production tiers and the canonical Named NPC roster. NPC relevance may be promoted/reduced later without redesigning the architecture.

## Core boundary: NPC vs Ally vs Enemy
- Recruitable allies are persistent special community members with meaningful combat and/or community identities; see `ALLIES_ROSTER.md`.
- **NPCs do not participate in combat while functioning as NPCs.**
- A narrative character may have a **separate Enemy/Boss representation** for an encounter. Once functioning as an NPC, that character no longer takes combat turns as an NPC.
- Exceptional NPCs may later become recruitable allies, but this requires a concrete narrative/system reason and is not the default.
- NPCs may be community residents and perform specialized services/functions, provided they do not invalidate distinctive ally identities.
- Autonomous activity without Alya is an **Expedition**; Sidequests require Alya/player participation.

## NPC taxonomy
NPCs use **independent tags**, not mutually exclusive categories. One NPC may be vendor + quest giver + faction representative + information source, for example.

### Named
Persistent, individually authored NPC with a stable identity and narrative purpose, even if small.

### Template
Reusable visual/social/function archetype with controlled variations.

### Background
Low-importance procedural or largely anonymous population for atmosphere/basic simulation.

## Population targets
- **Named recurring:** approximately 15–25.
- **Reusable templates:** approximately 8–15.
- **Background:** procedural/elastic; no quota.
- Dense hubs should contain substantial NPC presence; exploration should be punctuated by NPC encounters.
- Some recurring NPCs may change location according to state.
- One-off NPCs should exist moderately where quests/events justify them.

These are planning ranges, not quotas.

## Functional tags
**Mandatory:** Quest Giver; Quest Target; Vendor; Narrative Antagonist; Recruitment Candidate; World-event Participant.

**Desirable:** Information/Rumors; Faction Representative; Mentor/Trainer.

**Optional:** Authority; Specialist; Social/Relationship.

Tags may be expanded when later design reveals a real need.

## Services, community and progression
- NPCs may execute community functions, including specialized ones.
- NPC services may overlap with ally/community capabilities when they do not replace an ally's distinctive identity.
- Community coverage is not a one-character-per-facility checklist.
- NPC progression is lightweight: function/relationship state may improve, unlock or change, but NPCs do not use the allies' deep combat progression model.

## Relationships and persistence
- Named recurring NPCs can have meaningful relationships with Alya.
- Recurring NPCs can have relationships with one another.
- NPCs may leave the community/world under explicit conditions.
- Only selected named NPCs can die as narrative consequences.
- Recruitment conditions should be discoverable and clear once relevant, but need not always be immediately visible.
- Named NPCs use persistent stable IDs.

## Factions
- Target: approximately **4–6 factions**.
- Faction state combines reputation and narrative states.
- Important quest outcomes may absorb a faction/community into Alya's community.
- `EnemyCommander` is a recurring faction commander and may have both NPC and separate Enemy/Boss representations.
- Some antagonists are conversational rather than immediate combat encounters.

## Expeditions
- NPCs do not join combat as NPCs.
- Some NPCs can provide unique modifiers to autonomous Expeditions.
- NPCs cannot perform Sidequests independently of Alya.

## H-content tier system
H-content is **relevance-driven**, not mandatory for every NPC.

| Tier | Identity | H-content expectation |
|---|---|---|
| **H0** | Background | No individual H-content |
| **H1** | Template | No individual H-content; template-level implications only if later justified |
| **H2** | Named Functional | May receive light/relationship-driven H-content when appropriate |
| **H3** | Named Recurring | Can receive full individual H-content when relevant |
| **H4** | Major NPC | Full individual H-content; may receive dedicated CGs and bespoke presentation |

Dedicated CGs are reserved primarily for H4/most important NPCs. Promotion to a higher H tier later does not require architectural changes.

## Visual production rules
Named NPCs receive, when justified by importance: full visual reference, portrait, exploration/world sprite, and CGs when narrative/H importance warrants them. A battle representation exists only for a separate Enemy/Boss representation.

The global visual direction remains rigidly consistent with the project's extremely feminine aesthetic. NPCs should have substantially more species diversity than allies. Reusable templates are encouraged for lower tiers, with controlled variations.

## Visual Safety & Identity Constraints
These constraints apply globally to NPCs and should also be treated as a global character-design rule. They are duplicated in `CHARACTER_BIBLE.md` because the Bible is the production-facing identity source.

1. **Adult visual readability:** all characters are adults and must have an unambiguous adult visual read. Young-adult characters must still look clearly adult.
2. **No child-coded body archetypes:** do not use `petite` as a character-design category or intentionally infantilized proportions. Avoid loli, shota, childlike, adolescent-coded or otherwise minor-coded presentation.
3. **Adult body diversity:** acceptable silhouettes include slim, athletic, curvy, voluptuous, muscular, tall, average-height and mature bodies, provided the overall presentation remains clearly adult.
4. **No furry-first identity:** AHTW is a humanoid fantasy RPG, not a furry-focused setting. Beastfolk/animal-derived species are minority elements and should remain clearly humanoid rather than animal-dominant in visual identity.
5. **Species diversity without beastfolk saturation:** prefer Human, Elf/subspecies, supernatural humanoid and other established humanoid species where appropriate instead of defaulting to beastfolk.
6. **Species, culture and function are separate axes:** a character's species should not automatically determine their faction, culture or gameplay role.
7. **Subspecies may be visual/cultural only:** visual subspecies such as `Desert Elf` may exist without creating mechanical differentiation when the distinction is intended to be purely aesthetic/cultural.
8. **No mechanical inflation from visual taxonomy:** purely visual/cultural species or subspecies distinctions should not create unnecessary stat, aptitude, combat or progression branches.
9. **Character reference minimum:** each Named character's production reference must record species/subspecies, presentation, adult age bracket, height class, body type, distinctive visual traits and relevant generation constraints.
10. **Presentation is not age:** Feminine, Futanari and Femboy are presentation categories and never imply a younger age bracket.

## Canonical Named NPC roster
The finalized planning target is **21 Named recurring NPCs**. `NPC-020 Wanderer` was removed because the concept is already represented by the locked First Ally; it must not be recreated without new narrative/system justification.

| ID | Concept | Scope/Faction | Species | Presentation | H Tier | Core function |
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

IDs remain stable; the unused `NPC-020` slot is intentional after the Wanderer retirement.

## Species / culture decisions

- **Tribe A = Mycelia.** Distinct species-based tribal society with matriarchal spiritual organization.
- **Tribe B = Orc.** Distinct species-based tribal society centered on strength, status, duels and rites of passage.
- The two tribes remain species-distinct without requiring unique mechanics for every member.
- **Desert Elf** is a visual/cultural Elf subspecies. The Dancer has darker skin and an athletic adult body; there is no mechanical distinction from Elf.
- Existing CSV species/concepts are seeds rather than mandatory limits. The current enemy catalog includes Mycelia, Augmented, Orc, Dullahan, Angel, Fallen Angel, Lamia and Demon among other concepts, supporting a humanoid/supernatural-heavy roster without beastfolk saturation.

## Cross-roster audit

- **Combat boundary:** NPCs never participate in combat while functioning as NPCs. Enemy/Boss representations are separate when needed.
- **Ally boundary:** persistent combat-capable community identity remains concentrated in the 10 recruitable allies.
- **Functional overlap:** NPC services may overlap with ally community capabilities only when the ally's distinctive identity remains intact.
- **Species balance:** the NPC roster is deliberately human/humanoid/supernatural-heavy; strongly animal-derived species are a small minority.
- **Visual safety:** no `petite` category, no child-coded proportions, and every character requires an unmistakably adult visual read.
- **Relationship density:** dedicated relationship content is reserved for meaningful recurring connections rather than a complete matrix.
- **H-content:** H tier is relevance-driven; H4 is reserved for major NPCs and dedicated CG scope.

## Downstream production data
Stable IDs, exact relationship variables, recruitment/rehabilitation state machines, quest hooks, H scene definitions, dialogue, localization, visual references, portraits, sprites, CGs, asset IDs and audio mapping remain downstream specifications.

## Content-lock verdict
**C4 concrete NPC roster LOCKED. Character identity rules LOCKED.** Reopen the roster only when a concrete narrative/system gap is demonstrated.
