# Game Core

## Purpose

This document defines the stable player-facing identity of the translated game. It is intentionally independent of replaceable art, audio, terminology, and cosmetic presentation.

## High concept

A light fantasy RPG in which the player grows from a relatively isolated protagonist into the leader of an expanding community. Exploration and turn-based conflict feed recruitment, assignment, base growth, character progression, and access to new regions.

## Player fantasy

The player should feel that every expedition can strengthen both the active party and the wider community. Progress is not limited to defeating enemies: conflicts may also end through loss of opposition and voluntary surrender, creating narrative opportunities for recruitment.

## Core loop

1. Prepare the party and review available community assignments.
2. Explore the current region.
3. Encounter combat, quests, discoveries, resources, or recruitable characters.
4. Resolve conflicts through Health depletion or Moral depletion.
5. If Moral reaches its surrender condition, enter a post-combat narrative resolution.
6. Gain resources, progress, allies, unlocks, or quest state.
7. Return to the base when desired or required.
8. Heal, equip, assign, integrate, build, improve, or dispatch community members.
9. Unlock new capabilities, content, and regions.
10. Repeat with increased strategic options.

## Core pillars

### Dual-path conflict resolution

Combat uses Health and Moral as independent resolution resources. Health depletion represents conventional defeat. Moral depletion leads to Surrender and a post-combat narrative resolution.

### Recruitment and community growth

Characters can join the player through explicit story or post-combat conditions. Recruited characters expand either active-party options, community functions, or both.

### Party versus base allocation

Available characters are not merely collectible. The player decides whether suitable characters participate directly in expeditions or contribute to persistent base systems.

### Data-driven progression

Characters, enemies, skills, equipment, quests, structures, regions, and presentation bindings must be represented as data rather than hardcoded one-off behavior.

### Presentation independence

Gameplay code must depend on IDs, tags, roles, states, and effects. Replaceable portraits, sprites, sounds, animation sets, UI themes, and display labels must be bound through a presentation layer.

## Canonical vocabulary

- **Health:** conventional combat endurance.
- **Moral:** willingness or capacity to continue opposition.
- **Surrender:** terminal Moral-resolution state.
- **Post-combat resolution:** dialogue/event state following Surrender.
- **Recruitment:** explicit addition of a character to the player's available roster.
- **Community:** all persistent characters and systems associated with the player's base.
- **Expedition:** a party or assigned group sent outside the base.

## Non-goals of this document

Exact balance values, village timings, production costs, probability formulas, and final presentation themes are not defined here unless later promoted to canonical design.
