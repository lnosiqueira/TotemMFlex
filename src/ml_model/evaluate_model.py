import pickle
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, classification_report
from sklearn.ensemble import RandomForestClassifier

def evaluate():

    np.random.seed(42)

    X = np.random.rand(500, 1)
    y = np.array(["toque_longo" if v > 0.7 else "toque_curto" for v in X.flatten()])

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    rf_model = RandomForestClassifier(random_state=42)
    lr_model = LogisticRegression()

    rf_model.fit(X_train, y_train)
    lr_model.fit(X_train, y_train)

    rf_pred = rf_model.predict(X_test)
    lr_pred = lr_model.predict(X_test)

    print("\n===== RANDOM FOREST =====")
    print("Accuracy:", accuracy_score(y_test, rf_pred))
    print(classification_report(y_test, rf_pred))

    print("\n===== LOGISTIC REGRESSION =====")
    print("Accuracy:", accuracy_score(y_test, lr_pred))
    print(classification_report(y_test, lr_pred))

    print("\n===== VALIDAÇÃO CRUZADA (5-FOLD) =====")
    print("RF Média:", cross_val_score(rf_model, X, y, cv=5).mean())
    print("LR Média:", cross_val_score(lr_model, X, y, cv=5).mean())

if __name__ == "__main__":
    evaluate()