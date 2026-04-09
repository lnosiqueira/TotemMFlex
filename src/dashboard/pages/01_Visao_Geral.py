import streamlit as st
import pandas as pd
import requests
import plotly.express as px

st.set_page_config(layout="wide")

# =============================
# 🎨 CSS PREMIUM
# =============================
st.markdown("""
<style>

/* FUNDO */
body {
    background: linear-gradient(135deg, #0f172a, #020617);
}

/* CONTAINER */
.block-container {
    padding-top: 1rem;
    padding-bottom: 1rem;
}

/* CARDS */
.card {
    background: linear-gradient(145deg, #0f172a, #1e293b);
    padding: 25px;
    border-radius: 16px;
    color: white;
    box-shadow: 0 10px 30px rgba(0,0,0,0.4);
    transition: 0.3s;
}

/* HOVER */
.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 20px 40px rgba(0,0,0,0.6);
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
col1, col2, col3 = st.columns(3)

total = len(df)
media = df["valor"].mean()
toque_curto = (df["classificacao"] == "toque_curto").mean() * 100

col1.markdown(f"""
<div class="card">
📊 <b>Total</b><br><h2>{total}</h2>
</div>
""", unsafe_allow_html=True)

col2.markdown(f"""
<div class="card">
🧠 <b>Média Valor</b><br><h2>{media:.2f}</h2>
</div>
""", unsafe_allow_html=True)

col3.markdown(f"""
<div class="card">
⚡ <b>% Toque Curto</b><br><h2>{toque_curto:.1f}%</h2>
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

fig1.update_layout(template="plotly_dark")

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