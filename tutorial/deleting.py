import sqlite3

#connect to database
conn = sqlite3.connect('customer.db')

#create a cursor
c = conn.cursor()

#deleting a record
c.execute("DELETE from customers WHERE rowid = 6")

conn.commit()

c.execute("SELECT rowid, * FROM customers")

items = c.fetchall()

for item in items:
    print(item)