import streamlit as st
import pandas as pd
import requests
import random
from openai import OpenAI

# =========================
# CONFIG
# =========================
API_URL = "https://totemmflex.onrender.com"

client = OpenAI(api_key=st.secrets.get("OPENAI_API_KEY"))

st.set_page_config(layout="wide")

# =========================
# HEADER ESTILO EMPRESA
# =========================
st.markdown("""
<h1 style='text-align:center;'>🚀 TotemMFlex Analytics</h1>
<p style='text-align:center;'>Inteligência comportamental em tempo real</p>
""", unsafe_allow_html=True)

# =========================
# BOTÕES
# =========================
col_btn1, col_btn2 = st.columns(2)

with col_btn1:
    if st.button("⚡ Simular Interação"):
        try:
            requests.post(f"{API_URL}/interactions/", json={
                "sensor_type": random.choice(["toque","voz","movimento","scroll"]),
                "valor": round(random.uniform(0.1,1),2)
            })
            st.success("Interação enviada!")
        except:
            st.error("Erro ao enviar")

with col_btn2:
    if st.button("🔄 Atualizar"):
        st.rerun()

# =========================
# DADOS
# =========================
try:
    response = requests.get(f"{API_URL}/interactions/")
    data = response.json()
    df = pd.DataFrame(data)
except:
    st.error("Erro API")
    st.stop()

if df.empty:
    st.warning("Sem dados")
    st.stop()

df["data"] = pd.to_datetime(df["data"])
df = df.sort_values("data")

# =========================
# MÉTRICAS AVANÇADAS
# =========================
df["diff"] = df["data"].diff().dt.total_seconds()

total = len(df)
media = df["valor"].mean()
tempo_medio = df["diff"].mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric("👥 Interações", total)
col2.metric("📊 Engajamento", round(media,2))
col3.metric("⏱ Tempo Médio", f"{round(tempo_medio,2)}s")
col4.metric("🔥 Pico Valor", round(df["valor"].max(),2))

# =========================
# ALERTAS INTELIGENTES
# =========================
if tempo_medio > 3:
    st.error("⚠ Usuários demorando para interagir")
elif tempo_medio < 1:
    st.success("🔥 Interação rápida")

# =========================
# GRÁFICOS
# =========================
st.subheader("📈 Interações ao longo do tempo")

df_time = df.groupby(df["data"].dt.strftime("%H:%M:%S")).size()
st.line_chart(df_time)

col_g1, col_g2 = st.columns(2)

with col_g1:
    st.subheader("📊 Distribuição")
    st.bar_chart(df["sensor_type"].value_counts())

with col_g2:
    st.subheader("📊 Engajamento")
    st.line_chart(df["valor"])

# =========================
# IA PREMIUM
# =========================
def gerar_insight(df):
    resumo = df.describe().to_string()

    prompt = f"""
    Você é um especialista em SaaS e comportamento do usuário.

    Analise os dados e entregue:

    - Insight estratégico
    - Risco
    - Oportunidade
    - Recomendação prática

    Dados:
    {resumo}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content

st.subheader("🤖 IA Estratégica")

if st.session_state.get("plano") == "free":
    st.warning("Plano FREE: insight básico limitado")

if st.button("Gerar Insight Premium"):
    with st.spinner("Analisando..."):
        st.success(gerar_insight(df))

# =========================
# TABELA
# =========================
st.subheader("📋 Últimos dados")
st.dataframe(df.tail(20))

# =========================
# EXPORT
# =========================
csv = df.to_csv(index=False)

st.download_button(
    "📥 Baixar CSV",
    csv,
    "dados.csv",
    "text/csv"
)