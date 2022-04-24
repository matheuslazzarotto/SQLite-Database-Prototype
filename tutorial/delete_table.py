import sqlite3

#connect to database
conn = sqlite3.connect('customer.db')

#create a cursor
c = conn.cursor()

#deleting table
c.execute("DROP TABLE customers")

conn.commit()

c.execute("SELECT rowid, * FROM customers")

items = c.fetchall()

for item in items:
    print(item)