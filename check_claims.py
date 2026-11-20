"""Check the slides' claims of theoremhood and non-theoremhood in GL and R⁻.

Each rule of the slides, premises over a conclusion, is checked as the implication from the
conjunction of the premises to the conclusion. The claims about K and K4 are not checked: the
decider decides GL and R⁻ only.

The Lean project decide-provability is found at $DECIDE_PROVABILITY:

    $ DECIDE_PROVABILITY=/path/to/decide-provability uv run check_claims.py
"""

import os
import sys

from rtableau import Decider

GODEL = "⊡(q ↔ ¬□q)"
LOB = "⊡(L ↔ (□L → P))"
ROSSER = "⊡(R ↔ □¬R ≺ □R)"

# (sentence, whether it is claimed to be a theorem, where the slides claim it)
CLAIMS = [
    # Part 1: the Gödel sentence
    (f"{GODEL} ∧ ¬□⊥ → q", True, "Part 1: the Gödel sentence is true"),
    (f"{GODEL} ∧ ¬□⊥ → ¬□q", True, "Part 1: the Gödel sentence is unprovable"),
    # Part 2: provability logic
    (f"{GODEL} ∧ ¬□⊥ → ¬□¬□⊥", True, "Part 2: second incompleteness from the Gödel sentence"),
    ("¬□⊥ → ¬□¬□⊥", True, "Part 2: second incompleteness"),
    (f"{LOB} ∧ □(□P → P) → □P", True, "Part 2: Löb's theorem from the Löb sentence"),
    ("□(□P → P) → □P", True, "Part 2: Löb's axiom"),
    # Part 3: Rosser's trick
    (f"{GODEL} ∧ ¬□⊥ → ¬□¬q", False, "Part 3: the Gödel sentence is not shown irrefutable"),
    (f"{ROSSER} ∧ □¬R ∧ ¬□⊥ → R", True, "Part 3: if R is refutable, R is true"),
    (f"{ROSSER} ∧ ¬□⊥ ∧ □R → ¬R", True, "Part 3: if R is provable, R is false"),
    (f"{ROSSER} ∧ ¬□⊥ → ¬□R ∧ ¬□¬R", True, "Part 3: R is undecidable"),
    # crossed out in the notes, and not on the slides
    (f"{ROSSER} → □¬R", False, "Notes, crossed out: R is refutable"),
]


def main():
    project = os.environ.get("DECIDE_PROVABILITY")
    if not project:
        sys.exit("Set $DECIDE_PROVABILITY to a checkout of the Lean project decide-provability")
    wrong = 0
    with Decider(project) as d:
        for sentence, claimed, where in CLAIMS:
            theorem = d.closed(d.tableau(sentence))
            ok = theorem == claimed
            wrong += not ok
            verdict = "theorem" if theorem else "not a theorem"
            print(f"{'ok   ' if ok else 'WRONG'}  {verdict:13}  {sentence}    [{where}]")
    print(f"\n{len(CLAIMS) - wrong} of {len(CLAIMS)} claims hold")
    sys.exit(1 if wrong else 0)


if __name__ == "__main__":
    main()
