import requests
import streamlit as st
import pandas as pd
from openai import OpenAI
import random

# =========================
# CONFIG API KEY
# =========================
api_key = st.secrets.get("OPENAI_API_KEY")

if not api_key:
    st.error("❌ API KEY não encontrada no Streamlit Secrets")
    st.stop()

client = OpenAI(api_key=api_key)

# =========================
# FUNÇÃO IA
# =========================
def gerar_insight_ia(df):
    try:
        resumo = df.describe().to_string()

        prompt = f"""
Você é um especialista em análise de comportamento do usuário em sistemas interativos.

Analise os dados abaixo e gere um insight estratégico:

{resumo}

Estruture sua resposta em:

1. 📊 Padrão identificado
2. 🧠 Interpretação do comportamento
3. ⚠ Possível problema ou oportunidade
4. 💡 Recomendação prática

Seja direto, profissional e estratégico.
"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Erro IA: {str(e)}"

# =========================
# CONFIG APP
# =========================
API_URL = "https://totemmflex.onrender.com"

st.title("🚀 TotemMFlex Analytics")

# =========================
# GERAR INTERAÇÃO
# =========================
if st.button("⚡ Gerar interação"):
    try:
        response = requests.post(
            f"{API_URL}/interactions/",
            json={
                "sensor_type": random.choice(["toque", "voz", "gesto"]),
                "valor": round(random.uniform(0.1, 1.0), 2)
            },
            timeout=5
        )

        if response.status_code == 200:
            st.success("Interação enviada!")
            st.rerun()
        else:
            st.error(f"Erro ao enviar interação: {response.status_code}")

    except Exception as e:
        st.error(f"Erro ao enviar interação: {e}")

# =========================
# BUSCAR DADOS
# =========================
try:
    try:
    requests.post(...)
    st.success("Interação enviada!")
except:
    st.error(f"Erro: {response.status_code} - {response.text}")

# =========================
# VALIDAÇÃO
# =========================
if df.empty:
    st.warning("Sem dados ainda")
    st.stop()

# Ajustar data
df["data"] = pd.to_datetime(df["data"], errors="coerce")
df = df.dropna(subset=["data"])

# =========================
# MÉTRICAS
# =========================
df = df.sort_values("data")

df["diff"] = df["data"].diff().dt.total_seconds()
tempo_medio = df["diff"].mean()

if pd.isna(tempo_medio):
    tempo_medio = 0

col1, col2, col3 = st.columns(3)

col1.metric("📊 Total", len(df))
col2.metric("🧠 Média Valor", round(df["valor"].mean(), 2))
col3.metric("⏱ Tempo Médio", f"{round(tempo_medio, 2)}s")

# =========================
# GRÁFICOS
# =========================
st.subheader("📈 Interações ao longo do tempo")
df_time = df.groupby(df["data"].dt.strftime("%H:%M:%S")).size()
st.line_chart(df_time)

st.subheader("📊 Distribuição por tipo")
df_tipo = df.groupby("sensor_type").size()
st.bar_chart(df_tipo)

# =========================
# TABELA
# =========================
st.subheader("📋 Últimas interações")
st.dataframe(df.tail(20))

# =========================
# INSIGHT SIMPLES
# =========================
st.subheader("🧠 Insight do Sistema")

media = df["valor"].mean()
total = len(df)

if total < 10:
    st.warning("Poucos dados ainda")
else:
    if media > 0.7:
        st.success("🔥 Alto engajamento")
    elif media > 0.4:
        st.info("📊 Interação moderada")
    else:
        st.warning("⚠ Baixo engajamento")

    if df["sensor_type"].nunique() == 1:
        st.info("👆 Baixa diversidade de interação")

# =========================
# IA
# =========================
st.subheader("🤖 Insight com IA")

if st.button("Gerar Insight Inteligente"):
    with st.spinner("Analisando com IA..."):
        insight = gerar_insight_ia(df)
        st.success(insight)