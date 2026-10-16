from __future__ import annotations

import json


def hello_http(request):
    """HTTP Cloud Function for a simple MLOps deployment example."""
    request_json = request.get_json(silent=True)
    name = request_json.get("name") if request_json else None

    response = {
        "status": "success",
        "message": "Hello from GCP Cloud Function!",
        "name": name or "world",
        "environment": "gcp",
    }
    return json.dumps(response), 200, {"Content-Type": "application/json"}
