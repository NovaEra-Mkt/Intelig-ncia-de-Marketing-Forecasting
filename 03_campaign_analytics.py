# Databricks notebook source
# DBTITLE 1,Importando bibliotecas

from pyspark.sql.functions import *

def gerar_dados_campanha(df_clientes):
    # simulação simples
    campanhas = df_clientes.select("cliente_id").withColumn(
        "campanha", when(rand() > 0.5, "Promo A").otherwise("Promo B")
    ).withColumn(
        "respondeu", when(rand() > 0.6, 1).otherwise(0)
    )

    return campanhas

# COMMAND ----------

# DBTITLE 1,Analisando campanhas
from pyspark.sql.functions import *

def gerar_campanhas(df_clientes):
    return df_clientes.select("cliente_id").withColumn(
        "campanha", when(rand() > 0.5, "Promo A").otherwise("Promo B")
    ).withColumn(
        "respondeu", when(rand() > 0.6, 1).otherwise(0)
    )


def analisar_campanhas(df_campanhas, rfm):
    df = df_campanhas.join(rfm, "cliente_id")

    return df.groupBy("campanha", "segmento").agg(
        count("*").alias("total"),
        sum("respondeu").alias("respostas"),
        (sum("respondeu") / count("*")).alias("conversao")
    )


campanhas = gerar_campanhas(rfm_final)
performance = analisar_campanhas(campanhas, rfm_final)

display(performance)

# COMMAND ----------



# COMMAND ----------

