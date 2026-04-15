import streamlit as st
from PIL import Image
import os

st.set_page_config(layout="centered")

# =========================
# ESCONDER SIDEBAR
# =========================
if "logado" not in st.session_state:
    st.markdown("""
        <style>
            section[data-testid="stSidebar"] {display: none;}
        </style>
    """, unsafe_allow_html=True)

# =========================
# ESTILO PREMIUM
# =========================
st.markdown("""
<style>
body {
    background-color: #f4f6f9;
}

/* CARD CENTRAL */
.login-card {
    background: white;
    padding: 40px;
    border-radius: 18px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.08);
    max-width: 420px;
    margin: auto;
}

/* INPUTS */
div[data-testid="stTextInput"] input {
    border-radius: 10px;
    padding: 12px;
    font-size: 14px;
}

/* BOTÃO */
div.stButton > button {
    background: linear-gradient(90deg, #1d74d8, #1bb3d3);
    color: white;
    border: none;
    border-radius: 10px;
    height: 45px;
    font-weight: 600;
}

/* CENTRALIZA */
.block-container {
    padding-top: 80px;
}
</style>
""", unsafe_allow_html=True)

# =========================
# USERS
# =========================
USERS = {
    "admin": {"senha": "123", "plano": "premium"},
    "user": {"senha": "123", "plano": "free"},
    "lnosiqueira": {"senha": "fiap0316", "plano": "dev_admin"}
}

# =========================
# LOGO
# =========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(BASE_DIR, "..", "assets", "logo-totemmflex.png")

# =========================
# LOGIN
# =========================
if "logado" not in st.session_state or not st.session_state["logado"]:

    st.markdown('<div class="login-card">', unsafe_allow_html=True)

    # LOGO
    if os.path.exists(logo_path):
        logo = Image.open(logo_path)
        st.image(logo, width=180)
    else:
        st.error("Logo não encontrada")

    st.markdown("<br>", unsafe_allow_html=True)

    # INPUTS
    usuario = st.text_input("", placeholder="Usuário")
    senha = st.text_input("", type="password", placeholder="Senha")

    st.markdown("<br>", unsafe_allow_html=True)

    # BOTÃO
    if st.button("Entrar", use_container_width=True):
        if usuario in USERS and USERS[usuario]["senha"] == senha:
            st.session_state["logado"] = True
            st.session_state["usuario"] = usuario
            st.session_state["plano"] = USERS[usuario]["plano"]
            st.rerun()
        else:
            st.error("Usuário ou senha inválidos")

    st.markdown('</div>', unsafe_allow_html=True)

    st.stop()