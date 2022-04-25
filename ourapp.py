import database
import sqlite3

print("Welcome to the database. Your options are:")
print("1 - Show the database's current contents;")
print("2 - Add an object to the database;")
print("3 - Delete an object from the database;")

value = float(input("Please choose an option: "))
if value == 1:
    database.show_all()
if value == 2:
    first_name = input("please insert the first name: ")
    last_name = input("please insert the last name: ")
    email = input("please insert the email: ")
    database.add_one(first_name,last_name,email)

if value == 3:
    id = str(input("insert the id you'd like to delete:"))
    database.delete_one(id)

#show db
#database.show_all()

#add a record to the db
#database.add_one("Laura","Smith","laura@smith.com")

#delete record (use row id as string in the '()')
#database.delete_one()

#add more than one record to the list
# stuff = [
#     ('Brenda', 'Seinfield', 'brenda@smitherton.com'),
#     ('Tony', 'Soprano', 'tony@soprano.com')
#     ]
# database.add_many(stuff)
