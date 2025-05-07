import pandas as pd
import matplotlib.pyplot as plt

# Load the sentiment results
df = pd.read_csv("sentiment_results.csv")

# Count occurrences of each sentiment
sentiment_counts = df["sentiment"].value_counts()

# Plot a bar chart
plt.figure(figsize=(8, 5))
sentiment_counts.plot(kind="bar")
plt.title("Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Number of Tweets")
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.savefig("sentiment_distribution.png")
print("✅ Chart saved as 'sentiment_distribution.png'")