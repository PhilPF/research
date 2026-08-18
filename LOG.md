## Round 0 — 2026-08-18 — jet-transport
Statement: N/A — no single claim fixed yet. Round 0 is a scoping step: the
user supplied a raw batch of questions on how far the "jet transport"
property's hypothesis can/should be strengthened (vector-field class,
Weil-algebra/extension class, parameter/time/initial-value extensions,
per-coordinate extensions, nested/iterated extensions, isomorphic-dimension
Weil algebras). Lilith was dispatched (not MAGI) to order, digest, and
structure these into MAGI-ready candidate directions.
Argument shape: N/A (no MAGI dispatch this round).
Outcome: scoping-round (not in the §5 mechanical table — no MAGI ran;
recorded for completeness of the state/rounds history).
MAGI: not dispatched this round.
Unfinished: 4 prerequisite/definitional items flagged by Lilith as not yet
well-posed enough for a MAGI claim (see reviews file and carried-to-eve list
in state/rounds/jet-transport-r0.json).
Extensions: none petitioned.
Reviews: reviews/jet-transport-r0-input.md (raw user input, stored verbatim),
reviews/jet-transport-r0-lilith.md (Lilith's full digest/ordering)
Carried to Lilith: n/a — Lilith itself produced this round's output; next
step is the user's choice of one of Lilith's 5 candidate directions (or a
prerequisite) to become Round 1's single MAGI claim.

## Round 1 — 2026-08-18 — jt-percoord
Statement: State and test jet transport under a per-coordinate fibered
extension, where each coordinate of the original system is Weil-lifted
independently rather than the system sharing one global Weil algebra.
(Lilith Direction 4 from the jet-transport Round 0 scoping step; chosen by
the user.)
Argument shape: none — round 1, no argument attempted yet; MAGI assessed
the statement itself as posed.
Outcome: gap-located + misframed (both §5 rows independently triggered)
MAGI: M gap-found | B vacuous-or-trivial | C likely-misframed
Unfinished: Melchior — comparison to literature two-Weil-algebra fibered
bundle functors (untouched), audit of quantifiers in "jet transport as
method-property" (untouched). Balthasar — same-dimension/isomorphic Weil
algebra non-canonicity (partial), nested extensions and parameter/time/
initial-value extensions (untouched), n>=3 and nonlinear coupling, higher/
mixed-order algebras (untouched). Casper — degenerate/vacuous ends of the
per-coordinate extension (partial).
Extensions: none petitioned.
Reviews: reviews/jt-percoord-r1-{melchior,balthasar,casper}.md
Carried to Lilith: compatibility/gluing map between per-coordinate Weil
algebras A_i, A_j for coupled coordinates is unspecified and choice-
dependent (Melchior); reading (R1) untyped for coupled systems, reading
(R2) collapses to the single global Weil algebra construction, decoupled
case adds no content (Balthasar); fixed ambient algebra under (R2) is
non-canonical among same-dimension alternatives, tying to Direction 5
(Balthasar); per-coordinate lift breaks coordinate-freedom that appears
load-bearing for the broader program (Casper); axis was picked from an
uncommitted menu with no argued priority (Casper).

Lilith (propose, jt-percoord r1): 4 directions returned — see
reviews/jt-percoord-r1-lilith.md and state/lilith/jt-percoord-r1-propose.json.
Awaiting user choice for Round 2.

New user input (jt-percoord, pre-round-2): renaming-invariance idea — the
two per-coordinate Weil algebras R[eps_1]/(eps_1)^2 and R[eps_2]/(eps_2)^2
are the same algebra under symbol renaming; should a method be required to
respect that renaming-invariance the way an ODE's solution is invariant
under a consistent renaming of its variables? Framed as a question about
what the *method* accepts (not the vector field), and whether requiring it
as part of jet-transport's machinery is sensible and how restrictive it is.
Dispatched to Lilith (propose mode, capped at exactly 2 directions) to fold
into the jt-percoord direction-space alongside Round 1's findings.

Lilith (propose, jt-percoord r2, capped at 2 routes): 2 directions returned
— see reviews/jt-percoord-r2-lilith.md and
state/lilith/jt-percoord-r2-propose.json. Awaiting user choice for Round 2's
claim.

## Round 2 — 2026-08-18 — jt-percoord
Statement: Restrict to the equal-order case W_1=W_2=R[e]/(e^2). Require the
per-coordinate lift to satisfy relabeling/renaming equivariance (swapping
which coordinate gets which formal nilpotent symbol, together with
x_1<->x_2, must commute with forming the lift). Test whether this rules out,
distinguishes, or is vacuous for the two Round-1-located candidate
cross-term maps: (a) index-blind projection, (b) degree-truncation.
Argument shape: none — round 1 of testing this specific claim.
Outcome: pending (MAGI dispatched, awaiting reports).
MAGI: dispatched (melchior, balthasar, casper) in parallel, identical
sanitized input including the neutral technical setup (per-coordinate lift,
the two candidate maps) needed to make the claim well-posed, per the user's
renaming-invariance idea (Lilith r2-propose Direction 1).
Extensions: none yet.
Reviews: reviews/jt-percoord-r2-{melchior,balthasar,casper}.md (pending)
