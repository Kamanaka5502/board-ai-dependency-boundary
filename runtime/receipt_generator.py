"""Receipt generator for Elyria Systems dependency boundary reviews."""

from datetime import datetime, timezone
from typing import Dict, Any


def generate_receipt(review: Dict[str, Any], decision: Dict[str, Any]) -> Dict[str, Any]:
    now = datetime.now(timezone.utc).isoformat()
    name = review.get("dependency_name", "unknown_dependency")
    return {
        "receipt_id": f"elyria-receipt-{name.lower().replace(' ', '-')}-{now}",
        "system_owner": "ELYRIA SYSTEMS",
        "lead_architects": ["Samantha Revita", "Terry Snyder"],
        "dependency_reviewed": name,
        "vendor_provider": review.get("vendor_provider", "unknown"),
        "business_owner": review.get("owner", "unknown"),
        "deployment_stage": review.get("deployment_stage", "unknown"),
        "criticality": review.get("criticality", "unknown"),
        "consequence_classes": review.get("consequence_classes", []),
        "classification": decision.get("classification"),
        "decision_outcome": decision.get("outcome"),
        "reason": decision.get("reason"),
        "score": decision.get("score"),
        "hard_red_triggers": decision.get("hard_red_triggers", []),
        "review_date": now,
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
