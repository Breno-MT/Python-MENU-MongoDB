from pandas import DataFrame
from modules.pymongo_database import get_database

def query_all():
    dbname = get_database()
    collection_name = dbname["users"]

    query_all = collection_name.find()
    query_df = DataFrame(query_all)

    if len(query_df) == 0:
        print("There's no User in Database, try to create one! :D")

    print(f"""User(s): \n {query_df}""")

def query_by_name(name):
    dbname = get_database()
    collection_name = dbname["users"]

    query_name = collection_name.find({"name": {"$regex": f"{name}"}})
    query_df = DataFrame(query_name)

    if len(query_df) > 0:
        print(f"""User(s) found: \n {query_df}""")
    
    if len(query_df) == 0:
        print("No Users found! :(")
        print("If you didn't found your user, don't worry, try again.")

def query_by_code(code):
    dbname = get_database()
    collection_name = dbname["users"]

    query_code = collection_name.find({"code": {"$regex": f"{code}"}})
    query_df = DataFrame(query_code)

    if len(query_df) > 0:
        print(f"Users(s) found: \n {query_df}")

    if len(query_df) == 0:
        print("No Users found! :(")
        print("If you didn't found your user, don't worry, try again.")

