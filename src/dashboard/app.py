import streamlit as st
import requests
import pandas as pd
import plotly.express as px

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
# CSS GLOBAL (LIGHT + DARK OK)
# =========================
st.markdown("""
<style>

/* RESET VISUAL */
html, body, [class*="css"]  {
    font-family: 'Segoe UI', sans-serif;
}

/* HEADER */
.title {
    font-size: 48px;
    font-weight: 800;
}

/* CARD BASE */
.card {
    padding: 25px;
    border-radius: 20px;
    color: white;
    background: linear-gradient(135deg, #6366f1, #38bdf8);
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
}

/* KPI */
.kpi-main {
    font-size: 40px;
    font-weight: bold;
}

.kpi-label {
    opacity: 0.8;
}

/* BOTÃO */
.stButton>button {
    background: linear-gradient(90deg, #6366f1, #38bdf8);
    color: white;
    border-radius: 12px;
    padding: 10px 20px;
    border: none;
}

/* GARANTE VISUAL EM LIGHT MODE */
@media (prefers-color-scheme: light) {
    .card {
        color: white !important;
    }
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown("""
<h1 class='title'>
🚀 TotemMFlex <span style='color:#38bdf8;'>Analytics</span>
</h1>
""", unsafe_allow_html=True)

st.caption("Monitoramento inteligente em tempo real")

# =========================
# LOAD DATA (SEM BUG)
# =========================
@st.cache_data(ttl=2)
def load_data():
    try:
        return requests.get(API_URL).json()
    except:
        return []

# =========================
# BOTÃO INTERAÇÃO
# =========================
col_btn, col_msg = st.columns([1,3])

with col_btn:
    if st.button("⚡ Gerar interação"):
        try:
            res = requests.post(
                PREDICT_URL,
                json={
                    "sensor_type": "toque",
                    "valor": 0.5,
                    "data": pd.Timestamp.now().isoformat()
                }
            )
            st.success("Interação enviada com sucesso!")
            st.cache_data.clear()
        except:
            st.error("Erro ao enviar interação")

# =========================
# DATAFRAME
# =========================
data = load_data()
df = pd.DataFrame(data)

if df.empty:
    st.warning("⚠ Nenhuma interação ainda")
    st.stop()

df["data"] = pd.to_datetime(df["data"])
df["hora"] = df["data"].dt.hour

# =========================
# KPIs
# =========================
total = len(df)
media = df["valor"].mean()
pct_curto = (df["classificacao"] == "toque_curto").mean() * 100

col1, col2, col3 = st.columns(3)

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

graf = df.groupby("hora").size().reset_index(name="qtd")

fig1 = px.line(
    graf,
    x="hora",
    y="qtd",
    markers=True
)

fig1.update_traces(
    line=dict(width=4),
    marker=dict(size=10)
)

fig1.update_layout(
    template="plotly_dark",
    title="Interações por Hora",
    transition_duration=500
)

with col_g1:
    st.plotly_chart(fig1, use_container_width=True)

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
# INSIGHT
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