# Melchior — Coherence Review, jt-nonisom, Round 1

## Subtask decomposition (priority order)
1. Verify the two Weil algebras and their invariants (dim, m/m^2) as stated. — done
2. Verify f: A→A' and g: A'→A (and the flagged alternative g') are well-defined
   unital R-algebra homomorphisms, and are genuinely non-invertible (neither
   injective nor surjective). — done
3. Check the claim that a Weil-algebra homomorphism φ: A→B induces a natural
   transformation T_φ: T_A ⇒ T_B of the associated Weil functors, and that the
   direction (f gives A⇒A′, g gives A′⇒A) is consistent with the standard
   construction. — done (at the level of citing/checking the standard
   construction's shape, not re-deriving naturality in full generality)
4. Directly test the ambiguity the prompt itself flags: does the non-canonicity
   of g (vs. the alternative g′) produce two *diverging*, checkable readings
   of the claim, in particular for the composite maps g∘f and f∘g? — done,
   this is where I found the load-bearing issue.
5. Assess whether the (a)/(b)/(c) trichotomy is well-typed given 1–4. —
   partial (see below; this is really Lilith/Casper territory once the
   ambiguity in 4 is accounted for, but it bears on whether the *statement*
   is coherent enough to pose the trichotomy meaningfully).

## 1–2. Algebra checks (computationally verified)
Represent A-elements as (a,b,c) ↔ a + b e + c e², with e³=0 truncation, and
A′-elements as (a,b,c) ↔ a + b e1 + c e2, with (e1,e2)²=0 (any product of two
non-constant parts vanishes). I implemented both multiplication tables in
Python (no CAS available in this sandbox — verified by hand-multiplication
truncation rules, see `/tmp/.../scratchpad/check2.py`) and confirmed:

- f(e²) = f(e)·f(e) = e1² = 0 in A′ — so f is well-defined, and its image is
  only span{1,e1}, a 2-dimensional subspace of the 3-dimensional A′. f is
  **neither injective** (ker f = span{e²}) **nor surjective** (misses e2).
  This matches the "non-invertible" billing.
- g(e1)=e², g(e2)=0: checked g(e1)²=0, g(e1)g(e2)=0, g(e2)²=0, all required
  since (e1,e2)²=0 must map to 0 — g is well-defined. Image = span{1,e²},
  again 2-dimensional; ker g = span{e2}. Also neither injective nor
  surjective.
- The flagged alternative g′(e1)=0, g′(e2)=e² is equally well-defined by the
  symmetric computation.

These are not in dispute; the statement's algebra is correct as posed.

**Refinement beyond what the statement says**: g is not merely "one of two"
choices. Any map A′→A sending e1 ↦ λe², e2 ↦ μe² is a valid algebra
homomorphism for *arbitrary* scalars (λ,μ) ∈ R², since m²(A) = span{e²} is
1-dimensional and every element of it squares to 0 and multiplies to 0 with
every other such element (e⁴=0). So the "two equally valid alternatives" in
the statement are really the two extreme points of a genuine linear family;
the statement's framing as a binary choice understates the moduli of valid
non-canonical choices, though (as found below) g and g′ happen to be the two
choices that showcase the extremal behaviors of the family for the specific
composite the statement is implicitly gesturing at.

## 3. Naturality of the induced transformation
The construction "algebra hom φ:A→B induces natural transformation
T_φ: T_A ⇒ T_B" is the standard postcomposition map on the functor-of-points
description T_A(M) = Hom_alg(C^∞(M), A), φ*: h ↦ φ∘h [UNVERIFIED against a
citable source — no references/ dir in this repo; this is the shape of the
construction in Kolář–Michor–Slовák, *Natural Operations in Differential
Geometry*, §35, from memory, flagged UNVERIFIED per instructions rather than
invented]. Under this convention the direction is covariant in the algebra
argument, so f:A→A′ ⇒ T_f: T_A⇒T_A′ and g:A′→A ⇒ T_g: T_A′⇒T_A, matching
the statement's stated directions. I did not find a gap in this part of the
setup — it is standard and the hypotheses (unital R-algebra homomorphism
between augmented, finite-dim, local R-algebras) are exactly what the
construction needs. I did not re-derive full naturality-in-M from scratch;
I checked only that the construction's hypotheses are met, not the theorem's
proof itself (out of round-1 scope, and it is not new content specific to
this claim).

## 4. The load-bearing finding: g's non-canonicity produces a genuine, checkable divergence

The statement itself invites checking whether the g/g′ ambiguity is
"cosmetic" or produces "diverging readings... with a concrete witness."
I computed the two composites that any subsequent (a)/(b)/(c) analysis would
have to use to test the claim ("does requiring commutation with the induced
transformations force something beyond the isomorphism-equivariance case"):

**Composite g∘f : A → A** (using the *stated* g, g(e1)=e², g(e2)=0):
```
(g∘f)(e) = g(f(e)) = g(e1) = e²   ≠ 0
```
This is a genuinely non-trivial (non-identity, non-invertible — it kills e²
but sends e ↦ e²) endomorphism of A. It is *not* the "trivial through-R
augmentation-then-unit" map that option (c) names as the degenerate case.

**Composite g′∘f : A → A** (using the *flagged alternative* g′(e1)=0, g′(e2)=e²):
```
(g′∘f)(e) = g′(f(e)) = g′(e1) = 0
```
This *is exactly* the trivial through-R augmentation-then-unit map (kills
all of m, factors as A → A/m ≅ R → A) — i.e., exactly the degenerate
construction that option (c) of the claim names as the trivial/vacuous case.

Both computations are verified against an explicit coordinate implementation
(see script output above): `(g∘f)(e) = (0,0,1) = e²` vs. `(g′∘f)(e) = (0,0,0) = 0`.

**This is a concrete, checkable divergence, not a speculative worry.** The
single natural candidate composite that a reader would use to test whether
"commuting with the induced transformation" is non-vacuous (option a) versus
degenerate to the trivial augmentation map (option c) gives *opposite
answers* depending on which of the two "equally valid" g's from the
statement is used. Using the stated g, the composite looks like solid
evidence against (c) (non-trivial induced map exists). Using the flagged
alternative g′, the *very same* composite construction *is* the (c)-style
degenerate map. The statement's own text ("noting g is non-canonical... an
equally valid alternative") flags this ambiguity as something to watch, but
the statement does not resolve which g is meant to be tested against
options (a)/(b)/(c), and the two choices are not interchangeable for that
purpose — they push toward opposite conclusions on exactly the axis the
statement asks to be resolved.

**Asymmetry note** (partial finding, worth carrying forward): the reverse
composite f∘g is trivial (=0 on m′) for *both* choices of g — because A has
m³=0 but A′ has m′²=0, and f kills exactly f(m²(A))=0, any valid g:A′→A
(image forced into m²(A) by the relations of A′) becomes killed by f
afterward regardless of the (λ,μ) chosen. So the ambiguity is invisible if
you only test f∘g, and only appears when testing g∘f. This means the
direction of composition used to probe (a)/(b)/(c) matters, and is itself
an implicit, unstated choice in the claim.

## 5. Effect on the (a)/(b)/(c) trichotomy
I did not attempt to resolve (a)/(b)/(c) — out of scope for a coherence
review and not requested. But the finding in §4 means the trichotomy, as
posed against *this specific pair* (f,g), is not yet well-typed: "does
requiring commutation with the induced transformations reduce to option (c)"
has different apparent answers depending on an arbitrary, unfixed choice
(which g among a continuum). Any argument in a later round that picks one g
silently and concludes (a) or (c) is at risk of having smuggled in the
answer via the choice of representative, rather than deriving it from the
non-isomorphism structure itself.

## ACQUISITION
Would like to ground the "Weil algebra homomorphism induces natural
transformation of Weil functors" construction against a citable source
(e.g., Kolář–Michor–Slovák §35, or Michor's lecture notes) — currently
flagged [UNVERIFIED], not invented, per repo instructions since no
references/ directory exists here.

## Audit scope
- Examined at full computational depth: well-definedness of f, g, g′;
  non-invertibility of f, g; the composites g∘f, g′∘f, f∘g, f∘g′.
- Examined at citation-recall depth only (not re-derived): the general
  theorem that Weil-algebra homomorphisms induce natural transformations of
  Weil functors on manifolds. Hypotheses of that construction were checked
  to hold for A, A′, f, g.
- Not examined: the (a)/(b)/(c) trichotomy's mathematical content itself —
  that is next-round argument content, not statement coherence. Also not
  examined: whether "commute with the induced transformation," as a
  property of a "method" (jet-transport-style operator), has a determinate
  meaning beyond the two example algebras — the statement explicitly scopes
  this round to the anchor pair, and I stayed within that scope.
