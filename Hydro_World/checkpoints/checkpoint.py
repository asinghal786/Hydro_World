import os
import joblib

CHECKPOINT_DIR = "checkpoints"


def save_model(model, name):
    os.makedirs(CHECKPOINT_DIR, exist_ok=True)
    path = os.path.join(CHECKPOINT_DIR, f"{name}.joblib")
    joblib.dump(model, path)


def load_model(name):
    path = os.path.join(CHECKPOINT_DIR, f"{name}.joblib")
    if os.path.exists(path):
        return joblib.load(path)
    return None
