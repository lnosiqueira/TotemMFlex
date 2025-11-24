# 🟦 TotemMFlex — Sprint 2 (Versão 2.0)

Challenge FlexMedia — FIAP 2025  
Repositório: https://github.com/lnosiqueira/TotemMFlex - Privado

## 📌 Controle de Versão

| Sprint | Versão | Status |
|--------|---------|--------|
| Sprint 1 | v1.0 | Finalizada |
| Sprint 2 | v2.0 | Atual |

## 1. Introdução — Sprint 2

Nesta Sprint, expandimos o ToteMFlex para um sistema funcional com sensores/simulação, banco SQL, análise de dados, dashboard, ML supervisionado, multi-tenancy, white-label, segurança e pipeline de voz.

## 2. Arquitetura v2.0

[Sensores/Simulação] → [Coletor Python] → [SQLite] → [ETL/Estatística] → [Dashboard] → [ML]

## 3. Multi-Tenancy + White-Label

Configuração por tenant via arquivos JSON.

## 4. Segurança Operacional

Segregação de dados, logs, LGPD, rate limiting, validações, gestão de segredos.

## 5. Pipeline de Voz

VAD, Noise Filtering e fallback automático para texto.

## 6. Simulação de Sensores

Código Python completo incluído na Sprint (omitido aqui por brevidade).

## 7. Dashboard

Streamlit com métricas e gráficos interativos.

## 8. Machine Learning

Classificação toque curto/longos usando RandomForest.

## 9. Métricas MVP

Operacionais e ML (acurácia, confusão, recall, precision).

## 10. Estrutura do Repositório

TotemMFlex/
 ├── sensor_simulation/
 ├── database/
 ├── analysis/
 ├── dashboard/
 ├── ml_model/
 ├── docs/
 ├── logs/
 └── README.md

## 11. Responsáveis Sprint 2

| Integrante | RM | Responsabilidade |
|-----------|-----|------------------|
| Leno Siqueira | RM567893 | Arquitetura, SQL, Dashboard |
| Fred Villagra | RM567187 | Sensores / Simulação |
| Paulo Benfica | RM567648 | ML / Limpeza de dados |
| Mateus Lima | RM568518 | Vídeo / Integração final |

## 12. Vídeo Sprint 2

Link será adicionado até 27/11.

## 13. Histórico Sprint 1 — v1.0

Conteúdo original mantido em docs/ ou arquivo anterior.
