from pawpal_system import Task, Pet, Owner, Scheduler

def test_mark_complete_changes_status():
    task = Task("Feeding", "09:00", "daily", False)
    task.mark_complete()
    assert task.completed == True

def test_add_task_increases_pet_task_count():
    pet = Pet("Mochi", "Cat", [])
    initial_task_count = len(pet.tasks)
    pet.add_task(Task("Feeding", "09:00", "daily", False))
    assert len(pet.tasks) == initial_task_count + 1

def test_sort_by_time_returns_chronological_order():
    owner = Owner("Jordan")
    pet = Pet("Mochi", "Cat", [])
    owner.add_pet(pet)
    pet.add_task(Task("Walk", "11:00", "daily", False))
    pet.add_task(Task("Feeding", "09:00", "daily", False))

    scheduler = Scheduler(owner)
    sorted_tasks = scheduler.sort_by_time()

    times = [task.time for _, task in sorted_tasks]
    assert times == ["09:00", "11:00"]

def test_sort_by_time_with_no_tasks_returns_empty_list():
    owner = Owner("Jordan")
    pet = Pet("Mochi", "Cat", [])
    owner.add_pet(pet)

    scheduler = Scheduler(owner)
    assert scheduler.sort_by_time() == []

def test_detect_conflicts_flags_same_time_across_pets():
    owner = Owner("Jordan")
    mochi = Pet("Mochi", "Cat", [])
    biscuit = Pet("Biscuit", "Dog", [])
    owner.add_pet(mochi)
    owner.add_pet(biscuit)

    mochi.add_task(Task("Feeding", "09:00", "daily", False))
    biscuit.add_task(Task("Grooming", "09:00", "once", False))

    scheduler = Scheduler(owner)
    conflicts = scheduler.detect_conflicts()

    assert len(conflicts) == 1

def test_detect_conflicts_with_no_overlap_returns_empty_list():
    owner = Owner("Jordan")
    pet = Pet("Mochi", "Cat", [])
    owner.add_pet(pet)

    pet.add_task(Task("Feeding", "09:00", "daily", False))
    pet.add_task(Task("Walk", "11:00", "daily", False))

    scheduler = Scheduler(owner)
    assert scheduler.detect_conflicts() == []