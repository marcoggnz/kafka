import logging
import sys
import config
import json
import torch
import time
import pandas as pd
from kafka import KafkaConsumer
from transformers import pipeline

# Configure logging to write consumer events to a log file
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("consumer.log")
    ]
)

# Initialize Kafka consumer
consumer = KafkaConsumer(
    config.TOPIC,
    group_id="py-group-test",
    bootstrap_servers=config.SERVERS,
    auto_offset_reset="earliest",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

# Load model ONCE globally
pipeline_ml = pipeline(
    "sentiment-analysis",
    model=config.MODEL_NAME,
    device=torch.device("cuda" if torch.cuda.is_available() else "cpu")
)

# Analyze the content of one Kafka message
def analyze_message(message, results):
    logging.info(f"Received message: {message.value}")

    raw_text = str(message.value.get("text", ""))
    # Skip empty or missing texts
    if not raw_text.strip():
        logging.warning(f"Empty or invalid text in message: {message.value}")
        return

    # Measure inference time
    start = time.time()
    sentiment_analysis = pipeline_ml(raw_text)[0]
    duration = time.time() - start

    # Store sentiment result with metadata
    results.append({
        "textID": message.value.get("textID", "unknown"),
        "text": raw_text,
        "sentiment": sentiment_analysis["label"],
        "score": sentiment_analysis["score"],
        "age": message.value.get("Age of User", "unknown"),
        "country": message.value.get("Country", "unknown"),
        "time_of_day": message.value.get("Time of Tweet", "unknown"),
        "processing_time": duration
    })

    logging.info(
        f"TextID: {message.value.get('textID')} | Sentiment: {sentiment_analysis['label']} | Score: {sentiment_analysis['score']} | Time: {duration:.2f}s"
    )

# Main loop to consume and process Kafka messages
def main():
    logging.info("Starting Kafka consumer ...")
    results = []
    try:
        for idx, message in enumerate(consumer, 1):
            analyze_message(message, results)
            # Save results every 10 messages
            if idx % 10 == 0:
                df = pd.DataFrame(results)
                df.to_csv("sentiment_results.csv", index=False)
                logging.info(f"Saved {idx} sentiment results to sentiment_results.csv")
    except KeyboardInterrupt:
        # Save any remaining data on shutdown
        logging.info("Shutting down Kafka consumer...")
        df = pd.DataFrame(results)
        df.to_csv("sentiment_results.csv", index=False)
        logging.info("Final sentiment results saved.")
        consumer.close()

if __name__ == "__main__":
    main()