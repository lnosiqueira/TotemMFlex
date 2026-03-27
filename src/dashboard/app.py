import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

API_URL = "https://totemmflex.onrender.com/interactions/"
PREDICT_URL = "https://totemmflex.onrender.com/predict/"

# =========================
# CSS FORTE (FUNCIONA MESMO)
# =========================
st.markdown("""
<style>

/* REMOVE PADDING DEFAULT */
.block-container {
    padding-top: 1rem;
    padding-bottom: 1rem;
}

/* BACKGROUND */
body {
    background-color: #0f172a;
}

/* TITLE */
.title {
    font-size: 42px;
    font-weight: 800;
    color: #38bdf8;
}

/* CARDS */
.card {
    background: linear-gradient(145deg, #0f172a, #1e293b);
    padding: 25px;
    border-radius: 16px;
    color: white;
    box-shadow: 0 10px 30px rgba(0,0,0,0.4);
}

/* KPI */
.kpi {
    font-size: 38px;
    font-weight: 900;
}

/* BOTÃO */
.stButton>button {
    background: linear-gradient(90deg, #6366f1, #38bdf8);
    color: white;
    border-radius: 12px;
    padding: 12px 20px;
    border: none;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# =========================
# LOAD DATA
# =========================
@st.cache_data(ttl=2)
def load_data():
    try:
        return requests.get(API_URL).json()
    except:
        return []

data = load_data()
df = pd.DataFrame(data)

if not df.empty:
    df["data"] = pd.to_datetime(df["data"])
    df["hora"] = df["data"].dt.hour

# =========================
# HEADER
# =========================
st.markdown("<div class='title'>🚀 TotemMFlex Analytics</div>", unsafe_allow_html=True)

# =========================
# BOTÃO
# =========================
if st.button("⚡ Gerar interação"):
    requests.post(PREDICT_URL, json={
        "sensor_type": "toque",
        "valor": 0.5,
        "data": pd.Timestamp.now().isoformat()
    })
    st.success("Interação enviada!")
    st.cache_data.clear()

# =========================
# SEM DADOS
# =========================
if df.empty:
    st.warning("Sem dados ainda")
    st.stop()

# =========================
# KPIs
# =========================
total = len(df)
media = df["valor"].mean()
pct = (df["classificacao"] == "toque_curto").mean() * 100

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="card">
        Total de Interações
        <div class="kpi">{total}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="card">
        Média
        <div class="kpi">{media:.2f}</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="card">
        Toques Curtos
        <div class="kpi">{pct:.1f}%</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("## 📈 Tendência")

graf = df.groupby("hora").size().reset_index(name="qtd")

fig = px.line(graf, x="hora", y="qtd", markers=True)
fig.update_layout(
    plot_bgcolor='#0f172a',
    paper_bgcolor='#0f172a',
    font_color='white'
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("## 📊 Distribuição")

fig2 = px.pie(df, names="classificacao")
fig2.update_layout(
    plot_bgcolor='#0f172a',
    paper_bgcolor='#0f172a',
    font_color='white'
)

st.plotly_chart(fig2, use_container_width=True)

# =========================
# INSIGHT
# =========================
st.markdown("## 🧠 Insight")

hora = df["hora"].value_counts().idxmax()
st.info(f"Pico de uso às {hora}h")
