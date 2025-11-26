import sqlite3
import pandas as pd
import streamlit as st

DB_PATH = "src/database/totem.db"

def load():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM interactions", conn)
    conn.close()
    return df

st.title("Dashboard – TotemMFlex Sprint 2")

df = load()

st.subheader("📌 Últimas Interações")
st.dataframe(df)

st.subheader("📊 Métricas")
if len(df) > 0:
    st.write("Total registros:", len(df))
    st.write("Toque curto:", len(df[df.prediction == "toque_curto"]))
    st.write("Toque longo:", len(df[df.prediction == "toque_longo"]))
else:
    st.info("Execute o simulador para gerar dados.")
