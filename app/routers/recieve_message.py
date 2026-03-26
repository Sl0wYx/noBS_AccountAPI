from fastapi import APIRouter, Request, HTTPException
import json
import os
from dotenv import load_dotenv
from pathlib import Path


load_dotenv(Path("app/data/private/.env"))

API_TOKEN = os.getenv("API_TOKEN")
router = APIRouter()
@router.get("/get_message", tags=["telegram"])
async def get_message():
    with open("app/data/message.json", mode='r', encoding='utf-8-sig') as message:
        return json.load(message)

@router.post('/receive_message', tags=["telegram"])
async def receive_message(data: dict, request: Request):
    if request.headers.get("Authorization") != API_TOKEN:
        raise HTTPException(status_code=401, detail="Invalid API Token")
    else:
        base = Path("app/data")
        path = base / "message.json"
        path.write_text(json.dumps(data))