# Design, features, refactoring, and prototypes

1. Trace the existing subsystem with [investigation.md](investigation.md).
   Establish caller-visible behavior and the acceptance criteria.
2. Write a usage example before choosing interfaces. Identify the domain model,
   state owner, boundary validation, and important invariants. For a consequential
   or contested choice, compare two structurally different designs or prototypes.
   For trivial changes, use the existing pattern without a design ceremony.
3. Choose the smallest coherent design. Prefer an interface that hides real
   complexity and makes invalid states difficult to express. Use runtime evidence
   to resolve empirical questions; preserve user choice on product preferences.
4. Split implementation into verifiable units. Identify blocking steps, independent
   slices, shared writes, and who owns the combined result. Read [codex.md](codex.md)
   if delegation or competing implementations would help and is permitted.
5. Implement and verify each unit. Review the integrated diff for dead code,
   accidental compatibility paths, redundant validation, and unnecessary layers.
   If repeated workarounds contradict the model, revisit the design.
6. Verify the behavior through the actual interface users exercise, then perform
   the relevant checks in [review.md](review.md).

For a **refactor**, capture existing observable behavior and preserve it. Cover
meaningful contracts rather than snapshotting internal structure. Do not turn a
refactor into a behavior change without identifying that change to the user.

For a **prototype**, state the decision it will settle and the experiment's limits.
Keep throwaway artifacts isolated. Compare the alternatives using the same inputs.
Do not present a prototype as production-ready or silently merge it into the app.

For **visual parity**, compare the same viewport, content, state, and interaction.
Capture both actual surfaces and inspect differences. Recheck after changes.
If the browser or native surface cannot be driven, report the limitation rather
than declaring visual equivalence from source code alone.

Report what changed, the key tradeoff, verification results, and open decisions.
Use [delivery.md](delivery.md) when PR preparation is part of the requested task.
