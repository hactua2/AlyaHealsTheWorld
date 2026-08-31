# Asset Gap List — Production Baseline

## Purpose

This is the current production baseline for art/visual assets. It is intentionally organized by **required asset family**, not by arbitrary file count. It becomes the definitive file-level checklist after content locks and the existing-asset registry are completed.

## Status vocabulary

- **LOCKED** — upstream content is final.
- **AUDIT** — existing assets must be classified.
- **MISSING** — requirement is known but no acceptable asset is mapped yet.
- **DEPENDENT** — cannot be finalized until another content category is locked.

## Current list

### Alya / protagonist
- [ ] Base character reference — AUDIT
- [ ] Default outfit — AUDIT
- [ ] Nude state — AUDIT
- [ ] Slave outfit/state — AUDIT
- [ ] Shibari outfit/state — AUDIT
- [ ] CowPrint outfit — AUDIT
- [ ] Dancer outfit — AUDIT
- [ ] Witch outfit — AUDIT
- [ ] Armor outfit — AUDIT
- [ ] Nun outfit — AUDIT
- [ ] Dress outfit — AUDIT
- [ ] Demon Armor outfit — AUDIT
- [ ] Required portrait variants — DEPENDENT
- [ ] Required battle variants — DEPENDENT
- [ ] Required expression set — DEPENDENT

### Skills
- [ ] Icon for every final skill — DEPENDENT
- [ ] Cut-in for every skill classified as cut-in eligible — DEPENDENT
- [ ] VFX/presentation package per skill family — DEPENDENT

### Recruitable allies
- [ ] Character design/reference for each final ally — DEPENDENT
- [ ] Portrait for each final ally — DEPENDENT
- [ ] Battle representation for each combatant — DEPENDENT
- [ ] Expressions/variants where required — DEPENDENT
- [ ] Outfit variants where required — DEPENDENT

### Named NPCs
- [ ] Character design/reference per final named NPC — DEPENDENT
- [ ] Portraits — DEPENDENT
- [ ] Expressions — DEPENDENT
- [ ] Battle representation for combatants — DEPENDENT

### Generic NPC archetypes
- [ ] 8–15 reusable visual archetypes — DEPENDENT
- [ ] Controlled clothing/body/appearance variations — DEPENDENT

### Enemies
- [ ] Battle presentation for every final enemy type — DEPENDENT
- [ ] UI portrait/icon representation where required — DEPENDENT
- [ ] Elite/miniboss variants — DEPENDENT
- [ ] Boss presentation packages — DEPENDENT
- [ ] H-interaction presentation where applicable — DEPENDENT
- [ ] Enemy-family reusable bases/variants — DEPENDENT

### Items
- [ ] Icon for every final item — DEPENDENT
- [ ] Special presentation for build-defining items where required — DEPENDENT

### Facilities
- [ ] Facility icon for every logical facility — DEPENDENT
- [ ] Exterior visual family — DEPENDENT
- [ ] Interior/background where required — DEPENDENT
- [ ] Upgrade variants where visually meaningful — DEPENDENT

### World
- [ ] World-map asset set — DEPENDENT
- [ ] Region visual identities — DEPENDENT
- [ ] Exploration backgrounds — DEPENDENT
- [ ] Combat backgrounds — DEPENDENT
- [ ] Community/town backgrounds — DEPENDENT
- [ ] Special story locations — DEPENDENT

### Narrative / CG
- [ ] Major story CGs — DEPENDENT
- [ ] Relationship/character CGs — DEPENDENT
- [ ] High-value H-content CGs — DEPENDENT
- [ ] Selected event illustrations — DEPENDENT

### UI
- [ ] Status/effect icons — DEPENDENT
- [ ] Resource icons — DEPENDENT
- [ ] Currency icons — DEPENDENT
- [ ] Quest icons — DEPENDENT
- [ ] Facility icons — DEPENDENT
- [ ] Map/location icons — DEPENDENT
- [ ] Equipment-slot icons — DEPENDENT
- [ ] H-system UI graphics — DEPENDENT
- [ ] Progression/skill-tree graphics — DEPENDENT

## What is deliberately NOT listed as a separate art requirement yet

- One bespoke image per quest.
- One bespoke image per generic NPC.
- One unique building illustration per facility upgrade.
- One cut-in per passive skill.
- One unique background per encounter.
- One CG per H interaction.

These would be production bloat unless later content analysis demonstrates a real need.

## Finalization gate

This document becomes a file-level checklist only after:

`C2–C10 LOCKED → C11 asset registry → C12 final reconciliation`

At that point every row should become one of:

**KEEP / REFINE / REPLACE / MISSING / NOT REQUIRED**

with a stable content ID and production priority.
