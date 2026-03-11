import csv
import random

SAMPLES = 300

middlewares = ["FastDDS", "CycloneDDS", "Zenoh"]
networks = ["LAN", "WAN"]
message_sizes = [1, 4, 16, 64]  # KB


def latency(middleware: str, network: str, size: int) -> float:
    """
    Simulate latency in ms.
    Designed so:
    - CycloneDDS is best on LAN
    - FastDDS is moderate on LAN
    - Zenoh is slower on LAN
    - Zenoh degrades less on WAN
    """
    # Message size cost
    size_cost = size * 0.05

    if middleware == "CycloneDDS":
        base = 2.0 + size_cost
        noise = random.gauss(0, 0.35)
        wan_penalty = 3.0 + size * 0.06

    elif middleware == "FastDDS":
        base = 3.0 + size_cost
        noise = random.gauss(0, 0.55)
        wan_penalty = 4.2 + size * 0.07

    else:  # Zenoh
        base = 4.0 + size_cost
        noise = random.gauss(0, 0.65)
        wan_penalty = 1.8 + size * 0.035

    if network == "LAN":
        return max(0.1, base + noise)

    return max(0.1, base + wan_penalty + noise)


def jitter(middleware: str, network: str) -> float:
    """
    Simulate jitter in ms.
    CycloneDDS lowest, FastDDS moderate, Zenoh highest.
    WAN increases jitter for all, but DDS degrades more noticeably.
    """
    if middleware == "CycloneDDS":
        base = abs(random.gauss(0.22, 0.08))
        if network == "WAN":
            base += abs(random.gauss(0.18, 0.05))

    elif middleware == "FastDDS":
        base = abs(random.gauss(0.40, 0.14))
        if network == "WAN":
            base += abs(random.gauss(0.20, 0.07))

    else:  # Zenoh
        base = abs(random.gauss(0.55, 0.18))
        if network == "WAN":
            base += abs(random.gauss(0.08, 0.04))

    return max(0.0, base)


def packet_loss(middleware: str, network: str) -> float:
    """
    Simulate packet loss percent.
    WAN causes more packet loss overall.
    Zenoh is slightly more resilient in WAN scenarios.
    """
    if network == "LAN":
        return max(0.0, random.gauss(0.03, 0.02))

    if middleware == "Zenoh":
        return max(0.0, random.gauss(0.7, 0.25))

    if middleware == "CycloneDDS":
        return max(0.0, random.gauss(1.4, 0.45))

    return max(0.0, random.gauss(1.2, 0.40))  # FastDDS


def throughput(middleware: str, network: str, size: int) -> float:
    """
    Simulate throughput in Mbps.
    WAN reduces throughput for all.
    Zenoh holds up slightly better across WAN.
    """
    if middleware == "CycloneDDS":
        base = random.gauss(92, 5)

    elif middleware == "FastDDS":
        base = random.gauss(86, 6)

    else:  # Zenoh
        base = random.gauss(80, 6)

    # Larger messages can reduce effective throughput a little
    base -= size * 0.08

    if network == "WAN":
        if middleware == "Zenoh":
            base -= random.gauss(10, 2)
        else:
            base -= random.gauss(18, 3)

    return max(1.0, base)


def cpu_usage(middleware: str) -> float:
    """
    CPU usage mostly tied to middleware characteristics,
    not strongly to network type in this simple model.
    """
    if middleware == "CycloneDDS":
        return max(1.0, random.gauss(18, 3))

    if middleware == "FastDDS":
        return max(1.0, random.gauss(25, 4))

    return max(1.0, random.gauss(20, 4))  # Zenoh


rows = []

for middleware in middlewares:
    for network in networks:
        for size in message_sizes:
            for _ in range(SAMPLES):
                rows.append([
                    middleware,
                    network,
                    size,
                    round(latency(middleware, network, size), 3),
                    round(jitter(middleware, network), 3),
                    round(packet_loss(middleware, network), 3),
                    round(throughput(middleware, network, size), 2),
                    round(cpu_usage(middleware), 2),
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
        "cpu_usage_percent",
    ])
    writer.writerows(rows)

print("Dataset generated: rmw_simulated_dataset.csv")