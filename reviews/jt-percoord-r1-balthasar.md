# Balthasar — Round 1 — claim: jt-percoord

## 0. Framing

No formal hypotheses have been fixed for this claim. There is no definition on
record in this repo of "jet transport," "Weil lift," "Weil algebra,"
"extension," or "method." The claim itself is a proposal to *state and test*
a generalization ("per-coordinate fibered extension") of an unstated base
notion. My mandate is adversarial probing of the *statement as posed*, not of
an argument (none exists). Given the near-total absence of hypotheses, the
productive move is: (a) enumerate the plausible literal formalizations of
"per-coordinate fibered extension" that the words support, (b) test each
against degenerate/boundary cases, (c) report where the natural readings
either fail to type-check or collapse to something with no new content.

## 1. Subtask decomposition (priority order)

1. **[done]** Pin down candidate formalizations of "each coordinate is
   Weil-lifted independently" for a coupled ODE system.
2. **[done]** Test the single-coordinate boundary case (n=1).
3. **[done]** Test the decoupled/diagonal system case (f_i depends only on x_i).
4. **[done]** Test a genuinely coupled system (2D linear oscillator) under the
   most literal "independent per-coordinate algebra" reading.
5. **[done]** Test a patched reading with a shared ambient algebra (ordered
   tensor/exterior product of the per-coordinate pieces) on the same coupled
   system, to see whether the obstruction in (4) is an artifact of a
   too-literal reading or persists.
6. **[partial]** Same-dimension / isomorphic-Weil-algebra case ("may need to
   respect some change") — only touched briefly, not searched.
7. **[untouched]** Nested extensions; extensions w.r.t. parameters, time,
   initial value. These are separate limbs of the background text, not part
   of the specific "per-coordinate" claim; flagged out of scope for this
   round but noted as adjacent unexplored territory.

(No CAS available in this sandbox — `sympy` is not installed and `pip
install` has no network access to PyPI here. All computations below are
first-order Taylor/linear-substitution arithmetic done by hand; they are
elementary enough that this is not a rigor loss, but I flag the missing
tool for the record.)

## 2. Candidate formalizations

Take an ODE system dx_i/dt = f_i(x_1,...,x_n), i=1..n, on some open set.
"One global Weil algebra" jet transport (the presumed base case) lifts the
whole state to A^n for a single local Artinian R-algebra A = R⊕m (m
nilpotent), via X_i = x_i + (nilpotent part in A), and asks that the
vector field's A-linear extension applied to the lift agree with what the
numerical method produces order-by-order in m.

"Per-coordinate fibered extension" as worded suggests: pick possibly
distinct Weil algebras A_1,...,A_n (one per coordinate) and lift X_i ∈ A_i
independently, rather than all X_i living in a shared A. Two literal
readings:

- **(R1) No shared ambient structure.** X_i ∈ A_i, full stop; f_i is
  evaluated on the tuple (X_1,...,X_n) with no map relating A_i and A_j
  for i≠j.
- **(R2) Shared ambient algebra Λ, with each A_i ↪ Λ.** E.g. Λ = tensor or
  exterior product of the A_i's (this is the natural candidate for what
  "fibered" is meant to supply), and X_i is regarded inside Λ via its
  embedding.

## 3. Boundary case n = 1

If the system has a single coordinate, "per-coordinate" and "global" are
the same statement by definition (there is only one coordinate to
"fiber"). No content is added or tested. Trivial, but worth recording:
any interesting content of this claim requires n ≥ 2 *and* coupling
between at least two coordinates — see §5.

## 4. Diagonal / decoupled systems: f_i = f_i(x_i) only

Take dx_i/dt = f_i(x_i) for each i (no cross-dependence). Lift under
reading (R1): X_i = x_i + e_i v_i, A_i = R[e_i]/(e_i²).

  f_i(X_i) = f_i(x_i) + e_i v_i f_i'(x_i)  (dropping e_i², truncating at
  first order — the standard first-jet computation, done independently in
  each A_i since f_i never touches x_j, j≠i).

Compare against the *global* single-Weil-algebra construction with one
shared e, e²=0, applied to the whole vector: X_i = x_i + e v_i,
  f_i(X_i) = f_i(x_i) + e v_i f_i'(x_i) for every i.

These two computations are literally the same equations up to the
cosmetic renaming e ↦ e_i per component (no e_i e_j cross term ever
arises, precisely because the system is diagonal, so the fact that the
e_i's are formally distinguishable symbols never gets exercised). So on
the diagonal-system class, "per-coordinate fibered extension" produces
*exactly* the same transported dynamics, equation by equation, as the
already-existing single global Weil algebra. There is no new
mathematical content in this case: the "fibering" is invisible whenever
there is nothing to fiber over.

## 5. Coupled system: harmonic oscillator dx/dt = y, dy/dt = −x

This is the smallest genuinely coupled instance (n=2, off-diagonal
Jacobian entries ±1, both nonzero).

### 5a. Reading (R1): independent A_1 = R[e_1]/(e_1²), A_2 = R[e_2]/(e_2²), no shared structure

Lift X = x + e_1 v_1 ∈ A_1, Y = y + e_2 v_2 ∈ A_2. The equation for the
first coordinate requires dX/dt = f_1(X,Y) where f_1(x,y) = y. Substituting:

  f_1(X, Y) = Y = y + e_2 v_2.

But dX/dt must be an element of A_1 (X lives in A_1 by construction, its
formal time-derivative is tracked inside A_1, i.e. it should be of the
form (something) + e_1(something)). The right-hand side y + e_2 v_2 is
not an element of A_1 at all — e_2 is not a generator of A_1, there is no
map A_2 → A_1 or A_1 → A_2 supplied by the hypotheses that would let you
reinterpret e_2 v_2 as a multiple of e_1. **The lifted vector field is not
well-typed.** Symmetrically for the second coordinate: f_2(X,Y) = −X =
−x − e_1 v_1, foreign to A_2.

So under the most literal reading of "each coordinate is Weil-lifted
independently" (no shared structure between the per-coordinate algebras),
*the construction does not exist* as soon as any off-diagonal Jacobian
entry ∂f_i/∂x_j (i≠j) is nonzero — i.e. as soon as the system is coupled
at all. This is not a subtle failure of some strengthened property; the
object "the A-lift of the vector field" fails to be defined, so there is
nothing for "jet transport" to be a property *of*.

### 5b. Reading (R2): shared ambient Λ = R[e_1,e_2] with e_1²=e_2²=0, e_1e_2 kept (dimension 4, a genuine Weil algebra: exterior algebra on 2 generators)

Embed A_1, A_2 ↪ Λ in the obvious way. Set X = x + e_1 v_1 ∈ Λ,
Y = y + e_2 v_2 ∈ Λ (both now typed in the *same* algebra, so no
mismatch). Then:

  f_1(X,Y) = Y = y + e_2 v_2  (an honest element of Λ now: coefficients
  1 ↦ y, e_1 ↦ 0, e_2 ↦ v_2, e_1e_2 ↦ 0)

  f_2(X,Y) = −X = −x − e_1 v_1.

Demanding dX/dt = f_1(X,Y) forces the e_2-coefficient of dX/dt to equal
v_2. But X was posited to have *no* e_2-component (X = x + e_1 v_1, an
element of the A_1-summand of Λ only) — so consistency of the ODE forces
X to *acquire* a nonzero e_2-component under the flow, i.e. X cannot
stay inside the A_1-summand; the dynamics push it into the full Λ. The
same happens to Y with respect to e_1. In other words: the only way to
patch reading (R1) into something well-typed is to let every coordinate's
lift range over the *entire* shared ambient algebra Λ from the start —
at which point what you have built is not "coordinate i lives in its own
Weil algebra A_i" but rather "the whole system lives in one shared Weil
algebra Λ," which is precisely the pre-existing global construction the
claim proposes to go beyond. The per-coordinate labelling (which basis
vector of Λ was initially assigned to which coordinate) does no work once
the flow is run; it is not preserved by the dynamics.

### 5c. Non-canonicity as a second-order remark

Even restricting to reading (R2), the choice of ambient Λ is not forced:
one could instead take Λ' = R[e_1,e_2]/(e_1²,e_2²,e_1e_2) (the "all cross
terms zero" ambient, dimension 3) instead of the exterior algebra
(dimension 4, e_1e_2 ≠ 0 retained). These give different transported
dynamics for the *same* coupled system and the same per-coordinate data
(in Λ', the inconsistency of §5b becomes an outright contradiction
0 = v_2 rather than a forced collapse, since there is no e_2-slot in X's
target that could ever be reached — Λ' is even more restrictive). This
matches the background text's own remark that Weil algebras "of the same
dimension... may be isomorphic, so the method may need to respect some
change" — confirmed here as a real, not hypothetical, extra-structure
requirement: the claim as posed does not specify *which* ambient/gluing
algebra realizes "fibered," and different choices are inequivalent.

## 6. Reading of the evidence

Across the only two readings the wording supports:

- No-shared-structure reading (R1): well-typed **only** for diagonal
  (decoupled) systems, where it silently reduces to n disconnected copies
  of the single-coordinate theory (§4) — zero new content.
- Shared-ambient reading (R2): for coupled systems, consistency forces
  collapse back onto an ordinary single global Weil algebra applied to
  the whole state (§5b), the very thing the claim was meant to move past;
  and even then the choice of ambient algebra is not canonical (§5c).

I did not find a "coupled AND genuinely per-coordinate" regime under
either natural reading. This is the shape of a vacuity finding rather
than a counterexample to a fixed proposition: the statement, as currently
worded, does not yet pick out a well-defined mathematical object outside
of the trivial (diagonal) case, so there is no non-trivial claim yet to
break with a specific counterexample.

## 7. What would exclude this finding (observation, not a fix)

The obstruction in §5 is located precisely at the absence of any
specified structure relating A_i to A_j for coordinates i,j linked by a
nonzero ∂f_i/∂x_j. Supplying such structure explicitly — e.g. fixing the
ambient algebra Λ as a specific, motivated construction (not merely "some
tensor product") together with a rule for how the flow's coupling terms
are routed through the A_i ↪ Λ embeddings, and showing that rule is
independent of an arbitrary choice among the isomorphic same-dimension
options (§5c) — is the minimal addition that would let the coupled case
even be posed as a testable proposition. Absent that, the claim currently
only has content on the class of systems for which it is not needed
(diagonal systems), which is the definition of vacuity for this specific
generalization.

## 8. Scope actually covered

- n=1: covered (trivial).
- n=2 linear diagonal: covered by hand.
- n=2 linear coupled (harmonic oscillator), first-order (dual-number)
  Weil algebras only, both readings (R1) and (R2), plus one alternative
  ambient algebra in (R2): covered by hand.
- Not covered: n≥3, nonlinear coupled systems, higher-order (A = k[e]/e^k,
  k≥3) per-coordinate algebras, mixed-order per-coordinate algebras
  (A_1 of order 1, A_2 of order 2), nested extensions, parameter/time/
  initial-value extensions. These remain open probes for a later round if
  the statement is reformulated with an explicit gluing structure.

## 9. Verdict

`vacuous-or-trivial`: under both literal readings of "per-coordinate
fibered extension" available from the wording, the construction is either
undefined (coupled systems, no shared structure) or collapses to the
pre-existing single global Weil algebra (coupled systems, shared ambient
structure), with the only well-defined and non-collapsing instance
(diagonal systems) contributing no content beyond n disconnected copies
of the single-coordinate theory. No counterexample to a specific
proposition is reported because no proposition survives to be tested
outside the trivial case; this is a vacuity/misframing finding at the
level of the statement itself, per the task's own directive to report a
formalization gap as a legitimate finding.
