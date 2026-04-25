---
name: query
description: Acts as a writing assistant to answer continuity questions while drafting.
---

# Query Skill

When the user is writing and asks a continuity or detail question, do the following:

1. **Information Retrieval**: Read the relevant entity pages in `wiki/characters/`, `wiki/locations/`, or `wiki/plot/timeline.md`.
2. **Manuscript Fallback**: If wiki content is insufficient, check the most recent manuscript chapters for additional context. Clearly distinguish wiki-sourced vs. manuscript-sourced information in your answer.
3. **Synthesis**: Synthesize an answer based on the wiki and manuscript content. Do not invent new traits unless explicitly asked to brainstorm.
4. **Citations**: Mention where you found the information (e.g., "According to `john.md` and the Ch 3 timeline...").
5. **Propose Draft (Optional)**: If the user asks for a scene draft or beat sheet based on the query, generate it aligning with the current wiki state and `wiki/style_guide.md`.
6. **Log**: Append `## [YYYY-MM-DD HH:MM] query | <Question summary>` to `wiki/log.md`.
