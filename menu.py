from typing import Tuple
import streamlit as st

from steps.step import Step

def show_side_menu( steps: Tuple[Step]) -> tuple:
    menu_item_2_step = [{"menu_item": step.menu_item, "step": step} for step in steps]
    menu_items = [step.menu_item for step in steps]
    side_menu = st.sidebar.selectbox("Menu", menu_items)
    return side_menu, menu_item_2_step