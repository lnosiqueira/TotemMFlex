# 📘 Documentação Técnica — Sprint 3 (TotemMFlex)

> **Sprint 3:** Integração de Machine Learning + persistência de interações (SQLite) + evidências no Swagger/UI e banco.

---

## 1. Objetivo da Sprint 3

Nesta sprint foi implementado o **pipeline completo de Machine Learning**, integrando:

- **Treinamento e avaliação de modelos** (Random Forest e Regressão Logística)
- **Serialização do modelo escolhido** (`model.pkl`)
- **Endpoint de predição** consumindo o modelo treinado
- **Persistência das interações** (entrada do sensor e classe prevista) em **SQLite**
- **Endpoint de listagem de interações**
- **Evidências visuais** (Swagger + DB Browser) versionadas no GitHub

---

## 2. Arquitetura técnica (visão rápida)

**Camadas principais:**
- **API (FastAPI)**: expõe endpoints e Swagger UI
- **ML (scikit-learn)**: scripts de treino/avaliação e modelo serializado
- **Banco (SQLite)**: armazena histórico das interações
- **Simulador**: gera valores simulados para testes

**Fluxo (alto nível):**
1. Usuário/Simulador envia um valor via `POST /predict`
2. API carrega `model.pkl`, executa a predição
3. API grava a interação no `totem.db` (tabela `interactions`)
4. Usuário consulta histórico via `GET /interactions`

---

## 3. Estrutura de diretórios relevante

> A estrutura abaixo descreve apenas as partes usadas na Sprint 3.

```
src/
  backend/
    main.py
    routers/
    services/
  database/
    create_db.py
    totem.db
  ml_model/
    train_model.py
    evaluate_model.py
    predict_model.py
    model.pkl
    metrics_sprint3.txt
  sensor_simulation/
    simulator.py
document/
  sprint3/
    evidencias/
      00_swagger_status.png
      01_swagger_predict.PNG
      02_swagger_predict_response.PNG
      03_swagger_interactions.PNG
      04_model_training.PNG
      05_model_comparison.PNG
      06_sqlite_data.PNG
      07_project_structure.PNG
    README_SPRINT3.md
    avaliacao_modelo.md
    comparacao_modelos_ml.md
    matriz_confusao_sprint3.png
    modelo de comparacao.png
```

---

## 4. Modelos de Machine Learning

### 4.1 Dataset / Entradas
- A entrada do modelo é um **valor numérico (float)** representando a leitura do sensor (simulado).
- A saída é uma **classe**:
  - `toque_curto`
  - `toque_longo`

### 4.2 Modelos treinados
Foram treinados e avaliados:
- **Random Forest**
- **Logistic Regression**

### 4.3 Métricas e escolha do modelo
- O **Random Forest** apresentou melhor desempenho geral no cenário testado.
- As métricas de avaliação e validação cruzada foram registradas no terminal e podem ser mantidas em arquivo:
  - `src/ml_model/metrics_sprint3.txt`

> Evidência visual do processo:  
![Treinamento do Modelo](./evidencias/04_model_training.PNG)  
![Comparação de Modelos](./evidencias/05_model_comparison.PNG)

### 4.4 Artefato gerado
- Modelo final serializado em: `src/ml_model/model.pkl`

---

## 5. API (FastAPI) e Endpoints

### 5.1 Swagger UI
- Swagger disponível localmente em:  
  `http://127.0.0.1:8000/docs`

> Evidências:  
![Status no Swagger](./evidencias/00_swagger_status.png)  
![Endpoint /predict](./evidencias/01_swagger_predict.PNG)  
![Resposta do /predict](./evidencias/02_swagger_predict_response.PNG)  
![Histórico /interactions](./evidencias/03_swagger_interactions.PNG)

### 5.2 Endpoints implementados

#### ✅ `GET /status`
- Verifica saúde do serviço e retorna status/versão.

**Exemplo de resposta (200):**
```json
{
  "status": "ok",
  "service": "TotemMFlex API",
  "version": "3.0"
}
```

#### ✅ `POST /predict`
- Recebe um valor numérico e retorna a classificação prevista.
- Também grava a interação no SQLite.

**Request Body:**
```json
{
  "valor": 0.85
}
```

**Exemplo de resposta (200):**
```json
{
  "valor_sensor": 0.85,
  "classificacao": "toque_longo"
}
```

#### ✅ `GET /interactions`
- Lista todas as interações registradas no banco SQLite.

**Exemplo de resposta (200):**
```json
[
  {
    "id": 133,
    "sensor_type": "sensor_simulado",
    "value": 0.85,
    "prediction": "toque_longo",
    "created_at": "2026-03-04T15:53:58"
  }
]
```

---

## 6. Banco de Dados (SQLite)

### 6.1 Arquivo do banco
- Localização: `src/database/totem.db`

### 6.2 Tabela `interactions`
Campos (modelo esperado):
- `id` (inteiro, PK, autoincremento)
- `sensor_type` (texto) — ex.: `sensor_simulado`
- `value` (real) — valor numérico do sensor
- `prediction` (texto) — `toque_curto` ou `toque_longo`
- `created_at` (texto/datetime) — timestamp de inserção

> Evidência de consulta no DB Browser:  
![Dados no SQLite](./evidencias/06_sqlite_data.PNG)

### 6.3 Criação do banco
- Script: `src/database/create_db.py`  
Esse script cria a base e a tabela caso ainda não existam.

---

## 7. Simulador de Sensor

- Script: `src/sensor_simulation/simulator.py`
- Finalidade: gerar valores simulados para testar o endpoint `POST /predict` e popular o banco.

---

## 8. Como executar localmente

### 8.1 Preparar ambiente
No Windows (PowerShell / CMD), dentro da pasta do projeto:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 8.2 Treinar modelo (Sprint 3)
```bash
python src/ml_model/train_model.py
```

### 8.3 Avaliar modelos
```bash
python src/ml_model/evaluate_model.py
```

### 8.4 Subir a API
Exemplo (ajuste o import do app conforme seu `main.py`):

```bash
uvicorn src.backend.main:app --reload
```

Acesse:
- Swagger: `http://127.0.0.1:8000/docs`

---

## 9. Evidências e rastreabilidade

As evidências desta sprint estão versionadas em:

- Pasta: `document/sprint3/evidencias/`
- Documento principal: `document/sprint3/README_SPRINT3.md`
- Documentos de apoio:
  - `document/sprint3/avaliacao_modelo.md`
  - `document/sprint3/comparacao_modelos_ml.md`

> Observação: Para garantir que as imagens apareçam no GitHub, os links devem ser **relativos ao arquivo .md** (ex.: `./evidencias/nome.png`) e o nome do arquivo deve bater exatamente com maiúsculas/minúsculas.

---

## 10. Checklist final (Sprint 3)

- [x] Modelo treinado e salvo (`model.pkl`)
- [x] Avaliação comparativa (RF vs LR)
- [x] Endpoint `POST /predict` funcionando e registrando no SQLite
- [x] Endpoint `GET /interactions` listando histórico
- [x] Swagger validado com prints
- [x] Evidências no GitHub em pasta versionada

---

**Autor:** Leno Siqueira  
**Projeto:** TotemMFlex  
**Sprint:** 3
