"""
Checkpoint Manager
Handles saving and loading model checkpoints
"""

import joblib
import os


def save_checkpoint(model, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    joblib.dump(model, path)


def load_checkpoint(path):
    if os.path.exists(path):
        return joblib.load(path)
    return None
