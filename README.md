# Kafka Twitter Sentiment Analysis Pipeline

A real-time sentiment analysis system using **Apache Kafka** and **Hugging Face Transformers**, powered by a local Kafka cluster in Docker. Tweets are simulated from a CSV file and analyzed using a fine-tuned BERT model.. This project is part of the Master's in Big Data Architecture & Engineering at Datahack.

## Technologies used

- **Python 3.12**
- **Apache Kafka** (via Docker Compose)
- **Kafka UI** for topic monitoring
- **pandas** for data handling
- **transformers** from Hugging Face for NLP
- **PyTorch** (via `transformers[torch]`) as ML backend
- **Docker Compose** for Kafka cluster
- **Matplotlib** for basic visualizations
- **Kafka-Python** for producing/consuming messages

## Introduction

This project simulates a real-time Twitter stream by:
1. Reading messages from a dataset (`test.csv`)
2. Producing them to a Kafka topic (`x-data`)
3. Consuming them using a Kafka consumer
4. Performing sentiment analysis on each message
5. Saving results to a CSV file
6. Visualizing the sentiment distribution

It’s ideal for learning how to integrate data streaming with machine learning pipelines in Python.


## Setup Instructions

### Option 1: One-Click Deployment (Recommended for Local Dev)

Just run the provided script from your terminal:

```
chmod +x run_pipeline.sh
./run_pipeline.sh
```

This will:
* Start the Kafka cluster
* Activate your Python virtual environment
* Install dependencies
* Send tweets using the producer
* Start the consumer for sentiment analysis

### Option 2: Manual Setup
1. Clone the repository
git clone https://github.com/marcoggnz/kafka-sentiment-pipeline.git
cd kafka-sentiment-pipeline

2. Start the Kafka Cluster
Start the local Kafka + Zookeeper cluster and Kafka UI using Docker Compose:

```
docker compose -f images/docker-compose-cluster-kafka.yml up -d
```

3. Create and Activate a Virtual Environment

```
python3 -m venv .venv
source .venv/bin/activate
```

4.  Install Python Dependencies

```
pip install kafka-python transformers[torch] pandas matplotlib
```

5.  Run the Producer

```
python src/producer.py
```

This will send a batch of simulated tweets to Kafka.

6. Run the Consumer (on a new terminal)

```
python src/consumer.py
```

It will process the messages and save results to **sentiment_results.csv**.

7. Visualize the Results

```
python src/visualization.py
```

This will generate sentiment_distribution.png showing the sentiment breakdown.

## Monitoring

Open Kafka UI at http://localhost:8080

## Project Structure

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
├── run_pipeline.sh              # One-click startup script 🟢
├── sentiment_results.csv        # Output file with predictions
├── sentiment_distribution.png   # Chart of sentiment results
├── producer.log                 # Log file
├── consumer.log                 # Log file
├── README.md                    # You are here
└── .venv/                       # Virtual environment (not committed)

## Notes

* Topic name, sample size, and model are configurable via config.py.
* Logs go to both the terminal and files.
* Designed for local dev but extensible for cloud use.

## Ideas for Improvement

There are plenty of ideas this project can be improved since the main goal is to get comfy with the Kafka environment and flow. However some room for improvement could be:
* Build a dashboard (e.g. Streamlit, Dash)
* Send results to a database or API
* Integrate with managed Kafka platforms (like Confluent Cloud)