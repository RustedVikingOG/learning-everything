# Custom Agents

Custom agents configure AI to adopt specialized personas with specific tools and instructions.

## File Structure

**Extension:** `*.agent.md`  
**Location:** `.github/agents/` (workspace) or user profile

```markdown
---
description: Generate implementation plans without code changes
name: Planner
tools: ['search', 'fetch', 'githubRepo', 'usages']
model: Claude Sonnet 4
handoffs:
  - label: Start Implementation
    agent: agent
    prompt: Implement the plan above.
---
# Planning Instructions

You are in planning mode. Generate implementation plans only.
Do NOT make code edits.

Include:
- Overview of the feature
- Requirements list
- Step-by-step implementation
- Testing strategy
```

## Frontmatter Options

| Field | Purpose | Example |
|-------|---------|---------|
| `name` | Agent display name | `"Planner"` |
| `description` | Shown in chat input | `"Generate implementation plans"` |
| `tools` | Available tools | `['search', 'editFiles']` |
| `model` | Language model | `"Claude Sonnet 4"` |
| `handoffs` | Next-step buttons | See below |
| `infer` | Use as subagent | `true` (default) |

## Tools Configuration

Specify which tools the agent can access:

```yaml
tools: ['search', 'fetch', 'usages']          # Specific tools
tools: ['myMcpServer/*']                       # All MCP server tools
tools: ['editFiles', 'runTerminalCommand']     # Edit capabilities
```

**Read-only agents:** Omit `editFiles` and `runTerminalCommand`

## Handoffs

Create guided workflows between agents:

```yaml
handoffs:
  - label: Start Implementation
    agent: agent
    prompt: Implement the plan outlined above.
    send: false
  - label: Request Review
    agent: reviewer
    prompt: Review the implementation.
    send: true
```

| Field | Purpose |
|-------|---------|
| `label` | Button text |
| `agent` | Target agent name |
| `prompt` | Pre-filled prompt |
| `send` | Auto-submit (default: false) |

## Example: Security Reviewer

```markdown
---
description: Review code for security issues
name: Security Reviewer
tools: ['search', 'usages', 'fetch']
---
# Security Review Agent

Focus on identifying:
- Authentication/authorization flaws
- Injection vulnerabilities
- Data exposure risks
- Insecure configurations

Provide severity ratings and remediation steps.
Do NOT modify code directly.
```

## Example: Frontend Developer

```markdown
---
description: Frontend development with Vue/React
name: Frontend Dev
tools: ['editFiles', 'search', 'runTerminalCommand']
model: Claude Sonnet 4
---
# Frontend Developer

Specialize in:
- Vue 3 / React components
- CSS/Tailwind styling
- Accessibility (WCAG 2.1)
- Responsive design

Follow the project's [coding standards](../instructions/frontend.instructions.md).
```

## Using Custom Agents

1. Open Chat view
2. Select agent from dropdown (or type `@agent-name`)
3. Start conversation

## Tips

- Limit tools to what's needed for the role
- Use read-only tools for planning/review agents
- Reference instruction files to avoid duplication
- Chain agents with handoffs for workflows
