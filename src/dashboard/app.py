import streamlit as st

# Simulação de usuários (depois vira banco)
USERS = {
    "admin": {"senha": "123", "plano": "premium"},
    "user": {"senha": "123", "plano": "free"}
}

def login():
    st.title("🔐 TotemMFlex Login")

    user = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        if user in USERS and USERS[user]["senha"] == senha:
            st.session_state["user"] = user
            st.session_state["plano"] = USERS[user]["plano"]
            st.success("Login realizado!")
            st.rerun()
        else:
            st.error("Credenciais inválidas")

if "user" not in st.session_state:
    login()
    st.stop()

st.sidebar.success(f"Logado como: {st.session_state['user']}")
st.sidebar.info(f"Plano: {st.session_state['plano']}")
