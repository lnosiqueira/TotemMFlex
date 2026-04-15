import requests
import streamlit as st
import pandas as pd
from openai import OpenAI

# =========================
# CONFIG
# =========================
API_URL = "https://totemmflex.onrender.com"
client = OpenAI(api_key=st.secrets.get("OPENAI_API_KEY"))

plano = st.session_state.get("plano", "free")
usuario = st.session_state.get("usuario", "desconhecido")

# =========================
# HEADER
# =========================
st.title("🚀 TotemMFlex Analytics")
st.write(f"👤 Usuário: {usuario} | Plano: {plano.upper()}")

# =========================
# PERMISSÕES
# =========================
def pode_usar_premium():
    return plano in ["premium", "dev_admin"]

def is_dev():
    return plano == "dev_admin"

# =========================
# BUSCAR DADOS
# =========================
try:
    response = requests.get(f"{API_URL}/interactions/", timeout=5)

    if response.status_code != 200:
        raise Exception("API fora")

    data = response.json()
    df = pd.DataFrame(data)

    if df.empty:
        raise Exception("Sem dados")

except Exception as e:
    st.warning(f"⚠ API offline — usando dados simulados ({e})")

    df = pd.DataFrame({
        "sensor_type": ["toque", "voz", "movimento", "scroll"] * 15,
        "valor": [0.2, 0.5, 0.8, 0.3] * 15,
        "data": pd.date_range(end=pd.Timestamp.now(), periods=60)
    })

# =========================
# TRATAMENTO DATA
# =========================
df["data"] = pd.to_datetime(df["data"], errors="coerce")

# =========================
# MÉTRICAS
# =========================
col1, col2, col3 = st.columns(3)

col1.metric("📊 Total", len(df))
col2.metric("🧠 Média", round(df["valor"].mean(), 2))

tempo_medio = df["data"].diff().dt.total_seconds().mean()
col3.metric("⏱ Tempo Médio", f"{round(tempo_medio,2)}s")

# =========================
# GRÁFICOS
# =========================
st.subheader("📈 Interações no tempo")

df_time = df.groupby(df["data"].dt.strftime("%H:%M")).size()
st.line_chart(df_time)

st.subheader("📊 Distribuição")

df_tipo = df.groupby("sensor_type").size()
st.bar_chart(df_tipo)

# =========================
# IA BÁSICA
# =========================
def gerar_ia(df, amostra=20):
    sample = df.tail(amostra)
    resumo = sample.describe().to_string()

    prompt = f"""
    Analise os dados abaixo e gere insights de negócio:

    {resumo}

    Gere:
    - comportamento do usuário
    - padrão oculto
    - recomendação estratégica
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

# =========================
# IA FREE
# =========================
st.subheader("🤖 Insight IA")

if st.button("Gerar Insight"):
    st.info("Plano FREE (limitado)")
    st.success(gerar_ia(df, 10))

# =========================
# IA PREMIUM
# =========================
if pode_usar_premium():
    if st.button("🔥 Insight Premium"):
        st.info("Plano PREMIUM ativado")
        st.success(gerar_ia(df, 50))

# =========================
# DEV AREA
# =========================
if is_dev():
    st.subheader("🧠 Modo Desenvolvedor")

    st.write("Debug dataset:")
    st.dataframe(df.tail(50))

    st.write("📊 Estatísticas completas:")
    st.write(df.describe())

    if st.button("Gerar Insight Full"):
        st.success(gerar_ia(df, len(df)))