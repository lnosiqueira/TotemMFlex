# 📊 Avaliação do Modelo – Sprint 3

Data de avaliação: Fevereiro/2026  
Base de teste: 100 amostras  
Distribuição das classes:
- toque_curto: 72%
- toque_longo: 28%

## Modelo Utilizado
RandomForestClassifier

## Métricas Obtidas

- Accuracy: 100%
- Precision: 100%
- Recall: 100%
- F1-Score: 100%

## Matriz de Confusão

|               | Previsto Curto | Previsto Longo |
|---------------|----------------|----------------|
| Real Curto    | 72             | 0              |
| Real Longo    | 0              | 28             |

## Interpretação Técnica

O modelo apresentou desempenho máximo na base de testes,
classificando corretamente 100% das interações.

A matriz de confusão demonstra ausência de falsos positivos
e falsos negativos.

Esse resultado indica que os dados simulados possuem
padrões bem definidos entre as classes "toque_curto"
e "toque_longo".

Entretanto, em cenários reais com maior ruído e variabilidade,
é esperado que a performance apresente pequenas variações.

O modelo demonstra consistência estatística dentro do escopo
da base simulada utilizada na Sprint 3.