import streamlit as st

from steps.step import Step

class HabitDashboard(Step):

    def show(self):
        st.header("Habit Dashboard")
        # Implement your habit dashboard functionality here
        st.write("Habit dashboard here")