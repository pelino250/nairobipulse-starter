import pytest
from app.main import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_health_returns_ok(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"

def test_districts_returns_list(client):
    response = client.get("/districts")
    data = response.get_json()
    assert "districts" in data
    assert len(data["districts"]) > 0
