import streamlit as st

from ui_steps.step import HabitStep
from models.habit_model import HabitModel

class HabitDashboard(HabitStep):

    def show(self):
        st.header("Habit Dashboard")
        self._show_all_habits()
        st.write("Habit dashboard here")

    def _show_all_habits(self):
        habits_cursor = self.habit_service.get_all_habits()
        for i, habit in enumerate(habits_cursor):
            # TODO habit_model = HabitModel.from_dict() - use HabitModel for operations on habits in dashboard
            if st.button(habit.get('name'), key=habit.get("_id")):
                self._edit_habit(habit: dict)

    def _edit_habit(self, habit):
        habit["name"] = st.text_input("Name", value=habit.get("name"))
                