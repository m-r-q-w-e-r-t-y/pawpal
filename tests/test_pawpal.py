from pawpal_system import Task, Pet

def test_mark_complete_changes_status():
    task = Task("Feeding", "09:00", "daily", False)
    task.mark_complete()
    assert task.completed == True

def test_add_task_increases_pet_task_count():
    pet = Pet("Mochi", "Cat", [])
    initial_task_count = len(pet.tasks)
    pet.add_task(Task("Feeding", "09:00", "daily", False))
    assert len(pet.tasks) == initial_task_count + 1