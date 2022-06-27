from fastapi.testclient import TestClient
import pytest
from main import app

client = TestClient(app)


def test_create_item():
    response = client.post(
        "/api/detector/initialized",
        headers={"X-Token": "coneofsilence"},
        json={"model": "MyModel", "serialNumber": "231432432",
              "conformityCertificate": {"expirationDate": "12-12-2012", "number": "1233123"}},
    )
    # assert response.status_code == 201
    assert response.json() == {
        "id": "foobar",
        "title": "Foo Bar",
        "description": "The Foo Barters",
    }
