#!/bin/bash

# Bonsai URL Monitor Script
# Monitors Bonsai output for authentication URLs and sends them to Telegram

# Telegram configuration (replace with your actual chat ID and bot token)
TELEGRAM_CHAT_ID="1451738933"  # Your Telegram chat ID
TELEGRAM_BOT_TOKEN="your_bot_token_here"  # Replace with your actual bot token

# Function to send message to Telegram
send_telegram_message() {
    local message="$1"
    local url="https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage"
    
    curl -s -X POST "$url" \
        -H 'Content-Type: application/json' \
        -d "{\"chat_id\": \"$TELEGRAM_CHAT_ID\", \"text\": \"$message\", \"parse_mode\": \"Markdown\"}"
}

# Monitor Bonsai output for URLs
echo "🔍 Monitoring Bonsai output for authentication URLs..."

# Check if bonsai is running
if pgrep -f "bonsai start claude" > /dev/null; then
    echo "✅ Bonsai session is running, monitoring for URLs..."
    
    # Monitor the log file for new URLs
    tail -f /tmp/bonsai_output.log | while read -r line; do
        # Look for URLs in the line
        url=$(echo "$line" | grep -oE 'https?://[^\s]+')
        
        if [ ! -z "$url" ]; then
            echo "🔗 Found URL: $url"
            
            # Send to Telegram
            telegram_message="🔐 *Bonsai Authentication URL Detected*\n\nURL: $url\n\nPlease use this URL to authenticate your Bonsai session."
            send_telegram_message "$telegram_message"
            
            echo "✅ URL sent to Telegram"
            break
        fi
    done
else
    echo "❌ No Bonsai session running"
    echo "Please run 'bonsai start claude' first"
fi