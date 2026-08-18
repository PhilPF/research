# Melchior — Coherence Review — jt-percoord — Round 2

## Subtask plan (10-min budget)
1. (priority) Pin down precise definitions of (a) and (b) as literal maps W_1⊗W_2 → W_i; check they are actually well-typed, single, determinate objects — this is where "convenient reinterpretation" risk is highest. [DONE]
2. Formalize the relabeling/swap automorphism σ and the equivariance condition Lift(F^σ)_i = σ(Lift(F)_{σ(i)}) precisely. [DONE]
3. Test the equivariance condition against (a) and (b) concretely (hand derivation + numerical check) to see whether the claim's anticipated branches ("rules out one/both/neither") are actually reachable, and to find the weakest inferential step. [DONE]
4. Check whether the answer depends on unstated choices, i.e. whether the objects being tested are actually uniquely specified by the background text. [DONE — this is where the gap sits]
5. Check quantifier scope (all F vs. symmetric F only), scope of "equal order," and whether W_1 ≅ W_2 claim in the motivation is correct. [DONE, brief — no issue found]

## Setup used for testing
W_i = R[e_i]/(e_i^2), lift X_i = x_i + e_i (unit nilpotent, WLOG for structural testing).
Taylor expansion of f_i at the lifted point, exact since e_1^2=e_2^2=0:

  f_i(x_1+e_1, x_2+e_2) = f_i + ∂_1f_i·e_1 + ∂_2f_i·e_2 + ∂_1∂_2f_i·e_1e_2  ∈ W_1⊗W_2 (basis 1,e_1,e_2,e_1e_2).

Both candidate maps must send this down to W_i = span{1, e_i} (basis dim 2). The swap
σ: x_1↔x_2, e_1↔e_2 is a bona fide automorphism of the whole ambient structure because
W_1 = W_2 as algebras; the swapped system is F^σ_1(x_1,x_2) := f_2(x_2,x_1),
F^σ_2(x_1,x_2) := f_1(x_2,x_1). Equivariance required: Lift(F^σ)_1 = σ(Lift(F)_2) (and
symmetric statement for index 2).

## Candidate (a), reconstructed
Φ_i^{(a)}: 1↦1, e_i↦e_i, e_j↦0 (j≠i), e_1e_2↦0.
  Lift(F)_i^{(a)} = f_i + ∂_i f_i · e_i.
This is fully and unambiguously pinned down by the background's description ("keeps only
same-index nilpotent terms") — no hidden choices.

## Candidate (b), reconstructed — and where the gap is
The background's description of (b) is: "keeps only terms up to a fixed total
nilpotent-degree bound, counted across all the W_j's jointly (does not discriminate by
index, only by total degree)."

This sentence determines *which graded piece of W_1⊗W_2 survives* (degree ≤ D for some D;
D=1 is forced if the output is to fit inside W_i without residual e_1e_2 debris, matching
the "equal order" / order-1 Weil algebra). It does **not** determine *where that surviving
piece lands inside W_i*. The degree-≤1 piece of W_1⊗W_2 is 3-dimensional (span{1,e_1,e_2}),
but W_i is only 2-dimensional (span{1,e_i}). So an extra linear map ρ: e_j ↦ c·e_i (j≠i) is
needed to finish specifying (b) as an actual map into W_i — and no such ρ, nor any
constraint pinning down c, is given in the background or in the round-2 statement.

This is not a cosmetic gap:
- If c = 0, "(b)" collapses exactly onto (a) (the ∂_j f_i term is simply dropped), which
  contradicts the background's assertion that (a) and (b) "generally disagree on which
  cross terms survive" — so c=0 cannot be the intended reading, but nothing in the given
  text says so.
- For any fixed c ≠ 0, one obtains a *distinct* map Φ_i^{(b,c)}: f_i ↦ f_i + (∂_i f_i +
  c·∂_j f_i)·e_i. I verified numerically (finite differences on generic concrete f_1, f_2,
  script below) that Φ^{(b,c)} is σ-equivariant for *every* constant c, exactly as (a) is
  equivariant. Equivariance is checked by matching Lift(F^σ)_1 against σ(Lift(F)_2) at a
  generic point (x1,x2) = (0.7,-1.3):

  a-branch: coeff of e_1 under swap(Lift(F)_2) matches direct Lift(F^σ)_1 to 1e-4.
  b-branch (c=1, the "merge" reading): same match, to 1e-4.
  (The identical argument, symmetric in x1,x2, shows equivariance holds for any c, since
  the construction never distinguishes "index 1" from "index 2" as labels, only uses them
  to route derivatives — and that routing rule commutes with any *simultaneous* relabeling
  regardless of c.)

So: **the family of maps compatible with the literal text of "(b)" is not a single map but
a one-parameter family {Φ^{(b,c)}}_{c∈R}, and the requested equivariance test has zero
power to select among them** — every member passes, for the same structural reason (a)
passes: none of them privileges "coordinate 1" over "coordinate 2" as a label, and the swap
only permutes labels. The round's question ("does it rule out (a), (b), both, or neither")
presupposes (b) denotes one definite map; as literally specified it does not, and the
particular completion needed to make (b) an interesting, non-degenerate alternative to (a)
(i.e. c=1, "merge the two derivatives into the single surviving slot") is supplied by the
reader, not by the given definitions.

## Is the eventual mathematical outcome itself suspicious?
My own reconstruction (the natural completion c=1) suggests the true answer to the
question posed is "rules out neither — vacuous for this pair," which is one of the
disjuncts the claim's own phrasing anticipates as a legitimate outcome. That in itself is
not a defect of the statement — the statement is honestly hedged. The issue I am flagging
is upstream of that conclusion: the object "candidate (b)" that the round asks to test is
underdetermined by the definitions carried over from the background, so "vacuous for this
pair" is currently a claim about a family member chosen by inference, not about the
candidate as given.

## Other checks performed (no issue found)
- W_1 ≅ W_2 via e_1↔e_2 (motivation's premise): correct, both are R[e]/(e^2).
- Quantifier scope of equivariance (must hold for all coupled F, not just symmetric F):
  consistent reading, no ambiguity found; my test used a generic non-symmetric F pair and
  it still held.
- "Equal order" hypothesis is used essentially (both N_i one-dimensional) — consistent
  with statement's restriction; not itself a source of gap.

## Scope not covered (time-boxed out)
- Did not check whether a *degree bound D ≠ 1* (e.g. keeping the e_1e_2 term too, D=2, with
  some further compression into e_i) could still count as "(b)" and whether equivariance
  behaves differently there — background suggests D=1 is intended (matches Weil-algebra
  order) but this is itself inferred, not stated.
- Did not explore n>2 or unequal-order cases (out of scope per claim).
- Did not attempt to determine what a "compatible" map would look like if the requirement
  *did* rule something out (not needed, since the finding is that the object (b) itself is
  underspecified prior to that question).

## Verification script (bash / python, no sympy available; used finite differences)
Ran locally; both (a) and (b, c=1) matched swap-vs-direct lift coefficients to 1e-4 on a
generic non-symmetric pair f_1, f_2, confirming the hand derivation via chain rule.
