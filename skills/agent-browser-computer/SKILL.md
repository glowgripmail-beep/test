---
name: agent-browser-computer
description: "Read before the first step that uses a browser or desktop-control tool, or when output must be complete and untruncated. Covers (1) the built-in browser, the desktop app's browser pane (in-app browser, browser pane, Claude's browser, \"your own browser\"; tools mcp__Claude_Browser__* or mcp__remote-devices__Claude_Browser__*, or a single enable__mcp__remote-devices__Claude_Browser tool); (2) Claude in Chrome, the extension in the person's real Chrome (Chrome, the browser extension, the external browser; tools mcp__claude-in-chrome__* or enable__mcp__claude-in-chrome); (3) computer use / desktop control: doing something in an app on the person's own computer (Notes, Finder, System Settings, any desktop app) or looking at their screen (tools mcp__computer-use__*, mcp__remote-devices__computer_*, or enable__mcp__remote-devices__computer); (4) full-output enforcement: complete code, no placeholders, clean token-limit splits for exhaustive output. Hebrew: דפדפן, כרום, שליטה במחשב, צילום מסך, פלט מלא, בלי קיצורים."
license: Proprietary. LICENSE.txt has complete terms
---

# Agent browser, computer use and full output

This skill merges four former skills. Each lives in its own folder with its original text in `GUIDE.md` (original description, compatibility and license kept at the top of each file):

| Folder | Former skill | What it covers |
|---|---|---|
| `built-in-browser/` | built-in-browser | The browser pane inside the Claude desktop app: tool prefixes, enabling, what the person can see, persistent sign-ins, tabs and `preview_start`, bulk ToolSearch loading, reading pages as text, site approvals and `request_access`, what it cannot open (`file://`, Claude's own `localhost`), when it is offline |
| `chrome-browser/` | chrome-browser | Claude in Chrome extension: loading tools in one ToolSearch call, tab context first then a new tab, site permissions, GIF recording, console logs, avoiding alert/confirm dialogs, when to stop and ask |
| `computer-use/` | computer-use | Desktop control: turning it on from a chat, separate filesystems, picking the right tool tier (dedicated MCP, then browser, then computer use), look before asserting, bulk ToolSearch loading, access flow, tiered apps (read / click / full), link safety, financial actions |
| `full-output-enforcement/` | full-output-enforcement | No truncation: banned placeholder patterns, scope/build/cross-check process, handling long outputs with a `[PAUSED — X of Y complete ...]` marker, quick check |

The guides in `built-in-browser/`, `chrome-browser/` and `computer-use/` say the other browser "has its own skill"; that skill is now the matching folder in this same skill.

## Which file to read when

| Task | Read |
|---|---|
| Any step using `mcp__Claude_Browser__*`, `mcp__remote-devices__Claude_Browser__*` or `enable__mcp__remote-devices__Claude_Browser` | `built-in-browser/GUIDE.md` |
| Any step using `mcp__claude-in-chrome__*` or `enable__mcp__claude-in-chrome` | `chrome-browser/GUIDE.md` |
| Doing something in a native desktop app, looking at the person's screen, `mcp__computer-use__*`, `mcp__remote-devices__computer_*`, `enable__mcp__remote-devices__computer` | `computer-use/GUIDE.md` |
| Deciding between a dedicated MCP, a browser and computer use | `computer-use/GUIDE.md` ("Pick the right tool for the app") |
| A link found in an email, message or document | `computer-use/GUIDE.md` ("Link safety") |
| Anything involving money, trades, orders or transfers on the person's computer | `computer-use/GUIDE.md` ("Financial actions") |
| A request for full files, many deliverables, or long output that must not be cut short | `full-output-enforcement/GUIDE.md` |

Neither browser guide decides which browser to use: follow the session's browser guidance (a `<browsers>` section in the prompt, if present), otherwise whichever one is connected.

## Differences and conflicts between sources

The sources do not contradict each other on any rule. They differ in these places, each scoped to its own tools; nothing here is resolved, each side is labeled by source:

- **Loading tools via ToolSearch.**
  - built-in-browser: load all tools in a single ToolSearch call whose query is the full name prefix, e.g. `{ query: "mcp__remote-devices__Claude_Browser__", max_results: 64 }`.
  - chrome-browser: load every tool expected to be needed in ONE `select:` call with a comma-separated list (a core set of six tools plus task-specific ones); a second ToolSearch only for a tool needed later.
  - computer-use: load all in one call `{ query: "computer", max_results: 40 }`.
- **Tabs.**
  - built-in-browser: prefers `preview_start` with a `url` (opens an additional tab, returns `tabId`) over `tabs_create` + `navigate`; omitting `tabId` targets the active tab.
  - chrome-browser: call `tabs_context_mcp` first, reuse an existing tab only when the person explicitly asks, otherwise open a new tab with `tabs_create_mcp` and close created tabs before finishing.
- **Refused or blocked sites.**
  - built-in-browser: tell the person and move on rather than retrying; with the `mcp__remote-devices__Claude_Browser__` prefix and a `request_access` tool present, call `request_access` (scope "once" or "site"), wait, then retry.
  - chrome-browser: tell the person and wait for them to allow it; a declined site is their decision, move on.
- **When to stop.**
  - chrome-browser: stop and ask after 2 or 3 failed attempts, no response, unresponsive elements, unexpected complexity, or several failed approaches.
  - full-output-enforcement: never end with "Let me know if you want me to continue" and never deliver partial output; when near the token limit, stop at a clean breakpoint with the `[PAUSED ...]` marker. (This governs output length, not tool failures.)
- **Note inside full-output-enforcement:** its "הערות כלליות" section was originally copied from a design-skill connector block (it mentions React/Tailwind code and design copy), while its last line says the skill is "כללי לכל קוד, לא רק לעיצוב".
