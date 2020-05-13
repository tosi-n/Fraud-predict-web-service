from django.apps import AppConfig
import joblib


class PredictClaimConfig(AppConfig):
    name = 'predict_claim'    


class model_wts:
    def __init__(self, filename):
        self.filename = filename
        self.model = joblib.load(self.filename)

    def _predict(self, inport):
        return self.model.predict(inport)
