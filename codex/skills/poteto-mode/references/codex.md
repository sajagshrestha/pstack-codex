# Codex capabilities

Inspect the tools and permissions available in the current session. Tool names
and model-selection support vary between Codex hosts. Prefer capabilities over
hardcoded APIs.

| Upstream mechanism | Codex adaptation |
| --- | --- |
| Cursor slash skill and persistent custom mode | Select the skill or mention `$poteto-mode`; do not promise a persistent mode toggle |
| Task and named poteto-agent | Use exposed subagent tools, with the skill path and a scoped assignment |
| Fixed Claude/Grok review panel | Inherit the current model; use other models only when available and permitted by user/host configuration |
| Swarm | Disjoint assignments with one owner per writable artifact |
| Arena | Independent candidates in separate directories or worktrees, followed by comparison |
| Cursor control-ui/control-cli | Available browser/native UI tools, terminal, and project test harness |
| Cursor todo tool | Available planning tool or a concise written plan |
| Cursor rules for model configuration | Existing Codex/user configuration; no automatic global edits |
| Cursor loop and background agents | Work within the active session; schedule continued work only when requested and supported |
| deslop/no-comments dependency | Review complexity and comment value directly using review.md |

## Delegating work

Use subagents only when allowed by the host and relevant to the task. Keep narrow
or tightly coupled work in one agent. Give each worker the outcome, source paths,
write ownership, constraints, and evidence required on completion. Pass paths and
brief context rather than entire logs. A read-only request must explicitly forbid
edits if the tool has no enforceable read-only mode.

Use isolated worktrees for competing implementations when available. Never let
multiple workers edit the same shared checkout files concurrently. Wait for
completed artifacts, inspect their diffs, and verify the combined result yourself.
Worker summaries are leads, not proof. A failed worker is a missing result, not
a passing vote. Stop launching new work if the user pauses or redirects the task.

## Arena and swarm

For arena, give each candidate the same concrete task and compare outcomes against
acceptance criteria established in advance. Prefer structurally distinct designs.
Read each result, select a coherent base, adopt only compatible improvements, and
verify the synthesis. Record why the base won and what was retained or rejected.

For swarm, partition the search or implementation space so coverage is explicit.
Aggregate findings, resolve contradictions against source evidence, and identify
uncovered slices. If subagents are unavailable or forbidden, perform the slices
sequentially and say so. Do not start separate user-visible chats as a substitute.
