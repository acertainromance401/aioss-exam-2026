from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_returns_ok() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_recommendation_uses_baseline_when_flag_off(monkeypatch) -> None:
    monkeypatch.setenv("FEATURE_NEXT_RECOMMENDER", "false")
    monkeypatch.setenv("FEATURE_NEXT_RECOMMENDER_ROLLOUT", "100")

    response = client.get("/recommendation", params={"user_id": "user-101"})
    assert response.status_code == 200
    assert response.json()["model"] == "baseline-v1"


def test_recommendation_uses_next_when_flag_on_and_rollout_full(monkeypatch) -> None:
    monkeypatch.setenv("FEATURE_NEXT_RECOMMENDER", "true")
    monkeypatch.setenv("FEATURE_NEXT_RECOMMENDER_ROLLOUT", "100")

    response = client.get("/recommendation", params={"user_id": "user-101"})
    assert response.status_code == 200
    assert response.json()["model"] == "next-v2"
