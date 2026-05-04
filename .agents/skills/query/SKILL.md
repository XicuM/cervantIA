---
name: query
description: Continuity assistant while drafting.
metadata: { "openclaw": { "emoji": "🔍" } }
---
# Query Skill
**Model**: Mid-tier (good comprehension, moderate context).

1. **Retrieve**: Use the `search` skill to find relevant files instead of reading the entire `wiki/` directory. Read only the specific `.md` files returned by the search.
2. **Fallback**: Check recent manuscript chapters if wiki is insufficient. Distinguish sources.
3. **Synthesize**: Answer using wiki/manuscript. DO NOT invent unless asked.
4. **Cite**: Mention source (e.g., "Per `john.md`...").
5. **Format (Chat)**: Short paragraphs, bullets, **bold** entities.
6. **Draft (Optional)**: If requested, draft scene/beat sheet based on wiki & `style_guide.md`.
7. **Log**: Append `## [YYYY-MM-DD HH:MM] query | <Summary>` to `logs/[YYYY-MM].md`.
