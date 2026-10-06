# Debugging and runtime forensics

1. Reproduce the reported symptom on the affected surface. Record inputs,
   environment, expected behavior, and actual behavior. If direct reproduction
   fails, narrow triggering conditions or instrument the runtime. Explain exactly
   what is inaccessible before asking the user to perform a step.
2. Trace the relevant subsystem. List plausible causes, then choose experiments
   that eliminate the most uncertainty. Inspect runtime values instead of adding
   defensive guards based on guesses. Confirm the causal mechanism before fixing.
3. If a cheap, stable behavior test can express the bug, write it first and run it
   against the unfixed code. Confirm it fails for the reported reason, not a setup
   error. Otherwise retain a reproducible runtime procedure as the verification.
4. Make the smallest change at the responsible boundary or state owner. Remove
   speculative changes when evidence disproves their premise. For interface changes,
   consult [design.md](design.md).
5. Run the original reproduction again on the same surface. Run relevant regression
   checks. An inconclusive reproduction or a successful typecheck is not a pass.
6. Review the diff and report the symptom, root cause, fix, and actual failing and
   passing evidence. Keep observed output distinct from illustrative output.

For a diagnosis-only **runtime forensics** request, stop after establishing the
mechanism and evidence. Do not silently implement a fix. Preserve useful traces
without exposing secrets or unrelated user data.

If repeated fixes fail, reconsider what state is shared, who owns it, and whether
the initial explanation was wrong. Avoid stacking retries and null checks over
an unproven hypothesis.
