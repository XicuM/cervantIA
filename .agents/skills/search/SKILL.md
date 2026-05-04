---
name: search
description: Search the wiki efficiently for entities, locations, and events.
metadata: { "openclaw": { "emoji": "🔎" } }
---
# Search Skill
**Model**: Any model capable of running tools/commands.

1. **Locate Script**: Use the python script located at `.agents/skills/search/scripts/search_wiki.py`.
2. **Execute**: Run `python .agents/skills/search/scripts/search_wiki.py --query "<your_query>"` to find relevant files.
3. **Filter**: You can restrict the search to a directory by adding `--dir <directory>` (e.g. `characters`, `locations`, `plot`).
4. **Analyze**: Read only the markdown files returned by the search script if you need more details.
5. **Log**: Append `## [YYYY-MM-DD HH:MM] search | Searched for "<your_query>"` to `logs/[YYYY-MM].md`.
