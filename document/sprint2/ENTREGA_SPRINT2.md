# 📘 ENTREGA – SPRINT 2  
## TotemMFlex – FIAP + FlexMídia  
### Modelo Híbrido (FIAP + Técnico Profissional)

---

# 🟦 1. Identificação do Projeto

**Projeto:** TotemMFlex – Evolução do Totem IA Educacional  
**Sprint:** 2  
**Disciplina:** Challenge FlexMídia + AI Systems  
**Instituição:** FIAP  
**Turma:** 55 – Grupo S  

**Integrantes:**
- Leno Siqueira  
- Paulo Benfica  
- Fred Villagra  
- Mateus Lima  

---

# 🟩 2. Objetivo da Sprint 2

A Sprint 2 teve como objetivo transformar o protótipo inicial Totem-IA Educacional em uma solução técnica completa, modular e escalável: **TotemMFlex**.

Nesta sprint, implementamos:

- Arquitetura local 100% funcional  
- Deploy completo na AWS EC2 (Cloud)  
- API em FastAPI com múltiplos endpoints  
- ML básico de predição (toque curto/long)  
- Dashboard monitorável (Streamlit)  
- Banco de dados SQLite integrado  
- Simulador de sensores em tempo real  
- Execução da API como serviço automático no Windows Server  
- Documentação completa + prints + diagramas  

---

# 🧱 3. Arquitetura – Ambiente Local

![Arquitetura Local](../src/assets/prints/01_project_structure.png)

---

# 🔄 4. Fluxo de Dados (Sprint 2)

![Fluxo de Dados](../diagrams/fluxo_de_dados.png)

---

# 🌐 5. API Backend – FastAPI

A API fornece endpoints para:

| Endpoint | Método | Função |
|---------|--------|--------|
| `/status` | GET | Status geral da API |
| `/health` | GET | Health-check |
| `/predict` | POST | Predição do tipo de toque |
| `/sensor` | GET | Últimas leituras |
| `/voice` | GET | Simulação de status de voz |

### 🟦 Logs da API (Local)  
![API Logs](../src/assets/prints/03_api_backend_logs.png)

### 🟦 Status  
![API Status](../src/assets/prints/04_api_status.png)

### 🟦 Predição – Toque Curto  
![Predição Curto](../src/assets/prints/05_swagger_predict_curto.png)

### 🟦 Predição – Toque Longo  
![Predição Longo](../src/assets/prints/06_swagger_predict_longo.png)

---

# 📡 6. Simulador de Sensores

![Simulador](../src/assets/prints/07_simulator_running.png)

---

# 🗃 7. Banco de Dados (SQLite)

![Banco SQLite](../src/assets/prints/08_database_select.png)

---

# 📊 8. Dashboard – Monitoramento Local

![Dashboard Local](../src/assets/prints/09_dashboard_main.png)

---

# ☁️ 9. Arquitetura Cloud – AWS EC2

## 9.1 Instância Ativa  
![AWS EC2](../src/assets/prints/10_aws_EC2_instance.png)

## 9.2 API Como Serviço Automático (Windows Server)  
![Service Auto](../src/assets/prints/11_aws_service_auto.png)

## 9.3 Estrutura do Projeto na Nuvem  
![Estrutura Cloud](../src/assets/prints/12_aws_estrutura_cloud.png)

## 9.4 Swagger – Cloud  
![Swagger Cloud](../src/assets/prints/13_swagger_cloud.png)

## 9.5 Dashboard – Cloud  
![Dashboard Cloud](../src/assets/prints/14_dashboard_cloud.png)

---

# ⚙️ 10. Como Executar – Ambiente Local

### 1. Ativar ambiente virtual
```
venv/Scripts/activate
```

### 2. Instalar dependências
```
pip install -r requirements.txt
```

### 3. Iniciar API
```
uvicorn src.backend.main:app --reload
```

### 4. Rodar simulador
```
python src/sensor_simulation/simulator.py
```

### 5. Abrir dashboard
```
streamlit run src/dashboard/app.py
```

---

# ☁️ 11. Como Executar – Cloud (AWS)

1. Conectar via RDP  
2. Acessar pasta do projeto  
3. Ativar venv  
4. A API inicia automaticamente pelo serviço: NSSM 2.24 -    
   **TotemMFlex API Service**  
5. Acessar:
```
http://18.191.224.166:8000/status
http://18.192.224.166:8000/docs
http://18.191.224.166:8501
```
---

# 🏁 12. Conclusão

A Sprint 2 consolidou o TotemMFlex como um MVP real, robusto e escalável.

Com a união de:

- API  
- ML básico  
- Banco  
- Simulador  
- Dashboard  
- Arquitetura Local  
- Arquitetura Cloud  

O sistema está pronto para expansão, integração com hardware real e evolução futura nas próximas sprints.

---

# ✔ Arquivo gerado automaticamente por LA + Grupo S  
FIAP – Challenge FlexMídia 2025  
