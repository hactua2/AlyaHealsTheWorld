# AHTW — Full Game Content Lock

**Status:** Proposed canonical full-game content lock, authored under the project owner's standing instruction to accept recommendations by default. This document closes the *design/content-definition* layer for the base game. It does not claim runtime integration, final numerical balance, art production, localization, or QA completion.

**Authority:** Narrative canon and system contracts remain authoritative for behavior. This document is authoritative for the concrete base-game roster, act structure, content counts, names, narrative beats, unlock dependencies, and intended content coverage. Structured catalogs under `data/content/` carry stable IDs. If a catalog and this document disagree, stop and reconcile rather than silently inventing a third version.

## 1. Product scope and content promise

AHTW is a single-player, turn-based narrative RPG with light community/base management, adult characters and themes, exploration, direct sidequests, and autonomous NPC-only Expeditions. The base game contains five acts, one central home community that evolves politically and mechanically, a six-region cooperation network plus the starting region, ten recruitable allies, twenty-one named recurring NPCs, reusable population templates, a curated enemy/boss roster, and several world-state endings.

### Locked base-game targets

| Content family | Locked target | Notes |
|---|---:|---|
| Acts | 5 | Each has a distinct narrative and management purpose |
| Main quest stages | 45 | 9 per act; stable IDs in the world/narrative catalog |
| Authored sidequests | 25 | Five per act; procedural/repeatable activities are separate |
| Regions | 7 | One starting region + six later regions |
| Recruitable allies | 10 | Canonical roster already locked |
| Named recurring NPCs | 21 | NPC-020 intentionally remains unused; IDs are not recycled |
| Factions | 6 | Independent internal states, not a single reputation meter |
| Enemy archetypes | 35 | Includes the existing legacy types plus defined Ferida-specific roles |
| Major bosses | 9 | One or more per act; some story characters have separate combat representations |
| Special/mini-boss encounters | 8 | Reuse enemy families with encounter-specific rules |
| Facilities | 12 | One initial facility choice; other facilities unlock by progression |
| Resources | 8 | No inventory capacity ceiling |
| Canonical items/equipment | 36 | Legacy items are normalized into stable IDs; new entries fill functional gaps |
| Skill catalog | 67 canonical records | Existing normalized catalog; do not add skills merely to hit a quota |
| Alya outfit slots | 8 retained base outfits | Legacy candidates are reviewed; see section 10 |
| Main endings | 5 state families | Not a binary morality outcome; no exact ending percentages |

This is the intended **base-game** scope, not a promise that every record needs unique bespoke art. Variants should reuse family assets where readable and appropriate. Do not expand these counts without a demonstrated coverage gap.

## 2. Narrative spine and act locks

### Act I — Foundation: “The Water We Share”
**Region:** Ashfen Verge. **Hub:** Brackenford. **Ferida manifestation:** “The Red Thread.”

Alya arrives at Brackenford and becomes involved in a water-allocation dispute involving Mara Venn, the lower terraces, a failing sluice, and a seed reserve. Scarcity and unequal access existed before the Ferida appeared; the manifestation intensifies exhaustion, suspicion, and fixation rather than creating the dispute from nothing. The Organization offers a defensible containment plan that protects downstream settlements by sealing the lower sluice and sacrificing the root-vault. Alya helps construct a third option through local knowledge, repair materials, and coordinated care.

**Mandatory cost:** the lower-terrace seed reserve and a substantial part of the next planting cycle are lost. The downstream channel is protected for the present. No branch removes both costs.

**Act-end state:** Alya is recognized as Brackenford's leader; community management begins; one facility is selected; the first autonomous Expedition is unlocked. The ultimate nature of the Ferida and the full truth of Alya's past remain unrevealed.

### Act II — Construction: “A Place for the Uncounted”
**Region:** Greenwake Basin, with Brackenford as the home hub.

Brackenford grows into a refuge and training site. The player learns construction, production, aptitude-based assignments, rehabilitation, representation, and trade. A displaced group arrives after an official relocation order. Some residents fear resource pressure; others fear repeating the lower-terrace sacrifice. The Organization wants the community to become a replicable pilot and asks for standardization, monitoring, and controlled admissions.

Alya initially tries to personally resolve every dispute. This causes delays and undermines delegates. The act's central crisis concerns a mixed convoy of displaced people and an unstable Ferida-marked patient. The community creates a supervised, voluntary integration process with explicit limits and review rather than either indiscriminate acceptance or collective punishment.

**Point of no return:** Brackenford shelters a group the Organization has formally ordered relocated, after documenting the risk and arranging containment. This creates an institutional rupture without making all Organization members enemies.

**Act-end state:** the community becomes a semi-autonomous regional partner and establishes its first external agreements. Leadership is formalized through a council/delegate model rather than personal rule alone.

### Act III — Consequences: “The Cost of Being Free”
**Regions:** Glassstep March and Mycelian Reach.

Autonomy exposes the community to shortages, contradictory requests for aid, trade leverage, and political resentment. The player cannot maximize every region's welfare simultaneously. A trade blockade and a conflict between two tribal societies reveal that the cooperation network cannot be built by simply exporting Brackenford's rules.

The Organization's internal factions become explicit: pragmatists want evidence and negotiated safeguards; hardliners want enforceable uniformity; reformers argue for plural local authority. Allies and NPC delegates can make decisions Alya would not have chosen if the player has built systems that genuinely distribute responsibility.

**Act-end state:** three regions form a voluntary mutual-aid compact with distinct local rules, shared emergency signals, resource commitments, and dispute resolution. The network is useful but fragile; its existence does not erase regional grievances.

### Act IV — Escalation: “What the Wound Learns”
**Regions:** Cinderfall Reach and the Shattered Archive.

The Ferida begins exploiting not only individual vulnerabilities but the systems created to manage them: reputation, assignments, trade routes, institutional protocols, and the network's own trust. Familiar solutions become dangerous when applied without context. A major attack fractures the network, isolates a region, and forces the community to choose between preserving its own infrastructure and sending people and supplies to a threatened partner.

Alya's flaw returns: she attempts to carry too much herself and becomes vulnerable to the Ferida's amplification of guilt and control. The player must rely on allies, delegates, regional leaders, and prior preparations. No single stat, ally, facility, or faction score can substitute for the network's accumulated readiness.

**Act-end state:** the network survives in a changed form, and the Shattered Archive yields evidence that the Ferida is sustained by recurring patterns of exploitation and failed correction, not by one simple external switch. Alya learns that destroying a visible manifestation is not equivalent to healing the underlying conditions.

### Act V — Revelation and Resolution: “A Future Without a Center”
**Region:** The Wound's Confluence, reached through the Shattered Archive and a multi-region coalition.

The party discovers that the Ferida is a self-reinforcing wound in the world's relational and ecological systems. It amplifies vulnerabilities, turns useful structures into instruments of exclusion, and persists when communities externalize costs and deny correction. Its personification, the Ferida Manipulator, is an antagonist and agent, not the sole origin of every injustice. Alya's past failure involved choosing a narrow containment solution and accepting an institutional account of who could be sacrificed; she survived, but people she was trying to protect did not. The full details are disclosed through evidence and character testimony, not a single exposition dump.

The final confrontation is a multi-stage encounter with combat and world-state objectives. Victory requires disrupting the manifestation, keeping coalition links active, and making local systems capable of responding without Alya's continuous direction. The final choice determines which structures are preserved, reformed, decentralized, or abandoned. It does not guarantee that the Ferida will never return.

**Act-end state:** the wound's sustaining conditions are transformed or constrained; the future remains uncertain but no longer depends on one exceptional individual.

## 3. Main quest graph — 45 stages

Main quests are mandatory in sequence within each act unless a stage explicitly allows a state-dependent variant. Optional discoveries and adult content never gate the main ending. Each quest has a stable ID, a visible objective, a state mutation, and an authored exit condition.

### Act I — Foundation
1. **Q01 The Empty Cistern** — meet Mara and the First Ally; establish the water dispute and first local choice.
2. **Q02 A Ration Is Not a History** — interview residents; uncover that the allocation dispute predates the Red Thread.
3. **Q03 Signs Beneath the Water** — investigate the moving red filaments; introduce the Ferida as an unknown risk.
4. **Q04 A Door Left Open** — stabilize an affected resident and decide how to share scarce clean water.
5. **Q05 The Cost of a Quick Fix** — explore the root-vault approach; discover evidence that the sluice can be repaired but not without sacrifice.
6. **Q06 The Organization Arrives** — meet the Pragmatic Mentor and Institutional Representative; receive the containment proposal.
7. **Q07 Three Parts of a Third Option** — gather repair materials, local knowledge, and coordinated care; choose preparation priority.
8. **Q08 Hold the Sluice** — objective-based climax; stabilize diversion, sever the active filament, and secure the gate.
9. **Q09–Q11 Act I Epilogue Chain** — “What Remains” records the seed loss; “A Place That Must Continue” formalizes leadership and chooses a facility; “First Delegation” launches the first Expedition. These are three implementation stages but share the three final slots in the slice graph. For catalog accounting, Q09, Q10, and Q11 are the stable IDs; the first eight are Q01–Q08.

### Act II — Construction
10. **Q12 A Roof for Strangers** — convert temporary shelter into a permanent refuge; introduce upkeep and space trade-offs.
11. **Q13 The Work Nobody Sees** — assign residents to gathering, care, training, and maintenance; show aptitude and morale.
12. **Q14 The Ledger of Needs** — establish a transparent resource ledger; choose which shortage to address first.
13. **Q15 A Place at the Table** — recruit the Devoto or resolve their introductory mediation arc; introduce social cohesion.
14. **Q16 The Shape of a Promise** — Alya makes a public promise and must define its limits and review conditions.
15. **Q17 A Road with Two Names** — open Greenwake Basin; negotiate access with local stewards and traders.
16. **Q18 The Pilot Community** — Organization proposes standards, reporting, and a supervised pilot arrangement.
17. **Q19 The People Marked for Moving** — discover the relocation order and hear the affected group's own account.
18. **Q20 The Order We Refuse** — shelter the group under a documented risk plan; rupture with the Organization's hardline wing and establish council/delegate governance.

### Act III — Consequences
19. **Q21 Freedom Has a Price** — autonomy removes a support guarantee; choose an initial economic stabilization policy.
20. **Q22 The Glassstep Contract** — negotiate a trade compact with explicit quotas, exceptions, and a dispute clause.
21. **Q23 The Empty Caravan** — investigate a missing shipment; distinguish sabotage from a bad incentive structure.
22. **Q24 Two Fires, One River** — mediate a resource dispute between regional communities; no outcome satisfies every faction.
23. **Q25 A Different Kind of Kinship** — enter Mycelian Reach and negotiate with the Matriarch and Guide.
24. **Q26 What the Roots Remember** — uncover a local memory network that preserves evidence but can also preserve grievance.
25. **Q27 The Price of a Cure** — decide how to share scarce treatment and research access.
26. **Q28 A Voice from the Organization** — cooperate with an internal reformer while protecting local authority.
27. **Q29 The Compact of Three Regions** — ratify the mutual-aid compact with explicit contributions and local exceptions.

### Act IV — Escalation
28. **Q30 When the Signals Lie** — a trusted warning system is manipulated; establish verification and redundancy.
29. **Q31 The Cinderfall Evacuation** — evacuate civilians under limited transport and time.
30. **Q32 The Measure of a Life** — challenge a triage protocol that hides value judgments behind neutral metrics.
31. **Q33 The Delegates Disagree** — resolve a major council dispute without allowing Alya to simply overrule everyone.
32. **Q34 The Broken Route** — reopen a damaged regional corridor through an expedition and a direct mission.
33. **Q35 A Familiar Mistake** — Alya's attempt to control every response causes a setback; allies must intervene.
34. **Q36 The Shattered Archive** — enter the archive and collect records from multiple sources.
35. **Q37 The Wound Learns** — learn how the Ferida exploits systems and feedback loops.
36. **Q38 The Network Under Fire** — defend multiple objectives; prior regional preparation changes support and costs.

### Act V — Revelation and Resolution
37. **Q39 The Promise Alya Buried** — reconstruct Alya's earlier failure from evidence and survivor testimony.
38. **Q40 The Personification** — confront the Ferida Manipulator's account of the world's wound.
39. **Q41 The Coalition's Terms** — negotiate a final coalition with explicit costs and local authority.
40. **Q42 A Road Without a Hero** — distribute final operational responsibilities among allies and delegates.
41. **Q43 Into the Confluence** — reach the Wound's Confluence; optional side paths change support, not basic access.
42. **Q44 The Wound's Heart** — first phase of the final encounter; disrupt the manifestation's anchors.
43. **Q45 The Last Pattern** — final objective phase; preserve coalition links and stop the Ferida from rebuilding its feedback loop.
44. **Q46 What We Leave Running** — choose which institutions and network structures are preserved, reformed, decentralized, or retired.
45. **Q47 A Future Without a Center** — epilogue resolves the world-state ending family and ally/NPC epilogues.

**ID correction rule:** The act list above is the complete 47-stage authored story graph including all three Act I epilogue stages. The initial planning target of 45 is superseded by this explicit graph; do not renumber Q46–Q47 or compress stages to preserve the old estimate. The content catalog uses Q01–Q47.

## 4. Regions and world progression

1. **Ashfen Verge** — starting region; waterworks, farms, damp lowlands, Brackenford; themes of scarcity and blame.
2. **Greenwake Basin** — refuge corridors, reclaimed fields, workshops, trade crossings; themes of growth and capacity.
3. **Glassstep March** — salt-glass flats, caravan roads, market forts; themes of contracts, scarcity pricing, and leverage.
4. **Mycelian Reach** — living forest and fungal memory network; tribal societies, stewardship, and historical grievance.
5. **Cinderfall Reach** — volcanic ashlands and industrial settlements; evacuation, labor, infrastructure, and triage.
6. **The Shattered Archive** — broken research/ritual complex with several competing records of the Ferida; evidence and institutional history.
7. **The Wound's Confluence** — final region where ecological and relational systems converge; access is gated by Act V coalition readiness, not a single numerical reputation score.

Each region has a hub or safe staging point, 3–5 authored POIs, one signature gathering profile, one regional encounter pool, at least one ally/NPC thread, one main-quest chain, and one optional discovery that reveals context rather than a mandatory key. The world map is a regional graph; no tactical grid or freeform open-world traversal is implied.

## 5. Factions

1. **Brackenford Council** — local residents and delegates. States: trust, cohesion, representation quality, and unresolved grievances.
2. **The Organization** — a necessary regional institution. Internal blocs: Pragmatists, Reformers, Hardliners. Track cooperation, oversight pressure, and credibility separately.
3. **Glassstep Caravans** — merchants, carriers, and route stewards. Track contract reliability and route access; do not reduce all merchants to greed.
4. **Mycelian Circles** — distinct tribal communities linked by a living memory tradition. Track consent to share knowledge, stewardship obligations, and grievance.
5. **Cinderfall Works** — industrial and evacuation authorities. Track safety, labor obligations, and public legitimacy.
6. **The Unbound** — displaced people, deserters, stigmatized groups, and mutual-aid cells; not a single ideology. Track safe passage, representation, and internal fragmentation.

The Ferida is not a reputation faction. Its manifestations are world/encounter states driven by authored progression and unresolved conditions. The Organization's blocs must have independent NPCs and quest outcomes; “Organization trust” alone cannot erase their differences.

## 6. Recruitable ally arcs

The ten locked allies keep their established names/concepts and IDs. Each has a recruitment condition, a personal conflict, an Act III/IV contribution, and an Act V epilogue condition. Recruitment is optional except that the First Ally is the initial companion; no single optional ally is required to finish the main story.

- **ALLY-001 First Ally / Generalist:** starts as a survivor who lost their group; learns that adaptability is not the same as having no boundaries. Personal arc: locate the former group's trail, learn why it fractured, and choose a voluntary future with Brackenford. Signature: versatile loadout and development redistribution.
- **ALLY-002 Guardiã:** recruited after protecting a vulnerable settlement and accepting help rather than taking every burden herself. Arc: separate care from control; late-game holds a defensive line only if the player has supported delegation. Signature: Guard/Interception and ally protection.
- **ALLY-003 Rival:** recruited after a competing leader's plan fails and Alya offers partnership without demanding ideological surrender. Arc: transform competitive leadership into accountable challenge; can publicly oppose Alya if the council is being centralized. Signature: pressure, momentum, and disadvantage exploitation.
- **ALLY-004 Erudita:** recruited after a research expedition exposes the cost of treating people as data. Arc: preserve research while adopting consent, review, and transparent risk practices. Signature: creature study, alchemy, and encounter knowledge.
- **ALLY-005 Cuidadora:** conditionally recruited through the Act I care route or Recovery Room investment. Arc: transition from emergency care to prevention and community health; challenges leaders who use treatment to justify preventable risk. Signature: diagnosis, recovery, and health-system resilience.
- **ALLY-006 Artesã:** recruited through a workshop/repair quest. Arc: accept maintenance and safety standards without losing inventive freedom. Signature: construction, modification, and controlled transmutation.
- **ALLY-007 Caçadora:** recruited through an exploration chain after a route rescue. Arc: choose between solitary competence and reciprocal responsibility; her expedition bonuses improve discovery and reduce route risk but never guarantee success. Signature: ranged combat, traps, and exploration.
- **ALLY-008 Mercador:** recruited through a trade dispute after returning a profitable but harmful contract. Arc: distinguish prosperity from extraction and create resilient trade rather than dependency. Signature: better trade access, price negotiation, and commercial opportunities; intentionally lower combat contribution.
- **ALLY-009 Inadaptada:** optional sidequest recruitment after the player follows a series of misunderstood incidents. Arc: build confidence without requiring assimilation; exceptional learning is strong but requires time and support to unlock safely. Signature: accelerated flexible development.
- **ALLY-010 Devoto:** recruited through a mediation and morale chain. Arc: retain idealism while learning that compassion requires boundaries and accountable processes. Signature: protection/buffs tied to morale, integration, and community cohesion.

Relationship clusters remain selective, not a complete matrix: First Ally–Caçadora–Inadaptada; Guardiã–Rival–Cuidadora; Erudita–Artesã; Mercador–Devoto–Inadaptada. These relationships unlock dialogue, support actions, optional adult scenes, or expedition synergies only when the relevant narrative state supports them. Adult content requires adult characters and clear consent; it never gates critical progression.

## 7. Named NPC arcs

The canonical roster remains the 21-entry roster in `docs/characters/NPCS_DESIGN.md` and `docs/characters/CHARACTER_BIBLE.md`. This lock assigns each NPC a game-long purpose:

- **NPC-001 Tavernkeeper:** rumor hub; tracks how local stories change after each act; exposes the difference between a fact and a repeated account.
- **NPC-002 Dancer:** public performance and cultural events; helps morale but refuses to be treated as a universal solution to hardship.
- **NPC-003 Community Elder:** preserves local history; initially supports continuity, later must admit the community's old allocation rules caused harm.
- **NPC-004 Mediator:** helps disputes become explicit agreements; can become a council process lead if the player supports review and records.
- **NPC-005 Pragmatic Mentor:** provides field training and institutional context; remains willing to cooperate after the rupture if local safeguards are credible.
- **NPC-006 Institutional Representative:** negotiates reporting and supervision; can become an intermediary between local autonomy and formal obligations.
- **NPC-007 Ferida Researcher:** develops a safer evidence protocol; must choose between publication, restricted containment, and shared research.
- **NPC-008 Hardliner:** recurring institutional opponent; can be constrained politically or persuaded by evidence, but never converted by one speech.
- **NPC-009 Regional Authority:** grants legitimacy when the network demonstrates accountable governance; also demands transparent cost-sharing.
- **NPC-010 Trade Representative:** negotiates route access, contract clauses, and supply shocks.
- **NPC-011 Priestess:** supports rites of grief, recovery, and community memory; does not replace medical care or political accountability.
- **NPC-012 Tribal Matriarch:** protects Mycelian sovereignty; shares memory only with consent and reciprocity.
- **NPC-013 Tribal Guide:** mediates travel and cultural interpretation; can expose when Alya's assumptions are wrong.
- **NPC-014 War-Chief:** tests agreements through ritualized contest and resource obligations; respects explicit terms over flattery.
- **NPC-015 EnemyCommander:** recurring adversarial leader with separate Enemy/Boss combat records; represents a faction that exploits instability, not the Ferida itself.
- **NPC-016 Faction Dissident:** reveals internal dissent and helps build safe defections without requiring unconditional allegiance.
- **NPC-017 Ferida Manipulator:** major antagonist who uses true grievances to justify destructive absolutes; separate NPC dialogue and boss encounter representations.
- **NPC-018 Reaper:** neutral threshold figure; reveals consequences and mortality without becoming a quest vending machine.
- **NPC-019 Dryad:** regional ecology contact; supports restoration if extraction and stewardship obligations are honored.
- **NPC-021 Survivor:** a living consequence of prior containment; can become a witness, advocate, or leave if repeatedly instrumentalized.
- **NPC-022 Demonkin:** rescue/rehabilitation and legacy conflict; demonstrates that species and origin do not determine consent, allegiance, or moral character.

NPC-020 remains retired and must never be reused. Tavernkeeper, Elder, Mediator, Cuidadora, and other characters may support the same system but cannot erase an ally's distinctive gameplay identity.

## 8. Enemy and boss content lock

### Enemy archetypes (35)

Existing legacy archetypes are preserved where useful and mapped to stable IDs. Enemy names do not imply that a species is inherently hostile. The combat roster uses these roles:

1. ENM-001 Guard — disciplined human/civilized defender.
2. ENM-002 Slime — low-tier adaptive body; tests multi-hit and elemental coverage.
3. ENM-003 Cockatrice — status and vulnerability pressure.
4. ENM-004 Warrior — direct melee baseline.
5. ENM-005 Goblin — evasive utility/scavenger.
6. ENM-006 Mycelian Sentinel — territorial defense; not a generic evil tribe.
7. ENM-007 Zombie — slow attrition/undead effects.
8. ENM-008 Augmented Agent — institutional elite; counters repeated tactics.
9. ENM-009 Kunoichi — evasion, marks, and target switching.
10. ENM-010 Krakenblood — resilient pressure attacker.
11. ENM-011 Kitsune Trickster — decoys and intent manipulation.
12. ENM-012 Barbarian — high damage, low flexibility.
13. ENM-013 Royal Guard — formation and interception.
14. ENM-014 Minotaur — charge/guard-break archetype.
15. ENM-015 Wolfkin Stalker — pack coordination and pursuit.
16. ENM-016 Orc Challenger — duel/resolve pressure; may be neutral in narrative.
17. ENM-017 Haunt — reactive spirit, weak to knowledge and preparation.
18. ENM-018 Witch — curse and control specialist; some are NPCs in separate contexts.
19. ENM-019 Mummy — endurance, attrition, and seal mechanics.
20. ENM-020 Dullahan — elite execution pressure; story counterpart is NPC-018 Reaper only if explicitly authored, otherwise distinct.
21. ENM-021 Angelic Arbiter — protection and judgment effects; not automatically evil.
22. ENM-022 Dragonkin — elemental elite, high threat telegraphs.
23. ENM-023 Fallen Angel — multi-phase control and vulnerability.
24. ENM-024 Lamia Duelist — constriction/control and positional abstraction.
25. ENM-025 Demon — high-pressure hybrid; alignment varies.
26. ENM-026 Threadling — low-health Ferida swarm unit; multiplies when ignored.
27. ENM-027 Hollow Warden — objective defender with linked resistance.
28. ENM-028 Root-Knot Anchor — objective entity; defeating it alone is not necessarily encounter victory.
29. ENM-029 Red-Tide Leech — drains resources/strains; vulnerable after feeding.
30. ENM-030 Echo Husk — repeats the last common action pattern; countered by varied tactics.
31. ENM-031 Guilt Mirror — uses party relationship flags to create pressure, never reveals private player data.
32. ENM-032 Ashbound — Cinderfall hazard fighter; alternates armor and exposure.
33. ENM-033 Archive Custodian — research construct; tests interrupts and source discovery.
34. ENM-034 Network Eater — attacks links/objectives rather than simply Vitality.
35. ENM-035 Confluence Herald — late-game Ferida manifestation; multi-target threat with explicit phase conditions.

### Major bosses (9)

- **BOS-001 Root-Knot at the Sluice** — Act I objective boss; stabilize diversion, sever filament, secure gate.
- **BOS-002 The Pilgrim Engine** — Act II corrupted logistics construct; protect shelter routes and disable three supply anchors.
- **BOS-003 The Contract Eater** — Act III Glassstep boss; break exploitative contract seals while keeping caravan escorts alive.
- **BOS-004 The Memory That Bites** — Act III Mycelian encounter; resolve the living memory crisis without destroying the network.
- **BOS-005 The Ashen Measure** — Act IV Cinderfall boss; counter a triage engine that converts people into risk categories.
- **BOS-006 EnemyCommander: Siege of the Broken Route** — Act IV faction battle; the Commander can retreat, yield, or be defeated; NPC state follows authored result.
- **BOS-007 The Archive's False Witness** — Act IV/early V; tests evidence verification and counters repeated actions.
- **BOS-008 The Ferida Manipulator** — Act V personal confrontation; dialogue and combat are separate representations of NPC-017.
- **BOS-009 The Confluence Pattern** — final multi-phase encounter; disrupt anchors, maintain coalition links, and complete the world-state objective.

### Special encounters (8)
- SPC-001 The First Threadling Nest — teaches enemy reinforcement.
- SPC-002 The Sealed Clinic — optional care/containment dilemma.
- SPC-003 The Caravan in the Salt Storm — protect supplies or rescue stragglers.
- SPC-004 The Silent Grove — exploration/knowledge check.
- SPC-005 The Broken Lift — objective encounter with environmental hazards.
- SPC-006 The Evacuation Clock — timed objective, not a pure damage race.
- SPC-007 The Unreliable Signal — encounter modifiers change after evidence gathering.
- SPC-008 The Empty Throne — late optional encounter testing delegation and ally synergy.

Every boss must have a readable intent/phase contract, a non-damage objective where appropriate, retreat/failure consequences, and a defined post-encounter world-state mutation. Do not scale every encounter universally to player level.

## 9. Facilities, resources, and economy

### Facilities (12)

- **FAC-001 Recovery Room** — recovery, condition stabilization, care route; improves health/status recovery.
- **FAC-002 Common Workshop** — basic crafting, repairs, equipment modification.
- **FAC-003 Coordination Board** — assignment visibility, Expedition overview, delegation reports; does not gate Expeditions.
- **FAC-004 Storehouse** — production buffer and resource reporting; does not create an inventory capacity limit.
- **FAC-005 Training Yard** — training assignment and combat aptitude development.
- **FAC-006 Research Annex** — Ferida research, enemy knowledge, recipe discovery.
- **FAC-007 Alchemy Bench** — consumables, botanical processing, controlled transmutation.
- **FAC-008 Trade Stall** — local trade and market opportunities.
- **FAC-009 Community Hall** — council, representation, grievance review, morale.
- **FAC-010 Refuge Wing** — housing, rehabilitation, and integration capacity.
- **FAC-011 Expedition Lodge** — specialist preparation, route intel, Expedition risk modifiers.
- **FAC-012 Signal Tower** — regional warning network and late-game coalition coordination.

Act I offers a choice among FAC-001, FAC-002, or FAC-003. All three remain constructible later. Basic assignments and Expeditions unlock at Act I completion regardless of facility choice; FAC-003 only improves visibility and coordination.

### Resources (8)

- **RES-001 Timber** — structural construction and repairs.
- **RES-002 Fiber** — bindings, reinforcement, clothing/field kits.
- **RES-003 Botanical Extract** — care, alchemy, and stabilization.
- **RES-004 Gold** — trade, wages, contracts, and selected services.
- **RES-005 Provisions** — community upkeep, travel preparation, and evacuation.
- **RES-006 Salvage** — mechanical parts and advanced repairs.
- **RES-007 Research Notes** — knowledge unlocks and controlled research.
- **RES-008 Trust Tokens** — not a universal currency; represents documented reciprocal commitments used by specific coalition/faction actions and should be capped per agreement, not globally farmed.

Unique narrative resources (e.g., the Act I seed reserve) are quest/world-state objects, not general currencies. Resource values and yields remain provisional until the first integrated economy pass. No inventory capacity ceiling exists.

### Economy guardrails
- Every required construction has a guaranteed feasible route; optional crafting cannot consume reserved main-quest materials.
- Main-quest rewards should not make gathering/Expeditions irrelevant.
- Trade prices use region, contract, reputation state, and stock profile; avoid random price swings that invalidate a promised deal.
- Production/upkeep resolves on the canonical time tick. A missing assigned worker pauses or reduces the authored output according to the recipe; it does not create hidden negative inventory.
- Expeditions can return partial success, delay, injury, lost opportunity, or discovery; failure should not delete a unique character or hard-lock the main quest.

## 10. Items and Alya's outfits

### Item catalog target: 36 canonical items

Retain and normalize the existing useful equipment families; do not preserve ambiguous legacy names as separate items when they are stages of one evolution chain.

**Build-defining equipment (10):**
- ITM-001 Crux of Enlightenment — balanced Soul/Body and H-damage specialization.
- ITM-002 Oath of Obedience — blessed defensive sustain; unlocks through a protection vow.
- ITM-003 Underwear of Restoration — recovery/status-cleansing synergy.
- ITM-004 Forever Cage — cursed risk/reward item evolving from True-Size Cage; Strain interaction.
- ITM-005 Chastity Belt — defensive anti-penetration/anti-control build.
- ITM-006 Ofuda Chastity — blessed defensive counterpart with Soul/Masochism profile.
- ITM-007 Hypnosis → Reprogram → Slave — one cursed evolution chain, not three inventory records.
- ITM-008 Sensitivity → Receptacle → Fulfilled — one cursed evolution chain with incoming-pressure and recent-hit stages.
- ITM-009 Restraint → Suffer → Canvas — one cursed resistance/effect-conversion chain.
- ITM-010 Messaging → Sway → Pheromone — blessed area-support chain; presentation must preserve consent framing.

**Core equipment and utility (16):**
- ITM-011 Body Amulet; ITM-012 Agility Ring; ITM-013 Soul Amulet; ITM-014 Charm Ring.
- ITM-015 Field Harness — expedition/repair preparation.
- ITM-016 Reinforced Boots — travel hazard reduction.
- ITM-017 Sluiceworker Gloves — construction/repair bonus.
- ITM-018 Herbal Satchel — care/alchemy output.
- ITM-019 Surveyor Lens — discovery and enemy intent information.
- ITM-020 Archive Seal — research protection and controlled access.
- ITM-021 Caravan Ledger — contract/trade insight.
- ITM-022 Guard's Buckler — defensive reaction synergy.
- ITM-023 Thread-Cut Knife — Ferida-filament utility; no automatic boss victory.
- ITM-024 Resonance Charm — research/Strain interaction.
- ITM-025 Expedition Rations — preparation item; consumable.
- ITM-026 Emergency Filter Kit — one-use spread-risk mitigation.

**Consumables and quest items (10):**
- ITM-027 Healing Draught.
- ITM-028 Clear-Mind Tonic.
- ITM-029 Field Dressing.
- ITM-030 Botanical Stabilizer.
- ITM-031 Smoke Pellet.
- ITM-032 Thread-Salt.
- ITM-033 Repair Kit.
- ITM-034 Research Sample Case.
- ITM-035 Seed-Reserve Ledger (quest evidence; not the reserve itself).
- ITM-036 Coalition Signal Key (quest/coordination item; no global unlock bypass).

Legacy tattoos, jewelry, plugs, clothing, and transformation chains may be retained when they have distinct mechanics and a consent-aware narrative context. They must receive stable IDs, explicit slot, effects, curse/blessing state, removal/evolution policy, unlock conditions, and asset classification. The 36-item list is the authored core set; additional legacy variants can be retained as sub-variants only if they do not inflate the core catalog or create redundant choices.

### Alya outfits: retain 8 base sets
- **OUT-001 Traveler's Lace** — default, balanced baseline.
- **OUT-002 Field Armor** — defensive combat identity.
- **OUT-003 Witch's Mantle** — magic/research specialization.
- **OUT-004 Dancer's Regalia** — social/Charm and event presentation.
- **OUT-005 Nun's Habit** — restraint/protection visual identity; not a morality marker.
- **OUT-006 Formal Dress** — diplomacy and major civic scenes.
- **OUT-007 Demon Armor** — late-game Ferida-facing equipment, powerful but with explicit trade-offs.
- **OUT-008 Shibari Harness** — specialized risk/reaction build; unlock and presentation remain consent-framed.

**Not retained as independent base outfits:** Nude (presentation state, not equipment); Slave (a narrative/curse state, never a default outfit slot or identity label); CowPrint (cosmetic variant/event unlock unless it receives a genuine mechanical identity). Small cosmetic variants do not become separate equipment systems.

## 11. Sidequests and autonomous Expeditions

### Authored sidequests (25; five per act)

**Act I**
- SQ-001 A Bowl Kept Warm — resolve a food-sharing dispute; unlocks a resident support flag.
- SQ-002 The Missing Filter — recover a lost filter; lowers one Q07 preparation cost.
- SQ-003 The Quiet Room — help exhausted workers establish voluntary recovery space.
- SQ-004 A Map in the Rafters — discover a safer route; grants expedition route knowledge.
- SQ-005 Mara's Ledger — reconstruct water allocation records; changes local trust, not the mandatory seed loss.

**Act II**
- SQ-006 The Unclaimed Bed — determine how refuge spaces are allocated.
- SQ-007 A Tool for Every Hand — help Artesã test a safe repair design.
- SQ-008 The Unfinished Lesson — help Guardiã and Rival establish training rules.
- SQ-009 A Contract in Ink — expose a one-sided trade clause.
- SQ-010 The Names We Keep — create a consent-based resident record.

**Act III**
- SQ-011 Salt on the Road — rescue caravan cargo or stranded travelers.
- SQ-012 The Root That Remembers — decide what memory the Mycelian Circles share.
- SQ-013 A Debt with No Owner — settle a legacy debt without punishing descendants.
- SQ-014 The Broken Bell — restore a warning system with redundant signals.
- SQ-015 The Price of Quiet — address a rumor campaign without suppressing dissent.

**Act IV**
- SQ-016 Ashes in the Clinic — distribute scarce treatment with a public review process.
- SQ-017 The Route Nobody Owns — restore a route with shared maintenance.
- SQ-018 The False Witness — gather evidence before accusing an ally or faction.
- SQ-019 A Seat Left Empty — respond to a delegate's resignation without forcing them back.
- SQ-020 The Last Workshop Shift — save a facility or evacuate its workers.

**Act V**
- SQ-021 The Witnesses' Circle — reconcile contradictory accounts of Alya's past.
- SQ-022 What the Reaper Carries — help a community memorialize a loss.
- SQ-023 A Garden Outside the Wall — establish a recovery plot beyond the hub.
- SQ-024 The Unbound's Terms — negotiate representation for a displaced group.
- SQ-025 A Signal Sent Twice — build redundant coalition communication.

Sidequests may grant items, knowledge, relationships, optional ally scenes, faction changes, or encounter modifiers. They never remove mandatory losses or serve as the only key to the final boss.

### Expedition templates (8 reusable templates)
- EXP-001 Foraging Run — provisions/botanical materials; weather and aptitude modifiers.
- EXP-002 Timber Survey — timber/salvage; route risk and tool quality.
- EXP-003 Safe-Road Survey — reveals POIs and lowers travel uncertainty.
- EXP-004 Resident Escort — protects travelers; morale and trust outcome.
- EXP-005 Research Retrieval — research notes/samples; enemy knowledge and contamination risk.
- EXP-006 Trade Negotiation — gold, contracts, market access; requires a negotiator or preparation.
- EXP-007 Emergency Relief — sends provisions/care to a region; costs resources but can preserve network stability.
- EXP-008 Signal Relay — repairs coalition communications; late-game redundancy.
  
An Expedition uses NPC/community members only. Assigned allies are unavailable to the active party until return. Results are deterministic from seeded resolution, assignment, aptitude, preparation, route, time, and authored modifiers. It cannot silently become a player-controlled Sidequest.

## 12. Endings and world-state outcomes

Five ending families; the game selects a family and composes epilogues from explicit state flags. No exact percentage meter is shown.

1. **END-001 The Shared Table** — strong, accountable network; local autonomy preserved; the Organization is reformed through negotiated oversight. Alya remains a participant, not a central authority.
2. **END-002 The Many Lanterns** — highly decentralized network; weaker central coordination but strong local resilience. Some regions remain distant; the future is plural and uncertain.
3. **END-003 The Necessary Compact** — a more centralized coalition survives with safeguards, appeal routes, and sunset clauses. It is effective but must continue to be questioned.
4. **END-004 The Quiet Refuge** — Brackenford and several partners endure, but broader cooperation remains limited. The local community is safe enough; the world-scale wound is constrained rather than fully addressed.
5. **END-005 The Unfinished Road** — the network fractures under unresolved grievances, but not into total annihilation. Alya prevents immediate collapse; future recovery depends on people who choose to rebuild.

Ending inputs include regional readiness, delegated responsibility, faction agreements, evidence integrity, ally arcs, care/integration policy, and the final choice. No single companion, romance, adult scene, or faction reputation can dictate the ending.

## 13. Adult-content and consent policy for content authoring

All characters are adults. Adult content is optional, character-specific, and gated by relationship/context flags. It must not be required for main progression, critical rewards, or ending access. Consent, boundaries, and consequences remain legible. Curses and supernatural influence are gameplay states and must not be presented as equivalent to consent. NPCs who are not recruited may have lower-tier optional scenes only when their authored relevance supports them; the tier system in `NPCS_DESIGN.md` remains authoritative.

This lock defines adult content *placement and unlock philosophy*, not explicit scene scripts or final CG asset IDs. Those are production items and should be authored against the character's arc, not produced as a quota.

## 14. Content dependencies and production order

1. Lock stable IDs and validate all structured catalogs.
2. Complete main quest graph, sidequest triggers, flags, and ending-state mapping.
3. Normalize enemy/item/facility/resource IDs and link them to existing legacy data.
4. Define encounter phase/objective contracts and quest rewards.
5. Complete ally/NPC recruitment, relationship, and state transitions.
6. Map every content ID to UI, audio, portrait, sprite, combat, CG, and localization needs.
7. Build the vertical slice against this catalog before expanding production art.
8. Run runtime integration, numerical balance, playtest, accessibility, and save migration tests after the implementation foundation exists.

## 15. What this lock does and does not mean

**Closed here:** base-game content scope; five-act narrative sequence; region progression; main quest stages; sidequest set; faction identities; ally and NPC arc assignments; enemy and boss coverage; facility/resource/item roster; outfit scope; Expedition templates; ending families; adult-content integration principles.

**Still production work:** schema implementation and validation; linking IDs to existing CSVs and legacy asset files; exact stat/skill coefficients and encounter tuning; dialogue for every quest stage; all final dialogue localization; audio; final CG scripts and asset IDs; visual asset generation/review; UI implementation; automated and manual QA; accessibility; save migration; performance and release work.

No claim of runtime completeness or release readiness is made by this document.
