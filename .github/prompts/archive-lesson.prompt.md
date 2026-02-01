# Archive Completed Lesson

Archive the current lesson plan to the lessons folder with proper numbering.

## Instructions

1. **Determine the next lesson number:**
   - Check `learning/[topic]/lessons/` for existing lessons
   - New lesson number = highest existing number + 1
   - Format: two digits, e.g., `01`, `02`, `10`

2. **Create the archived lesson file:**
   - Path: `learning/[topic]/lessons/lesson-[NN]-[slug].md`
   - Slug: lowercase, hyphens, based on lesson title (e.g., `web-api-basics`)

3. **Archive content should include:**
   ```markdown
   # [Topic] Lesson [NN]: [Title]

   **Date Completed:** [Today's date]  
   **Estimated Time:** [From original lesson plan]  
   **Report:** [Link to corresponding report if exists]  
   **Milestone:** [N] - [Milestone Name from goals.md]

   ---

   ## Objectives

   [Copy objectives from lesson plan, mark all as completed]

   ---

   ## Key Concepts Covered

   [List the main concepts that were taught]

   ---

   ## What Was Built

   [Brief description of exercises completed or code written]

   ---

   ## Connections Made

   [Any connections to prior knowledge noted during the lesson]

   ---

   ## Areas Identified for Next Lesson

   [Topics that came up for future exploration]
   ```

4. **Update the README lesson index:**
   - Add row to the "Lessons Completed" table in `learning/[topic]/README.md`
   - Format: `| [NN] | [Title] | [Date] | [Report Link] |`

5. **Update goals.md:**
   - Mark any completed skills in the current milestone
   - Update lesson numbers in the skill table
   - Recalculate progress percentages

## Example

If archiving a lesson about "Routes and Parameters" as lesson 02:

**File:** `learning/dotnet/lessons/lesson-02-routes-and-parameters.md`

**README update:**
```markdown
| 02 | Routes & Parameters | 2026-02-01 | [Report](../../reports/dotnet/20260201-report.md) |
```
