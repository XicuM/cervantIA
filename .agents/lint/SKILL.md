---
name: lint
description: Runs a health and consistency check across the wiki and manuscript.
---

# Lint Skill

When triggered to lint or health-check the project:

1. **Timeline Check**: Review `wiki/plot/timeline.md` and character appearances. Look for impossible travel times or characters being in two places at once.
2. **Character Consistency Check**: Cross-reference character traits in `wiki/characters/` against their recent actions in the timeline or manuscript. Flag uncharacteristic behavior.
3. **Frontmatter Validation**: Verify all character and location pages have valid YAML frontmatter matching the schema in `AGENTS.md`.
4. **Manuscript ↔ Wiki Cross-Check**: Cross-reference the latest manuscript chapters against the wiki. Flag any characters, locations, or events in the manuscript that are absent from the wiki.
5. **Manuscript Internal Consistency**: Scan across manuscript chapters for contradictory physical descriptions, unresolved promises or foreshadowing, and redundant character introductions.
6. **Dead Link Detection**: Check all internal wiki links (e.g., `[John](../characters/john.md)`) resolve to existing files.
7. **Orphan Check**: Identify any plot threads in `timeline.md` marked as unresolved that have gone ignored for too long. Identify any characters mentioned in the index that lack a dedicated page.
8. **Style Compliance**: Check that manuscript chapters follow the conventions in `wiki/style_guide.md` (language, POV, tense, chapter length).
9. **Report**: Generate a clean markdown report of your findings for the user to review. Do not make unprompted corrections to the wiki during a lint pass; wait for user approval.
10. **Log**: Append `## [YYYY-MM-DD HH:MM] lint | <Summary of findings>` to `wiki/log.md`.
