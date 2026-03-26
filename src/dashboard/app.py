import random
import requests
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import time

# CONFIGURAÇÃO (SEMPRE PRIMEIRO)
st.set_page_config(page_title="TotemMFlex Dashboard", layout="wide")

# URL da API
API_URL = "https://totemmflex.onrender.com"

# AUTO REFRESH GLOBAL
if st.toggle("🔄 Atualização automática"):
    time.sleep(3)
    st.rerun()

st.title("📊 TotemMFlex - Dashboard Inteligente")

# =========================
# SIMULAÇÃO
# =========================
st.subheader("🎮 Simulação em Tempo Real")

col1, col2 = st.columns(2)

# BOTÃO MANUAL
if col1.button("🚀 Gerar nova interação"):
    valor = round(random.uniform(0, 100), 2)

    try:
        response = requests.post(
            f"{API_URL}/predict",
            json={"valor": valor}
        )

        if response.status_code == 200:
            st.success(f"Interação gerada com valor {valor}")
            st.rerun()
        else:
            st.error("Erro ao enviar para API")

    except Exception as e:
        st.error(f"Erro: {e}")

# AUTO SIMULAÇÃO
auto = col2.toggle("🔁 Simulação automática")

if auto:
    valor = round(random.uniform(0, 100), 2)
    requests.post(f"{API_URL}/predict", json={"valor": valor})
    time.sleep(2)
    st.rerun()

# =========================
# BUSCAR DADOS
# =========================
try:
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
    col2.metric("Média dos Valores", round(metrics.get("media_valor", 0), 2))
    col3.metric("Mais Comum", metrics.get("mais_comum", "N/A"))

    # =========================
    # INSIGHTS
    # =========================
    st.subheader("🧠 Insights Inteligentes")

    if not df.empty:
        media = df["valor"].mean()
        mais_comum = df["classificacao"].value_counts().idxmax()

        if media < 0.4:
            st.warning("⚠️ Baixo engajamento detectado")
        elif media < 0.7:
            st.info("ℹ️ Engajamento moderado")
        else:
            st.success("🚀 Alto nível de interação")

        st.write(f"🔥 Padrão dominante: {mais_comum}")

        df["hora"] = pd.to_datetime(df["data"]).dt.hour
        pico = df["hora"].value_counts().idxmax()

        st.write(f"⏰ Horário de maior atividade: {pico}h")

    # =========================
    # TABELA
    # =========================
    if df.empty:
        st.warning("⚠️ Sem interações registradas ainda.")
    else:
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