# Alya Heals the World — NPC Design & Tier System

## Status
**C4 — Conceptually LOCKED.** Source of truth for NPC structure and production tiers. Exact roster, numerical data, dialogue, quests and assets remain downstream. NPC relevance may be promoted/reduced later without redesigning the architecture.

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

## Legacy seed handling
Existing CSV concepts are seeds, not automatically canonized. Preserve only concepts that pass the C4 audit.

Current seeds requiring explicit audit:
- `Tavernkeeper` — must be part of the community.
- `Reaper` — neutral mysterious recurring NPC.
- `Dryad` — nature/exploration quest giver and recurring multi-function narrative character.
- `Priestess` — candidate NPC, subject to non-duplication audit.
- `Dancer` — candidate for social/entertainment/world-event use, subject to non-duplication audit.
- `EnemyCommander` — recurring faction commander; NPC + separate Enemy/Boss representation.
- `Demonkin` — prisoner/slave of a faction; central to the legacy rescue concept.
- `DemonAlly` — legacy rescue-quest seed associated with Demonkin; final entity structure remains downstream and should not assume two unrelated final characters.

Other legacy seeds that strongly overlap the locked ally roster should not be duplicated merely because they exist in the old CSV.

## Addition/removal rule
Create a new NPC when a clear narrative or system function benefits from a distinct entity. A quest may also legitimately create a new NPC when required by its story.

Do not create NPCs merely to hit a count, fill every facility, or duplicate an ally identity.

NPC relevance is deliberately **elastic**: an NPC may be promoted from Template/Background to Named, or from a lower Named/H tier to a more important role, when later evidence supports it. Such changes should primarily affect content/asset scope, not architecture.

## Cross-system constraints
- NPCs may provide services, relationships, quests, information, faction state, community functions and Expedition modifiers.
- NPCs do not use combat turns as NPCs.
- Separate Enemy/Boss representations are allowed for narrative characters.
- Recruitable allies remain the principal persistent combat-capable community characters.
- H-content follows the tier model rather than forcing bespoke assets for every NPC.
- Persistent IDs allow promotion/demotion and state changes without rewriting references.

## Content-lock verdict
**C4 is conceptually closed.** Remaining work is the concrete NPC roster and downstream implementation data: stable IDs, exact functions, faction assignments, recruitment candidates, quest hooks, relationship states, H tiers, dialogue, visual assets and asset IDs.
