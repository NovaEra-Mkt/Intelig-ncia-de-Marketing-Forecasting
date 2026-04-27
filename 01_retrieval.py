# Databricks notebook source
from pyspark.sql.functions import *
from pyspark.sql.types import *

def gerar_dados_fake():

    data = [
        ("C1", "2024-01-01", 100.0),
        ("C1", "2024-02-10", 150.0),
        ("C2", "2024-01-05", 50.0),
        ("C3", "2024-03-01", 300.0),
        ("C2", "2024-03-10", 80.0),
        ("C4", "2024-02-15", 200.0),
        ("C5", "2024-03-05", 120.0)
    ]

    schema = StructType([
        StructField("cliente_id", StringType(), True),
        StructField("data", StringType(), True),
        StructField("valor", DoubleType(), True),
    ])

    df = spark.createDataFrame(data, schema)
    df = df.withColumn("data", to_timestamp("data"))

    return df

df_vendas = gerar_dados_fake()

display(df_vendas)