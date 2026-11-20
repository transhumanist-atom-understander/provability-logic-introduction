import os

from rtableau import Decider

GODEL = "⊡(γ ↔ ¬□γ)"
ROSSER = "⊡(ρ ↔ □¬ρ ≺ □ρ)"

# (sentence, whether it is claimed to be a theorem)
CLAIMS = [
    ("¬□⊥ → ¬□¬□⊥", True),
    (f"({GODEL} ∧ ¬□⊥) → ¬□¬γ", False),
    (f"({ROSSER} ∧ ¬□⊥) → ¬□ρ ∧ ¬□¬ρ", True)
]

project = os.environ.get("DECIDE_PROVABILITY")
assert project is not None
with Decider(project) as d:
    for sentence, claimed in CLAIMS:
        is_theorem = d.closed(d.tableau(sentence))
        result_string = 'is a theorem' if is_theorem else 'is not a theorem'
        print(f'{sentence} {result_string}')
        assert is_theorem == claimed
