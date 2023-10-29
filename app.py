import streamlit as st

# Create a Streamlit app
st.title("Habit Tracker App")

# Define and display a sample habit
habit = st.text_input("Enter a habit:")
st.write(f"Your habit is: {habit}")
