import json
import logging
import pandas as pd
from kafka import KafkaProducer
import config

# Configure logging to write producer events to a log file
import sys

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("producer.log")
    ]
)

# Initialize Kafka producer with JSON serializer
producer = KafkaProducer(
    bootstrap_servers=config.SERVERS,
    value_serializer=lambda m: json.dumps(m).encode("utf-8"),
)

# Callback on successful message delivery
def on_send_success(meta):
    logging.info(f"Successfully sent message to Topic: {meta.topic} - Offset: {meta.offset}")

# Callback on message delivery error
def on_send_error(ex):
    logging.error(f"Error while producing message to Kafka topic: {config.TOPIC}", exc_info=ex)

# Load and preprocess CSV data for sending
def load_data():
    df = pd.read_csv(config.DATASET_PATH, sep=",", encoding="latin1")
    # Remove rows with missing or empty 'text'
    df = df[df["text"].notnull() & (df["text"].str.strip() != "")]
    # Drop irrelevant columns based on name
    df = df.drop(columns=[col for col in df.columns if "sentiment" in col.lower() or "population" in col.lower() or "land" in col.lower() or "density" in col.lower()])
    return df.sample(n=config.SAMPLE_SIZE).to_dict("records")

# Main producer logic
def main():
    data_to_send = load_data()
    print(f"Loaded {len(data_to_send)} messages to send.")
    for msg in data_to_send:
        # Use country name as message key
        key = str(msg.get("Country", "unknown")).encode("utf-8")
        # Send message to Kafka topic
        producer.send(
            config.TOPIC,
            key=key,
            value=msg
        ).add_callback(on_send_success).add_errback(on_send_error)
    # Ensure all messages are flushed
    producer.flush()

if __name__ == "__main__":
    main()
