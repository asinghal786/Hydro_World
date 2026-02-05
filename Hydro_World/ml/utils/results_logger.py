import json
import os
from datetime import datetime


RESULTS_DIR = "results"
HISTORY_FILE = os.path.join(RESULTS_DIR, "history.json")


def save_results(results, dataset_name="water_potability.csv"):
    os.makedirs(RESULTS_DIR, exist_ok=True)

    entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "dataset": dataset_name,
        **results
    }

    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            history = json.load(f)
    else:
        history = []

    history.append(entry)

    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)
