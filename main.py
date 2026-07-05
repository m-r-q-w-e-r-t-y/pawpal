from pawpal_system import Owner, Pet, Task, Scheduler

def main():
    owner = Owner("Jordan")

    mochi = Pet("Mochi", "Cat", [])
    biscut = Pet("Biscut", "Dog", [])

    owner.add_pet(mochi)
    owner.add_pet(biscut)

    mochi.add_task(
        Task(
            "Morning Walk",
            "11:00",
            "daily",
            False
        )
    )
    mochi.add_task(
        Task(
            "Feeding",
            "09:00",
            "daily",
            False
        )
    )

    biscut.add_task(
        Task(
            "Grooming",
            "09:00",
            "once",
            False
        )
    )

    biscut.add_task(
        Task(
            "Vet appointment",
            "14:30",
            "once",
            False
        )
    )

    scheduler = Scheduler(owner)

    print(f"Today's Schedule for {owner.name}:")
    for pet, task in scheduler.sort_by_time():
        print(f"  {task.time} — {pet.name}: {task.description} ({task.frequency})")

    conflicts = scheduler.detect_conflicts()
    if conflicts:
        print("\nSchedule Conflicts:")
        for warning in conflicts:
            print(f"  {warning}")

if __name__ == "__main__":
    main()