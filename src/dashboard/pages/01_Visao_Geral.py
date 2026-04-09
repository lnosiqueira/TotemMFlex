import streamlit as st
import pandas as pd
import requests
import plotly.express as px

st.set_page_config(layout="wide")

# =============================
# 🎨 CSS NOVO (LIGHT PREMIUM)
# =============================
st.markdown("""
<style>

/* FUNDO */
body {
    background: #f5f7fb;
}

/* HERO */
.hero {
    text-align: center;
    margin-top: 20px;
    margin-bottom: 30px;
}

/* LOGO */
.logo {
    width: 260px;
}

/* SUBTITLE */
.subtitle {
    color: #6b7280;
    font-size: 18px;
    margin-top: 10px;
}

/* CARDS */
.card {
    background: white;
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.08);
    transition: 0.3s;
}

.card:hover {
    transform: translateY(-5px);
}

/* TITULOS */
.card-title {
    font-size: 14px;
    color: #6b7280;
}

.card-value {
    font-size: 32px;
    font-weight: bold;
    color: #111827;
}

</style>
""", unsafe_allow_html=True)

# =============================
# 🚀 HEADER COM LOGO
# =============================
st.markdown("""
<div style='text-align: center; margin-top: 10px;'>
    <img src="src/assets/logo_totemmflex.png" width="260"/>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style='text-align: center; color: #94a3b8; font-size: 18px; margin-bottom: 30px;'>
Inteligência comportamental em tempo real
</div>
""", unsafe_allow_html=True)

API_URL = "https://totemmflex.onrender.com/interactions/"

# =============================
# BUSCAR DADOS
# =============================
try:
    response = requests.get(API_URL)
    data = response.json()
    df = pd.DataFrame(data)

except Exception as e:
    st.error(f"Erro ao buscar dados: {e}")
    st.stop()

# =============================
# SEM DADOS
# =============================
if df.empty:
    st.warning("Nenhum dado disponível ainda.")
    st.stop()

# =============================
# TRATAMENTO
# =============================
df["data"] = pd.to_datetime(df["data"], errors="coerce")

# =============================
# KPIs (CARDS)
# =============================

ccol1, col2 = st.columns(2)

col1.markdown(f"""
<div class="card">
    <div class="card-title">VISITANTES</div>
    <div class="card-value">{total}</div>
</div>
""", unsafe_allow_html=True)

col2.markdown(f"""
<div class="card">
    <div class="card-title">MÉDIA DE INTERAÇÃO</div>
    <div class="card-value">{media:.2f}</div>
</div>
""", unsafe_allow_html=True)

# =============================
# GRÁFICO DE LINHA
# =============================
st.subheader("📈 Tendência de Interações")

df_time = df.copy()
df_time["hora"] = df_time["data"].dt.hour

grafico_linha = df_time.groupby("hora").size().reset_index(name="quantidade")

fig1 = px.line(
    grafico_linha,
    x="hora",
    y="quantidade",
    markers=True
)

fig.update_layout(template="simple_white")

st.plotly_chart(fig1, use_container_width=True)

# =============================
# GRÁFICO DE BARRAS
# =============================
st.subheader("📊 Distribuição")

grafico_barra = df["classificacao"].value_counts().reset_index()
grafico_barra.columns = ["classificacao", "quantidade"]

fig2 = px.bar(
    grafico_barra,
    x="classificacao",
    y="quantidade",
    color="classificacao"
)

fig2.update_layout(template="plotly_dark")

st.plotly_chart(fig2, use_container_width=True)

# =============================
# GRÁFICO DE PIZZA
# =============================
st.subheader("🥧 Comportamento")

fig3 = px.pie(
    df,
    names="classificacao"
)

fig3.update_layout(template="plotly_dark")

st.plotly_chart(fig3, use_container_width=True)

# =============================
# INSIGHT
# =============================
st.subheader("🧠 Insight Inteligente")

if toque_curto > 70:
    st.success("Interações rápidas predominam ⚡")
elif toque_curto > 40:
    st.info("Comportamento equilibrado 🤝")
else:
    st.warning("Usuários estão mais analíticos 🧠")