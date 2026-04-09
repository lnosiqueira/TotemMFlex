import streamlit as st
import pandas as pd
import requests
import plotly.express as px

st.set_page_config(layout="wide")

# =============================
# 🎨 RESET TOTAL STREAMLIT
# =============================
st.markdown("""
<style>

/* REMOVE MENU E SIDEBAR VISUAL */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* FUNDO TOTAL */
html, body, [class*="css"]  {
    background-color: #f5f7fb;
}

/* CENTRALIZA CONTEÚDO */
.block-container {
    padding-top: 0rem;
    padding-bottom: 2rem;
    max-width: 1200px;
}

/* HERO */
.hero {
    text-align: center;
    margin-top: 30px;
    margin-bottom: 50px;
}

/* LOGO */
.logo {
    width: 320px;
}

/* SUBTITLE */
.subtitle {
    color: #6b7280;
    font-size: 18px;
    margin-top: 10px;
}

/* GRID */
.grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
}

/* CARD */
.card {
    background: white;
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0 15px 40px rgba(0,0,0,0.08);
    transition: 0.3s;
}

.card:hover {
    transform: translateY(-6px);
}

/* TEXTO */
.title {
    font-size: 14px;
    color: #6b7280;
}

.value {
    font-size: 40px;
    font-weight: bold;
    color: #111827;
}

</style>
""", unsafe_allow_html=True)

# =============================
# 🚀 HERO (IGUAL O DA REFERÊNCIA)
# =============================
st.markdown("""
<div class="hero">
    <img src="src/assets/logo_totemmflex.png" class="logo"/>
    <div class="subtitle">
        Inteligência comportamental em tempo real
    </div>
</div>
""", unsafe_allow_html=True)

# =============================
# API
# =============================
API_URL = "https://totemmflex.onrender.com/interactions/"

response = requests.get(API_URL)
data = response.json()
df = pd.DataFrame(data)

if df.empty:
    st.warning("Sem dados ainda")
    st.stop()

df["data"] = pd.to_datetime(df["data"], errors="coerce")

# =============================
# KPIs
# =============================
total = len(df)
media = df["valor"].mean()

# =============================
# GRID VISUAL (MONSTRO)
# =============================
st.markdown(f"""
<div class="grid">

    <div class="card">
        <div class="title">VISITANTES</div>
        <div class="value">{total}</div>
    </div>

    <div class="card">
        <div class="title">ENGAJAMENTO</div>
        <div class="value">{media:.2f}</div>
    </div>

</div>
""", unsafe_allow_html=True)

# =============================
# GRÁFICOS
# =============================
st.markdown("<br>", unsafe_allow_html=True)

st.subheader("Desempenho")

df["hora"] = df["data"].dt.hour
grafico = df.groupby("hora").size().reset_index(name="qtd")

fig = px.line(grafico, x="hora", y="qtd")
fig.update_layout(template="simple_white")

st.plotly_chart(fig, use_container_width=True)