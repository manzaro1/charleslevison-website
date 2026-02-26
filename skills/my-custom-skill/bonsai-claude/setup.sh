#!/bin/bash

# Bonsai Claude Setup Script
# This script executes the Bonsai CLI setup and captures the authentication URL for Telegram notification

echo "🚀 Setting up Bonsai Claude CLI..."

# Step 1: Install Bonsai CLI
echo "Installing Bonsai CLI..."
npm install -g @bonsai-ai/cli

# Step 2: Login to Bonsai
echo "Logging into Bonsai..."
bonsai login

# Step 3: Start Claude and capture authentication URL
echo "Starting Claude Code session..."
echo "Waiting for authentication URL..."

# Start the session and capture the output
bonsai start claude 2>&1 | tee /tmp/bonsai_output.log &

# Wait a moment for the process to start
sleep 5

# Check if the process is running and capture any URLs
if pgrep -f "bonsai start claude" > /dev/null; then
    echo "✅ Bonsai Claude session started successfully"
    echo "📋 Check the output log for authentication URL"
    echo "📁 Log file: /tmp/bonsai_output.log"
    
    # Look for URLs in the log file
    if [ -f "/tmp/bonsai_output.log" ]; then
        echo ""
        echo "🔍 Extracted URLs from log:"
        grep -oE 'https?://[^\s]+' /tmp/bonsai_output.log | head -5
    fi
else
    echo "❌ Failed to start Bonsai Claude session"
    exit 1
fi

echo ""
echo "📱 Please check the URLs above and send them to Charles via Telegram for activation"