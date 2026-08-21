# Melchior — jt-weil — Round 1

Slot start 15:35Z. Coherence audit only: I locate gaps, I do not fix them and do not
rank the claim's truth or interest.

## Subtask decomposition (worked in this order)

1. `references/` sweep for definitions of Weil algebra / Weil functor / jet transport.
2. (c) Well-definedness of `C(n,A)` — foundational: if `C(n,A)` is not a function of `A`
   alone, (a), (b), (d) are all statements about an undefined object.
3. Prior to (c): does the skeleton actually *define* `C(n,A)`?
4. (a) restriction along divisor chains — does the divisibility poset carry the natural
   restriction structure on Weil algebras at all?
5. (b) tensor composition of edges.
6. (d) "vector fields in common".

## 1. References — `untouched by necessity`

`/home/user/research/references/` does not exist on branch
`claude/jet-transport-weil-algebra-weyote`. Per §6.7 this is **not** evidence that no such
sources exist. Every attribution below is therefore tagged `[UNVERIFIED]`.

Definitions I am using (standard, from memory, `[UNVERIFIED]`):
a **Weil algebra** is a finite-dimensional commutative unital local `R`-algebra `A` with
residue field `R`, i.e. `A = R ⊕ m` with `m` the nilpotent maximal ideal. The associated
**Weil functor** `T_A` sends a smooth `f: R^n -> R^n` to `f_A: A^n -> A^n` (equivalently
`T_A R^n = A^n`), and `T_A T_B = T_{A ⊗_R B}` `[UNVERIFIED]` (Kolář–Michor–Slovák, product-
preserving functors on manifolds).

## 2. The condition `C(n,A)` is never defined — primary structural gap

The skeleton says:

> "define the compatibility condition C(n,A) on Phi **relating** phi_n(f) and phi_{nN}(f_A)"

`relating` is a placeholder, not content. Per §6.3 this is a `[GAP]`, and it is the gap
that everything the round was asked to assess sits on top of: (a) asks how these conditions
restrict, (b) how they compose, (c) whether they are basis-independent, (d) whether two of
them agree — none of these questions has a determinate answer while the relation is a blank.

At least two readings are in live circulation and they are not equivalent:

- **R1 (equivariance / strict lift):** `phi_{nN}(f_A) = (phi_n(f))_A` as maps `A^n -> A^n`.
- **R2 (projection / base-trajectory only):** `pi ∘ phi_{nN}(f_A) = phi_n(f) ∘ pi`, where
  `pi: A^n -> R^n` is induced by `A -> A/m = R`. I.e. the lifted run only has to reproduce
  the base trajectory, with no constraint on the nilpotent directions.

Divergence: take `n = 1`, `A = R[e]/(e^2)`, basis `(1,e)`, so `m = 2`. Then
`f_A(x,y) = (f(x), y f'(x))`. Let `phi_1(f)(x) = x + h f(x)` (Euler) and define
`phi_2(g)(x,y) = (x + h g_1(x,y), y + 2h g_2(x,y))`. This `Phi` is a legitimate
"function of `(n,f)` alone". It satisfies R2 at this instance (first component is
`x + h f(x)`, depends on `x` only, so it descends and equals `phi_1(f)∘pi`), and violates
R1 (`y + 2hy f'(x)` vs `y(1 + h f'(x))`). So the class of `Phi` "supporting jet transport"
is reading-dependent, and (d)'s "two prescriptions at once" only bites under R1 — under R2
the two conditions constrain *projections along different quotients* and generically do not
touch each other. I do not choose between R1 and R2.

The user's prose ("phi_m receives two prescriptions at once") leans R1; that is a lean, not
a definition, and it is not mine to convert into one.

## 3. (c) Basis dependence — the located gap

Skeleton step, quoted:

> "Fixing an R-basis of A gives an R-linear isomorphism A^n =~ R^{nN}, so (A^n, f_A)
> becomes an input (nN, f_A) to phi_{nN}."

**This step does not follow into a condition on `A` alone.** Two bases of `A` differ by
`T ∈ GL_N(R)`; the two coordinate presentations of the same map `f_A` differ by conjugation
by `S = T^{⊕n} ∈ GL_{nN}(R)`. A method is, by the stated hypothesis, *only* a function of
`(m, f)` — nothing in the hypotheses gives
`phi_m(S g S^{-1}) = S phi_m(g) S^{-1}`. Without that equivariance, `C(n,A)` is a condition
on the pair (algebra, basis), not on the algebra.

**Concrete witness that this is not a formality.** `n = 1`, `A = R[e]/(e^2)`.
`phi_1 =` Euler. Define
`phi_2(g)(x,y) = (x,y) + h·g(x,y) + (0, h·g_2(0,0))`.

- Basis `(1, e)`: coordinates of `a + be` are `(a,b)`; `g = f_A` is
  `g(x,y) = (f(x), y f'(x))`, so `g_2(0,0) = 0`. The perturbation vanishes, and
  `phi_2(f_A) = (x + hf(x), y(1 + hf'(x))) = (phi_1(f))_A`. **C(1,A) holds (R1).**
- Basis `(1 + e, e)`: coordinates `(alpha, beta)` with `a = alpha`, `b = alpha + beta`.
  Then `g(alpha,beta) = (f(alpha), (alpha+beta) f'(alpha) - f(alpha))`, so
  `g_2(0,0) = -f(0)`. For any `f` with `f(0) != 0` the perturbation is nonzero and
  `phi_2(f_A) != (phi_1(f))_A`. **C(1,A) fails.**

So `C(1, R[e]/(e^2))` is true in one basis and false in another *for the same `Phi`*. The
answer to (c) as posed — "is `C(n,A)` independent of the basis choice?" — is **no**, absent
an equivariance hypothesis that the statement does not contain. The `Aut_{R-alg}(A)` action
asked about in (c) is moreover the *wrong* group for this: basis changes form `GL_N(R)`,
while `Aut_{R-alg}(A)` is a (usually much smaller) subgroup — for `A = R[e]/(e^2)`,
`Aut = {e -> ce, c != 0} =~ R^*`, one-dimensional inside `GL_2(R)`. My witness above uses a
basis change *outside* `Aut(A)`. So even full `Aut(A)`-equivariance of `Phi` would not make
`C(n,A)` well-defined; what is needed is equivariance under all of `GL_N(R)` acting
`n`-diagonally. (c) as posed conflates "acts on the condition" with "makes the condition
well-defined"; those are different groups and the smaller one does not suffice.

`[HEURISTIC]` Affine-equivariant methods (Euler, all classical RK) *are* conjugation-
equivariant, so on the intended class of methods the gap is invisible — which is exactly why
it survived into the statement. It is still a missing hypothesis, not a triviality, because
the family `Phi` is defined here with no structure at all beyond "a function of `(n,f)`".
`[/HEURISTIC]`

## 4. (a) Restriction along divisor chains — the framing does not carry the structure

Two independent failures.

**(a-i) The natural restriction maps for Weil algebras are not divisibility-compatible.**
The genuine functoriality of jet transport is along *algebra homomorphisms* — truncation
`R[x]/x^{k+1} -> R[x]/x^k` (drop the top-order jet coefficient), inclusion of a sub-jet,
etc. Dimensions along these do not divide one another: `dim R[x]/x^3 = 3`,
`dim R[x]/x^2 = 2`, and `2 does not divide 3`. So the surjection `A -> A'` that expresses
"a 2-jet run restricts to a 1-jet run" is *not* an edge of the divisibility poset and cannot
be one. The divisibility poset indexes only the *ambient dimension bookkeeping*
(`n -> nN`), and the restriction structure the question asks about lives on a different,
non-divisibility-graded category. Asking "how do the conditions restrict along a chain of
divisors" therefore asks about a structure the index has no room for. `[GAP]`

**(a-ii) A divisor chain does not determine the conditions, so nothing is "forced".**
Two chains `n | 2n | 4n` and the direct step `n | 4n` bear on the same pair
`(phi_n, phi_{4n})` but via genuinely different algebras: composing `R[e]/(e^2)` with itself
gives `R[x,y]/(x^2,y^2)`, whereas the direct `N = 4` edge may be `R[x]/x^4` — non-isomorphic
algebras of the same dimension 4. `C(n, R[x,y]/(x^2,y^2))` and `C(n, R[x]/x^4)` are distinct
conditions, related by no restriction map. The claim in (a) that "coherence is forced when
`m` factors two different ways through the same chain" is unsupported: the only coherence
available is between chains that come from a *common tensor factorization*, and equality of
the dimension factorizations does not produce one.

**(a-iii) It is not a poset diagram.** From `N = 3` upward there are non-isomorphic Weil
algebras of equal dimension (`R[x]/x^3` and `R[x,y]/(x,y)^2`, both dim 3). Edges `n -> nN`
are therefore not determined by their endpoints, so `{C(n,A)}` is not a diagram over the
divisibility poset (a thin category); it is at best a diagram over a category with many
parallel arrows, fibred over `(N, ×)` by `dim`. The statement's "object indexed by the
divisibility poset, with the algebras as edges" is a mismatch with its own content — the
algebras cannot be the edges of a poset. This is a mismatch between the STATEMENT and the
FORMAL SKELETON's poset reading, flagged as instructed.

## 5. (b) Tensor composition — composes only up to a coordinate shuffle

Granting `T_A T_B = T_{A ⊗ B}` `[UNVERIFIED]`, the *maps* compose: `(f_A)_B = f_{A⊗B}`.
But the question asked is about the edges as inputs to `phi`, and there the composite
identification
`(A ⊗ B)^n =~ (A^n)⊗B =~ (R^{nN_A})⊗B =~ R^{nN_A N_B}`
differs from a directly chosen basis-identification of `(A⊗B)^n` by a **permutation of
coordinates** (the shuffle). Likewise `A ⊗ B =~ B ⊗ A` as algebras, but the two induced
identifications with `R^{nN_AN_B}` differ by the flip permutation `sigma`. Hence
`C(n, A ⊗ B)` obtained by composing the `A`-edge then the `B`-edge, and `C(n, A ⊗ B)`
obtained directly (or via the `B`-then-`A` route), are conjugate by `P_sigma`, not equal.
Composition of edges is therefore correct **only if** `Phi` is equivariant under those
permutation conjugations — the same missing hypothesis as §3, and my §3 witness functional
`g -> g_2(0,0)` is exactly the kind of non-equivariant ingredient that breaks it. So the
answer to (b)'s "does the poset-edge structure compose correctly" is: not from the stated
hypotheses; the square commutes on algebras and fails to commute on conditions.

Secondary, smaller: the edge `n -> n N_A` followed by `n N_A -> n N_A N_B` uses
`C(n N_A, B)`, which quantifies over **all** `f: R^{nN_A} -> R^{nN_A}`, whereas the
composite only needs it for the `f` of the special form `g_A`. So `C(n,A) & C(nN_A,B)`
implying `C(n, A⊗B)` (given equivariance) is plausible, but the converse direction —
`C(n, A⊗B)` giving back `C(nN_A, B)` — is not, since the latter is a strictly larger
quantifier range. Any claim that the conditions "compose under tensor products" must say
which direction; the statement does not. `[GAP]`

## 6. (d) "have vector fields in common" — `partial`

Fix `m` and two structures `m = n_1 N_1 = n_2 N_2` with algebras `A_1, A_2`. Let
`L_i ⊂ Maps(R^m, R^m)` be the image of `f -> (f)_{A_i}` under the chosen identification.

The natural single reading is `L_1 ∩ L_2 != {}` and, for `g` in that intersection with
`g = (f_1)_{A_1} = (f_2)_{A_2}`, the two prescriptions are
`phi_m(g) = (phi_{n_1}(f_1))_{A_1}` and `phi_m(g) = (phi_{n_2}(f_2))_{A_2}` (reading R1).

Findings:

- **Nothing forces agreement.** The two right-hand sides are computed from different data
  (`phi_{n_1}` vs `phi_{n_2}`) and no hypothesis relates them. So "supporting jet transport"
  as defined in the skeleton is a conjunction of conditions that may be jointly
  unsatisfiable, or may be satisfiable only by imposing an *additional* coherence axiom.
  The statement's "there `phi_m` receives two prescriptions at once" presupposes both are
  prescriptions of the same thing and silently treats consistency as automatic. `[GAP]`
  Which of {forced-agree, forced-disagree, independent} holds is exactly what is *not*
  determined by the stated hypotheses — the honest answer to (d) as posed is "none of the
  three follows".
- **The intersection is identification-dependent.** Whether `L_1 ∩ L_2` is nonempty is
  computed *after* choosing bases, so (d) is downstream of §3: change the basis of `A_1`
  and `L_1` moves inside `Maps(R^m,R^m)`. So "have vector fields in common" is not yet a
  property of `(n_1,A_1,n_2,A_2)`.
- **Degenerate common fields always exist**, e.g. `g = 0` (`0_{A} = 0` for every `A`), on
  which both prescriptions read `phi_m(0) = (phi_{n_i}(0))_{A_i}` and agree whenever
  `phi_n(0) = id`. So the intersection being nonempty is never in itself informative; the
  question needs the *non-degenerate* part of the intersection isolated, which the statement
  does not do. I did not get to computing a non-degenerate intersection
  (`m = 4`: `n=1, dim 4` vs `n=2, dim 2`) — `partial`.

## 7. What I did not examine

- Whether `phi_n(f)` is even required to be smooth (needed for `(phi_n(f))_A` to exist under
  reading R1 — Weil functors act on smooth maps). Untouched; a further candidate gap.
- Step size `h`: `phi_n` is declared a function of `(n,f)` alone, so `h` is either absorbed
  into `f` or is silent extra data. Under `h` absorbed into `f`, `(hf)_A = h·f_A` needs
  checking. Untouched.
- Convergence/order-of-accuracy content: out of scope for coherence.
- Any literature standing judgment: Casper's role, not mine.

## Verdict

`gap-found`, primary location §3 (basis step of the skeleton), with §2, §4 and §5 as
independent further gaps. In addition I report a `definitional-ambiguity` with witness on
the quantifier over bases (see block below), since (c) is exercised by it directly.

### DEFINITIONAL-AMBIGUITY

Convention: "**once a basis of A is fixed**" — the quantifier over bases in the definition
of `C(n,A)`.

- Reading **B1**: `C(n,A)` holds iff the relation holds **for some** basis of `A`.
- Reading **B2**: ... **for every** basis of `A`.
- Reading **B3**: a global choice function `A -> basis(A)` is fixed once and for all, and
  `C(n,A)` is evaluated in `basis(A)`.

Witness (the case §3 exercises): `n = 1`, `A = R[e]/(e^2)`, `phi_1 =` Euler,
`phi_2(g)(x,y) = (x,y) + h g(x,y) + (0, h·g_2(0,0))`, and any `f` with `f(0) != 0`.
`C(1,A)` **holds** in basis `(1, e)` and **fails** in basis `(1 + e, e)`. So this `Phi`
satisfies `C(1,A)` under B1, fails it under B2, and its status under B3 depends on the
choice function. The class of methods "supporting jet transport" — and hence every answer
to (a)–(d) — differs between the readings. I do not choose.

A second, prior ambiguity (R1 vs R2, §2) is reported there with its own witness; I list the
basis one as primary because it is textual (the statement says "once a basis is fixed") and
is the one (c) directly exercises.

## ACQUISITION

Kolář–Michor–Slovák, *Natural Operations in Differential Geometry*, ch. VIII (Weil functors,
`T_A T_B = T_{A⊗B}`), plus a primary source on jet transport of ODE integrators
(Alessi/Farrés/Haro or Gimeno–Jorba) for the intended form of the compatibility condition.
