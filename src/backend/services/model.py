import pickle
import os

MODEL_PATH = "src/ml_model/model.pkl"

def load_model():
    if os.path.exists(MODEL_PATH):
        return pickle.load(open(MODEL_PATH, "rb"))
    return None

def predict_value(model, value: float):
    if model is None:
        return "toque_longo" if value > 0.7 else "toque_curto"
    return model.predict([[value]])[0]


