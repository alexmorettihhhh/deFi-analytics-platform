from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to DeFi Analytics Platform"}

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert "database" in response.json()
    assert "redis" in response.json()