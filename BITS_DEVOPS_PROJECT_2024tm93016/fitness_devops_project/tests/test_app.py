import pytest
from app import create_app

@pytest.fixture()
def client():
    app = create_app({"TESTING": True})
    with app.test_client() as client:
        yield client

def test_index(client):
    res = client.get("/")
    assert res.status_code == 200
    assert res.get_json()["status"] == "running"

def test_health(client):
    res = client.get("/health")
    assert res.status_code == 200
    assert res.get_json()["status"] == "ok"

def test_add_and_get_workouts(client):
    # Add workout
    res = client.post("/add_workout", json={"workout": "Running", "duration": 30})
    assert res.status_code == 201
    assert "added successfully" in res.get_json()["message"]

    # Get workouts
    res = client.get("/workouts")
    data = res.get_json()
    assert res.status_code == 200
    assert data["count"] == 1
    assert data["workouts"][0]["workout"] == "Running"


