# 🟦 TotemMFlex -- MVP Sprint 2 (FIAP + FlexMídia)

Sistema de predição e monitoramento com FastAPI, Streamlit e execução em
nuvem AWS EC2.

------------------------------------------------------------------------

# 🧠 Visão Geral

O TotemMFlex evoluiu do ambiente local para um ambiente profissional em
nuvem, mantendo arquitetura limpa e modular.

------------------------------------------------------------------------

# 🏗️ Arquitetura do Projeto -- Ambiente Local

    TotemMFlex/
    ├── data/
    ├── diagrams/
    ├── document/
    ├── hardware/
    ├── r_analysis/
    ├── src/backend/
    │   ├── routers/
    │   ├── services/
    │   ├── main.py
    │   └── __init__.py
    ├── application.py
    ├── requirements.txt
    └── venv/

------------------------------------------------------------------------

# ☁️ Arquitetura do Projeto -- AWS EC2

    TotemMFlex-Cloud/
    ├── src/backend/
    │   ├── routers/
    │   ├── services/
    │   ├── main.py
    │   └── __init__.py
    ├── requirements.txt
    ├── application.py
    └── .venv/

------------------------------------------------------------------------

# 🌎 API Rodando na Nuvem -- AWS

## Instância EC2 Ativa

![EC2](/mnt/data/aws_instancia_totemmflexcloud.PNG)

## Serviço Automático

![Service](/mnt/data/serviceauto_totemmflexcloud.PNG)

## Estrutura na Nuvem

![Estrutura](/mnt/data/estrutura_totemmflexcloud.PNG)

## Swagger Público

![Swagger](/mnt/data/http_swagger_totemmflexcloud.png)

------------------------------------------------------------------------

# 📊 Dashboard (Execução Local)

![Dashboard](/mnt/data/dashboard_totemmflexcloud.PNG)

------------------------------------------------------------------------

# 📡 Endpoints

  Método   Rota       Função
  -------- ---------- -----------------------------
  GET      /status    Status da API
  GET      /health    Health check
  GET      /predict   Predição
  GET      /sensor    Dados dos sensores
  GET      /voice     Simulação de comando de voz
  GET      /docs      Swagger

------------------------------------------------------------------------

# 👥 Equipe

-   **Leno Siqueira** -- https://www.linkedin.com/in/leno-siqueira/
-   (Adicionar os demais)

------------------------------------------------------------------------

# 👨‍🏫 Professores

-   (Adicionar conforme lista original)

------------------------------------------------------------------------

# 🏁 Conclusão

Entrega Sprint 2 completa: ✔ Ambiente local\
✔ Ambiente em nuvem\
✔ API com serviço automático\
✔ Arquitetura organizada\
✔ Dashboard funcional
