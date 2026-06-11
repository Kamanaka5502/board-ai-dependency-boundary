from runtime.decision_engine import DependencyReview, classify


def test_bounded_internal_dependency_admits():
    review = DependencyReview(
        name="Internal Drafting Copilot",
        criticality="optional",
        consequence_classes=["internal"],
        persistent_memory=False,
        autonomous_execution=False,
        cross_border_exposure=False,
        authority_clear=True,
        receipt_available=True,
        replay_available=True,
        exit_path_available=True,
        conditions_changed=False,
        existing_deployment=False,
    )
    decision = classify(review)
    assert decision["classification"] == "green"
    assert decision["outcome"] == "admit"


def test_important_internal_dependency_narrows():
    review = DependencyReview(
        name="Team Productivity Assistant",
        criticality="important",
        consequence_classes=["internal"],
        persistent_memory=False,
        autonomous_execution=False,
        cross_border_exposure=False,
        authority_clear=True,
        receipt_available=True,
        replay_available=True,
        exit_path_available=True,
        conditions_changed=False,
        existing_deployment=False,
    )
    decision = classify(review)
    assert decision["classification"] == "yellow"
    assert decision["outcome"] == "narrow"


def test_red_dependency_halts_when_existing_deployment():
    review = DependencyReview(
        name="AI Claims Routing Assistant",
        criticality="critical",
        consequence_classes=["regulated", "customer"],
        persistent_memory=True,
        autonomous_execution=True,
        cross_border_exposure=True,
        authority_clear=False,
        receipt_available=False,
        replay_available=False,
        exit_path_available=False,
        conditions_changed=False,
        existing_deployment=True,
    )
    decision = classify(review)
    assert decision["classification"] == "red"
    assert decision["outcome"] == "halt"


def test_changed_conditions_revalidate():
    review = DependencyReview(
        name="Vendor Model API",
        criticality="important",
        consequence_classes=["customer"],
        persistent_memory=False,
        autonomous_execution=False,
        cross_border_exposure=False,
        authority_clear=True,
        receipt_available=True,
        replay_available=True,
        exit_path_available=True,
        conditions_changed=True,
        existing_deployment=False,
    )
    decision = classify(review)
    assert decision["classification"] == "yellow"
    assert decision["outcome"] == "revalidate"
