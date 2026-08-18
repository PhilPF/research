# Lilith — Mode 1 (propose) — jt-percoord, post-Round-3

## 1. Reading of the full history

**Round 0 (jet-transport, scoping).** No claim yet; Lilith digested a raw
batch of user questions into 5 candidate directions. Direction 4
("per-coordinate fibered extension") was chosen by the user to become
jt-percoord.

**Round 1.** Statement: per-coordinate Weil-lift jet transport, posed
directly with no gluing/compatibility map specified between per-coordinate
Weil algebras for coupled coordinates. Outcome: gap-located + misframed.
Melchior located the missing compatibility map; Balthasar showed the
statement was untyped for coupled systems and collapsed to the ordinary
(non-fibered) construction for decoupled systems; Casper flagged that the
direction was chosen from an uncommitted menu with no argued priority, and
that per-coordinate lifting breaks a coordinate-freedom load-bearing for
the broader program. **Classification: structural.** The statement itself
had no well-typed content for the case it was meant to cover (coupling).

**Round 2.** Statement narrowed to equal-order W_1=W_2, added a
renaming/relabeling-equivariance requirement meant to discriminate between
two candidate cross-term maps, (a) index-blind projection and (b)
degree-truncation. Outcome: gap-located + misframed again. Balthasar showed
swap-equivariance as literally stated is satisfied by *both* candidates —
it does not discriminate at all — but located a *different* probe
(independence of per-coordinate nilpotent parameters) that does separate
them. Melchior showed candidate (b) needs an unspecified routing
coefficient and collapses to (a) at one value of it. Casper: the dispute
was never really about relabeling symmetry. **Classification: structural.**
The diagnostic chosen to adjudicate between candidates was orthogonal to
what actually separates them; a real discriminator exists but wasn't the
one tested.

**Round 3.** Statement fixed the lift to candidate (a), and posed jet
transport as a naturality/commuting identity M[L_D(F)] = T_D(Phi_h^M[F])
in W_D, tested against five methods including a search for a B-series
necessary-and-sufficient structural condition. Outcome: gap-located +
misframed for a third time. Melchior: L_D(F) is only defined on-slice;
off-slice, candidate (a) has two readings ("a-full" vs "a-trunc") that
diverge, with an explicit witness. Balthasar: under (a), the hypothesis on
M *already is* the sufficient condition — the identity is definitional,
so D_1≠D_2 does no work — and backward Euler is a genuine counterexample
to the necessity half (it commutes exactly, yet is not a B-series method).
Casper: the whole setup is close to product-preserving-functor naturality
with no negative control, so necessity is structurally unreachable as
posed. Both extension petitions (Melchior's well-definedness audit of
a-trunc; Balthasar's exact-jet/AD probe) were denied because both would
have run *inside* the same undefined convention rather than resolving it.
**Classification: structural.** The lift itself (candidate (a)) is
underspecified exactly where the test needs it defined (off-slice), and
even where it is defined, the commuting condition it induces is close to
tautological — it cannot fail for the class of M it was built from, so
"necessity" was never a testable question in this formulation.

## 2. The three-round pattern (§6.6)

All three closed rounds on jt-percoord landed on **gap-located +
misframed**, and in each case the failure is structural rather than a
missing lemma:

- R1: the statement had no well-typed content for the coupled case it was
  meant to cover.
- R2: the discriminating test chosen was orthogonal to the actual
  distinction between candidates.
- R3: the lift candidate is undefined off-slice, and on-slice the
  commuting condition it generates is close to definitional/tautological,
  giving no negative control.

This is not "three technical setbacks on the same sound idea." It is the
same underlying move — pick an ad hoc candidate cross-term/lift
construction, then test a naturality-style identity built directly from
that candidate — failing for a related but distinct structural reason each
time. Per operating rule §6.6, three consecutive rounds with no movement
on one statement calls for stopping to summarize and asking the user how
to proceed, rather than reflexively proposing a fourth attempt in the same
vein. I am flagging this explicitly per the task instruction. I am still
providing directions below (Mode 1 requires it), but they should be read
as candidates for *if* the user chooses to continue on jt-percoord, not as
a substitute for that decision point.

## 3. Duplication check

None of the five directions below repropose: fixing L_D to a specific
candidate and testing exact-identity commuting (R3's move); the
swap/relabeling-equivariance diagnostic (R2's move, shown vacuous); or an
unglued per-coordinate statement with no compatibility map (R1's move).
Direction 3 (restricting the method class) is close in spirit to
Balthasar's carried finding about widening M, but reframes it as a
statement split rather than a widened test — flagged as such below rather
than presented as novel.

## 4. Directions

**Direction 1 — replace exact identity with an order/defect measure
(statement axis).** Instead of asking whether M[L_D(F)] equals
T_D(Phi_h^M[F]) identically in W_D (a binary condition that Round 3 showed
collapses to definitional under candidate (a)), restate jet transport as a
question about the *order in h* of the discrepancy between the two sides,
for a lift construction that need not be exact off-slice. This was flagged
as "asymptotic-in-h refinement (untouched)" in Round 3's own unfinished
list. [HEURISTIC] An order-based statement gives real negative control:
two methods can share leading-order behavior but diverge at higher order,
so the statement stops being automatically true of whatever M the lift was
built from.

**Direction 2 — ground the lift in a universal property instead of a
picked candidate (statement axis).** Rounds 1–3 all built the per-coordinate
lift from an ad hoc candidate chosen off a short menu (index-blind
projection, degree-truncation, ...). Replace this with a lift required to
satisfy an explicit universal property relative to the category of Weil
algebras and Weil-algebra homomorphisms (e.g., characterized as the unique
natural transformation compatible with all structure maps between W_D and
its coordinate projections/truncations), rather than tested post hoc for
properties like swap-equivariance. [HEURISTIC] This targets Casper's
"near-circular naturality with no negative control" directly: a
universal-property lift is either unique and forced, or provably
nonexistent — both outcomes are informative, unlike a candidate chosen
first and then checked for closure properties it may already encode.

**Direction 3 — split the claim into a scoped-sufficiency statement plus a
separate, explicitly open widening question (statement axis).** Round 3's
backward-Euler counterexample kills the necessity half of any B-series
characterization exactly because backward Euler needs an implicit
solve/root selection to commute exactly. Rather than continue testing "is
the structural condition necessary and sufficient," restate the target as
sufficiency-only for the class of methods expressible via elementary
differentials (B-series), and log the wider class (implicit/root-selecting,
adaptive, norm-comparison methods) as a distinct, separately-scoped
question rather than folding it into the same necessity test. ROUTES
AROUND: this is adjacent to Balthasar's carried "widen M" finding but is
not the same move — it does not widen the *test*, it splits the *claim*
so the counterexample no longer falsifies the statement being tested.
[HEURISTIC] Necessity claims are exactly what backward Euler broke;
removing them from the object of test (rather than patching the
definition again) is a statement-axis move, not a technique retry.

**Direction 4 — require naturality across the whole diagram of Weil
algebras, not just at one fixed D (technique axis, genuinely different
from R3's fixed-D test).** Round 3 tested commuting at one fixed W_D.
Instead, require compatibility with the truncation/refinement maps that
relate W_D to W_D' for varying per-coordinate order vectors D, D'
(an indexed/diagram condition rather than a single square). ROUTES AROUND:
Balthasar's finding that under candidate (a), the single-D identity is
definitional and D_1≠D_2 is inert — a diagram condition across several D's
simultaneously is not automatically satisfied by construction the way a
single instance is, since it constrains how M behaves as the truncation
maps vary. [HEURISTIC] This is the same broad technique family
(naturality/functoriality) but changes what must be shown enough that the
Round 3 tautology argument does not immediately transfer — untested,
flagged as a technique-axis change under the routing-around requirement
rather than a statement change.

**Direction 5 — leave the per-coordinate axis and take a different Round-0
branch (statement axis, structural pivot).** All three closed rounds on
the per-coordinate fibered-extension branch (Round 0 Direction 4) failed
structurally, and Casper flagged in Round 1 that this branch breaks a
coordinate-freedom load-bearing for the broader jet-transport program.
Round 0 produced 5 candidate directions total; the other four
(parameter/time/initial-value extension, nested/iterated extension,
isomorphic-dimension Weil algebras, vector-field class strengthening —
exact list in reviews/jet-transport-r0-lilith.md) have not been tried.
[HEURISTIC] A branch that fails structurally three times running is weak
evidence the branch itself, not just each statement tried on it, is the
obstruction; an unrelated branch from the same original menu is a cheaper
way to make progress on the broader program than a fourth per-coordinate
attempt.

## 5. Note on axis balance

Per the propose-mode rule to prioritize statement-axis ideas when the log
shows `misframed`, four of five directions above are statement-axis
(1, 2, 3, 5); one (4) is technique-axis, included because it is
*qualitatively* different from the fixed-D test that failed in Round 3
(it constrains a diagram, not a single square) rather than a patched
version of the same test.
