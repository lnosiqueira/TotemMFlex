import requests
import streamlit as st
import pandas as pd
from openai import OpenAI

# =========================
# CONFIG
# =========================
st.set_page_config(layout="wide")

API_URL = "https://totemmflex.onrender.com"

client = OpenAI(api_key=st.secrets.get("OPENAI_API_KEY"))

# =========================
# FUNÇÃO IA
# =========================
def gerar_insight_ia(df):
    try:
        resumo = df.describe().to_string()

        prompt = f"""
Você é um especialista em análise de comportamento do usuário.

Analise os dados abaixo e gere:

1. Um resumo do comportamento
2. Um insight estratégico
3. Uma recomendação prática

Dados:
{resumo}

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
# SIDEBAR
# =========================
st.sidebar.title("🔎 Filtros")

data_inicio = st.sidebar.date_input("Data inicial")
data_fim = st.sidebar.date_input("Data final")

if st.sidebar.button("🔄 Atualizar dados"):
    st.rerun()

# =========================
# HEADER
# =========================
st.title("🚀 TotemMFlex Analytics")
st.caption("Plataforma de análise comportamental com IA")

# =========================
# BOTÕES
# =========================
col_btn1, col_btn2 = st.columns(2)

with col_btn1:
    if st.button("⚡ Simular interação"):
        try:
            response = requests.post(f"{API_URL}/interactions/", json={
                "sensor_type": "toque",
                "valor": 0.5
            })
            st.success("Interação registrada!")
        except:
            st.error("Erro ao enviar interação")

with col_btn2:
    if st.button("🔄 Recarregar dados"):
        st.rerun()

# =========================
# BUSCAR DADOS
# =========================
try:
    response = requests.get(f"{API_URL}/interactions/")
    data = response.json()
    df = pd.DataFrame(data)
except Exception as e:
    st.error(f"Erro ao conectar API: {e}")
    st.stop()

if df.empty:
    st.warning("Sem dados ainda")
    st.stop()

# =========================
# TRATAMENTO
# =========================
df["data"] = pd.to_datetime(df["data"], errors="coerce")
df = df.sort_values("data")

# =========================
# TEMPO MÉDIO REAL
# =========================
df["diff"] = df["data"].diff().dt.total_seconds()
tempo_medio = df["diff"].mean()

# =========================
# CARDS
# =========================
col1, col2, col3, col4 = st.columns(4)

col1.metric("📊 Total", len(df))
col2.metric("🧠 Engajamento", round(df["valor"].mean(), 2))
col3.metric("⏱ Tempo Médio", f"{round(tempo_medio,2)}s" if tempo_medio else "N/A")
col4.metric("👆 Tipo dominante", df["sensor_type"].mode()[0])

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
# EXPORT CSV
# =========================
csv = df.to_csv(index=False)

st.download_button(
    label="📥 Baixar CSV",
    data=csv,
    file_name="dados_totem.csv",
    mime="text/csv"
)

# =========================
# INSIGHTS AUTOMÁTICOS
# =========================
st.subheader("🧠 Insights Automáticos")

media = df["valor"].mean()
total = len(df)

insights = []

if total > 10:
    insights.append("Alta atividade detectada no sistema.")
else:
    insights.append("Baixo volume de interações.")

if media > 0.7:
    insights.append("Usuários altamente engajados.")
elif media > 0.4:
    insights.append("Engajamento moderado.")
else:
    insights.append("Baixo engajamento.")

toques = df[df["sensor_type"] == "toque"]

if len(toques) > total * 0.9:
    insights.append("Sistema depende quase exclusivamente de toques.")

cols = st.columns(len(insights))

for i, insight in enumerate(insights):
    cols[i].info(insight)

# =========================
# TABELA
# =========================
st.subheader("📋 Últimas interações")
st.dataframe(df.tail(20), use_container_width=True)

# =========================
# IA
# =========================
st.subheader("🤖 Insight com IA")

if st.button("Gerar Insight Inteligente"):
    with st.spinner("Analisando..."):
        insight = gerar_insight_ia(df)
        st.success(insight)