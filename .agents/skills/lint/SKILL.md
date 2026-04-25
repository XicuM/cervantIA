---
name: lint
description: Health & consistency check across wiki and manuscript.
metadata: { "openclaw": { "emoji": "🔎" } }
---
# Lint Skill
**Model**: Large context, analytical reasoning.

1. **Timeline**: Check `wiki/plot/timeline.md` for impossible travel/overlaps.
2. **Character**: Cross-ref `wiki/characters/` traits vs recent actions. Flag uncharacteristic behavior.
3. **Frontmatter**: Validate YAML schema (`AGENTS.md`).
4. **Wiki/Manuscript Sync**: Flag manuscript entities missing from wiki.
5. **Manuscript Consistency**: Check for contradictory descriptions, unresolved promises, redundant intros.
6. **Dead Links**: Verify all internal wiki links resolve.
7. **Orphans**: Flag ignored unresolved plot threads & uncreated linked pages.
8. **Style**: Verify manuscript complies with `wiki/style_guide.md`.
9. **Report**: Create markdown report (use ✅, ⚠️, ❌ in chat; 1-2 lines per finding). Wait for user approval before fixing wiki.
10. **Log**: Append `## [YYYY-MM-DD HH:MM] lint | <Summary>` to `wiki/log.md`.
