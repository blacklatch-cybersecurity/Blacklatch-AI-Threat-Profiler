# ⚡ Blacklatch AI Threat Profiler v1

An AI-driven local SOC prototype that detects, classifies, and visualizes simulated cyber threats in real-time — built entirely in Python by **Blacklatch Cyber Defense**.

## 🧠 Overview

This project simulates and classifies security events (like brute-force logins, persistence tactics, data exfiltration, etc.) using machine learning and displays results on a live dashboard.

### System Architecture

┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│ generate_logs│ ---> │ profiler.py │ ---> │ profiles.json│ ---> │ Flask Web UI │
└──────────────┘ └──────────────┘ └──────────────┘ └──────────────┘


### Features
- AI-based threat classification (Recon, Persistence, Execution, Exfiltration)
- Real-time dashboard
- Offline local analysis (TinyDB + Flask)
- Extensible for packet capture or real log feed

## 🛠️ Setup
```bash
git clone https://github.com/blacklatch-cybersecurity/Blacklatch-AI-Threat-Profiler.git
cd Blacklatch-AI-Threat-Profiler
bash run.sh
