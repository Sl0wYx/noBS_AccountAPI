from fastapi.testclient import TestClient
from app.main import app
import os
from dotenv import load_dotenv
from pathlib import Path
client = TestClient(app)

load_dotenv(Path("app/data/private/.env"))
API_TOKEN = os.getenv("API_TOKEN")

def test_get_image_success():
    response = client.get("/get_image/2026-03-26_18-06-09")
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"

def test_get_image_not_found():
    response = client.get("/get_image/2026-03-26_18-06-0")
    assert response.status_code == 404
    assert response.json() == {"detail": "Image not found"}

def test_receive_message_right_token():
    response = client.post(
        "/receive_message",
        headers={"authorization": f"{API_TOKEN}"},
        json={"message": "Hi this is a test message!", "date": f"21-12-32"}
    )
    assert response.status_code == 200

def test_receive_message_false_token():
    response = client.post(
            "/receive_message",
            headers={"authorization": f"false_token1000"},
            json={"message": "Hi this is a bad message!", "date": f"21-12-32"}
    )
    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid API Token"}


def test_receive_message_with_image():
    response = client.post(
        "/receive_message",
        headers={"authorization": f"{API_TOKEN}"},
        json={"message": "Hi this is a test message!", "date": f"21-12-32", "image": True}
    )
    assert response.status_code == 200

def test_receive_message_with_image_wrong_token():
    response = client.post(
        "/receive_message",
        headers={"authorization": f"really_cool_token2"},
        json={"message": "Hi this is a test message!", "date": f"21-12-32", "image": True}
    )
    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid API Token"}