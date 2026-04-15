import streamlit as st
from PIL import Image
import os

st.set_page_config(layout="centered")

# =========================
# ESCONDER MENU LATERAL (ANTES DO LOGIN)
# =========================
if "logado" not in st.session_state:
    st.markdown("""
        <style>
            section[data-testid="stSidebar"] {display: none;}
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
# CAMINHO DINÂMICO DA LOGO (NUNCA QUEBRA)
# =========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(BASE_DIR, "..", "assets", "logo-totemmflex.png")

# =========================
# LOGIN
# =========================
if "logado" not in st.session_state or not st.session_state["logado"]:

    col1, col2, col3 = st.columns([1,2,1])

    with col2:

        # LOGO (COM FALLBACK)
        if os.path.exists(logo_path):
            logo = Image.open(logo_path)
            st.image(logo, use_container_width=True)
        else:
            st.warning("Logo não encontrada. Verifique o caminho: src/assets/")

        st.markdown("<br>", unsafe_allow_html=True)

        # INPUTS
        usuario = st.text_input("Usuário")
        senha = st.text_input("Senha", type="password")

        if st.button("Entrar", use_container_width=True):
            if usuario in USERS and USERS[usuario]["senha"] == senha:
                st.session_state["logado"] = True
                st.session_state["usuario"] = usuario
                st.session_state["plano"] = USERS[usuario]["plano"]
                st.rerun()
            else:
                st.error("Usuário ou senha inválidos")

    st.stop()