import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("rmw_simulated_dataset.csv")

print(data.head())

# Boxplot: latency by middleware
plt.figure()
data.boxplot(column="latency_ms", by="middleware")
plt.title("Latency Distribution by Middleware")
plt.suptitle("")
plt.xlabel("Middleware")
plt.ylabel("Latency (ms)")
plt.show()

# Average latency vs message size
avg_latency = data.groupby(["message_size_kb", "middleware"])["latency_ms"].mean().unstack()

plt.figure()
for middleware in avg_latency.columns:
    plt.plot(avg_latency.index, avg_latency[middleware], marker="o", label=middleware)

plt.title("Average Latency vs Message Size")
plt.xlabel("Message Size (KB)")
plt.ylabel("Average Latency (ms)")
plt.legend()
plt.show()

# Boxplot: jitter by middleware
plt.figure()
data.boxplot(column="jitter_ms", by="middleware")
plt.title("Jitter Comparison")
plt.suptitle("")
plt.xlabel("Middleware")
plt.ylabel("Jitter (ms)")
plt.show()

# Boxplot: CPU usage by middleware
plt.figure()
data.boxplot(column="cpu_usage_percent", by="middleware")
plt.title("CPU Usage by Middleware")
plt.suptitle("")
plt.xlabel("Middleware")
plt.ylabel("CPU Usage (%)")
plt.show()
