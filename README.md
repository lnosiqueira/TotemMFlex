# 🟦 **ToteMFlex -- Plataforma Inteligente para Ambientes de Trabalho Humanizados, Inclusivos e Sustentáveis**

### **Global Solution -- FIAP 2025.2**

### **Curso: Inteligência Artificial**

------------------------------------------------------------------------

# 👥 **Integrantes do Grupo S**

  Nome                RM
  ------------------- ----------
  **Leno Siqueira**   RM567893
  **Fred Villagra**   RM567187
  **Paulo Benfica**   RM567648
  **Maria Mendes**    RM568563
  **Mateus Lima**     RM568518

------------------------------------------------------------------------

# 👩‍🏫 **Professores**

-   **Tutor(a):** Sabrina Otoni\
-   **Coordenador(a):** André Godoi

------------------------------------------------------------------------

# 📘 **1. Introdução**

O mundo do trabalho passa por transformações profundas impulsionadas por
Inteligência Artificial, automação, análise de dados e novos modelos
organizacionais. As organizações estão diante do desafio de criar
ambientes mais **humanos, inclusivos e sustentáveis**, ao mesmo tempo em
que buscam alta performance e equilíbrio emocional de seus
colaboradores.

Atendendo ao desafio proposto pela FIAP na *Global Solution 2025.2 -- O
Futuro do Trabalho*, desenvolvemos o **ToteMFlex**, uma plataforma
inteligente que integra:

-   Inteligência Artificial\
-   Machine Learning\
-   Redes Neurais\
-   Banco de Dados\
-   Computação em Nuvem\
-   R para análises estatísticas\
-   Cibersegurança\
-   (Opcional) IoT e sensores\
-   Automação cognitiva

Tudo isso para apoiar organizações a cuidar do bem-estar dos
colaboradores e criar locais de trabalho mais saudáveis.

------------------------------------------------------------------------

# 🎯 **2. Problema**

As empresas enfrentam desafios crescentes como:

-   Alto nível de estresse e burnout;\
-   Falta de acompanhamento contínuo do bem-estar;\
-   Baixo engajamento em iniciativas corporativas;\
-   Escassez de dados estruturados sobre clima e saúde emocional;\
-   Pouco uso de IA para apoio ao colaborador;\
-   Dificuldade em criar práticas inclusivas de forma sustentável.

Isso gera impactos em:

-   Produtividade\
-   Absenteísmo\
-   Cultura organizacional\
-   Saúde física e mental\
-   Rotatividade

------------------------------------------------------------------------

# 🎯 **3. Objetivos**

## **3.1 Objetivo Geral**

Desenvolver uma **Prova de Conceito (POC)** de uma plataforma
inteligente capaz de coletar, analisar e gerar recomendações
personalizadas de bem-estar e produtividade no ambiente de trabalho.

## **3.2 Objetivos Específicos**

-   Implementar IA, ML e Redes Neurais para análise de humor e risco.\
-   Desenvolver API em Python usando FastAPI.\
-   Criar um modelo de base de dados estruturado.\
-   Processar e visualizar dados com Python e R.\
-   Aplicar princípios de cibersegurança.\
-   Preparar deployment em Azure.\
-   Criar um MVP funcional para demonstração em vídeo.

------------------------------------------------------------------------

# 🧠 **4. Solução Proposta -- ToteMFlex**

O **ToteMFlex** é um sistema composto por:

-   **Camada de Coleta:** check-ins de humor, dados de ambiente,
    sensores opcionais (ESP32).\
-   **Camada de Processamento:** ML, RN, análise comportamental.\
-   **Camada de Inteligência:** recomendações automáticas e insights.\
-   **Camada de Visualização:** gráficos R, dashboard básico e API
    documentada.\
-   **Cloud:** backend pronto para deploy em Azure App Service.

------------------------------------------------------------------------

# 🏛 **5. Arquitetura da Solução (Visão Técnica)**

### **Frontend (Opcional / Futuro)**

-   HTML/CSS/JS simples\
-   Formulário de check-in\
-   Visualização de resultados

### **Backend (Python -- FastAPI)**

-   Rotas principais:
    -   `GET /` → Status\
    -   `POST /checkin` → Recebe humor, estresse, sono e processa\
    -   Futuro: /predict, /analytics, /riscos
-   Integrações:
    -   ML (scikit-learn)
    -   RN (TensorFlow/Keras)
    -   Banco de dados\
    -   Scripts R

### **IA / ML / RN**

-   Classificação de risco de estresse\
-   Rede neural MLP\
-   Pipeline de treinamento\
-   Dataset simulado para POC

### **Banco de Dados**

Tabelas:

  Tabela                Descrição
  --------------------- --------------------------
  colaboradores         registro dos usuários
  checkins_bem_estar    coleta diária
  sensores (opcional)   leituras IoT
  recomendacoes         retornos gerados pela IA

### **Computação em Nuvem**

-   Deploy do backend em Azure App Service\
-   GitHub Actions (futuro)\
-   Logs e monitoramento

### **Cibersegurança**

-   Boas práticas de API\
-   Validação de entrada\
-   Estrutura pronta para JWT\
-   Privacidade (LGPD)

------------------------------------------------------------------------

# 🗂 **6. Estrutura do Projeto**

    ToteMFlex/
    ├── backend/
    │   ├── main.py
    │   ├── requirements.txt
    │   ├── services/
    │   ├── models/
    │   └── database/
    ├── data/
    │   ├── raw/
    │   └── processed/
    ├── r_analysis/
    │   └── analysis.R
    ├── docs/
    │   └── arquitetura.png
    ├── hardware/
    │   └── esquema_esp32.png
    └── README.md

------------------------------------------------------------------------

# 📊 **7. Análises com R**

O diretório **r_analysis/** contém:

-   Script `analysis.R`\
-   Gráficos gerados automaticamente\
-   Exemplo:
    -   humor médio ao longo do tempo\
    -   dispersão de estresse\
    -   evolução temporal

------------------------------------------------------------------------

# 🤖 **8. Machine Learning / Redes Neurais**

Modelos implementados:

-   **Classificador supervisonado:** Logistic Regression / RandomForest\
-   **Rede Neural MLP:**
    -   Entrada: humor, estresse, sono\
    -   Ocultas: 2 camadas\
    -   Saída: risco (baixo / moderado / alto)

------------------------------------------------------------------------

# 🌐 **9. Deploy em Azure**

O projeto está preparado para:

-   Deploy via App Service\
-   Uso de `requirements.txt`\
-   Startup com `uvicorn`\
-   Integração GitHub → Azure

------------------------------------------------------------------------

# 📝 **10. Vídeo (AI Challenge)**

O vídeo conterá:

1.  Nome do grupo\
2.  Frase **"QUERO CONCORRER"**\
3.  Motivação e problema\
4.  Demonstração da API\
5.  Explicação das disciplinas\
6.  Conclusão\
7.  Link no PDF

------------------------------------------------------------------------

# 📘 **11. PDF Final -- Estrutura Base**

-   Capa\
-   Introdução\
-   Desenvolvimento\
-   Arquitetura\
-   Disciplinas integradas\
-   Prints do MVP\
-   Conclusão\
-   Link do vídeo\
-   Link do GitHub privado

------------------------------------------------------------------------

# © **Direitos**

Projeto acadêmico desenvolvido para a **FIAP -- Global Solution
2025.2**, turma de **Inteligência Artificial**.
