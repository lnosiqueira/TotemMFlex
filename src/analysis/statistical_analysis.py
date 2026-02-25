import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

DB_PATH = "src/database/totem.db"

def analyze():
    # Conectar ao banco
    conn = sqlite3.connect(DB_PATH)

    # Carregar dados
    df = pd.read_sql_query("SELECT * FROM interactions", conn)
    conn.close()

    if df.empty:
        print("Banco vazio. Rode o simulador antes.")
        return

    print("\n===== ANÁLISE ESTATÍSTICA =====")
    print("Total de interações:", len(df))

    # Distribuição de predições
    counts = df["prediction"].value_counts()
    print("\nDistribuição de predições:")
    print(counts)

    print("\nPercentual:")
    print((counts / len(df)) * 100)

    print("\nMédia dos valores capturados:")
    print(df["value"].mean())

    # Gerar gráfico
    plt.figure()
    counts.plot(kind="bar")
    plt.title("Distribuição de Interações - Sprint 3")
    plt.xlabel("Tipo de Toque")
    plt.ylabel("Quantidade")
    plt.tight_layout()
    plt.savefig("src/assets/prints/16_statistical_distribution_sprint3.png")
    plt.close()

    print("\nGráfico salvo com sucesso!")

if __name__ == "__main__":
    analyze()