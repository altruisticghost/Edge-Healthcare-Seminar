# Edge-Healthcare-Seminar
A Python-based simulation demonstrating Edge Computing for real-time healthcare monitoring, designed to reduce latency in critical patient alerts.

Edge Computing in Smart Healthcare: Real-Time Patient Monitoring
Course: CSE435 - Comprehensive Seminar

Student Type: Non-Placed (Industry-Ready Project Track)

1. Project Overview
This project addresses the critical issue of "latency jitter" in traditional cloud-based healthcare monitoring systems. By implementing Edge Computing, we process vital signs closer to the source, reducing emergency alert delays from seconds to milliseconds.




2. Industry & Research Justification (CO1 & CO2)

Problem: Centralized cloud processing introduces a 2–5 second delay, which is critical during cardiac events.


Trend: Shift toward decentralized intelligent systems to save bandwidth and energy.



Research Basis: Findings synthesized from IEEE Xplore and ACM Digital Library regarding real-time data filtering.


3. Technology Stack (CO3)

Language: Python 3.x (Signal Analysis & Logic).



Simulation Hardware: Raspberry Pi (Edge Node Logic).


Communication: MQTT / WebSocket simulation for low-latency triggers.


Modern Tools: Git/GitHub for version control and Gamma AI for technical communication.


4. System Workflow (Bloom’s Level 3: Apply)

Data Capture: Wearable sensors collect heart rate (BPM) and SpO2 data.



Edge Analysis: Local node runs threshold-based logic to detect anomalies.



Local Alert: Immediate sirens/mobile notifications triggered upon detecting critical vitals.



Cloud Sync: Summarized, non-critical data is synced for long-term records.


5. Development Workflow Analysis
Methodology: Agile/Iterative development.


Version Control: Transparent commit history maintained to show progress from initial research to functional simulation.



Ethical Practice (PO8): Data privacy is ensured by processing raw sensitive health data locally rather than sending it to the public cloud.
