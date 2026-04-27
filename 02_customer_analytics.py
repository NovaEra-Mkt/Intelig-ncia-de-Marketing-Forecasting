# Databricks notebook source
# Importa bibliotecas

from pyspark.sql.functions import *
from pyspark.sql.window import Window

# COMMAND ----------

# Função para calcular RFM

from pyspark.sql.functions import *
from pyspark.sql.window import Window

def gerar_rfm(df_vendas):
    snapshot_date = df_vendas.select(max("data")).collect()[0][0]

    rfm = df_vendas.groupBy("cliente_id").agg(
        datediff(lit(snapshot_date), max("data")).alias("recencia"),
        count("*").alias("frequencia"),
        sum("valor").alias("valor_total")
    )
    return rfm


def segmentar_clientes(rfm):
    rfm = rfm.withColumn("r_score", ntile(5).over(Window.orderBy(desc("recencia")))) \
             .withColumn("f_score", ntile(5).over(Window.orderBy("frequencia"))) \
             .withColumn("v_score", ntile(5).over(Window.orderBy("valor_total")))

    rfm = rfm.withColumn(
        "segmento",
        when((col("v_score") >= 4) & (col("f_score") >= 4), "VIP")
        .when((col("f_score") >= 4), "Frequente")
        .when((col("r_score") >= 4), "Em risco")
        .otherwise("Normal")
    )

    return rfm


def run_customer_analytics(df_vendas):
    rfm = gerar_rfm(df_vendas)
    return segmentar_clientes(rfm)


rfm_final = run_customer_analytics(df_vendas)
display(rfm_final)

# COMMAND ----------

# Função Segmentação 

def segmentar_clientes(rfm):
    rfm = rfm.withColumn("r_score", ntile(5).over(Window.orderBy(desc("recencia")))) \
             .withColumn("f_score", ntile(5).over(Window.orderBy("frequencia"))) \
             .withColumn("v_score", ntile(5).over(Window.orderBy("valor_total")))

    rfm = rfm.withColumn(
        "segmento",
        when((col("v_score") >= 4) & (col("f_score") >= 4), "VIP")
        .when((col("f_score") >= 4), "Frequente")
        .when((col("r_score") >= 4), "Em risco")
        .otherwise("Normal")
    )

    return rfm

# COMMAND ----------

# Execução (Entrada → Saída)

def run_customer_analytics(df_vendas):
    rfm = gerar_rfm(df_vendas)
    rfm_segmentado = segmentar_clientes(rfm)
    return rfm_segmentado