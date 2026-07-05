from dataclasses import dataclass

@dataclass
class Task:
    description: str
    time: str
    frequency: str
    completed: bool

    def mark_complete(self) -> None:
        pass

@dataclass
class Pet:
    name: str
    species: str
    tasks: list[Task]

    def add_task(self, task: Task) -> None:
        pass

    def list_tasks(self) -> list[Task]:
        pass

class Owner:
    def __init__(self, name: str):
        self.name = name
        self.pets = []

    def add_pet(self, pet: Pet) -> None:
        pass

    def get_all_tasks(self) -> list[tuple[Pet, Task]]:
        pass

class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner

    def sort_by_time(self) -> list[tuple[Pet, Task]]:
        pass

    def detect_conflicts(self) -> list[str]:
        pass