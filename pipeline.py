from typing import Any, Dict, List, Tuple

from menu import show_side_menu
from ui_steps.step import Step

class Pipeline:
    def __init__(self, steps: Tuple[Step]) -> None:
        self.steps = steps

    def run(self):
        menu_items_2_steps: List[Dict[str, Step]] = [] # type anotatin only
        (side_menu, menu_items_2_steps) = show_side_menu(self.steps)
        for menu_item_2_step in menu_items_2_steps:
            print(menu_item_2_step)
            print(menu_item_2_step.get("menu_item"), " outer")
            print("Menu: ", str(side_menu))
            if side_menu == menu_item_2_step.get("menu_item"):
                print(menu_item_2_step.get("menu_item"), " inner")
                menu_item_2_step.get("step").show()


