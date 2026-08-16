# Math Research — Rules

This repo is for exploring theorem/characterization attempts in pure math.
No production code. Correctness of mathematical claims is the only goal.

## Non-negotiable rules

1. Never assert a claim as established without either citing it (name the
   theorem/paper) or giving a real proof. If unsure of a citation, say so
   rather than inventing one.
2. Any non-rigorous step (heuristic, dimension count, generic-position
   argument, numerics) must be wrapped in `[HEURISTIC] ... [/HEURISTIC]`.
   Nothing inside those tags counts as proved.
3. Never say "clearly," "it is easy to see," or "by a standard argument"
   without either giving the argument or tagging it `[GAP]`.
4. Before proposing a proof of a statement, first spend effort trying to
   find a counterexample to it — including writing and running a script
   (Python/SageMath/SymPy are available) to check small/structured cases.
5. After any failed attempt: write the failure to `LOG.md` first, then
   invoke `strategist` for the next direction. Do not patch a broken
   argument in the same context that just produced it.
6. If three consecutive attempts on the same statement fail even with
   `strategist`, stop. Summarize all failure modes in `LOG.md` and ask me
   how to proceed rather than trying a fourth variation unprompted.

## Agents

Four subagents, two distinct jobs. Never merge these roles.

**Generative (never validates):**
- `strategist` — invoked after a failure. Reads `LOG.md`, proposes 2–5
  distinct new directions. Its output is never a proof or a verdict.

**Judging (never proposes strategies) — the MAGI trio:**
- `melchior` — formal validity of the argument as written.
- `balthasar` — adversarial counterexample hunt against the statement.
- `casper` — outside-view fit, plus constructive/intuitionistic status.

If a MAGI report implies a fix, do not adopt it — log it as input for the
next `strategist` call.

Sequence per attempt: failure logged → `strategist` proposes → a direction
is chosen → attempt → MAGI review → repeat.

## MAGI review protocol

Before presenting any "this holds" or "this is disproved" conclusion to me:

1. Dispatch the same claim + proof/counterexample **in parallel, in one
   turn**, to `melchior`, `balthasar`, and `casper`. No agent may see
   another's output before giving its verdict. Dispatching them
   sequentially defeats the entire purpose.
2. Record all three verdicts verbatim in `LOG.md`.
3. Resolve using the table below. You only route verdicts — you may not
   overrule an agent or average dissent into a softer conclusion.

### Verdict resolution

| Condition | Outcome |
|---|---|
| Melchior `invalid`, or Balthasar `counterexample found` | **Rejected.** Report the failure plainly, no hedging. Go to rule 5. |
| Balthasar `vacuous or trivial`, or Casper `likely misframed` | **Rejected as posed** — the statement, not the proof, is the problem. Route to `strategist` for a statement change, not a technique change. |
| Melchior `incomplete` | **Not accepted.** Treat the missing piece as an open subgoal; it is a `[GAP]`, not a proof. |
| All three clean (`valid` / `none found in search` / `plausible`) | **Accepted**, presented with all three verdicts and the scope of Balthasar's search attached. |
| Melchior `valid` + Balthasar `none found` + Casper `suspicious` | **No consensus.** Present all three to me unresolved and say so explicitly. Do not decide it yourself. |

Casper's `CONSTRUCTIVE STATUS` is **reported, never a rejection**. A
classically valid, non-constructive proof is an accepted result with a
noted caveat — flag the non-constructive step and move on.

Balthasar's `none found in search` is bounded evidence, never proof.
Always carry its stated search scope into any accepted conclusion.

## Workflow per problem

1. Restate the target with fully precise definitions/quantifiers. Confirm
   with me if anything is ambiguous.
2. Note related known theorems/counterexamples you're aware of, flagging
   uncertain attributions as uncertain.
3. Attempt a proof or hunt a counterexample — always try to break the
   statement before trying to prove a strengthened version of it.
4. Run the MAGI protocol above before showing me any conclusion.
5. Update `LOG.md`.

## LOG.md format

Create it if absent. One entry per attempt, append-only — never rewrite or
delete past entries, `strategist` depends on the full failure history:

```
## Attempt N — YYYY-MM-DD
Statement: <exact version tried, with hypotheses>
Approach: <technique used>
Status: proved / disproved / open
Failure mode: technical (missing lemma/bound) | structural (technique
  cannot work here) | n/a
Detail: <where exactly it broke>
MAGI: Melchior <verdict> | Balthasar <verdict> | Casper <verdict>
```

Keep this file short. Problem-specific content goes in `LOG.md`, not here.
