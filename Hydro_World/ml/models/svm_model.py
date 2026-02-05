from sklearn.svm import SVC

class SVMModel:
    def __init__(self, **kwargs):
        # Force probability=True
        self.model = SVC(probability=True, **kwargs)

    def train(self, X, y):
        self.model.fit(X, y)

    def predict_proba(self, X):
        return self.model.predict_proba(X)
