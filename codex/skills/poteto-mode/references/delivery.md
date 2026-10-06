# PRs, longer work, pause, and resume

## Prepare a PR

When requested or authorized by the development task, inspect the actual diff,
run relevant checks, and prepare small coherent commits and a description of the
problem, changed behavior, validation, and material limitations. Follow repository
templates. Exclude unrelated user changes. Check the target repository and base
before publishing. Do not rewrite shared history merely to tidy it.

## Babysit and ship

Distinguish a status question from an instruction to fix CI or merge. For status,
inspect once and report actionable information. For authorized repairs, reproduce
failures, assess review comments on merit, fix root causes, and rerun relevant checks.
Do not churn code to satisfy incorrect automated feedback.

Merge only within the user's authorization. Before landing, verify the exact head,
required checks, relevant review requirements, and branch dependencies. For a stack,
land bottom-up and revalidate changed heads as needed; green checks alone do not
establish correctness. Stop at failed or unverified prerequisites.

Use available GitHub tools or CLI. If credentials or permissions are missing,
preserve local work and explain the specific blocker. Do not invent a successful
push, PR, merge, or review approval.

## Longer tasks

Write a concrete completion predicate and split the work into verified phases.
For many independent slices, consult [codex.md](codex.md). Track decisions with
their evidence, current artifact paths, and remaining checks. Keep this record
proportionate; do not generate a log for every trivial edit.

Stay within the active session and the user's scope. A skill cannot enable persistent
background execution. If the user requests a future wakeup or ongoing monitor, use
the host's scheduling tools when available. Report missing scheduling capability.
Do not claim that an ended chat is still watching CI.

## Pause and resume

On an explicit pause, stop new work, coordinate running workers, and preserve the
current state. Record branch, uncommitted changes, active processes, completed checks,
next action, and blockers. Do not commit or terminate unrelated user work.

On resume, read that record and inspect the actual repository and process state.
Reconcile stale assumptions before continuing. Preserve user changes and reuse
existing suitable worktrees. For cleanup requests, identify exact ownership and
recoverability before removal, using managed worktree tools where available.

Report completed work separately from queued work and unverified claims.
