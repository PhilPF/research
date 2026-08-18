# Balthasar Review — jt-percoord — Round 2

## Task decomposition (priority order)
1. Formalize candidates (a) index-blind projection and (b) degree-truncation
   precisely enough to test the stated swap-equivariance requirement. [done]
2. Formalize the swap/relabeling automorphism precisely. [done]
3. Test equivariance for (a) and (b) via exact symbolic computation on a
   generic asymmetric coupled 2D system (not just at a point — full
   polynomial-coefficient identity). [done]
4. Search for alternative reasonable formalizations of (b) (different degree
   bounds, different collapsing rules) that might break equivariance where
   the "canonical" formalization does not. [done]
5. Probe adjacent/boundary structural differences between (a) and (b) not
   captured by the literal swap test (independence of per-coordinate
   nilpotent parameters), to see whether the *stated* test is under-selective
   even though a nearby test is not. [partial — one concrete check only]
6. Check satisfiability / non-triviality of the hypotheses themselves
   (equal-order case actually admits both candidates as well-typed maps).
   [done, folded into #1]

## Setup used

W_1 ⊗ W_2 = R[e_1,e_2]/(e_1²,e_2²), basis {1, e_1, e_2, e_1e_2}. For
X_i = x_i + e_i, the full (untruncated) Taylor lift of f_i is exactly

  f_i(x) + ∂_1f_i · e_1 + ∂_2f_i · e_2 + ∂_1∂_2f_i · e_1e_2  ∈ W_1⊗W_2,

which then needs a map φ_i : W_1⊗W_2 → W_i = R[e_i]/(e_i²) (basis {1,e_i}).

- **(a) index-blind projection**: φ_i^(a)(1)=1, φ_i^(a)(e_i)=e_i,
  φ_i^(a)(e_j)=0 (j≠i), φ_i^(a)(e_1e_2)=0.
- **(b) degree truncation**, most natural non-degenerate reading in the
  *equal-order* case: since W_1=W_2=R[e]/(e²) are literally the same
  algebra with a relabeled generator, "not discriminating by index" forces
  identifying e_1=e_2=e directly (this matches the motivation text's own
  framing that the two extensions "are actually the same algebra with
  distinct naming of the symbol"). Under e_1=e_2=e, e_1e_2 ↦ e²=0
  automatically (not by an extra truncation choice), and the degree-1 part
  collapses additively: φ_i^(b)(1)=1, φ_i^(b)(e_1)=φ_i^(b)(e_2)=e_i,
  φ_i^(b)(e_1e_2)=0.

Note: because e_i²=0 already kills anything above total degree 2, and the
identification forces e_1e_2↦0 regardless of the "bound" chosen ≥1, the
equal-order restriction collapses "degree truncation" to effectively one
non-trivial map (up to the fully degenerate bound-0 map, which discards the
lift entirely and is obviously equivariant but uninteresting).

## Swap automorphism

τ: x_1↔x_2, e_1↔e_2, and correspondingly f_1↔f_2 (the vector field's own
components swap roles). Equivariance required: lift(τ·F) = τ·lift(F),
i.e. φ_2∘τ = τ∘φ_1 componentwise (with τ on the codomain side the obvious
relabeling W_1≅W_2).

## Computation (exact, symbolic-integer coefficients, not a single point)

Checked with an explicit script (`/tmp/.../probe2.py`, reproduced here in
essence) using generic asymmetric coupled polynomials

  f_1 = 3x_1²x_2 + 5x_1x_2² + 7x_1,  f_2 = 11x_1x_2² + 13x_2³ + 17x_2

(chosen with all-distinct coefficients and f_1 ≠ f_2 under any relabeling,
so no accidental symmetry of the *vector field* itself could mask a
failure). Result: **for both (a) and (b), lift(τ·F) = τ·lift(F) exactly**,
as a polynomial identity in x_1,x_2 (verified by direct coefficient
comparison, not sampling). Hand-derivation confirms this is not
coefficient-specific: both φ^(a) and φ^(b) are built from a rule that only
references "own index i" vs "other index," never a hard-coded "1" vs "2,"
so relabeling the concrete indices 1↔2 together with the formal symbols
e_1↔e_2 leaves the *rule* invariant by construction — the equivariance
check is automatically satisfied by any map defined this way.

I searched for alternative formalizations of (b) that might break this:
- Different degree bounds (0, 1, 2): bound 0 is degenerate (trivial, still
  equivariant); bound ≥1 forces the identification above regardless of the
  exact bound value in the equal-order case, since e_1e_2=e²=0 is forced by
  the *ring relation*, not by a choice.
- A "keep degree ≤1 without identifying e_1,e_2" reading is not well-typed
  into the stated codomain W_i (only one nilpotent generator available), so
  it cannot be formalized as stated without either (i) collapsing to
  candidate (a) (if you just discard the other index's degree-1 term when
  forced to choose) or (ii) collapsing to the "sum" reading of (b) above.

No formalization consistent with the problem's own description of (b)
("does not discriminate by index, only total degree") produces a map that
fails swap-equivariance.

## Adjacent (but distinct) probe: independence of nilpotent parameters

Not the literal stated test, but a natural nearby one, since it surfaced
while formalizing (b): with X_i = x_i + t_i e_i for scalar weights t_i,
candidate (a)'s rule never mixes t_1,t_2 (φ^(a) coefficient of e_i only
ever sees t_i), so (a) supports fully independent t_1, t_2 — in particular
the "silent coordinate" case t_2=0, t_1≠0 (perturb x_1 only). Candidate
(b)'s identification e_1=e_2=e presupposes a *single* shared formal
generator, so t_1=t_2 is baked into the construction; (b) as formalized
cannot natively express "perturb x_1 only, leave x_2 exactly fixed" — doing
so would require re-introducing two independent parameters, which
contradicts the very identification that defines (b) in the equal-order
case. This is a genuine structural asymmetry between (a) and (b), but it is
answering a different question (compatibility with restriction to
partial/silent perturbations) than the one posed (swap-relabeling
equivariance). I flag it because it shows the two candidates *are*
distinguishable by some symmetry/naturality-flavored test — just not the
one named in this round's claim.

## Assessment against the claim's three branches

The claim explicitly offers "rules out neither / vacuous for this pair" as
one of its own branches. Direct computation supports exactly that branch
for the *specific* swap-equivariance requirement as stated: both (a) and
(b), under every formalization consistent with their verbal descriptions,
already satisfy it. This is not a coincidence to be treated as fragile —
it is forced structurally: any map W_1⊗W_2→W_i defined by a formula
referencing only "same index vs. other index" (a's case) or "identify same-
order generators regardless of index" (b's case) is automatically covariant
under simultaneous relabeling, because neither formula ever hard-codes
which concrete index is "1" versus "2." The requirement as posed can only
ever exclude a map that is *not* built this way (e.g., one that privileges
literal index 1 over index 2 by fiat) — and no such candidate was offered.

## Locates

The swap-equivariance requirement, as literally stated (pure relabeling of
e_1↔e_2, x_1↔x_2 applied to the whole construction, tested against exactly
these two named maps), is satisfied by both and hence does not discriminate
them in the equal-order case. What *would* make a discriminating test:
either (i) a genuinely non-covariant third candidate (one that references
concrete index 1 vs 2, not just "own vs other"), which was not in scope
here, or (ii) strengthening/replacing the test with a different naturality
requirement — e.g. the "independence of per-coordinate nilpotent
parameters" probe above, or a restriction-to-silent-coordinate requirement
— which *does* separate (a) from (b) in the equal-order case, since (b)'s
own construction forces the two coordinates' nilpotent generators to be
literally identified while (a)'s does not.

## Scope

- Algebra: equal-order case only, W_1=W_2=R[e]/(e²), as required by the
  claim's hypotheses.
- Candidates: exactly (a) and (b) as named, tested under every
  formalization of "degree truncation" that remains faithful to the verbal
  description ("does not discriminate by index, only total degree");
  degenerate bound-0 case also checked.
- Vector fields: one explicit generic asymmetric coupled polynomial pair
  (all-distinct integer coefficients, genuinely coupled: ∂_2f_1≠0,
  ∂_1f_2≠0), checked as an exact polynomial identity (stronger than a
  numeric spot-check). Did not sweep a large family of vector fields
  because the equivariance identity is visibly independent of the
  particular f_1,f_2 chosen (it holds at the level of the abstract linear
  maps on the 4-dimensional basis {1,e_1,e_2,e_1e_2}, which is what the
  Taylor-coefficient computation instantiates) — this was checked by direct
  algebraic argument in addition to the one computational instance.
- Not exhaustively swept: general-order Weil algebras, n>2 dimensions,
  non-polynomial f_i, or alternative degree-bound values beyond the
  equal-order-forced collapse (out of scope per the claim's own
  restriction to the equal-order, two-candidate case).

## Tooling note

sympy was unavailable in this sandbox (no network); computation done with a
small hand-rolled exact integer/rational polynomial-differentiation engine
in plain Python instead. Scripts left at
`/tmp/claude-0/-home-user-research/d3d2dec8-1303-5f9f-92f7-0e998b33925d/scratchpad/probe2.py`
and `probe3.py` (scratch dir, not part of the repo).
