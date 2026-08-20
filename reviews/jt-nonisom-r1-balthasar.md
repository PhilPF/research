# Balthasar Round 1 — claim jt-nonisom

## Subtask plan (priority order)
1. Verify f, g, g' are well-defined algebra homomorphisms as claimed. [done]
2. Characterize Hom(A,A') and Hom(A',A) fully — check whether f, g are
   really "the" canonical choices or one point in a larger family
   (definitional-ambiguity probe). [done]
3. Build a concrete test-method family (ring-arithmetic-realized Euler
   step for a nonlinear vector field) and check whether naturality w.r.t.
   f, g, g' is automatic, vacuous, or a real constraint. [done]
4. Search for a "bespoke" (non-universal-formula) method that breaks
   naturality, to calibrate exactly what class of methods the
   (a)/(b)/(c) question is really about. [done]
5. Check g vs g' for an actual divergence witness (the researcher's
   explicit ask). [done]

All five completed within budget; see raw computation log below.

## 1. Well-definedness (verified numerically, 200 random rational trials
   each, exact `Fraction` arithmetic, script in scratchpad)

Representing A = R[e]/(e^3) as triples (a0,a1,a2) ↔ a0+a1 e+a2 e^2 and
A' = R[e1,e2]/(e1,e2)^2 as (b0,b1,b2) ↔ b0+b1 e1+b2 e2, with
multiplication tables enforcing e^3=0 and e1^2=e2^2=e1e2=0 respectively:

- f(a0,a1,a2) = (a0,a1,0) is an algebra homomorphism A→A' (confirmed).
  Kernel = span{e^2} (dim 1), image = span{1,e1} (dim 2): neither
  injective nor surjective, as claimed.
- g(b0,b1,b2) = (b0,0,b1) is an algebra homomorphism A'→A (confirmed).
  Kernel = span{e2}, image = span{1,e^2}: neither injective nor
  surjective.
- g'(b0,b1,b2) = (b0,0,b2) (the flagged "equally valid alternative") is
  also a bona fide algebra homomorphism (confirmed).

So the hypotheses are jointly satisfiable — no vacuity from
ill-posedness at this level.

## 2. The "canonical vs non-canonical" framing is asymmetric and understated

The statement flags g as non-canonical (one discrete alternative, the
e1↔e2 swap) but presents f as if it were essentially forced. Direct
computation shows both Hom-spaces are much richer than either discrete
alternative suggests:

- **Hom(A,A')**: since m' = (e1,e2) satisfies m'^2 = 0 exactly, *every*
  element b ∈ m' trivially satisfies b^3 = 0, so f(e) may be **any**
  element of the 2-dimensional space m' = span{e1,e2} (checked directly
  from the multiplication table: any (0,β1,β2) squares to 0, hence cubes
  to 0). f(e)=e1 is one point on a continuum, not "the" canonical map.
- **Hom(A',A)**: solving b^2=0 in A forces b ∈ span{e^2} exactly (the
  linear coefficient must vanish: (b0,b1,b2)^2=(b0^2,2b0b1,2b0b2+b1^2),
  requiring b0=b1=0). So g(e1), g(e2) are each independently *any*
  multiple of e^2, and the product condition g(e1)g(e2)=α2β2·e^4=0 holds
  automatically. Hom(A',A) is a 2-dimensional vector space (α2,β2)∈R^2 —
  again a continuum, not a 2-element ambiguity.

So the "non-canonical, one alternative" framing for g understates the
true ambiguity, and the same ambiguity (in equal measure) afflicts f,
which the statement implicitly treats as unproblematic. [Not fully
brute-force verified but straightforward:] Aut(A') acts as the *full*
GL_2(R) on m' (since m'^2=0, multiplication imposes no constraint on
linear automorphisms of the 2-dim space {e1,e2}), and this action is
transitive on m'\{0}; combined with Aut(A) (which scales the e^2-coefficient
by c^2>0 for units c, but GL_2(R) alone already supplies transitivity on
R^2\{0} including sign flips), Hom(A,A')\{0} and Hom(A',A)\{0} are each a
**single orbit** under pre/post-composition by automorphisms — cleanly
separated from the zero map (the augmentation-then-unit map flagged in
option (c)), which is its own fixed orbit. This refines option (c): the
trivial map is a genuinely distinguished degenerate orbit, but it is not
alone — there is exactly one other (generic) orbit in each Hom-space, and
f, g, g' are simply three representatives of it.

## 3. Does naturality under f, g actually constrain a test method family?

Modeled "jet transport method" in its most natural/likely sense:
apply a fixed real-coefficient formula (built only from +, ×, scalar
multiplication by h) to the jet data using the *target Weil algebra's own
ring arithmetic* — i.e., literally run the numerical scheme's formula
with A-valued (resp. A'-valued) arithmetic. This is the standard way a
Weil functor T_A transports a map. Concretely tested explicit-Euler for
the (nonlinear!) vector field X(x)=x², i.e. a_{n+1} = a_n + h·a_n² carried
out entirely inside A, and separately inside A':

- Checked (200 random rational trials, exact arithmetic):
  `f(Euler_A(a)) == Euler_A'(f(a))` — **holds identically, always**.
  `g(Euler_A'(b)) == Euler_A(g(b))` — **holds identically, always**.
  `g'(Euler_A'(b)) == Euler_A(g'(b))` — **holds identically, always**.

This is not a coincidence of this particular X or step: it is a general
algebraic fact — any ring homomorphism h:A→B automatically commutes with
evaluation of a *fixed* polynomial/power-series formula (h(P(a)) =
P(h(a)) for any ring hom h, by definition of ring homomorphism), for
**every** algebra homomorphism, invertible or not, same-dimension or not.
So for the entire class of "ring-arithmetic-realized" methods (Euler,
midpoint/Heun-type RK2, any explicit Runge–Kutta scheme expressed via
+,×,scalar-mult of the vector field), naturality under f and g is an
automatic tautology and **adds no discriminating power whatsoever** — it
cannot rule out any method in this class, nor can it distinguish g from
g' (see §5). This directly falsifies reading (a) ("genuinely new,
non-vacuous constraint") for this natural method class, and pushes past
reading (b) ("already implied by existing hypotheses") into outright
triviality: the fact needs no jet-transport-specific machinery at all,
only that h is a ring homomorphism.

## 4. Locating where a real constraint *would* bite

To check the vacuity isn't an artifact of an impoverished method class, I
constructed a deliberately "bespoke," non-universal-formula method for
T_A' M: same Euler step for the (y0,y1) part, but with an unmotivated
extra coupling term added to the y2-update:
`y2_new = y2 + h·(2 y0 y2) + eps·h·y1` (a term with no counterpart forced
by any single formula shared with the A-side method).

Result (found on first random trial, eps=-4, h=5/4): this construction
**breaks** `f(Euler_A(a)) == bogus_A'(f(a))` — a genuine violation.

This pins the exact locator: naturality under f (and, symmetrically,
under g) is vacuous *precisely* for methods that arise as one universal
polynomial/power-series formula evaluated via each Weil algebra's own
arithmetic; it becomes a real, checkable, bite-having constraint (reading
(a)) the moment "method" is allowed to be an independently-specified,
per-Weil-algebra construction not reducible to that common formula (e.g.
algebra-structure-aware iteration counts, ad hoc coupling terms, or
different stage points chosen depending on the algebra's nilpotency
degree). The statement as posed does not fix which of these two method
classes is meant — that missing definition is exactly what would resolve
(a) vs (b) vs (c).

## 5. Divergence witness g vs g' (explicit ask)

Tested directly: for the ring-arithmetic-realized Euler method, g and g'
give **no divergence** — both satisfy naturality identically and always
(by the same general ring-homomorphism fact, which doesn't care which
representative of the orbit is used). So, contrary to what one might
expect from "g is non-canonical," the two choices are *not*
distinguishable by this naturality requirement for the natural method
class; the ambiguity in choosing g vs g' is real (§2) but inert for the
specific question posed. No divergence witness found despite an
explicit search with a genuinely nonlinear vector field.

## Assessment against (a)/(b)/(c)

- For the most natural reading of "jet transport method" (single
  universal formula, applied via each Weil algebra's arithmetic):
  **vacuous** — reading (c)-adjacent, stronger than (b): the constraint
  is a tautology of ring homomorphisms, not special to Weil algebras,
  jets, or the specific maps f/g, and it does not distinguish g from g'.
- For a broader, unstated class of "bespoke per-algebra" methods: the
  constraint is real and can fail (§4) — reading (a) becomes live, but
  only once that broader class is what's meant.
- The statement does not fix which class is intended; this is the
  missing hypothesis. Additionally, the framing of f as canonical vs g
  as merely "one alternative among two" understates a genuine
  2-dimensional continuum of choices in *both* Hom(A,A') and Hom(A',A)
  (§2), though all nonzero choices in each direction are demonstrably
  equivalent up to automorphism, so this particular imprecision does not
  by itself change the (a)/(b)/(c) verdict.

## Scope of search
- Exact rational arithmetic, 200 random trials per identity check
  (Euler/f, Euler/g, Euler/g', hom-checks) — effectively exhaustive for
  these polynomial identities since a polynomial identity failing would
  fail on a positive-measure set of rational inputs and 200 independent
  trials did not find one.
- One explicit nonlinear vector field family tested (X(x)=x²); did not
  sweep other nonlinearities (e.g. X(x)=x³, X(x)=1/x via truncated
  series) or multi-stage RK2/Heun explicitly (argued generally via the
  ring-homomorphism fact but not separately numerically instantiated).
- One "bespoke" counter-construction found on first attempt; did not
  explore the boundary of how minimal a deviation from "universal
  formula" suffices to break naturality.
- Automorphism-orbit transitivity argued by hand (dimension count and
  group actions), not brute-force verified computationally.

## Files
- scratchpad script: check2.py (see session scratchpad dir) — exact
  rational-arithmetic verification of all claims above.
