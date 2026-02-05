import os
import joblib

CHECKPOINT_DIR = "checkpoints"


def ensure_checkpoint_dir():
    if not os.path.exists(CHECKPOINT_DIR):
        os.makedirs(CHECKPOINT_DIR)


def save_model(model, filename):
    ensure_checkpoint_dir()
    path = os.path.join(CHECKPOINT_DIR, filename)
    joblib.dump(model, path)


def load_model(filename):
    path = os.path.join(CHECKPOINT_DIR, filename)
    if not os.path.exists(path):
        return None
    return joblib.load(path)
