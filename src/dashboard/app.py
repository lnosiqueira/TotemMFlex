import streamlit as st
from PIL import Image
import os

st.set_page_config(layout="wide")

# =========================
# SESSION DEFAULT
# =========================
if "logado" not in st.session_state:
    st.session_state["logado"] = False

# =========================
# ESCONDER MENU LATERAL
# =========================
if not st.session_state["logado"]:
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
    "lnosiqueira": {"senha": "lno@p0o9I*U&", "plano": "dev_admin"}
}

# =========================
# CAMINHO DA LOGO
# =========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(BASE_DIR, "..", "assets", "logo-totemmflex.png")

# =========================
# LOGIN
# =========================
if not st.session_state["logado"]:

    col1, col2, col3 = st.columns([1,4,1])

with col2:
    st.markdown("<div style='text-align:center'>", unsafe_allow_html=True)
    st.image(logo, width=450)
    st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.error(f"Logo não encontrada em: {logo_path}")

        st.markdown("<br>", unsafe_allow_html=True)

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