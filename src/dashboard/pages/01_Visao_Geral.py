import streamlit as st
import requests
import pandas as pd
import google.generativeai as genai
import os

# =========================
# CONFIG IA
# =========================
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def gerar_insight_ia(df):
    try:
        resumo = df.describe().to_string()

        prompt = f"""
        Analise os dados abaixo e gere um insight de comportamento do usuário:

        {resumo}

        Seja direto, profissional e estratégico.
        """

        response = model.generate_content(prompt)

        return response.text

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
        requests.post(f"{API_URL}/interactions/", json={
            "sensor_type": "toque",
            "valor": 0.5
        })
        st.success("Interação enviada!")
    except:
        st.error("Erro ao enviar interação")

# =========================
# BUSCAR DADOS
# =========================
try:
    response = requests.get(f"{API_URL}/interactions/")
    data = response.json()
    df = pd.DataFrame(data)
except:
    st.error("Erro ao conectar API")
    st.stop()

# =========================
# VALIDAÇÃO
# =========================
if df.empty:
    st.warning("Sem dados ainda")
    st.stop()

# Garantir formato de data
df["data"] = pd.to_datetime(df["data"], errors="coerce")

# =========================
# MÉTRICAS
# =========================
col1, col2, col3 = st.columns(3)

col1.metric("📊 Total", len(df))
col2.metric("🧠 Média Valor", round(df["valor"].mean(), 2))
col3.metric("⏱ Tempo Médio", "N/A")

# =========================
# GRÁFICO DE TEMPO
# =========================
st.subheader("📈 Interações ao longo do tempo")

df_time = df.groupby(df["data"].dt.strftime("%H:%M:%S")).size()
st.line_chart(df_time)

# =========================
# GRÁFICO POR TIPO
# =========================
st.subheader("📊 Distribuição por tipo de interação")

df_tipo = df.groupby("sensor_type").size()
st.bar_chart(df_tipo)

# =========================
# TABELA
# =========================
st.subheader("📋 Interações")
st.dataframe(df.tail(20))

# =========================
# INSIGHT SIMPLES
# =========================
st.subheader("🧠 Insight do Sistema")

media = df["valor"].mean()
total = len(df)

if total < 10:
    st.warning("Poucos dados para análise ainda")
else:
    if media > 0.7:
        st.success("🔥 Alto engajamento detectado")
    elif media > 0.4:
        st.info("📊 Interação moderada")
    else:
        st.warning("⚠ Baixo engajamento")

    # Padrão de comportamento
    toques = df[df["sensor_type"] == "toque"]

    if len(toques) > total * 0.9:
        st.info("👆 Sistema baseado quase totalmente em toques (baixa diversidade)")

# =========================
# INSIGHT COM IA (REAL)
# =========================
st.subheader("🤖 Insight com IA")

if st.button("Gerar Insight Inteligente"):
    with st.spinner("Analisando dados com IA..."):
        insight = gerar_insight_ia(df)
        st.success(insight)