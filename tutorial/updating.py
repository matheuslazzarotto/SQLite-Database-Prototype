import sqlite3

#connect to database
conn = sqlite3.connect('customer.db')

#create a cursor
c = conn.cursor()

#update record
c.execute("""
            
            UPDATE customers set first_name = 'John'
            WHERE rowid = 1
            
          """)

conn.commit()

c.execute("SELECT rowid, * FROM customers")

items = c.fetchall()

for item in items:
    print(item)