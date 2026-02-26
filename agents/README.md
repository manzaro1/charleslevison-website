# 🤖 Agent System for Charles Levison

## Your Team

| Agent | Specialty | Use For |
|-------|-----------|---------|
| **Milo** | Project Planning | Film schedules, art exhibitions, construction timelines |
| **Josh** | Budget Analysis | Financial planning, cost calculations, ROI |
| **Angela** | Marketing & Research | Social media, market research, promotion |
| **Bob** | Code & Tech | CS homework, debugging, automation |

## Quick Start

```bash
cd ~/.openclaw/workspace/agents

# Call by name with task
./agent.sh Milo "Plan my film project"
./agent.sh Josh "Calculate exhibition budget"
./agent.sh Angela "Research marketing strategies"
./agent.sh Bob "Debug my Python code"

# Interactive menu
./agent.sh menu

# View status
./agent.sh status
./agent.sh memory
```

## Files

- `agent.sh` — Main dispatcher script
- `Milo.md`, `Josh.md`, `Angela.md`, `Bob.md` — Agent profiles
- `memory.json` — Shared memory (projects, tasks, notes)
- `activity.log` — Activity history

## Tips

- Be specific when giving tasks
- Agents share memory — they know your context
- Use natural language — no special commands needed
- All activity is logged for your review