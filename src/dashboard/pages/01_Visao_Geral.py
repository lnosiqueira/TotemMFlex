import streamlit as st
import pandas as pd
import requests

# =============================
# CONFIG
# =============================
st.set_page_config(page_title="TotemMFlex Analytics", layout="wide")

API_URL = "https://totemmflex.onrender.com"

# =============================
# FUNÇÕES
# =============================

def carregar_interacoes():
    try:
        response = requests.get(f"{API_URL}/interactions/")
        if response.status_code == 200:
            return response.json()
        else:
            st.error("Erro ao buscar interações")
            return []
    except:
        st.error("Erro ao conectar com API")
        return []


def carregar_metricas():
    try:
        response = requests.get(f"{API_URL}/metrics")
        if response.status_code == 200:
            return response.json()
        else:
            return {"total_interacoes": 0, "media_valor": 0}
    except:
        return {"total_interacoes": 0, "media_valor": 0}


def gerar_interacao():
    try:
        payload = {
            "sensor_type": "toque",
            "valor": 0.5
        }
        requests.post(f"{API_URL}/interactions/", json=payload)
        st.success("Interação enviada!")
    except:
        st.error("Erro ao enviar interação")


# =============================
# UI
# =============================

st.title("🚀 TotemMFlex Analytics")

if st.button("⚡ Gerar interação"):
    gerar_interacao()

# =============================
# DADOS
# =============================

data = carregar_interacoes()
metrics = carregar_metricas()

df = pd.DataFrame(data)

# =============================
# MÉTRICAS
# =============================

col1, col2, col3 = st.columns(3)

col1.metric("📊 Total", metrics.get("total_interacoes", 0))
col2.metric("🧠 Média Valor", metrics.get("media_valor", 0))
col3.metric("⏱ Tempo Médio", "N/A")

# =============================
# TRATAMENTO
# =============================

if not df.empty:
    if "data" in df.columns:
        df["data"] = pd.to_datetime(df["data"])

# =============================
# GRÁFICO
# =============================

st.subheader("📈 Interações ao longo do tempo")

if not df.empty and "data" in df.columns:
    df_group = df.groupby(df["data"].dt.strftime("%H:%M:%S")).size()
    st.line_chart(df_group)
else:
    st.warning("Sem dados para gráfico")

# =============================
# TABELA
# =============================

st.subheader("📋 Interações")

if not df.empty:
    st.dataframe(df)
else:
    st.warning("Sem dados ainda")

# =============================
# INSIGHT INTELIGENTE
# =============================

st.subheader("🧠 Insight do Sistema")

if len(df) < 10:
    st.warning("Poucos dados para análise")
else:
    media = df["valor"].mean()

    if media > 0.7:
        st.success("🔥 Alta interação detectada")
    elif media > 0.4:
        st.info("📊 Interação moderada")
    else:
        st.warning("⚠️ Baixo engajamento")

# =============================
# INSIGHT COM IA (OPCIONAL)
# =============================

def gerar_insight_ia(dados):
    try:
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Authorization": "Bearer SUA_API_KEY"
            },
            json={
                "model": "gpt-4o-mini",
                "messages": [
                    {
                        "role": "user",
                        "content": f"Analise esses dados e gere um insight curto:\n{dados}"
                    }
                ]
            }
        )

        return response.json()["choices"][0]["message"]["content"]

    except:
        return "Erro ao gerar insight com IA"


if not df.empty:
    if st.button("🤖 Gerar Insight com IA"):
        insight = gerar_insight_ia(df.tail(20).to_dict())
        st.success(insight)