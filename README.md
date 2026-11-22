

# Metamathematics in modal logic

Gödel shocked the world of mathematics by showing that formal proofs of number theory could be done within number theory itself.
Sentences and proofs could be coded as numbers, and correctness of a proof was a number theoretic property.
Furthermore, sentences could refer to their own properties, by the trick we now call quining.
From there, he could demonstrate that number theory, if consistent, must be incomplete.

In my opinion, the profound insights here were about self-reference: that number theory could represent its own rules, and that sentences could refer to themselves.
From there to the consequences about incompleteness is straightforward.

Not just straightforward: it’s mechanical, with modal logic.

My goal in this post is to show you the arguments of metamathematics that can be formalized in the modal logic $\mathrm{K4}$.
By the end we’ll also see what’s missing, and I’ll show how to complete the system in the next post.
But already in $\mathrm{K4}$ we can reason through Gödel’s first and second incompleteness theorems.
In fact, I actually never managed to follow the second incompleteness theorem before I learned to do it in $\mathrm{K4}$.

## Provability and possibility

Modal logic was developed by philosophers to formalize arguments about the concepts of necessity and possibility.

The new symbols are a box and a diamond. $\Box P$ means necessarily $P$, and $\Diamond P$ means possibly $P$.

To do metamathematics in modal logic, we instead interpret $\Box P$ in terms of provability.
We will assume a formal system $\mathrm{PA}$ for first-order Peano arithmetic.
Such a system has a provability predicate $\mathrm{Prov}(\ulcorner A \urcorner)$ representing the provability of the sentence $A$ (where $\ulcorner A \urcorner$ is the numeric Gödel code of the sentence).
We will interpret a sentence $\Box P$ by replacing the letter $P$ with some sentence $A$ of Peano arithmetic, and interpreting $\Box P$ as $\mathrm{Prov}(\ulcorner A \urcorner)$.

I’ll avoid the possibility operator to keep things simple, except to note that I think the provability interpretation of “possibility” fits well with the English word.
In modal logic, the relationship of necessity and possibility is that $\Diamond P$ iff $\lnot \Box \lnot P$.
Interpreting the box as provability, then our diamond means that there’s no disproof of $P$.
That does intuitively mean it’s possibly true.
Gödel’s surprise, then, was that if number theory is consistent, there must be a sentence in the language of number theory that is possible but not provable.

## The requirements for a provability predicate

[There are standard conditions a provability predicate must satisfy](https://en.wikipedia.org/wiki/Hilbert%E2%80%93Bernays%E2%80%93L%C3%B6b_provability_conditions#The_conditions).
As it turns out, these precisely match the system of modal logic known to philosophers as $\mathrm{K4}$.

## Writing things modally

I’ll make a few abbreviations to write out valid arguments in $\mathrm{K4}$.

I’ll write premises above a line and conclusions below it:

$$\frac{\begin{gathered}P_1\\P_2\end{gathered}}{C}$$

This means $\mathrm{K4}\vdash (P_1 \land P_2) \to C$.

$\boxdot A$ means $A \land \Box A$.
Well we want to make an argument from some sentence that is true in PA, we’ll always represent it like this.
You’ll see a why later.

The first incompleteness theorem, for a Gödel sentence $\gamma$:

$$\frac{\begin{gathered}\boxdot(\gamma \leftrightarrow \lnot\Box\gamma) \\ \lnot\Box\bot\end{gathered}}{\gamma}$$

And also (since the conclusion is equivalent):

$$\frac{\begin{gathered}\boxdot(\gamma \leftrightarrow \lnot\Box\gamma) \\ \lnot\Box\bot\end{gathered}}{\lnot\Box\gamma}$$

## How it applies to $\mathrm{PA}$

If $\mathrm{PA}$ is consistent, the Gödel sentence is true, and unprovable.
That’s what we want to say, but so far all we have is a theorem of the modal logic $\mathrm{K4}$.
From there though we can get a theorem of $\mathrm{PA}$.

Remember, $\gamma$ is just a symbol, a “sentence letter” as we call it, a fundamental unit of our language of modal logic.
We’re going to interpret our sentences of modal logic.
That has a technical meaning: we’ll replace each sentence letter with a sentence of PA, and translate boxes as provability predicates.

Let $G$ be the Gödel sentence $\mathrm{PA}$.
In $\mathrm{PA}$ we have:
$$\mathrm{PA}\vdash G \leftrightarrow \lnot\mathrm{Prov}(\ulcorner G \urcorner)$$

And furthermore—this is why it’s fine that we put $\boxdot$ in front of our premise:

$$\mathrm{PA}\vdash \mathrm{Prov}\bigl(\ulcorner G \leftrightarrow \lnot\mathrm{Prov}(\ulcorner G \urcorner) \urcorner\bigr)$$

Any $\mathrm{PA}$ theorem can be wrapped in a provability predicate like that.
A theorem of $\mathrm{PA}$ has a proof, and that proof has a Gödel code.
Or maybe I should just say it’s one of the conditions mentioned earlier.

All theorems of $\mathrm{K4}$, when interpreted, are theorems of $\mathrm{PA}$.
Interpreting our $\mathrm{K4}$ formalization of Gödel’s first incompleteness theorem:

$$\mathrm{PA}\vdash \boxdot(G \leftrightarrow \lnot\mathrm{Prov}(\ulcorner G \urcorner)) \land \lnot\mathrm{Prov}(\ulcorner 0=1 \urcorner) \to G$$

We could have replaced $\gamma$ with any $\mathrm{PA}$ sentence and gotten a $\mathrm{PA}$ theorem, but what’s special about replacing it with $G$ is is that now, putting those two $\mathrm{PA}$ theorems together, we hvae

$$\mathrm{PA}\vdash \lnot\mathrm{Prov}(\ulcorner 0=1 \urcorner) \to G$$

That is, $\mathrm{PA}$, augmented with its own consistency as an assumption, does prove $G$.

## The second incompleteness theorem

I don’t think we really needed modal logic to understand that.
But here’s something that I got for the first time as a modal logic argument.
In $\mathrm{K4}$:
$$ \frac{\begin{gathered}\boxdot(\gamma \leftrightarrow \lnot\Box\gamma) \\ \lnot\Box\bot\end{gathered}}{\lnot\Box\lnot\Box\bot} $$

I don’t want to go through the proof right now, I just want to show you how far $\mathrm{K4}$ can take you.
But doing this proof in $\mathrm{K4}$ was my first real experience of the power of modal logic to track quotation levels that I can’t track in my head.

But it’s not satisfactory.
Why does the Gödel sentence have to appear in the premises if it’s not part of the conclusion?

We want just
$$ \frac{\begin{gathered}\lnot\Box\bot\end{gathered}}{\lnot\Box\lnot\Box\bot} $$

And in fact, in PA we have:
$$ \mathrm{PA}\vdash \lnot\Box\bot \to \lnot\Box\lnot\Box\bot $$

$\mathrm{K4}$ cannot prove all the metamathematical statements we want.
Next part we’ll see what we need to add.
