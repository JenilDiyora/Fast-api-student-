from motor import motor_asyncio

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.student

student_collection = database.get_collection("students_collection")

faculty_collection = database.get_collection("faculty_collection")