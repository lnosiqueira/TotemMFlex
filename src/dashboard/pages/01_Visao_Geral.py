import streamlit as st
import pandas as pd
import requests
import plotly.graph_objects as go
from datetime import timedelta

st.set_page_config(layout="wide")

API_URL = "https://totemmflex.onrender.com"

st.title("📊 Visão Geral")
st.markdown("Painel executivo consolidado do comportamento do Totem.")

# =========================
# BUSCAR DADOS DA API
# =========================
try:
    response = requests.get(f"{API_URL}/interactions")
    data = response.json()

    df = pd.DataFrame(data)

except Exception as e:
    st.error(f"Erro ao carregar dados: {e}")
    st.stop()

if df.empty:
    st.warning("Nenhum dado disponível.")
    st.stop()

# =========================
# TRATAMENTO
# =========================
df["data"] = pd.to_datetime(df["data"], errors="coerce")
df = df.dropna(subset=["data"])

df["hora"] = df["data"].dt.hour

# =========================
# COMPARATIVO
# =========================
agora = df["data"].max()
inicio_24h = agora - timedelta(hours=24)

df_ultimas_24h = df[df["data"] >= inicio_24h]
df_anteriores = df[df["data"] < inicio_24h]

total_atual = len(df_ultimas_24h)
total_anterior = len(df_anteriores)

variacao = ((total_atual - total_anterior) / total_anterior * 100) if total_anterior > 0 else 0

# =========================
# HERO CHART
# =========================
st.markdown("## 📈 Tendência de Interações (24h)")

uso_hora = df.groupby("hora").size().reset_index(name="Interações")

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=uso_hora["hora"],
    y=uso_hora["Interações"],
    mode="lines+markers",
    fill="tozeroy"
))

fig.update_layout(
    height=400,
    xaxis_title="Hora",
    yaxis_title="Interações"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# =========================
# KPIs
# =========================
col1, col2, col3, col4 = st.columns(4)

media = df["valor"].mean()
predominancia = (df["classificacao"] == "toque_curto").mean() * 100
hora_pico = uso_hora.loc[uso_hora["Interações"].idxmax(), "hora"]

col1.metric("Total 24h", total_atual, f"{variacao:.1f}%")
col2.metric("Média Valor", f"{media:.2f}")
col3.metric("Toque Curto (%)", f"{predominancia:.1f}%")
col4.metric("Pico", f"{hora_pico}:00")

st.markdown("---")

# =========================
# SCORE
# =========================
score = 0

if predominancia >= 60:
    score += 40
elif predominancia >= 40:
    score += 25
else:
    score += 10

desvio = df.groupby("hora").size().std()
media_hora = df.groupby("hora").size().mean()

if desvio < media_hora * 0.5:
    score += 30
elif desvio < media_hora:
    score += 20
else:
    score += 10

media_valor = df["valor"].mean()
if 0.3 <= media_valor <= 0.8:
    score += 30
else:
    score += 15

# =========================
# EXIBIÇÃO
# =========================
st.markdown("## 🧠 Score")

colA, colB = st.columns([1,2])

with colA:
    st.markdown(f"<h1>{score}/100</h1>", unsafe_allow_html=True)

with colB:
    st.progress(score / 100)

if score >= 80:
    st.success("🟢 Operação saudável")
elif score >= 60:
    st.warning("🟡 Monitorar")
else:
    st.error("🔴 Atenção")

st.markdown("---")

# =========================
# INSIGHT
# =========================
st.markdown("## 🔍 Insight")

st.write(f"""
Foram registradas **{total_atual} interações nas últimas 24h**  
Variação de **{variacao:.1f}%**  

Pico às **{hora_pico}:00h**  
Predominância: **{predominancia:.1f}% toque curto**
""")