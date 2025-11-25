# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href="https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Administração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# TotemMFlex – Sistema Inteligente de Engajamento Corporativo
Challenge FlexMedia — FIAP 2025
Curso: Inteligência Artificial  
Repositório: https://github.com/lnosiqueira/TotemMFlex - Privado

## Grupo S – Turma 55

## 👨‍🎓 Integrantes
- <a href="https://www.linkedin.com/in/leno-siqueira-36789544?utm_source=share_via&utm_content=profile&utm_medium=member_ios">Leno Siqueira</a> — RM: 567893  
- <a href="https://www.linkedin.com/in/paulo-benfica-76057a7b">Paulo Benfica</a> — RM: 567648  
- <a href="https://www.linkedin.com/in/federico-villagra-97378838a">Fred Villagra</a> — RM: 567187  
- <a href="https://www.linkedin.com/in/math-penteado-1b4807200/">Mateus Lima</a> — RM: 568518  

## 👩‍🏫 Professores
### Tutor(a)
- <a href="https://www.linkedin.com/in/sabrina-otoni-22525519b?utm_source=share_via&utm_content=profile&utm_medium=member_ios">Sabrina Otoni FIAP</a>

### Coordenação
- <a href="https://www.linkedin.com/company/inova-fusca">André Godoi FIAP</a>

---

## 📜 Descrição

O **TotemMFlex** é um sistema inteligente voltado para ambientes corporativos, integrando IA generativa, sensores/simulações, análise de dados, dashboard gerencial e recursos de segurança corporativa.  
A solução permite registrar humor, engajamento, solicitações, ocorrências e percepções de colaboradores por meio de um **totem físico** conectado a serviços Azure, banco SQL e dashboards interativos.

---

## 📁 Estrutura de Pastas
- **.github/** — automações  
- **assets/** — imagens e arquivos estáticos  
- **config/** — parâmetros do sistema  
- **document/** — documentos das entregas  
- **scripts/** — scripts auxiliares  
- **src/** — código-fonte completo (backend, sensores, ML, dashboard)  
- **README.md** — documentação principal  

---

## 🔧 Como Executar o Código

### Pré-requisitos
- Python 3.10+  
- FastAPI  
- Streamlit  
- SQLite  
- Azure OpenAI  
- Scikit-Learn  

### Passo a passo

#### 1. Clonar o repositório:
```bash
git clone https://github.com/lnosiqueira/TotemMFlex
cd TotemMFlex
```

#### 2. Instalar dependências:
```bash
pip install -r requirements.txt
```

#### 3. Executar o backend:
```bash
uvicorn src.backend.main:app --reload
```

#### 4. Executar simulação de sensores:
```bash
python src/sensor_simulation/simulator.py
```

#### 5. Executar dashboard:
```bash
streamlit run src/dashboard/app.py
```

---

## 🗃 Histórico de Lançamentos
- **2.0.0 — 27/11/2025**  
  Sprint 2: ML, simulação, dashboard, pipeline de voz, multi-tenant  

- **1.0.0 — 20/11/2025**  
  Sprint 1: Arquitetura, fluxo, MVP backend e protótipo  

---

## 📋 Licença
<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1">

Repositório baseado no modelo oficial FIAP, licenciado sob Creative Commons Attribution 4.0 International.
Esse projeto é intectualidade dos Integrantes desse grupo.
