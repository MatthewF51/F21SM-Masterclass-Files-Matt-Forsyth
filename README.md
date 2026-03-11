# F21SM-Masterclass-Files-Matt-Forsyth

## Overview

In this lab task, you will analyse performance data for different ROS2 middleware implementations.

The middleware systems included in this dataset are:

- **Fast DDS**
- **Cyclone DDS**
- **Zenoh**
(Others are available)

All three can be used through the **ROS 2 Middleware Interface (RMW)**, but they have different architectural design goals and performance characteristics.

The goal of this exercise is to:

- Explore how middleware behaviour changes under different conditions
- Interpret communication performance metrics
- Use this information to make architectural decisions about middleware selection

---

# Dataset
You can generate your own dataset with:
python csvGenerator.py

The dataset file is:
rmw_simulated_dataset.csv

It contains simulated performance measurements for multiple middleware implementations under different network conditions.

Each row represents one simulated communication measurement.

# Running the Analysis Script

A starter analysis script is provided:
exampleAnalysisFile_Task1.py


This script loads the dataset and generates several plots to help visualise the performance characteristics.

### Required Python Libraries

The script requires:
pandas
matplotlib

Which can be installed with:
pip install pandas matplotlib


### Running the Script
Run with:
python exampleAnalysisFile_Task1.py


After running, several plots will be generated inside a folder called:
/plots

---

# Generated Plots

The script produces several visualisations.

### 1. Latency (LAN vs WAN)

Shows how communication latency changes between local networks and wide-area networks.

This illustrates how different middleware responds to changes in network topology.

---

### 2. Jitter (LAN vs WAN)

Shows variability in communication timing.

Low jitter is important for real-time robotic control systems.

---

### 3. CPU Usage by Middleware

Shows estimated processing overhead of different middleware implementations.

This can influence middleware choice for embedded or resource-constrained systems.

---

### 4. Latency vs Message Size

Shows how communication latency scales with increasing message payload size.

---

### 5. Packet Loss Comparison

Shows how different network environments influence packet loss behaviour.

---

# Lab Tasks

Using the plots and dataset, answer the following questions.

### Latency

- Which middleware shows the lowest latency on LAN?
- How does latency change when moving from LAN to WAN?

### Jitter

- Which middleware shows the lowest jitter?
- Why might low jitter be important in robotic systems?

### Resource Usage

- Which middleware appears to use the least CPU?
- In what situations might CPU usage influence middleware choice?

### Network Behaviour

- How does WAN networking affect communication performance?
- Which middleware appears most resilient to network degradation?

---

# Scenario-Based Questions

Based on your analysis, choose a middleware implementation for each scenario and explain your reasoning.

### Scenario 1 – Industrial Robot

A robotic arm operating on a factory floor:

- deterministic control loops
- stable local network
- strict timing requirements

---

### Scenario 2 – Research Mobile Robot

A mobile robot operating in a robotics lab:

- multiple sensors
- moderate compute resources
- strong ROS ecosystem integration required

---

### Scenario 3 – Distributed Robot Fleet

A fleet of warehouse robots connected to a cloud monitoring system:

- robots deployed across multiple subnets
- routers and firewalls present
- distributed monitoring and coordination required

---
