from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path

from fastapi.testclient import TestClient

from app.main import app


def main() -> None:
    client = TestClient(app)
    user_id = "user-101"

    os.environ["FEATURE_NEXT_RECOMMENDER"] = "false"
    os.environ["FEATURE_NEXT_RECOMMENDER_ROLLOUT"] = "100"
    off_resp = client.get("/recommendation", params={"user_id": user_id}).json()

    os.environ["FEATURE_NEXT_RECOMMENDER"] = "true"
    os.environ["FEATURE_NEXT_RECOMMENDER_ROLLOUT"] = "100"
    on_resp = client.get("/recommendation", params={"user_id": user_id}).json()

    artifacts = Path("artifacts")
    artifacts.mkdir(parents=True, exist_ok=True)

    (artifacts / "feature_flag_off.json").write_text(
        json.dumps({"mode": "OFF", "response": off_resp}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    (artifacts / "feature_flag_on.json").write_text(
        json.dumps({"mode": "ON", "response": on_resp}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    (artifacts / "feature_flag_evidence.json").write_text(
        json.dumps(
            {
                "captured_at_utc": datetime.now(timezone.utc).isoformat(),
                "user_id": user_id,
                "off_env": {
                    "FEATURE_NEXT_RECOMMENDER": "false",
                    "FEATURE_NEXT_RECOMMENDER_ROLLOUT": "100",
                },
                "on_env": {
                    "FEATURE_NEXT_RECOMMENDER": "true",
                    "FEATURE_NEXT_RECOMMENDER_ROLLOUT": "100",
                },
                "off_response": off_resp,
                "on_response": on_resp,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    print("OFF:", off_resp)
    print("ON:", on_resp)


if __name__ == "__main__":
    main()
