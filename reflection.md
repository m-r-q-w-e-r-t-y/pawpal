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

I went phase by phase instead of asking for the whole project at once — UML, then class skeletons, then logic, then algorithms, then tests, then docs. That kept each request scoped enough that I could actually check the output instead of just trusting it. The most useful prompts weren't "build X," they were "explain why this line works" — like asking why `field(default_factory=list)` is needed instead of `= []`, or what each piece of a Mermaid relationship arrow means. Understanding the syntax before typing it caught a couple of things I would've otherwise copy-pasted blindly.

**b. Judgment and verification**

A few times. The clearest one: when wiring `app.py`, the AI rewrote way more than I asked for — it added an "Add Pet" button, a pet selector dropdown, a whole extra table, when all I wanted was the existing placeholders replaced with real method calls. I pushed back and had it redo it as a minimal diff instead. Separately, when it told me `detect_conflicts()` should return "a list of warning strings," I asked it to point to exactly where INSTRUCTIONS.md said that — turned out only "a warning message" (singular) was actually specified; the list part was its own reasonable extrapolation from the rubric's multi-pet requirement, not something dictated. I kept the list design because the reasoning held up, but I wanted to know the difference between "the assignment requires this" and "the AI decided this."

---

## 4. Testing and Verification

**a. What you tested**

Two categories: the basic class behaviors (marking a task complete, adding a task to a pet) and the two scheduling algorithms (sorting, conflict detection), including edge cases — an empty task list, and a case with no conflicts at all. The algorithm tests mattered most since that's where actual logic lives; the class tests are simple but they're what the assignment explicitly asked for first.

**b. Confidence**

4/5. Everything I built is tested and passing, including the cross-pet conflict case, which is the part of the rubric I cared most about getting right. The gap is that conflict detection only checks for exact time matches, not overlapping durations — documented as a known tradeoff in section 2b, not an oversight. If I had more time I'd add a test with three or more overlapping tasks at once, since right now every conflict test only checks a pair.

---

## 5. Reflection

**a. What went well**

The object model held up end to end — what I sketched in the UML on day one is still the same shape in the final code. No do-overs on `Owner`/`Pet`/`Task`/`Scheduler`, just refinements to return types as the design got more specific.

**b. What you would improve**

My commit hygiene early on — a couple of times I let two or three steps of work pile up before committing, so I had to go back and do catch-up commits. Committing right after each step, every time, would've made the history read more naturally.

**c. Key takeaway**

Being the "lead architect" means the AI will happily move fast in a direction you didn't ask for if you let it — the value I added wasn't writing the code, it was constantly checking claims against the actual rubric and instructions instead of taking either the AI's or the assignment's word for it, and being willing to say "that's not what I asked for" when the scope crept.
