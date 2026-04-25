---
name: ingest
description: Files new raw note (character, scene, reference) into Book Wiki.
metadata: { "openclaw": { "emoji": "📥" } }
---
# Ingest Skill
**Model**: Mid-tier (good comprehension, moderate context).

1. **Analyze**: Read raw note. Identify characters, locations, plot, worldbuilding.
2. **Conflict Check**: If contradicting wiki, flag in log & ask user. DO NOT overwrite silently.
3. **Plot**: Update `wiki/plot/timeline.md` chronologically.
4. **Characters**: Update/Create in `wiki/characters/` (use Character Schema in `AGENTS.md`).
5. **Locations**: Update/Create in `wiki/locations/`.
6. **Frontmatter**: Validate YAML schema per `AGENTS.md`.
7. **Traceability**: Add source file to `Appearances` section.
8. **Index**: Link new pages in `wiki/index.md`.
9. **Chat**: Summarize changes if in chat channel.
10. **Log**: Append `## [YYYY-MM-DD HH:MM] ingest | <Short desc>` to `wiki/log.md`.
