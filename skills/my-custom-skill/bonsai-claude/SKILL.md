name: bonsai-claude
description: Use Bonsai AI's Claude Code CLI for facilitated coding sessions with agent collaboration (bob, charles, etc.). Executes terminal commands and captures authentication URLs for Telegram notification.
homepage: https://bonsai-ai.com
metadata: {"clawdbot":{"emoji":"🤖","requires":{"bins":["claude","curl","npm"],"npm":["@bonsai-ai/cli"]},"install":[{"id":"npm","kind":"npm","package":"@bonsai-ai/cli","label":"Install Bonsai CLI"},{"id":"curl","kind":"system","bins":["curl"],"label":"Install curl for Telegram notifications"}]}}

# Bonsai Claude Code CLI

Use Bonsai AI's Claude Code CLI for facilitated coding sessions with agent collaboration. This skill executes terminal commands to set up Bonsai and captures authentication URLs for Telegram notification, ensuring it uses Bonsai's own resources rather than consuming your model quota.

## Setup

### 1. Install Dependencies
```bash
# Install Bonsai CLI
npm install -g @bonsai-ai/cli

# Install curl (for Telegram notifications)
# On macOS: brew install curl
# On Ubuntu/Debian: sudo apt-get install curl
# On Windows: Download from https://curl.se/windows/
```

### 2. Configure Telegram (Optional)
Set up a Telegram bot for URL notifications:
1. Create a bot with @BotFather
2. Get your bot token
3. Get your chat ID (from @userinfobot)

### 3. Execute Setup Script
```bash
# Run the automated setup script
cd /home/charlesclaw/.picoclaw/workspace/skills/bonsai-claude
chmod +x setup.sh
./setup.sh
```

## Scripts

### setup.sh
Automates the Bonsai CLI setup:
```bash
#!/bin/bash
echo "🚀 Setting up Bonsai Claude CLI..."
npm install -g @bonsai-ai/cli
bonsai login
bonsai start claude 2>&1 | tee /tmp/bonsai_output.log &
```

### url_monitor.sh
Monitors for authentication URLs and sends them to Telegram:
```bash
#!/bin/bash
# Monitors Bonsai output and sends URLs to Telegram
# Requires Telegram bot configuration
```

## Usage Pattern

When given coding tasks, this skill enables:
- **Terminal execution** of Bonsai CLI commands
- **Authentication URL capture** and Telegram notification
- **Facilitated coding** through Bonsai's Claude Code CLI
- **Agent collaboration** (bob, charles, etc.) for complex tasks
- **Human intervention** points where Charles can directly assist
- **Distributed coding** approach rather than direct implementation

## Workflow

1. **Execute Bonsai setup** in terminal
2. **Capture authentication URL** when prompted
3. **Send URL to Telegram** for user activation
4. **Start Claude Code session** after activation
5. **Assign coding tasks** to the session
6. **Allow agents** (bob, etc.) to facilitate the work
7. **Intervene directly** when needed (Charles involvement)
8. **Review and approve** completed work

## Manual Execution

If you prefer manual execution:
```bash
# Install Bonsai CLI
npm install -g @bonsai-ai/cli

# Login to Bonsai
bonsai login

# Start Claude (this will show the authentication URL)
bonsai start claude
```

**Important:** When `bonsai start claude` shows the authentication URL, copy it and send it to Charles via Telegram for activation.

## Notes

- This skill uses Bonsai's own resources, not your model quota
- Authentication URLs are temporary and must be used promptly
- Telegram notifications require bot setup
- The setup script captures URLs in `/tmp/bonsai_output.log`
- Always check the log file for authentication URLs