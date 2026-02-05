import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from ml.models.svm_model import SVMModel
from ml.models.gb_model import GBModel
from ml.ensemble.combined_model import CombinedModel


class Trainer:
    def __init__(self, svm_params=None, gb_params=None, combined_weights=(0.5, 0.5)):
        """
        Pure CPU Trainer for sklearn models.
        No device argument anywhere.
        """
        self.svm = SVMModel(**(svm_params or {}))
        self.gb = GBModel(**(gb_params or {}))
        self.combined_weights = combined_weights
        self.combined = None

    def train_all(self, X, y):
        # Train individual models
        self.svm.train(X, y)
        self.gb.train(X, y)
        # Create ensemble using trained models
        self.combined = CombinedModel(self.svm, self.gb, self.combined_weights)

    def _evaluate_model(self, model, X, y_true):
        # Get probabilities in 1D shape
        probs = model.predict_proba(X)
        if probs.ndim == 2:
            probs = probs[:, 1]  # Take positive class

        best_metrics = None
        best_acc = 0

        thresholds = np.arange(0.3, 0.7, 0.01)
        for threshold in thresholds:
            y_pred = (probs >= threshold).astype(int)
            acc = accuracy_score(y_true, y_pred)
            if acc >= best_acc:  # prioritize accuracy while searching
                best_acc = acc
                best_metrics = {
                    "accuracy": round(acc * 100, 2),
                    "precision": round(precision_score(y_true, y_pred, zero_division=0) * 100, 2),
                    "recall": round(recall_score(y_true, y_pred, zero_division=0) * 100, 2),
                    "f1_score": round(f1_score(y_true, y_pred, zero_division=0) * 100, 2),
                    "confusion_matrix": confusion_matrix(y_true, y_pred).tolist()
                }

        return best_metrics

    def evaluate_all(self, X, y):
        y_true = np.array(y).reshape(-1).astype(int)
        return {
            "svm": self._evaluate_model(self.svm, X, y_true),
            "gradient_boosting": self._evaluate_model(self.gb, X, y_true),
            "combined": self._evaluate_model(self.combined, X, y_true)
        }
