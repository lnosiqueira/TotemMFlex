# 🟦 ToteMFlex – Plataforma Inteligente para Ambientes de Trabalho Humanizados, Inclusivos e Sustentáveis  

### Global Solution – FIAP 2025.2  
### Grupo: (colocar nomes + RAs)

---

## 📌 Visão Geral

O **ToteMFlex** é uma plataforma inteligente que utiliza **IA, Machine Learning, Redes Neurais, IoT (opcional) e análise de dados** para promover:

- Bem-estar no ambiente de trabalho  
- Inclusão e acessibilidade  
- Engajamento dos colaboradores  
- Sustentabilidade e eficiência  

A solução se conecta com colaboradores, sensores e o ambiente, criando uma visão integrada da experiência de trabalho — apoiando organizações a tornarem o ambiente mais humano, seguro e produtivo.

---

## 🎯 Objetivo da POC

Demonstrar, de forma funcional, como tecnologias modernas podem:

- detectar padrões de bem-estar  
- gerar recomendações personalizadas  
- monitorar ambiente (sensores ou simulação)  
- analisar tendências usando ML e Redes Neurais  
- visualizar dados via Python e R  

---

## 🏛 Arquitetura (Visão Macro)

- **Frontend**: interface simples web (HTML/CSS/JS) para check-ins de bem-estar e visualização básica.  
- **Backend (Python)**: API em FastAPI/Flask que recebe dados, consulta modelos de ML/RN e retorna recomendações.  
- **IA / ML / RN**: modelos treinados em Python (scikit-learn, TensorFlow/Keras).  
- **Banco de Dados**: armazenamento de usuários, check-ins, sensores e recomendações.  
- **R**: análises estatísticas e gráficos para insights agregados.  
- **Cloud**: backend preparado para deploy em Azure App Service.  

---

## 📂 Estrutura do Projeto

```text
backend/        # API, modelos ML/RN, conexão com banco
data/           # dados brutos e tratados
r_analysis/     # scripts e plots em R
docs/           # PDF final, diagramas, documentação
hardware/       # (opcional) código e esquemas de sensores

---

## 🔧 Tecnologias Principais

Python, FastAPI/Flask, scikit-learn, TensorFlow/Keras

R (ggplot2, dplyr, etc.)

Banco de Dados (SQLite/PostgreSQL/Oracle)

Azure (deploy da API)

Git / GitHub

