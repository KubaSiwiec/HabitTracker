import streamlit as st

from ui_steps.step import HabitStep

class HabitDashboard(HabitStep):

    def show(self):
        st.header("Habit Dashboard")
        # Implement your habit dashboard functionality here
        st.write("Habit dashboard here")