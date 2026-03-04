# 📊 Comparação de Modelos – Sprint 3

## Modelos Avaliados

- RandomForestClassifier
- LogisticRegression

## Resultados no Conjunto de Teste

### Random Forest
- Accuracy: 100%
- Performance perfeita nas classes
- Nenhum erro de classificação

### Logistic Regression
- Accuracy: 97%
- Pequena redução no recall da classe "toque_longo"

## Validação Cruzada (5-Fold)

### Random Forest
- Scores: [1.0, 1.0, 1.0, 1.0, 1.0]
- Média: 1.0
- Desvio padrão: 0.0

### Logistic Regression
- Scores: [0.97, 0.99, 0.98, 0.99, 0.98]
- Média: 0.982
- Desvio padrão: 0.007

## Análise Técnica

Ambos os modelos apresentaram desempenho elevado na base simulada.

Entretanto, o Random Forest demonstrou:

- Maior estabilidade estatística
- Menor variabilidade entre folds
- Melhor desempenho geral

Optou-se pela utilização do Random Forest
por sua robustez superior e melhor capacidade
de generalização em cenários potencialmente não lineares.