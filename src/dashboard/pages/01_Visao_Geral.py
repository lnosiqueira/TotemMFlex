import streamlit as st
import requests
import pandas as pd
from openai import OpenAI

# =========================
# BLOQUEIO (OBRIGATÓRIO)
# =========================
if "logado" not in st.session_state or not st.session_state["logado"]:
    st.warning("🔒 Faça login para acessar")
    st.stop()

# =========================
# CONFIG
# =========================
API_URL = "https://totemmflex.onrender.com"
client = OpenAI(api_key=st.secrets.get("OPENAI_API_KEY"))

usuario = st.session_state["usuario"]
plano = st.session_state["plano"]

# =========================
# HEADER
# =========================
st.title("TotemMFlex Analytics")
st.write(f"👤 {usuario} | Plano: {plano}")

# =========================
# BOTÃO INTERAÇÃO
# =========================
if st.button("⚡ Simular interação"):
    try:
        tipos = ["toque", "scroll", "clique", "inatividade"]

        r = requests.post(
            f"{API_URL}/interactions/",
            json={
                "sensor_type": random.choice(tipos),
                "valor": round(random.uniform(0.1, 1.0), 2)
            },
            timeout=5
        )

        if r.status_code == 200:
            st.success("Interação enviada!")
        else:
            st.error(f"Erro API: {r.status_code}")

    except Exception as e:
        st.error(f"Erro conexão: {e}")

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
        st.warning("Sem dados ainda")
        st.stop()

except Exception as e:
    st.error(f"Erro ao carregar dados: {e}")
    st.stop()

# =========================
# TRATAMENTO
# =========================
df["data"] = pd.to_datetime(df["data"], errors="coerce")

# =========================
# MÉTRICAS
# =========================
col1, col2, col3 = st.columns(3)

col1.metric("📊 Total", len(df))
col2.metric("🧠 Média", round(df["valor"].mean(), 2))

tempo = df["data"].diff().dt.total_seconds().mean()
col3.metric("⏱ Tempo Médio", f"{round(tempo,2)}s")

# =========================
# GRÁFICOS
# =========================
st.subheader("📈 Interações no tempo")
df_time = df.groupby(df["data"].dt.strftime("%H:%M:%S")).size()
st.line_chart(df_time)

st.subheader("📊 Distribuição")
df_tipo = df.groupby("sensor_type").size()
st.bar_chart(df_tipo)

# =========================
# IA
# =========================
def gerar_ia(df, n=20):
    resumo = df.tail(n).describe().to_string()

    prompt = f"""
    Analise os dados abaixo:

    {resumo}

    Gere:
    - comportamento
    - padrão oculto
    - recomendação
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

st.subheader("🤖 Insight IA")

if st.button("Gerar Insight"):
    st.success(gerar_ia(df, 10))

if plano in ["premium", "dev_admin"]:
    if st.button("🔥 Insight Premium"):
        st.success(gerar_ia(df, 50))

if plano == "dev_admin":
    if st.button("🧠 Insight Full"):
        st.success(gerar_ia(df, len(df)))