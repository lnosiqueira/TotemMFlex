import streamlit as st
import pandas as pd
import requests
import plotly.express as px

# =============================
# CONFIGURAÇÃO DA PÁGINA
# =============================
st.set_page_config(
    page_title="TotemmFlex Analytics",
    layout="wide"
)

# =============================
# 🎨 CSS – FUNDO + CARDS PREMIUM
# =============================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(
        rgba(255,255,255,0.92),
        rgba(255,255,255,0.92)
    ),
    url("https://i.imgur.com/6YQZB7Z.png"); /* troque pela URL do seu logo/fundo */
    background-size: 520px;
    background-position: top center;
    background-repeat: no-repeat;
}

.kpi-card {
    background: white;
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.08);
    text-align: center;
}

.kpi-title {
    font-size: 14px;
    color: #6b7280;
    font-weight: 600;
}

.kpi-value {
    font-size: 36px;
    font-weight: 800;
    color: #0A66C2;
}

.header-title {
    font-size: 38px;
    font-weight: 900;
    color: #0A66C2;
}

.header-sub {
    font-size: 16px;
    color: #374151;
}
</style>
""", unsafe_allow_html=True)

# =============================
# 🚀 HEADER
# =============================
st.markdown("""
<div style="text-align:center; margin-top:120px;">
    <div class="header-title">TotemmFlex Analytics</div>
    <div class="header-sub">Inteligência comportamental em tempo real</div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =============================
# API
# =============================
API_URL = "https://totemmflex.onrender.com/interactions/"

try:
    response = requests.get(API_URL)
    data = response.json()
    df = pd.DataFrame(data)
except Exception as e:
    st.error(f"Erro ao buscar dados: {e}")
    st.stop()

if df.empty:
    st.warning("Nenhum dado disponível ainda.")
    st.stop()

# =============================
# TRATAMENTO DE DADOS
# =============================
df["data"] = pd.to_datetime(df["data"], errors="coerce")

total = len(df)
media = df.groupby("classificacao").size().mean()

# =============================
# KPIs
# =============================
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">VISITANTES</div>
        <div class="kpi-value">{total}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">MÉDIA DE INTERAÇÃO</div>
        <div class="kpi-value">{media:.2f}</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">TEMPO MÉDIO</div>
        <div class="kpi-value">0.0</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =============================
# 📈 TENDÊNCIA
# =============================
st.subheader("📈 Tendência de Interações")

df_time = df.copy()
df_time["hora"] = df_time["data"].dt.hour

grafico_linha = df_time.groupby("hora").size().reset_index(name="quantidade")

fig1 = px.line(
    grafico_linha,
    x="hora",
    y="quantidade",
    markers=True,
    template="simple_white"
)

st.plotly_chart(fig1, use_container_width=True)

# =============================
# 📊 DISTRIBUIÇÃO
# =============================
st.subheader("📊 Distribuição de Interações")

grafico_barra = df["classificacao"].value_counts().reset_index()
grafico_barra.columns = ["classificacao", "quantidade"]

fig2 = px.bar(
    grafico_barra,
    x="classificacao",
    y="quantidade",
    color="classificacao",
    template="simple_white"
)

st.plotly_chart(fig2, use_container_width=True)

# =============================
# 🧠 INSIGHT
# =============================
st.subheader("🧠 Insight Inteligente")

toque_curto = (
    grafico_barra
    .loc[grafico_barra["classificacao"] == "toque_curto", "quantidade"]
    .sum()
)

if toque_curto > total * 0.7:
    st.success("Interações rápidas predominam ⚡")
elif toque_curto > total * 0.4:
    st.info("Comportamento equilibrado 🤝")
else:
    st.warning("Usuários realizam interações mais longas 🧠")