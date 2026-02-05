import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib
import os


def load_and_prepare_data(
    dataset_path,
    test_size=0.2,
    random_state=42
):
    df = pd.read_csv(dataset_path)

    df = df.fillna(df.mean(numeric_only=True))

    X = df.drop("Potability", axis=1)
    y = df["Potability"].astype(int)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
        stratify=y
    )

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    os.makedirs("checkpoints", exist_ok=True)
    joblib.dump(scaler, "checkpoints/scaler.pkl")

    return X_train, X_test, y_train.values, y_test.values
