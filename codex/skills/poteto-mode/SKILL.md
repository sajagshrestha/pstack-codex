---
name: poteto-mode
description: Apply pstack engineering workflows to code investigation, design, debugging, performance work, and adversarial review. Use when the user asks for Poteto Mode, pstack, or an evidence-driven engineering workflow.
---

# Poteto Mode for Codex

Adapted from Lauren Tan's pstack. Choose a workflow below, read its reference,
and use only the parts relevant to the user's task. This package is self-contained;
it does not require the upstream Cursor skills or other plugins.

## Start

1. Establish the requested outcome and how to observe success. Read repository
   instructions and inspect existing changes before editing.
2. Trace the relevant entry point, data ownership, callers, and failure paths.
   Ground architectural claims in code or runtime evidence.
3. Choose the workflow below. For substantial work, keep a short plan with
   independently verifiable steps. State material assumptions and proceed with
   authorized work; ask only for missing decisions that evidence cannot settle.
4. Make the smallest coherent change that solves the actual problem. Name the
   data shape and ownership before adding stateful logic. Prefer eliminating
   invalid states over adding guards throughout the implementation.
5. Verify the requested behavior on the affected surface. Review the final diff
   and report the outcome, evidence, and remaining limitations.

## Choose a workflow

| Request | Read |
| --- | --- |
| Explain how or why; investigate; teach a subsystem; assess blast radius | [Investigation](references/investigation.md) |
| Add a feature; design interfaces; refactor; compare prototypes or arena candidates | [Design and implementation](references/design.md) |
| Reproduce and fix a bug; TDD; diagnose a live symptom | [Debugging](references/debugging.md) |
| Improve performance; analyze a profile; repeatedly improve a metric | [Performance](references/performance.md) |
| Interrogate a diff; independent review; simplify code and comments | [Review](references/review.md) |
| Prepare or babysit a PR; ship; resume; pause; coordinate a longer task | [Delivery](references/delivery.md) |

For parallel work, additionally read [Codex capabilities](references/codex.md).
For skill authoring, use the installed skill-creator if available. For other
uncovered tasks, state a task-specific workflow and its verification criteria;
do not pretend an unported upstream playbook is implemented.

## Engineering judgment

- Remove unnecessary work and redundant state before adding abstractions.
- Validate inputs at system boundaries; model internal invariants in types and
  structures. Migrate internal callers together when replacing an internal API.
- Separate mutable state between concurrent workers before reaching for locks.
- Make retryable operations converge safely after partial failure.
- Test observable behavior. A successful build is not proof that a UI bug is gone.
- When successive fixes fail for the same reason, revisit the premise and ownership.
- Keep comments explaining constraints the code cannot express. Do not remove
  useful rationale or license notices merely to reduce comment count.
- Capture recurring failures in types, checks, or tools when practical.

## Scope and capability boundaries

The user's scope and the host's instructions govern this workflow. Invoking a
skill does not authorize messaging people, publishing, merging, deployments,
destructive cleanup, or changing account-wide configuration. Reuse authorization
already given; do not invent extra approval checkpoints.

Use the actual tools exposed in this session. Never call Cursor's Task tool,
assume named agent types exist, or choose unavailable model identifiers. Missing
delegation does not block ordinary engineering work: work sequentially and disclose
the review limitation. Never describe one model's repeated reviews as multi-model
consensus. Never imply that a chat will keep running after its turn ends.

Keep the final explanation plain and proportionate. Separate what was measured,
what was inferred, and what could not be verified. Link only inspected or created
artifacts. An investigation or review ends with findings, not an unsolicited PR.
