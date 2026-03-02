# PicoClaw Gateway Monitor Skill

Monitors PicoClaw gateway and restarts it if stopped.

## Overview

This skill ensures PicoClaw is always running by:
1. Checking if PicoClaw gateway is running
2. Restarting it if not running
3. Sending notification when restarted

## Setup

The skill runs automatically via heartbeat or cron.

## Usage

### Check Status
```bash
picoclaw status
```

### Manually Restart
```bash
picoclaw gateway start
```

### Check if Running
```bash
ps aux | grep picoclaw
```

## Implementation

### Check Script
```bash
#!/bin/bash
# Check if picoclaw gateway is running

if pgrep -f "picoclaw gateway" > /dev/null; then
    echo "PicoClaw is running"
    exit 0
else
    echo "PicoClaw is NOT running - starting..."
    picoclaw gateway start
    exit 1
fi
```

### Auto-Restart Script
```bash
#!/bin/bash
# restart-picoclaw.sh

# Check if picoclaw is running
if ! pgrep -f "picoclaw gateway" > /dev/null; then
    echo "$(date): PicoClaw not running, restarting..."
    picoclaw gateway start
    echo "$(date): PicoClaw restarted" >> /var/log/picoclaw_restart.log
else
    echo "$(date): PicoClaw is running"
fi
```

## Cron Job

Add to crontab:
```bash
# Check PicoClaw every 5 minutes
*/5 * * * * /home/charlesclaw/.openclaw/workspace/skills/my-custom-skill/picoclaw-monitor/restart-picoclaw.sh
```

## Integration with OpenClaw

OpenClaw can call this skill to restart PicoClaw:
1. Check shared message file
2. Execute restart script
3. Confirm status

## Files

- `restart-picoclaw.sh` - Main restart script
- `check-status.sh` - Status check script
- `SKILL.md` - This file
