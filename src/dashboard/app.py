import streamlit as st
import os
import base64

st.set_page_config(layout="wide")

# =========================
# SESSION
# =========================
if "logado" not in st.session_state:
    st.session_state["logado"] = False

# =========================
# ESCONDER SIDEBAR
# =========================
if not st.session_state["logado"]:
    st.markdown("""
        <style>
        section[data-testid="stSidebar"] {display: none;}
        </style>
    """, unsafe_allow_html=True)

# =========================
# USERS
# =========================
USERS = {
    "admin": {"senha": "123", "plano": "premium"},
    "user": {"senha": "123", "plano": "free"},
    "lnosiqueira": {"senha": "lno0316", "plano": "dev_admin"}
}

# =========================
# LOGO PATH
# =========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(BASE_DIR, "..", "assets", "logo-totemmflex.png")

# =========================
# LOGIN UI ESTILO SaaS
# =========================
if not st.session_state["logado"]:

    with open(logo_path, "rb") as f:
        logo_base64 = base64.b64encode(f.read()).decode()

    st.markdown(f"""
    <style>
    body {{
        background-color: #f5f6fa;
    }}

    .login-container {{
        display: flex;
        justify-content: center;
        align-items: center;
        height: 90vh;
    }}

    .login-box {{
        background: white;
        padding: 40px;
        border-radius: 20px;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.1);
        width: 400px;
        text-align: center;
    }}

    .logo {{
        width: 200px;
        margin-bottom: 20px;
    }}

    .input {{
        width: 100%;
        padding: 12px;
        margin: 10px 0;
        border-radius: 10px;
        border: 1px solid #ddd;
    }}

    .button {{
        width: 100%;
        padding: 12px;
        border-radius: 10px;
        border: none;
        background: linear-gradient(90deg, #007bff, #00c6ff);
        color: white;
        font-size: 16px;
        cursor: pointer;
        margin-top: 10px;
    }}
    </style>

    <div class="login-container">
        <div class="login-box">
            <img class="logo" src="data:image/png;base64,{logo_base64}">
            <form method="post">
                <input class="input" placeholder="Usuário">
                <input class="input" placeholder="Senha">
            </form>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # INPUTS STREAMLIT (LÓGICA REAL)
    usuario = st.text_input("Usuário", key="user_hidden", label_visibility="collapsed")
    senha = st.text_input("Senha", type="password", key="pass_hidden", label_visibility="collapsed")

    if st.button("Entrar", use_container_width=True):
        if usuario in USERS and USERS[usuario]["senha"] == senha:
            st.session_state["logado"] = True
            st.session_state["usuario"] = usuario
            st.session_state["plano"] = USERS[usuario]["plano"]
            st.rerun()
        else:
            st.error("Usuário ou senha inválidos")

    st.stop()

# =========================
# PÓS LOGIN
# =========================
st.sidebar.success(f"Usuário: {st.session_state['usuario']}")
st.sidebar.info(f"Plano: {st.session_state['plano']}")

if st.sidebar.button("Logout"):
    st.session_state["logado"] = False
    st.rerun()

st.title("🚀 TotemMFlex Analytics")
st.write("Agora sim você tem uma tela nível SaaS de verdade.")