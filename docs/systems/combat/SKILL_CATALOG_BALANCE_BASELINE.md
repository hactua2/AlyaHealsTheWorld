# Skill Catalog Balance Baseline
**Version:** 1.0.0-provisional. Numeric values are first-pass implementation defaults, not playtest-balanced.

## Formula
Weighted primary attributes are summed first. Then apply the matching Aspect affinity separately: `clamp(1 + affinity_percent/200, 1.0, 1.5)`. Multi-Aspect skills use the arithmetic mean; `All` means no affinity modifier. Round to nearest integer, halves away from zero; apply target resistance, vulnerability/debuff, cap, then mutate the meter.

## Progression and economy
- Tier 1/2/3 Skill Point cost: 1/2/3.
- Tier 1 no milestone gate; Tier 2 Act I complete; Tier 3 Act II complete; character prerequisites are additional.
- Active skill costs one action point. No extra actions are granted.
- Command cap 8; Resolve cap 4; Pressure cap 6; Fortitude cap 2.
- Default cooldown is zero unless explicitly raised in the CSV; multi-target and finishers use 1–4 action cooldowns.

## Baseline effects
- Focused Strain/Vitality outputs: base power 10/9 and tier output caps 24/32/40.
- Flirt: 0.65× base Strain and +2 Command; less efficient than specialist actions.
- DoTs: 4–5 Strain per target-turn for 2 turns; refresh max(remaining,new), no duplicate stacking.
- Area caps: Summon c-s total 48/per-target 24; G-bang group bonus max +30% and total cap 36; Summon Tentacles per-target cap 18.
- Finishers use 80% Strain baseline and request only encounter-permitted Yield/Disable/Capture; no implicit Defeat. Bkakke failure adds 12 Strain to Alya and victory requires every request to succeed.
- Overflow listener priority: S Symbol 10, Ecstasy Aftershocks 20, Overflow Engine 30; one event per affected actor/action; recursion guard; max chain depth 1.
- P-growth is persistent and Alya-only; dependent skills validate before costs commit.

## Required encounter balance scenarios
Single-target specialist vs Flirt vs Command; 1–6 targets for every AoE; Command→Break→control/finisher; Provoke→Dancing Moves→Counter/Endure; exposure→Resolve; Overflow normal crossing/repeated damage/lock expiry/multiple listeners; finisher below threshold/ineligible/partial success; P-growth absent/removed/ally; DoT first/final tick/reapplication/resistance/cleanse.
