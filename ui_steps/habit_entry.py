import streamlit as st

from ui_steps.step import HabitStep
from models.habit_model import HabitModel

# Create a list of days of the week
# TODO use weekday class
days_of_week: tuple = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

class HabitEntry(HabitStep):

    def show(self):
        # Habit Entry View
        st.header("Habit Entry")

        # Habit Name Input
        habit = st.text_input("Enter a habit:")

        if habit:
            # Habit Duration
            duration = st.number_input("How long do you want to stick to this habit (in days)?", min_value=1)

            # Activity Time
            st.write("Select the time for the activity:")
            hours = st.slider("Hours", 0, 23)
            minutes = st.slider("Minutes", 0, 59)

            # Days of the Week Selection
            st.write("Select the days of the week for the habit:")
            selected_days = [day for day in days_of_week if st.checkbox(day)]

            # Check if time of activity is zero or no days are selected
            conditions_met = (hours == 0 and minutes == 0) or not selected_days

            if conditions_met:
                st.error("Please ensure you've selected at least one day and set a non-zero time for the activity.")
            elif st.button("Save Habit"):
                habit_model = HabitModel(habit, number_of_days=duration, daily_hours=hours, daily_minutes=minutes, weekdays=selected_days)
                habit_json = habit_model.as_dict()
                habit_id = self.habit_service.insert_habit(habit_json)
                print(f"Inserted habit with ID: {habit_id}")
                with st.expander("Habit inserted to dashboard"):
                    # Process and store the habit details
                    st.write("Habit Name:", habit)
                    st.write("Habit Duration (days):", duration)
                    st.write("Activity Time:", f"{hours:02d}:{minutes:02d}")
                    st.write("Frequency:", selected_days)
                # TODO call the presenter to save habit model to DB