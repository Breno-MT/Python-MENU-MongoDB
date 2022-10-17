from pandas import DataFrame
from modules.pymongo_database import get_database

def query_all():
    dbname = get_database()
    collection_name = dbname["users"]

    query_all = collection_name.find()
    query_df = DataFrame(query_all)

    print(f"""User(s): \n
            {query_df}""")


def query_by_name(name):
    dbname = get_database()
    collection_name = dbname["users"]

    query_name = collection_name.find({"name": {"$regex": f"{name}"}})

    print(f"""User(s) found: \n
        {query_name}""")
    
    print("If you didn't found your user, don't worry, try again.")
