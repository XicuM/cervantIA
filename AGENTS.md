# cervantIA Book Wiki Schema

Always-on context for managing the Book Wiki.

## Rules
1. **Immutable**: Never modify `raw/`.
2. **Ownership**: Maintain `wiki/` consistency aggressively.
3. **Manuscript**: Use the wiki for strict continuity in `manuscript/`.
4. **Style**: Conform to `wiki/style_guide.md` when writing/reviewing prose.

## Workflow
1. `query` — Gather context (timeline, characters, locations).
2. `write` — Draft in `manuscript/` per style guide and wiki.
3. `ingest` — Sync wiki with new entities from draft.
4. `lint` — Validate consistency across wiki/manuscript.

## Entities (`wiki/`)
### `characters/[name].md`
**YAML**: `name`, `aliases` (list), `age`, `role` (protagonist|antagonist|supporting|minor), `status` (alive|deceased|missing|unknown), `first_appearance`.
**Body**: Physical Appearance, Personality & Traits, Voice, Backstory, Arc, Relationships, Appearances.

### `locations/[name].md`
**YAML**: `region`, `control_faction`.
**Body**: Sensory Details, History & Lore, Key Features, Associated Characters.

### `plot/timeline.md`
Chronological events, Chapter Mapping, Unresolved Threads.

### `worldbuilding/[topic].md`
Overview, Relevance, Key Details.

## Logs
Append to `wiki/log.md`: `## [YYYY-MM-DD HH:MM] skill_name | Short description`

## Channel Output
- **Chat (Telegram/OpenClaw)**: Echo manuscript prose to user (e.g., "✍️ `manuscript/ch-03.md`\n\n[text]"). Do NOT echo wiki updates (confirm only: "📝 Updated `wiki/characters/x.md`"). Keep reports short, use emojis.
- **Desktop**: Write to files normally.
