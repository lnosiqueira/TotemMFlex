import requests
import streamlit as st
import pandas as pd
from openai import OpenAI
import random

# =========================
# CONFIG
# =========================
st.set_page_config(layout="wide")

API_URL = "https://totemmflex.onrender.com"

client = OpenAI(api_key=st.secrets.get("OPENAI_API_KEY"))

# =========================
# ESTILO PREMIUM
# =========================
st.markdown("""
<style>
.metric-card {
    background: #111827;
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    color: white;
}
.metric-title {
    font-size: 14px;
    opacity: 0.7;
}
.metric-value {
    font-size: 28px;
    font-weight: bold;
}
.insight-card {
    background: #1f2937;
    padding: 15px;
    border-radius: 10px;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# =========================
# IA
# =========================
def gerar_insight_ia(df):
    try:
        resumo = df.describe().to_string()

        prompt = f"""
Você é um analista de produto SaaS.

Analise os dados e entregue:

1. O que está acontecendo
2. Problema principal
3. Oportunidade
4. Recomendação prática

Dados:
{resumo}
"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Erro IA: {str(e)}"

# =========================
# SIDEBAR
# =========================
st.sidebar.title("🔎 Filtros")

data_inicio = st.sidebar.date_input("Data inicial")
data_fim = st.sidebar.date_input("Data final")

if st.sidebar.button("🔄 Atualizar"):
    st.rerun()

# =========================
# HEADER
# =========================
st.title("🚀 TotemMFlex Analytics")
st.caption("Plataforma SaaS de análise comportamental com IA")

# =========================
# BOTÕES
# =========================
col1, col2 = st.columns(2)

with col1:
    if st.button("⚡ Simular interação"):
        try:
            requests.post(f"{API_URL}/interactions/", json={
                "sensor_type": "toque",
                "valor": round(random.uniform(0.1, 1.0), 2)
            })
            st.success("Interação registrada")
        except:
            st.error("Erro ao enviar interação")

with col2:
    if st.button("🔄 Recarregar"):
        st.rerun()

# =========================
# DADOS
# =========================
try:
    response = requests.get(f"{API_URL}/interactions/")
    data = response.json()
    df = pd.DataFrame(data)
except Exception as e:
    st.error(f"Erro ao conectar API: {e}")
    st.stop()

if df.empty:
    st.warning("Sem dados")
    st.stop()

# 👉 CONVERSÃO CORRETA DE DATA
df["data"] = pd.to_datetime(df["data"], errors="coerce")

# 👉 AJUSTE BRASIL
df["data"] = df["data"].dt.tz_localize("UTC").dt.tz_convert("America/Sao_Paulo")

# 👉 FILTRO FUNCIONANDO
if data_inicio and data_fim:
    df = df[
        (df["data"].dt.date >= data_inicio) &
        (df["data"].dt.date <= data_fim)
    ]

# 👉 TEMPO ENTRE INTERAÇÕES
df = df.sort_values("data")
df["diff"] = df["data"].diff().dt.total_seconds()

tempo_medio = df["diff"].mean() if "diff" in df else 0

# =========================
# MÉTRICAS
# =========================
col1, col2, col3, col4 = st.columns(4)

def card(title, value):
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">{title}</div>
        <div class="metric-value">{value}</div>
    </div>
    """, unsafe_allow_html=True)

with col1:
    card("Total", len(df))

with col2:
    card("Engajamento", round(df["valor"].mean(), 2))

with col3:
    card("Tempo Médio", f"{round(tempo_medio,2)}s")

with col4:
    card("Tipo", df["sensor_type"].mode()[0])

# =========================
# GRÁFICOS
# =========================
st.subheader("📈 Interações ao longo do tempo")
df_time = df.groupby(df["data"].dt.strftime("%H:%M:%S")).size()
st.line_chart(df_time)

st.subheader("📊 Distribuição")
df_tipo = df.groupby("sensor_type").size()
st.bar_chart(df_tipo)

# =========================
# INSIGHTS AUTOMÁTICOS
# =========================
st.subheader("🧠 Insights Inteligentes")

media = df["valor"].mean()
total = len(df)

insights = []

if total > 20:
    insights.append("Alta atividade no sistema")
else:
    insights.append("Baixo volume de dados")

if media > 0.7:
    insights.append("Usuários altamente engajados")
elif media > 0.4:
    insights.append("Engajamento moderado")
else:
    insights.append("Baixo engajamento")

if len(df[df["sensor_type"] == "toque"]) > total * 0.9:
    insights.append("Dependência de interação por toque")

cols = st.columns(len(insights))

for i, insight in enumerate(insights):
    cols[i].markdown(f"""
    <div class="insight-card">
        {insight}
    </div>
    """, unsafe_allow_html=True)

# =========================
# TABELA
# =========================
st.subheader("📋 Últimas interações")
st.dataframe(df.tail(20), use_container_width=True)

# =========================
# EXPORT
# =========================
csv = df.to_csv(index=False)

st.download_button(
    "📥 Baixar CSV",
    csv,
    "dados.csv"
)

# =========================
# IA PREMIUM
# =========================
st.subheader("🤖 IA Estratégica")

if st.button("Gerar Insight Premium"):
    with st.spinner("Analisando dados..."):
        insight = gerar_insight_ia(df)

        st.markdown(f"""
        <div class="insight-card">
        {insight}
        </div>
        """, unsafe_allow_html=True)