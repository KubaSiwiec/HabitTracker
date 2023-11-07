from pymongo import MongoClient
from pymongo.cursor import Cursor
import os

class MongoService:
    def __init__(self) -> None:
        self.client = MongoClient(os.getenv("MONGO_CONNECTION_STRING"))
        self.db = self.client.HabitTracker


class HabitService(MongoService):

    def __init__(self) -> None:
        super().__init__()
        self.habits_collection = self.db.habits

    def insert_habit(self, habit: dict):
        post_id = self.habits_collection.insert_one(habit).inserted_id
        return post_id
    
    def get_all_habits(self) -> Cursor:
        return self.habits_collection.find()
    
    def get_habit_by_id(self, id: str) -> dict:
        return self.habits_collection.find_one({"_id": id})
