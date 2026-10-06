# Performance, trace analysis, and hillclimbing

Define the user-visible metric and workload before optimizing. Capture a baseline
with the relevant profiler or benchmark. Record environment, inputs, warmup,
sample count, measurement boundaries, and errors. Ensure useful work actually ran.

Trace the bottleneck and propose a falsifiable hypothesis. Consider avoiding work,
avoiding repetition, doing less, deferring it, and only then changing concurrency
or implementation cost. Measure each attempt against the same baseline conditions.
Preserve correctness and check an end-to-end measure when a microbenchmark improves.

Repeat enough trials to distinguish the effect from noise. Report variability,
absolute numbers, units, and relative change. Identify whether CPU, I/O, contention,
memory, or another constraint dominates. Do not call a cache hit, failed operation,
or reduced workload an equivalent speedup.

For **trace forensics**, inspect the supplied artifact, its capture conditions,
sampling limits, and relevant call paths. Separate observed hot spots from guessed
causes. Diagnosis does not authorize implementing a fix.

For **hillclimbing**, establish the target and time/iteration budget. Log each
hypothesis, experiment, result, and keep/revert decision. Keep accepted improvements
separable and verified. Stop on the target, exhausted budget, missing prerequisite,
or a user stop request. Do not continue an unbounded optimization loop.

Report before/after measurements and link the artifacts that support them. If no
trustworthy measurement is possible, report a hypothesis and verification gap,
not a performance gain.
