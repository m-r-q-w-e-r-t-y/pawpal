from pawpal_system import Owner, Pet, Task

def main():
    owner = Owner("Jordan")

    mochi = Pet("Mochi", "Cat", [])
    biscut = Pet("Biscut", "Dog", [])

    owner.add_pet(mochi)
    owner.add_pet(biscut)

    mochi.add_task(
        Task(
            "Feeding",
            "09:00",
            "daily",
            False
        )
    )
    mochi.add_task(
        Task(
            "Morning Walk",
            "11:00",
            "daily",
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

    print(f"Today's tasks for {owner.name}:")
    for pet, task in owner.get_all_tasks():
        print(f"{pet.name}: {task.description} at {task.time}")

if __name__ == "__main__":
    main()