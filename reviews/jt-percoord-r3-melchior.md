# Melchior — coherence audit — claim `jt-percoord`, round 3

Slot 1. Time override: 5 minutes. Started 19:55:51Z.

## Subtask plan (priority order)

1. Well-typedness of `L_D(F)` as an object that method formulas can consume
   (i.e. as a map on `W_D^n`, not just on the slice `{x + t·e}`). — **done**
2. Well-typedness of `T_D(Φ)` and of the two sides of the commutation identity. — **done**
3. Quantifier audit of the DEFINE clause. — **done**
4. Well-definedness of "running M's formula over `W_D`" for the implicit member
   of the test family, and of `Φ_h^M[F]` as a map `R^n→R^n` for *every* `h>0`. — **partial**
5. Work the test family (Euler / RK2 / RK4 / BE / exact-jet) against the identity. — **partial**
   (blocked on subtask 1: the identity does not have a determinate truth value
   for any multi-stage method until 1 is resolved.)

There is no argument-so-far, so this audit is of the **statement as posed**.
A gap here is a gap in the claim's well-posedness, not in a proof step.

---

## GAP (primary): `L_D` is defined only on the slice, and the two natural extensions to `W_D^n` disagree — at exactly the point RK2 needs to evaluate it

### The quoted step

> "Fix the per-coordinate Weil lift of a vector field `L_D(F)` to be candidate
> (a) index-blind projection = the full multivariable Taylor expansion of `F`
> truncated coordinatewise: `L_D(F)(x+t·e) = Σ_{α: 0≤α_i≤D_i} (1/α!) ∂^α F(x) t^α`."

and

> "A one-step method M is an algorithm producing … a formula built from finitely
> many evaluations of F … this licenses running M's SAME formula with
> `W_D`-arithmetic in place of `R`-arithmetic."

### Why it does not follow / is not well-typed

The displayed formula defines `L_D(F)` **only at arguments of the special form
`x + t·e`**, i.e. points of `W_D^n` whose `i`-th component has nilpotent part a
scalar multiple of the single generator `e_i`. Call this the *slice*.

But "running M's same formula with `W_D`-arithmetic" requires `L_D(F)` to be a
function on (a neighbourhood-in-`W_D^n` of) all reachable arguments. For any
method with two or more stages, the second and later stages evaluate `F` at a
point **off the slice**: e.g. RK2's inner stage is `X + (h/2)·L_D(F)(X)`, whose
`i`-th component has nilpotent part `e_i + (h/2)Σ_j ∂_j F_i(x_0) e_j + …` —
a *mixture* of generators as soon as `F` is genuinely coupled (`∂_j F_i ≠ 0`,
`j ≠ i`). This is precisely the regime the TEST demands ("at least one genuinely
coupled 2-coordinate vector field").

Off the slice the statement's own two descriptions of candidate (a) come apart:

* **(a-full)** "index-blind projection … full multivariable Taylor expansion":
  `L_D(F)(x+N) = Σ_{all α} (1/α!) ∂^α F(x) N^α`, the sum terminating because `N`
  is nilpotent in `W_D`. The truncation is then *automatic from the algebra*,
  never applied by hand. This is the routing-free / functorial reading, and it is
  index-blind in the literal sense: nothing in it refers to which generator sits
  in which coordinate slot.
* **(a-trunc)** "truncated coordinatewise", read literally off the displayed
  formula: `Σ_{α: 0≤α_i≤D_i} (1/α!) ∂^α F(x) N^α`. The cut `α_i ≤ D_i` bounds the
  number of *differentiations in the i-th argument of F* by the nilpotency order
  of the *i-th generator* `e_i`. That is an index-dependent routing rule. It is
  only justified when `N_i ∈ R·e_i`.

On the slice these coincide (there `N^α = t^α e^α`, and `e^α = 0` exactly when
some `α_i > D_i`), which is why the formula looks harmless. Off the slice they
differ, because a nilpotent `N_i` containing `e_j` with `D_j > D_i` survives to
power `D_j`, and (a-trunc) discards those surviving terms while (a-full) keeps
them.

So the phrase "index-blind projection **=** full multivariable Taylor expansion
truncated coordinatewise" asserts an identity of two prescriptions that is true
only on the slice, and the claim then uses `L_D` off the slice. The commutation
identity `M[L_D(F)](x_0+t·e) = T_D(Φ_h^M[F])(x_0+t·e)` therefore has **no
determinate truth value for any multi-stage M** until `L_D(F)` is pinned down as
a map on `W_D^n`. (Explicit Euler is the one member of the test family that
escapes: it evaluates `F` only at `x_0 + t·e`, on the slice. That is why the gap
is invisible if one sanity-checks with Euler only.)

### Concrete instance witnessing the divergence

`n = 2`, `D = (1,2)`, `F(x) = (x_1^2 + x_2, x_1 x_2)` (coupled: `∂_2F_1 = 1`;
and `∂_1^2 F_1 = 2 ≠ 0`, the derivative order that `D_1 = 1` cuts off).
`x_0 = (2,5)`, `h = 1/3`, base point `X_0 = (2 + e_1, 5 + e_2)`.

Stage 1 (`K_1 = L_D(F)(X_0)`) is on the slice: **identical** under both readings,
`K_1 = (9 + 4e_1 + e_2,\ 10 + 5e_1 + 2e_2 + e_1e_2)`.

Inner point `Y = X_0 + (h/2)K_1`:
`Y_1 = 7/2 + (5/3)e_1 + (1/6)e_2`  ← off the slice, `e_2` has entered coordinate 1.

Stage 2 (`K_2 = L_D(F)(Y)`), first component:

* (a-trunc): `227/12 + (25/2)e_1 + (5/2)e_2 + (1/6)e_1e_2`
* (a-full) : `227/12 + (25/2)e_1 + (5/2)e_2 + (13/18)e_1e_2 + (1/36)e_2^2`

Difference `= (5/9)e_1e_2 + (1/36)e_2^2 = N_1^2`, i.e. exactly the `α = (2,0)`
term `(1/2!)∂_1^2F_1 · N_1^2` that (a-trunc) deletes because `α_1 = 2 > D_1 = 1`
even though the monomials it produces (`e_1e_2`, `e_2^2`) are **nonzero in
`W_D`**. Verified by exact rational arithmetic in `W_{(1,2)}`; script at
`/tmp/claude-0/-home-user-research/d3d2dec8-1303-5f9f-92f7-0e998b33925d/scratchpad/wd.py`.

Both readings then produce different RK2 updates, and the discrepancy already
lands in the `e_1e_2` and `e_2^2` components — the very components the
per-coordinate-order construction exists to compute. So this is not a pedantic
typing complaint: the two readings of the round-3 background convention give
different answers to the round-3 TEST question for RK2 (and a fortiori RK4),
on the smallest coupled example with `D_1 ≠ D_2`.

I am not proposing which reading to adopt; that is outside my role. I record only
that the claim as posed does not determine one.

---

## Secondary observations (lower confidence, less load-bearing)

**S1 — `T_D` is fine as used.** `T_D(Φ)(x_0 + t·e) = Σ_α (1/α!) ∂^α Φ(x_0) t^α`
is evaluated only at slice arguments in the DEFINE clause, so the same
slice-only ambiguity does not bite the right-hand side. It does require `Φ_h^M[F]`
to be `C^{|D|}` near `x_0`; "admissible F" is never defined, so the hypothesis
that makes `T_D(Φ_h^M[F])` exist is left implicit. Flagged, not a gap on its own.

**S2 — quantifier defect in DEFINE.** "M commutes with `L_D` if, for every
admissible F, **every D**, every h>0, every x_0 …": `D` is bound by the subscript
in the definiendum `L_D` and then re-quantified inside the definiens. As written
the definiendum has a free/bound clash — either the property is `D`-indexed
(drop "every D") or it is not (write "M commutes with L", quantifying D inside).
This matters because the TEST asks about "commutation to hold at **every** order
D", which presupposes the second reading while the notation asserts the first.
Repairable by rewording; I note it as a scope defect, not the primary gap.

**S3 — "every h>0" is too strong for the implicit member.** Backward Euler's
`Φ_h^M[F]` is not a map `R^n → R^n` for every `h>0` and every admissible `F`
(no global solvability of `X = x + hF(X)`). Under the stated universal
quantifier, "backward Euler commutes" is then vacuously false / ill-posed for
large `h` rather than informative. Also, an implicit solve is *not* "a formula
built by literal substitution", so the licensing sentence ("this licenses running
M's SAME formula with `W_D`-arithmetic") does not actually cover the implicit
member of the test family; the `W_D` solve needs a separate existence/uniqueness
argument (nilpotent-perturbation/Hensel-style), which the claim assumes rather
than states. Partial: I did not check whether that solve is canonical under
reading (a-trunc), which is not obviously an algebra-endomorphism-compatible
operation.

**S4 — a consequence worth recording, contingent on S1–S3.** Under (a-full),
`L_D(F)` is the evaluation of `F`'s Taylor series at a `W_D`-point and is
`R`-algebra natural, so the commutation identity becomes a naturality statement;
under (a-trunc) it is not the image of anything functorial, since (a-trunc) is
not compatible with the `W_D` multiplication (the example above is exactly a
failure of `Σ_{α≤D}` to respect products of nilpotents). The TEST's final
question — whether "expressible as a finite polynomial in F and its partials …"
is necessary/sufficient — is therefore answering two different questions under
the two readings. I did not have time to work either through the full family.

---

## Audit scope

Examined in depth: the definition of `L_D` and its applicability to multi-stage
method formulas (with an exact `W_{(1,2)}` computation); the slice-vs-general
argument distinction; the quantifier structure of DEFINE; the well-typedness of
`T_D`.

Examined shallowly: implicit-solve well-definedness over `W_D`; the "every h>0"
quantifier.

Not examined: RK4 specifically; the exact-jet/truncated-Taylor method; the
asymptotic-in-h refinement of the question; the necessity/sufficiency of the
B-series structural property; any comparison with candidate lifts other than (a);
prior rounds' material (deliberately not read — independence).

Ended 20:01Z (approx.), within the scaled margin.
