# Implementación de un Sistema de Análisis de Sentimiento de Comentarios en X con Apache Kafka

## Objetivo

El objetivo de la práctica es diseñar e implementar un sistema de análisis de sentimiento de comentarios en Twitter utilizando diversas funcionalidades de Apache Kafka. Este proyecto forma parte del Máster in Big Data Architecture & Engineering.

El proyecto ha sido dividido en tres etapas para ser abordado:

1. <strong>Extracción de datos</strong>: se ha llevado a cabo desde el dataset [Sentiment140 con 1.6M tweets](https://www.kaggle.com/datasets/kazanova/sentiment140) a un topic de Kafka. Se ha utilizado ese dataset ya que la API de X tiene limitado el acceso de forma gratuita.
2. <strong>Ánalisis de sentimientos</strong>: se ha realizado un análsis de sentimientos de los tweets en tiempo real mediante el [analizador de sentimientos](https://huggingface.co/blog/sentiment-analysis-python) localizado en el blog Hugging Face e implementado en Python.
3. <strong>Consumo de resultados</strong>: la información obtenida en el análisis se ha entregadod e vuelta a otro topic de Kafka para que sean consumidos por servicios como KSQLDB, MongoDB o Jupyter.

## Tecnologías Utilizadas

* Kafka
* Python
* Docker
* Jupyter
* MongoDB

## Manual de Despliegue

...

## Referencias

...
