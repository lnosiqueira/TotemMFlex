import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="TotemMFlex",
    layout="wide"
)

API_URL = "https://totemmflex.onrender.com/interactions/"
PREDICT_URL = "https://totemmflex.onrender.com/predict/"

# =========================
# FONT + CSS (APPLE STYLE)
# =========================
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800;900&display=swap" rel="stylesheet">

<style>

/* GLOBAL */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: #f8fafc;
}

/* HEADER */
.title {
    font-size: 48px;
    font-weight: 900;
    letter-spacing: -1px;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background: #0f172a;
    padding-top: 30px;
}

section[data-testid="stSidebar"] * {
    color: #e2e8f0 !important;
}

/* MENU */
.menu-title {
    font-size: 14px;
    text-transform: uppercase;
    opacity: 0.5;
    margin-bottom: 10px;
}

.menu-item {
    padding: 10px 15px;
    border-radius: 10px;
    margin-bottom: 5px;
    cursor: pointer;
}

.menu-item:hover {
    background: rgba(255,255,255,0.1);
}

.active {
    background: linear-gradient(90deg, #6366f1, #38bdf8);
}

/* CARDS */
.card {
    padding: 25px;
    border-radius: 20px;
    background: white;
    box-shadow: 0 10px 25px rgba(0,0,0,0.05);
}

/* KPI */
.kpi {
    font-size: 36px;
    font-weight: 800;
}

/* BOTÃO */
.stButton>button {
    background: linear-gradient(90deg, #6366f1, #38bdf8);
    color: white;
    border-radius: 12px;
    padding: 10px 20px;
    border: none;
    font-weight: 600;
}

/* TITULOS */
h1, h2, h3 {
    font-weight: 800;
}

</style>
""", unsafe_allow_html=True)

# =========================
# MENU (CUSTOM)
# =========================
menu = st.sidebar.radio(
    "",
    ["🚀 Dashboard", "📊 Visão Geral"]
)

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
st.markdown("""
<h1 class='title'>
TotemMFlex <span style='color:#38bdf8;'>Analytics</span>
</h1>
""", unsafe_allow_html=True)

st.caption("Monitoramento inteligente em tempo real")

# =========================
# BOTÃO INTERAÇÃO
# =========================
if st.button("⚡ Gerar interação"):
    try:
        requests.post(
            PREDICT_URL,
            json={
                "sensor_type": "toque",
                "valor": 0.5,
                "data": pd.Timestamp.now().isoformat()
            }
        )
        st.success("Interação registrada!")
        st.cache_data.clear()
    except:
        st.error("Erro ao enviar")

# =========================
# DASHBOARD
# =========================
if menu == "🚀 Dashboard":

    if df.empty:
        st.warning("Sem dados ainda")
        st.stop()

    total = len(df)
    media = df["valor"].mean()
    pct_curto = (df["classificacao"] == "toque_curto").mean() * 100

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
        <div class="card">
            <div>Total de Interações</div>
            <div class="kpi">{total}</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="card">
            <div>Média</div>
            <div class="kpi">{media:.2f}</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="card">
            <div>Toques Curtos</div>
            <div class="kpi">{pct_curto:.1f}%</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("## 📈 Tendência")

    graf = df.groupby("hora").size().reset_index(name="qtd")

    fig = px.line(graf, x="hora", y="qtd", markers=True)
    fig.update_layout(template="simple_white")

    st.plotly_chart(fig, use_container_width=True)

# =========================
# VISÃO GERAL
# =========================
elif menu == "📊 Visão Geral":

    if df.empty:
        st.warning("Sem dados ainda")
        st.stop()

    st.markdown("## 📊 Análise Completa")

    col1, col2 = st.columns(2)

    # BAR
    bar = df["classificacao"].value_counts().reset_index()
    bar.columns = ["Tipo", "Quantidade"]

    fig1 = px.bar(bar, x="Tipo", y="Quantidade")
    fig1.update_layout(template="simple_white")

    with col1:
        st.plotly_chart(fig1, use_container_width=True)

    # PIE
    fig2 = px.pie(bar, names="Tipo", values="Quantidade")

    with col2:
        st.plotly_chart(fig2, use_container_width=True)

    # INSIGHT
    st.markdown("## 🧠 Insight")

    hora_pico = df["hora"].value_counts().idxmax()

    st.info(f"Pico de uso às {hora_pico}h")

    pct_curto = (df["classificacao"] == "toque_curto").mean() * 100

    if pct_curto > 70:
        st.success("Engajamento alto")
    elif pct_curto > 40:
        st.warning("Engajamento médio")
    else:
        st.error("Engajamento baixo")