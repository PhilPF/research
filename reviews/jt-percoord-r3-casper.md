# Casper — outside-view review — claim `jt-percoord`, round 3

Slot budget: 5 minutes (override). Subtask plan, in priority order:

1. Fit to known theory: does the statement reduce to a known functoriality fact? (done)
2. Does the distinguishing hypothesis (D_i distinct) do any work? (done)
3. Circularity check: is the sought "structural property" the hypothesis restated? (done)
4. Test-family scope: can the stated TEST answer what it asks? (done)
5. Degenerate ends / vacuity. (done)
6. Constructive status. (partial)
7. Whether fixing L_D=(a) presupposes the Round 1-2 open question. (done)

---

## 1. Fit to known theory

Under choice (a), `W_D = R[e_1..e_n]/(e_i^{D_i+1})` is a finite-dimensional
local commutative R-algebra with nilpotent maximal ideal — i.e. a **Weil
algebra** — and `L_D(F)` as written (full multivariable Taylor expansion,
truncated on the monomial support `{α : α_i ≤ D_i}`) is *exactly* the
canonical Weil-functor lift `T^{W_D}(F)`. The statement even says so: `T_D`
is defined by the same formula, so `L_D = T_D` on maps `R^n → R^n`.

The relevant standard fact: `T^A` is a product-preserving functor on smooth
manifolds/maps; `T^A(g ∘ f) = T^A(g) ∘ T^A(f)`, and `T^A` sends the ring
operations of `R` to the ring operations of `A`. (Weil 1953; product-
preserving-functor classification via Kainz–Michor / Eck / Luciano;
textbook exposition in Kolář–Michor–Slovák, *Natural Operations in
Differential Geometry*, and Kriegl–Michor, *Convenient Setting*. Exact
chapter attribution **unverified** — treat as "standard Weil functor
theory", not as a pinpoint citation.)

Consequence, stated as the outside view and not as a proof: if `M`'s update
map is a finite composite of (i) evaluations of `F` and (ii) R-algebra ring
operations, then substituting `W_D`-arithmetic gives the `T^{W_D}`-image of
the same composite, which is `T_D(Φ_h^M[F])`. Commutation is then not a
property distinguishing methods; it is functoriality applied to a composite
that was *assumed* to be built from functorial pieces.

## 2. The distinguishing hypothesis does no work

The headline of the round is "distinct per-coordinate orders `D_i`,
`D_1 ≠ D_2`, genuinely coupled field". But nothing in the functoriality
argument sees the shape of the ideal. `W_D` for `D = (3,1)` and for
`D = (2,2)` are both just Weil algebras; the argument, and therefore the
answer, is identical. **My prediction (as a framing judgement, not a
verified computation): the prescribed 2-coordinate `D_1 ≠ D_2` test will
exhibit no distinction whatsoever between the `D_1 = D_2` and `D_1 ≠ D_2`
cases.** If that is right, the round's central experiment is designed to
have a null outcome that is uninformative about the motivating question.

The motivation says "overloading **each equation** with a distinct jet
arithmetic … expanding in Taylor series each term of a vector function
around a **distinct point** and up to a **different order**." Read
literally, that is a *per-output* (per-equation) structure: coordinate `j`
of the state lives in its own algebra `W^{(j)}`, possibly around its own
base point. Choice (a) implements something structurally different: a
*single, shared* algebra whose nilpotency degrees are indexed by *input*
directions, common to all outputs. Those coincide only when one takes the
index-blind projection — which is precisely what (a) stipulates.

The mathematically live case is the other one: distinct `W^{(j)}` per
output forces **routing / projection maps** between non-isomorphic
algebras, and projections do not commute with nonlinear operations in
general. That is where a method can genuinely fail, and where "which
methods accept this" has non-trivial answers. Fixing (a) removes exactly
that content.

## 3. Near-circularity

The definition of an admissible `M` already requires it be "well-typed by
literal substitution over **any** commutative R-algebra". The TEST then
asks whether a structural property — "expressible as a finite polynomial in
`F` and its partials … with no comparison/ordering/norm operation" — is
necessary and/or sufficient for commutation. But that property is a
paraphrase of the admissibility hypothesis. So the sufficiency half is
close to "methods that are ring-formulas satisfy the identity that
ring-formulas satisfy". This is the exact failure mode I am here to catch:
the hypothesis class was narrowed until the technique (functoriality)
applies, and the conclusion then re-reports the narrowing.

Sharper diagnostic: any method that *fails* — adaptive step control, error-
norm comparison, step rejection, limiters, `min/max/sign/abs`, projection
onto constraints, norm-based scaling-and-squaring, Newton iteration with a
convergence stopping test — is **excluded by the definition of `M`** before
the test begins, because such formulas are not well-typed over an arbitrary
commutative R-algebra (`W_D` is not ordered and has no canonical norm). The
test family {Euler, RK2, RK4, backward Euler, Taylor} contains **no negative
control**. Necessity is therefore unreachable within the stated scope, not
merely hard: the statement asks a question its own hypotheses forbid it
from answering.

## 4. Was fixing L_D = (a) appropriate here?

Partly. Fixing a background convention to make a round tractable is
legitimate. But (a) is not a neutral convention — it is the choice under
which the phenomenon of interest cannot occur. So yes, fixing (a) does
quietly presuppose an answer to what I understand to be the rounds-1-2 open
question (which lift?): it presupposes that the per-coordinate structure can
be housed in one algebra with no routing. Under that presupposition the
round is a consistency check, not a discriminating experiment. It is worth
one cheap round *as a baseline* — establishing "with routing removed,
everything B-series-shaped commutes exactly, uniformly in `D`" is a useful
null result and a control for later rounds — but it should be framed and
logged as a baseline, not as an answer to the motivating question.

## 5. Degenerate ends

- `D_i = 0` for some `i`: then `e_i = 0`, that direction collapses, and the
  statement is silently about a lower-dimensional jet. Not excluded by
  `D_i ≥ 1`, which does exclude it — fine, but note `D_i = 1` for all `i`
  is plain dual-number forward AD, where the commutation is classical
  folklore, so the "test" degenerates to a known case.
- `D_1 = D_2`: reduces to the standard uniform Weil case; the whole novelty
  is the off-diagonal case, which per §2 I expect is not novel at all.
- Implicit Euler is the one member where content could survive: `T_D(Φ)`
  presupposes the real update map `Φ` is smooth, which needs `I - h∂F`
  invertible (implicit function theorem) — an unstated hypothesis. And
  there is a real ambiguity the claim does not resolve: is `Φ_h^M[F]` the
  *exact* implicit solve, or the *implemented* finite Newton/fixed-point
  iterate? These are different maps with different lifts. The claim should
  pick one. This is the only place in the test family I would expect a
  genuine subtlety.

## 6. A conflation the claim correctly avoids (credit where due)

The claim compares `M[L_D(F)]` to `T_D(Φ_h^M[F])` — the lift of the
*numerical* map — not to the jet of the true flow. That is the right
comparison and it is good that it is stated precisely. But it also isolates
what may be the researcher's actual interest: whether the transported jet
approximates the *flow's* jet to order `p` in every component, and whether
high-`D_i` components suffer order reduction. That question is (i) non-
trivial, (ii) genuinely sensitive to `D_1 ≠ D_2`, and (iii) unreachable from
the present statement. I flag it as the plausibly-intended question.

## 7. Constructive status (partial)

The sufficiency direction is constructive: `W_D` is finite-dimensional, the
identity is a polynomial identity in finitely many coefficients, and the
`W_D`-side implicit solve is a terminating nilpotent Neumann series once
`I - h∂F(x_0)` is invertible. The classical steps are (i) smoothness of the
real implicit-Euler update via the implicit function theorem, needed even to
*write* `T_D(Φ)`, and (ii) unrestricted quantification over "every
admissible `F`" with `admissible` undefined. A necessity proof pursued by
contradiction, with no exhibited non-commuting method, would be non-
constructive — but that gap would be an artifact of the argument, not
inherent. Not a defect either way.

## Bottom line

Well-posed, probably true, and answering a question adjacent to the one that
was asked. The per-coordinate distinctness — the entire motivation — is
inert under convention (a), and the sought structural characterization is
the admissibility hypothesis restated. Recommend it be recorded as a
baseline/control result and that the statement-axis move to the routing
(distinct algebra per equation / per output) formulation where the question
has teeth.
