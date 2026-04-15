import streamlit as st

st.set_page_config(page_title="TotemMFlex", layout="centered")

# =========================
# CSS PROFISSIONAL
# =========================
st.markdown("""
<style>

body {
    background: linear-gradient(135deg, #0f172a, #1e3a8a);
}

.main {
    background: transparent;
}

.login-box {
    background: rgba(255,255,255,0.05);
    padding: 40px;
    border-radius: 20px;
    backdrop-filter: blur(12px);
    box-shadow: 0px 10px 40px rgba(0,0,0,0.3);
    width: 100%;
    max-width: 420px;
    margin: auto;
}

.title {
    font-size: 32px;
    font-weight: 700;
    color: white;
    text-align: center;
    margin-bottom: 10px;
}

.subtitle {
    text-align: center;
    color: #cbd5e1;
    margin-bottom: 30px;
}

.stTextInput > div > div > input {
    border-radius: 10px;
    padding: 12px;
}

.stButton button {
    width: 100%;
    border-radius: 10px;
    padding: 12px;
    background: #2563eb;
    color: white;
    font-weight: bold;
}

.footer {
    text-align: center;
    color: #94a3b8;
    margin-top: 20px;
    font-size: 12px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# USUÁRIOS
# =========================
USERS = {
    "admin": {"senha": "123", "plano": "premium"},
    "user": {"senha": "123", "plano": "free"},
    "lnosiqueira": {"senha": "fiap0316", "plano": "dev_admin"}
}

# =========================
# LOGIN UI
# =========================
st.markdown('<div class="login-box">', unsafe_allow_html=True)

st.markdown('<div class="title">🚀 TotemMFlex</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Inteligência comportamental em tempo real</div>', unsafe_allow_html=True)

usuario = st.text_input("Usuário")
senha = st.text_input("Senha", type="password")

if st.button("Entrar"):
    if usuario in USERS and USERS[usuario]["senha"] == senha:
        st.session_state["logado"] = True
        st.session_state["usuario"] = usuario
        st.session_state["plano"] = USERS[usuario]["plano"]
        st.rerun()
    else:
        st.error("Usuário ou senha inválidos")

st.markdown('<div class="footer">© TotemMFlex Analytics</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
