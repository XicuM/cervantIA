---
name: lint
description: Health & consistency check across wiki and manuscript.
metadata: { "openclaw": { "emoji": "🔎" } }
---
# Lint Skill
**Model**: Large context, analytical reasoning.

1. **Structural Checks**: Run `python .agents/skills/lint/scripts/lint_wiki.py` to automatically check for dead links, missing YAML schema fields, and orphan files.
2. **Timeline**: Check `wiki/plot/timeline.md` for impossible travel/overlaps.
3. **Character**: Cross-ref `wiki/characters/` traits vs recent actions. Flag uncharacteristic behavior.
4. **Wiki/Manuscript Sync**: Flag manuscript entities missing from wiki.
5. **Manuscript Consistency**: Check for contradictory descriptions, unresolved promises, redundant intros.
6. **Style**: Verify manuscript complies with `wiki/style_guide.md`.
7. **Report**: Create markdown report (use ✅, ⚠️, ❌ in chat; 1-2 lines per finding). Wait for user approval before fixing wiki. Include the output of the Python script in the report.
8. **Log**: Append `## [YYYY-MM-DD HH:MM] lint | <Summary>` to `logs/[YYYY-MM].md`.
