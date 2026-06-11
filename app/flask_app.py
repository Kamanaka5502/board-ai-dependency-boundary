"""Starter Flask app for Board AI Dependency Boundary review."""

from flask import Flask, jsonify, request
from runtime.decision_engine import DependencyReview, classify

app = Flask(__name__)


@app.get("/")
def index():
    return {
        "name": "Board AI Dependency Boundary",
        "promise": "No receipt, no board assurance. No replay, no dependency confidence.",
        "outcomes": ["admit", "narrow", "escalate", "refuse", "halt", "revalidate"],
    }


@app.post("/classify")
def classify_dependency():
    payload = request.get_json(force=True)
    review = DependencyReview(**payload)
    return jsonify(classify(review))


if __name__ == "__main__":
    app.run(debug=True)
