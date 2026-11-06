import json
from app import create_app

def setup_client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()

def test_root_returns_application_details():
    response = setup_client().get("/")
    assert response.status_code == 200
    data = response.get_json()
    assert data["application"] == "devops-api"
    assert "version" in data

def test_health_endpoint():
    response = setup_client().get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}

def test_info_endpoint_reads_environment_variables(monkeypatch):
    monkeypatch.setenv("APP_VERSION", "2.1.0")
    monkeypatch.setenv("APP_ENV", "testing")
    response = setup_client().get("/api/info")
    assert response.status_code == 200
    data = response.get_json()
    assert data["version"] == "2.1.0"
    assert data["environment"] == "testing"

def test_status_endpoint():
    response = setup_client().get("/api/status")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"

def test_unknown_endpoint_returns_404():
    response = setup_client().get("/does-not-exist")
    assert response.status_code == 404
