## test.csv

This is the dataset with simulated Twitter-like messages and metadata.

Sample columns:

* <strong>textID</strong>: unique identifier of the tweet.
* <strong>text</strong>: tweet content.
* <strong>sentiment</strong>: labeled sentiment (not used in classification, only for validation).
* Other metadata like Time of Tweet, Age of User, Country, etc.

## docker-compose-cluster-kafka.yml

### Purpose:
Sets up a local Kafka cluster with:

* 3 Kafka brokers
* 1 ZooKeeper
* Kafka UI to monitor topics

### Breakdown:

* kafka-ui: A web UI to monitor topics, consumers, and messages.
* zoo1: A single ZooKeeper instance.
* kafka1, kafka2, kafka3: Three Kafka brokers for high availability and replication.

### Ports:

* External ports like 9092, 9093, 9094 expose Kafka to the host.
* Internal ports 19092, 19093, 19094 are used inside Docker.

## Dockerfile

### Purpose:
Creates a container with Python + required libraries for running your producer and consumer code.

### Key Steps:

* Uses a lightweight python:3.12-slim base image.
* Installs:
    * kafka-python: Kafka client
    * transformers[torch]: Hugging Face Transformers + PyTorch
    * pandas: data handling
* Copies your data and src directories into /app/.
* Sets working directory to /app.
* Sleeps to keep the container running (ENTRYPOINT).

## config.py

### Purpose

Stores shared configuration for producer and consumer scripts.

### Breakdown

Dynamically selects internal Docker addresses or localhost depending on whether it's running inside Docker.

## producer.py

### Purpose:
Reads test.csv, preprocesses it, and sends messages to Kafka.

## consumer.py

### Purpose:

Consumes tweets from Kafka, runs sentiment analysis, logs results.

