import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_user():
    response = requests.get(f"{BASE_URL}/users/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "username" in data

def test_get_invalid_user():
    response = requests.get(f"{BASE_URL}/users/9999")
    assert response.status_code == 404 or response.json() == {}

def test_list_users():
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200
    users = response.json()
    assert isinstance(users, list)
    assert len(users) > 0