import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

st.set_page_config(layout="wide")

st.title("📊 Visão Geral")
st.markdown("Painel executivo consolidado do comportamento do Totem.")

# =========================
# BANCO
# =========================
conn = sqlite3.connect("src/database/totem.db")
df = pd.read_sql_query("SELECT * FROM interactions", conn)
conn.close()

if df.empty:
    st.warning("Nenhum dado disponível.")
    st.stop()

df["created_at"] = pd.to_datetime(df["created_at"])

# =========================
# COMPARATIVO (simples)
# =========================
agora = df["created_at"].max()
inicio_24h = agora - timedelta(hours=24)

df_ultimas_24h = df[df["created_at"] >= inicio_24h]
df_anteriores = df[df["created_at"] < inicio_24h]

total_atual = len(df_ultimas_24h)
total_anterior = len(df_anteriores)

if total_anterior == 0:
    variacao = 0
else:
    variacao = ((total_atual - total_anterior) / total_anterior) * 100

# =========================
# HERO CHART (DOMINANTE)
# =========================
st.markdown("## 📈 Tendência de Interações (24h)")

df["hour"] = df["created_at"].dt.hour
uso_hora = df.groupby("hour").size().reset_index()
uso_hora.columns = ["Hora", "Interações"]

fig_hero = go.Figure()

fig_hero.add_trace(go.Scatter(
    x=uso_hora["Hora"],
    y=uso_hora["Interações"],
    mode="lines+markers",
    fill="tozeroy",
    line=dict(width=4)
))

fig_hero.update_layout(
    height=420,
    margin=dict(l=10, r=10, t=10, b=10),
    xaxis_title="Hora do Dia",
    yaxis_title="Volume de Interações"
)

st.plotly_chart(fig_hero, use_container_width=True)

st.markdown("---")

# =========================
# KPIs EXECUTIVOS
# =========================
col1, col2, col3, col4 = st.columns(4)

total = len(df)
media = df["value"].mean()
predominancia = (df["prediction"] == "toque_curto").mean() * 100
hora_pico = uso_hora.loc[uso_hora["Interações"].idxmax(), "Hora"]

col1.metric(
    "Total Interações (24h)",
    total_atual,
    f"{variacao:.1f}% vs período anterior"
)

col2.metric(
    "Média de Valor",
    f"{media:.3f}"
)

col3.metric(
    "Predominância Toque Curto",
    f"{predominancia:.1f}%"
)

col4.metric(
    "Horário Crítico",
    f"{hora_pico}:00h"
)

st.markdown("---")

# =========================
# SCORE DE EFICIÊNCIA
# =========================

# 1️⃣ Predominância
predominancia = (df["prediction"] == "toque_curto").mean()

if predominancia >= 0.6:
    score_pred = 40
elif predominancia >= 0.4:
    score_pred = 25
else:
    score_pred = 10

# 2️⃣ Estabilidade
interacoes_por_hora = df.groupby("hour").size()
desvio = interacoes_por_hora.std()

if desvio < interacoes_por_hora.mean() * 0.5:
    score_estabilidade = 30
elif desvio < interacoes_por_hora.mean():
    score_estabilidade = 20
else:
    score_estabilidade = 10

# 3️⃣ Duração média (value)
media_duracao = df["value"].mean()
range_total = df["value"].max() - df["value"].min()

if range_total > 0:
    normalizado = (media_duracao - df["value"].min()) / range_total
else:
    normalizado = 0.5

if 0.3 <= normalizado <= 0.8:
    score_duracao = 30
elif 0.2 <= normalizado <= 0.9:
    score_duracao = 20
else:
    score_duracao = 10

# Score final
score_total = score_pred + score_estabilidade + score_duracao

# =========================
# EXIBIÇÃO VISUAL
# =========================

st.markdown("## 🧠 Score de Eficiência Operacional")

col_score, col_bar = st.columns([1,2])

with col_score:
    st.markdown(f"<h1 style='font-size:64px'>{score_total}/100</h1>", unsafe_allow_html=True)

with col_bar:
    st.progress(score_total / 100)

if score_total >= 80:
    st.success("🟢 Operação Estável e Otimizada")
elif score_total >= 60:
    st.warning("🟡 Operação Moderada — Monitorar")
else:
    st.error("🔴 Possível Gargalo Detectado")

# =========================
# STATUS OPERACIONAL
# =========================
st.markdown("## 🧠 Status Operacional")

engajamento = "Alto" if predominancia > 60 else "Moderado"
estabilidade = "Estável" if variacao >= 0 else "Oscilando"

colA, colB = st.columns(2)

with colA:
    st.success(f"🟢 Engajamento: {engajamento}")

with colB:
    st.info(f"🔵 Sistema: {estabilidade}")

st.markdown("---")

# =========================
# INSIGHT EXECUTIVO
# =========================
st.markdown("## 🔍 Insight Estratégico")

st.markdown(f"""
O sistema registrou **{total_atual} interações nas últimas 24h**, 
com variação de **{variacao:.1f}%** em relação ao período anterior.

O pico de uso concentra-se às **{hora_pico}:00h**, 
indicando janela crítica de operação.

A predominância de toque curto sugere padrão de uso rápido e objetivo.
""")