from pymongo import MongoClient
from pymongo.errors import PyMongoError


class AnimalShelter:
    """CRUD operations for Animal collection in MongoDB."""

    def __init__(self):
        USER = "aacuser"
        PASS = "lemonboy1"
        HOST = "localhost"
        PORT = 27017
        DB = "aac"
        COL = "animals"

        self.client = MongoClient(
            f"mongodb://{USER}:{PASS}@{HOST}:{PORT}/?authSource=admin"
        )
        self.database = self.client[DB]
        self.collection = self.database[COL]

    def create(self, data):
        if data is None:
            return False
        try:
            self.collection.insert_one(data)
            return True
        except PyMongoError as e:
            print("Create failed:", e)
            return False

    def read(self, query):
        try:
            results = self.collection.find(query, {"_id": 0})
            return list(results)
        except PyMongoError as e:
            print("Read failed:", e)
            return []

    def update(self, query, new_values):
        try:
            result = self.collection.update_many(query, {"$set": new_values})
            return result.modified_count
        except PyMongoError as e:
            print("Update failed:", e)
            return 0

    def delete(self, query):
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except PyMongoError as e:
            print("Delete failed:", e)
            return 0