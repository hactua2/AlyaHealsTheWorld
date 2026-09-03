# Alya Heals the World — Character Data Alpha

## Status
**ALPHA — concrete character data baseline.**

This document turns the locked character architecture into implementable first-pass data. It is intentionally a balance-ready specification rather than final tuning: exact skill coefficients, XP curves, item IDs, quest IDs, dialogue and H-scene asset IDs remain downstream implementation/content work.

The alpha is designed to be internally coherent enough to begin implementation and placeholder art without reopening the character architecture.

## 1. Stat model selected by audit

### Primary attributes
The game uses exactly eight mechanically central attributes:

`Body`, `Agility`, `Soul`, `Charm`, `Dominance`, `Submission`, `Sadism`, `Masochism`.

**Internal scale: 1–100.** UI may later compress this to bands, but data should retain integer precision on the 1–100 scale.

- 10 = weak baseline
- 25 = below average adult
- 40 = competent
- 55 = strong specialization
- 70 = exceptional
- 85 = extraordinary
- 100 = practical ceiling before explicit temporary modifiers

This scale is preferred because it supports readable base values, percentage modifiers, aptitude curves and equipment effects without forcing fractional attributes into content authoring.

### Stat interpretation
- **Body:** health capacity, physical damage, damage resistance.
- **Agility:** accuracy, evasion, initiative.
- **Soul:** magic power, H-resistance, supernatural stability.
- **Charm:** H-damage, H-accuracy, social influence and susceptibility shaping.
- **Dominance:** H-damage, H-accuracy, resistance to H-attacks.
- **Submission:** vulnerability to H-attacks, H-damage contribution, buff empowerment.
- **Sadism:** damage/accuracy in aggressive H-oriented effects.
- **Masochism:** H-resistance, damage resistance and debuff resistance.

The old `Health`, `H-power`, etc. concepts remain derived values; they are not additional primary stats.

### Character stat construction
For allies:

`Effective Attribute = Base Attribute + Natural Growth + Direct Growth + Modifiers`

Natural aptitude is a separate 1–5 rating per attribute/function and affects future growth, not starting power alone.

Initial direct-growth budget is small. Level provides modest automatic growth and Skill Points; actual play, skills, context and assignments also feed natural development.

### Alpha growth bands
- **5 — Exceptional:** +18% natural-growth efficiency
- **4 — High:** +10%
- **3 — Normal:** baseline
- **2 — Low:** -10%
- **1 — Poor:** -20%

These are efficiency modifiers, not hard caps. Characters can exceed their aptitude with diminishing returns.

## 2. Shared ally defaults

- Starting level: **1** unless noted.
- Starting active skill slots: **3**.
- Starting passive slots: **1**.
- H-skills use normal active slots.
- Initial skill point package: **3 SP**.
- Skills have no levels.
- Loadouts can be changed outside combat.
- All allies are adults.
- All allies can eventually receive H-content, but H-content is character-specific and never substitutes for characterization.

## 3. Recruitable Allies — concrete alpha

| ID | Name | Species | Presentation | Adult age | Height | Body | Combat role | Community role |
|---|---|---|---|---|---|---|---|---|
| ALLY-001 | First Ally | Human | Femboy | Young adult | Average | Slim-athletic | Generalist | Generalist / flexible |
| ALLY-002 | Guardiã | Minotauroid | Futanari | Mature young adult | Very tall | Muscular-athletic | Tank / Support | Security / Training |
| ALLY-003 | Rival | Predatory beastfolk | Feminine | Young adult | Tall | Athletic-curvy | Bruiser / DPS | Crisis management |
| ALLY-004 | Erudita | Arcane humanoid | Feminine | Young adult | Average-tall | Slim | Pure Mage | Research / Alchemy |
| ALLY-005 | Cuidadora | Human | Futanari | Mature young adult | Average | Curvy-athletic | Healer / Support | Health / Recovery |
| ALLY-006 | Artesã | Goblin humanoid | Feminine | Young adult | Short-average | Compact-athletic | Utility / Control | Construction / Production / Equipment |
| ALLY-007 | Caçadora | Fox beastfolk | Futanari | Young adult | Average | Lean-athletic | Ranged DPS / Traps | Expeditions / Exploration |
| ALLY-008 | Mercador | Feline beastfolk | Femboy | Young adult | Average | Slim | Utility / low combat | Commerce / Economy |
| ALLY-009 | Inadaptada | Rare exotic humanoid | Futanari | Young adult | Average | Unusual, proportionate adult | Flexible generalist | Negotiation / interpersonal |
| ALLY-010 | Devoto | Faerie-like humanoid | Feminine | Young adult | Average | Soft-curvy adult | Protection / Buff | Cohesion / morale / integration |

### ALLY-001 — First Ally
**Identity:** Human, Femboy, average height, slim-athletic adult. Practical clothes, travel wear, visible signs of repeated repairs. Friendly face but guarded eyes.

**Base attributes:** Body 34 / Agility 38 / Soul 31 / Charm 42 / Dominance 30 / Submission 38 / Sadism 28 / Masochism 35.

**Aptitudes:** Body 3, Agility 4, Soul 3, Charm 4, Dominance 3, Submission 3, Sadism 2, Masochism 3.

**Preferred functions:** Generalist, scouting, flexible assignments. No hard specialization.

**Growth identity:** Learns from changing jobs and active participation. Changing assignment can redistribute future natural-growth weighting without erasing learned competence.

**Starting skills:**
- `Quick Strike` — low-cost single-target physical attack.
- `Adapt` — temporarily improves the attribute most relevant to the next declared action.
- `Encourage` — minor ally support and Charm-weighted recovery of combat momentum.

**Signature mechanic — Versatility:** Can change preferred function/loadout with reduced friction. When switching assignment or role, retains 50% of the previous contextual growth weighting for a short transition period rather than starting from zero.

**Narrative:** Curious, pragmatic, socially observant. Motivation is to stop being the person who only survives and become someone capable of building a stable place. Flaw: over-adapts to others and delays choosing a personal direction.

**Recruitment:** First permanent recruit after the opening crisis. No rehabilitation gate.

**Relationships:** Deepest bond with Inadaptada; meaningful exploratory friendship with Caçadora.

**H direction:** Starts shy/uncertain about receiving attention; becomes more confident when trust is demonstrated. Prefers responsive, relationship-driven progression. H content should emphasize mutual trust and the contrast between adaptability and having personal wants.

### ALLY-002 — Guardiã
**Identity:** Minotauroid, Futanari, very tall, large horns, muscular-athletic adult build. Practical protective equipment, minimal ornamentation.

**Base attributes:** Body 68 / Agility 31 / Soul 28 / Charm 25 / Dominance 55 / Submission 22 / Sadism 35 / Masochism 30.

**Aptitudes:** Body 5, Agility 2, Soul 2, Charm 2, Dominance 4, Submission 2, Sadism 3, Masochism 3.

**Preferred functions:** Security, Training, frontline combat.

**Starting skills:** `Guard`, `Interception`, `Brace`.

**Signature mechanic — Guard + Interception:** Marked allies receive a portion of attacks redirected to Guardiã; interception becomes stronger when protecting a lower-Body ally.

**Growth identity:** Gains additional natural growth when successfully preventing damage or completing security/training assignments.

**Narrative:** Disciplined, protective, reserved. Motivation is to ensure nobody under her protection is abandoned. Flaw: assumes responsibility for problems that should be delegated.

**Recruitment:** Joins after a community-defense crisis establishes trust in Alya's leadership.

**Relationships:** Cuidadora is her trusted practical counterpart; Rival is an ideological and competitive foil.

**H direction:** Reserved until trust. Strong preference for deliberate progression, reassurance and controlled vulnerability; avoid making her meek. Her appeal is that the protector chooses when to lower her guard.

### ALLY-003 — Rival
**Identity:** Predatory beastfolk, Feminine, tall athletic-curvy adult. Distinctive ears/tail, travel gear adapted for speed and intimidation.

**Base attributes:** Body 58 / Agility 57 / Soul 20 / Charm 34 / Dominance 61 / Submission 18 / Sadism 48 / Masochism 24.

**Aptitudes:** Body 4, Agility 5, Soul 1, Charm 3, Dominance 5, Submission 1, Sadism 4, Masochism 2.

**Preferred functions:** Crisis management, combat leadership, rapid-response assignments.

**Starting skills:** `Breakthrough`, `Pursuit`, `Pressure`.

**Signature mechanic — Fury + Momentum:** Gains Momentum when attacking an enemy who is stronger or when an ally is incapacitated; Fury converts Momentum into stronger follow-up actions. Momentum decays if she spends a turn without meaningful action.

**Growth identity:** Excels through difficult encounters and crisis assignments rather than routine work.

**Narrative:** Competitive, confrontational, pragmatic. Motivation is to prove that her harsher survival philosophy works. Flaw: interprets compromise as weakness until shown concrete results.

**Recruitment:** Initially leads a competing group and obstructs expansion; later becomes recruitable after a conflict exposes the limits of her approach.

**Relationships:** Rivalry with Guardiã; direct ideological conflict and eventual respect with Alya.

**H direction:** Provocative/competitive. Trust grows through challenge, competence and honest confrontation. H content should preserve her agency and competitive personality rather than turning her into a generic submissive archetype.

### ALLY-004 — Erudita
**Identity:** Original arcane humanoid species, Feminine, average-tall slim adult. Distinctive luminous markings and practical research attire.

**Base attributes:** Body 24 / Agility 30 / Soul 70 / Charm 31 / Dominance 43 / Submission 27 / Sadism 32 / Masochism 25.

**Aptitudes:** Body 1, Agility 2, Soul 5, Charm 3, Dominance 4, Submission 2, Sadism 3, Masochism 2.

**Preferred functions:** Research, Alchemy, magical analysis.

**Starting skills:** `Arcane Bolt`, `Analyze`, `Study Creatures`.

**Signature mechanic — Study Creatures:** Repeatedly observing/encountering a creature family unlocks additional knowledge bonuses against that family and can improve expedition analysis.

**Growth identity:** Strongly rewards experimentation, discovery and successful research rather than repetition of a single safe action.

**Narrative:** Eccentric, obsessive, brilliant. Motivation is understanding magic, biology and the Ferida. Flaw: curiosity can override social tact and risk assessment.

**Recruitment:** Recruited through research collaboration; her continued presence requires a functioning research/alchemy environment.

**Relationships:** Strong intellectual bond with Artesã; unusual protective curiosity toward Inadaptada.

**H direction:** Curious/experimental, but trust-gated. Keep her intellectual identity central; intimacy should be framed as another domain she learns to understand rather than reducing her to experimentation.

### ALLY-005 — Cuidadora
**Identity:** Human, Futanari, average-height curvy-athletic adult. Practical medical clothing, organized tools, confident posture.

**Base attributes:** Body 47 / Agility 28 / Soul 55 / Charm 35 / Dominance 34 / Submission 29 / Sadism 18 / Masochism 34.

**Aptitudes:** Body 3, Agility 2, Soul 5, Charm 3, Dominance 3, Submission 2, Sadism 1, Masochism 4.

**Preferred functions:** Health, Recovery, prevention.

**Starting skills:** `Diagnose`, `Restore`, `Stabilize`.

**Signature mechanic — Diagnosis + Prevention:** Correctly identifying a condition before treatment improves recovery efficiency and reduces recurrence of that condition in the community.

**Growth identity:** Gains strong natural growth from successful treatment, prevention and recovery assignments.

**Narrative:** Practical, objective, authoritative. Motivation is to make survival less dependent on luck. Flaw: can become controlling when she thinks others are making avoidable mistakes.

**Recruitment:** Joins after Alya helps resolve a shortage/crisis in local care.

**Relationships:** Deep trust with Guardiã; supportive spiritual contrast with Devoto.

**H direction:** Practical and comfortable once trust exists. H content should emphasize communication, care and competence rather than making her primarily eroticized by profession.

### ALLY-006 — Artesã
**Identity:** Goblin, Feminine, short-average adult with compact-athletic build. Large tool belt, asymmetrical practical gear, expressive hands.

**Base attributes:** Body 35 / Agility 43 / Soul 48 / Charm 39 / Dominance 29 / Submission 31 / Sadism 29 / Masochism 30.

**Aptitudes:** Body 3, Agility 4, Soul 4, Charm 3, Dominance 2, Submission 3, Sadism 2, Masochism 3.

**Preferred functions:** Construction, production, equipment modification.

**Starting skills:** `Improvised Device`, `Tripwire`, `Modify Equipment`.

**Signature mechanic — Workshop Improvisation:** Can alter construction/equipment recipes at the workshop to trade one resource for another or add a controlled secondary property. Outside combat this is a core identity; in combat she uses utility/control effects rather than trap spam.

**Growth identity:** Gains development from successful builds, repairs and modifications.

**Narrative:** Chaotic inventor, playful, proud. Motivation is to prove that clever design can beat scarcity. Flaw: underestimates maintenance and sometimes creates solutions nobody asked for.

**Recruitment:** Recruited through a construction/equipment problem where conventional solutions fail.

**Relationships:** Intellectual chemistry with Erudita; commercial friction/friendship with Mercador.

**H direction:** Playful and inventive, comfortable with experimentation after trust. Preserve adult confidence and avoid childish visual coding despite the Goblin species.

### ALLY-007 — Caçadora
**Identity:** Fox beastfolk, Futanari, average-height lean-athletic adult. Bow, field gear, expressive ears/tail, quiet stance.

**Base attributes:** Body 36 / Agility 62 / Soul 26 / Charm 39 / Dominance 36 / Submission 27 / Sadism 38 / Masochism 26.

**Aptitudes:** Body 3, Agility 5, Soul 2, Charm 4, Dominance 3, Submission 2, Sadism 4, Masochism 2.

**Preferred functions:** Expeditions, exploration, scouting.

**Starting skills:** `Aimed Shot`, `Snare`, `Track`.

**Signature mechanic — Hunt & Discovery:** Expedition results gain a chance to reveal special locations/events and reduce risk when the expedition passes through known hunting/exploration conditions. It is a bonus, not a mandatory gate.

**Growth identity:** Strong natural growth from successful exploration, scouting and varied field encounters.

**Narrative:** Quiet, observant, provocative/playful when comfortable. Motivation is to understand the world through direct experience. Flaw: avoids difficult emotional conversations by turning them into jokes or practical tasks.

**Recruitment:** Encountered through exploration and gradually convinced to invest in the community.

**Relationships:** Quietly close with First Ally.

**H direction:** Provocative but comfortable; confidence should increase through mutual trust rather than a personality replacement.

### ALLY-008 — Mercador
**Identity:** Feline beastfolk, Femboy, average-height slim adult. Polished travel clothes, jewelry, portable ledgers and expressive smile.

**Base attributes:** Body 29 / Agility 36 / Soul 34 / Charm 67 / Dominance 40 / Submission 28 / Sadism 31 / Masochism 25.

**Aptitudes:** Body 2, Agility 3, Soul 3, Charm 5, Dominance 4, Submission 2, Sadism 3, Masochism 2.

**Preferred functions:** Commerce, Economy, trade opportunities.

**Starting skills:** `Bargain`, `Distract`.

**Signature mechanic — Commercial Network:** Improves vendor availability/prices, generates occasional trade opportunities and increases the value of selected community outputs. Combat contribution remains intentionally low.

**Growth identity:** Grows through successful trade, negotiations and economic optimization.

**Narrative:** Charming, persuasive trickster. Motivation is to build the region's most profitable commercial network. Flaw: defaults to manipulation even when sincerity would work better.

**Recruitment:** Recruited through trade negotiations and an opportunity to profit from the growing community.

**Relationships:** Strong commercial friendship with Artesã; complementary tension with Devoto.

**H direction:** Charming/manipulative at first, then increasingly sincere. Keep consent and negotiation central to his characterization.

### ALLY-009 — Inadaptada
**Identity:** Rare/exotic poorly understood humanoid species, Futanari, average-height adult with unusual but proportionate features. Silhouette should be immediately distinct without becoming animal-dominant.

**Base attributes:** Body 27 / Agility 34 / Soul 39 / Charm 23 / Dominance 22 / Submission 49 / Sadism 24 / Masochism 47.

**Aptitudes:** Body 3, Agility 4, Soul 4, Charm 4, Dominance 3, Submission 5, Sadism 3, Masochism 5.

**Preferred functions:** Negotiation, interpersonal relations, flexible long-term development.

**Starting skills:** `Observe`, `Improvise`, `Learn from Failure`.

**Signature mechanic — Exceptional Learning / Adaptation:** Starts below most allies in raw power but receives accelerated natural-growth gains from varied contexts. Learning one function never permanently erases previous development, enabling unusual hybrid builds.

**Growth identity:** Highest long-term flexibility in roster; weakest early specialist performance.

**Narrative:** Shy, determined, insecure. Motivation is to discover where she belongs. Flaw: assumes rejection before it happens.

**Recruitment:** Optional sidequest chain; recruitment is not mandatory for main progression.

**Relationships:** First Ally is her safest interpersonal anchor; Erudita becomes fascinated by her unusual development.

**H direction:** Shy initially, increasingly confident as social security develops. Intimacy should mirror the character arc from fear of rejection to self-directed desire and boundaries.

### ALLY-010 — Devoto
**Identity:** Faerie-like humanoid, Feminine, average-height soft-curvy adult. Luminous details, modest ceremonial clothing, warm expressive face.

**Base attributes:** Body 41 / Agility 29 / Soul 56 / Charm 58 / Dominance 32 / Submission 36 / Sadism 17 / Masochism 39.

**Aptitudes:** Body 3, Agility 2, Soul 5, Charm 5, Dominance 2, Submission 4, Sadism 1, Masochism 4.

**Preferred functions:** Morale, mediation, integration, welfare and social cohesion.

**Starting skills:** `Protective Blessing`, `Inspire`, `Reconcile`.

**Signature mechanic — Community Faith:** Protective/buff effects become stronger when the community has high cohesion and when Devoto has personally resolved or supported a meaningful conflict. This is social support, not religious power scaling.

**Growth identity:** Grows through successful mediation, morale support and integration of difficult residents.

**Narrative:** Idealistic, empathetic, optimistic. Motivation is to make people believe cooperation is possible. Flaw: can forgive too quickly and underestimate repeated harmful behavior.

**Recruitment:** Joins after helping resolve a community conflict or integration problem.

**Relationships:** Complements Mercador; develops a patient friendship with Inadaptada; supportive link to Cuidadora.

**H direction:** Shy initially, comfortable after trust. Intimacy should emphasize emotional safety, affection and the tension between idealism and personal desire.

## 4. NPC data model

NPCs never participate in combat while functioning as NPCs. Their concrete data therefore does **not** assign combat stats, combat skills or combat loadouts.

For implementation, Named NPCs use a lightweight profile:
- **Influence:** 1–5, affects social/quest leverage.
- **Expertise:** one primary domain plus optional secondary domain.
- **Relationship depth:** 0–100 with Alya and selected NPCs.
- **Quest importance:** H0–H4 content tier.
- **Availability:** location/state conditions.
- **Departure condition:** none / conditional / scheduled.
- **Recruitment eligibility:** false by default; only true where a future concrete story path exists.

### NPC profile ratings
`Influence 1–5` is not a combat stat. It measures how much leverage the NPC can exert through authority, information, reputation, resources or social access.

## 5. Named NPCs — concrete alpha

| ID | Concept | Species | Presentation | Adult age | H | Influence | Expertise | Core personality / motivation |
|---|---|---|---|---|---|---:|---|---|
| NPC-001 | Tavernkeeper | Human | Futanari | Mature adult | H3 | 3 | Hospitality / rumors | Warm, practical; wants a safe social center |
| NPC-002 | Dancer | Desert Elf | Feminine | Young adult | H2/H3 | 2 | Entertainment / social events | Energetic, observant; wants freedom and a stable audience |
| NPC-003 | Community Elder | Human | Feminine | Mature adult | H3 | 5 | History / memory | Patient, firm; wants the community to retain identity |
| NPC-004 | Mediator | Human | Futanari | Mature young adult | H2/H3 | 4 | Mediation / dispute resolution | Calm, analytical; wants conflicts solved before they become crises |
| NPC-005 | Pragmatic Mentor | Human | Feminine | Mature adult | H3 | 4 | Organization / training | Direct, competent; wants Alya to learn sustainable leadership |
| NPC-006 | Institutional Representative | Human | Femboy | Young adult | H3 | 4 | Protocol / negotiation | Polished, procedural; wants a workable organization-community relationship |
| NPC-007 | Ferida Researcher | Augmented | Feminine | Mature young adult | H3 | 3 | Ferida research / investigation | Intense, methodical; wants evidence rather than superstition |
| NPC-008 | Hardliner | Human | Futanari | Mature adult | H3/H4 | 5 | Enforcement / policy | Severe, utilitarian; wants predictable regional security |
| NPC-009 | Regional Authority | Angel | Feminine | Mature adult | H3 | 5 | Governance / legitimacy | Formal, fair; wants regional stability |
| NPC-010 | Trade Representative | Lamia | Futanari | Young adult | H2/H3 | 4 | Trade / routes | Shrewd, sociable; wants profitable stable routes |
| NPC-011 | Priestess | Human | Feminine | Mature young adult | H3 | 3 | Spiritual counsel / rites | Traditional but genuinely compassionate; wants people to retain hope |
| NPC-012 | Tribal Matriarch | Mycelia | Feminine | Mature adult | H3 | 5 | Tribal leadership / spirituality | Contemplative, authoritative; protects tribal continuity |
| NPC-013 | Tribal Guide | Mycelia | Futanari | Young adult | H2/H3 | 3 | Exploration / mediation | Curious, grounded; wants safe contact with outsiders |
| NPC-014 | War-Chief | Orc | Futanari | Mature adult | H3 | 5 | Strength/status / rites | Proud, honorable, demanding; wants worthy leadership |
| NPC-015 | EnemyCommander | Human | Futanari | Mature adult | H3/H4 | 5 | Military organization | Disciplined, calculating; believes order prevents catastrophe |
| NPC-016 | Faction Dissident | Human | Femboy | Young adult | H3 | 2 | Internal politics / intelligence | Nervous, idealistic; wants reform without destroying his faction |
| NPC-017 | Ferida Manipulator | Fallen Angel | Feminine | Mature adult | H4 | 5 | Psychological manipulation / Ferida | Charismatic, cruel, patient; wants people to choose corruption themselves |
| NPC-018 | Reaper | Dullahan | Feminine | Ageless-presenting adult | H3/H4 | 4 | Thresholds / death mysteries | Detached, enigmatic; wants balance between endings and unfinished business |
| NPC-019 | Dryad | Dryad | Feminine | Mature young adult | H3 | 3 | Nature / ecology | Calm, sensual, protective; wants ecosystems to remain reciprocal |
| NPC-021 | Survivor | Orc | Futanari | Mature young adult | H2/H3 | 2 | Recovery / regional consequences | Guarded, resilient; wants a place where survival is not a permanent emergency |
| NPC-022 | Demonkin | Demon | Futanari | Young adult | H3/H4 | 3 | Rehabilitation / legacy conflict | Defensive, volatile, vulnerable; wants proof that origin does not determine destiny |

### NPC-001 — Tavernkeeper
- **Location:** Starting community; later may travel to regional hub during expansion.
- **Function:** Tavern, rumors, social gathering, minor services and community information.
- **Quest hooks:** missing travelers, rumors, disputes, morale events.
- **Relationship arc:** distrust of outsiders -> practical trust -> community confidant.
- **Departure:** only if community collapses or player explicitly neglects the tavern through a severe state.
- **Recruitment:** never by default.
- **H:** H3. Warm, experienced, playful; adult intimacy should feel grounded in social trust.

### NPC-002 — Dancer
- **Visual:** Desert Elf, darker skin, athletic adult body, elegant movement-focused clothing.
- **Function:** Entertainment, festival/event participation, rumor circulation through visitors.
- **Quest hooks:** performance opportunity, cultural misunderstanding, traveling troupe.
- **Relationship arc:** treats Alya as an audience -> collaborator -> trusted friend.
- **H:** H2/H3 depending narrative relevance. Sensual performance is character expression, not automatic consent to intimacy.

### NPC-003 — Community Elder
- **Visual:** Human, mature adult rather than elderly-coded.
- **Function:** historical context, memory, legitimacy and mediation.
- **Quest hooks:** old agreements, forgotten locations, community traditions.
- **Relationship arc:** tests Alya's commitment -> recognizes leadership -> becomes institutional memory.
- **H:** H3, mature and emotionally grounded.

### NPC-004 — Mediator
- **Function:** resolves recurring resident disputes and exposes hidden community-state problems.
- **Relationship arc:** professional neutrality -> respect -> confidant.
- **H:** H2/H3, trust and emotional intimacy focused.

### NPC-005 — Pragmatic Mentor
- **Function:** organization-side mentor; teaches sustainable delegation and institutional realities.
- **Relationship arc:** evaluates Alya -> challenges her -> becomes one of her most useful institutional allies.
- **H:** H3, mature and deliberate.

### NPC-006 — Institutional Representative
- **Function:** formal interface with the organization, contracts, protocols and negotiations.
- **Relationship arc:** polite procedural distance -> genuine respect -> conflicted loyalty during organizational rupture.
- **H:** H3, controlled/public composure contrasted with private vulnerability.

### NPC-007 — Ferida Researcher
- **Function:** specialist information, investigations and controlled research.
- **Relationship arc:** skepticism -> collaboration -> moral conflict when evidence conflicts with institutional priorities.
- **H:** H3, intellectually driven but consent-conscious.

### NPC-008 — Hardliner
- **Function:** recurring political pressure and enforcement.
- **Relationship arc:** sees Alya as dangerous exception -> direct adversary -> possible reluctant respect depending choices.
- **Departure:** can be reassigned away after major political failures.
- **H:** H3/H4 only if narrative relevance justifies it; not automatically sympathetic.

### NPC-009 — Regional Authority
- **Function:** governance, legitimacy, permits, regional decisions and political consequences.
- **Relationship arc:** formal evaluation -> earned legitimacy -> political partnership.
- **H:** H3; dignified, controlled and adult.

### NPC-010 — Trade Representative
- **Function:** trade routes, market opportunities, regional commerce.
- **Relationship arc:** evaluates community as a market -> becomes a recurring partner.
- **H:** H2/H3; playful negotiation and trust.

### NPC-011 — Priestess
- **Function:** spiritual community, rites, counsel and hope.
- **Design:** traditional but genuinely compassionate; not a hypocritical caricature.
- **Relationship arc:** tests whether Alya respects belief -> offers counsel -> becomes a bridge between secular and spiritual residents.
- **H:** H3, affection and vulnerability rather than coercive religious framing.

### NPC-012 — Tribal Matriarch
- **Function:** Tribe A leadership, spiritual authority and diplomatic gate.
- **Culture:** matriarchal spiritual society.
- **Relationship arc:** cautious diplomacy -> cultural exchange -> alliance.
- **H:** H3; ceremonial/relational tone.

### NPC-013 — Tribal Guide
- **Function:** exploration, cultural mediation and safe navigation.
- **Relationship arc:** curious intermediary -> trusted bridge between communities.
- **H:** H2/H3; adventurous, warm.

### NPC-014 — War-Chief
- **Function:** Tribe B leadership, strength/status challenges, duels and rites of passage as social structures rather than combat participation while NPC.
- **Culture:** strength/status + duels/rites of passage.
- **Relationship arc:** judges Alya through actions -> respect -> alliance.
- **H:** H3; pride, challenge and earned respect.

### NPC-015 — EnemyCommander
- **Function:** recurring adversarial commander. When a combat encounter requires this identity, a separate Enemy/Boss representation is used; the NPC instance itself never enters combat.
- **Relationship arc:** strategic opposition -> ideological dialogue -> possible divergence from faction depending story state.
- **H:** H3/H4 based on narrative importance, not combat rank.

### NPC-016 — Faction Dissident
- **Function:** internal opposition perspective, intelligence and alternative resolution path.
- **Relationship arc:** frightened contact -> reluctant informant -> potential political ally.
- **H:** H3, vulnerability and trust.

### NPC-017 — Ferida Manipulator
- **Function:** major H4 antagonist and psychological pressure point.
- **Relationship arc:** fascination -> manipulation -> direct ideological conflict.
- **H:** H4. Content should emphasize agency, temptation and psychological stakes without making coercion the default framing.

### NPC-018 — Reaper
- **Function:** neutral recurring mystery around death, thresholds and unfinished business.
- **Design:** clear clues accompany mystery; avoid arbitrary cryptic behavior.
- **Relationship arc:** curiosity -> mutual recognition -> conditional trust.
- **H:** H3/H4 depending narrative prominence; supernatural, emotionally distant and unusual.

### NPC-019 — Dryad
- **Function:** nature/ecology quests, exploration hooks and environmental consequences.
- **Relationship arc:** tests whether community behavior is reciprocal -> ally in ecological matters.
- **H:** H3; sensuality tied to nature and reciprocity, not mindless seduction.

### NPC-021 — Survivor
- **Function:** demonstrates consequences of regional conflict and provides recovery/integration quests.
- **Relationship arc:** guarded dependence -> practical trust -> stable community role.
- **H:** H2/H3; vulnerability requires especially careful consent and emotional pacing.

### NPC-022 — Demonkin
- **Function:** rehabilitation, legacy conflict and proof that origin does not dictate behavior.
- **Relationship arc:** fear/defensiveness -> controlled integration -> independent identity.
- **H:** H3/H4; content should follow trust and recovery rather than treating rehabilitation as sexual reward.

## 6. Relationship rules

Named relationships use a 0–100 internal relationship value plus discrete narrative states. Recommended state bands:

- 0–19 Hostile / Avoidant
- 20–39 Distant
- 40–59 Familiar
- 60–74 Trusted
- 75–89 Close
- 90–100 Intimate / Deep bond

A numerical relationship value never overrides a narrative lock, consent condition, quest state or character-specific boundary.

For allies, relationship values are used only for selected deep relationships, not a full matrix. The alpha deep links are:

- First Ally ↔ Inadaptada
- First Ally ↔ Caçadora
- Guardiã ↔ Cuidadora
- Guardiã ↔ Rival
- Erudita ↔ Artesã
- Erudita ↔ Inadaptada
- Cuidadora ↔ Devoto
- Artesã ↔ Mercador
- Mercador ↔ Devoto
- Inadaptada ↔ Devoto
- Rival ↔ Alya

## 7. NPC location / state defaults

| NPC | Initial scope | Movement | Persistence |
|---|---|---|---|
| Tavernkeeper | Community | Community ↔ regional hub | Persistent unless severe departure condition |
| Dancer | Community | Travel events / hubs | Persistent, may travel |
| Community Elder | Community | Rarely moves | Persistent |
| Mediator | Community | Community only | Persistent |
| Pragmatic Mentor | Organization | Organization ↔ community | Persistent recurring |
| Institutional Representative | Organization | Regional hubs ↔ community | Persistent until reassignment |
| Ferida Researcher | Organization | Research sites | Persistent recurring |
| Hardliner | Organization | Regional political sites | Conditional |
| Regional Authority | Regional Center | Regional center ↔ diplomatic visits | Persistent |
| Trade Representative | Regional Center | Trade routes | Mobile |
| Priestess | Regional Center | Religious sites / community visits | Persistent |
| Tribal Matriarch | Tribe A | Tribe A territory | Persistent |
| Tribal Guide | Tribe A | Tribe A ↔ exploration areas | Mobile |
| War-Chief | Tribe B | Tribe B territory | Persistent |
| EnemyCommander | Adversarial | Enemy-controlled areas / diplomatic scenes | Persistent while faction exists |
| Faction Dissident | Adversarial | Hidden cells / hubs | Conditional |
| Ferida Manipulator | Adversarial | Story-driven | Persistent major antagonist |
| Reaper | World | Contextual | Recurring conditional |
| Dryad | World | Natural sites | Recurring |
| Survivor | World | Community ↔ recovery sites | Conditional |
| Demonkin | Demon / World | Recovery/community | Conditional after rescue |

## 8. Visual production defaults

Every Named character needs:
1. full-body reference;
2. portrait/expression sheet;
3. world sprite or equivalent representation;
4. combat representation only when a separate Enemy/Boss identity is required;
5. H assets according to tier and narrative importance.

### Visual constraints
- All characters must read unmistakably adult.
- Do not use child-coded proportions or terminology.
- Do not use `petite` as a body category.
- Beastfolk remain clearly humanoid and a minority of the cast.
- Species, culture and gameplay function remain separate design axes.
- Mature characters should look mature without requiring elderly caricature.

## 9. Alpha balance audit

### Strengths
- The eight-stat architecture maps cleanly onto all ten allies.
- Every ally has at least one strong identity axis and one useful community role.
- Mercador and Inadaptada deliberately occupy low-raw-combat niches without being useless.
- Erudita remains a **pure Mage** rather than becoming a hybrid.
- Guardiã, Rival and Caçadora provide clearly different physical combat identities.
- Cuidadora and Devoto are mechanically distinct: recovery/treatment versus protection/cohesion.
- Artesã owns construction/modification utility rather than becoming another combat trap specialist.
- NPCs do not need combat stats, preventing the NPC roster from becoming a second hidden character-combat system.

### Tuning risks to monitor
1. Charm can become a universal social/H stat if every dialogue check uses it; keep quest outcomes context-specific.
2. Soul may dominate magical and H resistance simultaneously; equipment and skills should create counterplay.
3. Inadaptada's accelerated growth must not create runaway late-game superiority; cap the rate of learning, not the final potential.
4. Guardiã's interception should have a clear mitigation ceiling so multi-hit enemies do not make her mandatory.
5. Rival's disadvantage mechanic must reward controlled risk rather than intentional self-sabotage.
6. Devoto's cohesion scaling must remain useful even when community morale is already high.
7. Mercador's economy bonuses must affect opportunity and choice, not trivialize gold scarcity.

## 10. Implementation-ready decisions

The following are now considered **ALPHA-LOCKED** for implementation unless a concrete integration problem appears:

- Primary attribute scale: 1–100.
- Eight primary attributes only.
- Ally starting stat profiles and aptitude profiles in this document.
- Ally functional identities and signatures.
- NPCs use influence/expertise/relationship profiles instead of combat stats.
- NPC combat boundary remains absolute while they are NPCs.
- Relationship band model and sparse deep-link map.
- Adult visual-safety constraints.
- NPC movement/persistence defaults.
- H tiers as relevance-driven content scope.

Still intentionally tunable:
- exact damage/healing/H formulas;
- exact level curve and natural-growth numerical gains;
- exact Skill Point costs;
- exact skill coefficients and effect durations;
- exact equipment modifiers;
- quest-specific relationship deltas;
- exact H scene count and asset IDs;
- final dialogue and localization.

## Verdict

**PASS — Character Data Alpha is sufficient to begin implementation and first-pass character production.** Further work should now consume these values rather than reopen the character architecture. Balance changes should be made through data/tuning unless a demonstrated system gap requires architectural change.
