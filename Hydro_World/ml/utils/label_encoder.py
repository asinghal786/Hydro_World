from sklearn.preprocessing import LabelEncoder

class SafeLabelEncoder:
    def __init__(self):
        self.encoder = LabelEncoder()

    def fit_transform(self, y):
        return self.encoder.fit_transform(y)

    def transform(self, y):
        return self.encoder.transform(y)

    def inverse_transform(self, y):
        return self.encoder.inverse_transform(y)
