import bson
from modules.pymongo_database import get_database


def update_one_user(id, name, code):

    id_obj = bson.ObjectId(id)

    dbname = get_database()
    collection_name = dbname["users"]
    collection_name.update_one(
    {
        "_id": id_obj
    }, 
    
    {"$set": 
        {
        "name": name,
        "code": code
        }
    }
    )

    print("User updated successfully.")

