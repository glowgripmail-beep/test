---
name: research-methods
description: Use when researching any topic, question, market, product, or decision; researching a topic across multiple sources, comparing options or alternatives, analyzing trends or history, understanding markets or industries, or reviewing literature or studies; synthesizing research into a comprehensive, narrative report; or when you plan to search the web or internal knowledge bases. Covers two methods - (1) deep-research, which coordinates parallel research subagents and a report-writer subagent (use only when you have a tool for spawning subagents, the Agent or Task tool; otherwise research the question directly), and (2) research, a five-expert multi-perspective sweep (STORM) that maps where the experts disagree, fact-checks every source in a second pass, and returns findings ranked by reliability plus the angles nobody covered. Hebrew triggers - מחקר, לחקור, תחקיר, השוואה, סקירת שוק, מתחרים, מקורות, בדיקת עובדות.
---

# Research Methods

This skill merges two research methods. Both are complete, standalone workflows; pick one per request using the routing table, then read only that part's GUIDE.md.

- **deep-research** (`deep-research/`) - you act as a coordinator: ask follow-ups only if needed, pick a research title, create `research_notes/{title}/` and `reports/` folders, decompose the question into 1 to 6+ independent subtopics, spawn researcher subagents in parallel, optionally one extra gap-closing round, then one report-writer subagent that produces a narrative, cited report. Its subagent instructions live in `deep-research/references/researcher.md` and `deep-research/references/report-writer.md` (the coordinator must not read them; the subagents do).
- **research** (`research/`) - a five-lens STORM-style sweep (Practitioner, Academic, Skeptic, Economist, Historian), a disagreement map, a source verification pass, HIGH/MEDIUM/LOW reliability ranking, and a tight report that ends with BLIND SPOTS.

## Which part to read when

| Task | Read |
|---|---|
| The user wants a comprehensive, narrative research report synthesized from many sources, and you can spawn subagents (Agent/Task tool) | `deep-research/GUIDE.md` |
| You are a research subagent spawned by the deep-research coordinator | `deep-research/references/researcher.md` |
| You are the report-writer subagent spawned by the deep-research coordinator | `deep-research/references/report-writer.md` |
| Researching a topic, market, product or decision where multiple perspectives, disagreement mapping, source fact-checking and reliability ranking matter, with a short tight answer | `research/GUIDE.md` |
| Customer, review, competitor or avatar research; Israeli market; a video as a source; a specific expert's point of view | `research/GUIDE.md` section "חיבור לסקילים אחרים" (routes to consumer-psychology-audience-research, video-production, productivity-memory) |
| Single factual question | `deep-research/GUIDE.md` step 3 (1 researcher), or research the question directly if no subagent tool is available |
| No subagent tool available | `research/GUIDE.md` (run the five lenses yourself) or research the question directly, as deep-research's description says |

## Paths

- In `deep-research/GUIDE.md`, `{path_to_skill}` means the absolute path of the `deep-research/` folder inside this skill (the folder that holds `references/researcher.md` and `references/report-writer.md`), not this skill's root.

## Conflicts between sources

These are not resolved here; each side is labelled by its source.

1. **Number of researchers.**
   - deep-research: decompose the query; 1 researcher for a single factual question, 3 / 4 / 5 / 6+ by decomposition strategy; "When in doubt, 3 researchers is a reasonable default."
   - research: always "Run five researchers in parallel, one per lens" (Practitioner, Academic, Skeptic, Economist, Historian).
2. **How subtopics are split.**
   - deep-research: subtopics should be "mutually exclusive and collectively exhaustive" (facets, entities, regions), plus independent points of view where useful.
   - research: the same question asked from five fixed lenses; "Each one searches on its own and does not see the others' work."
3. **Clarifying questions.**
   - deep-research: ask follow-up questions (with the AskUserQuestion tool) only "when they would meaningfully impact how research is conducted."
   - research: "If the question is vague, ask ONE clarifying question, then keep going."
4. **Report format and length.**
   - deep-research (report-writer.md): BLUF paragraph, 3-5 narrative signpost sections, "Don't use bullets or numbered lists", conclusion of 1-2 paragraphs; "if the user's question requires depth and breadth, then make the report as long as necessary."
   - research: a fixed ordered list - answer in three sentences, HIGH findings, MEDIUM and LOW findings, disagreements, BLIND SPOTS; "keep it tight", "No brain dumps. If a finding does not change what the reader would do, cut it."
5. **Expressing uncertainty.**
   - deep-research (report-writer.md): "Avoid hedging ("may", "possibly")" while explicitly stating what is uncertain or unknown; take positions.
   - research: every surviving finding is tagged HIGH / MEDIUM / LOW; MEDIUM and LOW findings are reported, labeled.
6. **Disagreement between sources.**
   - deep-research: researchers note conflicts explicitly ("contradicted by [Source B](URL)"); the report writer synthesizes and takes positions; when earlier research and current notes disagree, "the notes in your folder win."
   - research: "Disagreement is the signal. Do not smooth it into an average." The report lists where experts disagreed and what would settle it.
7. **Claims without a source.**
   - deep-research (researcher.md): an unsourced fact moves to the Gaps section; (report-writer.md): a major finding without an inline source URL is not included in the final report.
   - research: a claim that fails verification "gets cut or demoted, never softened"; LOW findings (single weak source, secondhand) can still be reported, labeled; connector note: if there is no source, write "אין לי מקור לזה".
8. **Report language.**
   - deep-research: the research title is "in the user's language"; nothing else is specified about the report language.
   - research (connector section): "הדוח בעברית פשוטה".
9. **Additional research rounds.**
   - deep-research: at most one additional round of research, "This step can only be followed once".
   - research: no extra round; instead a verification pass that opens every source before any claim is written.
10. **Coordinator doing research itself.**
    - deep-research: the coordinator "should never conduct research or write files directly."
    - research: does not separate a coordinator; the five experts run in parallel and their results are put side by side and verified.
