# 🎓 FIAP -- Global Solution • TotemMFlex

## Sprint 2 -- Backend FastAPI + Execução em Nuvem (AWS EC2)

**Versão atualizada --- Janeiro/2025**

------------------------------------------------------------------------

## 👥 Integrantes do Grupo (com LinkedIn)

-   **Leno Siqueira** -- https://www.linkedin.com/in/leno-siqueira/
-   **Adriano Santos**
-   **Victor Hugo**
-   **Lucas Souza**
-   **Vitor Dias**

------------------------------------------------------------------------

## 👨‍🏫 Professores

-   Marcelo Ruiz
-   Guilherme Brito
-   Claudio Bonel
-   Eduardo Mendes
-   Felipe Luiz

------------------------------------------------------------------------

## 🧠 Visão Geral

O TotemMFlex é a evolução do Totem-IA Educacional, agora como solução
corporativa inteligente executando em nuvem.

------------------------------------------------------------------------

## ☁️ Execução em Nuvem -- AWS EC2

-   Windows Server 2025
-   Python 3.11
-   FastAPI + Uvicorn
-   Execução automática via Task Scheduler
-   Porta 8000 liberada
-   IP Público: **18.191.224.166**

### URLs públicas:

-   http://18.191.224.166:8000
-   http://18.191.224.166:8000/docs
-   http://18.191.224.166:8000/status

------------------------------------------------------------------------

## 🔧 Arquitetura (Sprint 2 + Cloud)

    EC2 Windows → FastAPI/Uvicorn → Rotas → Swagger

------------------------------------------------------------------------

## 📁 Estrutura do Projeto

    TotemMFlex-Cloud/
    ├── src/backend/
    │   ├── main.py
    │   ├── routers/
    │   └── services/
    ├── .venv/
    ├── requirements.txt
    └── run_api.bat

------------------------------------------------------------------------

## 🟧 Entregáveis Sprint 2

-   Backend modular
-   Rotas: predict, sensor, voice, health, status
-   Simuladores
-   API online 24/7
-   Documentação completa
-   Execução automática

------------------------------------------------------------------------

## 🧪 Status On-line

    {"status":"online","message":"API TotemMFlex funcionando!"}

------------------------------------------------------------------------

## ⚙ Como Rodar Localmente

    python -m venv .venv
    .\.venv\Scriptsctivate
    pip install -r requirements.txt
    uvicorn src.backend.main:app --reload

------------------------------------------------------------------------

## 🧭 Próximos Passos (Sprint 3)

-   Modelo real de ML
-   Dashboard
-   ESP32 integrado
-   Autenticação JWT
-   HTTPS com Nginx

------------------------------------------------------------------------

## 🏆 Conclusão

A migração para a nuvem elevou o TotemMFlex ao nível corporativo,
tornando a API escalável, acessível e robusta.

------------------------------------------------------------------------

### 💜 Desenvolvido pela equipe TotemMFlex -- FIAP 2025

Com apoio do LA (ChatGPT)
