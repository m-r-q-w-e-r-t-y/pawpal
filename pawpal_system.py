from dataclasses import dataclass

@dataclass
class Task:
    description: str
    time: str
    frequency: str
    completed: bool

    def mark_complete(self) -> None:
        """Mark the task as completed."""
        self.completed = True

@dataclass
class Pet:
    name: str
    species: str
    tasks: list[Task]

    def add_task(self, task: Task) -> None:
        """Add a task to the pet's list of tasks."""
        self.tasks.append(task)

    def list_tasks(self) -> list[Task]:
        """Return all tasks belonging to this pet."""
        return self.tasks

class Owner:
    def __init__(self, name: str):
        self.name = name
        self.pets = []

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to this owner's list of pets."""
        self.pets.append(pet)

    def get_all_tasks(self) -> list[tuple[Pet, Task]]:
        """Return every (pet, task) pair across all of this owner's pets."""
        return [(pet, task) for pet in self.pets for task in pet.tasks]

class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner

    def sort_by_time(self) -> list[tuple[Pet, Task]]:
        """Return all tasks across all pets, sorted chronologically by time."""
        return sorted(self.owner.get_all_tasks(), key=lambda x: x[1].time)

    def detect_conflicts(self) -> list[str]:
        """Return warning messages for any tasks scheduled at the same time."""
        warnings = []
        tasks = self.owner.get_all_tasks()
        for i in range(len(tasks)):
            for j in range(i + 1, len(tasks)):
                pet_a, task_a = tasks[i]
                pet_b, task_b = tasks[j]
                if task_a.time == task_b.time:
                    warnings.append(
                        f"⚠️ Conflict at {task_a.time}: {pet_a.name}'s '{task_a.description}' "
                        f"and {pet_b.name}'s '{task_b.description}'"
                    )
        return warnings