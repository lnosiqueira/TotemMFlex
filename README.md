# 🟦 FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
  <img src="src/assets/logo-fiap.png" width="40%" alt="FIAP">
</p>

# 🟩 TotemMFlex – Sistema Inteligente de Engajamento Corporativo

**Challenge FlexMídia — FIAP 2025**

📌 **Repositório Oficial (Privado):**  
https://github.com/lnosiqueira/TotemMFlex

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

# 🧠 Visão Geral

O TotemMFlex representa a evolução do Totem-IA Educacional para um ecossistema corporativo inteligente, integrando coleta de dados, processamento analítico e visualização estratégica em tempo real.

O sistema consolida:

- 📡 Simulação de sensores  
- 🗃 Banco de dados estruturado (SQLite)  
- 🤖 Modelo de Machine Learning (RandomForest)  
- 🌐 API REST desenvolvida em FastAPI  
- 📊 Dashboard interativo em Streamlit  
- ☁ Deploy validado em ambiente Cloud (AWS EC2)  

A arquitetura integra coleta, processamento e análise em um pipeline único e funcional.

---

# 🔄 Pipeline Integrado

Simulador → Banco de Dados → Modelo ML → API → Dashboard → Score Operacional

Integração superior a 60% dos módulos exigidos pela Sprint 3.

---

# ☁ Arquitetura em Nuvem (AWS EC2)

O sistema foi validado em ambiente Cloud utilizando AWS EC2, simulando um cenário corporativo real de deploy e operação contínua.

A aplicação executa:

- API em serviço ativo  
- Banco de dados integrado  
- Modelo preditivo carregado em runtime  
- Comunicação entre backend e dashboard  

---

# 🏗 Estrutura do Projeto

```text
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
```

---

# ▶ Como Executar – Ambiente Local

```bash
# Ativar ambiente virtual (Windows)
venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt

# Subir API
uvicorn src.backend.main:app --reload

# Rodar simulador
python src/sensor_simulation/simulator.py

# Rodar dashboard
streamlit run src/dashboard/app.py
```

---

# 📘 Histórico de Evolução por Sprints

- [Sprint 1](https://github.com/lnosiqueira/TotemMFlex/document/README_SPRINT1.md)
- [Sprint 2](https://github.com/lnosiqueira/TotemMFlex/document/README_SPRINT2.md)
- [Sprint 3](https://github.com/lnosiqueira/TotemMFlex/document/README_SPRINT3.md) 

---

# 📹 Demonstração em Vídeo

https://youtu.be/6F5Htntr5j8

---

# 🏁 Conclusão

Sistema integrado validado localmente e em nuvem, com modelo preditivo, análise estatística e score operacional aplicado.

O TotemMFlex consolida conceitos de engenharia de software, ciência de dados e arquitetura em nuvem, demonstrando aplicabilidade prática em ambiente corporativo.
