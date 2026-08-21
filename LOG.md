# Research Log

## Round 1 — 2026-08-21 — jt-weil
Statement: A numerical method Phi = (phi_n) supports jet transport iff, for every
n and every Weil algebra A of dimension N, a compatibility condition C(n,A)
relating phi_n(f) and phi_{nN}(f_A) holds (under the basis identification
A^n =~ R^{nN}). Ranging over factorizations m = nN of a fixed m organizes the
family as a diagram over the divisibility poset with Weil algebras as edges.
Round 1 tested, as one package: (a) restriction along divisor chains, (b)
composition under tensor product, (c) automorphism action / well-definedness,
(d) consistency where two lift structures on the same R^m share vector fields.
Argument shape: direct audit (well-definedness, restriction, tensor composition,
automorphism action, multi-structure consistency) — no proof attempted.
Outcome: definitional-halt (triggered by melchior and casper, each with a
divergence witness; outranks all other outcomes this round per CLAUDE.md §5).
MAGI: M gap-found (provisional-under-ambiguity) | B counterexample-found
(provisional-under-ambiguity) | C likely-misframed (provisional-under-ambiguity),
C-constructive unclear
Unfinished: melchior — (d) non-degenerate common vector fields at m=4: partial;
smoothness requirement on phi_n(f) and placement of step size h: untouched.
balthasar — (b) tensor composition: partial; (a) restriction along divisor
chains: partial; systematic GL_N basis sweep at dim>=3: untouched; algebras with
dim m/m^2>=3, dim>=5: untouched. casper — vacuity audit of (d): partial;
constructive-status: partial; grounding the Weil-functor composition theorem in
a primary source: untouched.
Extensions: melchior petitioned "(d) non-degenerate common vector fields at
m=4" — moot, round halted before reaching Lilith extension-ruling (not ruled).
balthasar petitioned "map the collision lattice at m=8 or 12 across all Weil
algebras of the relevant dimensions" — moot, same reason (not ruled).
Reviews: reviews/jt-weil-r1-{melchior,balthasar,casper}.md

### Definitional halt — two ambiguities, both require user ruling

**Ambiguity 1 (raised by melchior; corroborated independently by balthasar).**
Quantifier over bases of A in "once a basis of A is fixed" in the definition
of C(n,A):
- B1 — C(n,A) required to hold for SOME basis of A
- B2 — C(n,A) required to hold for EVERY basis of A
- B3 — a single global choice function A -> basis(A) is fixed once and for
  all; C(n,A) is only ever evaluated at that basis

Witness: n=1, A=R[e]/(e^2), phi_1 = explicit Euler,
phi_2(g)(x,y) = (x,y) + h g(x,y) + (0, h*g_2(0,0)). In basis (1,e):
g_2(0,0)=0, C(1,A) holds. In basis (1+e,e): g_2(0,0) = -f(0), C(1,A) fails
whenever f(0) != 0. Same Phi, same A, opposite verdicts under B1 vs B2/B3.

**Ambiguity 2 (raised by casper).** The content of C(n,A) itself — the
skeleton names it as "the compatibility condition relating phi_n(f) and
phi_{nN}(f_A)" but never states it:
- (i) full lift-equivariance: phi_{nN}(f_A) = T_A(phi_n(f)) under the chosen
  identification A^n =~ R^{nN}
- (ii) augmentation compatibility only: pi o phi_{nN}(f_A) = phi_n(f) o pi,
  for the augmentation pi: A -> A/m_A =~ R, with no constraint on the
  nilpotent part
- (iii) order-p agreement: phi_{nN}(f_A) = T_A(phi_n(f)) + O(h^{p+1}) for the
  method's order p

Witness: n=1, A=R[e]/(e^2), m=2, f(x)=x^2. Phi = explicit Euler at every
level except phi_2(g)(y) = (y1 + h g_1(y), y2 + h g_2(y) + h^2 g_1(y)^2).
Reading (i): C(1,A) fails. Reading (ii): C(1,A) holds. Reading (iii), p=1:
C(1,A) holds.

Per §5, this halts the round; melchior's gap, balthasar's counterexample, and
casper's misframing verdict are all recorded above as
provisional-under-ambiguity — not settled findings — until the user rules on
both readings. Not routed to Lilith. Awaiting user.

Carried to Lilith: none yet (halt precedes Lilith dispatch).

### Closure — user ruling on both ambiguities (2026-08-21)

**Ambiguity 1 (basis quantifier).** Ruled: **B2** — C(n,A) must hold for
every R-basis of A. User's own words, verbatim: "It must hold for all
bases, but that does not force equivariance."

**Ambiguity 2 (content of C(n,A)).** Ruled: **(i) full lift-equivariance**
— C(n,A) is the exact identity phi_{nN}(f_A) = T_A(phi_n(f)) under the
chosen R-linear identification A^n =~ R^{nN}.

Recorded in state/session.json under settled_conventions. Per §5, these
are now closed conventions: binding on all subsequent rounds of jt-weil,
to be included verbatim in every future dispatch's sanitized input. Round
1's provisional-under-ambiguity verdicts (melchior gap-found, balthasar
counterexample-found, casper likely-misframed) remain on record as
provisional and are not re-adopted as settled findings — round 2 retests
the same (a)-(d) package fresh, with C(n,A) now fully pinned down.

## Round 2 — 2026-08-21 — jt-weil
Statement: same package (a)-(d) as round 1, now with both settled
conventions substituted into C(n,A): C(n,A) is "for every R-basis of A,
phi_{nN}(f_A) = T_A(phi_n(f)) exactly, under the R-linear identification
A^n =~ R^{nN} induced by that basis, for every f: R^n -> R^n."
Argument shape: direct audit (well-definedness, restriction, tensor
composition, automorphism action, multi-structure consistency), same as
round 1, now unblocked by closed conventions.
Dispatched to melchior, balthasar, casper in parallel (Opus), byte-identical
sanitized input including the two settled conventions verbatim. Round 1
verdicts and partial/untouched subtasks are NOT included in this input,
per §3 (prior rounds' verdicts on this claim are stripped) — only the
settled_conventions carry forward, as the explicit exception.
Outcome: definitional-halt.

**Dispatch incident (orchestrator error, not an agent finding).** The first
balthasar launch (agent a918fcde0bb0d03d5) received extra framing melchior
and casper did not get, breaking §3's identical-input requirement. Caught
before casper was dispatched; balthasar was redispatched with corrected,
truly identical input. Both launches wrote to the same output paths; the
voided launch finished later and overwrote the corrected launch's files on
disk. Reconstructed the corrected launch's review/verdict from its
structured report (preserved verbatim in its completion notification).
Preserved the voided launch's distinct content (a different, arguably
sharper, "wild Phi" counterexample and a corrected m=3 collision, superseding
round 1's m=4 claim) at reviews/jt-weil-r2-balthasar-VOIDED-a918fcde.md,
clearly marked void and excluded from this round's resolution — kept as an
unverified lead for a future round.

MAGI: M gap-found | B none-found (bounded scope, dim<=4 algebras) |
C likely-misframed, C-constructive unclear

Selected non-ambiguity findings (all provisional-under-ambiguity per below,
except where noted independent):
- Melchior: convention 1 ("holds at every basis") does NOT reduce to inert
  well-definedness — it forces a restricted conjugation-equivariance of Phi
  under the block subgroup Delta_n(GL_N(R)), confirming and sharpening the
  user's own remark. This propagates into (b): tensor composition supplies
  equivariance only under the subgroup generated by the two factor groups
  (dim <= 7 inside GL_4 for N_A=N_B=2), while C(n, A tensor B) at every basis
  demands all of GL_4(R) — the diagram does not commute under convention 1
  as stated. [independent of the (d)-phrase ambiguity]
- Casper: the divisibility poset is a lossy dimension-shadow of the category
  of Weil algebras (collapses non-isomorphic same-dimension algebras, can't
  express truncation-order homomorphisms); separately, the pinned skeleton
  makes phi_n(f) a point with no initial condition or step size, so C(n,A)
  as stated constrains away exactly the nilpotent/derivative data jet
  transport exists to compute. [independent]
- Balthasar: Aut_{R-alg}(A) acts trivially on the set of conditions under
  convention 1 (naturality already identifies C(n,A) across an Aut(A)-orbit
  of bases) — corroborates melchior's finding from a different direction.
  phi_1 is entirely unconstrained by the whole diagram (no factorization
  other than 1x1). [independent]
- Voided-but-preserved (balthasar, not used for resolution): a "wild Phi"
  construction under which the closed conventions admit a discontinuous,
  non-convergent method as "supporting jet transport" — the diagram
  constrains phi_m only on a thin GL-orbit locus and leaves phi_1, and hence
  everything distinguishing Euler from RK4, entirely free.

Unfinished: melchior — A tensor B =~ B tensor A commuting square: untouched;
(a) restriction along divisor chains: partial (reduced to (b)+(d) only).
balthasar (corrected run) — S7 (explicit tensor-composition counterexample):
untouched; S8 (Weil algebras dim>=5): untouched. casper — restatement of
(a)/(b) over the category W: partial; constructive status: partial.

Extensions: melchior petitioned orbit-intersection geometry for (d) — moot
(round halted before Lilith extension-ruling). balthasar petitioned S7 — moot
(same reason). casper petitioned re-posing (a)-(d) over the category W of
Weil algebras — moot (same reason).

Reviews: reviews/jt-weil-r2-{melchior,balthasar,casper}.md (balthasar
reconstructed; voided duplicate at
reviews/jt-weil-r2-balthasar-VOIDED-a918fcde.md, not authoritative)

### Definitional halt — one fresh ambiguity, needs user ruling

**Raised by melchior and casper independently, both with divergence
witnesses; corroborated (non-halting) by balthasar.** What does item (d)'s
phrase "two lift structures on the same R^m have vector fields in common"
mean?

- **A** — same base field, different algebras: same n, same f: R^n -> R^n,
  two Weil algebras A,B of equal dimension N; phi_m receives one prescription
  from f_A and one from f_B. (Melchior reading II)
- **B** — any common image, including degenerate elements: some map
  F: R^m -> R^m lies in both lifted-image sets L(n,A) and L(n',B). (Melchior
  reading I / Casper reading A)
- **C** — non-degenerate common image: as B, but excluding always-present
  degenerate elements (zero field, scalar multiples of the identity). (Casper
  reading B)
- **D** — common refinement / compatible source: h = f_A = g_B with the two
  identifications compatible with a common refinement of the two lift
  structures. (Casper reading C; flagged by Casper as possibly near-circular)

Witness (Casper): the zero field 0 on R^m is the A-lift of f=0 and the B-lift
of g=0 for EVERY pair of lift structures on EVERY R^m — under B the
hypothesis of (d) is universally satisfied and carries no information; under
C it is a genuine restriction; under D it plausibly forces agreement by
construction. Vacuous / substantive / near-circular is the full spread.

Witness (Melchior): n=1, N=3, m=3; A=R[e]/(e^3), B=R[x,y]/(x,y)^2,
f(t)=t^2. f_A and f_B differ in their third coordinate (by a1^2). Under
B/C/D this pair is not even an instance of (d)'s hypothesis (f_A != f_B).
Under A it is an instance, and the two prescriptions are independent. Same
exact case, opposite characterizations of the round's own analysis.

Per §5 this halts the round; melchior's gap, casper's misframing verdict,
and balthasar's none-found are all recorded above as
provisional-under-ambiguity for the parts touching item (d). Not routed to
Lilith. Awaiting user.

Carried to Lilith: none yet (halt precedes Lilith dispatch).

