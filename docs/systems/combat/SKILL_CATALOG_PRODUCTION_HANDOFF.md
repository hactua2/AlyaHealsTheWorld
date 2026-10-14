# Normalized Skill Catalog — Production Handoff
**Status:** normalized candidate on a dedicated branch; numbers provisional pending encounter playtests.

## Files
- `data/skills/skills.csv`: 67 canonical records with stable IDs; no blank rows; Enslave retained as a presentation alias of `ABSOLUTE_CONTROL`.
- `data/skills/skill_definitions.json`: structured requirements, targeting, resource costs/generation, effects, scaling, timing, Chain, Threshold, Overflow, outcomes, P-growth, and presentation.
- `tools/validate_skill_catalog.py`: static validator.
- `tests/test_skill_catalog.py`: six deterministic reference-model regression tests.
- `docs/systems/combat/SKILL_CATALOG_BALANCE_BASELINE.md`: provisional numeric baseline.

## Run validation
```sh
python tools/validate_skill_catalog.py
python -m unittest discover -s tests -p 'test_*.py' -v
```

Static validation checks count, unique IDs, CSV/JSON identity, required companion sections, scaling weight sums, P-growth gates, Overflow recursion guards, DoT lifecycle, friendly-fire scope, and finisher outcome requests. The unit tests are reference models, not full runtime integration tests.

## Release gate
1. Run scripts in CI and make failures block merges.
2. Integrate the companion definitions with the actual combat resolver.
3. Simulate encounters with 1–6 enemies and varied attribute/Aspect builds.
4. Tune damage, resource loops, resistance, cooldowns and costs using playtest data.
5. Verify persistence, UI, localization and enemy AI use the same stable IDs.
