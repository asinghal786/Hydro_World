import pandas as pd
import os


def load_dataset(path: str):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Dataset not found at {path}")

    df = pd.read_csv(path)

    if "Potability" not in df.columns:
        raise ValueError("Dataset must contain 'Potability' column")

    return df
