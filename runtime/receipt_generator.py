"""Receipt generator for Elyria Systems dependency boundary reviews."""

from datetime import datetime, timezone
import hashlib
import json
from typing import Any, Dict


def canonicalize_payload(payload: Dict[str, Any]) -> str:
    """Return deterministic JSON for receipt digest and replay comparison."""
    return json.dumps(payload, sort_keys=True, separators=(",", ":"), default=str)


def compute_receipt_digest(review: Dict[str, Any], decision: Dict[str, Any]) -> str:
    """Compute a SHA-256 digest over the review and decision proof surface."""
    digest_payload = {
        "review": review,
        "decision": decision,
    }
    canonical = canonicalize_payload(digest_payload)
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def generate_receipt(review: Dict[str, Any], decision: Dict[str, Any]) -> Dict[str, Any]:
    now = datetime.now(timezone.utc).isoformat()
    name = review.get("dependency_name", "unknown_dependency")
    outcome = decision.get("outcome")
    classification = decision.get("classification")
    is_admitted = classification == "green" and outcome == "admit"

    receipt = {
        "receipt_id": f"elyria-receipt-{name.lower().replace(' ', '-')}-{now}",
        "system_owner": "ELYRIA SYSTEMS",
        "lead_architects": ["Samantha Revita", "Terry Snyder"],
        "dependency_reviewed": name,
        "vendor_provider": review.get("vendor_provider", "unknown"),
        "business_owner": review.get("owner", "unknown"),
        "deployment_stage": review.get("deployment_stage", "unknown"),
        "criticality": review.get("criticality", "unknown"),
        "consequence_classes": review.get("consequence_classes", []),
        "classification": classification,
        "decision_outcome": outcome,
        "reason": decision.get("reason"),
        "score": decision.get("score"),
        "hard_red_triggers": decision.get("hard_red_triggers", []),
        "review_date": now,
        "receipt_digest": compute_receipt_digest(review, decision),
        "admit_token": f"elyria-admit-{name.lower().replace(' ', '-')}" if is_admitted else None,
        "proceed_authorization": is_admitted,
        "no_effect_rule": "No admit token or proceed authorization is issued unless classification is green and outcome is admit.",
        "receipt_rule": "No receipt, no board assurance.",
        "replay_rule": "No replay, no dependency confidence.",
        "next_revalidation_triggers": [
            "vendor_change",
            "model_change",
            "retention_change",
            "jurisdiction_change",
            "api_or_tool_permission_change",
            "agent_autonomy_change",
            "expanded_use_case",
            "incident_or_near_miss",
            "regulatory_change",
        ],
    }
    return receipt
