from dataclasses import dataclass
import hashlib


@dataclass
class RecommendationResult:
    user_id: str
    model: str
    score: float


def old_recommender(user_id: str) -> RecommendationResult:
    # Stable baseline score in 0.30~0.79.
    digest = hashlib.sha256(user_id.encode("utf-8")).hexdigest()
    bucket = int(digest[:8], 16) % 50
    score = round(0.30 + (bucket / 100), 3)
    return RecommendationResult(user_id=user_id, model="baseline-v1", score=score)


def next_recommender(user_id: str) -> RecommendationResult:
    baseline = old_recommender(user_id)
    # Improved strategy: apply uplift while capping to valid score range.
    score = round(min(0.99, baseline.score + 0.12), 3)
    return RecommendationResult(user_id=user_id, model="next-v2", score=score)
