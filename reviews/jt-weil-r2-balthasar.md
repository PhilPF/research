# jt-weil — Round 2 — Balthasar (adversarial probe)

Slot start 2026-08-21T17:56:23Z. Budget 10 min.

## Subtask 0 — references/ (done)

`/home/user/research/references/` **still does not exist on this branch**
(`ls` error, not an empty directory). Per CLAUDE.md §6.7 this is not
evidence that no such sources exist. Standard facts leaned on:

- `[UNVERIFIED]` Weil functors are product-preserving; `f_{A⊗B} = (f_A)_B`
  (Kolář–Michor–Slovák, *Natural Operations in Differential Geometry*,
  ch. VIII). Used in (a),(b).
- `[UNVERIFIED]` For polynomial `f`, `f_A(u)` is evaluation of `f` at
  `u ∈ A`. All computations below use only this, and it is self-checking
  (Taylor series terminates by nilpotency).

---

## Subtask 1 — THE HEAD-ON TEST: is the family non-empty under the closed conventions? **YES. Not vacuous.** (done)

The dispatch conjectures that the round-1 basis witness may now kill
ordinary methods. **It does not.** The two are different objects:

- The round-1 witness was a *pathological* `Φ` (Euler + the `χ` kick),
  designed to be basis-sensitive. Convention 1 **kills that `Φ`** — it is
  no longer admissible. Correct; the witness did its job as calibration.
- **Euler survives convention 1 unscathed.** Reason: `φ_m(F)(y) = y+hF(y)`
  satisfies `φ_m(S∘F∘S⁻¹) = S∘φ_m(F)∘S⁻¹` for *every* `S ∈ GL_m(R)`.
  A change of `R`-basis of `A` changes `T_A` to `S∘T_A` with `S = g^{⊕n}`,
  `g ∈ GL_N(R)`. So `C(n,A)` at one basis ⟹ `C(n,A)` at every basis,
  automatically. Verified by hand in r1 §1 for `A = D` at basis `(1,1+ε)`:
  `Ψ₂(a,b) = (a,b) + h·F₂(a,b) = φ₂(F₂)` exactly.
- The same argument covers every Runge–Kutta method (explicit or
  implicit): an RK stage map is built from `+`, scalar multiplication and
  evaluations of `F`, all of which commute with linear conjugation, and
  all of which the Weil functor preserves.

**So: the family of admissible `Φ` is non-empty and contains the entire
classical RK class.** The statement is not vacuous.

**What convention 1 actually forces (answer to (c)).** *Not* full
equivariance. It forces exactly

  for all `g ∈ GL_N(R)`, all `f`:
  `φ_{nN}( g^{⊕n} f_A (g^{⊕n})⁻¹ ) = g^{⊕n} (φ_n f)_A (g^{⊕n})⁻¹`,

i.e. `GL_N`-equivariance of `φ_{nN}` **restricted to the `GL_N`-orbit of
the lift locus**, and nothing at all off that orbit. The user's remark
("must hold for all bases, but that does not force equivariance") is
**correct as stated**, and Subtask 3 below shows the gap between the two
is not a technicality — it is where the whole solution space lives.

`C(n,A)` is now well defined on `A` alone in the only sense that matters:
its *truth value* no longer depends on a choice, because the choice is
universally quantified. The price is Subtask 3.

---

## Subtask 2 — (d) two lift structures with common vector fields: **forced to agree, and the forcing is non-trivial.** (done for `n=1`, dim ≤ 5, identity identification)

Script: `/tmp/.../scratchpad/r2.py`. Exact `Fraction` arithmetic,
monomial-quotient Weil algebras, 40 random integer points per pair,
seed 7. Algebras exercised:

| dim | algebras |
|---|---|
| 3 | `R[x]/x³`, `R[x,y]/(x,y)²` |
| 4 | `R[x]/x⁴`, `R[x,y]/(x²,y²)`, `R[x,y]/(x³,xy,y²)`, `R[x,y,z]/m²` |
| 5 | `R[x]/x⁵`, `R[x,y]/(x³,y²)`-type, `R[x,y]/(x⁴,xy,y²)`, `R[x₁..x₄]/m²` |

Test: for `f` affine / quadratic / cubic / quartic, is `f_A = f_B` as maps
`R^N → R^N` under the monomial-basis identification?

**Raw result — every same-dimension pair, all 13 pairs, dims 3,4,5:**
agreement on **affine `f` only**; disagreement on quadratic, cubic,
quartic.

### Consequences

1. **The collision locus is exactly the affine fields**, at every
   dimension tested. r1 located this at `m = 4`; the **smallest case is
   `m = 3`** (`R[x]/x³` vs `R[x,y]/(x,y)²`), which r1 missed.
2. The two prescriptions on `φ_m` are therefore **forced to agree**, and
   agreement is equivalent (same computation applied to `ψ := φ₁(f)`) to
   `ψ` being affine. So the diagram *derives*:

   > **(R) Affine rigidity.** For every affine `f : R → R`, `φ₁(f)` must
   > be an affine map.

   Nothing in the hypotheses supplies this; the collision produces it.
   Euler and every RK method satisfy it (an RK step on an affine field is
   affine), so no collapse.
3. Answer to (d) as posed: not "independent", not "forced to disagree" —
   **over-determined but consistent**. The correct verdict is *forced to
   agree, and the forcing is a genuine, non-vacuous closure condition on
   `Φ`*. This is the strongest point in the statement's favour that I
   found.
4. **Contrasting free collision.** `(n,A) = (2,D)` vs `(1, D⊗D)` at
   `m = 4`: here `f_{D⊗D} = (f_D)_D`, so the second prescription is
   `(φ₂(f_D))_D = ((φ₁f)_D)_D = (φ₁f)_{D⊗D}` by `C(1,D)` — implied, not
   new. The binding collisions are exactly those between **tensor-
   indecomposable** labels (`dim m/m² = 1` for `R[x]/x^k`, `≥ 2` for a
   nontrivial tensor product).

**Not searched:** collisions under a *non-identity* `GL_N` identification
(i.e. `U f_A U⁻¹ = g_B` for `U ∈ GL_N` not a basis-matching), which
convention 1 makes legitimate and which could **enlarge** the collision
locus beyond affine `f` and hence strengthen (R). Flagged `partial`; this
is the extension I petition for.

---

## Subtask 3 — COUNTEREXAMPLE: the condition characterizes nothing about the method. (done)

This is the round's main adversarial finding, and it survives both closed
conventions.

### The object

Let `L*_m := { g^{⊕n} ∘ f_A ∘ (g^{⊕n})⁻¹ : m = nN, A Weil of dim N **with
N ≥ 2**, g ∈ GL_N(R), f smooth on R^n }` — the *non-trivially prescribed*
locus in the space of vector fields on `R^m`. (`N = 1` forces `A = R` and
`C(n,R)` is the tautology `φ_n(f) = φ_n(f)`; it prescribes nothing.)

`L*_m` is **thin**: for `m = 2` it is parameterised by one function of one
variable plus `dim GL₂ = 4` parameters, inside the space of all fields on
`R²` (two functions of two variables). It is a proper subset with empty
interior. `[HEURISTIC]` The same dimension count applies at every `m`.

Now define, for any `m ≥ 2`, any field `F₀ ∉ L*_m`, and any map
`G : R^m → R^m` whatsoever:

```
φ_1  := Euler on R^1
φ_m  := Euler everywhere on L*_m and everywhere except at F₀
φ_m(F₀) := G                                  (arbitrary garbage)
φ_k  for k > m := Euler, corrected on the lifts of F₀ so that
        C(m,A) : φ_{mN}((F₀)_A) = (G)_A  holds for every Weil A, basis
```

**Hypothesis audit.** Each `φ_k` is a function of `(k, ·)` and the field
alone ✔. `C(n,A)` holds at *every* basis for every `n`, `A`: on the lift
locus the values are Euler's, which are basis-independent by Subtask 1;
at `F₀` the condition `C(m,A)` is satisfied by construction (`(F₀)_A` for
`N ≥ 2` is a fresh field, not itself in `L*_{mN}` for generic `F₀`
`[HEURISTIC]`, so the redefinition creates no second prescription); `F₀`
never appears on the *right* of any condition with `φ_1` as source
because `F₀ ∉ L*_m`. Convention 2 (exact identity) ✔ — it *is* an exact
identity, just about a `Φ` nobody would call a method. Convention 1
(every basis) ✔.

**So `Φ` "supports jet transport" while being discontinuous, inconsistent
(zeroth order), non-convergent, and not equivariant.** `G` is arbitrary:
the admissible family contains a copy of `{all maps R^m → R^m}` for each
`m ≥ 2`.

### What this locates

The claim's framing — *"the characterization comes from taking that
seriously"* — is where this bites. `{C(n,A)}` is not a characterization
of anything; it is a **coherence / extension condition**. Structurally:

- `φ₁` is constrained by the system **only** through the affine rigidity
  (R) of Subtask 2. Nothing else in the entire diagram touches it.
  Everything that distinguishes Euler from RK4 lives in `φ₁` and is
  invisible to the diagram.
- On `L*_m`, `φ_m` is completely *determined* by lower levels.
- Off `L*_m`, `φ_m` is completely *free*.

So the diagram is a **left-Kan / free-extension structure**, not a
characterization: solutions = (arbitrary data off the lift loci) +
(forced propagation along them) + (the collision constraints of Subtask 2).

**Minimal condition that would exclude this object** (observation, not a
recommendation): the hypotheses need something that ties `φ_m` off the
lift locus to `φ_m` on it. Candidates in increasing strength:
continuity in `F` is **not** enough (`L*_m` is thin *and* closed, so a
bump supported off it is smooth); `GL_m(R)`-equivariance is **not**
enough (the orbit of `F₀` still misses `L*_m`); what does suffice is
**naturality/locality** — `φ_m(F)(y)` depending on `F` only through its
∞-jet at finitely many points, together with a uniform expression in `m`
(the "single map per dimension" of the statement's first sentence read as
*one formula*, not *one function*). The statement's own opening sentence
gestures at this and the skeleton drops it.

---

## Subtask 4 — (b) tensor composition. (done at the algebra level; partial at coordinates)

With convention 1, r1's coordinate objection **dissolves**: the composite
edge `n → nN_A → nN_A N_B` uses the product basis `{eᵢ⊗fⱼ}` in one order,
the direct `A⊗B` edge uses whichever basis, and since *every* basis of
`A⊗B` is quantified over, the product bases in both orders are among
them. So:

- `C(n,A) ∧ C(nN_A,B) ⟹ C(n,A⊗B)` **at the product bases**, via
  `f_{A⊗B} = (f_A)_B` `[UNVERIFIED]` and `(φ_n f)_{A⊗B} = ((φ_n f)_A)_B`.
- **Not** every basis of `A⊗B` is a product basis, so the converse
  direction — that `C(n,A⊗B)` at *all* bases follows from the two factor
  conditions at all their bases — needs the `GL_{N_A N_B}` orbit of
  product bases to be everything, which it is (any basis is `g·(product
  basis)`), **provided** the equivariance in Subtask 1 is available at the
  intermediate level. Since Subtask 1 gives equivariance only *restricted
  to lift orbits*, and `(f_A)_B` is in the lift orbit, this closes.
  `[GAP]` — I sketched this, did not verify it symbolically.
- `A⊗B ≅ B⊗A` gives two routes through different intermediate levels
  (`nN_A` vs `nN_B`); the square commutes for the same reason. **Both
  routes land on the same forced value of `φ_{nN_AN_B}`, so (b) coheres.**

**Where it does not cohere:** the poset-edge picture claims the edges
*compose*, but the set of edges `n → nN` is not closed under composition
in the relevant sense — `R[x]/x⁴` is a legitimate edge `1 → 4` that is
**not** any composite (it is tensor-indecomposable). The composable edges
generate only the decomposable labels. So the poset diagram has strictly
more edges than its composition closure, and by Subtask 2 the *binding*
constraints live exactly on the non-composable ones.

---

## Subtask 5 — (a) restriction along chains `n | n' | m`. (partial)

Coherence *is* forced along a chain when the two factorisations are
tensor factorisations of the same algebra (Subtask 4). It is **not
forced by the chain at all** when the label is indecomposable: `C(1,
R[x]/x⁴)` is not the composite of any pair of conditions on `1|2|4`.
Restated as an observation: divisibility records only `dim`, and `dim` is
a very lossy invariant of a Weil algebra (four non-isomorphic algebras at
`N = 4`, all giving different conditions on the same `φ₄`). The
index structure that actually carries the conditions is the **category of
Weil algebras**, with `dim : Weil → (N,×)` a monoidal functor down to the
poset. The poset is a shadow.

I could not extract a precise "restriction" statement to attack, so this
is a `[GAP]`, not a counterexample.

---

## Hypothesis-boundary probes (partial)

1. **Smoothness is missing.** The skeleton says "`f : R^n → R^n` a
   right-hand side" with **no regularity hypothesis**, but `f_A` is
   undefined for `f` that is not `C^k`, `k =` nilpotency order of `A`. So
   `C(n,A)` is not even a well-formed condition on the stated domain of
   `φ_n`. *Minimal condition that would exclude the pathology:* restrict
   the domain of `φ_n` to `C^∞` fields (or make `C(n,A)` conditional on
   `f ∈ C^{ord A}`). This is a real hole in the skeleton, cheap to close.
2. **`m = 1`.** The only factorisation is `1 = 1·1`, `A = R`, and
   `C(1,R)` is a tautology. So `φ₁` receives **no direct condition**;
   it is constrained only indirectly, via Subtask 2's affine rigidity
   pulled back from level 3. Worth recording: the base of the diagram is
   nearly free.
3. **`m` prime.** Only `n=1,N=m` and `n=m,N=1`. So `φ_p` is constrained
   only on the (thin) image of `L*_p` from level 1. Consistent with
   Subtask 3.
4. **Untouched:** step size `h` is nowhere in the skeleton. A real method
   is `φ_n(h,f)`; suppressing `h` is harmless for Euler/RK but I did not
   probe whether any condition becomes `h`-dependent (e.g. adaptive
   methods, where `φ_n` genuinely is not a function of `(n,f)` alone —
   the statement's opening sentence *excludes* adaptive methods by fiat,
   which is a scope choice worth surfacing).

---

## Definitional status

I considered raising `definitional-ambiguity` on the **coordinate
ordering of `A^n ≅ R^{nN}`** (component-major `(a₁ coords, a₂ coords, …)`
vs basis-major `(all first-basis-coords, all second, …)`; these differ by
a shuffle `σ` which is **not** of the form `g^{⊕n}`, so convention 1 does
*not* quantify it away). I attempted to build a `Φ` satisfying one
reading and not the other (`n=2`, `A=D`, `m=4`, a `φ₄` privileging
coordinate 2) and it **failed** — the candidate satisfied neither
reading. Without a verified divergence witness this is **vagueness, not
ambiguity**: recorded as a `[GAP]`, and the round proceeds. Someone
should pin the ordering down anyway.

---

## Search scope (bounds every "none found")

- **Weil algebras:** `R`; `D=R[x]/x²`; dim 3: `R[x]/x³`, `R[x,y]/(x,y)²`;
  dim 4: `R[x]/x⁴`, `R[x,y]/(x²,y²)`, `R[x,y]/(x³,xy,y²)`, `R[x,y,z]/m²`;
  dim 5: `R[x]/x⁵`, `R[x,y]/(x³,y²)`-monomial, `R[x,y]/(x⁴,xy,y²)`,
  `R⁴-fat-point`. **Monomial quotients only** — no non-monomial ideals,
  nothing of dim ≥ 6.
- **Identifications:** monomial-basis identity identification for the
  collision search; `GL₂` basis `(1,1+ε)` by hand for `D`. **No systematic
  `GL_N` sweep** — this is the main gap.
- **Fields:** univariate polynomial `f` of degree ≤ 4, 40 random integer
  points per pair, exact `Fraction`, seed 7. No multivariable `f`, no
  transcendental `f`, `n = 1` only in the collision search.
- **Methods:** explicit Euler (computed); RK reasoned about via linear-
  conjugation-equivariance, **not** computed; the Subtask-3 wild `Φ`
  (constructed, hypothesis-audited by hand, not machine-checked).
- **Levels:** `m ∈ {1,2,3,4,5}` plus prime/`m=1` boundary reasoning.

## Acquisition

`references/` is absent on this branch.

ACQUISITION: Kolář–Michor–Slovák, *Natural Operations in Differential
Geometry* ch. VIII (Weil bundles), and Jorba–Zou / Abad–Barrio–Blesa–
Rodríguez on jet-transport ODE integrators — to ground the two
`[UNVERIFIED]` facts and to check whether "the method is given by a
uniform arithmetic expression" is already standing in that literature
(that is exactly the hypothesis Subtask 3 shows is missing).

## Extension petition

**Subtask:** the `GL_N`-twisted collision search — solve
`U f_A U⁻¹ = g_B` for `U ∈ GL_N(R)`, `A ≇ B` of equal dimension, over
dims 3–6, rather than only the identity identification. **Expected
benefit:** qualitatively different from this round's sweep. Convention 1
makes twisted identifications legitimate edges, so a solution with `f`
**non-affine** would strengthen the derived rigidity (R) from "`φ₁`
preserves affine" to a constraint on higher jets — which is the only
route I see by which the diagram could constrain `φ₁` enough to say
anything about the *identity* of the method, and hence the only route by
which the word "characterization" in the claim could be earned. A null
result is equally informative: it would confirm that `φ₁` is essentially
free and the framework is a coherence condition only.
