from runtime.decision_engine import DependencyReview, classify
from runtime.receipt_generator import compute_receipt_digest, generate_receipt


def _review_payload(**overrides):
    payload = {
        "name": "Internal Copilot",
        "dependency_name": "Internal Copilot",
        "criticality": "optional",
        "consequence_classes": ["internal"],
        "persistent_memory": False,
        "autonomous_execution": False,
        "cross_border_exposure": False,
        "authority_clear": True,
        "receipt_available": True,
        "replay_available": True,
        "exit_path_available": True,
        "conditions_changed": False,
        "existing_deployment": False,
    }
    payload.update(overrides)
    return payload


def _decision_from_payload(payload):
    review = DependencyReview(**{k: v for k, v in payload.items() if k in DependencyReview.__dataclass_fields__})
    return classify(review)


def _normalized_receipt(receipt):
    excluded = {"receipt_id", "review_date"}
    return {k: v for k, v in receipt.items() if k not in excluded}


def test_same_payload_replays_same_decision_and_receipt_digest():
    payload = _review_payload()

    decision_one = _decision_from_payload(payload)
    decision_two = _decision_from_payload(payload)

    receipt_one = generate_receipt(payload, decision_one)
    receipt_two = generate_receipt(payload, decision_two)

    assert decision_one == decision_two
    assert receipt_one["receipt_digest"] == receipt_two["receipt_digest"]
    assert _normalized_receipt(receipt_one) == _normalized_receipt(receipt_two)


def test_changed_conditions_trigger_revalidation_delta():
    original_payload = _review_payload(conditions_changed=False)
    changed_payload = _review_payload(conditions_changed=True)

    original_decision = _decision_from_payload(original_payload)
    changed_decision = _decision_from_payload(changed_payload)

    assert original_decision["outcome"] == "admit"
    assert changed_decision["outcome"] == "revalidate"
    assert changed_decision["classification"] == "yellow"


def test_receipt_digest_changes_when_review_changes():
    original_payload = _review_payload()
    changed_payload = _review_payload(persistent_memory=True)

    original_decision = _decision_from_payload(original_payload)
    changed_decision = _decision_from_payload(changed_payload)

    assert compute_receipt_digest(original_payload, original_decision) != compute_receipt_digest(changed_payload, changed_decision)


def test_red_dependency_issues_no_admit_token_or_proceed_authorization():
    payload = _review_payload(
        name="Clinical Agent",
        dependency_name="Clinical Agent",
        criticality="critical",
        consequence_classes=["clinical"],
        autonomous_execution=True,
        authority_clear=False,
        receipt_available=False,
        replay_available=False,
        exit_path_available=False,
        existing_deployment=True,
    )

    decision = _decision_from_payload(payload)
    receipt = generate_receipt(payload, decision)

    assert decision["classification"] == "red"
    assert decision["outcome"] == "halt"
    assert receipt["admit_token"] is None
    assert receipt["proceed_authorization"] is False
