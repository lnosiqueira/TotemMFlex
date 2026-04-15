import streamlit as st
from PIL import Image
import os

st.set_page_config(layout="centered")

# =========================
# ESCONDER MENU LATERAL
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
# CAMINHO DA LOGO
# =========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(BASE_DIR, "..", "assets", "logo-totemmflex.png")

# =========================
# CONTROLE VISUAL SENHA
# =========================
if "show_pass" not in st.session_state:
    st.session_state["show_pass"] = False

# =========================
# LOGIN
# =========================
if "logado" not in st.session_state or not st.session_state["logado"]:

    col1, col2, col3 = st.columns([1,4,1])

    with col2:

        # LOGO
        if os.path.exists(logo_path):
            logo = Image.open(logo_path)
            st.image(logo, use_container_width=True)
        else:
            st.error(f"Logo não encontrada: {logo_path}")

        st.markdown("<br>", unsafe_allow_html=True)

        # USUÁRIO
        usuario = st.text_input(
            "Usuário",
            placeholder="Usuário",
            label_visibility="collapsed"
        )

        # SENHA COM OLHO
        col_pass, col_eye = st.columns([10,1])

        with col_pass:
            senha = st.text_input(
                "Senha",
                type="default" if st.session_state["show_pass"] else "password",
                placeholder="Senha",
                label_visibility="collapsed"
            )

        with col_eye:
            if st.button("👁️"):
                st.session_state["show_pass"] = not st.session_state["show_pass"]
                st.rerun()

        st.markdown("<br>", unsafe_allow_html=True)

        # BOTÃO LOGIN
        if st.button("Entrar", use_container_width=True):
            if usuario in USERS and USERS[usuario]["senha"] == senha:
                st.session_state["logado"] = True
                st.session_state["usuario"] = usuario
                st.session_state["plano"] = USERS[usuario]["plano"]
                st.rerun()
            else:
                st.error("Usuário ou senha inválidos")

    st.stop()