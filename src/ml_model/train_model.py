import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def train():

    np.random.seed(42)

    X = np.random.rand(500, 1)
    y = np.array(["toque_longo" if v > 0.7 else "toque_curto" for v in X.flatten()])

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    pickle.dump(model, open("src/ml_model/model.pkl", "wb"))

    print("Modelo treinado e salvo com sucesso!")

if __name__ == "__main__":
    train()