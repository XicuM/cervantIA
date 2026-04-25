---
name: ingest
description: Files a new raw note (character idea, scene brainstorm, reference) into the Book Wiki.
---

# Ingest Skill

When instructed to ingest a new source or idea, follow these steps meticulously:

1. **Analyze**: Read the provided raw note or idea. Identify any characters, locations, plot events, or worldbuilding elements mentioned.
2. **Conflict Check**: If new information contradicts an existing wiki entry, flag the conflict in the log and present both versions to the user for resolution. Do not silently overwrite.
3. **Update Plot**: If events occurred, update `wiki/plot/timeline.md` in chronological order.
4. **Update Characters**: 
   - Check if character pages exist in `wiki/characters/`. If not, create them using the Character Schema from `AGENTS.md`, including the required YAML frontmatter.
   - If they exist, update them with new traits, relationships, or state changes (e.g., injuries, relationship shifts).
5. **Update Locations**: 
   - Check if location pages exist in `wiki/locations/`. If not, create them.
   - If they exist, update sensory details or history.
6. **Frontmatter Validation**: Ensure all created or updated pages conform to the frontmatter schema defined in `AGENTS.md`.
7. **Source Tagging**: Record the source filename or reference in each updated wiki page's `Appearances` section for traceability.
8. **Index Maintenance**: Ensure all newly created pages are linked in `wiki/index.md` under the appropriate heading.
9. **Log Action**: Append a summary of what you did to `wiki/log.md` using the format: `## [YYYY-MM-DD HH:MM] ingest | <Short description>`
