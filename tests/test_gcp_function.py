import json

from gcp_function.main import hello_http


class DummyRequest:
    def get_json(self, silent=True):
        return {"name": "ML Ops"}


def test_hello_http_returns_success() -> None:
    response_body, status_code, headers = hello_http(DummyRequest())

    payload = json.loads(response_body)

    assert status_code == 200
    assert payload["status"] == "success"
    assert payload["name"] == "ML Ops"
    assert headers["Content-Type"] == "application/json"
