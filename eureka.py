import functions
import sqlite3

while(True):
    print(" ")
    print("Welcome to the database. Your options are:")
    print("1 - Show the database's current contents;")
    print("2 - Add an object to the database;")
    print("3 - Delete an object from the database;")
    print("4 - Fetch one object from the database;")
    print("5 - End program.")
    print()
    value = float(input("Please choose an option: "))
    
    if value == 1:
        functions.show_all()
        continue

    elif value == 2:
        functions.add_one(slope_name,slope_lat,slope_long,declivity,houses_per_square_meter,
        trees_per_square_meter,liquid_proximity,soil_umidity)

        continue

    elif value == 3:
        id = str(input("insert the id of the object you'd like to delete: "))
        functions.delete_one(id)
        continue
    
    elif value == 4:
        id = str(input("insert the id of the object you'd like to fetch: "))
        functions.fetch_one(id)
        continue
    break
