from bson import ObjectId
from modules.pymongo_database import get_database


def delete_user_by_id(id):
    dbname = get_database()
    collection_name = dbname["users"]
    id_obj = ObjectId(id)
    collection_name.delete_one({"_id": id_obj})
    print("User deleted successfully.")


def delete_all_data_in_collection():
    dbname = get_database()
    collection_name = dbname["users"]
    collection_name.delete_many({})
    print("Successfully deleted all data in Collection.")


