#!/bin/bash

echo "Starting Kafka cluster via Docker Compose..."
docker compose -f images/docker-compose-cluster-kafka.yml up -d

echo "Waiting for Kafka services to initialize..."
sleep 5  # give Kafka a moment to initialize

echo "Activating virtual environment..."
source .venv/bin/activate

echo "Installing dependencies..."
# Explicit version pinning
pip install --quiet \
    kafka-python==2.1.5 \
    transformers[torch]==4.51.0 \
    pandas==2.2.3 \
    matplotlib==3.8.4

echo "Sending tweets with the Kafka producer ..."
python src/producer.py

echo "Starting consumer with sentiment analysis..."
python src/consumer.py

echo "Generating sentiment distribution chart..."
python src/visualization.py

echo "Pipeline execution complete."
