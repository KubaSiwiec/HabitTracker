from pymongo import MongoClient
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
