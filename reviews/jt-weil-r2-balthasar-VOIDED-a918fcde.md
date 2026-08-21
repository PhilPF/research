# jt-weil — Round 2 — Balthasar — VOIDED DUPLICATE LAUNCH

**Status: VOID. Not used for round 2 resolution.** This run (agent
`a918fcde0bb0d03d5`) was dispatched under a prompt that included
balthasar-specific framing melchior's and casper's round-2 prompts did not
receive — an orchestrator error that broke the CLAUDE.md §3 identical-input
requirement. It was superseded by a corrected redispatch (agent
`a100b41b775e5ea07`, see `reviews/jt-weil-r2-balthasar.md`) before this run
finished. Kept here, unmodified, as a possible lead for a future round —
per CLAUDE.md §4 hard-kill practice of retaining whatever a disqualified run
wrote, even though this was a dispatch-integrity issue rather than a timeout.

## Structured report (verbatim from agent a918fcde0bb0d03d5's notification)

VERDICT: counterexample-found

COUNTEREXAMPLE:
HEAD-ON TEST FIRST — the family is NOT empty. Euler and every Runge–Kutta
method satisfy C(n,A) at EVERY basis, because phi_m(S F S^-1) = S phi_m(F) S^-1
for all S in GL_m(R), and a change of R-basis of A acts by S = g^{+n}. The
round-1 basis witness (Euler + chi kick) is correctly killed by convention 1,
but ordinary methods are not. Not vacuous.

The counterexample is to the word "characterization". Let
L*_m := { g^{+n} f_A (g^{+n})^-1 : m = nN, A Weil of dim N >= 2 } be the
non-trivially prescribed locus (N=1 forces A=R and C(n,R) is a tautology).
L*_m is thin: for m=2 it is one function of one variable plus 4 GL_2
parameters inside the space of all fields on R^2 — proper, empty interior.
Pick any F_0 not in L*_2 and any map G: R^2 -> R^2 whatsoever. Define
phi_1 = Euler; phi_2 = Euler except phi_2(F_0) := G; phi_k (k>2) = Euler
corrected on the lifts of F_0 so that C(2,A): phi_{2N}((F_0)_A) = (G)_A holds
for every A and every basis.
Hypothesis audit: each phi_k is a function of (k, field) alone; C(n,A) holds
as an EXACT identity (convention 2) at EVERY basis (convention 1) for every n
and every Weil A — on the lift locus the values are Euler's, which are
basis-independent; at F_0 it holds by construction; F_0 never appears on the
right of any condition since F_0 is not in L*_2.
So this Phi "supports jet transport" while being discontinuous,
zeroth-order-inconsistent, non-convergent and non-equivariant, and G is
arbitrary — the admissible family contains a copy of {all maps R^m -> R^m}
for each m >= 2. Structurally: phi_1 is constrained by the entire diagram only
through the affine rigidity below; on L*_m, phi_m is fully determined by lower
levels; off L*_m it is fully free. This is a left-Kan / free-extension
coherence condition, not a characterization — everything distinguishing Euler
from RK4 lives in phi_1 and is invisible to the diagram.

SECOND FINDING, answering (d) positively: exact-Fraction sweep over all 13
same-dimension pairs of monomial Weil algebras of dim 3, 4, 5 gives f_A = f_B
iff f is affine, in every pair. Smallest collision is m=3 (R[x]/x^3 vs
R[x,y]/(x,y)^2), correcting round 1's m=4. The two prescriptions are FORCED TO
AGREE, and agreement is equivalent to phi_1(f) being affine for affine f. So
(d) is "over-determined but consistent": the collision derives a genuine
closure condition no hypothesis supplies, satisfied by Euler and all RK.
Collisions between tensor-decomposable labels ((2,D) vs (1,D⊗D)) are free,
implied by C(1,D); the binding ones are exactly between tensor-INDECOMPOSABLE
labels.

THIRD, minor but real: the skeleton imposes no regularity on f, yet f_A is
undefined unless f is C^k for k = nilpotency order of A, so C(n,A) is not a
well-formed condition on the stated domain of phi_n.

LOCATES:
"phi_n is a function of (n,f) and nothing else" is too weak, and convention 1
does not repair it. The user is right that all-bases does not force
equivariance — but the gap between the two is where the whole solution space
lives: convention 1 forces GL_N-equivariance only RESTRICTED to the GL_N-orbit
of the lift locus, and nothing off it. Minimal conditions excluding the wild
Phi, increasing strength: continuity in F is NOT enough (L*_m is thin and
closed, so a bump supported off it is smooth); full GL_m(R)-equivariance is
NOT enough (the orbit of F_0 still misses L*_m); naturality/locality does
suffice — phi_m(F)(y) depending on F only through its infinite jet at finitely
many points, plus a uniform expression in m. That is the statement's own
opening sentence ("a single map per dimension") read as ONE FORMULA rather
than one function; the formal skeleton drops exactly that reading.
For (a)/(b): the edge set is not closed under composition — R[x]/x^4 is a
legitimate edge 1 -> 4 that is tensor-indecomposable, hence no composite — and
the binding constraints live exactly on the non-composable edges. Divisibility
records only dim, a lossy invariant (four non-isomorphic algebras at N=4 give
four different conditions on the same phi_4), so the poset is a shadow of the
category of Weil algebras with dim as a monoidal functor.
Regularity hole: restrict phi_n's domain to C^infinity fields, or make C(n,A)
conditional on f being C^{ord A}.

SCOPE:
Weil algebras (monomial quotients only; no non-monomial ideals, nothing of
dim >= 6): R; D=R[x]/x^2; dim 3: R[x]/x^3, R[x,y]/(x,y)^2; dim 4: R[x]/x^4,
R[x,y]/(x^2,y^2), R[x,y]/(x^3,xy,y^2), R[x,y,z]/m^2; dim 5: R[x]/x^5,
R[x,y]/(x^3,y^2)-monomial, R[x,y]/(x^4,xy,y^2), 4-variable fat point.
Identifications: monomial-basis identity identification for the collision
sweep; GL_2 basis (1,1+eps) for D by hand. NO systematic GL_N sweep of twisted
identifications — main unsearched region. Fields: univariate polynomial f of
degree <= 4, 40 random integer points per pair, exact Fraction, seed 7; no
multivariable f, no transcendental f, n=1 only in the collision sweep.
Methods: explicit Euler computed; RK reasoned about via linear-conjugation
equivariance, not computed; the wild Phi constructed and hypothesis-audited by
hand, not machine-checked. Levels m in {1,2,3,4,5} plus m=1 and m-prime
boundary reasoning. references/ absent on this branch.

SUBTASKS:
- references/ consultation: done
- head-on non-emptiness test under closed conventions: done
- (c) what every-basis forces structurally on Phi: done
- (d) collision sweep, dim 3-5, identity identification: done
- (d) collision sweep under GL_N-twisted identifications: untouched
- wild-Phi counterexample to characterization claim: done
- (b) tensor composition under all-bases convention: partial
- (a) restriction along divisor chains: partial
- hypothesis-boundary probes (regularity, m=1, m prime, step size h): partial
- coordinate-ordering divergence-witness attempt: done

FLAGS: none

PETITION: GL_N-twisted collision search — solve U f_A U^-1 = g_B for
U in GL_N(R) and non-isomorphic Weil algebras A, B of equal dimension, dims
3-6, rather than only the identity coordinate identification. Convention 1
makes twisted identifications legitimate edges, so a solution with f
NON-affine would strengthen the derived rigidity from "phi_1 preserves affine
maps" to a constraint on higher jets — the only route I see by which the
diagram could constrain phi_1 enough to say anything about the identity of the
method, i.e. the only route by which "characterization" could be earned. A
null result is equally informative: it would confirm phi_1 is essentially free
and the framework is a coherence condition only.

ACQUISITION: Kolář–Michor–Slovák, *Natural Operations in Differential
Geometry* ch. VIII (Weil bundles), and Jorba–Zou / Abad–Barrio–Blesa–Rodríguez
on jet-transport ODE integrators — to ground the two [UNVERIFIED] facts and
to check whether "the method is given by a uniform arithmetic expression" is
already standing in that literature.
