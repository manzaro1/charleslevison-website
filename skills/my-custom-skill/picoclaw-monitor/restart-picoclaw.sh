#!/bin/bash
# restart-picoclaw.sh - Restart PicoClaw if stopped

LOG_FILE="/home/charlesclaw/.openclaw/workspace/logs/picoclaw-monitor.log"

# Check if picoclaw gateway is running
if pgrep -f "picoclaw gateway" > /dev/null; then
    echo "$(date '+%Y-%m-%d %H:%M:%S') - PicoClaw is running" >> "$LOG_FILE"
    exit 0
else
    echo "$(date '+%Y-%m-%d %H:%M:%S') - PicoClaw NOT running, restarting..." >> "$LOG_FILE"
    
    # Start picoclaw gateway
    cd /home/charlesclaw/.picoclaw/workspace
    picoclaw gateway start >> "$LOG_FILE" 2>&1 &
    
    # Wait a moment
    sleep 3
    
    # Verify it started
    if pgrep -f "picoclaw gateway" > /dev/null; then
        echo "$(date '+%Y-%m-%d %H:%M:%S') - ✅ PicoClaw restarted successfully" >> "$LOG_FILE"
        exit 0
    else
        echo "$(date '+%Y-%m-%d %H:%M:%S') - ❌ Failed to restart PicoClaw" >> "$LOG_FILE"
        exit 1
    fi
fi
