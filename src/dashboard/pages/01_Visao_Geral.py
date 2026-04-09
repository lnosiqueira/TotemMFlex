import streamlit as st
import pandas as pd
import requests
import plotly.express as px

st.set_page_config(layout="wide")

# =============================
# 🎨 CSS
# =============================
st.markdown("""
<style>

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

html, body, [class*="css"]  {
    background-color: #f5f7fb;
}

.block-container {
    padding-top: 0rem;
    padding-bottom: 2rem;
    max-width: 1200px;
}

/* HERO */
.hero {
    text-align: center;
    margin-top: 40px;
    margin-bottom: 50px;
}

.logo {
    width: 320px;
}

.subtitle {
    color: #6b7280;
    font-size: 18px;
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
}

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
# 🚀 HERO (AGORA CERTO)
# =============================
st.markdown("""
<div class="hero">
</div>
""", unsafe_allow_html=True)

st.image("assets/logo_totemmflex.png", width=300)
st.caption("Inteligência comportamental em tempo real")

# =============================
# 💎 GRID
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
# 📊 GRÁFICO
# =============================
st.markdown("<br>", unsafe_allow_html=True)

st.subheader("Desempenho")

df["hora"] = df["data"].dt.hour
grafico = df.groupby("hora").size().reset_index(name="qtd")

fig = px.line(grafico, x="hora", y="qtd")
fig.update_layout(template="simple_white")

st.plotly_chart(fig, use_container_width=True)