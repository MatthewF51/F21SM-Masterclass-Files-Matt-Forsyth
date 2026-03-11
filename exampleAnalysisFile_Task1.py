import os
import pandas as pd
import matplotlib.pyplot as plt


def main() -> None:
    # ----------------------------
    # Setup
    # ----------------------------
    input_file = "rmw_simulated_dataset.csv"
    output_dir = "plots"

    os.makedirs(output_dir, exist_ok=True)

    # ----------------------------
    # Load dataset
    # ----------------------------
    data = pd.read_csv(input_file)

    print("Dataset loaded successfully.\n")
    print("First 5 rows:")
    print(data.head(), "\n")

    print("Dataset summary:")
    print(data.describe(include="all"), "\n")

    # Ensure consistent middleware order across plots
    middleware_order = ["CycloneDDS", "FastDDS", "Zenoh"]

    # ----------------------------
    # Plot 1: Latency split by LAN/WAN
    # ----------------------------
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    lan_data = data[data["network_condition"] == "LAN"]
    wan_data = data[data["network_condition"] == "WAN"]

    lan_data.boxplot(
        column="latency_ms",
        by="middleware",
        ax=axes[0],
        positions=range(1, len(middleware_order) + 1),
    )
    axes[0].set_title("Latency (LAN)")
    axes[0].set_xlabel("Middleware")
    axes[0].set_ylabel("Latency (ms)")
    axes[0].set_xticklabels(middleware_order, rotation=0)

    wan_data.boxplot(
        column="latency_ms",
        by="middleware",
        ax=axes[1],
        positions=range(1, len(middleware_order) + 1),
    )
    axes[1].set_title("Latency (WAN)")
    axes[1].set_xlabel("Middleware")
    axes[1].set_ylabel("Latency (ms)")
    axes[1].set_xticklabels(middleware_order, rotation=0)

    plt.suptitle("")
    plt.tight_layout()
    plt.savefig(
        os.path.join(output_dir, "plot_latency_lan_vs_wan.png"),
        dpi=300,
        bbox_inches="tight",
    )
    plt.close()

    # ----------------------------
    # Plot 2: Jitter split by LAN/WAN
    # ----------------------------
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    lan_data.boxplot(
        column="jitter_ms",
        by="middleware",
        ax=axes[0],
        positions=range(1, len(middleware_order) + 1),
    )
    axes[0].set_title("Jitter (LAN)")
    axes[0].set_xlabel("Middleware")
    axes[0].set_ylabel("Jitter (ms)")
    axes[0].set_xticklabels(middleware_order, rotation=0)

    wan_data.boxplot(
        column="jitter_ms",
        by="middleware",
        ax=axes[1],
        positions=range(1, len(middleware_order) + 1),
    )
    axes[1].set_title("Jitter (WAN)")
    axes[1].set_xlabel("Middleware")
    axes[1].set_ylabel("Jitter (ms)")
    axes[1].set_xticklabels(middleware_order, rotation=0)

    plt.suptitle("")
    plt.tight_layout()
    plt.savefig(
        os.path.join(output_dir, "plot_jitter_lan_vs_wan.png"),
        dpi=300,
        bbox_inches="tight",
    )
    plt.close()

    # ----------------------------
    # Plot 3: CPU usage by middleware
    # ----------------------------
    plt.figure(figsize=(10, 6))
    data.boxplot(column="cpu_usage_percent", by="middleware")
    plt.title("CPU Usage by Middleware")
    plt.suptitle("")
    plt.xlabel("Middleware")
    plt.ylabel("CPU Usage (%)")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(
        os.path.join(output_dir, "plot_cpu_usage_by_middleware.png"),
        dpi=300,
        bbox_inches="tight",
    )
    plt.close()

    # ----------------------------
    # Plot 4: Average latency vs message size
    # ----------------------------
    avg_latency = (
        data.groupby(["message_size_kb", "middleware"])["latency_ms"]
        .mean()
        .unstack()
        .reindex(columns=middleware_order)
    )

    plt.figure(figsize=(10, 6))
    for middleware in avg_latency.columns:
        plt.plot(
            avg_latency.index,
            avg_latency[middleware],
            marker="o",
            linewidth=2,
            markersize=8,
            label=middleware,
        )

    plt.title("Average Latency vs Message Size")
    plt.xlabel("Message Size (KB)")
    plt.ylabel("Average Latency (ms)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(
        os.path.join(output_dir, "plot_latency_vs_message_size.png"),
        dpi=300,
        bbox_inches="tight",
    )
    plt.close()

    # ----------------------------
    # Plot 5: Average packet loss by middleware and network
    # ----------------------------
    packet_loss_summary = (
        data.groupby(["network_condition", "middleware"])["packet_loss_percent"]
        .mean()
        .unstack()
        .reindex(columns=middleware_order)
    )

    packet_loss_summary.plot(kind="bar", figsize=(10, 6))
    plt.title("Average Packet Loss by Network Condition")
    plt.xlabel("Network Condition")
    plt.ylabel("Average Packet Loss (%)")
    plt.xticks(rotation=0)
    plt.legend(title="Middleware")
    plt.grid(True, axis="y", alpha=0.3)
    plt.tight_layout()
    plt.savefig(
        os.path.join(output_dir, "plot_packet_loss_by_network.png"),
        dpi=300,
        bbox_inches="tight",
    )
    plt.close()

    # ----------------------------
    # Plot 6: WAN latency vs message size
    # ----------------------------

    wan_data = data[data["network_condition"] == "WAN"]

    wan_avg_latency = (
        wan_data.groupby(["message_size_kb", "middleware"])["latency_ms"]
        .mean()
        .unstack()
    )

    plt.figure(figsize=(10,6))

    for middleware in wan_avg_latency.columns:
        plt.plot(
            wan_avg_latency.index,
            wan_avg_latency[middleware],
            marker="o",
            linewidth=2,
            label=middleware
        )

    plt.title("WAN Latency vs Message Size")
    plt.xlabel("Message Size (KB)")
    plt.ylabel("Average Latency (ms)")
    plt.legend()
    plt.grid(True, alpha=0.3)

    plt.savefig(
        os.path.join(output_dir, "plot_wan_latency_vs_message_size.png"),
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    # ----------------------------
    # Summary tables for students
    # ----------------------------
    print("Mean latency by middleware and network condition:")
    mean_latency = (
        data.groupby(["network_condition", "middleware"])["latency_ms"]
        .mean()
        .unstack()
        .reindex(columns=middleware_order)
    )
    print(mean_latency, "\n")

    print("Mean jitter by middleware and network condition:")
    mean_jitter = (
        data.groupby(["network_condition", "middleware"])["jitter_ms"]
        .mean()
        .unstack()
        .reindex(columns=middleware_order)
    )
    print(mean_jitter, "\n")

    print("Mean CPU usage by middleware:")
    mean_cpu = data.groupby("middleware")["cpu_usage_percent"].mean().reindex(middleware_order)
    print(mean_cpu, "\n")

    latency_summary = (
        data.groupby(["network_condition", "middleware"])["latency_ms"]
        .mean()
        .unstack()
    )

    lan_latency = latency_summary.loc["LAN"]
    wan_latency = latency_summary.loc["WAN"]

    increase = wan_latency - lan_latency
    percent_increase = (increase / lan_latency) * 100

    summary_table = pd.DataFrame({
        "LAN_avg_latency_ms": lan_latency,
        "WAN_avg_latency_ms": wan_latency,
        "increase_ms": increase,
        "increase_percent": percent_increase
    })

    print("\nLatency increase from LAN → WAN:")
    print(summary_table.round(2))

    # ----------------------------
    # Plot 7: WAN increase comparison
    # ----------------------------

    increase.plot(kind="bar", figsize=(8,5))

    plt.title("Latency Increase from LAN to WAN")
    plt.xlabel("Middleware")
    plt.ylabel("Latency Increase (ms)")
    plt.xticks(rotation=0)
    plt.grid(axis="y", alpha=0.3)

    plt.savefig(
        os.path.join(output_dir, "plot_latency_increase_lan_to_wan.png"),
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()
    
    print(f"Plots generated successfully in the '{output_dir}' folder.")


if __name__ == "__main__":
    main()