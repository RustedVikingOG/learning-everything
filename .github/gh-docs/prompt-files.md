# Prompt Files

Prompt files define reusable prompts for common development tasks that run on-demand in chat.

## File Structure

**Extension:** `*.prompt.md`  
**Location:** `.github/prompts/` (workspace) or user profile

```markdown
---
description: Generate a Vue component with tests
name: vue-component
agent: agent
tools: ['editFiles', 'runTests']
---
# Create Vue Component

Generate a Vue 3 component with:
- Composition API with `<script setup>`
- TypeScript
- Unit tests using Vitest
- Props validation

Component name: ${input:componentName}
```

## Frontmatter Options

| Field | Purpose | Example |
|-------|---------|---------|
| `name` | Slash command name | `vue-component` |
| `description` | Short description | `"Generate a Vue component"` |
| `agent` | Agent to use | `ask`, `edit`, `agent`, or custom |
| `model` | Language model | `"Claude Sonnet 4"` |
| `tools` | Available tools | `['editFiles', 'search']` |
| `argument-hint` | Input hint | `"Enter component name"` |

## Variables

### Built-in Variables

| Variable | Value |
|----------|-------|
| `${workspaceFolder}` | Workspace path |
| `${file}` | Current file path |
| `${selection}` | Selected text |
| `${fileBasename}` | Current file name |

### Input Variables

Prompt for user input:

```markdown
Component: ${input:componentName}
Type: ${input:componentType:functional or class}
```

## Using Prompts

1. **Slash command:** Type `/prompt-name` in chat
2. **Command Palette:** `Chat: Run Prompt`
3. **Editor:** Open `.prompt.md` and click play button

## Example: Code Review Prompt

```markdown
---
description: Security-focused code review
name: security-review
tools: ['search', 'usages']
---
# Security Review

Review the selected code for:
- SQL injection vulnerabilities
- XSS risks
- Hardcoded secrets
- Insecure dependencies

Code to review:
${selection}

Provide findings with severity levels.
```

## Example: API Scaffolding

```markdown
---
description: Generate REST API endpoint
name: api-endpoint
agent: agent
tools: ['editFiles', 'fetch']
---
# Create API Endpoint

Generate a REST API endpoint:
- Resource: ${input:resourceName}
- Methods: GET, POST, PUT, DELETE
- Include validation and error handling
- Add OpenAPI documentation comments
```

## Tips

- Use descriptive names for easy discovery
- Include examples of expected output
- Reference instruction files for consistency
- Test prompts with the editor play button
