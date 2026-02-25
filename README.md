# 🟦 FIAP - Faculdade de Informática e Administração Paulista

```{=html}
<p align="center">
```
`<img src="src/assets/logo-fiap.png" width="40%" alt="FIAP">`{=html}
```{=html}
</p>
```
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

O TotemMFlex evolui o Totem-IA Educacional para um sistema corporativo
completo, integrando:

-   📡 Simulação de sensores\
-   🗃 Banco de dados estruturado (SQLite)\
-   🤖 Modelo de Machine Learning (RandomForest)\
-   🌐 API em FastAPI\
-   📊 Dashboard interativo em Streamlit\
-   ☁ Deploy em ambiente Cloud (AWS EC2)

O sistema consolida coleta, análise e visualização em um pipeline único
funcional.

------------------------------------------------------------------------

# 🔄 Pipeline Integrado

Simulador → Banco de Dados → Modelo ML → API → Dashboard → Score
Operacional

<<<<<<< HEAD
Integração superior a 60% dos módulos exigidos pela Sprint 3.
=======
# ☁️ Estrutura do Ambiente Cloud – TotemMFlex (AWS EC2)

```
TotemMFlex-Cloud/
├── src/
│   ├── backend/
│   │   ├── routers/
│   │   │   ├── health_router.py
│   │   │   ├── predict_router.py
│   │   │   ├── sensor_router.py
│   │   │   ├── status_router.py
│   │   │   └── voice_router.py
│   │   │
│   │   ├── services/
│   │   │   ├── data_service.py
│   │   │   ├── ml_service.py
│   │   │   ├── nlp_service.py   (se aplicável)
│   │   │   └── predict_service.py
│   │   │
│   │   ├── main.py
│   │   └── __init__.py
│   │
│   ├── __pycache__/
│   └── venv/
│
├── requirements.txt
├── application.py  (ou script usado no serviço)
└── (Serviço registrado no Windows como "TotemMFlex API Service")
```

---
>>>>>>> 4dad630eea77e447866e3c3468b07800c0a9a27d

------------------------------------------------------------------------

# 🏗 Estrutura do Projeto

TotemMFlex/ ├── data/ ├── diagrams/ ├── document/ ├── hardware/ └── src/
├── backend/ ├── dashboard/ ├── sensor_simulation/ ├── database/ └──
ml_model/

------------------------------------------------------------------------

# ▶ Como Executar -- Local

venv`\Scripts`{=tex}`\activate  `{=tex} pip install -r requirements.txt\
uvicorn src.backend.main:app --reload\
python src/sensor_simulation/simulator.py\
streamlit run src/dashboard/app.py

------------------------------------------------------------------------

# 📘 Evolução por Sprints

-   Sprint 1 --- document/README_SPRINT1.md\
-   Sprint 2 --- document/README_SPRINT2.md\
-   Sprint 3 --- document/README_SPRINT3.md

------------------------------------------------------------------------

# 📹 Demonstração em Vídeo

https://youtu.be/6F5Htntr5j8

------------------------------------------------------------------------

# 🏁 Conclusão

<<<<<<< HEAD
Sistema integrado validado localmente e em nuvem, com modelo preditivo,
análise estatística e score operacional aplicado.
=======
---

## 📹 Demonstração em Vídeo – Sprint 2

https://youtu.be/6F5Htntr5j8

---

# 🏁 **Conclusão**

A Sprint 2 consolidou o TotemMFlex como um MVP **real**, funcional, modular e pronto para expansão.  
O sistema opera em ambiente local e em nuvem, inclui ML, API, dashboard, banco e simulador — tudo validado e documentado.
>>>>>>> 4dad630eea77e447866e3c3468b07800c0a9a27d
