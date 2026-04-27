# Databricks notebook source
# Importes Bibliotecas 

from pyspark.sql.functions import *
from pyspark.sql.window import Window

from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import GBTRegressor
from pyspark.ml import Pipeline

# COMMAND ----------

# Feature Engineering (Engenharia de Recursos)

from pyspark.sql.functions import *
from pyspark.sql.window import Window
from pyspark.ml.feature import VectorAssembler, StringIndexer
from pyspark.ml.regression import GBTRegressor

# ========================
# FERIADOS
# ========================
feriados = [
    ("2024-01-01", "Ano Novo"),
    ("2024-12-25", "Natal")
]

df_feriados = spark.createDataFrame(feriados, ["data", "nome"])
df_feriados = df_feriados.withColumn("data", to_timestamp("data"))

# ========================
# FEATURE ENGINEERING
# ========================
def criar_features(df):

    df = df.join(df_feriados, "data", "left")

    df = df.withColumn("is_feriado", when(col("nome").isNotNull(), 1).otherwise(0))
    df = df.withColumn("campanha_ativa", when(rand() > 0.7, 1).otherwise(0))
    df = df.withColumn("promocao", when(rand() > 0.6, 1).otherwise(0))
    df = df.withColumn("tipo_campanha", when(rand() > 0.5, "A").otherwise("B"))

    df = df.withColumn("ano", year("data")) \
           .withColumn("mes", month("data")) \
           .withColumn("dia_semana", dayofweek("data"))

    window = Window.partitionBy("cliente_id").orderBy("data")

    df = df.withColumn("lag_1", lag("valor", 1).over(window))
    df = df.withColumn("media_3", avg("valor").over(window.rowsBetween(-3, 0)))

    return df.dropna()


def treinar_forecast(df):

    df = criar_features(df)

    indexer = StringIndexer(inputCol="tipo_campanha", outputCol="campanha_idx")
    df = indexer.fit(df).transform(df)

    features = [
        "ano","mes","dia_semana",
        "lag_1","media_3",
        "is_feriado","campanha_ativa",
        "campanha_idx","promocao"
    ]

    assembler = VectorAssembler(inputCols=features, outputCol="features")
    df = assembler.transform(df)

    train, test = df.randomSplit([0.8, 0.2])

    model = GBTRegressor(labelCol="valor", featuresCol="features", maxIter=50)
    modelo = model.fit(train)

    previsoes = modelo.transform(test)

    return modelo, previsoes


modelo, previsoes = treinar_forecast(df_vendas)
display(previsoes.select("cliente_id", "valor", "prediction"))f

# COMMAND ----------

# Preparação do Dataset

def preparar_dados(df):

    df = criar_features(df)

    # remove nulls (causados por lag)
    df = df.dropna()

    features = ["ano", "mes", "dia_semana", "lag_1", "media_3"]

    assembler = VectorAssembler(
        inputCols=features,
        outputCol="features"
    )

    df = assembler.transform(df)

    return df


# COMMAND ----------

# Treinamento do Modelo 

def treinar_modelo(df):

    df = preparar_dados(df)

    train, test = df.randomSplit([0.8, 0.2], seed=42)

    model = GBTRegressor(
        featuresCol="features",
        labelCol="valor",
        maxIter=50
    )

    modelo_treinado = model.fit(train)

    previsoes = modelo_treinado.transform(test)

    return modelo_treinado, previsoes


# COMMAND ----------

#Execução

modelo, previsoes = treinar_modelo(df_vendas)

display(previsoes.select("cliente_id", "valor", "prediction"))