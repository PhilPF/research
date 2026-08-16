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
   `LOG.md` stating exactly where it broke and why. Do not silently patch a
   broken argument in the same breath it failed in — invoke the
   `strategist` subagent (see below) to propose the next direction rather
   than generating it yourself in the same context that just failed.
6. If three consecutive attempts on the same statement fail even after
   using `strategist` each time, stop. Write a summary of all failure
   modes to `LOG.md` and ask me how to proceed rather than trying a fourth
   variation unprompted.

## Idea generation vs. judging — do not conflate these

`strategist` and the MAGI trio (`melchior`, `balthasar`, `casper`) have
opposite jobs and must never be merged:
- `strategist` is invoked after a failure, reads `LOG.md`, and proposes
  new directions. It does not verify anything and its output is never
  treated as a proof or a verdict.
- MAGI is invoked after a candidate proof/counterexample exists, and only
  judges it. MAGI members never propose alternative strategies — if a
  MAGI member's report suggests a fix, log it as a `strategist` input for
  next time, not as an accepted revision.
Sequence per attempt: (failure logged) → `strategist` proposes directions
→ I pick or you pick the most promising one → attempt it → MAGI review
→ repeat.

## MAGI review protocol

Before presenting any "this claim now holds" or "this is disproved"
conclusion to me, run the MAGI protocol instead of asserting the
conclusion yourself:

1. Dispatch the exact same claim + proof/counterexample, in parallel and
   with no shared context, to all three subagents: `melchior` (formal
   validity), `balthasar` (counterexample hunt), `casper` (outside-view
   fit). Each must not see the others' output before giving its verdict.
2. Collect all three verdicts verbatim into `LOG.md`.
3. Apply the consensus rule:
   - All three agree the claim holds → present it to me as holding, with
     all three verdicts attached.
   - Any one reports a concrete counterexample or a concrete logical gap
     (not just "suspicious") → the claim does NOT hold. Report the failure,
     not a hedge.
   - Verdicts conflict without a concrete gap/counterexample on either
     side (e.g. Casper suspicious, Melchior and Balthasar clean) → do NOT
     resolve this yourself. Present all three verdicts to me directly and
     say explicitly that MAGI did not reach consensus.
4. You (the orchestrating session) only count and route verdicts here —
   you do not get to overrule a subagent's verdict or average them into a
   softer conclusion.

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
