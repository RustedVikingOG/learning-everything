```prompt
---
description: Create or find GitHub issues for tracking work
name: create-issue
---
# Create or Find GitHub Issue

## Before Creating: Check for Existing Issues

Always search first to avoid duplicates:

```bash
gh issue list --label "enhancement" --state open
gh issue list --label "documentation" --state open
gh issue list --state open --search "<keywords>"
```

If a matching issue exists, use it instead of creating a new one.

---

## Issue Creation

### For short bodies:
```bash
gh issue create \
  --title "<title>" \
  --body "<body>" \
  --label "<labels>" \
  --assignee "RustedVikingOG"
```

### For long bodies (recommended):
```bash
# 1. Create .tmp/issue-body.md with the content
# 2. Then:
gh issue create \
  --title "<title>" \
  --body-file .tmp/issue-body.md \
  --label "<labels>" \
  --assignee "RustedVikingOG"
```

---

## Title Format

`[<category>] <brief description>`

| Category | Use For |
|----------|---------|
| `[meta]` | Infrastructure, agents, prompts, templates |
| `[dotnet]` | .NET/C# learning content |
| `[lesson]` | Specific lesson work |
| `[fix]` | Bug fixes, corrections |

**Examples:**
- `[meta] Add capstone-driven learning system`
- `[dotnet] Learn Entity Framework basics`
- `[lesson] Complete lesson 02 - Routes and parameters`
- `[fix] Correct broken link in README`

---

## Labels

| Label | When to Use |
|-------|-------------|
| `enhancement` | New features, improvements, infrastructure |
| `documentation` | Docs-only changes |
| `lesson` | Learning session work |
| `dotnet` | .NET specific |
| `next` | Immediate priority |
| `bug` | Something broken |

**Combine as needed:** `--label "enhancement,dotnet"`

---

## Body Template

For substantial issues, use this structure:

```markdown
## Goal

<1-2 sentences: What needs to be accomplished>

## Context

<Why this matters, what it builds on, background>

## Acceptance Criteria

- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

## Resources

- [Relevant file](path/to/file.md)
- [Documentation](url)

## Related Issues

- Relates to #N
- Builds on #N
```

---

## Examples

### Feature/Enhancement Issue

**Title:** `[meta] Add capstone-driven learning system with milestone tracking`

**Body (.tmp/issue-body.md):**
```markdown
## Goal

Implement a capstone-driven learning approach where each topic has a main project that lessons build toward.

## Context

Learning without a concrete goal can feel aimless. By defining a capstone project and breaking it into milestones, lessons have clear purpose.

## Acceptance Criteria

- [ ] Create goals.md template
- [ ] Define milestones for .NET capstone (WebChat)
- [ ] Update teacher agent with milestone awareness
- [ ] Add capstone sprint prompt

## Resources

- [Teacher Agent](.github/agents/teacher.agent.md)
- [Goals Template](.github/templates/goals.md)
```

### Lesson Issue

**Title:** `[lesson] Learn route parameters and HTTP methods`

**Body:**
```markdown
## Goal

Complete Lesson 02: Add custom endpoints with route parameters to the Web API.

## Context

Builds on Lesson 01 (basic Web API scaffolding). Core skill for any API development.

## Acceptance Criteria

- [ ] Create GET endpoint with path parameter (`/hello/{name}`)
- [ ] Create POST endpoint accepting JSON body
- [ ] Understand HTTP method routing (MapGet, MapPost, MapPut, MapDelete)
- [ ] Return different response types

## Resources

- [Lesson 02 Plan](learning/dotnet/lesson-plan.md)
- [Goals](learning/dotnet/goals.md)
```

---

## Output

After creating, report:

```markdown
## Issue Created ✅

**Issue:** #<number>
**URL:** <url>
**Labels:** <labels>
**Assignee:** RustedVikingOG
```

```
