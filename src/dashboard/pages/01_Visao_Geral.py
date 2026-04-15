import requests
import streamlit as st
import pandas as pd
from openai import OpenAI

API_URL = "https://totemmflex.onrender.com"
client = OpenAI(api_key=st.secrets.get("OPENAI_API_KEY"))

# =========================
# BLOQUEIO
# =========================
if "logado" not in st.session_state:
    st.stop()

usuario = st.session_state["usuario"]
plano = st.session_state["plano"]

st.title("🚀 TotemMFlex Analytics")
st.write(f"👤 {usuario} | Plano: {plano}")

# =========================
# BOTÃO INTERAÇÃO (VOLTOU)
# =========================
if st.button("⚡ Simular interação"):
    try:
        requests.post(f"{API_URL}/interactions/", json={
            "sensor_type": "toque",
            "valor": 0.5
        })
        st.success("Interação enviada!")
    except Exception as e:
        st.error(f"Erro ao enviar: {e}")

# =========================
# BUSCAR DADOS
# =========================
try:
    response = requests.get(f"{API_URL}/interactions/", timeout=5)

    if response.status_code != 200:
        raise Exception("API fora")

    data = response.json()
    df = pd.DataFrame(data)

except Exception as e:
    st.error(f"Erro API: {e}")
    st.stop()

# =========================
# TRATAMENTO DATA
# =========================
df["data"] = pd.to_datetime(df["data"])

# =========================
# MÉTRICAS
# =========================
col1, col2, col3 = st.columns(3)

col1.metric("Total", len(df))
col2.metric("Média", round(df["valor"].mean(), 2))

tempo = df["data"].diff().dt.total_seconds().mean()
col3.metric("Tempo Médio", f"{round(tempo,2)}s")

# =========================
# GRÁFICOS
# =========================
st.subheader("Interações")

df_time = df.groupby(df["data"].dt.strftime("%H:%M:%S")).size()
st.line_chart(df_time)

df_tipo = df.groupby("sensor_type").size()
st.bar_chart(df_tipo)

# =========================
# IA
# =========================
def gerar_ia(df, n=20):
    resumo = df.tail(n).describe().to_string()

    prompt = f"""
    Analise os dados:

    {resumo}

    Gere:
    - comportamento
    - padrão
    - recomendação
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

st.subheader("🤖 IA")

if st.button("Gerar Insight"):
    st.success(gerar_ia(df, 10))

if plano in ["premium", "dev_admin"]:
    if st.button("🔥 Insight Premium"):
        st.success(gerar_ia(df, 50))

if plano == "dev_admin":
    if st.button("🧠 Insight Full"):
        st.success(gerar_ia(df, len(df)))