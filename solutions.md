# F21SM Masterclass Lab Worked Solutions

## Overview

This file gives example answers for the ROS 2 middleware lab.

These are not the only correct answers. In several places, more than one answer can be reasonable if it is supported with evidence from the plots and dataset.

Use this file to check your thinking after completing the lab.

---

## Task 1, Analyse the Data

In Task 1, the goal is to look for patterns in the plots and dataset.

You were asked to make a few short, evidence-based observations. A good answer does not just name a middleware. It explains what the plots suggest and why that matters.

### Example observations

- Cyclone DDS shows the lowest latency on LAN in the simulated results.
- Cyclone DDS also has low jitter, which makes it appealing for systems that need predictable timing.
- Zenoh appears to degrade less when moving from LAN to WAN, so it looks more resilient in distributed environments.
- All middleware show higher latency when message size increases.
- WAN conditions increase latency, jitter, and packet loss compared to LAN.
- Cyclone DDS also appears to use less CPU than Fast DDS in this simulated dataset.

### What these observations mean

A key point from the dataset is that there is no single best middleware in every situation.

Cyclone DDS looks strongest for local, timing-sensitive communication.

Zenoh looks strongest when communication has to cross wider or more complex networks.

Fast DDS performs reasonably well overall, but in this simulated dataset it is not always the top performer.

### Example short answer

A strong Task 1 response could look like this:

Cyclone DDS has the best LAN latency and low jitter, which suggests it is well suited to local real-time communication. Zenoh shows a smaller increase in latency when moving from LAN to WAN, so it appears more resilient in distributed systems. All middleware become slower as message size increases. WAN conditions also cause higher jitter and packet loss than LAN. Cyclone DDS appears to have relatively low CPU usage, which could matter on resource-constrained systems.

---

## Task 2, Scenario-Based Middleware Selection

In Task 2, the goal is to choose a middleware for each deployment scenario and justify the choice using evidence from Task 1.

The important part is the reasoning. You should always match the middleware choice to the needs of the scenario.

---

### Scenario 1, Industrial Robot

A robotic arm operating on a factory floor:

- deterministic control loops
- stable local network
- strict timing requirements

### Example answer

Cyclone DDS is the best choice for this scenario.

The reason is that the dataset suggests Cyclone DDS gives the best latency and low jitter on LAN. Since this robot operates on a stable local network and has strict timing requirements, local predictability matters more than WAN resilience. That makes Cyclone DDS the strongest option.

### Why this answer fits

This scenario is focused on local performance and timing consistency. It does not need cloud communication or multi-subnet flexibility. That is why LAN behaviour matters most here.

---

### Scenario 2, Research Mobile Robot

A mobile robot operating in a robotics lab:

- multiple sensors
- moderate compute resources
- strong ROS ecosystem integration required

### Example answer

Cyclone DDS is a strong choice for this scenario, although Fast DDS could also be justified.

Cyclone DDS looks attractive because it performs well on latency and jitter and also appears to use relatively low CPU in the simulated data. That could be useful on a robot with moderate compute resources and multiple active sensors. Fast DDS could also be argued because it is a well-known general-purpose DDS option in ROS 2 systems, but based on this dataset Cyclone DDS has the stronger performance case.

### Why this answer fits

This scenario is more balanced than the first one. It is not only about hard timing, but also about handling several communication flows efficiently. That makes either Cyclone DDS or Fast DDS reasonable, as long as the answer is justified properly.

---

### Scenario 3, Distributed Robot Fleet

A fleet of warehouse robots connected to a cloud monitoring system:

- robots deployed across multiple subnets
- routers and firewalls present
- distributed monitoring and coordination required

### Example answer

Zenoh is the best choice for this scenario.

The main reason is that Zenoh appears to be more resilient when moving from LAN to WAN. The scenario includes multiple subnets, routers, firewalls, and cloud-connected coordination, so WAN and routed-network behaviour matter more than local-only latency. In the simulated results, Zenoh shows the smallest performance degradation across those conditions, which makes it the most suitable choice.

### Why this answer fits

This scenario is exactly the kind of case where wider-network communication becomes important. A middleware that works well only on a flat local network is less suitable here.

---

## Task 3, QoS Selection

In Task 3, the goal is to choose suitable QoS settings for common ROS 2 message types.

The main policies to think about are:

- reliability
- durability
- history
- depth

The key idea is that different message types have different priorities. Some need the newest data as quickly as possible. Others need guaranteed delivery. Others may need to be available to nodes that join later.

---

### 1. Camera Stream

### Example answer

- reliability: best effort
- durability: volatile
- history: keep last
- depth: low, such as 1 to 5

### Explanation

Camera data is usually high-rate and continuous. The newest frame matters more than receiving every single old frame. If one frame is dropped, the next one arrives soon after. Best effort is often appropriate because it avoids building up delays. Volatile also makes sense because late subscribers usually do not need old camera frames.

### Main idea

For camera streams, freshness matters more than guaranteed delivery.

---

### 2. Velocity Commands

### Example answer

- reliability: reliable
- durability: volatile
- history: keep last
- depth: low, such as 1 to 5

### Explanation

Velocity commands affect robot motion, so correct delivery is important. Reliable delivery therefore makes sense. Volatile is suitable because a late-joining subscriber should not suddenly receive old movement commands. A low depth also helps prevent outdated commands from piling up.

### Main idea

For control commands, safe and correct delivery matters, but stale commands should not be kept around.

Note:
In some cases, students may argue for best effort in very fast control loops where freshness matters more than retransmission. That can still be a reasonable argument if it is explained clearly.

---

### 3. Battery or Diagnostics Telemetry

### Example answer

- reliability: best effort or reliable, depending on justification
- durability: volatile
- history: keep last
- depth: low to moderate

### Explanation

Telemetry messages are useful for monitoring system health, but they are often updated frequently. Because of that, occasional packet loss may be acceptable, which makes best effort a reasonable choice. On the other hand, a student could also argue that important health messages should use reliable delivery. Both can be acceptable if the reasoning is clear.

### Main idea

This is a trade-off case. The most important thing is to explain why a certain delivery style is appropriate.

---

### 4. Task or Goal Completion Status

### Example answer

- reliability: reliable
- durability: transient local or volatile, depending on justification
- history: keep last
- depth: low

### Explanation

Completion or status messages are important because they tell the rest of the system that something has happened. Reliable delivery therefore makes sense. In many cases, transient local is also a good choice because a node that joins later may still need the latest status message. A student who chooses volatile can still be correct if they explain why late joining does not matter in their interpretation.

### Main idea

State-like messages often need stronger delivery guarantees, and sometimes they should remain available for late subscribers.

---

## What You Should Take Away From the Lab

This lab is really about matching communication choices to system needs.

You should now be able to see that:

- middleware choice depends on deployment context
- LAN performance and WAN resilience are not the same thing
- different message types need different QoS policies
- there is rarely one universal best answer for every robotic system

A strong robotics communication design is not about choosing the most popular option. It is about understanding the trade-offs and making choices that fit the system you are building.
