from ml.data.dataset_loader import load_dataset
from ml.data.prepare_data import load_and_prepare_data
from ml.training.trainer import Trainer
from ml.utils.checkpoint import save_model
import os


def train_models(
    device="cpu",
    svm_params=None,
    gb_params=None,
    combined_weights=(0.5, 0.5),
    dataset_path="data/water_potability.csv"
):
    # --------------------------------------------------
    # 1. Resolve device (future-proof, CPU for now)
    # --------------------------------------------------

    # --------------------------------------------------
    # 2. Validate dataset
    # --------------------------------------------------
    if not os.path.exists(dataset_path):
        raise FileNotFoundError(
            f"Dataset not found at path: {dataset_path}"
        )

    # --------------------------------------------------
    # 3. Load & prepare data (single trusted function)
    # --------------------------------------------------
    X_train, X_test, y_train, y_test = load_and_prepare_data(
        dataset_path=dataset_path
    )

    # --------------------------------------------------
    # 4. Initialize trainer
    # --------------------------------------------------
    trainer = Trainer(
        svm_params=svm_params,
        gb_params=gb_params,
        combined_weights=combined_weights,
    )

    # --------------------------------------------------
    # 5. Train models
    # --------------------------------------------------
    trainer.train_all(X_train, y_train)

    # --------------------------------------------------
    # 6. Save trained models (safe)
    # --------------------------------------------------
    save_model(trainer.svm, "svm_model.pkl")
    save_model(trainer.gb, "gb_model.pkl")

    if trainer.combined is not None:
        save_model(trainer.combined, "combined_model.pkl")

    # --------------------------------------------------
    # 7. Evaluate
    # --------------------------------------------------
    results = trainer.evaluate_all(X_test, y_test)

    return {
        "status": "training_completed",
        "dataset": os.path.basename(dataset_path),
        "results": results
    }
