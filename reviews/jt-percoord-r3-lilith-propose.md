# Lilith — Mode 1 (propose) — jt-percoord Round 3 (single-direction dispatch)

## 0. Constraint on this run

Per instruction, exactly ONE direction, precise and self-contained enough
to be dispatched directly as Round 3's MAGI claim (no user pick-from-menu
step this time). The new input is a *pivot in subject*, not a request to
rank Round 2's four carried directions — the researcher has explicitly
said "we are not trying to study vector fields, but... how does this
restrict the methods." So this round formalizes that pivot rather than
selecting among the Round-2-propose menu (state/lilith/jt-percoord-r2-propose-v2.json).

## 1. What must be reused vs. what must not be reopened

- Round 1 located: the per-coordinate lift of a *vector field* requires an
  ad hoc cross-term routing map ρ (candidates (a) index-blind projection,
  (b) degree truncation) because a vector field's per-coordinate Weil
  lift is not literally "evaluate an existing map in a bigger algebra" —
  it must synthesize coupling data (∂f_i/∂x_j, j≠i) that has nowhere
  canonical to land.
- Round 2 located: naïve relabeling/swap symmetry cannot discriminate (a)
  from (b) (structural, both candidates already "own-vs-other-index"
  covariant); the independence-of-nilpotent-parameters probe can, but is
  only partially formalized; (b) is underspecified by a free constant c.
- The user's new input explicitly reframes the object of study: instead
  of asking "which routing map ρ is correct for the vector-field lift,"
  ask "which numerical/geometric integration METHODS M commute with
  taking a (possibly distinct-order) per-coordinate Weil lift of the
  vector field" — i.e., treat routing/lift-construction as a fixed
  background convention and make the method the variable.
- To keep the new statement well-posed WITHOUT re-litigating Round 1/2's
  open question, this direction fixes ρ = candidate (a) (index-blind
  projection / full multivariable Taylor expansion truncated
  coordinatewise) as the lift convention. (a) is the only candidate that
  survived every test run so far (both Round 2 tests, vacuous or partial,
  never disqualified it), so fixing it is the least assumption-laden
  choice available, not a re-adjudication.

## 2. The key structural observation that makes this a genuinely new question

Lifting a *map* Φ: R^n → R^n via the Weil functor T_D (the actual
multivariable Taylor expansion of Φ using real partial derivatives) is
CANONICAL — no routing ambiguity, because Φ already has honest mixed
partial derivatives ∂Φ_i/∂x_j to draw on. The routing ambiguity that
Round 1 found is specific to lifting a *vector field* (an infinitesimal
generator, not itself a map between Weil spaces) independently along each
coordinate direction. This means the new question — does running a
method's formula in Weil-algebra arithmetic on the lifted vector field
match the canonical functorial lift of the method's ordinary output map —
is well-posed on its "target" side even before ρ is chosen, and only
needs ρ fixed on its "source" side. That asymmetry is exactly what
licenses treating M, not ρ, as the free variable this round.

## 3. Duplication check

Not a repeat of any Round 1/2 direction: Round 1's Direction C (import
T^{A,B} functor) and this round's use of T_D are related only in that
both invoke Weil-functor machinery, but Direction C proposed importing an
external bundle functor to construct ρ itself; here T_D is used only on
the *output side* (lifting the method's plain flow-map, where no routing
choice is needed at all) and ρ is a fixed input, not the subject. Round
2's Directions 1-4 (independence-of-nilpotent-parameters, information-
preservation criterion on ρ, scaling-group descent, T^{A,B} import) are
all still about ρ/ the vector-field lift; none of them ask which methods
commute with a fixed lift. This is a distinct axis, not a cosmetic
variant.

## 4. The single formalized statement

Fix n≥2, an order vector D=(D_1,…,D_n) with each D_i≥1 (distinct orders
per coordinate permitted), and the Weil algebra
W_D := R[e_1,…,e_n] / (e_1^{D_1+1},…,e_n^{D_n+1}).

**Per-coordinate Weil lift of a vector field (fixed convention, = Round-1
candidate (a), not reopened this round):** for F:R^n→R^n admissible
(polynomial or C^∞), define
  L_D(F)(x + t·e) := Σ_{α : 0≤α_i≤D_i} (1/α!) ∂^α F(x) · t^α,
t=(t_1,…,t_n) independent nilpotent parameters, e=(e_1,…,e_n).

**One-step method:** M is an algorithm that, given (F,h), produces an
update map Φ_h^M[F]: R^n→R^n approximating the time-h flow of ẋ=F(x),
defined by a fixed formula built from finitely many evaluations of F (and,
for implicit methods, a solve of an implicit equation in F) — well-typed
by literal substitution over any commutative R-algebra in which that
formula makes sense. This is exactly the sense in which "the same method"
can be run with W_D-arithmetic in place of R-arithmetic.

**Canonical Weil lift of a map (no routing choice needed):** for
Φ:R^n→R^n, T_D(Φ)(x+t·e) := Σ_{α:0≤α_i≤D_i} (1/α!) ∂^αΦ(x)·t^α — the
ordinary multivariable Taylor/chain-rule lift, unambiguous because Φ is
already a genuine map with real mixed partials.

**Commutation condition (the property to characterize):** M commutes
with the per-coordinate Weil lift L_D if, for every admissible F, every D,
every h>0, and every base point x_0∈R^n,
  M[ L_D(F) ] (x_0 + t·e)  =  T_D( Φ_h^M[F] ) (x_0 + t·e)   for all t,
as an identity in W_D — i.e., "run M's defining formula in W_D-arithmetic
on the per-coordinate-lifted vector field, starting from the lifted
point" equals "run M in ordinary real arithmetic to get its output map,
then take that map's canonical functorial Weil lift."

**MAGI's task:** for the concrete test family {explicit Euler, explicit
midpoint/RK2, classical RK4, backward (implicit) Euler, the truncated
Taylor-series ("exact jet") method of order max_i D_i}, on at least one
genuinely coupled 2-coordinate test vector field with D_1≠D_2 permitted,
determine which of these methods satisfy the commutation identity exactly
(for all D and all admissible F), which fail it, which hold only to some
asymptotic order in h, and whether there is an identifiable structural
property of M's defining formula (e.g., expressible purely as a finite
polynomial in F and its partial derivatives evaluated at x_0 — i.e., a
B-series / elementary-differential-type method with no comparison,
ordering, or norm operation baked into its definition) that is necessary
and/or sufficient for commutation to hold at every order D.

## 5. Why this is the right single candidate here

It is the direct, minimal formalization of the researcher's own words —
"which methods do accept this kind of behavior" — with no invented
extra content beyond what is needed to make "commutes with" precise (the
T_D vs. L_D asymmetry in §2 is exactly the piece that had to be supplied
to make the two sides of the commutation square well-typed). It reuses
Round 1's surviving candidate (a) only as a fixed background convention,
so it neither re-litigates the closed ρ-question nor smuggles a verdict
on it in through the back door.
