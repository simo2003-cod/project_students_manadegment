from pymongo import MongoClient

MONGO_URI = "mongodb://localhost:27017"
DB_NAME = "students_db"
COLLECTION_NAME = "students"

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
students = db[COLLECTION_NAME]





