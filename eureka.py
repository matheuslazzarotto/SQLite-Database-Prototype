import functions
import sqlite3

while(True):
    print(" ")
    print("Welcome to the database. Your options are:")
    print("1 - Show the database's current slopes;")
    print("2 - Add an slope to the database;")
    print("3 - Delete a slope from the database;")
    print("4 - Fetch one slope from the database;")
    print("5 - Fetch a variable from one slope from the databse")
    print("0 - End program.")
    print()
    value = float(input("Please choose an option: "))
    
    if value == 1:
        functions.show_all()
        continue

    elif value == 2:
        slope_name= input("please insert the name of the slope: ")
        slope_lat= input("please insert the slope latitude: ")
        slope_long= input("please insert the slope longitude: ")
        declivity= input("please insert the slope's declivity: ")
        houses_per_square_meter= input("please insert the number of houses per square meter: ")
        trees_per_square_meter= input("please insert the number of trees per square meter: ")
        liquid_proximity= input("please insert the proximity to liquid surfaces: ")
        soil_umidity= input("please insert the coeficient for soil humidity: ")

        functions.add_one(slope_name,slope_lat,slope_long,declivity,houses_per_square_meter,
        trees_per_square_meter,liquid_proximity,soil_umidity)

        continue

    elif value == 3:
        id = str(input("insert the id of the object you'd like to delete: "))
        functions.delete_one(id)
        continue
    
    elif value == 4:
        id = str(input("insert the id of the object you'd like to fetch: "))
        functions.general_fetch(id)
        continue

    elif value == 5:
        id = (input("\ninsert the slope ID of the object you'd like to fetch: "))
        print("\n\ninsert below the specific value you'd like to fetch.\n\noptions: \n\n1 - slope name;")
        print("2 - slope latitude;\n3 - slope longitude;\n4 - declivity;\n5 - houses per square meter;")
        print("6 - trees per square meter,\n7 - liquid proximity,\n8 - soil umidity.")

        op = int(input("insert here: "))
        functions.specific_fetch(id,op)
        continue
    
    break