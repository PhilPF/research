# jt-weil — Round 1 — Balthasar (adversarial probe)

Slot start 2026-08-21T15:35:45Z. Budget 10 min.

## Subtask 0 — references/ (done)

`/home/user/research/references/` **does not exist on this branch**
(`ls` error, not an empty directory). Per CLAUDE.md §6.7 this is *not*
evidence that no such sources exist. All algebra/Weil-functor facts used
below are recomputed from scratch here rather than cited, and the two
standard facts I lean on are tagged `[UNVERIFIED]`:

- `[UNVERIFIED]` Weil functors are product-preserving functors on smooth
  manifolds; `f_{A⊗B} = (f_A)_B` (Kolář–Michor–Slovák, *Natural
  Operations in Differential Geometry*, ch. VIII). Used only in §(b).
- `[UNVERIFIED]` For *polynomial* `f`, `f_A(u)` is literally the
  evaluation of `f` at `u ∈ A` in the algebra `A`. This is the only
  form I actually compute with, and it is self-evidently consistent
  (Taylor expansion terminates), so the numerics below do not depend on
  the citation.

Prioritised subtasks: (c) well-definedness first — it is the cheapest
place for the statement to break; then (d) two-lift-structure collision;
then (b) tensor composition; then (a) restriction along chains.

---

## Subtask 1 — (c) Is `C(n,A)` well defined from `A` alone? **NO.**
Status: **done. Counterexample found.**

### Setup, using only the stated hypotheses

`Φ = (φ_m)`, `φ_m` a function of `(m, F)` and *nothing else*. In
particular **no equivariance, consistency, order, or continuity
hypothesis is imposed on Φ.** That is exactly what the statement says
("it receives a component count and a right-hand side, and nothing
else"), and it is the hypothesis I attack.

`A = D = R[ε]/(ε²)`, `N = 2`, `n = 1`, so `m = 2`.

Two `R`-bases of `D`:

- `β₁ = (1, ε)`: coordinates `(a,b) ↦ a + bε`.
- `β₂ = (1, 1+ε)`: coordinates `(a,b) ↦ (a+b) + bε`.

`β₂` is a perfectly legitimate basis. (It is *not* induced by an algebra
automorphism — `Aut_{R-alg}(D) = R^×` acts by `ε ↦ λε`, a 1-parameter
group inside the 4-parameter `GL₂(R)` of basis changes. So this
phenomenon is *not* captured by subtask (c)'s parenthetical "e.g. via
change of the chosen basis" being read as an `Aut(A)`-action: the
relevant group is `GL_N(R)`, strictly bigger.)

Coordinate expressions of the lift `f_D` of `f : R → R`:

- in `β₁`: `F₁(a,b) = ( f(a), f'(a)·b )`
- in `β₂`: `f_D((a+b)+bε) = f(a+b) + f'(a+b)b·ε`
  `= [f(a+b) − f'(a+b)b]·1 + [f'(a+b)b]·(1+ε)`, so
  `F₂(a,b) = ( f(a+b) − f'(a+b)b , f'(a+b)b )`.

Same for `ψ := φ₁(f)`, giving `Ψ₁, Ψ₂`.

`C(1,D)` reads `φ₂(F_i) = Ψ_i` — *one condition per basis*.

### The counterexample Φ

Define the functional `χ(F) := ∂F₁/∂b |_{(0,1)}` (well defined on any
`C¹` field `F : R² → R²`; it depends on `F` alone, so it is a legal
ingredient).

```
φ_m(F)(y) := y + h·F(y)                      for m ≠ 2      (Euler)
φ₂(F)(y)  := y + h·F(y) + h·χ(F)·(1,0)                      (Euler + kick)
```

`Φ` satisfies every stated hypothesis: each `φ_m` is a single map
depending on `(m, F)` only.

**In `β₁`, `C(1,D)` HOLDS for every `f`.** `∂(F₁)₁/∂b = ∂f(a)/∂b ≡ 0`,
so `χ(F₁) = 0` and `φ₂(F₁) = (a + h f(a), b + h f'(a)b)`. With
`ψ(t) = t + h f(t)`, `Ψ₁(a,b) = (a + h f(a), (1 + h f'(a))b)`. Equal. ✔

**In `β₂`, `C(1,D)` FAILS.** First, Euler alone is fine:
`Ψ₂(a,b) = (ψ(a+b) − ψ'(a+b)b, ψ'(a+b)b)
 = (a + h f(a+b) − h f'(a+b)b, b + h f'(a+b)b) = (a,b) + h·F₂(a,b)`. ✔
But
`∂(F₂)₁/∂b = f'(a+b) − f''(a+b)b − f'(a+b) = −f''(a+b)·b`,
so `χ(F₂) = −f''(1)`.

Take **`f(x) = x²/2`** ⇒ `f'' ≡ 1` ⇒ `χ(F₂) = −1` ⇒
`φ₂(F₂) = Ψ₂ − h·(1,0) ≠ Ψ₂` for every `h ≠ 0`.

**Hypothesis audit.** `Φ` is a family of maps of `(m, F)` only ✔;
`D = R[ε]/(ε²)` is a Weil algebra of dimension 2 ✔; `n = 1`, `nN = 2` ✔;
`β₁, β₂` are `R`-bases of `D` ✔; `f(x)=x²/2` is a smooth right-hand side
on `R¹` ✔. Nothing outside the stated hypotheses is used, and nothing
stated is violated.

### What this locates

`C(n,A)` is a condition on the pair `(A, chosen basis)`, not on `A`. The
edge `n → nN` of the divisibility diagram is therefore labelled by an
element of `{Weil algebras of dim N} × GL_N(R)/(nothing)` — there is a
`GL_N(R)`-torsor of parallel edges over each algebra, and the truth
values on parallel edges differ.

Minimal condition that would exclude the object (observation, not a
recommendation): require `φ_m` to be equivariant under linear
conjugation,
`φ_m(S∘F∘S^{-1}) = S∘φ_m(F)∘S^{-1}` for all `S ∈ GL_m(R)` — or at least
for `S` of the block form `I_n ⊗ T`, `T ∈ GL_N(R)`. Under that,
`φ₂(F₂) = S φ₂(F₁) S^{-1} = S Ψ₁ S^{-1} = Ψ₂` and the condition descends
to `A` alone. (Affine equivariance is automatic for Runge–Kutta methods,
which is presumably why the statement's author did not see it — but it is
a *hypothesis on Φ*, not a consequence of the definition given.)

### Two readings, and why I am not halting the round

`C(n,A)` admits: **(A)** "holds for some/a fixed distinguished basis" vs
**(B)** "holds for every basis". The `Φ` above is a divergence witness
(true under A, false under B). I am *not* raising a definitional halt,
because subtask (c) explicitly asks me to decide whether `C(n,A)` is
basis-independent, and the answer is a definite *no with witness* — the
halt would be spent on the very question the round was dispatched to
answer. Recorded here as a finding: **(B) is strictly stronger than (A),
and their gap is exactly `GL_N`-equivariance of `Φ`.**

---

## Subtask 2 — (d) two lift structures on the same `R^m`. **Not forced to agree; they impose a genuine rigidity constraint.**
Status: **done for `m = 4`; partial in general.**

### Making "have vector fields in common" precise

For two data `(n, A)`, `(n', B)` with `nN_A = n'N_B = m`, set
`L(n,A) := { f_A : f a smooth field on R^n } ⊂ {fields on R^m}`
(coordinates via chosen bases). "Have vector fields in common" =
`L(n,A) ∩ L(n',B) ≠ {trivial}`. This is the only reading that makes
`φ_m` "receive two prescriptions at once", so I take it as the single
natural reading. (It is basis-dependent for the same reason as §1 —
`L(n,A)` moves under `GL`.)

### Witness `m = 4`: `A = R[x,y]/(x²,y²)` vs `A'' = R[x]/(x⁴)`, `n = n' = 1`

Both are dimension-4 Weil algebras (local, `R`-augmented, nilpotent
maximal ideal). Bases `(1,x,y,xy)` and `(1,x,x²,x³)`. Exact rational
computation (`chk2.py`, seed 1, 20 random integer points per case,
`Fraction` arithmetic — no floating point):

| `g` | lifts `g_A` vs `g_{A''}` as maps `R⁴→R⁴` |
|---|---|
| `g` affine (`t`, `1+2t`, `t+5`) | **identical** |
| `g = t²` | **differ** (whenever `a₁ ≠ 0`; the `x²`/`y` slot differs by `g''a₁²/2`) |
| `g = t³` | **differ** (both the deg-2 and deg-3 slots) |

Hand check of the general shape: with `u = a₀ + a₁·(first nilpotent) + …`,
`A''`-lift third slot `= g'a₃ + g''a₁a₂ + g'''a₁³/6`, `A`-lift `xy`-slot
`= g'a₃ + g''a₁a₂`; second slot `g'a₂ + g''a₁²/2` vs `g'a₂`.

Consequences, all *within* the stated hypotheses:

1. **The intersection is nonempty and nontrivial.** Since the `1`-slot of
   `f_A` is `f(a₀)`, a common field forces the *same* source `f`, and
   `f_A = f_{A''}` iff `f'' ≡ f''' ≡ 0`, i.e. **`f` affine**. So
   `L(1,A) ∩ L(1,A'')` = lifts of affine fields on `R`, a nontrivial
   family (contains all linear ODEs `ẋ = αx + β`).
2. **The two prescriptions are NOT automatically equal.** For such `F`,
   `C(1,A)` says `φ₄(F) = ψ_A` and `C(1,A'')` says `φ₄(F) = ψ_{A''}`,
   with `ψ = φ₁(f)`. By the table these agree **iff `ψ'' ≡ ψ''' ≡ 0`,
   i.e. iff `ψ` is affine.**
3. **So the collision is a real, nonvacuous constraint on `Φ`:**
   *`φ₁` must send affine fields to affine step maps.* Nothing in the
   hypotheses gives this; it is *produced* by the collision. It is
   satisfied by Euler and by any Runge–Kutta method (an RK step on an
   affine field is affine), so the constraint is consistent — the family
   does not collapse.
4. **Answer to (d):** neither "forced to agree" nor "independent" nor
   "forced to disagree". The correct third option is **over-determined
   but consistent**: the two prescriptions are distinct conditions whose
   simultaneous satisfaction is an extra, nontrivial closure property of
   `Φ` — and it is where the interesting content of the diagram lives.
   This is the sharpest thing I found in favour of the statement's
   "point of interest".

### A contrasting collision that *is* automatic

`m = 4`, `(n,A) = (2,D)` vs `(n',B) = (1, D⊗D)`. Here
`L(1,D⊗D) ⊂ L(2,D)` because `f_{D⊗D} = (f_D)_D`, and the two
prescriptions agree **iff `C(1,D)` holds**. So this collision imposes
nothing new — it is implied by conditions already in the family. The
`A` vs `A''` collision above is essentially different precisely because
`R[x]/(x⁴)` is **indecomposable**: it is not a tensor product of smaller
Weil algebras (`dim m/m² = 1` for `R[x]/(x⁴)` but `= 2` for any
`A₁⊗A₂` with both factors nontrivial). *That* is the structural
separator between "free" and "binding" collisions.

---

## Subtask 3 — (b) tensor composition. Status: **partial.**

`f_{A⊗B} = (f_A)_B` `[UNVERIFIED]` holds at the level of *algebras*, so
the edge composition is right in spirit. Two objections at the level of
the actual condition:

- **Coordinates.** The A-edge then B-edge identifies
  `R^m ≅ B^{nN_A} ≅ (A⊗B)^n` via the product basis `{e_i ⊗ f_j}` in a
  particular *order*. The direct `A⊗B` edge uses whatever basis was
  fixed for `A⊗B`. These differ by a permutation matrix (and by more if
  the `A⊗B` basis is not a product basis at all — nothing in the
  hypotheses says it must be). By §1 the truth value of `C(n, A⊗B)` is
  not invariant under such a change, so **"the composite edge equals the
  `A⊗B` edge" is false as stated and true only after the `GL`-
  equivariance hypothesis of §1 is added.** Same root cause; not counted
  as a second counterexample.
- **`A⊗B ≅ B⊗A` but the two composites route through different
  intermediate levels** (`n → nN_A → nN_AN_B` vs `n → nN_B → nN_AN_B`),
  so the "diagram over the divisibility poset" has non-unique
  factorisations of the same edge. Whether that square commutes is again
  a `GL`/permutation-equivariance question, not an algebra question.
- Untested: whether `C(n,A)` ∧ `C(nN_A,B)` ⟹ `C(n,A⊗B)` in the strong
  (all-bases) reading. I believe it does modulo equivariance but did not
  verify; `[GAP]`.

---

## Subtask 4 — (a) restriction along chains `n | n' | m`. Status: **partial.**

One structural finding, stated as an observation:

**The diagram is not generated by its edges of prime index, so there is
in general nothing to restrict along.** Every dimension `N ≥ 1` is
realised by some Weil algebra (`R[x]/(x^N)`), so every divisibility edge
is nonempty; but the edge `1 → 4` labelled `R[x]/(x⁴)` **does not factor
through level 2 at all**, since `R[x]/(x⁴)` is indecomposable as a
tensor product (see §2). Consequently `C(1, R[x]/(x⁴))` is not the
composite of any two conditions of the chain `1 | 2 | 4`, and "coherence
forced when `m` factors two different ways through the same chain" is
**empty for indecomposable labels** — the interesting conditions are
exactly the ones the chain picture cannot see. Sub-Weil-algebras and
quotients (e.g. `R[x]/(x²) ↪ R[x]/(x⁴)`, `R[x]/(x⁴) ↠ R[x]/(x²)`) give
maps *between edges* but their dimensions (2 vs 4) do not match any
divisor factorisation of the target level, so they are not edges of the
divisibility poset either. **Divisibility appears to be the wrong index
category; the natural one is the category of Weil algebras itself, with
`dim` as a functor to `(N, ×)`.** I did not search for a counterexample
against a restriction statement because I could not extract a
restriction statement precise enough to attack. `[GAP]`, not a
counterexample.

## Subtask 5 — non-vacuity / non-triviality. Status: **done.**

The hypotheses are satisfiable and not trivially so. **Explicit
Euler.** `φ_m(F)(y) = y + hF(y)` satisfies `C(n,A)` for *every* `n` and
*every* Weil `A` in *every* basis: the step map is built from `+`,
multiplication by the scalar `h ∈ R`, and `F`, all of which the Weil
functor preserves; equivalently it is `GL`-equivariant and the `β₁`
computation of §1 goes through verbatim for any `A`. So `Φ` "supporting
jet transport" is neither vacuous nor forced to be the exact flow. Good
— the calibration in §1 is about `Φ`'s hypotheses, not about emptiness.

## Mismatch check: statement vs. formal skeleton

No mismatch found, with one caveat: the skeleton's phrase "**Fixing an
`R`-basis of `A`** gives an `R`-linear isomorphism `A^n ≅ R^{nN}`"
faithfully reproduces the statement's "**once a basis of `A` is
fixed**". Both therefore inherit exactly the defect of §1: the
construction is presented as if the basis were an implementation detail,
and the statement's next move ("this turns the family into an object
indexed by the divisibility poset, **with the algebras as edges**")
silently asserts the basis-independence that §1 refutes.

## Search scope (bounds every "none found")

- **Weil algebras exercised:** `R`; `D = R[x]/(x²)`; `R[x]/(x³)`;
  `R[x]/(x⁴)`; `R[x,y]/(x²,y²) = D⊗D`. Dimensions 1–4 only.
  *Not exercised:* `R[x,y,z]/m²`, `R[x,y]/(x³,xy,y²)`, any algebra of
  dim ≥ 5, any algebra with `dim m/m² ≥ 3`.
- **Bases exercised:** for `D`, `(1,ε)` and `(1,1+ε)`; for dim-4, the
  standard monomial bases only. No systematic `GL_N` sweep.
- **Methods exercised:** explicit Euler; Euler + the `χ` kick;
  RK reasoned about but not computed.
- **Levels:** `n ∈ {1,2}`, `m ∈ {2,4}`. Nothing at `m ≥ 5`.
- **Fields:** polynomial `f` of degree ≤ 3 in one variable; 20 random
  integer evaluation points per case; exact `Fraction` arithmetic, seed
  1. No multi-variable `f`, no non-polynomial `f`.
- Scripts: `chk.py` (basis witness — sympy unavailable in this
  environment, so this one was done by hand; the arithmetic is two
  derivatives and is reproduced in full in §1), `chk2.py` (dim-4 lift
  comparison, run, output in §2). Both under the session scratchpad.

## Acquisition

`references/` is absent on this branch.

ACQUISITION: Kolář–Michor–Slovák, *Natural Operations in Differential
Geometry*, ch. VIII (Weil bundles / product-preserving functors), plus
Jorba–Zou or Abad–Barrio–Blesa–Rodríguez on jet-transport/automatic-
differentiation ODE integrators — needed to ground the two `[UNVERIFIED]`
facts and to check whether affine-equivariance of the method is already
a standing hypothesis in the jet-transport literature.
