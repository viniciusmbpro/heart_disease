# flake8: noqa
from joblib import load
import numpy as np
import os


class HeartDiseaseModel:
    def __init__(self):
        global_path = os.path.dirname(os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))))

        self.drive_path = '/home/viniciusmb/Projects/python/heart_disease/App/bin/best_models'
        self.model_filename = os.path.join(
            self.drive_path, 'KNN10.joblib')
        self.loaded_model = load(self.model_filename)

    def predict(self, input_data):
        return self.loaded_model.predict(input_data)

    def predict_proba(self, input_data):
        return self.loaded_model.predict_proba(input_data)

    def bin_prediction(self, sample_input):
        prediction = self.predict(sample_input)
        return prediction

    def prob_prediction(self, sample_input):
        prediction_proba = self.predict_proba(sample_input)
        return prediction_proba


heart_disease_model = HeartDiseaseModel()
