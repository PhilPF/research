# Melchior Review — jt-percoord — Round 1

## Subtask decomposition (priority order)

1. **[done]** Check whether the objects named in the statement (jet transport,
   Weil lift, Weil algebra, extension, "fibered") are pinned down anywhere in
   this thread, or whether the statement borrows them from an unstated
   background theory.
2. **[done]** Locate the specific point where "per-coordinate" independence and
   "fibered" combination could fail to compose into a single well-defined
   object — i.e., stress-test the *construction implied by the statement*,
   not a written proof (none exists).
3. **[partial]** Check whether the statement, once minimally formalized in the
   most charitable way, reduces to something trivial (e.g. n independent
   copies of the 1-D theory) or is genuinely new content.
4. **[untouched]** Compare against the literature notion of two-Weil-algebra
   fibered bundle functors (Kolář–Michor–Slovák style $T^{A,B}$ constructions
   for a fibered manifold $p:Y\to M$) to see whether "per-coordinate" is a
   known generalization or a new, unverified one. Flagged as untouched due to
   time; noted as a lead only.
5. **[untouched]** Check quantifier scope in the background paragraph ("for a
   large enough class of vector fields," "for all Weil algebras that make
   sense") — this concerns the *property* jet-transport-of-a-method, which is
   not yet defined, so I could not audit its quantifiers without inventing a
   definition on the reviewers' behalf. I flag this rather than silently
   supply one.

## Analysis

### 1. No fixed definitions — but this alone is not "the gap"

The prompt is explicit that no formal definition of jet transport, Weil
algebra, Weil lift, or "extension" exists yet in this repository. Per my
brief, the *absence* of a definition is a reportable fact, but by itself it
does not locate a gap in an inferential step — there is no step yet. So I
looked instead for whether the *statement itself*, read as a proposed
construction ("each coordinate is Weil-lifted independently rather than the
system sharing one global Weil algebra"), is even coherent as a target once
you try to write down the most natural version of it. That is where I found
a concrete break.

### 2. The concrete break: cross-coordinate terms have no home

Take the ordinary (global) Weil lift as the baseline, since that is the
notion being contrasted against ("rather than the system sharing one global
Weil algebra"). For a system on $\mathbb R^n$ with vector field
$F=(f_1,\dots,f_n)$ and a single Weil algebra $W=\mathbb R\oplus N$
($N$ nilpotent), the Weil functor lifts $\mathbb R^n$ to $W^n$ and lifts $F$
to $\hat F$ by substituting $W$-valued points into the (necessarily
polynomial/finite Taylor, since $N$ is nilpotent) expansion of each $f_i$.
Every $f_i$'s expansion and every substituted variable lives in the *same*
algebra $W$, so $\hat f_i(X_1,\dots,X_n)\in W$ is automatic.

Now impose "per-coordinate": assign a possibly distinct Weil algebra $W_j$ to
coordinate $x_j$, so the lifted state space is $W_1\times\cdots\times W_n$,
with $X_j = x_j + n_j$, $n_j\in N_j$. Consider the lifted value of coordinate
$i$'s vector field, $\hat f_i(X_1,\dots,X_n)$. Whenever $f_i$ genuinely
depends on $x_j$ for some $j\ne i$ (the generic, coupled case — e.g.
$f_1(x,y)=xy$), the Taylor expansion of $\hat f_i$ contains terms built from
$n_j\in N_j$ with $j\ne i$, and cross-products like $n_i n_j$. These live in
$W_i\otimes W_j$ (or a further quotient of it), **not** in $W_i$. But the
i-th fiber of the lifted state space is $W_i$, and (for this to be a flow on
$W_1\times\cdots\times W_n$ at all) $\dot X_i$ must be $W_i$-valued. So the
"per-coordinate fibered extension," applied to any vector field that is not
already diagonal ($f_i$ depending only on $x_i$), does not by itself specify
where the cross terms go: some map $W_i\otimes W_j \to W_i$ (or a
family of such compatibility maps between all the $W_j$'s and the ambient
structure) has to be supplied and is not part of what "per-coordinate,
independent Weil lift" says.

Concrete instance to make this checkable rather than assumed: let $n=2$,
$W_1=\mathbb R[e_1]/(e_1^2)$ (dual numbers — order-1 jet in $x$), and
$W_2=\mathbb R[e_2]/(e_2^3)$ (order-2 jet in $y$) — a genuinely
"per-coordinate" choice, since assigning *different* orders/algebras to
different coordinates is exactly the extra freedom the statement is
proposing. Take $F=(xy,\,x^2)$. Lifting coordinate 1:
$$\hat f_1(X,Y) = (x+e_1)(y+e_2\delta_1+e_2^2\delta_2)
 = xy + e_1 y + x e_2 \delta_1 + x e_2^2\delta_2 + e_1e_2\delta_1+e_1e_2^2\delta_2 .$$
The terms $e_1y$ and $x e_2\delta_1$ etc. are of different "type" ($e_1\in
N_1$ vs $e_2\in N_2$) and the sum is not an element of $W_1$ under any
map that has been specified — it is an element of $W_1\otimes W_2$ (mod
whatever ideal one chooses). Two different, equally "natural" choices for
discarding/projecting the mixed terms (e.g. project to $W_1$ by killing all
$e_2$-terms, vs. project by keeping only terms of total nilpotent-degree
$\le$ some bound) give **inequivalent** dynamics for $X_1(t)$, i.e.
inequivalent candidate meanings of "jet transport under a per-coordinate
extension." The statement as posed does not adjudicate between them, nor
does it note that such a choice must be made.

Two ways this could resolve, neither of which the statement addresses:
- If the intended scope is *only* diagonal/decoupled systems
  ($f_i=f_i(x_i)$), the per-coordinate construction is well-defined but
  trivially reduces to $n$ independent copies of the ordinary 1-D Weil lift,
  adding no new content beyond bookkeeping — this conflicts with the stated
  motivation ("jet transport is much more than what seems a priori," "a
  combination of all these facts"), which clearly intends nontrivial,
  coupled systems.
- If coupled systems are intended (the interesting case, and the case the
  broader "combination of facts" framing needs), an extra structure (some
  compatibility/comparison maps among the $W_j$, or a single ambient algebra
  they all embed in) is required to even state what $\hat F$ is, and this
  structure is exactly what "fibered extension" would need to supply but
  currently does not.

This is the located gap: **the phrase "per-coordinate fibered extension"
presupposes a well-defined lift of a general (coupled) vector field once
each coordinate has its own Weil algebra, but no map handling
cross-coordinate nilpotent terms is specified, and the natural candidates
are inequivalent.** It sits prior to any question of whether "jet
transport" (whatever property that turns out to mean) holds for a "large
class" of vector fields — the object the property would be asserted of is
not yet pinned down for the general (coupled) case that motivates the
question in the first place.

### 3. Secondary observation (not the primary gap, flagged for the record)

The background text treats "jet transport" as a property of a *method*
holding for a *class* of vector fields, universally quantified over Weil
algebras "that make sense," and asks whether the same game can be played for
extensions w.r.t. parameters, time, initial value, nested extensions, and
same-dimension-but-non-isomorphic algebras. None of "method," "holds for a
vector field," or "makes sense" (for an extension) are defined in this
thread. I did not attempt to invent these definitions and audit their
quantifiers, since doing so would mean supplying the missing content myself
rather than reporting the gap — flagged as `untouched` rather than assumed
innocuous.

## Audit scope

Examined at depth: the internal coherence of "per-coordinate fibered
extension" as a would-be generalization of the single-global-Weil-algebra
lift, for both diagonal and coupled vector fields, including one worked
concrete instance (2-D system, two distinct Weil algebras). Not examined:
literature comparison to two-algebra fibered-bundle Weil functors (KMS-style
$T^{A,B}$), the nested-extension and same-dimension-isomorphic-algebra
variants raised in the background paragraph, and the quantifier structure of
"jet transport" as a method-property (since that notion is undefined here).
These are carried forward as untouched/partial, not certified clean.
