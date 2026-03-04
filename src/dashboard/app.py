import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

API_BASE = "http://127.0.0.1:8000"

st.set_page_config(page_title="TotemMFlex Dashboard", layout="wide")

st.title("📊 TotemMFlex Dashboard (Sprint 3)")
st.caption("Dashboard consumindo a API (FastAPI) + histórico rastreável no SQLite.")

colA, colB, colC = st.columns([1.2, 1, 1])

with colA:
    st.subheader("🔮 Fazer predição via API")
    valor = st.slider("Valor do sensor", min_value=0.0, max_value=1.0, value=0.85, step=0.01)

    if st.button("Enviar para /predict", use_container_width=True):
        try:
            r = requests.post(f"{API_BASE}/predict", json={"valor": float(valor)}, timeout=10)
            r.raise_for_status()
            data = r.json()
            st.success(f"Classificação: **{data['classificacao']}** | Valor: {data['valor_sensor']}")
        except Exception as e:
            st.error(f"Falha ao chamar API: {e}")

with colB:
    st.subheader("🧾 Últimas interações (API)")
    limit = st.number_input("Quantidade", min_value=10, max_value=1000, value=200, step=10)

    if st.button("Atualizar histórico", use_container_width=True):
        st.session_state["refresh"] = st.session_state.get("refresh", 0) + 1

with colC:
    st.subheader("⚙️ Status da API")
    try:
        s = requests.get(f"{API_BASE}/status", timeout=5).json()
        st.info(f"Status: {s.get('status')} | Versão: {s.get('version')}")
    except Exception:
        st.warning("API offline. Rode: `uvicorn src.backend.main:app --reload`")

st.divider()

# Carrega histórico sempre
try:
    resp = requests.get(f"{API_BASE}/interactions", params={"limit": int(limit)}, timeout=10)
    resp.raise_for_status()
    payload = resp.json()
    df = pd.DataFrame(payload["items"])

    if df.empty:
        st.warning("Sem interações registradas ainda. Faça uma predição para gerar histórico.")
    else:
        # KPIs
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Total (no recorte)", f"{len(df)}")
        c2.metric("% Toque Curto", f"{(df['prediction'].eq('toque_curto').mean()*100):.1f}%")
        c3.metric("% Toque Longo", f"{(df['prediction'].eq('toque_longo').mean()*100):.1f}%")
        c4.metric("Último registro", df.iloc[0]["created_at"])

        st.subheader("📋 Tabela")
        st.dataframe(df, use_container_width=True)

        # Gráfico simples por classe
        st.subheader("📈 Distribuição por classe")
        counts = df["prediction"].value_counts().sort_index()

        fig, ax = plt.subplots()
        ax.bar(counts.index.astype(str), counts.values)
        ax.set_xlabel("Classe")
        ax.set_ylabel("Quantidade")
        ax.set_title("Interações por classe (histórico)")
        st.pyplot(fig)

except Exception as e:
    st.error(f"Erro ao buscar /interactions: {e}")