"""
PicoClaw Monitor - Module for OpenClaw to wake up PicoClaw
"""

import subprocess
import os

MONITOR_SCRIPT = "/home/charlesclaw/.openclaw/workspace/skills/my-custom-skill/picoclaw-monitor/picoclaw_monitor.py"

def is_picoclaw_running():
    """Check if PicoClaw gateway is running"""
    result = subprocess.run(
        ["pgrep", "-f", "picoclaw gateway"],
        capture_output=True
    )
    return result.returncode == 0

def wake_up_picoclaw():
    """Wake up PicoClaw by starting the gateway"""
    if is_picoclaw_running():
        return {"status": "already_running", "message": "PicoClaw is already running"}
    
    # Start picoclaw gateway
    workspace = "/home/charlesclaw/.picoclaw/workspace"
    result = subprocess.run(
        ["picoclaw", "gateway", "start"],
        cwd=workspace,
        capture_output=True,
        text=True
    )
    
    # Wait a moment
    import time
    time.sleep(3)
    
    if is_picoclaw_running():
        return {"status": "restarted", "message": "PicoClaw restarted successfully"}
    else:
        return {"status": "failed", "message": "Failed to restart PicoClaw", "error": result.stderr}

def get_status():
    """Get PicoClaw status"""
    running = is_picoclaw_running()
    return {
        "running": running,
        "status": "online" if running else "offline"
    }

# For testing
if __name__ == "__main__":
    print(get_status())
