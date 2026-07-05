# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

Given that a pet owner can have many pets, tasks, and a schedule associated with those tasks, I came up with the following classes:
    - Task
    - Pet
    - Owner
    - Scheduler

For each of the entities, their relationships are as follows:
    - An Owner can have many pets
    - A Pet can have many tasks
    - A Scheduler reads an Owner to determine its pets and tasks to sort and detect conflicts

**b. Design changes**

As I was discussing with Claude Code and reviewing later phases, I decided to create 2 Mermaid diagrams. One representing the initial design direction (`uml_wip.mmd`) and when which will I will iterate on as I go through the project (`uml_initial.mmd`). The reason for this is that I identified that the methods for Owner and Scheduler need a specific return type to keep track of which pet each task belongs to. `detect_conflicts()` will also return a list of warning strings per Phase 4, Step 4.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

Our scheduler's primary constraint is task time — both sort_by_time() and detect_conflicts() are built entirely around comparing each task's "HH:MM" value. We didn't implement priority or duration as constraints, since neither was needed for the two algorithmic features we chose (sorting and conflict detection). Time was the most important constraint to handle first because it directly answers what a pet owner needs most immediately — knowing when something has to happen and whether two things collide.

**b. Tradeoffs**

Scheduler.detect_conflicts() only flags tasks that share the exact same time string (e.g., two tasks both at "09:00") rather than checking for overlapping time ranges. Since Task doesn't track a duration, there's no way to know how long a task actually occupies, so a real overlap check (e.g., a 9:00–9:30 walk conflicting with a 9:15 feeding) isn't possible with the current design. This is a reasonable simplification for this project's scope: it still catches the most obvious clashes using simple string equality, which is fast and trivial to test, while a true interval-overlap algorithm would require adding a duration field and comparing start/end ranges — more complexity than this scheduler needs.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
