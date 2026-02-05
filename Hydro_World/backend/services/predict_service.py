import joblib
import numpy as np
import os

CHECKPOINT_DIR = "checkpoints"

def predict_potability(input_data: dict):
    scaler = joblib.load(os.path.join(CHECKPOINT_DIR, "scaler.pkl"))
    svm = joblib.load(os.path.join(CHECKPOINT_DIR, "svm_model.pkl"))
    gb = joblib.load(os.path.join(CHECKPOINT_DIR, "gb_model.pkl"))

    features = np.array([[
        input_data["ph"],
        input_data["Hardness"],
        input_data["Solids"],
        input_data["Chloramines"],
        input_data["Sulfate"],
        input_data["Conductivity"],
        input_data["Organic_carbon"],
        input_data["Trihalomethanes"],
        input_data["Turbidity"]
    ]])

    features = scaler.transform(features)

    svm_prob = svm.predict_proba(features)[:, 1][0]
    gb_prob = gb.predict_proba(features)[:, 1][0]

    final_prob = (svm_prob + gb_prob) / 2

    return "Safe" if final_prob >= 0.5 else "Unsafe"
