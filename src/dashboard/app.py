import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

col1, col2 = st.columns([1, 4])

with col1:
    st.image("src/assets/logo_totemmflex.png", width=100)

with col2:
    st.markdown("<div style='margin-top:-10px'></div>", unsafe_allow_html=True)
    st.caption("Inteligência comportamental em tempo real")

API_URL = "https://totemmflex.onrender.com/interactions/"
METRICS_URL = "https://totemmflex.onrender.com/metrics"
PREDICT_URL = "https://totemmflex.onrender.com/predict"

# =========================
# CSS
# =========================
st.markdown("""
<style>
.block-container {
    padding-top: 1rem;
    padding-bottom: 1rem;
}
body {
    background-color: #0f172a;
}
.title {
    font-size: 42px;
    font-weight: 800;
    color: #38bdf8;
}
.card {
    background: linear-gradient(145deg, #0f172a, #1e293b);
    padding: 25px;
    border-radius: 16px;
    color: white;
    box-shadow: 0 10px 30px rgba(0,0,0,0.4);
}
</style>
""", unsafe_allow_html=True)

# =========================
# LOAD DATA
# =========================
@st.cache_data
def load_data():
    try:
        return requests.get(API_URL).json()
    except:
        return []

@st.cache_data
def load_metrics():
    try:
        return requests.get(METRICS_URL).json()
    except:
        return {}

data = load_data()
metrics = load_metrics()

df = pd.DataFrame([data])

if not df.empty:
    df["data"] = pd.to_datetime(df["data"])
    df["hora"] = df["data"].dt.hour

# =========================
# HEADER
# =========================
st.markdown('<div class="title">🚀 TotemMFlex Analytics</div>', unsafe_allow_html=True)

# =========================
# BOTÃO
# =========================
if st.button("⚡ Gerar interação"):
    requests.post(PREDICT_URL, json={
        "pergunta": "interação simulada"
    })
    st.success("Interação enviada!")
    st.cache_data.clear()

# =========================
# KPIs (AGORA INTELIGENTE)
# =========================
col1, col2, col3 = st.columns(3)

total = metrics.get("total_interacoes", 0)
media = metrics.get("media_valor", 0)
tempo = metrics.get("media_tempo", 0)

col1.markdown(f'<div class="card">📊 Total<br><h2>{total}</h2></div>', unsafe_allow_html=True)
col2.markdown(f'<div class="card">🧠 Média Valor<br><h2>{media}</h2></div>', unsafe_allow_html=True)
col3.markdown(f'<div class="card">⏱️ Tempo Médio<br><h2>{tempo}</h2></div>', unsafe_allow_html=True)

# =========================
# GRÁFICOS
# =========================
if not df.empty:

    st.subheader("📊 Distribuição de Interações")

    fig = px.histogram(df, x="classificacao", color="classificacao")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("📈 Interações por Hora")

    fig2 = px.histogram(df, x="hora")
    st.plotly_chart(fig2, use_container_width=True)

# =========================
# INSIGHT AUTOMÁTICO
# =========================
st.subheader("🧠 Insight do Sistema")

if "insight" in metrics:
    st.success(metrics["insight"])
else:
    st.warning("Sem insight disponível ainda")
