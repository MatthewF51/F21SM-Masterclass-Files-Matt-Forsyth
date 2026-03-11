import csv
import random

SAMPLES = 300

middlewares = ["FastDDS", "CycloneDDS", "Zenoh"]
networks = ["LAN", "WAN"]
message_sizes = [1, 4, 16, 64]  # KB


def latency(middleware, network, size):

    base = size * 0.05

    if middleware == "CycloneDDS":
        base += 2
        jitter = random.gauss(0, 0.3)

    elif middleware == "FastDDS":
        base += 3
        jitter = random.gauss(0, 0.6)

    else:  # Zenoh
        base += 4
        jitter = random.gauss(0, 0.8)

    if network == "WAN":
        base *= 3

    return max(0.1, base + jitter)


def jitter(middleware):

    if middleware == "CycloneDDS":
        return abs(random.gauss(0.25, 0.1))

    if middleware == "FastDDS":
        return abs(random.gauss(0.45, 0.2))

    return abs(random.gauss(0.6, 0.25))


def packet_loss(network):

    if network == "LAN":
        return random.uniform(0, 0.1)

    return random.uniform(0.5, 3)


def throughput(middleware):

    if middleware == "CycloneDDS":
        return random.gauss(90, 5)

    if middleware == "FastDDS":
        return random.gauss(85, 6)

    return random.gauss(80, 7)


def cpu_usage(middleware):

    if middleware == "CycloneDDS":
        return random.gauss(18, 3)

    if middleware == "FastDDS":
        return random.gauss(25, 4)

    return random.gauss(20, 4)


rows = []

for m in middlewares:
    for n in networks:
        for s in message_sizes:
            for _ in range(SAMPLES):

                rows.append([
                    m,
                    n,
                    s,
                    round(latency(m, n, s), 3),
                    round(jitter(m), 3),
                    round(packet_loss(n), 3),
                    round(throughput(m), 2),
                    round(cpu_usage(m), 2)
                ])


with open("rmw_simulated_dataset.csv", "w", newline="") as f:

    writer = csv.writer(f)

    writer.writerow([
        "middleware",
        "network_condition",
        "message_size_kb",
        "latency_ms",
        "jitter_ms",
        "packet_loss_percent",
        "throughput_mbps",
        "cpu_usage_percent"
    ])

    writer.writerows(rows)

print("Dataset generated.")
