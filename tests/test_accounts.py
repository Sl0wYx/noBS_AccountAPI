from fastapi.testclient import TestClient
from app.main import app
import os
from dotenv import load_dotenv
from pathlib import Path
client = TestClient(app)

load_dotenv(Path("app/data/private/.env"))
API_TOKEN = os.getenv("API_TOKEN")

def test_get_nonexisting_ID():
    response = client.get("/accounts/2")
    assert response.status_code == 404
    assert response.json() == {"detail": "Account with that ID does not exist"}

def test_get_account_success():
    response = client.get("/accounts/934533956244742194")
    assert response.status_code == 200
    assert isinstance(response.json()["DiscordID"], int)
    assert isinstance(response.json()["PlayerUUID"], str)

    


