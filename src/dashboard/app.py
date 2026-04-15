import streamlit as st

st.set_page_config(layout="wide")

USERS = {
    "admin": {"senha": "123", "plano": "premium"},
    "user": {"senha": "123", "plano": "free"},
    "lnosiqueira": {"senha": "lno@p0o9I*U&", "plano": "dev_admin"}
}

if "logado" not in st.session_state:
    st.session_state["logado"] = False

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
            st.error("Login inválido")

    st.stop()

# Se passou daqui → está logado
st.success(f"Bem-vindo {st.session_state['usuario']}")
