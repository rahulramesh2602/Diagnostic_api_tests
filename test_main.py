import httpx
from fastapi.testclient import TestClient
from main import app

# Create a test client that can make requests to our API
client = TestClient(app)

# Test the root endpoint
def test_read_root():
    response = client.get("/")  # Call the root endpoint
    assert response.status_code == 200  # Check status is OK
    assert response.json() == {"Message": "Tesla Diagnostic API running"}  # Check exact output

# Test the vehicle status endpoint
def test_vehicle_status():
    response = client.get("/vehicle/123/status")  # Call with vehicle_id=123
    assert response.status_code == 200
    data = response.json()
    assert data["vehicle_id"] == 123
    assert data["status"] == "OK"
    assert "firmware_version" in data  # Just check it exists