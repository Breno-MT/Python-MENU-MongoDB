from time import sleep
from pandas import DataFrame
from modules.pymongo_database import get_database
from modules.pymongo_create_user import create_user
from modules.pymongo_query import query_by_name, query_all

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
        print("To be created.")

    if choice == "5":
        print("To be created.")

    if choice == "0":
        break                                                                                      


