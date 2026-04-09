import streamlit as st
import pandas as pd
import requests
import plotly.express as px

st.set_page_config(layout="wide")

# ==============================
# 🎨 ESTILO GLOBAL
# ==============================
st.markdown("""
<style>

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.block-container {
    padding-top: 1rem;
    max-width: 1100px;
}

/* CENTRAL */
.center {
    text-align: center;
}

/* LOGO */
.logo {
    display: block;
    margin-left: auto;
    margin-right: auto;
}

/* SUBTITLE */
.subtitle {
    color: #6b7280;
    font-size: 16px;
    margin-top: 10px;
}

/* CARD */
.card {
    background: white;
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.08);
    text-align: center;
}

/* TITLE */
.title {
    font-size: 14px;
    color: #6b7280;
}

/* VALUE */
.value {
    font-size: 36px;
    font-weight: bold;
    color: #111827;
}

</style>
""", unsafe_allow_html=True)

# ==============================
# 🚀 LOGO CENTRALIZADO
# ==============================
st.markdown('<div class="center">', unsafe_allow_html=True)

st.image("src/assets/logo_totemmflex.png", width=280)

st.markdown(
    '<div class="subtitle">Inteligência comportamental em tempo real</div>',
    unsafe_allow_html=True
)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ==============================
# API
# ==============================
API_URL = "https://totemmflex.onrender.com/interactions/"

try:
    response = requests.get(API_URL)
    data = response.json()
except:
    st.error("Erro ao conectar API")
    st.stop()

df = pd.DataFrame(data)

if df.empty:
    st.warning("Sem dados ainda")
    st.stop()

df["data"] = pd.to_datetime(df["data"], errors="coerce")

# ==============================
# KPIs
# ==============================
total = len(df)
media = df["valor"].mean()

# ==============================
# CARDS (SEM BUG)
# ==============================
col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div class="card">
        <div class="title">VISITANTES</div>
        <div class="value">{total}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="card">
        <div class="title">ENGAJAMENTO</div>
        <div class="value">{media:.2f}</div>
    </div>
    """, unsafe_allow_html=True)

# ==============================
# GRÁFICO
# ==============================
st.markdown("<br>", unsafe_allow_html=True)

st.subheader("Desempenho")

df["hora"] = df["data"].dt.hour
grafico = df.groupby("hora").size().reset_index(name="qtd")

fig = px.line(grafico, x="hora", y="qtd")
fig.update_layout(template="simple_white")

st.plotly_chart(fig, use_container_width=True)