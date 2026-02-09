from fastapi.testclient import TestClient
from datetime import datetime
from src.main import app

client = TestClient(app)


def test_read_root():
    """Test the root endpoint returns current time."""
    response = client.get("/")
    assert response.status_code == 200
    
    # Check that the response contains current_time key
    data = response.json()
    assert "current_time" in data
    
    # Verify that the time can be parsed as ISO format
    try:
        datetime.fromisoformat(data["current_time"])
    except ValueError:
        assert False, "current_time is not in valid ISO format"
