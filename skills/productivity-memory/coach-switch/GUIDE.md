Original description: Switch from the current coach persona to a different person mid-conversation.

Original frontmatter: `argument-hint: new person's name` · `disable-model-invocation: true` (was a slash command, `/coach-switch <name>`; `$ARGUMENTS` below = the name the user gave).

# /coach-switch — change coaches

The user wants to switch coaches to **$ARGUMENTS**.

1. If a coach persona is currently active, close it out in one line as Claude
   ("{Old name} session ended."). If `$ARGUMENTS` is empty, ask who they want to
   switch to.
2. Then run the full `/coach` workflow for the new name: read
   `../coach/GUIDE.md` (the `coach/GUIDE.md` file inside the productivity-memory skill) and follow it from Step 0 with
   `$ARGUMENTS` as the person. Cached personas load instantly; new people get the
   full research build.
3. The new persona takes over from its Step 6 onward.

אם הנתיב `../coach/GUIDE.md` לא קיים (גרסה שהועלתה לחשבון), להפעיל את הסקיל productivity-memory (part: coach) במקום.
