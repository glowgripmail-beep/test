---
name: skill-building
description: "Create, find, install and improve agent skills. Use when users want to create a skill from scratch, edit or optimize an existing skill, turn a workflow into a skill, run evals to test a skill, benchmark skill performance with variance analysis, run a blind A/B comparison between skill versions, optimize a skill's description for better triggering accuracy, or package a skill. Also use when the user asks \"how do I do X\", \"find a skill for X\", \"is there a skill that can...\", wants to search for tools, templates or workflows, or expresses interest in extending capabilities with functionality that might exist as an installable skill (npx skills, skills.sh). Hebrew: סקיל, ליצור סקיל, לשפר סקיל, למצוא סקיל, להתקין סקיל."
---

# Skill building

This skill merges two former skills. Each lives in its own folder with its original text in `GUIDE.md` (original description kept at the top):

| Folder | Former skill | What it covers |
|---|---|---|
| `skill-creator/` | skill-creator | The full create → test → review → improve loop: capture intent, interview, write SKILL.md, skill writing guide, test cases, spawning with-skill and baseline runs, grading, benchmark aggregation, the eval viewer, feedback, improvement, blind comparison, description optimization, packaging, Claude.ai and Cowork specifics. Bundles `agents/`, `references/`, `scripts/`, `eval-viewer/`, `assets/` and `LICENSE.txt` exactly as in the original |
| `find-skills/` | find-skills | Discovering and installing skills from the open agent skills ecosystem (`npx skills find/add/update/init`, skills.sh leaderboard, quality checks, presenting options), plus house rules ("כללי הבית") that override its Step 6 |

**Paths.** Wherever `skill-creator/GUIDE.md` says "the skill-creator directory" or `<skill-creator-path>`, use `<this skill>/skill-creator/`. Commands such as `python -m scripts.aggregate_benchmark ...`, `python -m scripts.run_loop ...` and `python -m scripts.package_skill ...` run from inside that folder. Relative links in the guide (`agents/grader.md`, `references/schemas.md`, `assets/eval_review.html`, `eval-viewer/generate_review.py`) resolve against `skill-creator/`.

License: `skill-creator/LICENSE.txt` is kept from the original skill-creator. Neither source had a license field in its frontmatter.

## Which file to read when

| Task | Read |
|---|---|
| Create a new skill, or turn the current conversation's workflow into one | `skill-creator/GUIDE.md` ("Creating a skill") |
| Write test prompts, run evals, grade, benchmark, launch the viewer, read feedback | `skill-creator/GUIDE.md` ("Running and evaluating test cases") |
| Grade assertions against outputs | `skill-creator/agents/grader.md` |
| Blind A/B comparison of two versions | `skill-creator/agents/comparator.md`, then `skill-creator/agents/analyzer.md` |
| Analyst pass over benchmark results | `skill-creator/agents/analyzer.md` ("Analyzing Benchmark Results") |
| JSON formats (evals.json, grading.json, benchmark.json, timing.json, metrics.json, history.json, comparison.json, analysis.json) | `skill-creator/references/schemas.md` |
| Improve a skill's triggering description | `skill-creator/GUIDE.md` ("Description Optimization"), template `skill-creator/assets/eval_review.html`, scripts `skill-creator/scripts/run_loop.py` |
| Package a skill into a `.skill` file | `skill-creator/GUIDE.md` ("Package and Present"), `skill-creator/scripts/package_skill.py` |
| Working in Claude.ai or Cowork | `skill-creator/GUIDE.md` ("Claude.ai-specific instructions", "Cowork-Specific Instructions") |
| Find an existing skill for a task, or install one | `find-skills/GUIDE.md` (read "כללי הבית" first: it overrides Step 6) |
| No existing skill found and the user wants their own | `find-skills/GUIDE.md` ("When No Skills Are Found"), then `skill-creator/GUIDE.md` |

## Conflicts between sources

Not resolved here; each side is labeled by source.

- **Installing a skill (inside find-skills).**
  - find-skills, Step 6: "If the user wants to proceed, you can install the skill for them", and "The `-g` flag installs globally (user-level) and `-y` skips confirmation prompts."
  - find-skills, כללי הבית (stated to override Step 6): before installing, read the skill's contents and show the user what is in it (files, scripts, accompanying software, source and install count); install only after explicit approval, with `npx skills add <owner/repo@skill> -g -a claude-code --copy` (no `-y`).
- **Searching before suggesting.**
  - find-skills, Steps 2-3: check the skills.sh leaderboard first, then run `npx skills find`.
  - find-skills, כללי הבית: search freely and proactively everywhere (`npx skills find`, skills.sh, GitHub, web search, the connectors registry, already-available skills and plugins), and first check whether an existing skill covers the need.
- **Creating your own skill.**
  - find-skills ("When No Skills Are Found"): suggest the user create their own skill with `npx skills init` (e.g. `npx skills init my-xyz-skill`).
  - skill-creator: the full draft → test → review → improve loop with its own scripts and packaging (`scripts/package_skill.py`).
