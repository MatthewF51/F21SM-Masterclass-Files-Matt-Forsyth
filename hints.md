# Middleware Analysis Lab, Hints

If you are unsure how to interpret the generated plots, use the prompts below to guide your thinking.

The goal is not just to name a middleware. The goal is to explain what the plots suggest and why that matters for different robotic systems.

---

# Latency, LAN vs WAN

Look at how latency changes between **LAN** and **WAN** conditions.

Ask yourself:

- Which middleware has the **lowest latency on LAN**?
- Which middleware's latency increases the **most when moving to WAN**?
- Which middleware appears **least affected by WAN conditions**?

Think about what matters more in each case:

- **fast local communication**
- **resilience across wider networks**

Remember that some middleware is optimised more for **local network performance**, while others are better suited to **distributed systems**.

---

# Jitter

Jitter measures **variability in message timing**.

Questions to consider:

- Which middleware shows the **lowest jitter**?
- Why might low jitter be important for **robot control systems**?
- In what type of robot would predictable timing matter most?

Think about systems with:

- feedback loops
- motion control
- time-sensitive communication

---

# CPU Usage

Look at how much CPU each middleware consumes.

Ask:

- Which middleware appears most **lightweight**?
- Why might CPU usage matter on **embedded robots**, **mobile platforms**, or **edge devices**?
- Would CPU usage matter as much on a larger workstation or server?

Think about trade-offs between:

- performance
- efficiency
- available hardware resources

---

# Latency vs Message Size

Look at how latency changes as **message size increases**.

Ask:

- Which middleware scales best with **larger messages**?
- Which one shows the **largest increase in latency**?
- Would this matter more for **sensor data** or **small control messages**?

Try to connect message size to realistic ROS 2 data types, such as:

- camera streams
- LiDAR data
- telemetry
- command messages

---

# LAN vs WAN Behaviour

One of the most important comparisons in this lab is how middleware behaves across different network environments.

Ask yourself:

- Which middleware appears **most resilient to WAN conditions**?
- Which middleware appears optimised for **local networks**?
- Which middleware seems to degrade the least when moving away from an ideal local setup?

A middleware does not need to be the fastest on LAN to be the best choice for a distributed system.

---

# Task 1, Building Good Observations

For Task 1, try to write **3 to 5 short observations** based on the plots.

Good observations usually do one of these things:

- compare two or more middleware options
- describe how behaviour changes between LAN and WAN
- link a metric to a practical robotics consequence

Try to avoid writing only:

- "X is best"

Try to write things like:

- "X performs best on LAN, but Y degrades less on WAN"
- "CPU usage may make X more suitable for constrained platforms"
- "Larger messages increase latency for all middleware"

---

# Scenario Questions

Use the plots to decide which middleware is most suitable for each system.

Think carefully about the main constraint in each case.

| Scenario | Key requirement |
|----------|-----------------|
| Industrial robot | predictable timing on a stable local network |
| Research robot | balanced performance, moderate resources, good ROS integration |
| Distributed robot fleet | communication across wider, more complex networks |

Ask yourself:

- Does this scenario mainly care about **local timing**?
- Does it need to work well across **routers, firewalls, or multiple subnets**?
- Would **CPU usage** influence the decision?
- Is there an obvious trade-off between **local performance** and **distributed performance**?

Your answer should explain **why** the chosen middleware fits the scenario.

---

# Task 3, QoS Selection

For Task 3, focus on the purpose of the message.

You are choosing QoS settings for:

- camera stream
- velocity commands
- battery or diagnostics telemetry
- task or goal completion status

Think about these QoS policies:

- **reliability**
- **durability**
- **history**
- **depth**

Ask yourself:

- Does this message need **guaranteed delivery**, or is it acceptable to lose some messages?
- Is the **newest data** more important than receiving every old message?
- Should a **late-joining subscriber** receive the last message?
- Would a large queue create **stale data** or extra delay?

Helpful direction:

- A camera feed usually values **freshness**
- A control command usually values **correct delivery**
- Telemetry may depend on how critical the information is
- Status or completion messages may need to be seen by nodes that join later

---

# Tip

You may find it useful to compare **relative differences**, not just absolute values.

For example:

- How much does latency increase from LAN to WAN?
- Which middleware degrades the least?
- Which metrics matter most for the scenario you are answering?

A good answer is usually one that links the data to the needs of the robot system.
