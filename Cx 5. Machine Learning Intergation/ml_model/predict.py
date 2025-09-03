import joblib
import numpy as np
from typing import List

saved_model = joblib.load("C:/Users/abhay/Desktop/Advace fastapi/Cx 5. Machine Learning Intergation/ml_model/model.joblib")
print("Loaded the model")

def make_prediction(data: dict) -> float:
    features = np.array([
        [
            data['longitude'],
            data['latitude'],
            data['housing_median_age'],
            data['total_rooms'],
            data['total_bedrooms'],
            data['population'],
            data['households'],
            data['median_income']
        ]
    ])
    return saved_model.predict(features)[0]

def make_batch_predictions(data: List[dict]) -> np.array:
    X = np.array([
        [
            x['longitude'],
            x['latitude'],
            x['housing_median_age'],
            x['total_rooms'],
            x['total_bedrooms'],
            x['population'],
            x['households'],
            x['median_income']
        ]
        for x in data
    ])
    return saved_model.predict(X)