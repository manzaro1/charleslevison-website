#!/usr/bin/env python3
"""
PicoClaw Monitor - Check and restart PicoClaw gateway
"""

import subprocess
import time
import os
from datetime import datetime

LOG_FILE = "/home/charlesclaw/.openclaw/workspace/logs/picoclaw-monitor.log"

def log(msg):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"{timestamp} - {msg}"
    print(line)
    with open(LOG_FILE, "a") as f:
        f.write(line + "\n")

def is_running():
    """Check if picoclaw gateway is running"""
    result = subprocess.run(
        ["pgrep", "-f", "picoclaw gateway"],
        capture_output=True
    )
    return result.returncode == 0

def restart():
    """Restart picoclaw gateway"""
    log("PicoClaw NOT running, restarting...")
    
    # Change to workspace and start
    workspace = "/home/charlesclaw/.picoclaw/workspace"
    subprocess.Popen(
        ["picoclaw", "gateway", "start"],
        cwd=workspace,
        stdout=open(LOG_FILE, "a"),
        stderr=subprocess.STDOUT
    )
    
    # Wait and verify
    time.sleep(3)
    
    if is_running():
        log("✅ PicoClaw restarted successfully")
        return True
    else:
        log("❌ Failed to restart PicoClaw")
        return False

def main():
    if is_running():
        log("PicoClaw is running ✅")
        return 0
    else:
        restart()
        return 1

if __name__ == "__main__":
    exit(main())
