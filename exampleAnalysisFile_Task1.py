import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("rmw_simulated_dataset.csv")

print(data.head())

# ----------------------------
# Plot 1: Latency by Middleware
# ----------------------------
plt.figure()
data.boxplot(column="latency_ms", by="middleware")
plt.title("Latency Distribution by Middleware")
plt.suptitle("")
plt.xlabel("Middleware")
plt.ylabel("Latency (ms)")
plt.savefig("plot_latency_by_middleware.png", dpi=300, bbox_inches="tight")
plt.close()


# ----------------------------
# Plot 2: Latency vs Message Size
# ----------------------------
avg_latency = data.groupby(["message_size_kb", "middleware"])["latency_ms"].mean().unstack()

plt.figure()

for middleware in avg_latency.columns:
    plt.plot(avg_latency.index, avg_latency[middleware], marker="o", label=middleware)

plt.title("Average Latency vs Message Size")
plt.xlabel("Message Size (KB)")
plt.ylabel("Average Latency (ms)")
plt.legend()

plt.savefig("plot_latency_vs_message_size.png", dpi=300, bbox_inches="tight")
plt.close()


# ----------------------------
# Plot 3: Jitter by Middleware
# ----------------------------
plt.figure()
data.boxplot(column="jitter_ms", by="middleware")
plt.title("Jitter Comparison")
plt.suptitle("")
plt.xlabel("Middleware")
plt.ylabel("Jitter (ms)")
plt.savefig("plot_jitter_by_middleware.png", dpi=300, bbox_inches="tight")
plt.close()


# ----------------------------
# Plot 4: CPU Usage by Middleware
# ----------------------------
plt.figure()
data.boxplot(column="cpu_usage_percent", by="middleware")
plt.title("CPU Usage by Middleware")
plt.suptitle("")
plt.xlabel("Middleware")
plt.ylabel("CPU Usage (%)")
plt.savefig("plot_cpu_usage_by_middleware.png", dpi=300, bbox_inches="tight")
plt.close()


print("Plots generated successfully.")
