
# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
  <a href="https://www.fiap.com.br/">
    <img src="src/assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Administração Paulista" width="40%" height="40%">
  </a>
</p>

# TotemMFlex – Evolução do Totem‑IA Educacional  
### *Sprint 2 – Sistema Inteligente de Engajamento Corporativo*
Challenge FlexMedia — FIAP 2025  
Repositório: https://github.com/lnosiqueira/TotemMFlex

> **Observação:**  
> O TotemMFlex é a **evolução direta** do projeto **Totem‑IA Educacional**, entregue na Sprint 1.  
> O arquivo oficial da Sprint 1 (**README_SPRINT1.md**) encontra‑se em:  
> `document/README_SPRINT1.md`

---

## 👨‍🎓 Integrantes — Grupo S (Turma 55)

- <a href="https://www.linkedin.com/in/leno-siqueira-36789544?utm_source=share_via&utm_content=profile&utm_medium=member_ios">Leno Siqueira</a> — RM: 567893  
- <a href="https://www.linkedin.com/in/paulo-benfica-76057a7b">Paulo Benfica</a> — RM: 567648  
- <a href="https://www.linkedin.com/in/federico-villagra-97378838a">Fred Villagra</a> — RM: 567187  
- <a href="https://www.linkedin.com/in/math-penteado-1b4807200/">Mateus Lima</a> — RM: 568518  

---

## 👩‍🏫 Professores Responsáveis

### Tutor(a) 
- <a href="https://www.linkedin.com/in/sabrina-otoni-22525519b?utm_source=share_via&utm_content=profile&utm_medium=member_ios/">Sabrina Otoni FIAP</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/company/inova-fusca/">André Godoi FIAP</a>

---

# 📜 Descrição Geral

O **TotemMFlex** representa a **segunda fase** do projeto iniciado na Sprint 1.  
Se antes o Totem‑IA Educacional tinha foco acadêmico, agora o TotemMFlex evolui para um **ecossistema corporativo inteligente**, incluindo:

- Backend FastAPI  
- Pipeline de predição (ML simplificado)  
- Simulação de sensores em tempo real  
- Banco SQLite persistindo interações  
- Dashboard Streamlit monitorando métricas  
- Arquitetura modular  
- Preparação para integração futura com Azure e serviços corporativos  

---

# 🧱 Arquitetura – Sprint 2

![Arquitetura](diagrams/arquitetura.png)

---

# 🔄 Fluxo de Dados

![Fluxo de Dados](diagrams/fluxo_de_dados.png)

---

# 📁 Estrutura Atualizada do Projeto

```
src/
 ├── assets/
 │    ├── logo-fiap.png
 │    └── prints/
 │         ├── api_backend_logs.png
 │         ├── api_status.png
 │         ├── dashboard_main.png
 │         ├── database_select.png
 │         ├── project_structure.png
 │         ├── simulator_running.png
 │         ├── swagger_predict_curto.png
 │         └── swagger_predict_longo.png
 │
 ├── backend/
 │    ├── main.py
 │    ├── routers/predict.py
 │    └── services/
 │         ├── database.py
 │         └── model.py
 │
 ├── dashboard/app.py
 ├── sensor_simulation/simulator.py
 ├── database/totem.db
 └── ml_model/model.py
```

---

# 🚀 Backend – FastAPI

Logs da inicialização da API:

![API Backend Logs](src/assets/prints/api_backend_logs.png)

---

## 🔎 Endpoint `/status`

![API Status](src/assets/prints/api_status.png)

---

## 🔮 Endpoint `/predict`

### Predição — exemplo 1  
![Swagger Predição Longo](src/assets/prints/swagger_predict_longo.png)

### Predição — exemplo 2  
![Swagger Predição Curto](src/assets/prints/swagger_predict_curto.png)

---

# 🗃 Banco de Dados (SQLite)

Consulta a registros armazenados:

![Database Select](src/assets/prints/database_select.png)

---

# 📡 Simulador de Sensores

![Simulador Rodando](src/assets/prints/simulator_running.png)

---

# 📊 Dashboard – Streamlit

![Dashboard](src/assets/prints/dashboard_main.png)

---

# ▶️ Como Executar o Projeto

1. Ativar venv  
```
venv\Scripts\activate
```

2. Instalar dependências  
```
pip install -r requirements.txt
```

3. Rodar API  
```
uvicorn src.backend.main:app --reload
```

4. Rodar simulador  
```
python src/sensor_simulation/simulator.py
```

5. Rodar dashboard  
```
streamlit run src/dashboard/app.py
```

---

# 📘 Referência da Sprint 1

Arquivo original:  
`document/README_SPRINT1.md`

---

# ✔️ Entregáveis Técnicos da Sprint 2

A Sprint 2 consolidou a evolução do Totem-IA Educacional para um ambiente corporativo inteligente.  
Os entregáveis técnicos incluídos foram:

- **Backend FastAPI completo**, com endpoints /status e /predict  
- **Pipeline de predição (ML simplificado)** para cenários de engajamento  
- **Banco de dados SQLite**, armazenando interações para análise posterior  
- **Simulador de sensores** gerando dados em tempo real  
- **Dashboard Streamlit** com visualização das métricas do sistema  
- **Estrutura de projeto reorganizada**, modular e escalável  
- **Diagramas atualizados**: Arquitetura e Fluxo de Dados  
- **Documentação completa**, integrando Sprint 1 + Sprint 2  
- **Conjunto completo de prints** demonstrando execução real do sistema

> O arquivo entrega Sprint 2 (**ENTREGA_SPRINT2.md**) encontra‑se em:  
> `document/ENTREGA_SPRINT2.md`

---

# 🏁 Conclusão

A Sprint 2 entregou um MVP completo com backend, ML, dashboard e simulação — uma evolução sólida rumo ao produto final.

