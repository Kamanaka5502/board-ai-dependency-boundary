"""Replay engine for Elyria Systems dependency boundary reviews.

The replay engine is the public proof surface for deterministic review comparison.
It does not expose protected substrate internals.
"""

from copy import deepcopy
from typing import Any, Dict, Iterable

from runtime.decision_engine import DependencyReview, classify
from runtime.receipt_generator import generate_receipt

TIMESTAMP_FIELDS = {"receipt_id", "review_date"}


def review_from_payload(payload: Dict[str, Any]) -> DependencyReview:
    """Build a DependencyReview from a mixed customer payload."""
    allowed = DependencyReview.__dataclass_fields__.keys()
    return DependencyReview(**{k: v for k, v in payload.items() if k in allowed})


def normalize_receipt(receipt: Dict[str, Any], exclude: Iterable[str] = TIMESTAMP_FIELDS) -> Dict[str, Any]:
    """Remove timestamp-derived fields so replay comparison is deterministic."""
    excluded = set(exclude)
    return {k: v for k, v in receipt.items() if k not in excluded}


def run_review(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Run classification and receipt generation for one payload."""
    review = review_from_payload(payload)
    decision = classify(review).result()
    receipt = generate_receipt(payload, decision)
    return {
        "decision": decision,
        "receipt": receipt,
        "normalized_receipt": normalize_receipt(receipt),
    }


def replay(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Run the same payload twice and report replay equality."""
    first = run_review(deepcopy(payload))
    second = run_review(deepcopy(payload))
    return {
        "replay_equal": first["decision"] == second["decision"]
        and first["normalized_receipt"] == second["normalized_receipt"],
        "first": first,
        "second": second,
    }


def replay_delta(before_payload: Dict[str, Any], after_payload: Dict[str, Any]) -> Dict[str, Any]:
    """Compare two payloads and expose decision movement."""
    before = run_review(deepcopy(before_payload))
    after = run_review(deepcopy(after_payload))
    return {
        "before_decision": before["decision"],
        "after_decision": after["decision"],
        "changed": before["decision"] != after["decision"],
        "before_receipt_digest": before["receipt"]["receipt_digest"],
        "after_receipt_digest": after["receipt"]["receipt_digest"],
    }
