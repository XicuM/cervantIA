---
name: write
description: Drafts scenes/chapters based on wiki context.
metadata: { "openclaw": { "emoji": "✍️" } }
---
# Write Skill
**Model**: Strong creative reasoning.

1. **Style**: Read `wiki/style_guide.md` for POV, tense, tone, structure.
2. **Context**: Read `wiki/plot/timeline.md` and related `wiki/characters/`, `wiki/locations/`.
3. **Continuity**: Read last 1-2 manuscript chapters to match tone, open dialogues, cliffhangers.
4. **Draft**: Write in `manuscript/` per `style_guide.md`. Follow wiki traits/details.
   **Frontmatter**:
   ```yaml
   ---
   chapter: <num>
   title: ""
   pov_character: ""
   location: ""
   timeline_position: "" # relative to prior events
   ---
   ```
5. **Output (Chat)**: Send full drafted prose back prefixed with filename/metadata.
6. **Sync Wiki**: If draft adds events/entities, update wiki like `ingest` skill (validate, index, cite).
7. **Log**: Append `## [YYYY-MM-DD HH:MM] write | Drafted <Desc>` to `logs/[YYYY-MM].md`.
