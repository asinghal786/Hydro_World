"""
Standalone Training Runner
Used for testing ML pipeline
"""

from ml.data.dataset_loader import load_dataset
from ml.data.prepare_data import prepare_data
from ml.training.trainer import Trainer


def main():
    # CHANGE THIS PATH LATER
    dataset_path = "data/water_quality.csv"
    target_column = "label"

    df = load_dataset(dataset_path)

    X_train, X_test, y_train, y_test = prepare_data(
        df,
        target_column=target_column
    )

    trainer = Trainer()
    trainer.train_all(X_train, y_train)

    results = trainer.evaluate_all(X_test, y_test)

    print("\n=== TRAINING RESULTS ===\n")
    for model_name, metrics in results.items():
        print(f"{model_name.upper()}")
        for key, value in metrics.items():
            print(f"{key}: {value}")
        print("-" * 30)


if __name__ == "__main__":
    main()
