import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv("rmw_simulated_dataset.csv")

# Preview data
print(data.head())

# --- Plot 1: Latency by Middleware ---
plt.figure()
sns.boxplot(data=data, x="middleware", y="latency_ms")
plt.title("Latency Distribution by Middleware")
plt.ylabel("Latency (ms)")
plt.xlabel("Middleware")
plt.show()


# --- Plot 2: Latency vs Message Size ---
plt.figure()
sns.lineplot(data=data, x="message_size_kb", y="latency_ms", hue="middleware")
plt.title("Latency vs Message Size")
plt.ylabel("Latency (ms)")
plt.xlabel("Message Size (KB)")
plt.show()


# --- Plot 3: Jitter Comparison ---
plt.figure()
sns.boxplot(data=data, x="middleware", y="jitter_ms")
plt.title("Jitter Comparison")
plt.ylabel("Jitter (ms)")
plt.xlabel("Middleware")
plt.show()


# --- Plot 4: CPU Usage ---
plt.figure()
sns.boxplot(data=data, x="middleware", y="cpu_usage_percent")
plt.title("CPU Usage by Middleware")
plt.ylabel("CPU Usage (%)")
plt.xlabel("Middleware")
plt.show()
