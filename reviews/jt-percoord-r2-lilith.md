# Lilith — Mode 1 (propose) — jt-percoord Round 2 (closed) → Round 3 directions

## 1. Log review (recap, no re-litigation)

- Round 0: scoping; user chose per-coordinate fibered extension (axis g).
- Round 1: MAGI tested (g) as posed. `gap-located` + `misframed`
  simultaneously. Structural finding: cross terms from coupling land in
  $W_i\otimes W_j$, no canonical map $\rho:W_i\otimes W_j\to W_i$ is
  supplied by "independent per-coordinate Weil algebra"; two natural
  candidates ((a) index-blind projection, (b) degree truncation) give
  inequivalent dynamics and the statement adjudicates neither.
- Round 1→2 propose: four directions (A restrict vector-field class to
  triangular/fibered systems; B naturality under non-canonical same-
  dimension Weil-algebra isomorphism; C import KMS-style $T^{A,B}$
  base/fiber bundle functor; D abandon per-coordinate for the initial-
  value axis). All four left unchosen — the user instead supplied a new
  input (renaming/relabeling invariance).
- User's renaming-invariance idea folded in; capped r2-propose returned
  Direction 1 (add relabeling/swap equivariance as a hypothesis, test
  (a)/(b) against it) and Direction 2 (construct the routing map by
  symmetrization/descent under the relabeling group instead of testing).
  User chose Direction 1 → became Round 2's tested claim.
- **Round 2 (closed), just returned**: `gap-located` (Melchior) +
  `misframed` (Balthasar `vacuous-or-trivial`, Casper informational
  concurrence) simultaneously — the same joint pattern as Round 1, one
  level down in the direction tree.
  - **Melchior**: candidate (b) is not a single map — "keep terms up to
    total degree, not discriminating by index" pins down *which* graded
    piece survives but not *where it lands* inside the 2-dimensional
    $W_i$; a free routing constant $c$ is needed, giving a family
    $\{\Phi^{(b,c)}\}_{c\in\mathbb R}$. At $c=0$, (b) collapses to (a).
    Verified numerically that equivariance holds for *every* $c$ — the
    requested test has zero power to select among family members.
  - **Balthasar**: exact symbolic/exact-integer check on a generic
    asymmetric coupled pair confirms both (a) and every faithful
    formalization of (b) satisfy swap-equivariance identically, and
    argues this is forced structurally: any routing rule built only from
    "own index vs. other index" (never a hard-coded "1" vs "2") is
    automatically covariant under simultaneous relabeling — the
    requirement can only ever exclude an index-privileging map, and none
    was offered. Also surfaces, as an aside while formalizing (b), a
    **different** probe that *does* separate (a) from (b): independence
    of per-coordinate nilpotent parameters $t_1,t_2$ (equivalently, the
    "silent coordinate" restriction $t_2=0$). (a)'s rule never mixes
    $t_1,t_2$; (b)'s construction (identifying $e_1=e_2=e$ in the equal-
    order case) bakes in $t_1=t_2$ and cannot natively express "perturb
    $x_1$ only."
  - **Casper**: independently predicts, from the definitions alone
    (before computation), that a coarse relabeling symmetry is the wrong
    tool here — neither candidate's definition contains an
    index-privileging ingredient for such a test to catch — and names the
    actual axis of disagreement between (a) and (b): **how much
    cross-index data survives**, which is orthogonal to *which coordinate
    is called "1."*

## 2. Classifying the Round 2 failure: structural (wrong axis), with one nested technical gap

Two separate things are being reported and they must not be conflated:

- **Structural** (the dominant finding, echoed by both Balthasar and
  Casper independently): the *type* of naturality condition chosen —
  invariance under the finite relabeling/permutation group $S_2$ acting
  on the coordinate index set — cannot in principle discriminate (a) from
  (b), because both candidates' defining rules are already expressed
  purely in terms of "own index vs. other index," which is tautologically
  $S_2$-covariant. No sharper formalization of *this same* group action
  patches it; the obstruction is which symmetry group was chosen, not how
  precisely it was applied. This directly generalizes Round 1's
  structural pattern (a plausible-sounding compatibility axiom that turns
  out to add no content once formalized) and, per the standing procedure,
  rules out re-proposing "swap equivariance, refined" as a direction.
- **Technical, nested inside the same round** (Melchior): independent of
  the symmetry question, candidate (b) itself is underspecified — a free
  parameter $c$ — and this could in principle be patched by *some*
  auxiliary criterion, just not by the one tested this round.
- The good news buried in the round: Balthasar located a *genuinely
  discriminating* nearby axis (independence of per-coordinate nilpotent
  parameters / silent-coordinate compatibility) essentially for free while
  formalizing (b). This is exactly the kind of untouched/partial probe
  the standing procedure says may be a cheaper next step than a fresh
  direction, and it is statement-axis (it proposes a different hypothesis
  to add, not a different proof technique for the same hypothesis).

## 3. Direction sketches

**1 — Replace the axiom: promote Balthasar's independence-of-nilpotent-parameters / silent-coordinate condition to the tested hypothesis, and use it to also pin down Melchior's free constant $c$ (statement axis).**
Formalize precisely: require the per-coordinate lift, viewed as a function
of independent scalar weights $(t_1,\dots,t_n)$ (via $X_i=x_i+t_ie_i$), to
be compatible with setting any subset of the $t_j$ to zero (equivalently,
restrict to the sub-case where only some coordinates are perturbed at
all). Test candidate (a) and the *family* $\{\Phi^{(b,c)}\}$ against it —
Balthasar's sketch already suggests (a) passes unconditionally and (b)
passes only at $c=0$ (i.e. only by collapsing to (a)), which would be a
substantive, non-vacuous answer that simultaneously resolves Melchior's
open parameter. Only "partial — only sketched" per Balthasar's report;
this round would formalize and check it properly (all $c$, exact
identity, not just $t_2=0$).
ROUTES AROUND: both this round's findings at once — Balthasar's/Casper's
`vacuous-or-trivial` (wrong group; this uses the group/condition they
showed *does* bite) and Melchior's `gap-found` (the free constant $c$;
this direction's own test target is exactly what would fix it).
`[HEURISTIC]` a hypothesis that already has a partial positive
computation behind it (Balthasar's sketch) is lower-risk than an
untested symmetry group, though full generality (all $c$, all coupled
$F$, not just $t_2=0$) is unconfirmed.

**2 — Drop naturality/symmetry framing entirely; make "how much cross-index data survives" the literal subject of the hypothesis (statement axis).**
Casper's report names the actual disputed quantity directly: not
whether a map is covariant under an index-swap, but how much of
$\partial_jf_i$ ($j\neq i$) the routing map $\rho$ preserves. Reformulate
the claim as a condition on $\rho$ itself — e.g. require $\rho$ to be
injective on the "other-index" derivative slot (no cross-derivative
information silently discarded), or explicitly quantify the dimension of
information lost — rather than testing an external symmetry axiom against
it. This differs in kind from Direction 1: Direction 1 still uses a
naturality/invariance-under-a-group style hypothesis (just a
better-chosen group); this direction abandons the symmetry-axiom
approach altogether in favor of a direct information-preservation
criterion on $\rho$.
ROUTES AROUND: the general failure mode Casper named — that a symmetry
group can be structurally too coarse for the axis actually in dispute —
by not using any symmetry group at all for the load-bearing part of the
hypothesis.
`[HEURISTIC]` framing the requirement as "does not discard
cross-derivative data" is closer to what the researcher's program
actually needs from a per-coordinate extension (faithful transport of
coupling information) than any relabeling symmetry ever was; untested
whether it is satisfiable by any map at all into the 2-dimensional
codomain, which would be the first thing to check.

**3 — Construct (not test) the routing map via descent under the corrected group (technique axis).**
Round 2's own unused sibling, r2-propose Direction 2 (symmetrization/
invariant-theoretic descent to *build* $\rho$ so it is equivariant by
construction), was never tried — Round 2 tested Direction 1 only. Revive
it, but swap the acting group: instead of descending under the
$S_n$ relabeling action (now shown structurally incapable of
constraining anything, since every "own vs. other index" rule already
descends trivially), descend under the independent per-coordinate
scaling group $(\mathbb R^\times)^n$ (or its formal/graded analogue) that
Direction 1 targets — i.e., build $\rho$ as the unique/canonical map
equivariant for *that* action instead of for relabeling. This is a
different technique from Direction 1 (constructs a map guaranteed to
satisfy a property, rather than testing hand-picked candidates against
it) and from the original Direction 2 (different acting group, chosen
because Direction 2's original group is now shown non-discriminating).
ROUTES AROUND: Round 2's structural finding that $S_n$-descent targets
the wrong invariant, while preserving the "construct don't enumerate"
technique that Direction 2 offered and that this round never got to.
`[HEURISTIC]` averaging/coinvariant constructions under a
non-permutation (continuous scaling) group are a different and less
standard tool than the finite-group Reynolds operator originally
proposed; whether a nonzero, well-typed canonical map results is
unconfirmed and would be the first thing this slot needs to check.

**4 — Import the literature's two-Weil-algebra fibered bundle functor $T^{A,B}$ (technique axis, carried untouched from Round 1).**
Still untouched since Round-1 propose Direction C: Kolář–Michor–Slovák-
style base/fiber Weil functor supplies compatibility between two Weil
algebras by construction (one compatibility datum for a base/fiber
split), rather than by choosing among ad hoc pairwise routing maps and
then testing symmetry conditions on them after the fact. Distinct in
kind from 1–3: it does not touch the routing-map-family or
symmetry-axiom space at all; it replaces the whole per-coordinate
construction with an externally supplied, already-compatible one.
ROUTES AROUND: the entire family of problems this and Round 1 exposed
(underspecified routing maps, symmetry axioms that don't bite) by not
constructing a routing map from scratch at all.
`[HEURISTIC]` unconfirmed whether $T^{A,B}$'s base/fiber compatibility
shape (one base, one fiber algebra) can even express the per-coordinate
$n$-algebra setup at stake here without itself collapsing back to a
two-algebra (not $n$-algebra) picture; flagged as a lead, not a citation
of a settled applicability result.

## 4. Duplication check

- Direction 1 is not a repeat of Round-2's tested Direction 1 (that
  specific claim, swap-equivariance, is now closed as vacuous for this
  pair) — it substitutes a different hypothesis that already has partial
  positive evidence of discriminating.
- Direction 2 does not reuse any previously-named hypothesis (relabeling,
  non-canonical isomorphism, or independence-of-parameters) — it is a new
  axis (direct information content of $\rho$) not previously proposed.
- Direction 3 revives r2-propose's own Direction 2 but explicitly changes
  the acting group in response to this round's finding that the original
  group choice was the problem — not a cosmetic patch of Direction 1.
- Direction 4 is identical in substance to Round-1's Direction C, carried
  forward because it remains untouched and is orthogonal to everything
  tested since; included per the standing instruction to consider
  unfinished MAGI-adjacent leads as a possibly cheaper next step, not
  re-proposed as new.
- Round-1's Directions A (restrict vector-field class) and D (initial-
  value axis) are not repeated here; they remain available in the log but
  are not re-surfaced since nothing this round bears on them either way.
