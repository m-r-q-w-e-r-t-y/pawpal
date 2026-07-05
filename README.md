# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

```bash
> python main.py
Today's tasks for Jordan:
Mochi: Feeding at 09:00
Mochi: Morning Walk at 11:00
Biscut: Vet appointment at 14:30
```

```
# e.g.:
# Daily plan for Biscuit (Golden Retriever):
#   08:00 — Morning walk (30 min) [priority: high]
#   09:00 — Feeding (10 min) [priority: high]
#   ...
```

## 🧪 Testing PawPal+

Run the test suite with:

```bash
python -m pytest
```

The suite (`tests/test_pawpal.py`) covers six behaviors:
- Marking a task complete updates its status
- Adding a task increases a pet's task count
- `Scheduler.sort_by_time()` returns tasks in chronological order regardless of insertion order
- `Scheduler.sort_by_time()` returns an empty list when there are no tasks
- `Scheduler.detect_conflicts()` flags two tasks scheduled at the same time across different pets
- `Scheduler.detect_conflicts()` returns an empty list when no tasks overlap

Sample test output:

```
(.venv) ➜  ai110-module2show-pawpal-starter git:(main) python -m pytest
============================= test session starts ==============================
platform darwin -- Python 3.9.6, pytest-8.4.2, pluggy-1.6.0
rootdir: /Users/macbookair/Documents/ai110-module2show-pawpal-starter
collected 6 items

tests/test_pawpal.py ......                                              [100%]

============================== 6 passed in 0.01s ===============================
```

**Confidence Level:** ⭐⭐⭐⭐☆ (4/5) — all core class behaviors and both scheduling algorithms are verified with passing tests, including edge cases (no tasks, no conflicts). The one gap: `detect_conflicts()` is only tested for exact-time matches, consistent with the tradeoff documented in `reflection.md` section 2b — it doesn't cover overlapping durations, since `Task` has no duration field.

## 📐 Smarter Scheduling

> Fill in once you've implemented scheduling logic.

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | `Scheduler.sort_by_time()` | Sorts all tasks across every pet chronologically using Python's `sorted()` with a lambda key on each task's `"HH:MM"` time string. |
| Filtering | *Not implemented* | Not one of the two algorithmic features chosen for this project's required scope. |
| Conflict handling | `Scheduler.detect_conflicts()` | Flags any two tasks — same or different pets — scheduled at the exact same time, returning human-readable warning strings instead of raising an error. |
| Recurring tasks | *Not implemented* | Not one of the two algorithmic features chosen for this project's required scope. |

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. <!-- Describe this step -->
2. <!-- Describe this step -->
3. <!-- Describe this step -->
4. <!-- Describe this step -->
5. <!-- Add more steps as needed -->

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
