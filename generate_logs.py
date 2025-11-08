#!/usr/bin/env python3
import time, random

lines = [
    "User executed 'powershell -nop -w hidden -enc ...'",
    "Multiple failed SSH login attempts from 10.0.0.5",
    "DNS request for suspicious-domain[.]xyz",
    "Large upload to external IP 93.184.216.34",
    "New service installed: persistence agent",
    "Normal user login successful",
    "Scheduled task created running cmd.exe every minute",
    "Port scan from 192.168.1.50 seen on 5 ports",
    "Created compressed archive secret.zip and uploaded",
    "SSH login from known admin workstation"
]

log_file = "events.log"

while True:
    entry = random.choice(lines)
    print("[+] Log generated:", entry)
    with open(log_file, "a") as f:
        f.write(entry + "\n")
    time.sleep(random.uniform(1.0, 3.0))
