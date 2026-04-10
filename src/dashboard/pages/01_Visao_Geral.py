import streamlit as st
import requests
import pandas as pd

API_URL = "https://totemmflex.onrender.com"

st.title("🚀 TotemMFlex Analytics")

# =========================
# BOTÃO DE GERAR INTERAÇÃO
# =========================
if st.button("⚡ Gerar interação"):
    try:
        response = requests.post(f"{API_URL}/interactions/", json={
            "sensor_type": "toque",
            "valor": 0.5
        })
        if response.status_code == 200:
            st.success("Interação enviada!")
        else:
            st.error("Erro ao enviar interação")
    except:
        st.error("Erro ao conectar API")

# =========================
# BUSCAR DADOS
# =========================
try:
    metrics = requests.get(f"{API_URL}/metrics").json()
    interactions = requests.get(f"{API_URL}/interactions").json()
except:
    st.error("Erro ao conectar API")
    st.stop()

# =========================
# CARDS (METRICS)
# =========================
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📊 Total", metrics.get("total_interacoes", 0))

with col2:
    st.metric("🧠 Média Valor", metrics.get("media_valor", 0))

with col3:
    st.metric("⏱ Tempo Médio", "N/A")

# =========================
# DATAFRAME SEGURO
# =========================
if isinstance(interactions, list) and len(interactions) > 0:
    df = pd.DataFrame(interactions)

    # Só trata data se existir
    if "data" in df.columns:
        df["data"] = pd.to_datetime(df["data"], errors="coerce")

    st.subheader("📈 Interações")
    st.dataframe(df)

else:
    st.warning("Sem dados ainda")

# =========================
# INSIGHT
# =========================
st.subheader("🧠 Insight do Sistema")

if metrics.get("total_interacoes", 0) > 0:
    st.success("Sistema já possui dados para análise")
else:
    st.info("Sem insight disponível ainda")