import pickle
import numpy as np
from sklearn.base import BaseEstimator

MODEL_PATH = "src/ml_model/model.pkl"


def load_model() -> BaseEstimator:
    with open(MODEL_PATH, "rb") as f:
        return pickle.load(f)


def predict_value(model: BaseEstimator, valor: float) -> str:
    x = np.array([[float(valor)]])
    pred = model.predict(x)[0]
    return str(pred)


