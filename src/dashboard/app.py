import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from streamlit_autorefresh import st_autorefresh

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="TotemMFlex",
    layout="wide"
)

# Auto-refresh a cada 5 segundos
st_autorefresh(interval=5000, key="refresh")

# =========================
# CSS (AJUSTADO PARA HIERARQUIA VISUAL)
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

.title {
    font-size: 40px;
    font-weight: bold;
    margin-bottom: 10px;
}

.subtitle {
    opacity: 0.6;
    margin-bottom: 30px;
}

.card {
    background: linear-gradient(145deg, #1e293b, #0f172a);
    padding: 20px;
    border-radius: 20px;
    margin-bottom: 10px;
}

.card-main {
    border: 2px solid #38bdf8;
    box-shadow: 0 0 30px rgba(56,189,248,0.35);
}

.metric {
    font-size: 30px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown('<div class="title">🚀 TotemMFlex Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">🔄 Atualização automática a cada 5 segundos</div>', unsafe_allow_html=True)

API_URL = "https://totemmflex.onrender.com/interactions/"

# =========================
# BOTÃO DE TESTE
# =========================
if st.button("⚡ Gerar interação"):
    requests.post(
        "https://totemmflex.onrender.com/predict/",
        json={
            "sensor_type": "toque",
            "valor": 0.5,
            "data": pd.Timestamp.now().isoformat()
        }
    )
    st.success("Interação enviada!")

# =========================
# CACHE DA API
# =========================
@st.cache_data(ttl=5)
def load_data():
    return requests.get(API_URL, timeout=5).json()

with st.spinner("Atualizando dados..."):
    data = load_data()

df = pd.DataFrame(data)

if df.empty:
    st.warning("Sem dados ainda")
    st.stop()

df["data"] = pd.to_datetime(df["data"])

# =========================
# FUNÇÃO DE CARD
# =========================
def card(title, value, icon, main=False):
    css = "card card-main" if main else "card"
    st.markdown(f"""
    <div class="{css}">
        <div style="display:flex;align-items:center;gap:14px;">
            <div style="font-size:36px;">{icon}</div>
            <div>
                <div style="opacity:.8">{title}</div>
                <div class="metric">{value}</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# =========================
# KPIs COM HIERARQUIA
# =========================
pct_toque_curto = (df["classificacao"] == "toque_curto").mean() * 100

col1, col2, col3 = st.columns(3)

with col1:
    card("Total de Interações", len(df), "🖐️", main=True)

with col2:
    card("Média do Valor", f"{df['valor'].mean():.2f}", "📊")

with col3:
    card("Toques Curtos", f"{pct_toque_curto:.1f}%", "⚡")

# =========================
# GRÁFICO – USO POR HORA
# =========================
st.markdown("## 📊 Interações ao Longo do Dia")

df["hora"] = df["data"].dt.hour
graf = df.groupby("hora").size().reset_index(name="qtd")

fig = px.line(
    graf,
    x="hora",
    y="qtd",
    markers=True,
    title="Volume de Interações por Hora"
)

fig.update_traces(line=dict(width=4))
fig.update_layout(
    template="plotly_dark",
    font=dict(size=16),
    xaxis_title="Hora",
    yaxis_title="Quantidade"
)

st.plotly_chart(fig, use_container_width=True)

# =========================
# DASHBOARD INTELIGENTE (INSIGHTS AUTOMÁTICOS)
# =========================
hora_pico = graf.sort_values("qtd", ascending=False).iloc[0]["hora"]

st.markdown("## 🧠 Análise Inteligente")
st.info(f"⏰ Pico de uso identificado por volta das **{hora_pico}h**")

st.progress(min(int(pct_toque_curto), 100))

if pct_toque_curto > 70:
    st.success("🔥 Engajamento ALTO — usuários interagem rapidamente com o totem.")
elif pct_toque_curto > 40:
    st.info("🤔 Engajamento MÉDIO — há espaço para melhorar a experiência.")
else:
    st.warning("⚠ Engajamento BAIXO — revisar posicionamento ou interface do totem.")

# =========================
# DISTRIBUIÇÃO DE INTERAÇÕES
# =========================
st.markdown("## 📊 Tipos de Interação")

bar = df["classificacao"].value_counts().reset_index()
bar.columns = ["Tipo", "Quantidade"]

fig2 = px.bar(
    bar,
    x="Tipo",
    y="Quantidade",
    color="Tipo",
    title="Distribuição de Tipos de Interação"
)

fig2.update_layout(
    template="plotly_dark",
    font=dict(size=16)
)

st.plotly_chart(fig2, use_container_width=True)