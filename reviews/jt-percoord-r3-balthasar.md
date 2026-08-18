# Balthasar — jt-percoord — Round 3

Slot: 1. Budget: 5 min (override). Started 2026-08-18T19:56Z, ended ~2026-08-18T20:03Z.

## Hypotheses stripped

- W_D = R[e_1..e_n]/(e_i^{D_i+1}) — a **single commutative R-algebra** (a Weil algebra),
  local, finite-dimensional, max ideal nilpotent of index D_1+...+D_n+1.
- L_D(F) = coordinatewise-truncated Taylor expansion of F, i.e. (candidate (a))
  the evaluation of F in W_D-arithmetic at the W_D-point x + t·e.
- T_D(Φ) = the same construction applied to the real update map Φ_h^M[F].
- M = a formula built from finitely many evaluations of F, closed under
  +, ·, R-scalars (and an implicit solve), **"well-typed by literal substitution
  over any commutative R-algebra"**.
- Conclusion under test: M[L_D(F)] = T_D(Φ_h^M[F]) in W_D, plus a
  necessary/sufficient structural characterization.

## Prioritized subtasks

1. Does the test family actually commute exactly for D_1≠D_2? (done)
2. Is the hypothesis on M already the answer — vacuity check? (done)
3. Does D_1≠D_2 ever bite? Is "per-coordinate" doing any work? (done)
4. Well-definedness: is L_D(F) even defined where M evaluates it? (done)
5. Implicit Euler: existence/uniqueness/branch of the W_D solve; "every h>0". (partial)
6. Non-B-series but algebra-typed M; norms/comparisons. (partial)
7. Taylor method with W_D-arithmetic-derived (rather than exact) partials. (partial)

## Computations

Script: scratchpad `weil.py` (exact rationals) and `be.py` (floats).
n=2, D=(1,2) (distinct orders), h=3/7, base point (2/5,−1/3), genuinely
coupled polynomial field

    F(x,y) = ( x y + y^3 , x^2 − 2 x y + y ).

Two independent code paths for T_D: (i) literal Σ_α (1/α!)∂^α Φ t^α from the
exact real polynomial map, (ii) substitution x→x0+t1 e1, y→y0+t2 e2 with
truncation. They agree.

Results (exact rational equality):

| method | commutes exactly at D=(1,2) |
|---|---|
| explicit Euler | **yes** |
| explicit midpoint / RK2 | **yes** |
| classical RK4 | **yes** |
| order-2 Taylor ("exact jet"), exact symbolic elementary differentials | **yes** |
| backward/implicit Euler (h=0.05, floats, W-solve vs. central finite differences of the real Newton-solved Φ) | **yes**, max discrepancy 6.3e-6 against FD truncation noise ~1e-4 |

So all five members of the prescribed test family pass. No failure, no
h-asymptotic-only case, no D_1≠D_2 discrimination.

## Finding 1 — the claim is trivial as posed (primary)

W_D is a Weil algebra and nothing more; the "per-coordinate" structure is
invisible to the mathematics. Evaluation at x + t·e is a homomorphism of
R-algebras R[x_1..x_n] → W_D (extended to smooth F by truncated Taylor,
which is the Weil-functor lift). A method whose formula is, by hypothesis,
"well-typed by literal substitution over any commutative R-algebra" is by
definition a composite of the operations that any such homomorphism
preserves. Hence commutation is forced. Empirically confirmed above; the
one-line reason is that truncation is a ring quotient, not that the methods
are B-series.

Consequently the TEST's third question ("is there an identifiable structural
property ... necessary and/or sufficient") is answered by the definition of
M itself: the admissibility condition placed on M *is* the sufficient
condition. Nothing in the stated test family can fail, so the family cannot
calibrate anything. This is the vacuity: the quantifier "for every admissible
F" is not the weak point — the quantifier over M is, and it has been
narrowed until the conclusion is definitional.

Minimal condition that would make the question non-trivial: allow M's formula
to use an operation that is *not* an R-algebra operation — order comparison,
norm, absolute value, an adaptive/tolerance-based stopping rule, a step-size
controller, or a root-selection rule. Exactly those are what fail in practice,
and exactly those are excluded by the hypothesis on M.

## Finding 2 — the "necessary" half is false as stated

The candidate structural property offered is "expressible as a finite
polynomial in F and its partials evaluated at x_0". Backward Euler is not:
its Φ_h is an implicitly defined function of F, with an infinite B-series.
It nevertheless commutes exactly (verified numerically above, and for the
structural reason that the W_D solve is a Hensel lift of the real solve
whenever I − h DF is invertible). So the property is sufficient but not
necessary; any claim of necessity is refuted by implicit Euler, which
satisfies every stated hypothesis.

## Finding 3 — L_D(F) is not defined where multi-stage methods evaluate it

The statement specifies L_D(F) only by its values at points of the form
x + t·e. Running RK2 requires evaluating L_D(F) at x + t·e + (h/2)k_1.
Measured monomial support of that stage-2 argument in the run above:

    coord 1: (0,0),(0,1),(0,2),(1,0),(1,1)
    coord 2: (0,0),(0,1),(1,0),(1,1)

whereas the locus {x + t·e} allows only (0,0),(1,0) in coord 1 and
(0,0),(0,1) in coord 2. So for every method with ≥2 stages the left-hand
side of the identity is, read literally, undefined; it becomes defined only
after one silently extends L_D(F) to all of W_D^n as the full Weil lift.
Explicit Euler is the only member of the test family that stays on the locus
— it passes "for a shallow reason" in exactly the sense the prompt suspected.
Minimal condition excluding this: define L_D(F) as a map W_D^n → W_D^n
(Taylor at the real part of the argument), not as a formula in (x,t).

## Finding 4 — "every h>0" is not a well-formed quantifier for implicit methods

For F(x,y)=(x^2+y^2+1, xy) and h large the real backward-Euler equation has
no real solution, so Φ_h^M[F] does not exist and T_D(Φ_h^M[F]) is not a
term. Symmetrically, where I − h DF is singular the W_D solve is
unsolvable in the nilpotent directions — and there the real Φ_h cannot be
differentiable either (if ψ = id − hF has singular differential at y_0 then
ψ^{-1} cannot be C^1 at ψ(y_0)), so both sides fail together. This is not a
counterexample but an ill-posedness of the statement's quantifier: the
identity should be asserted only for (F,h,x_0) with I − h DF invertible at
the solution, which is also exactly the condition making the W_D solve a
unique Hensel lift. Root-selection for multiple real branches is likewise
unspecified; the identity holds per branch, but "the implicit solve" does
not name a branch. (Probed analytically; the large-h non-existence case was
argued, not run — marked partial.)

## Finding 5 — the per-coordinate feature is not exercised by candidate (a)

Under (a) all n output components live in the same algebra W_D; D_i indexes
the *input* coordinate's truncation order, uniformly for every output. The
motivation quoted ("expanding each term of a vector function ... up to a
different order") describes a different object: distinct truncation per
*output* equation, which is not a single Weil algebra and for which
functoriality is not automatic. Under (a) the answer to "which methods
accept this?" is "all of them", independently of D. Any discriminating
content lives in the routing-aware candidate (b), not here.

## Scope and honesty

Searched: n=2 only; D ∈ {(1,2)} exactly for the rational-exact sweep and for
the float backward-Euler check; one coupled polynomial field of degree 3;
one base point; h=3/7 (exact) and h=0.05 (implicit). Methods: Euler, RK2
midpoint, RK4, order-2 Taylor with exact partials, backward Euler. Not
searched: n≥3, D with a zero entry, D_i large, non-polynomial/analytic F,
multistep methods, partitioned/symplectic methods, methods with rational
(Padé/Rosenbrock) form and vanishing denominators, and the
"derivatives-obtained-from-W_D-arithmetic" reading of the Taylor method
(subtask 7 — this last one is the only place I expect an actual failure,
since a Taylor method of order p = max_i D_i needs order-p directional data
in coordinate i where W_D supplies only order D_i < p). Subtasks 5–7 are
partial; nothing here should be read as "no counterexample exists".
