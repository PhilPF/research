# casper — jt-weil — round 2 — outside-view / framing review

Slot: 10 min. Subtask decomposition (worked in order):

1. references/ sweep — **done** (directory absent on this branch)
2. Literature fit: does this framing match jet transport / Weil-functor
   literature? — **done**
3. Is the index structure (divisibility poset) the right one? — **done**
   (this is where my principal finding is)
4. Hypothesis/conclusion strength; degenerate ends; well-formedness — **done**
5. (d) "vector fields in common" — reading analysis — **done**
6. Constructive status — **partial**
7. Cross-check against how (a)/(b) would look in the alternative framing —
   **partial**

I did not read `reviews/jt-weil-r1-*.md`, including my own, to keep this
slot's input identical to what the dispatcher sanitized.

---

## 0. references/

`/home/user/research/references/` does not exist on this branch. Per the
standing rule this is not evidence that no primary source exists. All
attributions below are from recall and are marked `[UNVERIFIED]`
accordingly; I have invented no citation.

---

## 1. Literature fit — does anyone recognize this question?

Two distinct literatures are being fused here, and the fusion is real, not
imagined:

- **Jet transport / differential algebra (DA) integration.** Propagating a
  truncated Taylor polynomial through a standard integrator (RK, Taylor
  series, symplectic) by replacing real arithmetic with arithmetic in
  `R[x_1..x_k]/m^{d+1}`. Used in astrodynamics for uncertainty and
  invariant-manifold propagation. Associated with Berz (DA), and with
  Jorba/Gimeno and collaborators for the "jet transport" terminology.
  `[UNVERIFIED]`
- **Weil algebras / Weil functors.** The recognized structural theorem is
  that product-preserving functors on the category of smooth manifolds are
  exactly the Weil functors `T_A`, with `T_{A⊗B} = T_A ∘ T_B`. I recall this
  as the Eck / Kainz–Michor / Luciano circle, presented in Kolář–Michor–
  Slovák, *Natural Operations in Differential Geometry*, ch. VIII.
  `[UNVERIFIED]` — I could not ground the statement or its number without
  `references/`, and I will not assert a number I cannot check.

**Judgment:** the *substance* — "jet transport is not a method on an
enriched space, it is a compatibility condition between `phi_n` and
`phi_{nN}` through the lift `f ↦ f_A`" — is a correct and genuinely good
reframing, and it is the reframing the Weil-functor literature would
recognize. Both the folklore fact ("a method built from `+`, `×`, and
scalar operations on evaluations of `f` transports jets automatically,
because the lift is functorial for those operations") and the desired
converse ("that is the *only* way") are real, recognizable questions.

So the round is not chasing a phantom. My concern is entirely about the
*index structure* chosen to carry it.

---

## 2. Principal finding — the divisibility poset is the wrong index object

This is the outside-view concern I most want on record.

The statement organizes everything over `(N, |)`, with a Weil algebra `A`
of dimension `N` supplying an edge `n → nN`. But the structure that
actually carries the data is the **category `W` of Weil `R`-algebras with
`R`-algebra homomorphisms**, and `Phi` is (or wants to be) something like a
natural transformation over `W`. The divisibility poset is the image of `W`
under `A ↦ dim_R A` — a lossy, dimension-only shadow. Three consequences:

**(i) It collapses non-isomorphic algebras of equal dimension.** `dim = 4`
contains at least `R[x]/(x^4)`, `R[x,y]/(x^2, y^2)` (as a quotient of the
right degree), `R[x,y]/(x^2,xy,y^2)` extended, etc. These give genuinely
different conditions on the same `phi_{4n}`; the poset sees one edge
`n → 4n` where there are many. So the "diagram over the divisibility poset"
is not a diagram over a poset at all: it is a diagram over a free category
on edges labelled by isomorphism classes (and, with convention 1, by bases).
Calling it the divisibility poset is not a harmless abbreviation — it is the
very thing that makes item (d) look like a puzzle.

**(ii) It hides the real morphisms.** The interesting maps between Weil
algebras are algebra homomorphisms — the projection `R[x]/(x^3) →
R[x]/(x^2)` (truncation order), the inclusions/projections for `A ⊗ B`, the
augmentation `A → R`. *Truncation-order reduction is the single most
important operation in actual jet transport practice*, and it is precisely
an algebra homomorphism that the divisibility poset cannot express (it is a
surjection `3 → 2`, going the wrong way along divisibility, and `2 ∤ 3`).
A framing of jet transport that cannot express "drop from order 2 to order
1" has dropped the practitioner's main move.

**(iii) It makes (a) and (b) into bookkeeping and (d) into an artifact.**

- **(a) restriction along `n | n' | m`:** in `W`, chains of divisors are not
  the carrier of coherence; composition of algebra morphisms is. The
  question "is coherence forced when `m` factors two ways through the same
  chain" is, in `W`, the question of whether the relevant square of Weil
  functors commutes — and `T_{A⊗B} = T_A ∘ T_B` (up to canonical iso) says
  it does, *when the two factorizations are related by a tensor
  decomposition*. When they are not, the poset says the two edges share
  endpoints and the category says nothing links them. The poset framing
  invites the reader to expect coherence from the shared endpoint `m`, which
  is exactly the wrong expectation.
- **(b) tensor composition:** this is the one item where the poset framing
  does track the real structure, because `dim(A ⊗ B) = N_A N_B` is
  multiplicative and matches edge composition. I expect `C(n, A⊗B)` to
  follow from `C(n,A)` and `C(nN_A, B)` (given the canonical
  `T_{A⊗B} = T_A ∘ T_B`, and given that the tensor-product basis is among
  the bases quantified over) — but note the *converse* fails to be
  symmetric in an informative way: `A⊗B ≅ B⊗A` as algebras, so the two
  routes `n → nN_A → nN_A N_B` and `n → nN_B → nN_A N_B` must agree, and
  that agreement is a real constraint that the poset makes invisible
  (it is one edge either way). **This asymmetry is the genuine content
  hiding under (b), and (b) as posed does not ask for it.**
- **(d):** see §5. In `W`, "two lift structures on the same `R^m`" is not a
  coincidence to be resolved; it is two unrelated objects of `W` that happen
  to have the same dimension. The pressure to make them interact comes from
  the poset, not from the mathematics.

**Framing recommendation (stated as a finding, not a fix):** the statement
worth having is almost certainly indexed by `W`, with the divisibility poset
as a derived invariant. As posed, the characterization risks being a
technically correct result about a shadow of the right object.

---

## 3. Is the conclusion's strength matched to the hypotheses? / near-circularity

Two things concern me.

**(3a) `phi_n(f)` is a point, and there is no state and no step size.** The
skeleton says `phi_n` is a function of `(n, f)` alone and that
`phi_{nN}(f_A) = T_A(phi_n(f))` holds *as elements of `R^{nN}`*. So
`phi_n(f)` is a vector, not a map. A one-step numerical method is really
`Psi: (f, h) ↦ (R^n → R^n)`. Under the skeleton as written, `T_A(phi_n(f))`
only typechecks if `phi_n(f) ∈ R^n` is pushed into `A^n` along the scalar
inclusion `R ↪ A` — in which case the condition says: *running the method
over `A` returns a purely-real answer with zero nilpotent part.* That is the
negation of what jet transport is for; the nilpotent components **are** the
derivatives, and they are the entire product.

I do not think the user means this. But it is what the pinned-down skeleton
literally says, and the discrepancy is load-bearing: the whole point of jet
transport is that you seed at a *non-real* point `x_0 + ε` of `A^n` and read
off the infinitesimal part. A skeleton with no initial condition cannot see
that. **The most likely repair-shaped reading — `phi_n` is a map `R^n → R^n`
and the condition is `phi_{nN}(f_A) = T_A ∘ phi_n(f)_A ∘ T_A^{-1}` as maps —
is a materially different statement, and the round is being asked to analyse
the pointwise one.** I flag this as the largest single risk.

**(3b) Near-circularity risk.** If the reading is repaired to the map-level
one, the condition "`phi` commutes with every Weil lift" is very close to
being a restatement of "`phi` is computed by operations that commute with
Weil lifts", i.e. arithmetic in `f`-evaluations. That is the theorem worth
having *only if* the characterization output is an independent description
(e.g. "`phi_n(f)` is a polynomial/rational expression in evaluations of `f`
at affine combinations of the argument, with universal coefficients" — a
Butcher-series-like conclusion). If the conclusion is instead "`Phi` is a
natural transformation of Weil functors", the result is a rephrasing, not a
characterization. `[HEURISTIC]` I judge the Butcher/B-series-shaped
conclusion to be the one that would be recognized as a theorem; the
naturality-shaped one is definitional. `[/HEURISTIC]`

---

## 4. Degenerate ends and well-formedness

- **`N = 1`, `A = R`.** Not vacuous, and this is a good sign for convention
  1. Bases of `R` are nonzero scalars `λ`; `T_λ` is division by `λ`; `C(n,R)`
  at all bases becomes a scalar-rescaling equivariance for `phi_n`. Classical
  RK methods satisfy it. So the "every basis" convention has genuine, correct
  content even at the bottom of the poset. Convention 1 is doing real work.
- **Smoothness is missing from the hypotheses and is required.** `f_A` is
  undefined for a general `f: R^n → R^n`: for `A = R[ε]/(ε^2)` it needs `C^1`;
  for nilpotency order `d` it needs `C^d`; quantifying over *all* Weil
  algebras therefore needs `C^∞` (or polynomial/analytic). The skeleton says
  only "`f: R^n → R^n` a right-hand side". As stated the condition is
  ill-formed on most of its quantifier's range. This also has framing bite:
  a *numerical* method is judged on `C^1`/Lipschitz data, so a
  characterization that only sees `C^∞` inputs cannot constrain the method
  where it is actually used. Not fatal, but it should be a hypothesis, not
  an omission.
- **The large-`A` end.** "Every Weil algebra" is a proper-class quantifier
  as written; up to isomorphism it is essentially small but *not finite in
  each dimension* (there are positive-dimensional families of local
  algebras once `dim` is large enough) `[UNVERIFIED]`. Combined with "every
  basis", `C(n,A)` is an uncountable family of conditions. That is fine
  logically, but it means "supports jet transport" is not a checkable
  predicate on the nose — see §6.

---

## 5. (c) and (d)

**(c).** Convention 1 makes `C(n,A)` well-defined as a condition on `A`
alone: yes, trivially, since the basis is universally quantified away.
The substantive content is what I think the user's remark is pointing at,
and I believe the remark is correct. Changing the basis of `A` acts on
`R^{nN} = (R^N)^n` by the *block-diagonal* `g^{⊕n}`, `g ∈ GL_N(R)` — not by
general `GL_{nN}(R)`. So "holds at every basis" is equivalent to "holds at
one basis, **plus** `phi_{nN}` intertwines the `g^{⊕n}`-action **only on the
subset of vector fields that arise as `A`-lifts**". That is strictly weaker
than any equivariance requirement on `Phi`: it says nothing about `phi_m`
on a field that is not a lift, and nothing about `g ∈ GL_m` outside the
block-diagonal image. So the user's "it must hold for all bases, but that
does not force equivariance" is exactly right, and the precise content is:
*orbitwise equivariance on the image of the lift, under a proper subgroup.*
`Aut_{R-alg}(A)` is not superseded — it is the stabilizer of the lift
structure inside that subgroup, i.e. the `g` for which `f_A^{gB} = f_A^{B}`
for all `f`. It picks out where the "all bases" quantifier is *redundant*.
That is a real and worthwhile question and it survives my framing critique
intact. `[GAP]` I have not verified the claimed equivalence; I state it as
the shape I expect, not as established.

**(d) — the point of interest, and a fresh ambiguity.** "Have vector fields
in common" admits at least two readings that this round actually exercises,
and they disagree on whether the hypothesis of (d) is generic or rare. See
the DEFINITIONAL-AMBIGUITY block at the end.

Beyond the ambiguity: outside-view, I expect the honest answer to (d) to be
**"independent, except where an algebra homomorphism links the two"** — and
that answer is uninteresting *in the poset framing* while being the correct
and useful answer in the `W` framing. The fact that (d) is flagged as "the
point of interest" while being, I suspect, an artifact of the lossy index
structure is what pushes my verdict.

---

## 6. Constructive status (informational)

- The *definition* of `C(n,A)` is constructive: an equality of vectors,
  universally quantified. No excluded middle, no choice in the statement.
- "Supports jet transport" is a `Π`-statement over an essentially-small but
  uncountable index (algebras up to iso × bases × `n` × all `f`). Not
  decidable, but not classically-flavoured either; the `§5` reduction (one
  basis + equivariance) is a genuine constructive simplification if it holds.
- The *characterization theorem*, if it takes the expected shape ("`Phi`
  supports jet transport iff `phi_n(f)` is given by a universal expression
  in evaluations of `f`"), would very likely be proved by extracting the
  expression from `phi` via evaluation on lifted fields — i.e. **witness-
  producing**, hence plausibly constructive. I see no step that obviously
  demands choice.
- Not assessed: whether the "every Weil algebra" quantifier can be replaced
  by a cofinal countable family (e.g. `R[x_1..x_k]/m^{d+1}`) — that would
  matter a lot for computability. Marked partial.

Overall: **unclear**, leaning constructive, on incomplete analysis.

---

## 7. Verdict rationale

I am returning `likely-misframed`, on two independent grounds, either of
which alone I would have called `suspicious`:

1. The index structure is the dimension-shadow of the category of Weil
   algebras. It collapses non-isomorphic algebras, cannot express truncation
   morphisms (the practitioner's main operation), and manufactures (d) as a
   puzzle. Items (a) and (d) inherit their difficulty from the encoding.
2. `phi_n(f)` as an element of `R^n` with no initial condition and no step
   size makes the pinned-down `C(n,A)` say "the lifted run has zero nilpotent
   part" — i.e. it constrains away exactly the data jet transport exists to
   compute.

Item (b) and item (c) are, by contrast, well-posed and worth their slots.
This is a partial misframing, not a worthless one, and the salvage is
visible: re-index over `W`, and make `phi_n(f)` a map.

---

ACQUISITION: Kolář–Michor–Slovák, *Natural Operations in Differential
Geometry*, ch. VIII (product-preserving functors = Weil functors), plus one
primary jet-transport source (Berz, *Modern Map Methods*, or a
Jorba–Gimeno jet-transport paper) — I could not ground either attribution.
