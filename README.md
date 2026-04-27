# Intelig-ncia-de-Marketing-Forecasting

# 📊 Marketing Intelligence & Next Best Action Platform

Plataforma de Inteligência de Marketing baseada em dados, com foco em **análise de clientes, campanhas e previsão de comportamento**, incluindo recomendações automatizadas (**Next Best Action**).


## 🎯 Objetivo

Transformar dados brutos em decisões estratégicas, permitindo:

* 📈 Previsão de vendas (Forecasting)
* 👤 Segmentação inteligente de clientes
* 📢 Análise de campanhas de marketing
* 🎯 Recomendação da melhor ação por cliente


## 🧠 Arquitetura

O projeto segue uma arquitetura modular baseada em pipelines de dados:


Dados → Customer Analytics → Campaign Analytics → Forecasting → NBA → Coordinator


### 🔹 Módulos

* **01_retrieval** → Ingestão de dados
* **02_customer_analytics** → Segmentação (RFM)
* **03_campaign_analytics** → Performance de campanhas
* **04_forecasting** → Modelo preditivo (Spark ML)
* **05_next_best_action** → Recomendações por cliente
* **06_coordinator** → Orquestração do pipeline


## 🏗️ Tecnologias

* Apache Spark (Databricks)
* PySpark
* Spark ML (Machine Learning)
* GitHub (versionamento)



## 📊 Funcionalidades

### 👤 Customer Analytics

* Segmentação RFM (Recência, Frequência, Valor)
* Classificação de clientes:

  * VIP
  * Frequente
  * Em risco
  * Normal


### 📢 Campaign Analytics

* Análise de conversão
* Performance por segmento
* Simulação de campanhas


### 📈 Forecasting (Machine Learning)

Modelo baseado em Gradient Boosting com:

* Features temporais (ano, mês, dia da semana)
* Lag de compras
* Média móvel
* Feriados
* Campanhas
* Promoções


### 🎯 Next Best Action (NBA)

Recomenda ações como:

* Oferecer produto premium
* Enviar desconto
* Campanha padrão


## 🔮 Diferencial

O modelo não considera apenas histórico de vendas, mas também:

* 📅 Sazonalidade (feriados)
* 📢 Ações de marketing
* 💰 Promoções

Permitindo simulação de cenários e decisões mais assertivas.


## 🚀 Como usar

1. Executar o módulo `01_retrieval`
2. Rodar os módulos em sequência:

   * Customer Analytics
   * Campaign Analytics
   * Forecasting
   * Next Best Action
3. Executar o `06_coordinator` para pipeline completo


## 📂 Estrutura do Projeto


/Marketing-Intelligence
│
├── 01_retrieval
├── 02_customer_analytics
├── 03_campaign_analytics
├── 04_forecasting
├── 05_next_best_action
└── 06_coordinator




## 📌 Próximos Passos

* Integração com dados reais
* Deploy de dashboard (Streamlit)
* Modelos avançados de previsão
* NBA com probabilidade de compra


## 💡 Conclusão

Este projeto demonstra uma abordagem moderna de análise de dados, integrando machine learning, análise de comportamento e recomendação automatizada para suportar decisões estratégicas de marketing.

