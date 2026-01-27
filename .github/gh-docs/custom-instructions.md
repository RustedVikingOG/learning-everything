# Custom Instructions

Custom instructions define guidelines that automatically influence how Copilot generates code and handles tasks.

## Instruction File Types

| Type | Location | Auto-Applied |
|------|----------|--------------|
| `copilot-instructions.md` | `.github/copilot-instructions.md` | Yes, all requests |
| `*.instructions.md` | `.github/instructions/` or user profile | Based on `applyTo` glob |
| `AGENTS.md` | Workspace root | Yes, all requests |

## Basic Setup: copilot-instructions.md

Create `.github/copilot-instructions.md` at workspace root:

```markdown
# Project Guidelines

- Use TypeScript with strict mode
- Follow Vue 3 Composition API patterns
- Write unit tests for all business logic
- Use Pinia for state management
- Prefer `const` over `let`
```

**Enable setting:** `github.copilot.chat.codeGeneration.useInstructionFiles`

## Conditional Instructions: *.instructions.md

For language/framework-specific rules using glob patterns:

```markdown
---
applyTo: "**/*.py"
---
# Python Standards

- Follow PEP 8 style guide
- Include type hints for all functions
- Use 4 spaces for indentation
```

**Location:** `.github/instructions/` folder

### Frontmatter Options

| Field | Purpose |
|-------|---------|
| `applyTo` | Glob pattern for auto-application |
| `name` | Display name in UI |
| `description` | Short description |

## Settings-Based Instructions

For specialized tasks via VS Code settings:

```json
{
  "github.copilot.chat.commitMessageGeneration.instructions": [
    { "text": "Use conventional commits format" }
  ],
  "github.copilot.chat.reviewSelection.instructions": [
    { "file": "guidance/review-guidelines.md" }
  ]
}
```

**Available settings:**
- `commitMessageGeneration.instructions`
- `pullRequestDescriptionGeneration.instructions`
- `reviewSelection.instructions`

## Tips

- Keep instructions short and specific
- Use multiple files for different concerns
- Store in workspace to share with team
- Reference files with Markdown links
- Reference tools with `#tool:<tool-name>` syntax
