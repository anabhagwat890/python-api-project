import pytest
from utils.api_client import APIClient
from config.base_config import BASE_URL  # Import the URL here

@pytest.fixture
def client():
    return APIClient(BASE_URL)

def test_get_user_status_code(client):
    response = client.get_user(1)
    # Senior Tip: Always include a descriptive message in assertions
    assert response.status_code == 200, f"Expected 200 but got {response.status_code}"

def test_user_data_structure(client):
    response = client.get_user(1)
    data = response.json()
    assert "email" in data, "User record is missing email field"
    assert "@" in data["email"], "Email format is invalid"