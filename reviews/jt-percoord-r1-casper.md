# Casper Review — jt-percoord — Round 1

## Scope and method

Round 1, no prior formalization exists in this thread for "jet transport,"
"Weil lift," "Weil algebra," "extension," or "method." My job is not to
audit an argument (none exists) but to ask: is the posed statement —
"state and test jet transport under a per-coordinate fibered extension" —
the right question to be asking right now, in this form.

Subtask plan (priority order):
1. Identify what "jet transport" plausibly refers to and whether the
   posed generalization axis interacts with a load-bearing feature of the
   base notion. — **done**
2. Check whether the specific choice of axis ("per-coordinate") was
   selected for a reason, versus an arbitrary pick from a longer list the
   researcher themselves supplied. — **done**
3. Check degenerate/vacuous ends of the "per-coordinate fibered
   extension" hypothesis space. — **partial**
4. Constructive-status check. — **done** (mostly N/A, no argument yet)

## 1. What is "jet transport" here, and does it have a coordinate-free core?

A brief, scope-limited search turned up a real, named technique: "Jet
Transport" (JT), also called Differential Algebra (DA) in astrodynamics
(Berz, Makino, and later Farrés/Jorba/Villac et al.), which propagates
truncated Taylor jets of a flow map using Weil-algebra-type polynomial
arithmetic (dual-number-like rings). There is also a recent paper
explicitly titled "Jet Functors and Weil Algebras in Automatic
Differentiation: A Geometric Analysis," which looks like it may be from
the same research program this claim is drawn from, and a paper on
"Hamiltonian vector fields on Weil bundles." I did not read these papers
in depth — flag as **plausibly related to jet-transport/Weil-functor
literature (Berz–Makino DA propagation; Kolář–Michor–Slovák-style Weil
bundle functors), unverified in detail**. I am not citing them as
settling anything, only as evidence the base notion is a real, coordinate-
free construction: k-jets classically encode truncated Taylor expansion
"independently of any choice of coordinates" — that coordinate-invariance
is exactly the content of the Weil-functor formalism (Weil algebras
correspond to product-preserving bundle functors that are natural, i.e.
equivariant under all diffeomorphisms/coordinate changes).

This matters directly for the posed statement. If jet transport's whole
reason to route through *one* Weil algebra applied to the *whole* system
is to get a construction natural in the coordinate chart (so that "for a
large class of vector fields" can mean something chart-independent), then
asking whether each *coordinate* of the system can be Weil-lifted
*independently* is asking to break that naturality on purpose. A
per-coordinate fibered extension is manifestly not equivariant under a
change of coordinates that mixes components (e.g. any nonlinear or even
generic linear change of basis) — the construction depends on a
distinguished coordinate system, not just a distinguished manifold
structure. That is not automatically wrong, but it means the resulting
object is answering a *different kind* of question ("what happens for a
fixed presentation of the system") than the coordinate-free classification
of methods the surrounding research program (per the background text)
seems to want ("a large class of vector fields," suggesting invariance
under the group acting on that class). The statement as posed does not
say whether "per-coordinate" is meant relative to a fixed atlas/fixed
presentation (in which case it is a legitimate but narrower question) or
is meant to somehow still be coordinate-free (in which case it is not
obviously well-posed, since "coordinate" is exactly the datum being
varied).

## 2. Is "per-coordinate" a principled next case, or an arbitrary pick?

The background text is an unstructured brainstorm listing at least six
distinct generalization axes: (a) extensions wrt parameters, (b) wrt time,
(c) wrt initial value, (d) a distinct extension per coordinate, (e)
nested extensions (nesting all of the above "over and over"), (f)
extensions with Weil algebras of the same dimension but possibly
non-isomorphic-respecting structure. The claim under test isolates (d)
alone, with no argument for why per-coordinate is logically prior to, or
more informative than, the others, and no acknowledgment that (d)
interacts with (e) and (f) (a per-coordinate extension is itself a
special case of a "nested"/product Weil algebra, so testing (d) in
isolation from (e) may just be testing an easy sub-case that the harder
nested question will subsume anyway).

This is the central outside-view concern: the round has been set up to
test one item plucked from a stated menu, without the baseline case
("jet transport" for a single global Weil algebra, applied uniformly)
itself having been formalized in this thread. Testing a strengthening/
variant of an undefined base notion risks the two-sided failure this
review is meant to catch: either (i) the per-coordinate case turns out to
be no different from the global case once you notice a tensor product of
Weil algebras is again a Weil algebra (mathematically true and known —
so "per-coordinate" reduces to "the global Weil algebra happens to
factor as a tensor product indexed by coordinates," which is a
chart-dependent normal-form question, not a new phenomenon), making the
round's result near-trivial relative to what motivated it; or (ii) the
naturality-breaking noted in §1 is treated as an acceptable cost without
anyone deciding it's acceptable, silently narrowing "jet transport" from
a property of methods on a class of vector fields to a property of
methods on a class of *presentations* of vector fields — a materially
different and weaker object than what "a large class of vector fields"
in the background text seems to intend.

## 3. Degenerate ends

- If all per-coordinate Weil algebras are taken equal to the same
  algebra A, the construction should collapse to (something like) the
  global A^n lift — plausibly not vacuous, a sanity check the eventual
  formalization should reproduce.
- If the per-coordinate algebras have different dimensions, the "fibered
  extension" is presumably a tensor product ⊗A_i (still a Weil algebra,
  dimension = product of dimensions) — this seems fine algebraically but
  reinforces §1: nothing here forces or explains a distinguished
  coordinate splitting; it's imposed data, not derived from the vector
  field or the flow.
- I could not, in the time available, determine whether "per-coordinate"
  is even preserved under the flow itself (a vector field's flow
  generically does not respect a fixed coordinate splitting unless the
  vector field is itself in some fibered/skew-product form) — this is a
  possible further vacuity: for a "large class of vector fields," the
  per-coordinate fibered extension may only be flow-invariant/meaningful
  for a restrictive sub-class (e.g. triangular or skew-product systems),
  which would silently shrink "large enough class" precisely at the step
  the background text says should be maximized. Flagged as **untouched
  in depth** — I could state the concern but not chase a concrete example
  or resolve it; this is exactly a "concern I cannot fully make concrete"
  layered on top of the concrete framing concern above.

## 4. Constructive status

No argument has been given (round 1, statement-only). There is no
existence-by-contradiction, excluded middle, or choice step to flag yet.
Constructive status is therefore **unclear / not applicable** at this
stage — this is informational, not a defect of the round.

## Overall assessment

The statement is not obviously false or vacuous as a piece of
mathematics — tensor products of Weil algebras exist and per-coordinate
constructions are sensible objects to write down. The concern is
framing: (1) it tests one arbitrarily-selected branch from a longer
uncommitted menu before the base notion of "jet transport for a method"
has been pinned down in this thread; (2) the specific branch chosen
plausibly conflicts with a coordinate-invariance property that seems to
be load-bearing for what "jet transport" and "a large class of vector
fields" are supposed to mean in the surrounding program, and the
statement doesn't say whether that conflict is intended or accidental;
(3) there's a real risk the eventual answer is either near-trivial
(reduces to a known tensor-product-of-Weil-algebras fact) or answers a
narrower, coordinate-fixed question than the one motivating the whole
research direction, without that narrowing being flagged as a choice.

This pattern — an appealing-sounding generalization selected from a list,
tested before the base case is fixed, with a plausible silent narrowing
of scope (coordinate-freedom) baked in — is exactly the kind of
misframing this review exists to catch, even though I cannot rule out
that per-coordinate fibered extensions are in fact the right and
illuminating next case once definitions are pinned down.
