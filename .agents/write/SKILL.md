---
name: write
description: Drafts new scenes or chapters based on wiki context and user instructions.
---

# Write Skill

When instructed to write or draft a new scene or chapter, follow these steps:

1. **Style Check**: Read `wiki/style_guide.md` to confirm language, POV, tense, tone, and chapter structure settings.
2. **Context Gathering**: Read the current `wiki/plot/timeline.md` to understand the state of the story. Identify the characters and locations involved, and read their respective pages in `wiki/characters/` and `wiki/locations/`.
3. **Prose Continuity**: Read the last 1–2 manuscript chapters to carry forward the exact tone, pacing, open dialogue threads, and cliffhangers. Note any unresolved promises or foreshadowing that should be addressed or maintained.
4. **Drafting**: Write the scene or chapter in the `manuscript/` directory, following the naming convention and chapter structure defined in `wiki/style_guide.md`. Adhere strictly to the established character voices, personality traits, and sensory details from the wiki.

   **Chapter Frontmatter:**
   ```yaml
   ---
   chapter: 1
   title: ""
   pov_character: ""
   location: ""
   timeline_position: ""  # relative to prior events
   ---
   ```

5. **Wiki Synchronization**: If the drafted scene introduces new plot events, characters, or locations, update the corresponding wiki pages following the same protocol as the `ingest` skill (including frontmatter validation, index updates, and source tagging).
6. **Log Action**: Append `## [YYYY-MM-DD HH:MM] write | Drafted <Scene/Chapter description>` to `wiki/log.md`.
