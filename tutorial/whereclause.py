import sqlite3

#connect to database
conn = sqlite3.connect('customer.db')

#create a cursor
c = conn.cursor()

#query the database
c.execute("SELECT rowid, * FROM customers WHERE last_name = 'Elder'")
#c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'BR%'")
#c.execute("SELECT rowid, * FROM customers WHERE email LIKE '%codemy.com'")
#c.execute("SELECT rowid, * FROM customers WHERE age > 21")


items = c.fetchall()

for item in items:
    print(item)