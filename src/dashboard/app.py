import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# =========================
# CONFIG
# =========================
st.set_page_config(page_title="TotemMFlex", layout="wide")

# =========================
# CSS DARK PRO
# =========================
st.markdown("""
<style>
body {
    background-color: #0f172a;
    color: white;
}

.block-container {
    padding-top: 2rem;
}

.card {
    background: linear-gradient(145deg, #1e293b, #0f172a);
    padding: 20px;
    border-radius: 20px;
    box-shadow: 0 0 20px rgba(0,255,255,0.1);
}

.metric {
    font-size: 28px;
    font-weight: bold;
}

.title {
    font-size: 40px;
    font-weight: bold;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown('<div class="title">🚀 TotemMFlex Dashboard</div>', unsafe_allow_html=True)

API_URL = "https://totemmflex.onrender.com/interactions/"

# =========================
# BOTÃO
# =========================
if st.button("⚡ Gerar interação"):
    res = requests.post("https://totemmflex.onrender.com/predict/", json={
        "sensor_type": "toque",
        "valor": 0.5,
        "data": pd.Timestamp.now().isoformat()
    })
    st.success("Interação enviada!")

# =========================
# DADOS
# =========================
data = requests.get(API_URL).json()
df = pd.DataFrame(data)

if df.empty:
    st.warning("Sem dados ainda")
    st.stop()

df["data"] = pd.to_datetime(df["data"])

# =========================
# KPIs BONITOS
# =========================
col1, col2, col3 = st.columns(3)

col1.markdown(f"""
<div class="card">
<div>Total Interações</div>
<div class="metric">{len(df)}</div>
</div>
""", unsafe_allow_html=True)

col2.markdown(f"""
<div class="card">
<div>Média Valor</div>
<div class="metric">{df["valor"].mean():.2f}</div>
</div>
""", unsafe_allow_html=True)

pct = (df["classificacao"] == "toque_curto").mean()*100

col3.markdown(f"""
<div class="card">
<div>Toque Curto</div>
<div class="metric">{pct:.1f}%</div>
</div>
""", unsafe_allow_html=True)

# =========================
# GRÁFICOS
# =========================
st.markdown("## 📊 Uso em Tempo Real")

df["hora"] = df["data"].dt.hour
graf = df.groupby("hora").size().reset_index(name="qtd")

fig = px.line(graf, x="hora", y="qtd", markers=True)
fig.update_layout(template="plotly_dark")

st.plotly_chart(fig, use_container_width=True)

# =========================
# BARRAS
# =========================
st.markdown("## 📊 Distribuição")

bar = df["classificacao"].value_counts().reset_index()
bar.columns = ["tipo", "qtd"]

fig2 = px.bar(bar, x="tipo", y="qtd", color="tipo")
fig2.update_layout(template="plotly_dark")

st.plotly_chart(fig2, use_container_width=True)

# =========================
# INSIGHT
# =========================
st.markdown("## 🧠 Insight")

if pct > 70:
    st.success("🔥 Alto engajamento")
elif pct > 40:
    st.info("🤔 Engajamento médio")
else:
    st.warning("⚠ Baixo engajamento")