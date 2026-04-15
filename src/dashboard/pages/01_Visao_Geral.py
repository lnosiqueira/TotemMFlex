import streamlit as st
import pandas as pd
import requests
from openai import OpenAI

# =========================
# CONFIG
# =========================
st.set_page_config(layout="wide")

API_URL = "https://totemmflex.onrender.com"
client = OpenAI(api_key=st.secrets.get("OPENAI_API_KEY"))

# =========================
# HEADER EMPRESA
# =========================
st.markdown("""
<h1 style='text-align:center;'>TOTEMMFLEX ANALYTICS</h1>
<p style='text-align:center;'>Inteligência comportamental em tempo real</p>
""", unsafe_allow_html=True)

# =========================
# DADOS
# =========================
response = requests.get(f"{API_URL}/interactions/")
data = response.json()
df = pd.DataFrame(data)

if df.empty:
    st.warning("Sem dados")
    st.stop()

df["data"] = pd.to_datetime(df["data"])
df = df.sort_values("data")

df["diff"] = df["data"].diff().dt.total_seconds()

# =========================
# KPIs ESTILO EMPRESA
# =========================
col1, col2, col3, col4 = st.columns(4)

col1.metric("👥 Visitantes", len(df))
col2.metric("📊 Engajamento", round(df["valor"].mean(), 2))
col3.metric("⏱ Tempo Médio", f"{round(df['diff'].mean(),2)}s")
col4.metric("🔥 Pico", round(df["valor"].max(), 2))

# =========================
# GRÁFICOS
# =========================
col_g1, col_g2 = st.columns(2)

with col_g1:
    st.subheader("📈 Interações")
    df_time = df.groupby(df["data"].dt.strftime("%H:%M:%S")).size()
    st.line_chart(df_time)

with col_g2:
    st.subheader("📊 Tipos")
    st.bar_chart(df["sensor_type"].value_counts())

# =========================
# INSIGHTS AUTOMÁTICOS (SEM IA)
# =========================
st.subheader("🧠 Insights Automáticos")

col_i1, col_i2, col_i3 = st.columns(3)

with col_i1:
    if df["valor"].mean() > 0.7:
        st.success("🔥 Alto engajamento")
    else:
        st.info("📊 Engajamento moderado")

with col_i2:
    if df["diff"].mean() > 3:
        st.warning("⏱ Usuários demorando para agir")

with col_i3:
    if df["sensor_type"].value_counts().max() > len(df)*0.7:
        st.warning("⚠ Baixa diversidade de interação")

# =========================
# IA MONSTRO (UPGRADE REAL)
# =========================
def gerar_insight(df):
    resumo = df.describe().to_string()

    prompt = f"""
    Você é um especialista em SaaS e produto digital.

    Gere uma análise PROFISSIONAL com:

    - Diagnóstico do comportamento do usuário
    - O que isso significa para o negócio
    - O maior risco
    - A melhor oportunidade
    - 3 ações práticas para melhorar conversão

    Dados:
    {resumo}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content

st.subheader("🤖 IA Estratégica")

if st.button("Gerar Insight Premium"):
    with st.spinner("Analisando comportamento..."):
        st.success(gerar_insight(df))

# =========================
# TABELA
# =========================
st.subheader("📋 Últimos registros")
st.dataframe(df.tail(20))

# =========================
# EXPORT
# =========================
csv = df.to_csv(index=False)

st.download_button(
    "📥 Exportar CSV",
    csv,
    "dados.csv"
)