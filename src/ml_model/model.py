import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier

def train():
    X = np.array([[0.1],[0.2],[0.3],[0.8],[0.9],[1.0]])
    y = ["toque_curto","toque_curto","toque_curto","toque_longo","toque_longo","toque_longo"]

    model = RandomForestClassifier()
    model.fit(X, y)

    pickle.dump(model, open("src/ml_model/model.pkl", "wb"))
    print("Modelo treinado e salvo!")

train()
