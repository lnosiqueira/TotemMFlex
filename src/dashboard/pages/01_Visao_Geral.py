import streamlit as st
import pandas as pd
import requests
import plotly.express as px

st.set_page_config(layout="wide")

st.title("📊 TotemMFlex - Dashboard Inteligente")

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
# KPIs
# =============================
col1, col2, col3 = st.columns(3)

total = len(df)
media = df["valor"].mean()
toque_curto = (df["classificacao"] == "toque_curto").mean() * 100

col1.metric("Total de Interações", total)
col2.metric("Média dos Valores", f"{media:.2f}")
col3.metric("% Toque Curto", f"{toque_curto:.1f}%")

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
    markers=True,
    title="Interações por Hora"
)

st.plotly_chart(fig1, use_container_width=True)

# =============================
# GRÁFICO DE BARRAS
# =============================
st.subheader("📊 Distribuição de Interações")

grafico_barra = df["classificacao"].value_counts().reset_index()
grafico_barra.columns = ["classificacao", "quantidade"]

fig2 = px.bar(
    grafico_barra,
    x="classificacao",
    y="quantidade",
    color="classificacao",
    title="Tipos de Interação"
)

st.plotly_chart(fig2, use_container_width=True)

# =============================
# GRÁFICO DE PIZZA
# =============================
st.subheader("🥧 Proporção de Comportamento")

fig3 = px.pie(
    df,
    names="classificacao",
    title="Distribuição (%)"
)

st.plotly_chart(fig3, use_container_width=True)

# =============================
# INSIGHT AUTOMÁTICO
# =============================
st.subheader("🧠 Insight Inteligente")

if toque_curto > 70:
    st.success("Usuários estão interagindo rapidamente 🚀")
elif toque_curto > 40:
    st.info("Engajamento moderado 🤔")
else:
    st.warning("Usuários estão demorando mais nas interações ⏳")