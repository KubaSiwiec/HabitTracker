import streamlit as st

# Create a Streamlit app
st.title("Habit Tracker App")

# Create a list of days of the week
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Sidebar menu for navigation
menu = st.sidebar.selectbox("Menu", ["Habit Entry", "Habit Dashboard"])

if menu == "Habit Entry":
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
            # Process and store the habit details
            st.write("Habit Name:", habit)
            st.write("Habit Duration (days):", duration)
            st.write("Activity Time:", f"{hours:02d}:{minutes:02d}")
            st.write("Frequency:", selected_days)

elif menu == "Habit Dashboard":
    # Habit Dashboard View
    st.header("Habit Dashboard")
    # Implement your habit dashboard functionality here
