# Melchior — jt-weil — Round 2

Slot start 2026-08-21T17:55:58Z. Role: coherence / gap location only. No fixes, no truth-ranking.

## Subtask decomposition (worked in this order)

0. `references/` consultation — **done** (directory absent on this branch; see acquisition line).
1. Type-check the skeleton's core identity `phi_{nN}(f_A) = T_A(phi_n(f))` — **done**.
2. (c) What convention 1 ("every basis") actually forces — **done**. Highest priority: it is a pure quantifier computation and it gates (a),(b),(d).
3. (b) Tensor composition of poset edges — **done**.
4. (d) "vector fields in common" — readings + divergence witness — **done**.
5. (a) Restriction along divisor chains — **partial** (reduced to (b)+(d); the two-different-chains coherence question is only sketched).

---

## 0. References

`/home/user/research/references/` does not exist on branch `claude/jet-transport-weil-algebra-weyote`. Per the standing rule this is **not** evidence that no sources exist. Everything below that touches a known object is flagged.

Known objects I rely on, and their status:
- Weil algebra = finite-dimensional local commutative unital R-algebra `A = R (+) m` with `m` nilpotent. `[UNVERIFIED]` against this repo (standard; Kolar-Michor-Slovak §35 is the usual source).
- Weil functor composition `T_A o T_B = T_{A (x) B}` (naturally). `[UNVERIFIED]` here; standard (KMS §35.18).
- Classification of Weil algebras of dim <= 3 over R: dim 2 gives only `R[e]/(e^2)`; dim 3 gives exactly `R[e]/(e^3)` and `R[x,y]/(x,y)^2` up to iso. `[UNVERIFIED]` here; used below only to produce a witness, and the witness can be checked by hand without the classification.

---

## 1. The stated identity does not type-check as written  — [GAP]

Skeleton: "let `T_A` denote the R-linear isomorphism `A^n =~ R^{nN}` induced by that basis. `C(n,A)` is the condition that `phi_{nN}(f_A) = T_A(phi_n(f))`".

- `T_A` is declared with domain `A^n`.
- `phi_n(f)` is the output of a numerical method on `f`. Under the only reading that makes `phi_{nN}(f_A)` meaningful, `phi_n(f)` is a *map* (a step map `R^n -> R^n`, presumably `h`-dependent), not an element of `A^n`.
- So `T_A(phi_n(f))` applies a map with domain `A^n` to an object that is not in `A^n`.

The identity only becomes well-formed if `T_A` silently denotes **two different things**: (i) the basis iso `tau_A : A^n -> R^{nN}`, used to present `f_A` as a field on `R^{nN}` so that `phi_{nN}` can eat it at all, and (ii) the operation on *maps* `g |-> tau_A o g_A o tau_A^{-1}`, which invokes the Weil **lift functor applied to `phi_n(f)`** — an operation nowhere introduced in the skeleton and carrying its own hypothesis (that `phi_n(f)` is smooth/liftable, and that `h` is treated as a real scalar rather than an element of `A`).

I do **not** raise this as a definitional ambiguity: settled convention 2 names the content "full lift-equivariance", which selects reading (ii). But the skeleton as written does not say that, and the un-stated liftability hypothesis on `phi_n(f)` is load-bearing for every part of (a)-(d). Recorded as `[GAP]`: the object `T_A` is overloaded and the lift-of-the-output operation is used without being defined.

Note also the LHS is basis-dependent in a way the skeleton hides: `phi_{nN}` eats a field on `R^{nN}`, so the LHS is really `phi_{nN}(tau_A f_A tau_A^{-1})`. Both sides move when the basis moves. This is what makes §2 work.

---

## 2. (c) Convention 1 *does* force an equivariance — the package's framing of it is where the argument breaks

Write, for a basis `b` of `A`, `tau = tau_b : A^n -> R^{nN}` (acting coordinatewise on the `n` `A`-slots), and
- `F_tau := tau o f_A o tau^{-1}` (the lifted field as seen on `R^{nN}`),
- `P_tau := tau o (phi_n f)_A o tau^{-1}` (the lifted output as seen on `R^{nN}`).

`C(n,A)` at basis `b` is exactly `phi_{nN}(F_tau) = P_tau`.

Change basis by `g in GL_N(R)`. Then `tau' = G o tau` with `G = g^{(+)n}` (block-diagonal, the *same* `g` in each of the `n` `A`-slots), because `f_A` and `(phi_n f)_A` are basis-free maps `A^n -> A^n`. Hence
- `F_{tau'} = G F_tau G^{-1}`, `P_{tau'} = G P_tau G^{-1}`.

Imposing `C(n,A)` at both bases gives

>  `phi_{nN}(G F G^{-1}) = G phi_{nN}(F) G^{-1)`  for every `F` in the set `L(n,A) := {tau_b f_A tau_b^{-1}}` of lifted fields, and every `G in Delta_n(GL_N(R)) := {g^{(+)n}}`.

**So convention 1 is not quantifier hygiene; it is equivalent to (single-basis `C(n,A)`) AND (a genuine conjugation-equivariance of `phi_{nN}`).** Precisely:

- What it **does** force: `phi_{nN}` is `Delta_n(GL_N(R))`-equivariant *on the subset `L(n,A)` of lifted fields*.
- What it **does not** force: equivariance of `phi_{nN}` on arbitrary fields, and equivariance under arbitrary `GL_{nN}(R)` (or even arbitrary block-diagonal `GL_N` blocks that differ between slots). The user's remark "that does not force equivariance" is correct for the *full* `GL_{nN}(R)`-on-all-fields statement, and false for the restricted statement just displayed.

This is the weakest joint in the package: the task text treats convention 1 as making `C(n,A)` "well-defined as a condition on `A` alone" — a purely bookkeeping move — when in fact it strictly strengthens the round-1 single-basis condition by exactly the above equivariance. Well-definedness in the trivial sense (the quantified condition depends only on `A`, since the basis is bound) is granted; but the conclusion that the basis choice has been rendered *inert* does not follow, and §3 shows it has consequences.

Consequently the `Aut_{R-alg}(A)` question is **not** superseded, and the two group actions must be kept apart:
- `Aut_{R-alg}(A) <= GL_N(R)` is the subgroup whose conjugation action fixes `L(n,A)` setwise **and** commutes with the lift construction (`f_{A}` is `Aut`-equivariant because the lift is functorial in the algebra). For `alpha in Aut(A)`, both sides of `C(n,A)` transform the same way *for the same `f`*.
- A general `g in GL_N(R)` moves `f_A` to a field that is still in `L(n,A)` (it is `f_A` read in another basis) but the identification with "the lift of `f`" changes. The equivariance in the display is therefore a constraint on `phi_{nN}`, whereas the `Aut(A)` part of it is automatic given `C(n,A)` at one basis.

So the honest split is: **`C(n,A)` at all bases = `C(n,A)` at one basis + `GL_N(R)/Aut(A)`-conjugation-equivariance of `phi_{nN}` on `L(n,A)`.** `[GAP]`: the package never states this decomposition and (b) below silently needs it.

---

## 3. (b) Tensor composition: the poset edges do **not** compose to an equivalence

Set `A` (dim `N_A`), `B` (dim `N_B`).

**Forward direction (composite implies tensor edge, product bases only).** Using `T_A o T_B =~ T_{A (x) B}` `[UNVERIFIED here]`: `f_{A (x) B} = (f_A)_B` up to the canonical iso. Then
- `C(n,A)`: `phi_{nN_A}(f_A) = (phi_n f)_A`,
- `C(nN_A, B)` applied to the field `f_A` on `R^{nN_A}`: `phi_{nN_A N_B}((f_A)_B) = (phi_{nN_A}(f_A))_B = ((phi_n f)_A)_B = (phi_n f)_{A (x) B}`.

This is `C(n, A (x) B)` **at the product basis** `{a_i (x) b_j}` in the ordering induced by the composite identification `R^{(nN_A)N_B}`.

**Where it breaks.** Convention 1 demands `C(n, A (x) B)` at *every* R-basis of `A (x) B`, and not every basis of `A (x) B` is a product basis. By §2, the composite delivers, on top of the product-basis identity, exactly the equivariance generated by
- `Delta_n(GL_{N_A})` acting as `g_A (x) 1` (from `C(n,A)`, pushed through the `B`-lift), and
- `Delta_{nN_A}(GL_{N_B})` acting as `1 (x) g_B` (from `C(nN_A,B)`),

i.e. the subgroup `<GL_{N_A} (x) 1, 1 (x) GL_{N_B}> <= GL_{N_A N_B}(R)`, whereas `C(n, A (x) B)` at all bases requires equivariance under **all** of `GL_{N_A N_B}(R)`. These differ: for `N_A = N_B = 2` the generated subgroup has dimension at most `4 + 4 - 1 = 7` inside `GL_4` (dim 16). Concretely, `h in GL_4(R)` not of the form `(g_A (x) g_B)`-generated, e.g. a generic element mixing `1(x)b_1` with `a_1(x)1`, gives a basis of `A (x) B` at which the composite says nothing.

So, as stated, **(b) fails as an equality of conditions**: `C(n,A) & C(nN_A,B)  ==>  C(n, A(x)B)-at-product-bases`, strictly weaker than `C(n, A(x)B)`. The poset diagram commutes only after the all-bases quantifier is weakened to product bases on tensor edges — and convention 1 forbids that weakening. This is a concrete incoherence between convention 1 and the compositional structure the package asserts.

Additional unaddressed points in (b):
- The converse (`C(n,A(x)B) ==> C(n,A)`) is asserted nowhere and I see no route to it: `C(n,A(x)B)` constrains `phi_{n N_A N_B}` and `phi_n`, and does not mention `phi_{nN_A}` at all.
- `A (x) B =~ B (x) A` means the *same* poset edge `n -> nN_AN_B` is obtained via two different intermediate nodes (`nN_A` and `nN_B`). The package asserts edge-composition but never checks this square commutes; it is the (a)-question in disguise and it inherits the product-basis defect above.
- The `nN_A`-node is entered by `C(nN_A,B)` quantified over *all* fields on `R^{nN_A}`, but only ever used on `L(n,A)`. Not an error, but the diagram's "edges compose" language suggests a functor and there is none: edges are conditions on distinct `phi`'s, not morphisms with a composition law.

---

## 4. (a) Restriction along divisor chains — partial

Reduced, not resolved. `n | n' | m` with `n' = nN_A`, `m = n'N_B` is exactly the (b) situation, so all of §3 applies. The genuinely distinct case — `m` factoring two ways through the *same* chain, i.e. `m = nN = n''N''` with `n != n''` — produces two conditions on `phi_m` whose hypotheses (which fields they constrain) generally have different domains; whether they interact is precisely (d). I did not get to a systematic account of the restriction maps; **partial**.

One structural observation I did check: the "divisibility poset with algebras as edges" is not a poset diagram in the usual sense, because there are many edges `n -> nN` (one per Weil algebra of dim `N`, and dim-`N` Weil algebras are not unique for `N >= 3`). It is at best a graph/multicategory. The package's phrase "an object indexed by the divisibility poset" is `[GAP]`-tagged: no diagram shape is specified that could make the conditions restrict along divisors, and divisibility itself is not what indexes the data (the algebra does).

---

## 5. (d) "have vector fields in common" — definitional ambiguity **with witness**

At least two readings are in play, and my analysis of (d) exercises a case where they give different answers.

**Reading (I) — field-level overlap.** `F : R^m -> R^m` lies in `L(n,A) ∩ L(n'',B)`: the *same* map on `R^m` is simultaneously a basis-presentation of an `A`-lift and of a `B`-lift.

**Reading (II) — base-field-level overlap.** Same `n`, same `f : R^n -> R^n`, two algebras `A, B` of the same dimension `N`: `phi_m` receives a prescription from `f_A` and one from `f_B`; "the vector field in common" is `f`.

(A third reading — the two lift structures share a common quotient/sub-Weil-algebra, so the prescriptions agree on a subspace of `R^m` — is available; I did not exercise it, so I do not offer it as part of the witness.)

**Divergence witness (exercised in this round).** `n = 1`, `N = 3`, `m = 3`; `A = R[e]/(e^3)` with basis `1,e,e^2`; `B = R[x,y]/(x,y)^2` with basis `1,x,y`; `f(t) = t^2`.

- `f_A(a_0,a_1,a_2) = (a_0^2, 2a_0a_1, 2a_0a_2 + a_1^2)`.
- `f_B(b_0,b_1,b_2) = (b_0^2, 2b_0b_1, 2b_0b_2)`.

These differ (third coordinate, by `a_1^2`), so `f` is **not** a case of Reading (I): under (I) the hypothesis of (d) is not instantiated here at all, and (d) says nothing about this pair. Under Reading (II) the hypothesis *is* instantiated (same `f`, two dim-3 algebras), and the answer is "the two prescriptions are **independent**": they pin `phi_3` at two different arguments `f_A != f_B`, so nothing is forced.

Different verdicts on the same concrete case — "not an instance" vs "an instance on which nothing is forced" — and the case is one my §5 analysis actually runs. That is a divergence witness. I do not choose a reading.

**What I could establish under Reading (I), for the record** (this is the substantive content of (d) and is where the package's "point of interest" lives): the two prescriptions on a common `F` are *forced to agree*, trivially, since both equal `phi_m(F)`; the content is whether the overlap contains anything non-degenerate. In the standard bases, `f_A = g_B` (with `A,B` as above, `n=1`) forces `f = g` and then `f''(a_0) a_1^2 / 2 = 0` for all `a_1`, i.e. `f` affine — on which any reasonable method's output is affine and both lifts agree. So in standard bases the overlap is degenerate. But convention 1 makes the overlap the intersection of two `Delta_n(GL_N)`-**orbits**, which is a much larger set, and I have **no** argument either way about whether it meets the non-affine fields. `[GAP]`: the package asserts `phi_m` "receives two prescriptions at once" without establishing that the two prescription-domains meet at any field where the prescriptions have independent content. If they meet only at affine fields, the "point of interest" is empty; the package does not address this.

---

## 6. Summary of located gaps

- **G1 (§1)** `T_A` is overloaded: declared as a linear iso `A^n -> R^{nN}`, applied to `phi_n(f)` which is not in `A^n`. The lift-of-the-output operation and its liftability hypothesis on `phi_n(f)` are used but never introduced.
- **G2 (§2, primary)** The package's premise that convention 1 is inert bookkeeping does not follow. All-bases `C(n,A)` = one-basis `C(n,A)` + `Delta_n(GL_N(R))`-conjugation-equivariance of `phi_{nN}` on lifted fields. It forces a (restricted) equivariance; the `Aut(A)` action is the automatic part of it and is *not* superseded.
- **G3 (§3)** Edge composition fails: `C(n,A) & C(nN_A,B)` yields `C(n,A(x)B)` only at product bases; convention 1's all-bases quantifier demands `GL_{N_AN_B}(R)`-worth of bases, strictly more than the `<GL_{N_A}(x)1, 1(x)GL_{N_B}>` the composite supplies. The converse direction is unsupported.
- **G4 (§4)** "indexed by the divisibility poset" is not a diagram shape: multiple non-isomorphic algebras give parallel edges `n -> nN`, and no restriction maps are specified.
- **G5 (§5)** The (d) overlap is not shown non-degenerate; in standard bases it collapses to affine fields.

## Acquisition

ACQUISITION: Kolar-Michor-Slovak, *Natural Operations in Differential Geometry*, §35 (Weil algebras, Weil functors, `T_A o T_B = T_{A (x) B}`), plus any source classifying real Weil algebras in low dimension.
