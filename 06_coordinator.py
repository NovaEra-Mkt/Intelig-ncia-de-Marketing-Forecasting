# Databricks notebook source
# 

def run_pipeline(df_vendas):

    # Customer
    rfm = run_customer_analytics(df_vendas)

    # Campanhas
    campanhas = gerar_campanhas(rfm)
    performance = analisar_campanhas(campanhas, rfm)

    # Forecast
    modelo, previsoes = treinar_forecast(df_vendas)

    # NBA
    nba = gerar_nba(rfm, campanhas)

    return {
        "rfm": rfm,
        "campanhas": performance,
        "forecast": previsoes,
        "nba": nba
    }


resultado = run_pipeline(df_vendas)

display(resultado["rfm"])
display(resultado["campanhas"])
display(resultado["forecast"])
display(resultado["nba"])