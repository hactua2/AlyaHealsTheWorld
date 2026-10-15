#!/usr/bin/env python3
"""Static structural validation for the authored full-game content catalogs."""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
WORLD_PATH = ROOT / "data/content/full_game_world_catalog.json"
GAMEPLAY_PATH = ROOT / "data/content/full_game_gameplay_catalog.json"
CHARACTER_PATH = ROOT / "data/content/full_game_character_arcs.json"


def load(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"{path.relative_to(ROOT)}: {exc}") from exc


def records(data):
    return [
        record
        for value in data.values()
        if isinstance(value, list)
        for record in value
        if isinstance(record, dict) and isinstance(record.get("id"), str)
    ]


def duplicate_ids(data):
    ids = [record["id"] for record in records(data)]
    seen = set()
    duplicates = set()
    for item in ids:
        if item in seen:
            duplicates.add(item)
        seen.add(item)
    return sorted(duplicates)


def validate_data(world, gameplay, characters):
    errors = []
    for label, data in (
        ("world catalog", world),
        ("gameplay catalog", gameplay),
        ("character catalog", characters),
    ):
        for duplicate in duplicate_ids(data):
            errors.append(f"{label}: duplicate ID {duplicate}")

    acts = {item["id"] for item in world.get("acts", [])}
    regions = {item["id"] for item in world.get("regions", [])}
    quests = {item["id"] for item in world.get("mainQuests", [])}
    enemies = {item["id"] for item in gameplay.get("enemies", [])}
    bosses = {item["id"] for item in gameplay.get("bosses", [])}
    specials = {item["id"] for item in gameplay.get("specialEncounters", [])}

    expected_counts = (
        (world, "acts", 5),
        (world, "regions", 7),
        (world, "factions", 6),
        (world, "mainQuests", 47),
        (world, "sidequests", 25),
        (world, "expeditions", 8),
        (world, "endings", 5),
        (gameplay, "enemies", 35),
        (gameplay, "bosses", 9),
        (gameplay, "specialEncounters", 8),
        (gameplay, "facilities", 12),
        (gameplay, "resources", 8),
        (gameplay, "items", 36),
        (gameplay, "outfits", 8),
        (characters, "allies", 10),
        (characters, "namedNpcs", 21),
        (characters, "genericNpcTemplates", 12),
    )
    for data, key, expected in expected_counts:
        actual = len(data.get(key, []))
        if actual != expected:
            errors.append(f"{key}: expected {expected}, got {actual}")

    main_quests = world.get("mainQuests", [])
    sequences = sorted(item.get("sequence") for item in main_quests)
    if sequences != list(range(1, 48)):
        errors.append("mainQuests: sequence must be contiguous from 1 to 47")

    for quest in main_quests:
        qid = quest.get("id", "<missing-id>")
        if quest.get("act") not in acts:
            errors.append(f"{qid}: unresolved act {quest.get('act')}")
        if not quest.get("regionIds") or any(region not in regions for region in quest.get("regionIds", [])):
            errors.append(f"{qid}: missing or unresolved regionIds")
        if any(prereq not in quests for prereq in quest.get("prerequisiteQuestIds", [])):
            errors.append(f"{qid}: unresolved prerequisiteQuestIds")
        if any(encounter not in enemies | bosses | specials for encounter in quest.get("encounterIds", [])):
            errors.append(f"{qid}: unresolved encounterIds")
        for key in ("objectiveSteps", "keyChoice", "consequence", "rewardIntent", "exitFlag", "failurePolicy", "dialogueKeys"):
            if not quest.get(key):
                errors.append(f"{qid}: missing {key}")
        if quest.get("sequence", 99) <= 11:
            expected_slice_id = f"VS1_Q{quest['sequence']:02d}"
            if quest.get("verticalSliceId") != expected_slice_id:
                errors.append(f"{qid}: expected verticalSliceId {expected_slice_id}")

    for sidequest in world.get("sidequests", []):
        sid = sidequest.get("id", "<missing-id>")
        if any(prereq not in quests for prereq in sidequest.get("prerequisiteQuestIds", [])):
            errors.append(f"{sid}: unresolved prerequisiteQuestIds")
        if not sidequest.get("regionIds") or any(region not in regions for region in sidequest.get("regionIds", [])):
            errors.append(f"{sid}: missing or unresolved regionIds")
        for key in ("objective", "rewardIntent", "failurePolicy", "dialogueKeys"):
            if not sidequest.get(key):
                errors.append(f"{sid}: missing {key}")

    for boss in gameplay.get("bosses", []):
        bid = boss.get("id", "<missing-id>")
        import re
        for enemy_id in re.findall(r"ENM-\d{3}", boss.get("composition", "")):
            if enemy_id not in enemies:
                errors.append(f"{bid}: unresolved enemy composition reference {enemy_id}")

    for region in world.get("regions", []):
        if not region.get("pois") or not region.get("encounterPool"):
            errors.append(f"{region.get('id', '<missing-id>')}: missing POIs or encounter pool")
        for enemy_id in region.get("encounterPool", []):
            if enemy_id not in enemies:
                errors.append(f"{region.get('id')}: unresolved encounter pool enemy {enemy_id}")

    for item in gameplay.get("items", []):
        for key in ("name", "slot", "identity"):
            if not item.get(key):
                errors.append(f"{item.get('id', '<missing-id>')}: missing {key}")

    for npc in characters.get("namedNpcs", []):
        if npc.get("id") == "NPC-020":
            errors.append("NPC-020 is retired and must not be reused")

    return errors


def validate():
    try:
        world = load(WORLD_PATH)
        gameplay = load(GAMEPLAY_PATH)
        characters = load(CHARACTER_PATH)
    except ValueError as exc:
        print(f"FAIL: {exc}")
        return 1

    errors = validate_data(world, gameplay, characters)
    if errors:
        print("FAIL: full-game content catalogs")
        print("\n".join(f"- {error}" for error in errors))
        return 1

    print(
        "PASS: 5 acts, 47 main quests, 25 sidequests, 7 regions, 6 factions, "
        "35 enemies, 9 bosses, 12 facilities, 36 items, 10 allies, 21 named NPCs; "
        "IDs and cross-references validated."
    )
    return 0


if __name__ == "__main__":
    sys.exit(validate())
