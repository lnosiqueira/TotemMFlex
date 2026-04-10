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
# VALIDAÇÃO
# =========================
if df.empty:
    st.warning("Sem dados ainda")
    st.stop()

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
# INSIGHT INTELIGENTE
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

    # 🔥 NOVO: padrão de comportamento
    toques = df[df["sensor_type"] == "toque"]

    if len(toques) > total * 0.9:
        st.info("👆 Sistema baseado quase totalmente em toques (baixa diversidade)")

# =========================
# INSIGHT IA (REAL)
# =========================
if st.button("🤖 Gerar Insight com IA"):
    try:
        import openai

        openai.api_key = st.secrets["OPENAI_API_KEY"]

        prompt = f"""
        Analise esses dados de interação de usuários:

        Total de interações: {total}
        Média de valor: {media}

        Dê um insight objetivo sobre o comportamento do usuário.
        """

        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        st.success(response.choices[0].message.content)

    except Exception as e:
        st.error(f"Erro IA: {e}")