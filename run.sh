#!/usr/bin/env bash
cd "$(dirname "$0")"

# Activate or create venv
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi
source venv/bin/activate

# Install dependencies silently
pip install --upgrade pip >/dev/null 2>&1
pip install flask scikit-learn pandas tinydb >/dev/null 2>&1

# Stop old processes (if any)
pkill -f generate_logs.py >/dev/null 2>&1 || true
pkill -f profiler.py >/dev/null 2>&1 || true
pkill -f app.py >/dev/null 2>&1 || true

# Start components
nohup python3 generate_logs.py >/dev/null 2>&1 &
nohup python3 profiler.py >/dev/null 2>&1 &
python3 app/app.py
