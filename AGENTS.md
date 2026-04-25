# LLM Book Wiki Schema

This document provides the always-on context for managing the Book Wiki. 
The wiki is an auto-maintained knowledge base that tracks narrative elements.

## Core Rules
1. **Immutable Sources**: Never modify files in `raw/`. Only read from them.
2. **Wiki Ownership**: You own the `wiki/` directory. Maintain its consistency aggressively.
3. **Manuscript Assistance**: When assisting with the `manuscript/`, use the wiki to ensure strict continuity.
4. **Style Compliance**: Always read `wiki/style_guide.md` before writing or reviewing prose. All output must conform to the configured language, voice, and structure.

## Style & Configuration

The project's prose style, language, structure, and constraints are stored in `wiki/style_guide.md`. This file is populated by the `setup` skill and can be reconfigured at any time by re-running it. All writing and review agents must consult this file.

## Canonical Workflow

The recommended workflow for writing a chapter is:

1. **`query`** — Gather context: review timeline, characters, and locations relevant to the next scene.
2. **`write`** — Draft the scene/chapter in `manuscript/`, adhering to the style guide and wiki state.
3. **`ingest`** — Synchronize the wiki with any new events, characters, or locations introduced in the draft.
4. **`lint`** — Validate consistency across the wiki and manuscript. Fix issues before proceeding.

## Entity Formats

### Characters (`wiki/characters/[name].md`)

**Required YAML Frontmatter:**
```yaml
---
name: ""
aliases: []
age: ""
role: ""          # protagonist | antagonist | supporting | minor
status: alive     # alive | deceased | missing | unknown
first_appearance: ""  # chapter/scene reference
---
```

**Body Sections:**
- **Physical Appearance**: Distinguishing features, clothing style, mannerisms.
- **Personality & Traits**: Strengths, flaws, fears, core desires/motivations.
- **Voice**: Speech patterns, vocabulary, catchphrases.
- **Backstory**: History prior to chapter 1.
- **Character Arc**: Starting state vs. end goal.
- **Relationships**: Links to other character pages.
- **Appearances**: Links to chapters/scenes.

### Locations (`wiki/locations/[name].md`)
- **Metadata Frontmatter**: Region, Control/Faction.
- **Sensory Details**: Sights, sounds, smells, climate.
- **History & Lore**: Historical significance.
- **Key Features**: Landmarks, notable buildings.
- **Associated Characters**: Residents or tied characters.

### Plot & Timeline (`wiki/plot/timeline.md`)
- **Chronological Sequence**: Bulleted events.
- **Chapter Mapping**: Event to chapter correlation.
- **Unresolved Threads**: Open mysteries/plotlines.

### Worldbuilding (`wiki/worldbuilding/[topic].md`)
- **Overview**: Brief description of the topic (faction, culture, custom, technology).
- **Relevance**: How it affects the plot or characters.
- **Key Details**: Rules, norms, or notable facts.

## Log Format

All operations are logged to `wiki/log.md` using the format:
```
## [YYYY-MM-DD HH:MM] skill_name | Short description
```
