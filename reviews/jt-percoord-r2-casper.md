# Casper Review — jt-percoord, Round 2

## Subtask 1: Known pattern? (done)

The setup — per-coordinate Weil algebra lifts, cross terms in W_i⊗W_j needing
a routing/gluing map back into W_i — sits inside the general theory of Weil
functors / natural bundles (Kolář–Michor–Slovák-style natural operators on
jets), where naturality under automorphisms of the base structure is a
standard and well-motivated selection principle. I am not aware of a named
theorem covering exactly this "two coordinates, two named candidate gluing
maps, swap-equivariance" test; flagged as **plausibly related to naturality
conditions in Weil-functor/jet theory, unverified** — no citation invented.

The specific move — "renaming the nilpotent symbols should not change the
answer, just as renaming ODE variables does not" — is a legitimate and
independently-motivated symmetry principle (it is essentially: the
construction should be natural with respect to isomorphisms of the index
set {1,2}), not an artifact manufactured to make a technique apply.

## Subtask 2: Strategy failure mode (done)

The technique implicit in the question is a symmetry/naturality check: does
an S_2-action (simultaneous relabeling of coordinates and their nilpotent
symbols) commute with each candidate map. The known failure mode for this
class of argument is that the chosen symmetry group can be *too coarse* to
discriminate — i.e. every map in the ambient class of "reasonable" candidates
already commutes with it, making the criterion true-but-uninformative for
exactly the pair under dispute.

That is my central structural concern here. Both named candidates are
defined without ever privileging index 1 over index 2:
- (a) "keep same-index nilpotent terms" refers only to the *relation*
  same-index vs different-index, which is itself swap-symmetric by
  construction — it never says "index 1" specifically.
- (b) "keep terms up to total degree, not discriminating by index" is, by
  its own stated definition, blind to which factor a nilpotent degree came
  from.

Neither definition contains an asymmetric ingredient (e.g. an ordering
x_1 < x_2, or a preferred embedding of one W_j into the other) that the
swap could expose as broken. So there is a real possibility that this
specific equivariance requirement is satisfied by *both* candidates for
structural reasons visible directly from their definitions, independent of
any computation — i.e., the test may be foreseeably vacuous for exactly
this pair, even though it is a perfectly good constraint on the larger
(unnamed) space of all possible gluing maps.

This is not fatal — the question explicitly anticipates and accepts this as
one of its three possible outcomes ("if it rules out neither, is the
requirement vacuous for this pair") — but it is the outside-view risk worth
flagging: the round may return a true, checkable statement whose
information content relative to the paper's actual open dispute (how cross
terms should route — an *index-fidelity* question) is close to zero, because
permutation symmetry between 1 and 2 is orthogonal to that dispute. The
disagreement between (a) and (b) is about how much cross-coupling
information survives, not about which coordinate is called "1"; a symmetry
axiom that only forbids coordinate-favoritism does not obviously bear on
that axis at all.

## Subtask 3: Hypothesis strength vs. conclusion (done)

No silent strengthening detected. The restriction to equal-order dual
numbers and exactly the two previously-identified candidates is declared
up front, matches the "one claim per round" discipline, and is consistent
with the stated motivation (a felt disanalogy between vector fields, which
are manifestly renaming-invariant, and the lifting machinery, which might
not be). The three-way branch structure of the question (rules out neither
/ one / both) is honestly built in rather than assuming the interesting
branch. This is good practice, not hypothesis-shopping.

## Subtask 4: Degenerate ends (done)

At order 0 (W_i = R, no nilpotents) the whole gluing question disappears —
consistent, not silently vacuous, and outside the stated hypothesis (order
is fixed at 1) so not in scope here. No hidden degeneracy inside the
declared hypothesis range.

## Subtask 5: Constructive status (done)

The requested check is a finite, explicit verification: does a given
linear map on a finite-dimensional algebra commute with an explicit
finite-group action. No compactness, no choice, no excluded middle on an
undecidable predicate. Fully constructive; would survive intuitionistically
without modification.

## Overall framing assessment

This is a legitimate, well-scoped, self-aware narrow test — not a wrong
question. My one substantive concern, stated as a risk rather than a
verdict-driver: the specific symmetry chosen (index relabeling) looks, from
the definitions alone, likely to be satisfied by *both* named candidates,
because neither candidate's definition encodes any index-preference for the
requirement to catch. If that is what the round finds, it is valid evidence
(symmetry is not the axis that adjudicates (a) vs (b)), but the researcher
should not be surprised if this particular round's yield is "vacuous for
this pair" and should treat that as motivation to look for the actual
discriminating principle (something bearing on how much cross-index data is
preserved), which lies on a different axis than coordinate-relabeling
symmetry.
