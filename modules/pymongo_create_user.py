from pandas import DataFrame
from modules.pymongo_database import get_database

def create_user():
    
    dbname = get_database()

    collection_name = dbname["users"]


    name_user = str(input("Type your name: "))
    age_user = str(input("Type your age: "))
    birth_user = str(input("Type your birth e.g(10/25/1998): "))
    code_user = str(input("Type your code e.g(Yours mother name, anything really): "))

    user_data = {
        "name": name_user,
        "age": age_user,
        "birth": birth_user,
        "code": code_user
    }

    collection_name.insert_one(user_data)

    query_user = collection_name.find({"code": {"$regex": f"{code_user}"}})
    query_df = DataFrame(query_user)

    print("User created with success! Here's your information!")
    print(query_df)




