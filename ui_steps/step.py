# TODO to ABC
from services.mongo_service import HabitService

class Step():
    def __init__(self, menu_item: str):
        self.menu_item = menu_item

    def show():
        pass

class HabitStep(Step):
    def __init__(self, menu_item: str):
        self.menu_item = menu_item
        self.habit_service = HabitService()

    def show():
        pass