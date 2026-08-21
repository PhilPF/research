# casper — outside-view review — claim `jt-weil`, round 1

Role: framing fit. Not proving, not ranking truth, not proposing fixes.

## Subtask 0 — references (done)

`/home/user/research/references/` is **absent** on this branch (glob over
`references/**/*` returns nothing; the only `.md` files in the tree are
`CLAUDE.md` and the agent definitions). Per §6.7 this is **not** evidence that
no such sources exist. Every attribution below is therefore flagged
`[UNVERIFIED]` and the claims resting on them are weakened accordingly.
Acquisition request at the end.

---

## Subtask 1 — literature fit (done)

Two well-populated bodies of work sit under this statement, and the statement
sits between them without landing in either.

**(A) Jet transport / differential algebra (numerics).** `[UNVERIFIED]` The
technique the user names is the one used in astrodynamics and validated
integration: replace floating-point arithmetic by arithmetic in a truncated
polynomial algebra `R[x_1..x_k]/m^{q+1}` and run an *unmodified* integrator
over it, obtaining the flow's Taylor jet in initial conditions. Associated
names I recall but cannot ground here: Berz (differential algebra, COSY
Infinity, Taylor models); Jorba, Gimenez, Haro (jet transport); Wilczak
(rigorous C^r integration). All `[UNVERIFIED]`.

The operative folklore statement in that literature is *not* the one proposed.
It is: **a one-step method that is a composition of the ring operations and
`f`-evaluations commutes with base change along any commutative unital
`R`-algebra map**, hence with `T_A` for every Weil algebra `A`. The content is
carried by the *syntactic form of the method* (arithmetic expression in `f`),
not by an indexing of `phi` by dimension.

**(B) Weil functors (differential geometry / SDG).** `[UNVERIFIED]` Weil
algebras index the product-preserving bundle functors on manifolds:
`T_A ∘ T_B = T_{A⊗B}`, and product-preserving functors on `Mf` are exactly the
`T_A` (Kainz–Michor / Eck / Luciano; exposition in Kolář–Michor–Slovák,
*Natural Operations in Differential Geometry*). All `[UNVERIFIED]` — I could
not ground these in `references/`.

**Fit judgement.** A reader from either literature would recognise the
*subject*. They would not recognise the *question*, for the reasons in
Subtask 2. In particular (B) already supplies, in finished form, the answer to
task item (b) — and supplies it over the **category of Weil algebras**, not
over the divisibility poset. The proposal re-indexes a known monoidal
structure by a lossy invariant (`dim`) and then asks whether composition works
in the re-indexed structure.

---

## Subtask 2 — is this the statement worth having? (done)

### 2.1 The "characterization" has no right-hand side. This is the main concern.

The skeleton reads:

> `Phi` supports jet transport **iff** `C(n,A)` holds for every `n` and every
> Weil algebra `A`.

That is a **definition of the predicate**, presented as its characterization.
A characterization needs an independently-described class on the other side of
the `iff` — e.g. "…iff `Phi` is (locally) given by a B-series", "…iff each
`phi_n(f)` is a rational expression in finitely many `f`-evaluations", "…iff
`Phi` extends to a natural transformation on the category of Weil algebras".
None is offered. As posed, the theorem is `P ⟺ P`.

This is exactly the near-circularity failure mode I am here to catch, and it
appears at the top level rather than after a chain of quiet hypothesis
strengthening. The user's prose ("The characterization comes from taking that
seriously") shows the intent is genuinely to *derive structure* from the
condition — but the derived structure named in the prose is again a list of
properties **of the condition** (restriction, tensor composition, `Aut`
action), not a description of the methods satisfying it.

### 2.2 `C(n,A)` is never defined, and the readings are not equivalent

The skeleton says only "the compatibility condition `C(n,A)` … relating
`phi_n(f)` and `phi_{nN}(f_A)`". The whole round's deliverables (a)–(d) are
statements *about* `C`. See the definitional-ambiguity section below; I regard
this as the blocking issue, above even 2.1.

### 2.3 The axiom is too weak for its own construction to be well-posed (bears on (c))

"`phi_n` is a function of `(n,f)` alone" grants **no** equivariance. The
identification `A^n ≅ R^{nN}` requires a choice of `R`-basis of `A`; two
choices differ by `S ∈ GL_N(R)`, acting on `R^{nN}` as `S^{⊕n}`. `C(n,A)`
stated with basis 1 and with basis 2 are the same condition **only if**
`phi_{nN}` commutes with conjugation by `S^{⊕n}`. Nothing in the axioms
supplies that.

So (c) as asked ("is `C(n,A)` actually independent of the basis choice?") has,
on the stated hypotheses, the answer "no, it depends on `(A, basis)`" —
and the repair is to add linear (or affine) equivariance of `Phi`. That repair
is standard and true of real methods `[UNVERIFIED: Runge–Kutta methods are
equivariant under invertible linear changes of variables]`, but it is a
**hypothesis addition**, and it is the one to watch: once `Phi` is assumed
equivariant, `Aut_{R-alg}(A) ⊂ GL_N(R)` acts and (c) collapses into a
restatement of that assumption rather than a finding. Item (c) is therefore
structurally at risk of being "well-argued answer to a question the added
hypothesis already answered".

Note also the mismatch: (c) asks about `Aut_{R-alg}(A)`, but the object
actually threatening well-definedness is the full `GL_N(R)` of basis changes.
`Aut(A)` is the *stabiliser* of the algebra structure; it is not what the
identification `A^n ≅ R^{nN}` quantifies over. Flagging this as a mismatch
between the prose and the skeleton.

### 2.4 The divisibility poset is the wrong index category (bears on (a),(b))

`dim` is a very lossy invariant of a Weil algebra. `R[x]/(x^3)` and
`R[x,y]/(x,y)^2` both have `N = 3` and both give an edge `n -> 3n`, yet they
impose genuinely different conditions (second-order jet in one direction vs.
first-order jets in two). The poset records only that *some* edge exists.

Consequently:

- **(a) restriction along `n | n' | m`.** The poset structure suggests a sheaf-
  or diagram-coherence statement. But an edge `n -> n'` is not a morphism —
  it is a whole family of unrelated conditions indexed by the isomorphism
  classes (indeed the moduli) of Weil algebras of dimension `n'/n`. "Coherence
  forced when `m` factors two ways through the same chain" presupposes the
  edges compose as edges. They do not compose as *poset* edges carrying data;
  they compose as *algebra* data. So (a) is asking a coherence question in a
  structure that has been stripped of the very labels the coherence would be
  about.
- **(b) tensor product.** In the Weil-functor category this is settled:
  `T_A ∘ T_B = T_{A⊗B}` `[UNVERIFIED]`, and `dim(A⊗B) = N_A N_B` is a
  *corollary*, not the content. Under the poset re-indexing, (b) can only ask
  whether the dimensions multiply — which they do, trivially — so the poset
  formulation loses precisely what makes (b) a theorem. Worse, the poset does
  not see that not every `N_A N_B`-dimensional algebra is a tensor product, so
  the edge `n -> n N_A N_B` is over-populated relative to the composites.

I therefore judge the poset framing a **downgrade of an available and better
structure**. The honest object is: `Phi` together with the assignment
`A ↦ C(-,A)` is (or fails to be) a structure over the symmetric monoidal
category of Weil algebras. Dimension is its shadow.

### 2.5 Item (d) — the "point of interest" — risks near-vacuity

For fixed `m`, the condition `C(n,A)` constrains `phi_m` only on inputs of the
form `f_A` for `f: R^n -> R^n`. The set of such `g: R^m -> R^m` is an
enormously thin subclass of all right-hand sides (infinite codimension in any
reasonable sense). "Two lift structures have vector fields in common" then
means: the images of two lift maps intersect. Two prescriptions collide only
on that intersection.

I can see no single natural reading of "have vector fields in common". At
least these are on the table, and they are not the same set:

1. `g` lies in the image of both lift maps (as maps `R^m -> R^m`) for the two
   fixed identifications;
2. as in 1, but up to `GL_m(R)`-conjugacy of the two structures;
3. `g` is `A`-linear-compatible for both algebra structures on `R^m` — i.e.
   the two `R`-algebra actions on `R^m` share a common subalgebra through
   which `g` factors.

Under reading 1 with two *unrelated* factorizations the intersection can
collapse to something like the lifts of affine/constant fields — in which case
(d) is asking about forced agreement on a set so small that "forced to agree"
is true but empty of content. Under reading 3 it is a genuine question about
the lattice of Weil-algebra structures on `R^m`. I have **not** determined
which; that is Balthasar/Melchior territory and I am not doing it. I flag it as
the vacuity risk in (d) and as the item most likely to yield a technically
correct but not-worth-stating result.

[HEURISTIC] My expectation is that the real invariant governing (d) is not the
overlap of images but the poset of common quotients/subalgebras of the two
Weil algebras — i.e. again a statement in the Weil-algebra category, with the
`R^m` presentation an artifact. If so, (d) restated in that category would be
the version worth having. [/HEURISTIC]

### 2.6 Degenerate ends of the hypothesis space

- `N = 1`, i.e. `A = R`: `C(n,R)` is the tautology `phi_n(f) = phi_n(f)`. The
  poset's identity edges carry no information — fine, but it means the poset's
  reflexivity is decorative.
- `n = 1`: `C(1,A)` constrains `phi_N` on scalar-lifted fields only. Still
  non-vacuous.
- `A = R[e]/(e^2)`, `n` arbitrary: this is the whole of first-order variational
  transport and is the case that *matters* numerically. Any framing whose
  content evaporates here is not worth having; the proposed one does not
  evaporate here, which is a point in its favour.
- `Phi` unconstrained beyond "function of `(n,f)`": nothing forces `phi_n(f)`
  to be smooth, or even to be a map `R^n -> R^n` rather than an arbitrary
  gadget. But `T_A(phi_n(f))` — the natural right-hand side of `C` — requires
  `phi_n(f)` to be at least `C^∞` (or polynomial/analytic). So the axiom
  "nothing else" is in tension with the construction it is supposed to
  support. `[GAP]` — the regularity class of `phi_n(f)` is unstated and is
  load-bearing.
- Step size `h`: the axiom says `phi_n` receives "a component count and a
  right-hand side, and nothing else". Then `h` is either absorbed into `f`
  (rescaling) or absent. But adaptive step control — the place where jet
  transport genuinely *fails* to commute, because step selection uses norms
  and comparisons that are not `A`-algebra operations — is definitionally
  excluded by this axiom. The framing thus rules out the interesting
  obstruction before the analysis begins. I regard this as the second-most
  serious framing concern after 2.1/2.2.

---

## Subtask 3 — constructive status (done)

- No use of excluded middle on an undecidable-looking predicate is visible in
  the *setup*; `C(n,A)` for fixed `n, A, f` is an equation between explicitly
  computable objects (Weil algebras are finite-dimensional and finitely
  presented; `f_A` is computable from `f` by truncated arithmetic).
- The quantifier "for every Weil algebra `A`" ranges over an infinite family
  with moduli (for fixed `N ≥ 4`, isomorphism classes of Weil algebras of
  dimension `N` are not finite in general `[UNVERIFIED]`). Verifying the
  predicate is therefore not a finite check as stated. `[HEURISTIC]` It is
  plausibly reducible to the generating family `R[x_1..x_k]/m^{q+1}`, since
  every Weil algebra is a quotient of one of these `[UNVERIFIED]`, and the
  condition should descend along surjections — which would make the whole
  predicate a countable, effectively enumerable check. I have not verified the
  descent. `[/HEURISTIC]`
- No existence-by-contradiction and no choice is used anywhere in the stated
  material; the objects are all explicitly presented.
- I therefore rate the *statement* as plausibly constructive, but I cannot
  rate the argument, because the argument's central object `C` is undefined.
  **CONSTRUCTIVE-STATUS: unclear** — and per the protocol this is
  informational and does not affect my verdict.

---

## Definitional ambiguity, with divergence witness

**Convention at issue.** The content of `C(n,A)` — the "compatibility
condition relating `phi_n(f)` and `phi_{nN}(f_A)`". The skeleton names it and
never states it, and at least three standard readings are live.

**Readings.**

- **(i) Full lift-equivariance.** `phi_{nN}(f_A) = T_A(phi_n(f))` under the
  chosen identification `A^n ≅ R^{nN}`, i.e. the method's step map lifted to
  `A` *is* the method applied to the lifted field. (This is what jet transport
  actually delivers `[UNVERIFIED]`.)
- **(ii) Augmentation compatibility only.** `pi ∘ phi_{nN}(f_A) = phi_n(f) ∘ pi`
  where `pi: A -> R` is the augmentation (`A -> A/m_A ≅ R`), i.e. the lifted
  run's real part reproduces the base run, with no constraint on the nilpotent
  part.
- **(iii) Order-`p` agreement.** `phi_{nN}(f_A) = T_A(phi_n(f)) + O(h^{p+1})`,
  the reading a numerical analyst would default to when the method is only
  consistent to order `p`.

**Witness** (a case this round's item (d) and item (c) actually exercise).
Take `n = 1`, `A = R[e]/(e^2)` so `N = 2`, `m = 2`, basis `(1, e)`, and
`f(x) = x^2`. Then `f_A(y_1 + e y_2) = y_1^2 + 2 e y_1 y_2`, i.e. in
coordinates `g(y) = (y_1^2,\; 2 y_1 y_2)`.

Define `Phi` by: `phi_n = ` explicit Euler `x ↦ x + h f(x)` for every `n ≠ 2`,
and
```
phi_2(g)(y_1, y_2) = ( y_1 + h g_1(y),  y_2 + h g_2(y) + h^2 g_1(y)^2 ).
```
Then on this `f`:
- `T_A(phi_1(f))` has components `( y_1 + h y_1^2,\; y_2 + 2 h y_1 y_2 )`;
- `phi_2(f_A)` has components `( y_1 + h y_1^2,\; y_2 + 2 h y_1 y_2 + h^2 y_1^4 )`.

Hence for this `Phi`:
- reading **(i)** says `C(1, R[e]/(e^2))` **fails** (the `e`-components differ
  by `h^2 y_1^4 ≢ 0`);
- reading **(ii)** says `C(1, R[e]/(e^2))` **holds** (the real components
  agree identically);
- reading **(iii)** with `p = 1` (Euler's order) says `C(1, R[e]/(e^2))`
  **holds** (the discrepancy is `O(h^2)`).

One witness separates all three readings.

**Why it matters to this round, not just in principle.** The divergence
propagates straight into the deliverables. Under (ii), `Aut(A)` and the basis
choice are irrelevant because the augmentation `A -> R` is canonical, so (c)
is trivially "yes, well-defined"; under (i) the answer is "no, not without an
equivariance hypothesis" (§2.3). Under (ii), the tensor-product question (b)
degenerates because augmentations compose canonically; under (i) it is the
`T_A ∘ T_B = T_{A⊗B}` statement. And (d) — the declared point of interest —
is close to vacuous under (ii) (each prescription pins only a projection) and
substantive under (i). Under (iii) the two prescriptions in (d) can *both*
hold while disagreeing, so "forced to agree / forced to disagree" is not even
the right trichotomy.

I do not choose a reading. That is the user's alone.

---

## Verdict reasoning

`likely-misframed`, on three independent grounds, any one of which I would
have called at least `suspicious`:

1. The `iff` has no independent right-hand side — as posed this is a
   definition dressed as a characterization (§2.1). The thing a reader wants
   ("which methods support jet transport?") is not what is being asked.
2. The index structure is a lossy shadow of one that is already known and
   better behaved; item (b) is a solved statement in the category the proposal
   discards, and items (a),(b) are partly ill-posed in the poset (§2.4).
3. The axiom "component count and right-hand side, and nothing else" is
   simultaneously too weak (does not make `C` basis-independent, §2.3; does
   not fix the regularity of `phi_n(f)`, §2.6) and too strong (excludes step
   control, which is exactly where jet transport's commutation genuinely
   breaks, §2.6).

None of this says the underlying investigation is wrong-headed. The subject is
real and the (d) question, restated in the Weil-algebra category, looks to me
like the part worth keeping. But the *statement as posed* is the problem, not
the method — which is the `likely-misframed` row.

## Subtasks

- references check — **done** (directory absent)
- literature fit (jet transport / Weil functors) — **done**, all attributions
  `[UNVERIFIED]`
- circularity & right-hand-side audit — **done**
- index-category / poset critique, bearing on (a),(b) — **done**
- well-definedness & `Aut` vs `GL` mismatch, bearing on (c) — **done**
- vacuity audit of (d) and "vector fields in common" — **partial** (readings
  enumerated, thinness argued heuristically; I did not determine the actual
  intersection, and should not)
- degenerate ends — **done**
- constructive status — **partial** (descent along surjections of Weil
  algebras unverified)
- grounding the Weil-functor composition theorem in a primary source —
  **untouched** (no `references/`, declined to spend the slot on WebSearch)

## No extension petition

The qualitatively different subtask I would want (grounding the Weil-functor
literature) is blocked on a missing source, not on time; a second slot would be
"the same search, but longer". Not petitioning.

---

ACQUISITION: Kolář–Michor–Slovák, *Natural Operations in Differential
Geometry* (Weil functors, `T_A ∘ T_B = T_{A⊗B}`, product-preserving functors),
together with a primary jet-transport reference (Berz's differential algebra
or Jorba–Gimenez–Haro).
