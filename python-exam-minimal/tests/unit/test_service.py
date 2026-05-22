from app.service import next_recommender, old_recommender


def test_old_recommender_returns_baseline_model() -> None:
    result = old_recommender("user-101")
    assert result.model == "baseline-v1"


def test_old_recommender_score_range() -> None:
    result = old_recommender("user-101")
    assert 0.0 <= result.score <= 1.0


def test_next_recommender_returns_next_model() -> None:
    result = next_recommender("user-101")
    assert result.model == "next-v2"


def test_next_recommender_improves_or_equals_baseline_score() -> None:
    old_result = old_recommender("user-101")
    next_result = next_recommender("user-101")
    assert next_result.score >= old_result.score
