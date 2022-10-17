from modules.pymongo_database import get_database

dbname = get_database()

collection_name = dbname["users"]

category_index_name = collection_name.create_index("name")
category_index_code = collection_name.create_index("code")
