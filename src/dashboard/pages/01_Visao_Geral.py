import requests
import streamlit as st
import pandas as pd
from openai import OpenAI

# =========================
# CONFIG IA
# =========================
client = OpenAI(api_key=st.secrets.get("OPENAI_API_KEY"))

def gerar_insight_ia(df):
    try:
        resumo = df.describe().to_string()

        prompt = f"""
        Você é um analista de dados especialista em comportamento do usuário.

        Analise os dados abaixo e gere:

        - Padrão de comportamento
        - Possível problema ou oportunidade
        - Recomendação prática

        Dados:
        {resumo}

        Seja direto, estratégico e profissional.
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

st.set_page_config(layout="wide")

st.markdown("""
# 🚀 TotemMFlex Analytics  
Plataforma de análise comportamental em tempo real com IA
""")

st.divider()

# =========================
# BOTÕES PRINCIPAIS
# =========================
col_btn1, col_btn2, col_btn3 = st.columns(3)

# 🔥 SIMULAR INTERAÇÃO (COM DEBUG REAL)
if col_btn1.button("⚡ Simular interação"):
    try:
        payload = {
            "sensor_type": "toque",
            "valor": 0.5
        }

        st.write("📤 Enviando:", payload)

        response = requests.post(
            f"{API_URL}/interactions/",
            json=payload
        )

        st.write("📥 Status:", response.status_code)
        st.write("📥 Resposta:", response.text)

        if response.status_code == 200:
            st.success("✅ Interação registrada")
        else:
            st.error("Erro ao salvar interação")

    except Exception as e:
        st.error(f"Erro real: {e}")

# 🔥 ATUALIZAR
if col_btn3.button("🔄 Atualizar dados"):
    st.rerun()


# =========================
# BUSCAR DADOS
# =========================
try:
    response = requests.get(f"{API_URL}/interactions/")
    
    if response.status_code != 200:
        st.error(f"Erro ao buscar dados: {response.text}")
        st.stop()

    data = response.json()
    df = pd.DataFrame(data)

except Exception as e:
    st.error(f"Erro ao conectar API: {e}")
    st.stop()


# DEBUG (REMOVE DEPOIS)
st.write("🔍 DEBUG DADOS:", df.head())

# =========================
# VALIDAÇÃO
# =========================
if df.empty:
    st.warning("⚠ Sem dados ainda - verifique API")
    st.stop()

# =========================
# TRATAMENTO
# =========================
df["data"] = pd.to_datetime(df["data"], errors="coerce")
df = df.sort_values("data")

# =========================
# FILTROS
# =========================
st.sidebar.header("🔎 Filtros")

data_inicio = st.sidebar.date_input("Data inicial", df["data"].min())
data_fim = st.sidebar.date_input("Data final", df["data"].max())

df = df[(df["data"] >= str(data_inicio)) & (df["data"] <= str(data_fim))]

# =========================
# MÉTRICAS
# =========================
total = len(df)
media = df["valor"].mean()

df["diff"] = df["data"].diff().dt.total_seconds()
tempo_medio = df["diff"].mean()

if pd.isna(tempo_medio):
    tempo_medio = 0

col1, col2, col3 = st.columns(3)

col1.metric("📊 Total de Interações", total)
col2.metric("🧠 Engajamento Médio", round(media, 2))
col3.metric("⏱ Tempo Médio", f"{tempo_medio:.2f}s")

st.divider()

# =========================
# GRÁFICOS
# =========================
st.subheader("📈 Interações ao longo do tempo")

df_time = df.groupby(df["data"].dt.strftime("%H:%M:%S")).size()
st.line_chart(df_time)

st.divider()

st.subheader("📊 Distribuição por tipo")

df_tipo = df.groupby("sensor_type").size()
st.bar_chart(df_tipo)

st.divider()

# =========================
# EXPORTAÇÃO REAL (FUNCIONANDO)
# =========================
st.download_button(
    "📥 Baixar dados CSV",
    data=df.to_csv(index=False),
    file_name="dados_interacoes.csv",
    mime="text/csv"
)

# =========================
# TABELA
# =========================
st.subheader("📋 Últimas interações")
st.dataframe(df.tail(20))

st.divider()

# =========================
# INSIGHT SISTEMA
# =========================
st.subheader("🧠 Análise do Sistema")

if total < 10:
    st.warning("Poucos dados ainda")
else:
    if media > 0.7:
        st.success("🔥 Alto engajamento detectado")
    elif media > 0.4:
        st.info("📊 Engajamento moderado")
    else:
        st.warning("⚠ Baixo engajamento")

    if len(df[df["sensor_type"] == "toque"]) > total * 0.9:
        st.info("👆 Baixa diversidade de interação")

st.divider()

# =========================
# IA
# =========================
st.subheader("🤖 Análise Inteligente com IA")

if st.button("🧠 Gerar Insight Inteligente"):
    with st.spinner("Analisando comportamento..."):
        insight = gerar_insight_ia(df)
        st.success(insight)