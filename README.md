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
- Let a user add tasks (description, time, and frequency at minimum)
- Generate a daily schedule sorted by time, with conflict warnings
- Display the plan clearly
- Include tests for the most important scheduling behaviors

## ✨ Features

- **`Task`, `Pet`, `Owner`, `Scheduler`** classes modeling a pet owner with multiple pets, each with their own tasks
- **Sorting** — `Scheduler.sort_by_time()` returns every task across all pets in chronological order
- **Conflict detection** — `Scheduler.detect_conflicts()` flags any two tasks (same or different pets) scheduled at the same time
- A Streamlit UI to add pets/tasks and generate a sorted schedule with conflict warnings
- A `pytest` suite covering core class behavior and both scheduling algorithms

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
Today's Schedule for Jordan:
  09:00 — Mochi: Feeding (daily)
  09:00 — Biscut: Grooming (once)
  11:00 — Mochi: Morning Walk (daily)
  14:30 — Biscut: Vet appointment (once)

Schedule Conflicts:
  ⚠️ Conflict at 09:00: Mochi's 'Feeding' and Biscut's 'Grooming'
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

1. Run `streamlit run app.py`. Enter an owner name, pet name, and species — a `Pet` is created and persisted via `st.session_state`.
2. Add a task: enter a description, pick a time, and choose a frequency. Click "Add task" — this calls `pet.add_task()` and the task appears in the table below.
3. Add a second task at the same time as an existing one, to see conflict detection in action later.
4. Click "Generate schedule." This calls `Scheduler.sort_by_time()` and displays every task across all pets in chronological order via `st.table`.
5. Any tasks sharing a time slot are flagged with `st.warning`, one per conflict, from `Scheduler.detect_conflicts()`.

Sample CLI output demonstrating the same sorting and conflict detection from `main.py`:

```bash
> python main.py
Today's Schedule for Jordan:
  09:00 — Mochi: Feeding (daily)
  09:00 — Biscut: Grooming (once)
  11:00 — Mochi: Morning Walk (daily)
  14:30 — Biscut: Vet appointment (once)

Schedule Conflicts:
  ⚠️ Conflict at 09:00: Mochi's 'Feeding' and Biscut's 'Grooming'
```
