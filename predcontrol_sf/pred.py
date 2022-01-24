
import joblib


class PredModel:
    def __init__(self, model):
        self.model = model

    @classmethod
    def from_file(cls, path):
        loaded_model = joblib.load(path)
        return cls(loaded_model)
    
    def predict(self, X):
        return self.model.predict(X)