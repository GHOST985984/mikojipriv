import motor.motor_asyncio

from Miko import MONGO_DB_URL

# Create a MongoDB client using motor
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DB_URL)

# Get a reference to the database and collection
mongodb = client["Mikobot"]
