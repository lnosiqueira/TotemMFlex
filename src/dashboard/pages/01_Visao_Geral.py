import streamlit as st
import requests
import pandas as pd

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
# TRATAMENTO
# =========================
if df.empty:
    st.warning("Sem dados ainda")
    st.stop()

# Garantir colunas
if "data" in df.columns:
    df["data"] = pd.to_datetime(df["data"], errors="coerce")

# =========================
# MÉTRICAS
# =========================
col1, col2, col3 = st.columns(3)

col1.metric("📊 Total", len(df))
col2.metric("🧠 Média Valor", round(df["valor"].mean(), 2))
col3.metric("⏱ Tempo Médio", "N/A")

# =========================
# GRÁFICO
# =========================
st.subheader("📈 Interações ao longo do tempo")

if "data" in df.columns:
    df_group = df.groupby(df["data"].dt.strftime("%H:%M:%S")).size()
    st.line_chart(df_group)

# =========================
# TABELA
# =========================
st.subheader("📋 Interações")
st.dataframe(df)

# =========================
# INSIGHT SIMPLES
# =========================
st.subheader("🧠 Insight do Sistema")

media = df["valor"].mean()

if media > 0.7:
    st.success("🔥 Alto engajamento detectado")
elif media > 0.3:
    st.info("📊 Interação moderada")
else:
    st.warning("⚠ Baixo engajamento")

# =========================
# IA (OPCIONAL)
# =========================
if st.button("🤖 Gerar Insight com IA"):
    try:
        import openai

        openai.api_key = st.secrets["OPENAI_API_KEY"]

        prompt = f"""
        Analise os dados:
        Total: {len(df)}
        Média: {media}

        Gere um insight simples.
        """

        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        st.success(response.choices[0].message.content)

    except:
        st.error("Erro ao gerar insight com IA")