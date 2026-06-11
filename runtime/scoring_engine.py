"""Scoring engine for Elyria Systems AI Dependency Boundary Assurance."""

from dataclasses import dataclass
from typing import Dict, List, Any

DIMENSIONS = [
    "authority",
    "retention",
    "jurisdiction",
    "consequence",
    "reversibility",
    "exit",
    "receipt",
    "replay",
]

WEIGHTS = {
    "authority": 1.3,
    "retention": 1.3,
    "jurisdiction": 1.1,
    "consequence": 1.5,
    "reversibility": 1.2,
    "exit": 1.2,
    "receipt": 1.0,
    "replay": 1.2,
}


@dataclass
class BoundaryScore:
    scores: Dict[str, int]
    hard_red_triggers: List[str]


def weighted_average(scores: Dict[str, int]) -> float:
    total_weight = 0.0
    total = 0.0
    for dimension in DIMENSIONS:
        value = scores.get(dimension, 0)
        weight = WEIGHTS[dimension]
        total += value * weight
        total_weight += weight
    return round(total / total_weight, 2)


def classify_score(boundary: BoundaryScore) -> Dict[str, Any]:
    avg = weighted_average(boundary.scores)

    if boundary.hard_red_triggers:
        return {
            "classification": "red",
            "outcome": "escalate_or_halt",
            "score": avg,
            "hard_red_triggers": boundary.hard_red_triggers,
            "reason": "Hard red trigger present. Boundary cannot be treated as ordinary approval.",
        }

    if avg >= 3.1:
        return {
            "classification": "green",
            "outcome": "admit",
            "score": avg,
            "reason": "Boundary appears documented, verified, and sufficiently replayable.",
        }

    if avg >= 2.0:
        return {
            "classification": "yellow",
            "outcome": "narrow_or_revalidate",
            "score": avg,
            "reason": "Boundary is partially documented but not yet strong enough for structural admission.",
        }

    return {
        "classification": "red",
        "outcome": "refuse_or_halt",
        "score": avg,
        "reason": "Boundary evidence is insufficient for load-bearing dependency admission.",
    }


if __name__ == "__main__":
    demo = BoundaryScore(
        scores={
            "authority": 1,
            "retention": 1,
            "jurisdiction": 1,
            "consequence": 3,
            "reversibility": 1,
            "exit": 1,
            "receipt": 0,
            "replay": 0,
        },
        hard_red_triggers=["persistent_memory_without_retention_control"],
    )
    print(classify_score(demo))
