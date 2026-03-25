import requests
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# URL da API em produção
API_URL = "https://totemmflex.onrender.com"

st.set_page_config(page_title="TotemMFlex Dashboard", layout="wide")

st.title("📊 TotemMFlex - Dashboard Inteligente")

try:
    # =========================
    # BUSCAR DADOS DA API
    # =========================
    metrics_response = requests.get(f"{API_URL}/metrics")
    interactions_response = requests.get(f"{API_URL}/interactions")

    metrics = metrics_response.json()
    data = interactions_response.json()

    df = pd.DataFrame(data)

    # =========================
    # KPIs
    # =========================
    st.subheader("📌 Indicadores")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total de Interações", metrics.get("total_interacoes", 0))
    col2.metric("Média dos Valores", metrics.get("media_valor", 0))
    col3.metric("Mais Comum", metrics.get("mais_comum", "N/A"))

    # =========================
    # VERIFICA SE TEM DADOS
    # =========================
    if df.empty:
        st.warning("⚠️ Sem interações registradas ainda.")
    else:
        # =========================
        # TABELA
        # =========================
        st.subheader("📋 Histórico de Interações")
        st.dataframe(df, use_container_width=True)

        # =========================
        # GRÁFICO
        # =========================
        st.subheader("📊 Distribuição por Classificação")

        counts = df["classificacao"].value_counts()

        fig, ax = plt.subplots()
        ax.bar(counts.index.astype(str), counts.values)

        ax.set_xlabel("Classificação")
        ax.set_ylabel("Quantidade")
        ax.set_title("Interações por Classe")

        st.pyplot(fig)

except Exception as e:
    st.error(f"❌ Erro ao carregar dados: {e}")