# 🟦 FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
  <img src="src/assets/logo-fiap.png" width="40%" alt="FIAP">
</p>
# 🟩 TotemMFlex -- Sistema Inteligente de Engajamento Corporativo

**Challenge FlexMídia --- FIAP 2025**

📌 **Repositório Oficial (Privado):**\
https://github.com/lnosiqueira/TotemMFlex

------------------------------------------------------------------------

## 👨‍🎓 Integrantes --- Grupo S (Turma 55)

-   Leno Siqueira --- RM: 567893\
-   Paulo Benfica --- RM: 567648\
-   Fred Villagra --- RM: 567187\
-   Mateus Lima --- RM: 568518

------------------------------------------------------------------------

## 👩‍🏫 Professores Responsáveis

Tutor(a): Sabrina Otoni\
Coordenador(a): André Godoi

------------------------------------------------------------------------

# 🧠 Visão Geral

O TotemMFlex representa a evolução do Totem-IA Educacional para um
ecossistema corporativo inteligente, integrando coleta de dados,
processamento analítico e visualização estratégica em tempo real.

O sistema consolida:

-   📡 Simulação de sensores\
-   🗃 Banco de dados estruturado (SQLite)\
-   🤖 Modelo de Machine Learning (RandomForest)\
-   🌐 API REST desenvolvida em FastAPI\
-   📊 Dashboard interativo em Streamlit\
-   ☁ Deploy validado em ambiente Cloud (AWS EC2)

A arquitetura integra coleta, processamento e análise em um pipeline
único e funcional.

------------------------------------------------------------------------

# 🔄 Pipeline Integrado

Simulador → Banco de Dados → Modelo ML → API → Dashboard → Score
Operacional

Integração superior a 60% dos módulos exigidos pela Sprint 3.

------------------------------------------------------------------------

# ☁ Arquitetura em Nuvem (AWS EC2)

O sistema foi validado em ambiente Cloud utilizando AWS EC2, simulando
um cenário corporativo real de deploy e operação contínua.

A aplicação executa:

-   API em serviço ativo\
-   Banco de dados integrado\
-   Modelo preditivo carregado em runtime\
-   Comunicação entre backend e dashboard

------------------------------------------------------------------------

# 🏗 Estrutura do Projeto

    TotemMFlex/
    │
    ├── data/
    ├── diagrams/
    ├── document/
    ├── hardware/
    └── src/
        ├── backend/
        ├── dashboard/
        ├── sensor_simulation/
        ├── database/
        └── ml_model/

------------------------------------------------------------------------

# ▶ Como Executar -- Ambiente Local

``` bash
# Ativar ambiente virtual (Windows)
venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt

# Subir API
uvicorn src/backend/main:app --reload

# Rodar simulador
python src/sensor_simulation/simulator.py

# Rodar dashboard
streamlit run src/dashboard/app.py
```

------------------------------------------------------------------------

# 📘 Histórico de Evolução por Sprints

-   Sprint 1 → document/README_SPRINT1.md\
-   Sprint 2 → document/README_SPRINT2.md\
-   Sprint 3 → document/README_SPRINT3.md

------------------------------------------------------------------------

# 📹 Demonstração em Vídeo

https://youtu.be/6F5Htntr5j8

------------------------------------------------------------------------

# 🏁 Conclusão

Sistema integrado validado localmente e em nuvem, com modelo preditivo,
análise estatística e score operacional aplicado.

O TotemMFlex consolida conceitos de engenharia de software, ciência de
dados e arquitetura em nuvem, demonstrando aplicabilidade prática em
ambiente corporativo.
