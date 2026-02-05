import numpy as np

class CombinedModel:
    def __init__(self, svm_model, gb_model, weights=(0.5, 0.5)):
        self.svm = svm_model
        self.gb = gb_model
        self.w_svm, self.w_gb = weights

    def predict_proba(self, X):
        svm_probs = self.svm.predict_proba(X)[:, 1]
        gb_probs = self.gb.predict_proba(X)[:, 1]
        combined = self.w_svm * svm_probs + self.w_gb * gb_probs
        return combined  # 1D array
