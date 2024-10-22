from pymongo import MongoClient

from Miko import MONGO_DB_URL

client = MongoClient(MONGO_DB_URL)
dbname = client["Toggle"]

dwelcomedb = dbname.dwelcome


def is_dwelcome_on(chat_id: int) -> bool:
    chat = dwelcomedb.find_one({"chat_id_toggle": chat_id})
    return not bool(chat)


def dwelcome_on(chat_id: int) -> bool:
    dwelcomedb.delete_one(
        {"chat_id_toggle": chat_id}
    )  # Delete the chat ID from the database
    return True


def dwelcome_off(chat_id: int):
    dwelcomedb.insert_one(
        {"chat_id_toggle": chat_id}
    )  # Insert the chat ID into the database
