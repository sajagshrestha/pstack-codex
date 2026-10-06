# Interrogate and review

Establish the intended behavior, exact diff/base, and surrounding contracts before
reviewing. A review request is read-only unless fixes are requested.

For an adversarial review, use independent reviewers if authorized and available;
read [codex.md](codex.md) first. Give each the same intent, diff, and rubric below.
Use different models only when the host supports them and the user/configuration
permits them. Otherwise say that the review uses one model or one sequential pass.
Never claim independent reviewers ran when they did not.

## Rubric

- Correctness: trace concrete inputs through callers and state transitions. Check
  empty/boundary inputs, failure handling, idempotency, and concurrency where relevant.
- Root cause: does the fix repair the actual contract or hide the symptom?
- Structure: does ownership match the domain? Are boundaries and types sufficient?
  Does a new abstraction reduce complexity for callers?
- Verification: do tests exercise observable behavior? Would they detect the original
  bug? Does evidence cover the actual integration or UI surface?
- Complexity: identify unused paths, unjustified indirection, redundant state,
  speculative configuration, and comments that merely narrate code. Preserve
  useful rationale and legal notices.
- Security: report a specific input-to-sink path or permission failure, not generic
  concerns disconnected from this change.

Read findings against the actual source. Deduplicate, resolve disagreements, and
classify as actionable, worth considering, or dismissed with a reason. Agreement
can prioritize inspection but is not proof. A lone finding with a valid reproduction
outweighs unsupported consensus. Attach actionable findings to precise source locations.

If changes are authorized, fix accepted findings and recheck affected behavior.
Otherwise deliver findings and residual risks without modifying the code.
