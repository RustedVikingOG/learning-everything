# Update Capstone Progress

Update the goals.md file to reflect current milestone progress.

## Instructions

1. **Read the current state:**
   - Check `learning/[topic]/goals.md` for current milestone
   - Check `learning/[topic]/lessons/` for completed lessons
   - Check latest report for skills demonstrated

2. **Update skill statuses:**
   - ✅ = Demonstrated in a lesson
   - ⏳ = Currently learning (in current lesson plan)
   - ⬜ = Not started

3. **Update lesson references:**
   - Add lesson numbers to skills when they're covered
   - Format: `| Skill | ✅ | 02 |`

4. **Recalculate milestone progress:**
   - Count completed skills / total skills in milestone
   - Update the progress bar:
     ```
     Milestone 1: ████████░░ 80%
     ```
   - Use █ for complete segments, ░ for incomplete
   - 10 characters total for the bar

5. **Check for milestone completion:**
   - If all skills in a milestone are ✅, mark milestone complete
   - Change milestone header emoji: 🟡 → ✅
   - Update "Current Milestone" at top of file

6. **Update overall progress:**
   - Calculate: (completed milestones * 100 + current milestone %) / total milestones
   - Update the overall progress bar

## Progress Bar Reference

```
 0%: ░░░░░░░░░░
10%: █░░░░░░░░░
20%: ██░░░░░░░░
30%: ███░░░░░░░
40%: ████░░░░░░
50%: █████░░░░░
60%: ██████░░░░
70%: ███████░░░
80%: ████████░░
90%: █████████░
100%: ██████████
```

## Example Update

Before:
```markdown
| Route parameters | ⬜ | - |
```

After (lesson 02 covered it):
```markdown
| Route parameters | ✅ | 02 |
```
