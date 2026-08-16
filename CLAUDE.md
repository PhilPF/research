# Math Research — Rules

This repo is for exploring theorem/characterization attempts in pure math.
No production code. Correctness of mathematical claims is the only goal.

## Non-negotiable rules

1. Never assert a claim as established without either citing it (name the
   theorem/paper) or giving a real proof. If unsure of a citation, say so.
2. Any non-rigorous step (heuristic, dimension count, generic-position
   argument, numerics) must be wrapped in `[HEURISTIC] ... [/HEURISTIC]`.
   Nothing inside those tags counts as proved.
3. Before proposing a proof of a statement, first spend effort trying to
   find a counterexample to it — including writing and running a script
   (Python/SageMath/SymPy are available) to check small/structured cases.
4. Never say "clearly," "it is easy to see," or "by a standard argument"
   without either giving the argument or tagging it `[GAP]`.
5. After any failed proof attempt, before retrying: write one paragraph in
   `LOG.md` stating exactly where it broke and why, then invoke the
   `verifier` subagent on the next attempt before presenting it to me.
   Do not silently patch a broken argument in the same breath it failed in.
6. If three consecutive attempts on the same statement fail, stop. Write a
   summary of all three failure modes to `LOG.md` and ask me how to proceed
   rather than trying a fourth variation unprompted.

## Workflow per problem

1. Restate the target with fully precise definitions/quantifiers. Confirm
   with me if anything is ambiguous.
2. Note related known theorems/counterexamples if you're aware of any.
3. Attempt a proof OR search for a counterexample (whichever seems more
   likely to resolve it first) — always try to break the statement before
   trying to prove a strengthened version of it.
4. Before showing me a "this works" conclusion, run it past the `verifier`
   subagent and include its verdict.
5. Maintain `LOG.md`: one entry per attempt — statement version tried,
   hypotheses used, status (proved/disproved/open), and why.

Keep this file itself short. Put anything problem-specific in `LOG.md`,
not here.
