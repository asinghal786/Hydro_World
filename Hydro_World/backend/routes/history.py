import json
import os
from fastapi import APIRouter

router = APIRouter()

HISTORY_FILE = "results/history.json"


@router.get("/history")
def get_history():
    if not os.path.exists(HISTORY_FILE):
        return []

    with open(HISTORY_FILE, "r") as f:
        return json.load(f)
