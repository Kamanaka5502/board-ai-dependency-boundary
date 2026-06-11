from runtime.scoring_engine import BoundaryScore, classify_score, weighted_average


def test_weighted_average_returns_number():
    score = weighted_average({
        "authority": 4,
        "retention": 4,
        "jurisdiction": 4,
        "consequence": 4,
        "reversibility": 4,
        "exit": 4,
        "receipt": 4,
        "replay": 4,
    })
    assert score == 4.0


def test_hard_red_trigger_controls_classification():
    boundary = BoundaryScore(
        scores={
            "authority": 4,
            "retention": 4,
            "jurisdiction": 4,
            "consequence": 4,
            "reversibility": 4,
            "exit": 4,
            "receipt": 4,
            "replay": 4,
        },
        hard_red_triggers=["regulated_workflow_without_escalation"],
    )
    decision = classify_score(boundary)
    assert decision["classification"] == "red"
    assert decision["outcome"] == "escalate_or_halt"


def test_yellow_boundary_classification():
    boundary = BoundaryScore(
        scores={
            "authority": 2,
            "retention": 2,
            "jurisdiction": 2,
            "consequence": 3,
            "reversibility": 2,
            "exit": 2,
            "receipt": 2,
            "replay": 1,
        },
        hard_red_triggers=[],
    )
    decision = classify_score(boundary)
    assert decision["classification"] == "yellow"
