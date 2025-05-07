import os

# Path to the dataset CSV file
DATASET_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "data", "test.csv"
)

# Number of tweet samples to send to Kafka
SAMPLE_SIZE = int(os.getenv("SAMPLE_SIZE", 10))

# Kafka topic name, configurable via environment variable
TOPIC = os.getenv("TOPIC_NAME", "x-data")

# Kafka broker addresses for Docker or local mode
SERVERS = (
    ["127.0.0.1:9092", "127.0.0.1:9093", "127.0.0.1:9094"]
    if os.environ.get("RUNTIME") != "docker"
    else ["kafka1:19092", "kafka2:19093", "kafka3:19094"]
)

# Hugging Face model name for sentiment analysis
MODEL_NAME = os.getenv("MODEL_NAME", "distilbert/distilbert-base-uncased-finetuned-sst-2-english")
