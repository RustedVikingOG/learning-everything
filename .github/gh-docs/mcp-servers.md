# MCP Servers

Model Context Protocol (MCP) servers provide external tools for tasks like database queries, API calls, and file operations.

## Configuration Location

**File:** `.vscode/mcp.json` (workspace) or user settings

```json
{
  "servers": {
    "github": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "${input:github-token}"
      }
    }
  },
  "inputs": [
    {
      "type": "promptString",
      "id": "github-token",
      "description": "GitHub Personal Access Token",
      "password": true
    }
  ]
}
```

## Server Types

### Standard I/O (stdio)

For local servers communicating via stdin/stdout:

```json
{
  "type": "stdio",
  "command": "node",
  "args": ["server.js"],
  "env": { "API_KEY": "${input:api-key}" },
  "envFile": "${workspaceFolder}/.env"
}
```

| Field | Required | Purpose |
|-------|----------|---------|
| `type` | Yes | `"stdio"` |
| `command` | Yes | Executable command |
| `args` | No | Command arguments |
| `env` | No | Environment variables |
| `envFile` | No | Path to .env file |

### HTTP/SSE Servers

For remote servers over HTTP:

```json
{
  "type": "http",
  "url": "https://api.example.com/mcp",
  "headers": {
    "Authorization": "Bearer ${input:api-token}"
  }
}
```

## Input Variables

Securely store sensitive values:

```json
{
  "inputs": [
    {
      "type": "promptString",
      "id": "api-key",
      "description": "API Key",
      "password": true
    }
  ]
}
```

Reference in config: `${input:api-key}`

## Installing MCP Servers

### From VS Code

1. Open Extensions view (`Cmd+Shift+X`)
2. Search `@mcp`
3. Select server → Install

### From Command Line

```bash
# GitHub MCP Server
npx -y @modelcontextprotocol/server-github

# Filesystem MCP Server  
npx -y @modelcontextprotocol/server-filesystem
```

## Using MCP Tools

1. Open Chat view
2. Tools are auto-invoked in agent mode
3. Or reference explicitly: `#tool-name`

### In Custom Agents/Prompts

```yaml
tools: ['github/*']           # All GitHub MCP tools
tools: ['github/list_issues'] # Specific tool
```

## Common MCP Servers

| Server | Purpose |
|--------|---------|
| `server-github` | GitHub issues, PRs, repos |
| `server-filesystem` | File operations |
| `server-postgres` | PostgreSQL queries |
| `server-fetch` | HTTP requests |

## Trust & Security

- MCP servers run arbitrary code
- VS Code prompts for trust on first start
- Only use servers from trusted sources
- Reset trust: `MCP: Reset Trust` command

## Troubleshooting

**View logs:** `MCP: List Servers` → Select server → Show Output

**Restart server:** Click refresh in Chat view or use `MCP: List Servers`

**Reset tools cache:** `MCP: Reset Cached Tools`

## Resources

- [MCP Documentation](https://modelcontextprotocol.io/)
- [GitHub MCP Registry](https://github.com/mcp)
- [Official MCP Servers](https://github.com/modelcontextprotocol/servers)
