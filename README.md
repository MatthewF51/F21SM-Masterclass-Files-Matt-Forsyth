# F21SM Masterclass Lab Files, Matt Forsyth

## Overview

In this lab, you will analyse simulated performance data for different ROS 2 middleware implementations.

The middleware systems included in this dataset are:

- Fast DDS
- Cyclone DDS
- Zenoh

All three can be used through the ROS 2 Middleware Interface, but they have different architectural goals and performance characteristics.

The dataset is simulated, not taken from a real benchmark. It is designed to help you identify meaningful middleware trade-offs across different network conditions.

The goals of this lab are to:

- explore how middleware behaviour changes under different conditions
- interpret communication performance metrics
- use evidence from the data to make middleware selection decisions
- apply QoS reasoning to common ROS 2 communication scenarios

---

## Files Included

This lab includes the following files:

- `csvGenerator.py`, generates the simulated dataset
- `rmw_simulated_dataset.csv`, the generated dataset
- `exampleAnalysisFile_Task1.py`, starter analysis script for Task 1
- `requirements.txt`, Python dependencies for the lab

---

## Setup

Install the required dependencies with:

```bash
pip install -r requirements.txt
```

---

## Dataset

You can generate a fresh dataset with:

```bash
python csvGenerator.py
```

The dataset file is:

```bash
rmw_simulated_dataset.csv
```

It contains simulated communication measurements for multiple middleware implementations under different network conditions.

Each row represents one simulated communication measurement.

The dataset includes:

- middleware
- network condition
- message size
- latency
- jitter
- packet loss
- throughput
- CPU usage

---

## Running the Analysis Script

A starter analysis script is provided:

```bash
exampleAnalysisFile_Task1.py
```

This script loads the dataset and generates several plots to help visualise the performance characteristics of each middleware.

Run the script with:

```bash
python exampleAnalysisFile_Task1.py
```

After running, several plots will be generated inside a folder called:

```bash
plots
```

---

## Generated Plots

The analysis script produces several visualisations to support your answers.

### 1. Latency, LAN vs WAN

Shows how communication latency changes between local networks and wide-area networks.

### 2. Jitter, LAN vs WAN

Shows variability in communication timing. Low jitter is especially important in systems that need predictable timing.

### 3. CPU Usage by Middleware

Shows estimated processing overhead for each middleware implementation. This can matter for embedded or resource-constrained systems.

### 4. Average Latency vs Message Size

Shows how communication latency scales as payload size increases.

### 5. Packet Loss by Network Condition

Shows how different middleware behave when packet loss becomes more likely, especially under WAN conditions.

### 6. WAN Latency vs Message Size

Focuses specifically on how WAN communication behaves as message size grows.

### 7. Latency Increase from LAN to WAN

Shows how much each middleware degrades when moving from a local network to a wider and more complex network environment.

---

## Task 1, Analyse the Data

Using the plots and dataset, answer the following questions.

Prepare 3 to 5 short, evidence-based observations from the plots and summary values.

### Latency

- Which middleware shows the lowest latency on LAN?
- How does latency change when moving from LAN to WAN?
- How does message size affect latency?

### Jitter

- Which middleware shows the lowest jitter?
- Why might low jitter be important in robotic systems?

### Resource Usage

- Which middleware appears to use the least CPU?
- In what situations might CPU usage influence middleware choice?

### Network Behaviour

- How does WAN networking affect communication performance?
- Which middleware appears most resilient to network degradation?
- What trade-offs do you notice between LAN performance and WAN resilience?

---

## Task 2, Scenario-Based Middleware Selection

Based on your analysis, choose a middleware implementation for each scenario and explain your reasoning.

Use evidence from Task 1 to justify each choice. Explain the trade-offs, not just the benefits.

### Scenario 1, Industrial Robot

A robotic arm operating on a factory floor:

- deterministic control loops
- stable local network
- strict timing requirements

### Scenario 2, Research Mobile Robot

A mobile robot operating in a robotics lab:

- multiple sensors
- moderate compute resources
- strong ROS ecosystem integration required

### Scenario 3, Distributed Robot Fleet

A fleet of warehouse robots connected to a cloud monitoring system:

- robots deployed across multiple subnets
- routers and firewalls present
- distributed monitoring and coordination required

---

## Task 3, QoS Selection

For each message type below, choose suitable QoS settings and briefly justify your choices.

Focus on these QoS policies:

- reliability
- durability
- history
- depth

Message types:

- camera stream
- velocity commands
- battery or diagnostics telemetry
- task or goal completion status

When answering, think about what matters most for each message type:

- fresh data
- guaranteed delivery
- bounded buffering
- whether late-joining subscribers need earlier messages

This task connects the middleware discussion to ROS 2 communication policy. Different message types have different priorities, so the same QoS settings will not always be appropriate.

---

## Expected Outcome

By the end of this lab, you should be able to:

- interpret middleware performance data
- explain how network conditions affect ROS 2 communication
- choose a suitable middleware for different deployment scenarios
- justify QoS choices for different ROS 2 message types

---