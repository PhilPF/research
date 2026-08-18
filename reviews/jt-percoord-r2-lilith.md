# Lilith — Mode 1 (propose) — jt-percoord Round 2 directions

## 1. Log review (recap, no re-litigation)

- Round 0: scoping, user chose axis (g) per-coordinate fibered extension.
- Round 1: MAGI tested (g) as posed. Outcome `gap-located` (Melchior) **and**
  `misframed` (Balthasar `vacuous-or-trivial`, Casper `likely-misframed`)
  simultaneously.
  - Melchior's concrete break: for coupled $F$ (e.g. $F=(xy,x^2)$) with
    per-coordinate Weil algebras $W_1,W_2$, the lift $\hat f_1(X_1,X_2)$
    contains cross terms living in $W_1\otimes W_2$, not $W_1$. No map
    $\rho:W_1\otimes W_2\to W_1$ is supplied by "independent per-coordinate
    Weil lift," and Melchior exhibited **two different, equally natural
    candidate projections** ($\rho$'s) giving **inequivalent** dynamics —
    the statement adjudicates between neither.
  - Balthasar: only two literal readings exist; one is undefined under any
    coupling, the other collapses back to the single global Weil algebra
    it was meant to generalize past (and even then the choice of ambient
    algebra among same-dimension alternatives is non-canonical, §5c).
  - Casper: per-coordinate splitting breaks coordinate-freedom/naturality
    that looks load-bearing for the surrounding program; (g) was chosen
    from an uncommitted menu with no argued priority.
  - Classified **structural**: no patch to "independent per-coordinate
    Weil algebra" fixes the typing problem; every gluing-map patch was
    already tried under reading (R2) and shown to degenerate.
- Round 1 → Round 2 propose already returned four directions (A restrict
  vector-field class to flow-invariant/triangular systems, B pivot to
  Round-0 item (j) non-canonical-isomorphism naturality, C import KMS-style
  $T^{A,B}$ base/fiber bundle functor, D abandon per-coordinate for
  sibling axis (f) initial-value extension). All four remain live/unchosen
  as of this call.

## 2. The new input

The researcher observes: $\mathbb R[e_1]/(e_1^2)$ and $\mathbb R[e_2]/(e_2^2)$
are, as abstract $\mathbb R$-algebras, the *same* object — only the name of
the nilpotent generator differs. By analogy with an ODE's solution being
unaffected by renaming its variables (only by *consistently* renaming them),
the researcher asks whether jet transport — as a property of the *method*,
not of a vector field — should be required to be invariant under such
renaming, and, if imposed, what it restricts among candidate methods.
Explicitly flagged by the researcher as a question about the *machinery*
assumed by jet transport, not about vector fields, and not yet a claim to
be judged true or false.

This lands squarely inside the exact obstruction Melchior located: the
undetermined map $\rho:W_1\otimes W_2\to W_1$ handling cross terms. When
$W_1=W_2=\mathbb R[e]/(e^2)$ (the simplest case, same order, genuinely "the
same algebra renamed"), the abstract automorphism swapping the two generator
names is a bona fide symmetry of the underlying construction's raw
material. Requiring the construction to commute with this relabeling —
i.e., that permuting which coordinate is assigned "$e_1$" vs "$e_2$" (with
the matching permutation applied to the coordinates of $F$) reproduces the
permuted answer — is a well-posed, checkable naturality-in-index-set
condition, *sharper* than Round-1 Direction B (which concerned invariance
under replacing one Weil algebra by a structurally *different*
non-canonically-isomorphic same-dimension algebra, e.g. Balthasar's
exterior-algebra-vs-zero-cross-terms example). Here the two algebras are
not merely isomorphic but *identical up to variable name*, and the group
acting is the relabeling/permutation group on coordinate-indexed copies of
one fixed algebra, not the automorphism group between structurally distinct
presentations. `[HEURISTIC]` this reads as a genuine sharpening of B, not
a restatement: B asks "is the method invariant under swapping the target
Weil algebra for an isomorphic one," this asks "is the method invariant
under the $S_n$ action permuting which per-coordinate copy gets which
symbol," which is a strictly more specific, and directly Melchior-gap-
adjacent, question.

## 3. Direction sketches

**1 — add renaming/relabeling equivariance as a hypothesis on the per-coordinate machinery, and test which of Melchior's candidate gluing maps survive it (statement axis).**
Formalize the researcher's analogy precisely: for $\sigma\in S_n$
permuting coordinate indices, and $W_i$ all isomorphic as abstract algebras
(here, literally identical up to generator name), require that lifting
$F$ with $W_{\sigma(i)}$ assigned to coordinate $i$ and then applying
$\sigma^{-1}$ to the result agrees with permuting $F$ by $\sigma$ first and
lifting normally. Test Melchior's two concrete candidate projections
($\rho_1$: kill all $e_j$-terms with $j\ne i$; $\rho_2$: keep terms up to a
fixed total nilpotent degree) against this condition on the worked example,
generalized to $W_1=W_2=\mathbb R[e]/(e^2)$ (same-order case, so the
relabeling symmetry is literal, not merely an analogy). Ask whether the
condition is vacuous, selects exactly one candidate, rules out both, or is
satisfiable only by adding further structure.
ROUTES AROUND: Melchior's located gap (two natural, inequivalent
projections, no adjudication supplied) — this proposes the missing
adjudication principle as an explicit hypothesis rather than an arbitrary
choice, placed exactly where the obstruction sits, per the standing rule to
prioritize statement-axis leads that add a hypothesis at the located
obstruction.
`[HEURISTIC]` a naming-symmetry requirement is the kind of constraint that
plausibly discriminates between "kill mixed terms" and "truncate by total
degree" style projections without needing to import external machinery,
since one is manifestly index-blind by construction and the other may not
be — untested, flagged heuristic only.

**2 — construct (not merely test) the cross-term gluing map via symmetrization/invariant-theoretic descent under the relabeling action (technique axis).**
Rather than enumerating candidate $\rho$'s and checking them against
relabeling-equivariance after the fact (Direction 1), use the relabeling
group action itself as the *construction* tool: define $\hat f_i$ by
projecting $W_1\otimes\cdots\otimes W_n \to W_i$ through the coinvariants
(or an averaging/Reynolds-operator-style construction) of the subgroup of
$S_n$ stabilizing index $i$ acting on the "other" tensor factors, so the
map is equivariant by construction rather than by inspection. This is a
different technique from both Round-1 C (importing the KMS $T^{A,B}$
base/fiber bundle functor, which supplies compatibility via a base/fiber
split, not via symmetrization) and Round-1 A (restricting the admissible
vector-field class so cross terms never arise) — it keeps the general
coupled vector-field class and produces a canonical map via an averaging
principle instead of a hypothesis to check or a scope restriction.
ROUTES AROUND: same Melchior gap, but by manufacturing the missing
compatibility structure through a general invariant-theoretic construction
principle rather than testing ad hoc guesses or importing a literature
functor with a different (base/fiber) compatibility shape.
`[HEURISTIC]` symmetrization/averaging over a relabeling group is a
standard way invariant theory manufactures canonical maps out of
non-canonical raw data; whether the resulting $\rho$ is nonzero, well-typed
for genuinely coupled (non-symmetric) $F$, or reduces to one of Melchior's
already-found candidates is unconfirmed and would be the first thing this
direction's slot would need to check.

## 4. Duplication check

Neither direction repeats Round-1's tested readings (R1)/(R2). Both differ
from Round-1's already-proposed A–D:
- vs. **B** (generic non-canonical-isomorphism invariance): both new
  directions are strictly narrower/sharper — same-algebra-relabeling
  specifically, tied to the $S_n$ action on coordinate-index/generator
  pairs, not arbitrary same-dimension algebra swaps.
- vs. **A** (restrict vector-field class): neither new direction narrows
  which $F$ are admitted; both keep the general coupled case and instead
  add/construct compatibility structure.
- vs. **C** (import KMS base/fiber functor): Direction 2 uses a
  symmetrization/averaging construction, not a base/fiber split with one
  externally-supplied compatibility datum — different mathematical tool.
- vs. **D** (initial-value axis): unrelated, no overlap.
Direction 1 and Direction 2 differ from each other in kind: 1 is a
test/selection question (which existing candidate gluing maps satisfy an
added hypothesis), 2 is a constructive/existence question (build a
gluing map guaranteed to satisfy it). Both were checked for degeneracy in
the fully-diagonal case Balthasar flagged as content-free: in that case the
relabeling group acts trivially on each factor (no cross terms exist to
route), so neither direction reduces to Balthasar's zero-content diagonal
case — both are specifically about the coupled case where the Round-1 gap
lives.
