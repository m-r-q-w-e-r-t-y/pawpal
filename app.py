import streamlit as st
from pawpal_system import Owner, Scheduler,Pet, Task

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Quick Demo Inputs (UI only)")
owner_name = st.text_input("Owner name", value="Jordan")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

if "owner" not in st.session_state:
    st.session_state.owner = Owner(owner_name)

owner = st.session_state.owner

if "pet" not in st.session_state:
    new_pet = Pet(name=pet_name, species=species, tasks=[])
    owner.add_pet(new_pet)
    st.session_state.pet = new_pet

pet = st.session_state.pet

st.markdown("### Tasks")
st.caption("Add a few tasks. In your final version, these should feed into your scheduler.")

col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    task_time = st.time_input("Time")
with col3:
    frequency = st.selectbox("Frequency", ["once", "daily", "weekly"])

if st.button("Add task"):
    pet.add_task(
        Task(description=task_title, time=task_time.strftime("%H:%M"), frequency=frequency, completed=False)
    )

if pet.list_tasks():
    st.write("Current tasks:")
    st.table([{"description": t.description, "time": t.time, "frequency": t.frequency} for t in pet.list_tasks()])
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")
st.caption("This button should call your scheduling logic once you implement it.")

if st.button("Generate schedule"):
    scheduler = Scheduler(owner)
    sorted_tasks = scheduler.sort_by_time()

    if sorted_tasks:
        st.success("Today's Schedule (sorted by time):")
        st.table(
            [
                {"time": task.time, "pet": pet_obj.name, "description": task.description, "frequency": task.frequency}
                for pet_obj, task in sorted_tasks
            ]
        )

        for warning in scheduler.detect_conflicts():
            st.warning(warning)
    else:
        st.info("No tasks to schedule yet.")
