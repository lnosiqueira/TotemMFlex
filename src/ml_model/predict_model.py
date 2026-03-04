import pickle
import numpy as np
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")

# Carrega o modelo uma única vez
model = pickle.load(open(MODEL_PATH, "rb"))

def predict(valor_sensor: float):

    entrada = np.array([[valor_sensor]])
    pred = model.predict(entrada)

    return pred[0]