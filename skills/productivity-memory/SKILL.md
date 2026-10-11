---
name: productivity-memory
description: "Personal productivity, memory and voice. Use for: tasks in TASKS.md (what's on my plate, add/complete a task, waiting on); workplace memory that decodes shorthand, nicknames, acronyms and codenames (CLAUDE.md + memory/); setting up the productivity system and dashboard (/productivity:start) or syncing tasks and memory gaps (/productivity:update [--comprehensive]); importing a memory export from ChatGPT, Gemini or another assistant; the morning brief (/morning, only when explicitly asked to run, see or set it up); learning the user's writing voice (setup-writing-style) and drafting or editing prose the user will send as themselves (my-writing-style profile); and, only when the user explicitly invokes it, a coach persona of a public figure (/coach <name>, /coach-end, /coach-list, /coach-refresh <name>, /coach-switch <name>). A question about the day or calendar is not a morning-brief request."
---

# Productivity & memory

This skill merges thirteen former skills (four from Anthropic's productivity plugin, nine personal skills) into one topic skill. Each keeps its full original instructions in its own folder as `GUIDE.md`; supporting files keep their original relative paths.

| Part | Folder | Origin |
|---|---|---|
| memory-management | `memory-management/GUIDE.md` | productivity plugin (background knowledge) |
| start | `start/GUIDE.md` | productivity plugin (was `/productivity:start`) |
| task-management | `task-management/GUIDE.md` | productivity plugin (background knowledge) |
| update | `update/GUIDE.md` | productivity plugin (was `/productivity:update [--comprehensive]`) |
| dashboard | `dashboard.html` | productivity plugin (`skills/dashboard.html`), used by start and task-management |
| connectors | `CONNECTORS.md` | productivity plugin, linked from start and update (`~~category` placeholders) |
| import-memory | `import-memory/GUIDE.md` | personal skill |
| morning | `morning/GUIDE.md` (+ `morning/assets/fonts/`) | personal skill (was `/morning`) |
| setup-writing-style | `setup-writing-style/GUIDE.md` (+ `setup-writing-style/scripts/stylometry.py`) | personal skill |
| my-writing-style | `my-writing-style/GUIDE.md` | personal skill: the user's own writing-voice profile |
| coach | `coach/GUIDE.md` (+ `coach/references/`, `coach/scripts/`) | personal slash command `/coach <name>` |
| coach-end | `coach-end/GUIDE.md` | personal slash command `/coach-end` |
| coach-list | `coach-list/GUIDE.md` | personal slash command `/coach-list` |
| coach-refresh | `coach-refresh/GUIDE.md` | personal slash command `/coach-refresh <name>` |
| coach-switch | `coach-switch/GUIDE.md` | personal slash command `/coach-switch <name>` |

`LICENSE` (Apache 2.0) is the productivity plugin's license and covers the four plugin parts, `dashboard.html` and `CONNECTORS.md`. `morning/assets/fonts/Fraunces-OFL.txt` is the font's license.

## Which file to read when

| Task | Read |
|---|---|
| "What's on my plate", add a task, "remind me to", "done with X", "what am I waiting on", extract tasks from a meeting | `task-management/GUIDE.md` |
| A request full of shorthand (nicknames, acronyms, codenames), "remember this", "who is X", "what does X mean" | `memory-management/GUIDE.md` |
| First-time setup of tasks + memory + dashboard, bootstrapping memory from the user's task list | `start/GUIDE.md` (dashboard file: `dashboard.html`) |
| Sync tasks from a project tracker / GitHub, triage stale tasks, fill memory gaps, deep scan of chat/email/calendar/docs | `update/GUIDE.md` (`--comprehensive` mode for the deep scan) |
| Unfamiliar `~~category` placeholders or which tools are connected | `CONNECTORS.md` |
| Bring memories over from ChatGPT, Gemini or another assistant | `import-memory/GUIDE.md` |
| The user explicitly asks to run, see or set up their morning brief | `morning/GUIDE.md` |
| Set up / learn / capture the user's writing voice, or drafts sound generic and no profile exists | `setup-writing-style/GUIDE.md` |
| Draft or edit any prose the user will send or publish as themselves (email, WhatsApp, ad copy, doc, post) | `my-writing-style/GUIDE.md` (the profile), its "Applying this profile" section |
| The user gives feedback on how a draft sounds, "add that to my voice" | `my-writing-style/GUIDE.md` → "Updating this profile"; also `setup-writing-style/GUIDE.md` → "Updating the profile" |
| The user invokes a coach command | see "Slash-command parts (coach)" below |

## How the former commands are invoked now

These parts were standalone commands or skills. In this merged skill they are sections; when the user types the old command, or asks for the same thing in words, read the matching GUIDE.md and follow it.

| Old invocation | Now |
|---|---|
| `/productivity:start` | `start/GUIDE.md` |
| `/productivity:update`, `/productivity:update --comprehensive` | `update/GUIDE.md` (default mode, or comprehensive mode when `--comprehensive` or "deep scan" is asked for) |
| `/morning` | `morning/GUIDE.md`. Only when the user explicitly asks to run, see or set up the brief, or names /morning; a question about their day, schedule or calendar is answered directly instead. |
| memory-management, task-management (`user-invocable: false`) | background knowledge: apply whenever tasks or shorthand come up |

The GUIDE.md files still mention the old commands (`/productivity:start`, `/productivity:update`, `/coach-end`, ...) in their original wording; treat each mention as a pointer to the matching part in this table.

### Slash-command parts (coach)

The five coach parts were user-only slash commands (`disable-model-invocation: true`): never start one on your own initiative. Run a coach part only when the user explicitly asks for it, by typing the old command (`/coach Alex Hormozi`) or the merged form (`/productivity-memory coach Alex Hormozi`), or by asking in words ("I want to talk to X as my coach", "end the coach session").

| Command the user gives | Argument (`argument-hint`) | Read and follow | `$ARGUMENTS` in the guide means |
|---|---|---|---|
| `/coach <name>` | person's name | `coach/GUIDE.md` | the person's name the user gave (ask if empty) |
| `/coach-end` | none | `coach-end/GUIDE.md` | not used |
| `/coach-list` | none | `coach-list/GUIDE.md` | not used |
| `/coach-refresh <name>` | person's name | `coach-refresh/GUIDE.md` | the person to rebuild (ask if empty) |
| `/coach-switch <name>` | new person's name | `coach-switch/GUIDE.md` | the new coach (ask if empty) |

Paths: `coach/GUIDE.md` defines `COACH_DIR` (the `coach/` folder of this skill); the transcript fetcher is `coach/scripts/fetch_youtube.py` and the persona template is `coach/references/persona-template.md`. coach-refresh and coach-switch point to `../coach/GUIDE.md`. `${CLAUDE_PLUGIN_DATA}` will usually not substitute outside a plugin, so the persona cache falls back to `~/.claude/talk-to-anyone/personas` as each guide describes.

## Related skills

- Watching a video of a person (interviews, talks) for a coach build or any other reason: video-production (part: watch).
- Copy and ads written in the user's voice: copywriting-ads, together with `my-writing-style/GUIDE.md`.

## Conflicts between sources

Listed, not resolved; each side is labeled by its source part.

1. **Where memory lives.** memory-management: working memory in `CLAUDE.md` in the current working directory plus a `memory/` directory (`glossary.md`, `people/`, `projects/`, `context/company.md`). import-memory: Claude's memory tools only (`memory_write` / `memory_append`) with the taxonomy `/profile.md`, `/areas/<slug>.md`, `/people/<slug>.md`, `/topics/<slug>.md`, and "Do not write the export — or any cleaned, filtered, or summarized version of it — to local files".
2. **What goes into a person's file.** memory-management: full profiles (`memory/people/{name}.md`, filename by person's name e.g. `todd-martinez.md`, communication preferences, reports-to, personal notes such as "Cubs fan, likes talking baseball"). import-memory: "Relationship context only, not a dossier", family members slugged by relationship never by name, no files for care providers, and a privacy filter that drops protected attributes, health, money amounts and identifiers.
3. **Changing existing memory.** memory-management: promote/demote between `CLAUDE.md` and `memory/`, and stale items are removed from `CLAUDE.md` ("Historical/stale | ✗ Remove"). import-memory: "Additive only... Never rewrite, reorder, or delete any existing memory line or file" (stated for imports).
4. **Confirming before writing.** memory-management: on "remember this" / "X means Y", add it to memory. update, task-management and import-memory: never add tasks or memories without user confirmation / "Ask before adding" / "Confirm before writing".
5. **Names in the writing profile.** setup-writing-style: "Never write PII into the profile. No names... — the user's or anyone else's." my-writing-style (the saved profile): uses the user's first name in a heading ("## איך אושרי כותב (כללי)").
6. **Where the writing profile is saved.** setup-writing-style and my-writing-style ("Updating this profile"): save/re-save as a standalone `my-writing-style` skill (`save_writing_style`, `save_skill`, or `~/.claude/skills/my-writing-style/SKILL.md`). In this merged skill the profile is stored at `productivity-memory/my-writing-style/GUIDE.md`, so a re-save through those tools updates a separate copy, not this file.
7. **Surfaces of the writing profile.** setup-writing-style template: surfaces are email, Slack, DM, doc. my-writing-style: "email, WhatsApp, ad copy, doc" and sections by kind of writing (הסברים, שיווק, קופי, ניתוח מודעות).
8. **Fonts from Google Fonts.** morning: "Do not fetch fonts from Google Fonts" and embed Fraunces as base64. `dashboard.html` (start/task-management): loads Inter from `fonts.googleapis.com`.
