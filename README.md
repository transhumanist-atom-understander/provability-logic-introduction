

# Metamathematics in modal logic

To do metamathematics in modal logic, you take for granted all of Gödel’s great insights:

- That when formal proofs are represented as numbers, correctness of a proof can be defined in the language of number theory

- That a sentence can refer to itself by the trick we now call “diagonalization” or “quining”

Once you have Gödel’s sentence that says “I am not provable”, the interesting conceptual work is done.

The remaining part, from there to the incompleteness theorems, is rather mechanical.
In modal logic, these arguments become fully mechanical.
To me at least, it is appealing to be able to compute from the Gödel sentence to the unprovability of the consistency of arithmetic by a procedure as algorithmic as long division.

## Provability and possibility

Modal logic was developed by philosophers to formalize arguments about the concepts of necessity and possibility.

The new symbols are a box and a diamond. $\Box P$ means necessarily $P$, and $\Diamond P$ means possibly $P$.

To do metamathematics in modal logic, we instead interpret $\Box P$ in terms of provability.
We will assume a formal system $\mathrm{PA}$ for first-order Peano arithmetic.
Such a system has a provability predicate $\mathrm{Prov}(\ulcorner A \urcorner)$ representing the provability of the sentence $A$, where $\ulcorner A \urcorner$ is the numeric Gödel code of the sentence.
We will interpret a sentence $\Box P$ by replacing the sentence $P$ with some sentence $A$ of Peano arithmetic, and interpreting $\Box P$ as $\mathrm{Prov}(\ulcorner A \urcorner)$.

I’ll avoid the possibility operator to keep things simple, except to note that I think the provability interpretation of “possibility” fits well with the English word.
In modal logic, the relationship of necessity and possibility is that $\Diamond P$ iff $\lnot \Box \lnot P$.
Interpreting the box as provability, our notion of possibility is that there’s no disproof of $P$.

As it turns out, [the standard conditions a provability predicate must satisfy](https://en.wikipedia.org/wiki/Hilbert%E2%80%93Bernays%E2%80%93L%C3%B6b_provability_conditions#The_conditions) precisely match the axioms of a system of modal logic, known to philosophers as $\mathrm{K4}$.

## The Gödel sentence and consistency as sentences of modal logic

The Gödel sentence will appear in modal logic as a sentence equivalent to its own unprovability:

```math
\gamma \leftrightarrow \lnot\Box\gamma
```

$\gamma$ is just an elementary symbol of the logic, a “sentence letter” as some say.
I’ll be putting sentence letters in lowercase, whereas arbitrary sentences are uppercase.

The logic also has a symbol $\bot$ representing falsehood, equivalent to propositional contradictions like $p \land \lnot p$.
Our modal analogue of consistency is the claim that $\bot$ has no proof: $\lnot\Box\bot$.

## A modal logic analogue of the first incompleteness theorem

I won’t give any proofs of $\mathrm{K4}$ theorems.
We’ll just talk about what metamathematical arguments can be made in it, and what’s missing.

I’ll write premises above a line and conclusions below it:

```math
\frac{\begin{gathered}P_1\\P_2\end{gathered}}{C}
```

This means $\mathrm{K4}\vdash (P_1 \land P_2) \to C$.

Another abbreviation: $\boxdot A$ means $A \land \Box A$.

A modal logic analogue of the first incompleteness theorem:

```math
\frac{\begin{gathered}\boxdot(\gamma \leftrightarrow \lnot\Box\gamma) \\ \lnot\Box\bot\end{gathered}}{\gamma}
```

This is in fact a theorem of $\mathrm{K4}$.

And also (since the conclusion is equivalent):

```math
\frac{\begin{gathered}\boxdot(\gamma \leftrightarrow \lnot\Box\gamma) \\ \lnot\Box\bot\end{gathered}}{\lnot\Box\gamma}
```

That appears to say that, if $\gamma$ is a sentence asserting its own unprovability, then, assuming consistency, it is both true and unprovable.

## What we want is a $\mathrm{PA}$ theorem

So far all we have are theorems of modal logic onto which we can project metamathematical interpretations.

But the power of our modal logic is its *arithmetic soundness*: that whatever we prove in $\mathrm{K4}$ becomes a theorem of $\mathrm{PA}$ under any interpretation.

Before getting into how that works, let’s start with what $\mathrm{PA}$ theorems we might like to have.

We already have, for the sentence $G$ constructed according to Gödel’s recipe:

```math
\mathrm{PA}\vdash G \leftrightarrow \lnot\mathrm{Prov}(\ulcorner G \urcorner)
```

One thing we want to say is that $\mathrm{PA}$, augmented with the assumption of its own consistency, does in fact prove $G$:

```math
\mathrm{PA}\vdash \lnot\mathrm{Prov}(\ulcorner 0=1 \urcorner) \to G
```

## From $\mathrm{K4}$ to $\mathrm{PA}$

We’re going to interpret our sentences of modal logic.
That has a technical meaning: we’ll replace each sentence letter with a sentence of $\mathrm{PA}$, translate boxes to provability predicates, and translate all instances of $\bot$ to $0=1$.

Interpreting our $\mathrm{K4}$ formalization of Gödel’s first incompleteness theorem, replacing the sentence letter $\gamma$ with the complicated $\mathrm{PA}$ sentence $G$:

```math
\mathrm{PA}\vdash ((G \leftrightarrow \lnot\mathrm{Prov}(\ulcorner G \urcorner)) \land \mathrm{Prov}(\ulcorner G \leftrightarrow \lnot\mathrm{Prov}(\ulcorner G \urcorner) \urcorner) \land \lnot\mathrm{Prov}(\ulcorner 0=1 \urcorner)) \to G
```

On the left side of that implication, we see one thing that we have in $\mathrm{PA}$, that $G \leftrightarrow \lnot\mathrm{Prov}(\ulcorner G \urcorner)$.

In fact, we also have the next term:

```math
\mathrm{PA}\vdash \mathrm{Prov}\bigl(\ulcorner G \leftrightarrow \lnot\mathrm{Prov}(\ulcorner G \urcorner) \urcorner\bigr)
```

Any $\mathrm{PA}$ theorem can be wrapped in a provability predicate like this.
If it’s a theorem, then it has a proof, and we can Gödel code that proof.
This is also one of [the standard conditions for a provability predicate mentioned earlier](https://en.wikipedia.org/wiki/Hilbert%E2%80%93Bernays%E2%80%93L%C3%B6b_provability_conditions#The_conditions).

Since we have this implication by arithmetic soundness of $\mathrm{K4}$, and we have those first two terms of the antecedent, then we have what we wanted in $\mathrm{PA}$, to repeat:

```math
\mathrm{PA}\vdash \lnot\mathrm{Prov}(\ulcorner 0=1 \urcorner) \to G
```

## The second incompleteness theorem

I don’t think we really needed modal logic to understand that.
But here’s something that I got for the first time as a modal logic argument.
In $\mathrm{K4}$:

```math
\frac{\begin{gathered}\boxdot(\gamma \leftrightarrow \lnot\Box\gamma) \\ \lnot\Box\bot\end{gathered}}{\lnot\Box\lnot\Box\bot}
```

I don’t want to go through the proof right now, I just want to show you how far $\mathrm{K4}$ can take you.
But doing this proof in $\mathrm{K4}$ was my first real experience of the power of modal logic to track quotation levels that I can’t track in my head.

But it’s not satisfactory.
Why does the Gödel sentence have to appear in the premises if it’s not part of the conclusion?

We want just

```math
\frac{\begin{gathered}\lnot\Box\bot\end{gathered}}{\lnot\Box\lnot\Box\bot}
```

And in fact, in $\mathrm{PA}$ we have:

```math
\mathrm{PA}\vdash \lnot\mathrm{Prov}(\ulcorner 0=1 \urcorner) \to \lnot\mathrm{Prov}\bigl(\ulcorner \lnot\mathrm{Prov}(\ulcorner 0=1 \urcorner) \urcorner\bigr)
```

$\mathrm{K4}$ cannot prove all the metamathematical statements we want.
Next part we’ll see what we need to add.
