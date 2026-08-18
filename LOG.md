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
— see reviews/jt-percoord-r2-lilith-propose1.md and
state/lilith/jt-percoord-r2-propose.json. Awaiting user choice for Round 2's
claim.

[CORRECTION 2026-08-18: the review file for this entry was originally
written to reviews/jt-percoord-r2-lilith.md, then a later propose step
(logged below) reused that same filename and overwrote it, in violation of
the mandatory-round-number naming rule. Recovered from git history
(commit 1d14855) and renamed to reviews/jt-percoord-r2-lilith-propose1.md;
the overwriting content was renamed to reviews/jt-percoord-r2-lilith-propose2.md.
No verdicts or round outcomes were affected — this corrects a file-path
pointer only. Appended per the append-only log rule rather than editing the
original entry's outcome/verdict lines.]

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

## Round 2 (closed) — 2026-08-18 — jt-percoord
Outcome: gap-located + misframed (both §5 rows independently triggered)
MAGI: M gap-found | B vacuous-or-trivial | C plausible (constructive; informational, not a table trigger)
Unfinished: Melchior — alternative degree bounds D!=1 for candidate (b)
(untouched). Balthasar — the independence-of-nilpotent-parameters probe
(partial; only sketched, not fully worked); general-order/n>2/non-polynomial
cases (untouched, out of round scope).
Extensions: none petitioned.
Reviews: reviews/jt-percoord-r2-{melchior,balthasar,casper}.md
Carried to Lilith: candidate (b) is underspecified (needs a routing
coefficient; collapses to (a) at c=0) [Melchior]; swap-equivariance as
literally stated is vacuous for this pair — satisfied by both candidates
[Balthasar]; a DIFFERENT probe (independence of per-coordinate nilpotent
parameters / silent-coordinate test) DOES separate (a) from (b) [Balthasar];
the (a)-vs-(b) dispute is really about how much cross-index data survives,
not about coordinate-relabeling symmetry [Casper].

Lilith (propose, jt-percoord r2-v2): 4 directions returned — see
reviews/jt-percoord-r2-lilith-propose2.md and
state/lilith/jt-percoord-r2-propose-v2.json. Awaiting user choice for Round 3.

## Round 3 — 2026-08-18 — jt-percoord
Statement: Fix n>=2, per-coordinate order vector D, Weil algebra
W_D=R[e_1..e_n]/(e_i^{D_i+1}), with vector-field lift L_D fixed to Round-1
candidate (a) index-blind projection (background, not reopened). Define a
one-step method M "commutes with L_D" if M[L_D(F)] = T_D(Phi_h^M[F])
identically in W_D (T_D = canonical routing-free lift of an actual map via
real mixed partials). Test on {explicit Euler, RK2, RK4, implicit Euler,
exact-jet/truncated-Taylor method} on a coupled 2-D system with D_1!=D_2
permitted: which methods satisfy the identity exactly, which fail/hold only
to some order, and whether a structural (B-series/elementary-differential)
condition on M is necessary/sufficient. (Lilith's single formalized
proposal, per user instruction; dispatched directly to MAGI, no
pick-from-menu step.)
Argument shape: none — round 1 of testing this specific claim.
Outcome: pending (MAGI dispatched, awaiting reports).
MAGI: dispatched (melchior, balthasar, casper) in parallel, identical
sanitized input, MODEL OVERRIDE: Opus (claude-opus-5) instead of default
Sonnet, TIME OVERRIDE: 5-minute budget per agent instead of standard
10 minutes (scaled hard-kill ~7.5 min instead of 15), per explicit user
instruction for this round only.
Extensions: none yet.
Reviews: reviews/jt-percoord-r3-{melchior,balthasar,casper}.md (pending)

## Round 3 (closed) — 2026-08-18 — jt-percoord
Outcome: gap-located + misframed (Melchior gap-found triggers row 1;
Balthasar vacuous-or-trivial and Casper likely-misframed both trigger row 4)
MAGI (Opus, 5-min budget): M gap-found | B vacuous-or-trivial (+ found a
genuine counterexample to the proposed characterization's necessity half:
implicit/backward Euler commutes exactly yet is not a B-series method) |
C likely-misframed
Extensions: melchior petitioned (audit whether (a-trunc) is well-defined
independent of presentation) — Lilith: no (Balthasar/Casper already show
convention (a) is definitional with no negative control; effort belongs on
the statement axis). balthasar petitioned (run exact-jet/AD method with
elementary differentials computed by W_D arithmetic itself) — Lilith: no
(would run inside the same undefined convention Melchior located; any
result uninterpretable until that gap is resolved). Both rulings written to
state/lilith/jt-percoord-r3-ruling-{melchior,balthasar}.json.
Unfinished: RK4 specifically (Melchior, untouched); asymptotic-in-h
refinement (untouched); candidate lifts other than (a) (untouched); n>=3,
non-polynomial F, multistep/partitioned/symplectic/rational methods
(Balthasar, untouched, out of round scope).
Reviews: reviews/jt-percoord-r3-{melchior,balthasar,casper}.md
Carried to Lilith: L_D(F) is only defined on-slice; off-slice, candidate
(a)'s two readings (a-full vs a-trunc) diverge, exact witness given
[Melchior]; the implicit-solve licensing for backward Euler doesn't actually
apply as stated [Melchior]; under (a) the hypothesis on M already IS the
sufficient condition, making the identity definitional and D_1!=D_2 inert
[Balthasar]; backward Euler is a genuine counterexample to the proposed
characterization's NECESSITY half [Balthasar]; the non-vacuous fix is
widening M beyond algebra-homomorphism-preserved operations
(norm/comparison, adaptive stepping, root selection) [Balthasar]; the whole
setup is near-circular product-preserving-functor naturality with no
negative control, so necessity is unreachable by construction as posed
[Casper].

Lilith (propose, jt-percoord r3-v2): 5 directions returned, PLUS an explicit
§6.6 flag — jt-percoord has now closed 3 consecutive rounds (1,2,3), all
gap-located+misframed, each a different structural reason but the same
underlying pattern (testing an ad hoc candidate construction rather than a
well-posed one). Per standing rule 6.6, this is logged as the stop-and-ask
trigger; directions supplied are options for the user's decision, not a
default next dispatch. See reviews/jt-percoord-r3-lilith-propose.md and
state/lilith/jt-percoord-r3-propose-v2.json. Awaiting user decision.
