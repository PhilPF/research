# jt-nonisom — Round 1 — Lilith (propose, capped at 1) — full reasoning

## 0. Task framing

This is a targeted formalization task, not an open propose round: the
researcher has already chosen to revisit Round 0 Direction 5, but wants
the *complementary* half of it — same-dimension Weil algebras that are
**not** isomorphic, rather than the original text's "respect isomorphisms
between algebras that are isomorphic." Output is exactly one direction,
precise and self-contained enough to hand straight to MAGI as
`jt-nonisom` Round 1, no further Lilith menu step.

## 1. What Round 0 / Direction 5 actually said, and what's missing from it

Round 0 Direction 5 (Lilith's digest item (j)) reads: "Add an
equivariance hypothesis: require the method to respect isomorphisms
between Weil algebras of equal dimension... and test whether this is
already implied or is a genuinely new constraint." The raw user
fragment behind it: "What about extensions which have Weil algebras of
the same dimension? They may be isomorphic, so the method may need to
respect some change, that seems to impose extra structure."

Both the digest and the raw fragment only ever discuss the case where
the two algebras of equal dimension turn out to be isomorphic (possibly
non-canonically). Neither says anything about what happens when two
same-dimension Weil algebras are simply **not isomorphic at all** — is
there still something a "jet-transport-respecting" method must satisfy
relating the two lifts, or does non-isomorphism just mean the two lifts
are unrelated and the hypothesis is silent? That is exactly the
researcher's new steer, and it is a genuinely distinct question from
Direction 5's original text, not a cosmetic variant — Direction 5 assumed
an isomorphism to respect; here there is provably no isomorphism to
respect, so if a constraint exists at all it must come from a different
kind of structure than "respect a change of coordinates."

## 2. Relevant finding already on record (jt-percoord line)

jt-percoord Round 1 Balthasar (`reviews/jt-percoord-r1-balthasar.md`,
item 5b–5c, flagged partial/untouched) already ran into the *isomorphic*
side of this in passing: gluing two per-coordinate Weil algebras into an
ambient algebra is not forced — multiple non-isomorphic ambient choices
(the dimension-4 exterior algebra vs. the dimension-3 "all cross terms
zero" algebra) give different transported dynamics for the same input,
and no canonical choice among them is specified by the claim as posed.
That is a same-dimension-*isomorphism-choice* problem (§5c), not the
non-isomorphic-pair problem the researcher now wants — it is the
Direction-5-proper case, already showing the "respect some change"
worry is real. It does not resolve or preempt the non-isomorphic
question; nothing in the percoord line touches whether two *non*-
isomorphic same-dimension algebras impose any relation at all. Noted as
background confirmation that the isomorphic side of this fork is a real
obstruction, which makes the complementary non-isomorphic side worth
formalizing on its own rather than assuming it trivially reduces to
"nothing is required."

## 3. Choosing the minimal anchor pair

Need two Weil algebras, same dimension, provably non-isomorphic, small
enough for MAGI to compute with directly rather than reason about
abstractly. The standard smallest example of two non-isomorphic local
Weil algebras of equal dimension over R:

- A = R[e]/(e^3), dimension 3, basis {1, e, e^2}. Nilpotency index 3
  (e^2 != 0, e^3 = 0). This is the algebra of 2-jets in one variable.
- A' = R[e1,e2]/(e1,e2)^2, dimension 3, basis {1, e1, e2}. Nilpotency
  index 2 (every product of two elements of the maximal ideal is 0).
  This is the algebra of 1-jets in two variables.

These are not isomorphic: an algebra isomorphism must send the maximal
ideal m to m' and preserve the nilpotency filtration; m/m^2 has
dimension 1 in A but dimension 2 in A', an isomorphism invariant, so no
isomorphism can exist. Both are bona fide (unital, local, finite-
dimensional, augmented) Weil algebras of the same dimension.

`[HEURISTIC]` checked by hand, not run through a CAS: the dimension-of-
m/m^2 invariant argument is standard commutative algebra and should be
uncontroversial, but I have not independently verified it beyond this
one computation.

## 4. What comparability structure actually survives non-isomorphism

The naive answer to the researcher's question ("does non-isomorphism
just mean nothing is required?") is worth stress-testing before handing
it to MAGI as a foregone conclusion, because there is a concrete
candidate structure that survives even without an isomorphism: algebra
homomorphisms that are neither injective nor surjective.

- f: A -> A', f(e) = e1, extended by f(e^2) = e1^2 = 0. This is a valid
  R-algebra homomorphism (need f(e)^3 = 0 in A', true since e1^2 = 0
  already forces e1^3 = 0) but it is not injective (e^2 is killed) and
  not surjective (e2 is not hit).
- g: A' -> A, g(e1) = e^2, g(e2) = 0. Valid (g(e1)^2 = e^4 = 0 in A,
  g(e1)g(e2) = 0, g(e2)^2 = 0), also neither injective nor surjective.
  Note g is not unique: g(e1) = 0, g(e2) = e^2 is an equally valid,
  inequivalent choice, and there is no canonical way to prefer one over
  the other — unlike an isomorphism (if one existed), a non-invertible
  homomorphism between this pair comes in a non-canonical family.
- A degenerate homomorphism exists between *any* two local Weil
  algebras regardless of dimension or isomorphism type: the augmentation
  A -> R (kill the maximal ideal) followed by the unit R -> A' (embed
  scalars). This map is always present and always collapses the lift to
  the base point — it carries zero information about the nilpotent
  directions.

Any algebra homomorphism phi: A -> A' induces a natural transformation
T_phi: T_A => T_A' between the associated Weil functors (this is
functoriality of the Weil functor construction in the algebra variable,
independent of whether phi is invertible). So "respect a change" need
not stop at isomorphisms — the natural generalization is "respect every
algebra homomorphism between same-dimension Weil algebras," of which
isomorphism-equivariance (Direction 5 proper) is the special invertible
case, and the researcher's non-isomorphic case is the generic
non-invertible case. The trivial through-R homomorphism is the
degenerate member of that family and is a standing vacuity risk: if
"respect every homomorphism" is satisfiable only via that degenerate
map, the generalized hypothesis could be vacuous exactly where it is
meant to be informative — precisely the kind of concern Balthasar exists
to hunt for, and precisely why this must be posed as a single concrete
testable claim rather than left as "surely nothing is required."

## 5. Why this is one statement, not a menu

The researcher's question ("is there a meaningful compatibility
requirement at all, or does non-isomorphism mean unrelated") is not yet
answered either way in the log, and both answers are live: full
disconnection (nothing required beyond the trivial augmentation map) and
partial connection (the non-invertible homomorphisms above force some
compatibility) are both consistent with everything on record. Posing
"test whether homomorphism-naturality is genuinely constraining or
degenerates to the trivial map" as the single Round-1 claim, anchored on
the (A, A') pair above, gives MAGI one well-typed proposition instead of
an open-ended sweep over all non-isomorphic pairs. AXIS is statement,
not technique, since it proposes a hypothesis (generalized naturality
under algebra homomorphisms, not just isomorphisms) rather than a new
proof method for the existing statement — consistent with the operating
rule to prioritize statement-axis work given jet-transport's own
Round-0/Round-1 history already produced a `gap-located + misframed`
verdict on the sibling per-coordinate claim.

## 6. Duplication check

Not a duplicate of Round 0 Direction 5 (isomorphism case) or of any
jt-percoord round: percoord's line concerns fibered/per-coordinate
extension shape and stalled on gluing-map non-canonicity among
*isomorphic* ambient choices; this claim is about whether any relation
at all is forced between *non*-isomorphic same-dimension algebras, via
non-invertible homomorphisms rather than gluing maps. No prior round has
tested this.
