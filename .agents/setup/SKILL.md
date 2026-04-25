---
name: setup
description: Interviews the user to establish style, structure, and language preferences, then writes the project configuration.
---

# Setup Skill

When triggered to configure or reconfigure the project's style and writing parameters, follow these steps:

1. **Interview**: Ask the user the following questions (skip any that already have answers in `wiki/style_guide.md`):
   - **Language**: What language will the book be written in?
   - **Narrative POV**: First person, third person limited, third person omniscient, or other?
   - **Tense**: Past tense or present tense?
   - **Tone**: Literary, commercial, noir, lyrical, minimalist, etc.?
   - **Target audience**: Adults, young adult, middle grade?
   - **Chapter structure**: Approximate chapter length? Numbered chapters, named chapters, or both? File naming convention (e.g., `ch-01.md`, `chapter_one.md`)?
   - **Scene breaks**: How should scene breaks within a chapter be denoted? (e.g., `***`, `---`, blank line)
   - **Vocabulary constraints**: Any words or styles to avoid? Profanity level? Dialect considerations?
   - **Genre conventions**: Genre(s) of the work, to inform pacing and structure defaults.

2. **Write Configuration**: Populate `wiki/style_guide.md` with the user's answers using the template sections already present (Language, Narrative Voice, Prose Style, Chapter Structure, Vocabulary & Constraints).

3. **Update AGENTS.md**: If the user's preferences affect the global schema (e.g., adding new entity types or changing conventions), update the relevant sections of `AGENTS.md`.

4. **Log Action**: Append `## [YYYY-MM-DD HH:MM] setup | <Summary of configuration>` to `wiki/log.md`.

5. **Reconfiguration**: If the user later asks to change the style or structure, re-run this skill. Read the existing `wiki/style_guide.md` first and only update the changed fields.
