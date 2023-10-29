import streamlit as st

from  pipeline import Pipeline
from steps.habit_entry import HabitEntry
from steps.habit_dashboard import HabitDashboard

# Create a Streamlit app
st.title("Habit Tracker App")

steps: tuple = (
        HabitEntry("Enter Habit"),
        HabitDashboard("Habit Dashboard")
    )

pipeline = Pipeline(steps)
pipeline.run()


