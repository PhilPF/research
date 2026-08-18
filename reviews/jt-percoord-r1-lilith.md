# Lilith — Mode 1 (propose) — jt-percoord Round 1 → Round 2 directions

## 1. Log review

Two entries precede this call:

- **Round 0 (jet-transport, scoping)**: Lilith (not MAGI) parsed an
  unstructured researcher brainstorm into eleven distinct axes (a)–(l),
  merged/deduped them, flagged four unresolved prerequisites (P1–P4), and
  selected five round-0 candidate directions for the user to choose among:
  (f) initial-value extension, (a) maximal-vector-field-class reframing,
  (h) two-fold nested extension, (g) per-coordinate fibered extension, (j)
  equivariance under non-canonical Weil-algebra isomorphism. The user chose
  (g).
- **Round 1 (jt-percoord)**: MAGI tested (g) as posed — "each coordinate
  Weil-lifted independently rather than sharing one global Weil algebra."
  Outcome: `gap-located` (Melchior) **and** `misframed` (Balthasar
  vacuous-or-trivial, Casper likely-misframed) simultaneously — both §5
  table rows independently triggered, the strongest joint signal available
  short of `LOCALIZED-GAP` proper (which requires *no*-gap-found; here
  Melchior did find a gap, so it's not that exact row, but the effect is
  the same: multiple independent lines converge on one obstruction).

## 2. Classifying the Round 1 failure: structural, not technical

The three reports triangulate on a single obstruction, examined from three
angles:

- **Melchior**: under any coupling ($\partial f_i/\partial x_j \neq 0$,
  $i\neq j$), the lifted vector field's $i$-th component acquires terms
  built from $n_j \in N_j$, $j \neq i$ (worked concretely with mixed-order
  algebras $W_1=\mathbb R[e_1]/(e_1^2)$, $W_2=\mathbb R[e_2]/(e_2^3)$ on
  $F=(xy,x^2)$). These live in $W_i\otimes W_j$, not $W_i$, and "per-
  coordinate independent Weil lift" supplies no map to route them home.
  Two natural projection choices give inequivalent dynamics.
- **Balthasar**: enumerated the only two literal readings. (R1) no shared
  structure — undefined as soon as any off-diagonal Jacobian entry is
  nonzero (harmonic oscillator suffices to break it). (R2) shared ambient
  algebra $\Lambda$ — consistency of the ODE forces every coordinate's
  lift to range over all of $\Lambda$, i.e. collapses back to exactly the
  pre-existing single global Weil algebra construction the statement was
  meant to move past, and even then the choice of $\Lambda$ among same-
  dimension alternatives is non-canonical (§5c, tied to Round-0 item (j)).
  Only the fully diagonal case is well-typed, and there it is zero new
  content (n disconnected copies of the 1-D theory).
- **Casper**: independently flagged that per-coordinate splitting breaks
  the coordinate-freedom / naturality that appears to be load-bearing for
  what "jet transport" and "a large class of vector fields" are supposed
  to mean in the surrounding program, and that (g) was picked from an
  uncommitted menu without argued priority over siblings (f), (h), which
  Round 0 itself flagged as more classically grounded / logically prior.

This is **structural**, not a missing lemma: the construction cannot be
made well-typed for coupled systems by refining the same idea (independent
per-coordinate algebras). Every attempt to patch it (supplying *some*
gluing/compatibility map) was already tried inside Round 1 itself under
reading (R2) and shown to degenerate into the base case it was meant to
generalize past. Per the standing procedure, directions below therefore do
**not** propose a third patched reading of "independent per-coordinate
Weil algebra" — they change what is quantified over, what question is
asked, or which existing construction is imported.

## 3. Direction sketches

**A — restrict to flow-invariant fibered systems (statement, scope-narrowing).**
Instead of splitting an arbitrary coupled system into a Weil algebra per
coordinate, restrict the class of vector fields to those that already
carry a genuine skew-product / triangular / fibered structure preserved by
the flow itself (e.g. $\partial f_i/\partial x_j = 0$ for $j$ outside a
fixed partial order, or a genuine fiber bundle $p:Y\to M$ with $F$
$p$-projectable). On this restricted class the cross-coordinate terms
Melchior located have a canonical, order-respecting home (lower coordinates
never need to hear from higher ones), so the construction is well-typed
without inventing an arbitrary gluing map, and it does not collapse to the
global case the way the fully diagonal case does, because genuine (one-
directional) coupling survives. `[HEURISTIC]` this dodges Balthasar's
dichotomy because it is a genuine third class (properly coupled but not
symmetric), distinct from both the diagonal case (§4, no content) and the
symmetric coupled case (§5, undefined/collapses).

**B — pivot to Round-0 item (j): naturality under Weil-algebra presentation change (statement, different axis).**
Drop per-coordinate splitting entirely. Ask instead whether jet transport
of a method is invariant under replacing one Weil algebra by a
non-canonically-isomorphic same-dimension one — the exact non-canonicity
Balthasar found concretely in §5c (the choice between $\Lambda$ =
exterior algebra vs. $\Lambda'$ = all-cross-terms-zero, same dimension,
inequivalent dynamics) and that Round 0 flagged as prerequisite P4. This
targets the located obstruction directly, as a question about the
*target category* of Weil algebras rather than about splitting the domain.
`[HEURISTIC]` reframes the exact non-canonicity Balthasar exhibited as the
subject of the claim instead of as a side-defect of a different claim.

**C — import the literature's two-Weil-algebra fibered bundle functor (technique, transport of known construction).**
Melchior flagged as untouched the Kolář–Michor–Slovák-style $T^{A,B}$
construction for a fibered manifold $p:Y\to M$: a *base* Weil algebra $A$
and a *fiber* Weil algebra $B$ with an explicit compatibility built into
the bundle functor definition, rather than $n$ independent per-coordinate
algebras with no relation. Test jet transport against this literature
object as the formalization of "fibered extension" instead of inventing a
per-coordinate ad hoc splitting. `[HEURISTIC]` this is a real, published
answer to "how does one legitimately have more than one Weil algebra
acting on related coordinates," and it is structurally different from R1/
R2 because it requires only a base/fiber split (two algebras with one
compatibility datum), not pairwise compatibility among all $n$ coordinate
algebras. Unconfirmed whether this exact construction has been checked for
a jet-transport-style method property; flagged as a lead, not a citation
of a settled result.

**D — abandon per-coordinate for the sibling axis (f), initial-value extension (statement, different axis, addresses Casper's arbitrary-selection critique).**
Round 0 itself flagged (f) as "the most classically grounded entry point
... closest to classical variational-equation/flow-Jacobian jet
prolongation," and set it aside only because the user chose (g) instead.
Casper's Round 1 report independently argues (g) was selected from an
uncommitted menu with no priority argument, and may in any case be a
subcase subsumed by other axes. (f) uses a *single* Weil algebra (no
per-coordinate splitting, no cross-term typing problem at all) applied
along the initial-value direction, so it does not inherit the Round 1
obstruction — it was never exposed to it. `[HEURISTIC]` sidesteps the
whole multi-algebra compatibility problem by only ever using one algebra,
trading the coordinate-splitting question for a different, likely more
tractable one with closer literature precedent (Berz–Makino-style DA /
variational equations, per Casper's search).

## 4. Duplication check

None of A–D repeat Round 1's tested readings (R1)/(R2), and none propose a
"third gluing map" for the same per-coordinate idea. A and C both touch
"more than one Weil algebra" territory but differ in kind: A keeps a single
algebra per coordinate but restricts *which vector fields* are admitted
(statement/scope axis); C keeps the vector-field class general but
replaces the *construction* wholesale with a base/fiber pair from the
literature (technique axis). B and D both leave "per-coordinate" behind
entirely in favor of a different Round-0 axis; they are not duplicates of
each other since B targets the Weil-algebra side (target category) and D
targets the extension-direction side (source data: initial value vs.
coordinate splitting).
