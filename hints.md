# Middleware Analysis Lab – Hints

If you are unsure how to interpret the generated plots, consider the following questions.

---

# Latency (LAN vs WAN)

Look at how latency changes between **LAN** and **WAN** conditions.

Ask yourself:

- Which middleware has the **lowest latency on LAN**?
- Which middleware's latency increases the **most when moving to WAN**?
- Which middleware appears **least affected by WAN conditions**?

Remember that some middleware is optimised for **local networks**, while others are designed for **distributed systems**.

---

# Jitter

Jitter measures **variability in message timing**.

Questions to consider:

- Which middleware shows the **lowest jitter**?
- Why might low jitter be important for **robot control systems**?

Think about systems that require **predictable communication timing**.

---

# CPU Usage

Look at how much CPU each middleware consumes.

Questions:

- Which middleware appears most **lightweight**?
- Why might CPU usage matter on **embedded robots** or **edge devices**?

---

# Latency vs Message Size

Look at how latency changes as **message size increases**.

Ask:

- Which middleware scales best with **larger messages**?
- Which one shows the **largest increase in latency**?

---

# LAN vs WAN Behaviour

One of the most important comparisons in this lab is how middleware behaves across different network environments.

Ask yourself:

- Which middleware appears **most resilient to WAN conditions**?
- Which middleware appears optimised for **local networks**?

---

# Scenario Questions

Use the plots to decide which middleware is most suitable for each system.

Consider the requirements:

|Scenario                |Key requirement                    |
|------------------------|-----------------------------------|
|Industrial robot        | predictable timing                |
|Research robot          | flexibility and ecosystem support |
|Distributed robot fleet | WAN communication                 |

Select the middleware that best fits the system constraints and explain why.

---

# Tip

You may find it useful to compare **relative differences**, not just absolute values.

For example:

- How much does latency increase from LAN to WAN?
- Which middleware degrades the least?