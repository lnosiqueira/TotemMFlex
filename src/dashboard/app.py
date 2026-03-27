import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import time

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="TotemMFlex Dashboard",
    layout="wide"
)

API_URL = "https://totemmflex.onrender.com/interactions/"
PREDICT_URL = "https://totemmflex.onrender.com/predict/"

# =========================
# CSS PREMIUM
# =========================
st.markdown("""
<style>
body {
    background-color: #0b1120;
    color: white;
}

.block-container {
    padding-top: 2rem;
}

/* TITULO */
.title {
    font-size: 48px;
    font-weight: bold;
    background: linear-gradient(90deg, #38bdf8, #6366f1);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* CARD */
.card {
    background: linear-gradient(135deg, #111827, #1e293b);
    padding: 20px;
    border-radius: 20px;
    box-shadow: 0 0 25px rgba(59,130,246,0.2);
    transition: 0.3s;
}

.card:hover {
    transform: scale(1.02);
    box-shadow: 0 0 40px rgba(59,130,246,0.4);
}

/* KPI GRANDE */
.kpi-main {
    font-size: 50px;
    font-weight: bold;
}

.kpi-label {
    opacity: 0.7;
}

/* BOTÃO */
.stButton>button {
    background: linear-gradient(90deg, #38bdf8, #6366f1);
    color: white;
    border-radius: 12px;
    padding: 10px 20px;
    border: none;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown('<div class="title">🚀 TotemMFlex Dashboard</div>', unsafe_allow_html=True)
st.caption("Monitoramento inteligente em tempo real")

# =========================
# BOTÃO DE INTERAÇÃO
# =========================
col_btn, col_status = st.columns([1, 3])

with col_btn:
    if st.button("⚡ Gerar interação"):
        res = requests.post(
            PREDICT_URL,
            json={
                "sensor_type": "toque",
                "valor": 0.5,
                "data": pd.Timestamp.now().isoformat()
            }
        )
        st.success("Interação enviada!")

# =========================
# LOAD DATA
# =========================
@st.cache_data(ttl=5)
def load_data():
    return requests.get(API_URL).json()

data = load_data()
df = pd.DataFrame(data)

if df.empty:
    st.warning("Sem dados ainda...")
    st.stop()

df["data"] = pd.to_datetime(df["data"])
df["hora"] = df["data"].dt.hour

# =========================
# KPIs
# =========================
total = len(df)
media = df["valor"].mean()
pct_curto = (df["classificacao"] == "toque_curto").mean() * 100

# GRID KPI
col1, col2, col3 = st.columns([2,1,1])

with col1:
    st.markdown(f"""
    <div class="card">
        <div class="kpi-label">Total de Interações</div>
        <div class="kpi-main">{total}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="card">
        <div class="kpi-label">Média</div>
        <div class="kpi-main">{media:.2f}</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="card">
        <div class="kpi-label">Toques Curtos</div>
        <div class="kpi-main">{pct_curto:.1f}%</div>
    </div>
    """, unsafe_allow_html=True)

# =========================
# GRÁFICOS
# =========================
st.markdown("## 📊 Visão Analítica")

col_g1, col_g2 = st.columns(2)

# Linha por hora
graf = df.groupby("hora").size().reset_index(name="qtd")

fig1 = px.line(
    graf,
    x="hora",
    y="qtd",
    markers=True
)

fig1.update_traces(
    line=dict(color="#38bdf8", width=4),
    marker=dict(size=10)
)

fig1.update_layout(
    template="plotly_dark",
    title="Interações por Hora"
)

with col_g1:
    st.plotly_chart(fig1, use_container_width=True)

# Barras
bar = df["classificacao"].value_counts().reset_index()
bar.columns = ["Tipo", "Quantidade"]

fig2 = px.bar(
    bar,
    x="Tipo",
    y="Quantidade",
    color="Tipo"
)

fig2.update_layout(
    template="plotly_dark",
    title="Distribuição de Interações"
)

with col_g2:
    st.plotly_chart(fig2, use_container_width=True)

# =========================
# INSIGHT INTELIGENTE
# =========================
st.markdown("## 🧠 Insight Inteligente")

hora_pico = graf.sort_values("qtd", ascending=False).iloc[0]["hora"]

st.info(f"⏰ Pico de uso às **{hora_pico}h**")

if pct_curto > 70:
    st.success("🔥 Engajamento ALTO")
elif pct_curto > 40:
    st.warning("⚠ Engajamento MÉDIO")
else:
    st.error("🚨 Engajamento BAIXO")

# =========================
# AUTO REFRESH
# =========================
time.sleep(5)
st.experimental_rerun()