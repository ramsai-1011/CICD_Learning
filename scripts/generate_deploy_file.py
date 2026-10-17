from __future__ import annotations

import json
import os
from pathlib import Path


def generate_deploy_file() -> None:
    artifact_dir = Path("artifacts")
    artifact_dir.mkdir(exist_ok=True)

    payload = {
        "version": "v1.0.0",
        "environment": os.environ.get("DEPLOY_ENVIRONMENT", "non-prod"),
        "generated_by": "github_actions",
        "status": "ready_for_deploy",
    }

    output_file = artifact_dir / "deploy_config.json"
    output_file.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"Generated deployment metadata: {output_file}")


if __name__ == "__main__":
    generate_deploy_file()
