from time import sleep
from modules.pymongo_database import get_database
from modules.pymongo_create_user import create_user
from modules.pymongo_query import query_by_name, query_all
from modules.pymongo_delete import delete_all_data_in_collection, delete_user_by_id
from modules.pymongo_update import update_one_user

dbname = get_database()

collection_name = dbname["users"]



while True:
    sleep(1)
    choice = input("""
    ███████████  █████ █████ ██████   ██████    ███████    ██████   █████   █████████     ███████   
    ░███░░░░░███░░███ ░░███ ░░██████ ██████   ███░░░░░███ ░░██████ ░░███   ███░░░░░███  ███░░░░░███ 
    ░███    ░███ ░░███ ███   ░███░█████░███  ███     ░░███ ░███░███ ░███  ███     ░░░  ███     ░░███
    ░██████████   ░░█████    ░███░░███ ░███ ░███      ░███ ░███░░███░███ ░███         ░███      ░███
    ░███░░░░░░     ░░███     ░███ ░░░  ░███ ░███      ░███ ░███ ░░██████ ░███    █████░███      ░███
    ░███            ░███     ░███      ░███ ░░███     ███  ░███  ░░█████ ░░███  ░░███ ░░███     ███ 
    █████           █████    █████     █████ ░░░███████░   █████  ░░█████ ░░█████████  ░░░███████░  
    ░░░░░           ░░░░░    ░░░░░     ░░░░░    ░░░░░░░    ░░░░░    ░░░░░   ░░░░░░░░░     ░░░░░░░    
                                                                                                    
                                                                                                    
                                                                                                    
    ███████████  ███████████      ███████          █████ ██████████   █████████  ███████████        
   ░░███░░░░░███░░███░░░░░███   ███░░░░░███       ░░███ ░░███░░░░░█  ███░░░░░███░█░░░███░░░█        
    ░███    ░███ ░███    ░███  ███     ░░███       ░███  ░███  █ ░  ███     ░░░ ░   ░███  ░         
    ░██████████  ░██████████  ░███      ░███       ░███  ░██████   ░███             ░███            
    ░███░░░░░░   ░███░░░░░███ ░███      ░███       ░███  ░███░░█   ░███             ░███            
    ░███         ░███    ░███ ░░███     ███  ███   ░███  ░███ ░   █░░███     ███    ░███            
    █████        █████   █████ ░░░███████░  ░░████████   ██████████ ░░█████████     █████           
    ░░░░░        ░░░░░   ░░░░░    ░░░░░░░     ░░░░░░░░   ░░░░░░░░░░   ░░░░░░░░░     ░░░░░            

    [1] Insert Data
    [2] Query Users
    [3] Query by Name
    [4] Update User by _id
    [5] Delete User by _id
    [6] Delete All Data in Collection
    [0] Exit
    -> """)                                                                                              

    if choice == "1":
        create_user()
        sleep(1)


    if choice == "2":
        query_all()
        sleep(1)
        
    if choice == "3":
        name_to_be_found = str(input("Type the name: "))
        query_by_name(name_to_be_found)
        sleep(1)

    if choice == "4":
        id_to_be_updated = str(input("Type the ID: "))
        name_to_be_updated = str(input("Type the new name: "))
        code_to_be_updated = str(input("Type the new code: "))
        update_one_user(id_to_be_updated, name_to_be_updated, code_to_be_updated)

    if choice == "5":
        id_to_be_deleted = str(input("Type the ID: "))
        delete_user_by_id(id_to_be_deleted)

    if choice == "6":
        delete_all_data_in_collection()

    if choice == "0":
        break                                                                                      


