
# 🚀 DOCUMENTAÇÃO TÉCNICA + MANUAL DE EXECUÇÃO
# Projeto: TotemMFlex
## Sprint 3 – Integração de Machine Learning com API

Autor: Leno Siqueira  
Projeto acadêmico – FIAP

---

# 📌 1. Visão Geral do Projeto

O **TotemMFlex** é um sistema experimental que simula o funcionamento de um **totem inteligente com sensores**, capaz de:

• Receber dados de sensores  
• Classificar interações utilizando **Machine Learning**  
• Registrar todas as interações em **banco de dados SQLite**  
• Disponibilizar os dados através de uma **API REST (FastAPI)**  
• Exibir documentação automática via **Swagger**

Nesta Sprint 3 foi implementado:

✅ Treinamento de modelos de Machine Learning  
✅ Comparação entre modelos  
✅ Integração do modelo com API  
✅ Persistência das interações no banco  
✅ Histórico das interações  
✅ Evidências documentadas no GitHub

---

# 🧠 2. Arquitetura do Sistema

O projeto é dividido em quatro camadas principais.

## API Layer
Responsável pela comunicação externa.

Tecnologia:
FastAPI

Endpoints principais:
• `/status`
• `/predict`
• `/interactions`

---

## Machine Learning Layer

Responsável pelo treinamento, avaliação e execução do modelo.

Bibliotecas utilizadas:

• scikit-learn  
• pandas  
• numpy  

Modelos treinados:

• Random Forest  
• Logistic Regression  

Modelo escolhido para produção:

➡ Random Forest

Motivo:

Maior precisão e melhor desempenho na matriz de confusão.

---

## Data Layer

Responsável pela persistência das interações.

Banco utilizado:

SQLite

Arquivo do banco:

```
src/database/totem.db
```

Tabela principal:

```
interactions
```

Campos:

| Campo | Tipo | Descrição |
|-----|-----|-----|
id | integer | identificador |
sensor_type | text | tipo do sensor |
value | float | valor do sensor |
prediction | text | classificação |
created_at | datetime | data da interação |

---

# 📊 3. Fluxo de Funcionamento

Fluxo completo do sistema:

```
Sensor (simulado)
      ↓
API /predict
      ↓
Modelo ML (model.pkl)
      ↓
Classificação (toque_curto / toque_longo)
      ↓
Registro no SQLite
      ↓
Consulta via /interactions
```

---

# 🧪 4. Modelos de Machine Learning

Treinamento realizado no script:

```
src/ml_model/train_model.py
```

Avaliação realizada em:

```
src/ml_model/evaluate_model.py
```

Comparação entre modelos:

```
Random Forest
Logistic Regression
```

Resultado:

Random Forest apresentou melhor desempenho.

---

# 📉 5. Avaliação do Modelo

A avaliação foi realizada utilizando:

• Accuracy  
• Matriz de Confusão

Resultado observado:

Alta taxa de acerto para ambas classes.

Classes:

```
0 → toque_curto
1 → toque_longo
```

Imagem da matriz de confusão documentada no projeto.

---

# 🔌 6. API – Endpoints

Documentação automática disponível em:

```
http://127.0.0.1:8000/docs
```

---

## GET /status

Verifica o funcionamento da API.

Resposta esperada:

```
{
  "status": "ok",
  "service": "TotemMFlex API"
}
```

---

## POST /predict

Recebe valor do sensor e retorna classificação.

Exemplo de request:

```
{
  "valor": 0.85
}
```

Resposta:

```
{
  "valor_sensor": 0.85,
  "classificacao": "toque_longo"
}
```

Também registra automaticamente no banco de dados.

---

## GET /interactions

Lista todas as interações registradas.

Exemplo:

```
[
  {
    "id": 133,
    "sensor_type": "sensor_simulado",
    "value": 0.85,
    "prediction": "toque_longo",
    "created_at": "2026-03-04"
  }
]
```

---

# 🧰 7. Estrutura do Projeto

Estrutura principal:

```
TotemMFlex
│
├── data
├── diagrams
├── document
│   └── sprint3
│       └── evidencias
│
├── src
│   ├── backend
│   │   ├── routers
│   │   ├── services
│   │   └── main.py
│   │
│   ├── database
│   │   ├── create_db.py
│   │   └── totem.db
│   │
│   ├── ml_model
│   │   ├── train_model.py
│   │   ├── evaluate_model.py
│   │   ├── predict_model.py
│   │   └── model.pkl
│   │
│   └── sensor_simulation
│       └── simulator.py
│
└── requirements.txt
```

---

# ⚙️ 8. Manual Completo – Como Rodar do Zero

Este guia permite executar o projeto em qualquer máquina.

---

## 1️⃣ Clonar o repositório

```
git clone https://github.com/lnosiqueira/TotemMFlex.git
```

Entrar na pasta:

```
cd TotemMFlex
```

---

## 2️⃣ Criar ambiente virtual

Windows:

```
python -m venv venv
```

Ativar ambiente:

```
venv\Scripts\activate
```

---

## 3️⃣ Instalar dependências

```
pip install -r requirements.txt
```

---

## 4️⃣ Criar banco de dados

Executar:

```
python src/database/create_db.py
```

Isso irá gerar:

```
totem.db
```

---

## 5️⃣ Treinar o modelo

```
python src/ml_model/train_model.py
```

O modelo treinado será salvo como:

```
model.pkl
```

---

## 6️⃣ Avaliar modelos

```
python src/ml_model/evaluate_model.py
```

Este script compara:

• Random Forest  
• Logistic Regression

---

## 7️⃣ Subir a API

Executar:

```
uvicorn src.backend.main:app --reload
```

API disponível em:

```
http://127.0.0.1:8000
```

Swagger:

```
http://127.0.0.1:8000/docs
```

---

# 🧪 9. Testar a API

No Swagger:

Endpoint:

```
POST /predict
```

Enviar:

```
{
  "valor": 0.9
}
```

Resultado esperado:

```
toque_longo
```

Depois verificar histórico:

```
GET /interactions
```

---

# 🗄️ 10. Verificar Banco de Dados

Abrir arquivo:

```
src/database/totem.db
```

Utilizar ferramenta:

• DB Browser for SQLite

Tabela:

```
interactions
```

---

# 📸 11. Evidências da Sprint

Todas as evidências estão em:

```
document/sprint3/evidencias
```

Conteúdo:

• Swagger funcionando  
• Execução da API  
• Histórico de interações  
• Treinamento do modelo  
• Comparação entre modelos  
• Banco SQLite  
• Estrutura do projeto

---

# 📈 12. Evolução do Projeto

Sprint 1

Arquitetura inicial do sistema.

Sprint 2

Implementação da API e banco de dados.

Sprint 3

Integração completa com Machine Learning.

---

# 🏁 Conclusão

A Sprint 3 consolidou o funcionamento completo do sistema TotemMFlex, integrando:

• Machine Learning  
• API REST  
• Persistência de dados  
• Documentação e evidências

O projeto agora possui uma arquitetura funcional que permite evoluir para integração com sensores reais em ambientes físicos.

---

Projeto desenvolvido para fins acadêmicos.
