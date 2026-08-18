# jet-transport — Round 0 scoping (Lilith, propose mode, pre-MAGI)

## 0. Framing

This is not a MAGI round — no claim has been formalized, no LOG.md exists.
The input is a raw brainstorm about how far the hypothesis "the method
respects jet transport" can be generalized before it becomes a
classification tool for numerical/geometric integration methods. My job
is purely to parse this into a structured search space and hand back
candidate statements narrow enough to become single future claims, plus
flag what is not yet well-posed. No mathematical judgment is exercised
below.

## 1. Parse into distinct axes

Reading the raw paragraph sentence by sentence, the following distinct
threads are present (labels match the ones supplied in the task):

- (a) How large a class of vector fields must jet transport hold over —
  explicit uncertainty voiced by the researcher ("not sure if it is
  possible to state it for all vector fields").
- (b) How large/general a class of Weil algebras the property must hold
  over — explicit rejection of "trivial Weil algebra only."
- (c) Whether extensions that are *not* Weil lifts can carry a
  jet-transport property at all ("if those make sense with jet transport
  too").
- (d) Extension with respect to parameters.
- (e) Extension with respect to time.
- (f) Extension with respect to initial value.
- (g) A distinct extension per coordinate of the original system
  (fibered/product structure rather than one global extension).
- (h) Nested extensions — composing two extension types (e.g. IV-then-time).
- (i) Iterated/repeated nesting — "nesting extensions on the initial
  value with extensions in time with extensions in parameters over and
  over."
- (j) Extensions whose Weil algebras share dimension but may fail to be
  isomorphic (or may be isomorphic via a nontrivial automorphism) — the
  observation that this seems to force an extra "respect the change"
  condition on the method, i.e. some equivariance/naturality hypothesis.

Two more implicit items run through the whole paragraph rather than being
separate bullets:

- (k) A meta-principle, not a standalone claim: whichever axis is chosen,
  push it to the *maximal* class for which the property can be stated
  ("this game must be played for all other parts of the puzzle"). This
  modifies every other item rather than being its own direction.
- (l) The overall thesis that "jet transport" is not one property but a
  *conjunction* over all of the above axes, so the hypothesis as usually
  stated (fixed test vector fields, fixed Weil algebra) is likely much
  weaker than what's available. This is the motivating observation for
  doing this scoping at all, not itself an actionable direction.

## 2. Merge / dependency structure

- (d), (e), (f) are three instances of one construction: "extend along a
  distinguished coordinate/parameter of the system rather than along the
  state variables themselves." They are logically independent of each
  other (each can be tested on its own) but structurally parallel, so
  they should be tried as separate narrow claims rather than merged into
  one — merging would violate "one claim per round" once any of them
  turns out to need its own hypotheses (e.g. time extension needs
  autonomy/non-autonomy handling that parameter extension doesn't).
- (g) is orthogonal to (d)-(f): it is a claim about the *shape* of the
  extension (product/fibered over coordinates) rather than about *what*
  is extended. It presupposes ordinary per-object Weil-lift jet
  transport is already meaningful, and is a genuine strengthening of (b).
- (h) presupposes that at least two of (d)-(f) are individually
  well-posed as jet-transport statements — you cannot compose an
  initial-value extension with a time extension in a test until each one
  independently has a defined meaning of "the method respects jet
  transport."
- (i) is (h) taken to an unbounded/iterated limit ("over and over").
  It further presupposes a definitional fact not established anywhere in
  the input: that composing two Weil-functor extensions again yields an
  extension of the same (Weil-lift) kind, so that "iterate forever" is
  even a well-typed operation. Until that composition closure is settled,
  (i) is not yet a testable statement — it is downstream of (h), and (h)
  is downstream of (d)-(f).
- (j) is a refinement of (b): it isn't about how large the class of Weil
  algebras is, but about a subtlety inside that class (dimension does
  not determine isomorphism type, and even isomorphic algebras carry a
  choice of isomorphism). It surfaces a *candidate new hypothesis*
  (equivariance/naturality of the method under Weil-algebra
  isomorphisms) rather than a generalization of scope.
- (c) is independent of (d)-(j): it asks whether the entire Weil-lift
  scaffolding can be dropped in favor of some other kind of "extension."
  This is the most structurally open item and the least well-posed,
  since "jet transport" as named presumably has a Weil-algebra-based
  definition already; asking whether it "makes sense" for non-Weil-lift
  extensions requires first deciding what plays the role of the Weil
  algebra there.
- (a) is a genuine open scoping question distinct from (b): it is about
  the source category (vector fields) rather than the target/extension
  category (Weil algebras). It can be turned into a direction on its own:
  test the maximal regularity/completeness class rather than assume "all
  vector fields" trivially works.

## 3. Digest — one line per surviving item

1. (a) Maximal vector-field class: replace "large enough class" with
   "the maximal class of vector fields for which jet transport can be
   stated at all," sharpening the hypothesis from an arbitrary
   large-but-unspecified class to a canonical extremal one.
2. (b) Maximal Weil-algebra class: replace "nontrivial Weil algebra" with
   an explicit description of which Weil algebras the property must hold
   for, ruling out both the trivial case and silent restriction to a
   convenient subclass (e.g. only jets of order ≤2).
3. (c) Non-Weil-lift extensions: if some non-Weil-lift construction can
   still carry a jet-transport-like property, the classification widens
   to methods distinguished by behavior on constructions Weil theory
   doesn't see — a genuinely different sharpening axis, not a variant of
   (b).
4. (d) Parameter extension: adds a test class (systems with parameters,
   Weil-lifted in the parameter direction) the method must also respect,
   which would rule out methods that are only parameter-symbol-agnostic
   by accident.
5. (e) Time extension: analogous test in the time direction; likely
   interacts with autonomous-vs-non-autonomous system hypotheses already
   implicit in "vector field," so sharpens by forcing that distinction
   into the open.
6. (f) Initial-value extension: analogous test along IV — this is the
   closest to classical variational-equation/flow-Jacobian jet
   prolongation, so is the most likely to already have literature
   precedent to check against.
7. (g) Per-coordinate distinct extensions: replaces a single global
   Weil algebra with a fibered choice, one per coordinate — strengthens
   by forcing the method to be compatible with mixed-order/mixed-type
   jet structure rather than a single uniform order.
8. (h) Nested (two-fold) extensions: composing e.g. IV-extension with
   time-extension tests whether jet transport is stable under
   composition, which would be a strictly stronger and more informative
   hypothesis than any single-axis version.
9. (i) Iterated/unbounded nesting: pushes (h) to arbitrary depth; only
   sharpens the classification if closure of the composition operation
   is first established (see prerequisites) — otherwise it's not yet a
   distinct hypothesis from (h).
10. (j) Same-dimension non-isomorphic (or isomorphic-but-not-canonically)
    Weil algebras: surfaces a candidate *added* hypothesis — some
    equivariance/naturality of the method under change of Weil-algebra
    presentation — which would sharpen the classification by excluding
    methods that are extension-compatible only for one choice of
    coordinates on the Weil algebra.

## 4. Selection for directions (statement-axis, round-0 candidates)

All surviving items are strengthenings of hypotheses on the same target
statement (jet transport as a classifying property), so every direction
below is AXIS: statement, and none can be "ROUTES AROUND" a prior
failure since there is no LOG.md history yet for this claim-id.

Chosen for the directions list (narrow enough to become one MAGI claim
each): (f) initial-value extension (most classically grounded entry
point), (a) maximal-vector-field-class reframing (applies globally and
is cheap to test first), (h) two-fold nested extension (the first
non-trivial composition case, deliberately not (i) which is blocked on a
prerequisite), (g) per-coordinate fibered extension, and (j) the
equivariance/naturality hypothesis suggested by non-canonical
isomorphism of same-dimension Weil algebras. (b) is folded into each
direction implicitly as "state it for the maximal class of Weil algebras
for which the construction makes sense," per the meta-principle (k),
rather than listed as its own separate direction, to avoid a 6th
near-duplicate entry. (d) and (e) are not separately listed to keep the
list at 5 non-duplicate items; they are structurally identical in shape
to (f) (extend-along-a-distinguished-variable) and are recorded here as
carried-forward siblings for a later round once (f) has been run once as
the template case.

## 5. Prerequisites / definitional gaps (not yet promotable to a claim)

- P1 (from (a)): what minimal regularity / completeness-of-flow is
  needed for "jet transport" to be *defined* for a vector field at all?
  Without this, "for all vector fields" is not yet a well-typed
  quantifier.
- P2 (from (c)): what would play the role of the Weil algebra for a
  non-Weil-lift "extension"? Until an extension-not-arising-from-a-Weil-
  algebra is defined precisely, asking whether jet transport "makes
  sense" for it is not a testable statement.
- P3 (from (h)/(i)): does composing two Weil-functor extensions yield
  another construction of the same (Weil-lift) kind — e.g. indexed by a
  tensor/fiber-product Weil algebra? Iterated nesting (i) is only a
  distinct, well-typed hypothesis once this closure question is settled;
  right now it collapses into "test (h) at every depth," which is not
  yet a single claim.
- P4 (from (j)): what does "respecting a change of isomorphism between
  same-dimension Weil algebras" formally mean for a numerical/geometric
  method — i.e. what is the action, and what is method-invariance under
  it? The raw input flags that this "seems to impose extra structure"
  but does not say what structure; this must be pinned down before (j)
  can be stated as a testable hypothesis rather than a hunch.
