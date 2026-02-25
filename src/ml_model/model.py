import pickle
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def train():
    np.random.seed(42)

    # Dataset sintético
    X = np.random.rand(500, 1)
    y = np.array(["toque_longo" if v > 0.7 else "toque_curto" for v in X.flatten()])

    # Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Treino
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Avaliação
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    # Print console
    print("\n===== MÉTRICAS DO MODELO =====")
    print("Accuracy:", acc)
    print("\nMatriz de Confusão:")
    print(cm)
    print("\nRelatório de Classificação:")
    print(report)

    # Salvar modelo
    pickle.dump(model, open("src/ml_model/model.pkl", "wb"))

    # Salvar métricas em arquivo
    with open("src/ml_model/metrics_sprint3.txt", "w", encoding="utf-8") as f:
        f.write("===== MÉTRICAS DO MODELO =====\n")
        f.write(f"Accuracy: {acc}\n\n")
        f.write("Matriz de Confusão:\n")
        f.write(str(cm))
        f.write("\n\nRelatório de Classificação:\n")
        f.write(report)

    # Gerar gráfico da matriz
    plt.figure()
    plt.imshow(cm)
    plt.title("Matriz de Confusão - Sprint 3")
    plt.xlabel("Previsto")
    plt.ylabel("Real")
    plt.colorbar()
    plt.savefig("src/assets/prints/15_confusion_matrix_sprint3.png")
    plt.close()

    print("\nModelo treinado, métricas salvas e gráfico gerado com sucesso!")

if __name__ == "__main__":
    train()