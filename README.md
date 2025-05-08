# Pipeline de Análisis de Sentimientos en Twitter con Kafka

Un sistema de análisis de sentimientos en tiempo real utilizando **Apache Kafka** y **Hugging Face Transformers**, impulsado por un clúster local de Kafka en Docker. Los tweets se simulan desde un archivo CSV y se analizan con un modelo BERT ajustado. Este proyecto forma parte del Máster en Big Data Architecture & Engineering en Datahack.

## Tecnologías Utilizadas

- **Python 3.12**
- **Apache Kafka** (mediante Docker Compose)
- **Kafka UI** para monitorización de topics
- **pandas** para el manejo de datos
- **transformers** de Hugging Face para NLP
- **PyTorch** (via `transformers[torch]`) como backend de ML
- **Docker Compose** para el clúster de Kafka
- **Matplotlib** para visualizaciones básicas
- **Kafka-Python** para producir/consumir mensajes

## Introducción

Este proyecto simula un flujo de Twitter en tiempo real mediante:
1. Lectura de mensajes desde un dataset (`test.csv`).
2. Producción de los mensajes a un tópico de Kafka (`x-data`).
3. Consumo de los mensajes usando un consumidor de Kafka.
4. Análisis de sentimientos de cada mensaje.
5. Guardado de resultados en un archivo CSV.
6. Visualización de la distribución de sentimientos.

Es ideal para aprender a integrar streaming de datos con pipelines de machine learning en Python.

## Instrucciones de configuración

### Requisitos previos

* Python 3.12 instalado
* Docker y Docker Compose instalados
* (Solo WSL) Añadir esto en ```/etc/hosts```:
```
127.0.0.1 kafka1 kafka2 kafka3
```

### Opción 1: Despliegue con un clic (Recomendado para desarrollo local)

1. Clonar el repositorio
```
git clone https://github.com/marcoggnz/datahack-kafka.git
cd datahack-kafka
```

2. Abrir una terminal y hacer el script ejecutable:

```
chmod +x run_pipeline.sh
```


3. Ejecutar toda la app:

```
./run_pipeline.sh
```

El script hará:
* Iniciar el clúster de Kafka vía Docker.
* Activar el entorno virtual de Python.
* Instalar las dependencias fijadas.
* Enviar tweets mediante el productor.
* Analizar esos tweets con el consumidor.
* Generar un gráfico de barras de sentimientos.

### Opción 2: Configuración manual
1. Clonar el repositorio
```
git clone https://github.com/marcoggnz/datahack-kafka.git
cd datahack-kafka
```

2. Iniciar el clúster de Kafka  
Iniciar el clúster local de Kafka + Zookeeper y Kafka UI usando Docker Compose:

```
docker compose -f images/docker-compose-cluster-kafka.yml up -d
```


3. Crear y activar un entorno virtual
```
python3 -m venv .venv
source .venv/bin/activate
```

4. Instalar dependencias de Python
```
pip install kafka-python==2.1.5 \
            transformers[torch]==4.51.0 \
            pandas==2.2.3 \
            matplotlib==3.8.4

```
O simplemente ejecutar:
```
pip install -r requirements.txt
```

5. Ejecutar el Productor
```
python src/producer.py
```

Esto enviará un lote de tweets simulados a Kafka.

6. Ejecutar el Consumidor (en una nueva terminal)
```
python src/consumer.py
```

Procesará los mensajes y guardará los resultados en **sentiment_results.csv**.

7. Visualizar los Resultados
```
python src/visualization.py
```

Esto generará **sentiment_distribution.png** mostrando el desglose de sentimientos.

8. Paso opcional de limpieza:

```
docker compose -f images/docker-compose-cluster-kafka.yml down
```

## Monitorización

Abrir Kafka UI en http://localhost:8080

## Estructura del Proyecto

```
├── data/
│   └── test.csv
├── images/
│   ├── docker-compose-cluster-kafka.yml
│   └── Dockerfile
├── src/
│   ├── config.py
│   ├── producer.py
│   ├── consumer.py
│   └── visualization.py
├── run_pipeline.sh           # Script de inicio con un clic 🟢
├── sentiment_results.csv     # Archivo de salida con predicciones
├── sentiment_distribution.png # Gráfico de resultados de sentimiento
├── producer.log              # Archivo de log
├── consumer.log              # Archivo de log
├── README.md                 # Estás aquí
└── .venv/                    # Entorno virtual (no se sube al repositorio)
```

## Notas

* El nombre del tópico, el tamaño de muestra y el modelo son configurables en config.py.
* Los logs se registran tanto en terminal como en archivos.
* Diseñado para desarrollo local, pero extensible para uso en la nube.

## Ideas de mejora

Hay muchas formas en las que este proyecto puede mejorar, ya que el objetivo principal es familiarizarse con el entorno y flujo de Kafka. Algunas posibles mejoras son:
* Construir un dashboard (por ejemplo, con Streamlit o Dash).
* Enviar resultados a una base de datos o API.
* Integrarse con plataformas Kafka gestionadas (como Confluent Cloud).