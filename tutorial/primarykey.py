import sqlite3

#connect to database
conn = sqlite3.connect('customer.db')

#create a cursor
c = conn.cursor()

#query the database
c.execute("SELECT rowid, * FROM customers")

items = c.fetchall()

for item in items:
    print(item)