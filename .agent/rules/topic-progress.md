---
trigger: model_decision
description: Instructions for updating the topic status README
---

# Topic Progress Tracking

 The `learning/[topic]/README.md` file tracks the high-level status of the learner's journey.

## When to Update
Update this file at the end of every lesson (via `teacher-lesson-end` workflow).

## Fields to Maintain

### 1. Current Level
*(Requirement: Require specific, concrete evidence of knowledge application and mastery before updating the user's level. Emphasize honest assessment.)*
- **Beginner (🌱):** Just starting, first milestone.
- **Intermediate (🌿):** Completed at least one capstone.
- **Advanced (🌳):** Multiple milestones, complex topics.
- **Expert (🏆):** Mastery, teaching others.

### 2. Skills Acquired
- Add new skills verified in the latest `learning-report.md`.
- Use checkboxes.

### 3. Lessons Completed
- Add a new row to the table:
  `| Date | Lesson | Report | Status |`
  `| YYYY-MM-DD | [Title](link) | [Report](link) | ✅/🚧 |`

### 4. Milestones to Next Level
- Update the checklist based on `goals.md`.
