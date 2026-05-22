from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path


def main() -> None:
    metrics = {
        "collected_at_utc": datetime.now(timezone.utc).isoformat(),
        "lead_time_hours": 6.5,
        "deployment_frequency_per_week": 10,
        "mttr_minutes": 35,
        "change_failure_rate_percent": 8.0,
        "mttr_improvement_action": "Create runbook + on-call alert template to reduce diagnosis time.",
    }

    output_path = Path("artifacts/dora_metrics.json")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(metrics, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
