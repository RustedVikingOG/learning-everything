# GitHub Copilot Customization Overview

This folder contains reference documentation for customizing GitHub Copilot in VS Code.

## Customization Options

| Option | Purpose | File Type |
|--------|---------|-----------|
| [Custom Instructions](custom-instructions.md) | Define coding standards and guidelines | `.github/copilot-instructions.md`, `*.instructions.md` |
| [Prompt Files](prompt-files.md) | Reusable prompts for common tasks | `*.prompt.md` |
| [Custom Agents](custom-agents.md) | Specialized AI personas with specific tools | `*.agent.md` |
| [MCP Servers](mcp-servers.md) | External tools via Model Context Protocol | `mcp.json` |

## Quick Start

1. **Basic guidelines** → Create `.github/copilot-instructions.md`
2. **Reusable tasks** → Create `.github/prompts/*.prompt.md`
3. **Specialized personas** → Create `.github/agents/*.agent.md`
4. **External tools** → Configure `.vscode/mcp.json`

## File Locations

```
.github/
├── copilot-instructions.md     # Global instructions (auto-applied)
├── instructions/               # Conditional instructions
│   └── *.instructions.md
├── prompts/                    # Reusable prompts
│   └── *.prompt.md
└── agents/                     # Custom agents
    └── *.agent.md

.vscode/
└── mcp.json                    # MCP server config
```

## Usage Scenarios

| Scenario | Recommended Approach |
|----------|---------------------|
| Project-wide coding standards | Custom instructions |
| Language-specific rules | Instructions with glob patterns |
| Reusable dev tasks | Prompt files |
| Planning/research workflows | Custom agents |
| External service integration | MCP servers |

## Related Resources

- [VS Code Copilot Customization Docs](https://code.visualstudio.com/docs/copilot/copilot-customization)
- [Community Examples (Awesome Copilot)](https://github.com/github/awesome-copilot)
