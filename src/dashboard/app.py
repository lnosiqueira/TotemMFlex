import streamlit as st

# =========================
# CONFIG
# =========================
st.set_page_config(layout="wide")

# =========================
# ESCONDER MENU (ANTES LOGIN)
# =========================
hide_menu = """
<style>
[data-testid="stSidebarNav"] {display: none;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)

# =========================
# USERS
# =========================
USERS = {
    "admin": {"senha": "123", "plano": "premium"},
    "user": {"senha": "123", "plano": "free"},
    "lnosiqueira": {"senha": ,"lno@p0o9I*U&", "plano": "dev_admin"}
    "paulo": {"senha": "totem123", "plano": "dev_admin"}
    "math": {"senha": "totem123", "plano": "dev_admin"}
    "fred": {"senha": "fiap123", "plano": "dev_admin"}
}

# =========================
# SESSION INIT
# =========================
if "logado" not in st.session_state:
    st.session_state["logado"] = False

# =========================
# LOGIN
# =========================
if not st.session_state["logado"]:

    st.title("🔐 Login TotemMFlex")

    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        if username in USERS and USERS[username]["senha"] == password:
            st.session_state["logado"] = True
            st.session_state["usuario"] = username
            st.session_state["plano"] = USERS[username]["plano"]
            st.rerun()
        else:
            st.error("Usuário ou senha inválidos")

    st.stop()

# =========================
# MOSTRAR MENU (APÓS LOGIN)
# =========================
show_menu = """
<style>
[data-testid="stSidebarNav"] {display: block;}
header {visibility: visible;}
</style>
"""
st.markdown(show_menu, unsafe_allow_html=True)

# =========================
# HOME
# =========================
st.success(f"Bem-vindo, {st.session_state['usuario']} 👋")
st.write("Selecione uma página no menu lateral.")
