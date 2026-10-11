Original description: Rebuild a cached coach persona from fresh research — new videos, updated frameworks.

Original frontmatter: `argument-hint: person's name` · `disable-model-invocation: true` (was a slash command, `/coach-refresh <name>`; `$ARGUMENTS` below = the name the user gave).

# /coach-refresh — rebuild a persona

The user wants **$ARGUMENTS** rebuilt from scratch (their content has moved on, or the
first build was thin). If `$ARGUMENTS` is empty, ask who to refresh.

1. Resolve the personas directories the same way as /coach Step 0
   (`${CLAUDE_PLUGIN_DATA}/personas` primary, `~/.claude/talk-to-anyone/personas`
   legacy fallback) and the person's slug.
2. Wherever `<personas>/<slug>/` exists (check both locations), delete only its
   `persona.md`, `videos.json`, and `transcripts/` contents — that's the entire cache
   for this person.
3. Run the full `/coach` build for the name: read
   `../coach/GUIDE.md` (the `coach/GUIDE.md` file inside the productivity-memory skill) and follow it from Step 1 (the cache
   check will miss, forcing fresh research and transcript pulls).
4. Finish by adopting the rebuilt persona per /coach Step 6, and note in the handoff
   line that it was rebuilt fresh.

אם הנתיב `../coach/GUIDE.md` לא קיים (גרסה שהועלתה לחשבון), להפעיל את הסקיל productivity-memory (part: coach) במקום.
