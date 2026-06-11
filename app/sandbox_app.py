"""Customer sandbox app for Elyria Systems AI Dependency Boundary Assurance."""

from flask import Flask, jsonify, request

from runtime.decision_engine import DependencyReview, classify
from runtime.receipt_generator import generate_receipt

app = Flask(__name__)


@app.get("/")
def home():
    return jsonify({
        "system": "ELYRIA SYSTEMS",
        "product": "Board AI Dependency Boundary Review",
        "sandbox": "customer_playground",
        "status": "operational",
        "message": "Submit a dependency review to /sandbox/review.",
        "example_payload": {
            "name": "AI Claims Routing Assistant",
            "criticality": "critical",
            "consequence_classes": ["regulated", "customer"],
            "persistent_memory": True,
            "autonomous_execution": True,
            "cross_border_exposure": True,
            "authority_clear": False,
            "receipt_available": False,
            "replay_available": False,
            "exit_path_available": False,
            "conditions_changed": False,
            "existing_deployment": True
        }
    })


@app.post("/sandbox/review")
def sandbox_review():
    payload = request.get_json(force=True)
    review = DependencyReview(**payload)
    decision = classify(review)
    receipt = generate_receipt({
        "dependency_name": payload.get("name"),
        "vendor_provider": payload.get("vendor_provider", "sandbox_vendor"),
        "owner": payload.get("owner", "sandbox_owner"),
        "deployment_stage": payload.get("deployment_stage", "sandbox"),
        "criticality": payload.get("criticality"),
        "consequence_classes": payload.get("consequence_classes", []),
    }, decision)
    return jsonify({
        "decision": decision,
        "receipt": receipt,
        "buyer_rules": [
            "No receipt, no board assurance.",
            "No replay, no dependency confidence.",
            "No proof surface, no category claim."
        ]
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
