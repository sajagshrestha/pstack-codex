# Investigation, explanation, and blast radius

Keep the task read-only unless the user asks for changes. Decide what fact would
answer the question, then trace the smallest relevant path through the code.

For **how**, follow the entry point through transformations, state owners,
side effects, and returned values. Inspect callers and tests, not just definitions.
Explain the important concepts before implementation details, and link concrete
source locations. A useful explanation lets the reader predict behavior.

For **why**, consult available commit history, PRs, issues, and design records.
Distinguish documented intent from an inference based on current structure.
Do not invent historical motivations when records are absent. Query only sources
available and relevant to the question; finding history does not require messaging
the original authors.

For **blast radius**, enumerate callers, persisted formats, integrations, state
owners, and observable contracts affected by the proposed change. Identify the
invariant on which safety depends. Prove it with a targeted experiment or existing
behavior test when execution is within scope. Label any remaining uncertainty.

For **teach**, build one connected explanation from the how and why evidence.
Use a small example or diagram when it reduces ambiguity. Do not dump file-by-file
annotations. For complex investigations, read [codex.md](codex.md) before delegating
independent exploration angles.

Report the answer first, then the supporting trace and material unknowns. Stop
when the requested question is answered; do not generate code or a PR by default.
