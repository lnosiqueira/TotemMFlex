import streamlit as st
import requests
import random

API_URL = "https://totemmflex.onrender.com"

st.title("TotemMFlex - Dashboard Inteligente")

if st.button("🚀 Gerar nova interação"):
    try:
        st.write("🔥 BOTÃO FOI CLICADO")

        # Gera um valor automático (simulação)
        valor = round(random.uniform(0, 1), 2)

        # Chama a API de predição
        response = requests.post(
            f"{API_URL}/predict",
            json={"valor": valor}
        )

        st.write("Status:", response.status_code)
        st.write("Resposta:", response.text)

        if response.status_code == 200:
            result = response.json()

            # Salva interação
            salvar = requests.post(
                f"{API_URL}/interactions/",
                json={
                    "sensor_type": "toque",
                    "valor": valor,
                    "classificacao": result["classificacao"],
                    "data": "2026-03-27 12:00:00"
                }
            )

            st.success("✅ Interação salva com sucesso!")

        else:
            st.error("Erro na predição")

    except Exception as e:
        st.error(f"Erro: {e}")