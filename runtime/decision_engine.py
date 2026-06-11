"""Board AI Dependency Boundary decision engine.

Minimal operational classifier for load-bearing AI dependency review.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any


HIGH_CONSEQUENCE = {
    "financial",
    "clinical",
    "legal",
    "regulated",
    "cyber",
    "customer",
    "sovereign",
}


@dataclass
class DependencyReview:
    name: str
    criticality: str = "unknown"
    consequence_classes: List[str] = field(default_factory=list)
    persistent_memory: bool = False
    autonomous_execution: bool = False
    cross_border_exposure: bool = False
    authority_clear: bool = False
    receipt_available: bool = False
    replay_available: bool = False
    exit_path_available: bool = False
    conditions_changed: bool = False
    existing_deployment: bool = False


def classify(review: DependencyReview) -> Dict[str, Any]:
    """Classify dependency and return board-facing outcome."""

    consequence = {c.lower() for c in review.consequence_classes}
    high_consequence = bool(consequence & HIGH_CONSEQUENCE)

    red_triggers = [
        review.criticality.lower() == "structural",
        high_consequence and not review.authority_clear,
        review.autonomous_execution and high_consequence,
        review.cross_border_exposure and not review.authority_clear,
        not review.exit_path_available and review.criticality.lower() in {"critical", "structural"},
        not review.receipt_available and high_consequence,
        not review.replay_available and high_consequence,
    ]

    yellow_triggers = [
        review.criticality.lower() in {"important", "critical"},
        review.persistent_memory,
        review.autonomous_execution,
        review.cross_border_exposure,
        review.conditions_changed,
    ]

    if review.conditions_changed:
        return result("yellow", "revalidate", "Conditions changed; prior approval is no longer sufficient.")

    if any(red_triggers):
        if review.existing_deployment:
            return result("red", "halt", "Existing dependency is structurally unsafe, unauthorized, or insufficiently reviewable.")
        return result("red", "escalate", "Load-bearing consequence exposure requires board or authority escalation.")

    if any(yellow_triggers):
        return result("yellow", "narrow", "Dependency is emerging as load-bearing and must proceed only under bounded scope.")

    return result("green", "admit", "Dependency appears bounded, reversible, and non-structural.")


def result(classification: str, outcome: str, reason: str) -> Dict[str, str]:
    return {
        "classification": classification,
        "outcome": outcome,
        "reason": reason,
        "receipt_rule": "No receipt, no board assurance.",
        "replay_rule": "No replay, no dependency confidence.",
    }


if __name__ == "__main__":
    sample = DependencyReview(
        name="Example AI Agent Runtime",
        criticality="critical",
        consequence_classes=["cyber", "customer"],
        persistent_memory=True,
        autonomous_execution=True,
        authority_clear=False,
        receipt_available=False,
        replay_available=False,
        exit_path_available=False,
    )
    print(classify(sample))
