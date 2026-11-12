from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_blocked_ip():
    response = client.get("/check/192.0.2.10")
    assert response.status_code == 200
    assert response.json()["blocked"] is True

def test_ipv4_mapped_bypass():
    response = client.get("/check/::ffff:192.0.2.10")
    assert response.status_code == 200
    assert response.json()["blocked"] is True

def test_unblocked_ip():
    response = client.get("/check/192.0.2.11")
    assert response.status_code == 200
    assert response.json()["blocked"] is False

def test_invalid_ip():
    response = client.get("/check/not-an-ip")
    assert response.status_code == 400
    assert response.json()["detail"] == "invalid IP address"
