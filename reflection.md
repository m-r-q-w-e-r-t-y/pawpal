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

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

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
