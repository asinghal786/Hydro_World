from sklearn.ensemble import GradientBoostingClassifier

class GBModel:
    def __init__(self, **kwargs):
        self.model = GradientBoostingClassifier(**kwargs)

    def train(self, X, y):
        self.model.fit(X, y)

    def predict_proba(self, X):
        return self.model.predict_proba(X)
