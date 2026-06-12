"""Customer sandbox app for Elyria Systems AI Dependency Boundary Assurance."""

from flask import Flask, jsonify, request

from runtime.decision_engine import DependencyReview, classify
from runtime.receipt_generator import generate_receipt
from runtime.replay_engine import replay, replay_delta

app = Flask(__name__)


@app.get("/")
def home():
    return jsonify({
        "system": "ELYRIA SYSTEMS",
        "product": "Board AI Dependency Boundary Review",
        "sandbox": "customer_playground",
        "status": "operational",
        "deployment_boundary": "sandbox_only_not_production_enforcement",
        "message": "Submit a dependency review to /sandbox/review. Replay proof is available at /sandbox/replay and /sandbox/replay-delta.",
        "endpoints": {
            "review": "POST /sandbox/review",
            "replay": "POST /sandbox/replay",
            "replay_delta": "POST /sandbox/replay-delta"
        },
        "example_payload": {
            "name": "AI Claims Routing Assistant",
            "dependency_name": "AI Claims Routing Assistant",
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
    review = DependencyReview(**{k: v for k, v in payload.items() if k in DependencyReview.__dataclass_fields__})
    decision = classify(review).result()
    receipt = generate_receipt({
        **payload,
        "dependency_name": payload.get("dependency_name", payload.get("name")),
        "vendor_provider": payload.get("vendor_provider", "sandbox_vendor"),
        "owner": payload.get("owner", "sandbox_owner"),
        "deployment_stage": payload.get("deployment_stage", "sandbox"),
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


@app.post("/sandbox/replay")
def sandbox_replay():
    payload = request.get_json(force=True)
    return jsonify(replay(payload))


@app.post("/sandbox/replay-delta")
def sandbox_replay_delta():
    payload = request.get_json(force=True)
    return jsonify(replay_delta(payload["before"], payload["after"]))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
