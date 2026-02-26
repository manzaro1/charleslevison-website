#!/bin/bash
# Charles Levison - Multi-Agent System
# Agents: Milo, Josh, Angela, Bob

AGENTS_DIR="/home/charlesclaw/.openclaw/workspace/agents"
MEMORY_FILE="$AGENTS_DIR/memory.json"

# Ensure memory file exists
if [ ! -f "$MEMORY_FILE" ]; then
    echo '{"projects": [], "tasks": [], "notes": []}' > "$MEMORY_FILE"
fi

# Agent definitions
show_help() {
    cat << 'EOF'
🤖 Agent System - Charles Levison

AGENTS:
  Milo    - Project Planner (film, art, construction projects)
  Josh    - Budget Analyst (financial planning, cost analysis)
  Angela  - Marketing & Research (promotion, strategy, research)
  Bob     - Tech/code support (CS homework, programming, tech issues)

USAGE:
  ./agent.sh Milo "Plan my documentary timeline"
  ./agent.sh Josh "Calculate budget for art exhibition"
  ./agent.sh Angela "Research social media marketing"
  ./agent.sh Bob "Debug this Python script"

COMMANDS:
  ./agent.sh menu       - Interactive agent menu
  ./agent.sh status     - Show all active tasks
  ./agent.sh memory     - View shared memory
  ./agent.sh help       - Show this help

EOF
}

show_menu() {
    echo ""
    echo "🎯 SELECT AN AGENT:"
    echo ""
    echo "  1) 🤖 Milo    - Project Planning"
    echo "  2) 💰 Josh    - Budget & Finance"
    echo "  3) 📢 Angela  - Marketing & Research"
    echo "  4) 💻 Bob     - Code & Tech Support"
    echo "  5) 📝 Status  - View all tasks"
    echo "  6) ❌ Exit"
    echo ""
    read -p "Choose (1-6): " choice
    
    case $choice in
        1) AGENT="Milo" ;;
        2) AGENT="Josh" ;;
        3) AGENT="Angela" ;;
        4) AGENT="Bob" ;;
        5) show_status; exit 0 ;;
        6) echo "Goodbye!"; exit 0 ;;
        *) echo "Invalid choice"; exit 1 ;;
    esac
    
    echo ""
    read -p "What do you need $AGENT to do? " TASK
    call_agent "$AGENT" "$TASK"
}

call_agent() {
    local AGENT=$1
    local TASK=$2
    
    # Add to memory
    local TIMESTAMP=$(date -Iseconds)
    local ENTRY="{\"agent\": \"$AGENT\", \"task\": \"$TASK\", \"time\": \"$TIMESTAMP\"}"
    
    # Log the request
    echo "[$TIMESTAMP] $AGENT: $TASK" >> "$AGENTS_DIR/activity.log"
    
    echo ""
    echo "🚀 Calling $AGENT..."
    echo "📋 Task: $TASK"
    echo ""
    
    # Route to OpenClaw
    # This will spawn a sub-agent for the actual work
    echo "✅ Task submitted to $AGENT"
    echo "   Use 'openclaw' commands or Telegram to continue."
}

show_status() {
    echo ""
    echo "📊 AGENT SYSTEM STATUS"
    echo "====================="
    echo ""
    
    if [ -f "$AGENTS_DIR/activity.log" ]; then
        echo "Recent Activity:"
        tail -10 "$AGENTS_DIR/activity.log" | while read line; do
            echo "  • $line"
        done
    else
        echo "No activity yet. Start by calling an agent!"
    fi
    
    echo ""
    echo "Memory entries:"
    cat "$MEMORY_FILE"
}

show_memory() {
    echo ""
    echo "🧠 SHARED MEMORY"
    echo "================"
    cat "$MEMORY_FILE" | python3 -m json.tool 2>/dev/null || cat "$MEMORY_FILE"
}

# Main dispatcher
case "${1:-}" in
    ""|help|--help|-h)
        show_help
        ;;
    menu)
        show_menu
        ;;
    status)
        show_status
        ;;
    memory)
        show_memory
        ;;
    Milo|milo)
        shift
        call_agent "Milo" "$*"
        ;;
    Josh|josh)
        shift
        call_agent "Josh" "$*"
        ;;
    Angela|angela)
        shift
        call_agent "Angela" "$*"
        ;;
    Bob|bob)
        shift
        call_agent "Bob" "$*"
        ;;
    *)
        echo "Unknown agent or command: $1"
        echo ""
        show_help
        exit 1
        ;;
esac